#!/usr/bin/env python3
"""voice_range.py: measure a real voice from a recording and fit a song's melody to it (key, capo), plus a clipping check.
Used by vocal-route Route F (the owner's own natural voice) and song-from-idea (range before the melody is final).

    uv run --with librosa --with soundfile python voice_range.py <voice.wav> [--mode speech|sung] [--melody A2 C4] [--json]
    uv run --with librosa --with soundfile python voice_range.py --selftest

Measures pitch with pYIN (60-1000 Hz) on voiced frames only and prints the median, the middle 80% (10th-90th
percentile) and the extremes as note names, the voiced share, and the share of samples at full scale (clipping: a take
with clipped peaks cannot be mixed clean, re-record it with lower input gain).

Comfortable range:
  --mode sung    (a sung take, best: a slow scale or the chorus hummed) the 10th-90th percentile of the take.
  --mode speech  (any spoken take, e.g. an old voice-over) an ESTIMATE: 2 semitones under the 10th percentile up to an
                 octave over the median. INFERRED from the usual gap between speaking pitch and an untrained
                 singer's easy top; replace it with a sung measurement before the guide is recorded.
--melody LOW HIGH  the song's melody range as written (e.g. A2 C4). Prints the shift in semitones that puts the
                 highest note 1-2 semitones under the top of the comfortable range (vocal-route §2), and the capo
                 (shift up 1-7), or for a shift down of 1-5 the open shapes a fourth lower with a capo (Am at capo 0 = Em
                 shapes at capo 5, so down 3 = Em shapes at capo 2): one shape set covers every key from E to A.
Read-only on the input. Exit 0, or 1 on a failed selftest.
"""
import json, math, sys

NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def hz_to_midi(hz):
    return 69 + 12 * math.log2(hz / 440.0)


def midi_to_name(m):
    m = int(round(m))
    return f"{NAMES[m % 12]}{m // 12 - 1}"


def name_to_midi(name):
    name = name.strip().upper().replace("B#", "C").replace("E#", "F")
    flats = {"DB": "C#", "EB": "D#", "GB": "F#", "AB": "G#", "BB": "A#"}
    for f, s in flats.items():
        if name.startswith(f):
            name = s + name[2:]
    note = name[:2] if len(name) > 2 and name[1] == "#" else name[:1]
    octave = int(name[len(note):])
    return NAMES.index(note) + 12 * (octave + 1)


def measure(path):
    import numpy as np, librosa
    y, sr = librosa.load(path, sr=16000, mono=True)
    raw, _ = librosa.load(path, sr=None, mono=False)
    clip = float(np.mean(np.abs(raw) >= 0.999))
    f0, voiced, _ = librosa.pyin(y, fmin=60, fmax=1000, sr=sr, frame_length=2048)
    f0 = f0[voiced & ~np.isnan(f0)]
    if len(f0) < 20:
        return {"error": "too little voiced audio to measure", "clipping_share": clip}
    midi = np.array([hz_to_midi(h) for h in f0])
    p = np.percentile(midi, [1, 10, 50, 90, 99])
    return {"voiced_share": float(np.mean(voiced)), "clipping_share": clip, "median_hz": float(np.median(f0)),
            "p1": float(p[0]), "p10": float(p[1]), "median": float(p[2]), "p90": float(p[3]), "p99": float(p[4])}


def comfortable(m, mode):
    if mode == "sung":
        return m["p10"], m["p90"]
    return m["p10"] - 2, m["median"] + 12


def fit(lo_c, hi_c, mel_lo, mel_hi):
    shift = int(math.floor(hi_c - 2 - mel_hi))  # the top note lands about 2 semitones under the top of the range
    fits = (mel_hi - mel_lo) <= (hi_c - lo_c)
    if mel_lo + shift < lo_c and fits:          # the low end falls out: move up just enough
        shift = int(math.ceil(lo_c - mel_lo))
    if shift > 0:
        guitar = f"capo {shift}" if shift <= 7 else f"up {shift} semitones (past capo 7: change key)"
    elif shift < 0:
        d = -shift
        guitar = (f"down {d}: play the shapes a fourth lower (Am->Em, C->G, A->E) with capo {5 - d}" if d < 5 else
                  "down 5: the shapes a fourth lower (Am->Em), no capo" if d == 5 else
                  f"down {d} semitones: a lower key")
    else:
        guitar = "as written, no capo"
    return {"shift": shift, "fits": fits, "guitar": guitar,
            "melody_after": [midi_to_name(mel_lo + shift), midi_to_name(mel_hi + shift)]}


