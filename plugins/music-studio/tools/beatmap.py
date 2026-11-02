#!/usr/bin/env python3
"""beatmap.py: the music map of a song (tempo, beats, downbeats, bars, sections, energy) and a check that an edit's
cuts land on it. Used by guitar-capture (a take's tempo grid), produce-arrange (section map) and music-video (cuts).

    uv run --with librosa --with soundfile python beatmap.py map <audio> [--out map.json] [--bpm LO HI] [--click click.wav]
    uv run --with librosa --with soundfile python beatmap.py cuts <map.json> <cuts.txt|edl.json> [--fps 30] [--every 1]
    uv run --with librosa --with soundfile python beatmap.py --selftest

map   tempo (with a half/double octave check inside --bpm, default 70-180), beat times, downbeats (the beat phase whose
      onsets are strongest, every 4 beats; listen to --click before trusting it), bars, section boundaries (chroma +
      MFCC novelty, snapped to the nearest downbeat) and a 1 s RMS energy curve. --click writes the song at -6 dB with
      a high click on downbeats and a low click on other beats: the listen-check that the grid sits on the kick.
cuts  reads cut times in seconds (a text file, one per line, or a JSON list / {"cuts": [...]} / an EDL whose pieces
      carry "start" output times) and reports each cut's distance to the nearest beat (or every Nth beat with
      --every 2 / 4). On grid = within one frame at --fps. Prints the share on grid and the worst offenders.
      House bar for a music video: >= 90% of cuts on grid outside marked off-beat moments (references/music-video.md).
Read-only on every input. Exit 0 PASS, 1 below the bar (cuts) or a failed selftest.
"""
import json, os, sys


def load(path, sr=22050):
    import librosa
    y, sr = librosa.load(path, sr=sr, mono=True)
    return y, sr


def tempo_octave(bpm, lo, hi):
    while bpm < lo:
        bpm *= 2
    while bpm > hi:
        bpm /= 2
    return bpm


def analyse(path, lo=70, hi=180):
    import numpy as np, librosa
    y, sr = load(path)
    hop = 128   # 5.8 ms frames: beat times precise to a few ms, not the 23 ms of librosa's default hop
    onset = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, hop_length=hop, units="frames", tightness=100)
    tempo = float(np.atleast_1d(tempo)[0])
    t = tempo_octave(tempo, lo, hi)
    if abs(t - tempo) > 1:   # re-track at the corrected octave
        tempo, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, hop_length=hop, units="frames", bpm=t,
                                               tightness=100)
        tempo = float(np.atleast_1d(tempo)[0])
    beat_t = librosa.frames_to_time(beats, sr=sr, hop_length=hop)
    if len(beat_t) > 4:   # the tempo the beats actually keep (least squares over beat index), not a quantised estimate
        tempo = 60.0 / float(np.polyfit(np.arange(len(beat_t)), beat_t, 1)[0])
    strength = onset[beats] if len(beats) else np.array([])
    phase, conf = 0, 0.0
    if len(beats) >= 8:
        means = [float(strength[p::4].mean()) for p in range(4)]
        phase = int(np.argmax(means))
        srt = sorted(means)
        conf = round((srt[-1] - srt[-2]) / (srt[-1] + 1e-9), 3)
    downs = beat_t[phase::4]
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)   # default hop for structure: sections need no ms precision
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    feat = np.vstack([librosa.util.normalize(chroma, axis=1), librosa.util.normalize(mfcc, axis=1)])
    k = max(2, min(12, int(len(y) / sr / 20)))
    bounds = librosa.segment.agglomerative(feat, k)
    sec_t = librosa.frames_to_time(bounds, sr=sr)
    snap = lambda x: float(min(downs, key=lambda d: abs(d - x))) if len(downs) else float(x)
    sections = sorted({round(snap(x), 3) for x in sec_t})
    rms = librosa.feature.rms(y=y)[0]
    hop_t = librosa.frames_to_time(np.arange(len(rms)), sr=sr)
    energy = [round(float(rms[(hop_t >= s) & (hop_t < s + 1)].mean() if ((hop_t >= s) & (hop_t < s + 1)).any() else 0), 4)
              for s in range(int(len(y) / sr))]
    return {"file": os.path.basename(path), "duration": round(len(y) / sr, 3), "tempo": round(tempo, 2),
            "beats": [round(float(b), 3) for b in beat_t], "downbeats": [round(float(d), 3) for d in downs],
            "downbeat_confidence": conf, "sections": sections, "energy_1s": energy}


def click(path, m, out):
    import numpy as np, librosa, soundfile as sf
    y, sr = load(path, 44100)
    y = y * 0.5
    def tick(f):
        n = int(0.03 * sr)
        return 0.6 * np.sin(2 * np.pi * f * np.arange(n) / sr) * np.exp(-np.arange(n) / (0.006 * sr))
    downs = set(m["downbeats"])
    for b in m["beats"]:
        i = int(b * sr)
        s = tick(1600 if b in downs else 1000)
        y[i:i + len(s)] += s[:max(0, len(y) - i)]
    sf.write(out, y, sr)


def read_cuts(path):
    text = open(path, encoding="utf-8").read().strip()
    if path.endswith(".json"):
        d = json.loads(text)
        if isinstance(d, dict) and "cuts" in d:
            return [float(x) for x in d["cuts"]]
        if isinstance(d, dict) and "pieces" in d:
            return [float(p["start"]) for p in d["pieces"] if "start" in p][1:]
        return [float(x) for x in d]
    return [float(l.split()[0]) for l in text.splitlines() if l.strip() and not l.startswith("#")]


def check_cuts(m, cuts, fps=30.0, every=1):
    grid = m["beats"][::every] if every > 1 else m["beats"]
    if every == 4:
        grid = m["downbeats"]
    frame = 1.0 / fps
    rows = []
    for c in cuts:
        d = min(grid, key=lambda g: abs(g - c)) if grid else c
        rows.append((round(c - d, 3), c))
    on = [r for r in rows if abs(r[0]) <= frame + 1e-6]
    share = len(on) / len(rows) if rows else 1.0
    worst = sorted(rows, key=lambda r: -abs(r[0]))[:8]
    return share, worst


def selftest():
    import numpy as np, soundfile as sf, tempfile
    sr, bpm, dur = 22050, 120.0, 24.0
    y = np.zeros(int(sr * dur), dtype=np.float32)
    for i in range(int(dur * bpm / 60)):
        t = i * 60 / bpm
        n = int(0.05 * sr)
        amp = 1.0 if i % 4 == 0 else 0.45
        env = np.exp(-np.arange(n) / (0.01 * sr))
        burst = (np.random.default_rng(i).standard_normal(n) * env * amp).astype(np.float32)
        a = int(t * sr)
        y[a:a + n] += burst[:len(y) - a]
    d = tempfile.mkdtemp()
    p = os.path.join(d, "clicks.wav")
    sf.write(p, y, sr)
    m = analyse(p)
    ok = abs(m["tempo"] - bpm) < 2
    true_beats = [i * 0.5 for i in range(48)]
    errs = [min(abs(b - t) for t in true_beats) for b in m["beats"]]
    ok &= len(errs) > 30 and sorted(errs)[len(errs) // 2] < 0.03
    ok &= all(min(abs(x - k * 2.0) for k in range(13)) < 0.06 for x in m["downbeats"][1:-1])
    share, _ = check_cuts(m, [0.5 * k for k in range(4, 40, 2)], fps=30)
    share_bad, _ = check_cuts(m, [0.5 * k + 0.2 for k in range(4, 40, 2)], fps=30)
    ok &= share >= 0.9 and share_bad <= 0.1
    print(f"selftest {'PASS' if ok else 'FAIL'}: tempo {m['tempo']}, median beat error {sorted(errs)[len(errs)//2]*1000:.1f} ms, "
          f"downbeat conf {m['downbeat_confidence']}, cuts on grid {share:.0%} vs off-grid set {share_bad:.0%}")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if len(argv) < 2:
        print(__doc__)
        return 2
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    if argv[0] == "map":
        lo, hi = (float(argv[argv.index("--bpm") + 1]), float(argv[argv.index("--bpm") + 2])) if "--bpm" in argv else (70, 180)
        m = analyse(argv[1], lo, hi)
        out = opt("--out", os.path.splitext(argv[1])[0] + ".beatmap.json")
        json.dump(m, open(out, "w"), indent=1)
        if opt("--click"):
            click(argv[1], m, opt("--click"))
        print(f"{m['file']}: {m['tempo']} BPM, {len(m['beats'])} beats, {len(m['downbeats'])} bars, downbeat confidence "
              f"{m['downbeat_confidence']} (< 0.05: listen to --click before trusting bar lines), sections at {m['sections']} -> {out}")
        return 0
    if argv[0] == "cuts":
        m = json.load(open(argv[1]))
        share, worst = check_cuts(m, read_cuts(argv[2]), float(opt("--fps", 30)), int(opt("--every", 1)))
        print(f"cuts on grid: {share:.0%}  (bar >= 90%)")
        for off, c in worst:
            print(f"  cut {c:8.3f} s  off by {off*1000:+.0f} ms")
        return 0 if share >= 0.9 else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