def report(m, mode, melody):
    if "error" in m:
        return m["error"]
    lo_c, hi_c = comfortable(m, mode)
    lines = [
        f"voiced {m['voiced_share']:.0%} of frames | median {m['median_hz']:.0f} Hz ({midi_to_name(m['median'])})",
        f"middle 80%: {midi_to_name(m['p10'])} to {midi_to_name(m['p90'])} | extremes: {midi_to_name(m['p1'])} to "
        f"{midi_to_name(m['p99'])}",
        f"comfortable sung range ({'measured' if mode == 'sung' else 'ESTIMATE from speech'}): "
        f"{midi_to_name(lo_c)} to {midi_to_name(hi_c)}",
        f"clipping: {m['clipping_share']:.3%} of samples at full scale"
        + ("  FIX: lower the input gain and re-record" if m["clipping_share"] > 0.0001 else "  OK"),
    ]
    if melody:
        f = fit(lo_c, hi_c, name_to_midi(melody[0]), name_to_midi(melody[1]))
        lines.append(f"melody {melody[0]}-{melody[1]}: shift {f['shift']:+d} -> {f['melody_after'][0]}-"
                     f"{f['melody_after'][1]}; guitar: {f['guitar']}"
                     + ("" if f["fits"] else "  WARN: the melody is wider than the range, narrow it"))
    return "\n".join(lines)


def selftest():
    import numpy as np, soundfile as sf, tempfile, os
    ok = True
    for n in ("A2", "C4", "F#3", "Bb2"):
        ok &= midi_to_name(name_to_midi(n)) == n.replace("Bb", "A#")
    sr = 16000
    t = np.arange(int(sr * 3)) / sr
    glide = 0.4 * np.sin(2 * np.pi * np.cumsum(np.linspace(110, 220, len(t))) / sr)   # A2 up to A3
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "glide.wav")
        sf.write(p, glide, sr)
        m = measure(p)
    ok &= abs(m["median"] - name_to_midi("E3")) <= 1.5          # geometric middle of a linear Hz glide ~ E3/F3
    ok &= name_to_midi("A2") - 1 <= m["p1"] and m["p99"] <= name_to_midi("A3") + 1
    ok &= m["clipping_share"] == 0.0
    f = fit(name_to_midi("G2"), name_to_midi("D4"), name_to_midi("A2"), name_to_midi("C4"))
    ok &= f["shift"] == 0 and f["guitar"] == "as written, no capo"
    f = fit(name_to_midi("A2"), name_to_midi("F4"), name_to_midi("A2"), name_to_midi("C4"))
    ok &= f["shift"] == 3 and f["guitar"] == "capo 3"
    f = fit(name_to_midi("F2"), name_to_midi("B3"), name_to_midi("A2"), name_to_midi("C4"))
    ok &= f["shift"] == -3 and "capo 2" in f["guitar"]
    print("voice_range selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 1
    mode = argv[argv.index("--mode") + 1] if "--mode" in argv else "speech"
    melody = argv[argv.index("--melody") + 1: argv.index("--melody") + 3] if "--melody" in argv else None
    m = measure(argv[0])
    if "--json" in argv:
        out = dict(m)
        if "error" not in m:
            lo_c, hi_c = comfortable(m, mode)
            out["comfortable"] = [midi_to_name(lo_c), midi_to_name(hi_c)]
            if melody:
                out["fit"] = fit(lo_c, hi_c, name_to_midi(melody[0]), name_to_midi(melody[1]))
        print(json.dumps(out, indent=2))
    else:
        print(report(m, mode, melody))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
