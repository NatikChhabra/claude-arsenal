#!/usr/bin/env python3
"""guitar_level.py: measure a player's level from a short recording of songs he already plays, before writing parts.

    uv run --with librosa --with soundfile python guitar_level.py <take.wav> [--from S --to S]
    uv run --with librosa --with soundfile python guitar_level.py --selftest

Prints, for the whole take and for each stretch of continuous playing (split at gaps of 0.6 s or more):
  tuning     how far the guitar sits from A440, in cents (tell him to tune if more than 10 cents off)
  clipped    samples at full scale (more than 0: the mic is too close or the gain too high)
  notes/s    onsets per second while playing (his comfortable speed)
  steady     beat-to-beat spread as a % of the beat (under 5% is steady for a home player, over 8% is shaky)
  tonal      harmonic minus percussive energy in dB (positive: picked notes; negative: strums, chucks, slaps)
  range      5th to 95th percentile pitch of the picked notes
  gaps       pauses inside the take (hesitations show where chord changes or a passage are still hard)
Use: write parts at about 60-70% of his best clean notes/s, keep a part's hardest change inside what his steadiest
stretch shows, and ask him, rather than guess, about anything the numbers can't show (barre chords, harmonics, slaps).
Read-only on the input. Exit 0, or 1 on a failed selftest.
"""
import sys

SR = 22050


def _load(path, a=None, b=None):
    import numpy as np, soundfile as sf, librosa
    y, sr = sf.read(path, always_2d=True)
    clipped = int((np.abs(y) > 0.99).sum())
    ch = int(np.argmax((y ** 2).mean(0)))                     # phone and USB mics often fill one channel only
    x = y[:, ch]
    x = x[int((a or 0) * sr):int(b * sr) if b else None]
    return librosa.resample(x, orig_sr=sr, target_sr=SR), clipped


def runs(x, gap=0.6):
    """Stretches of continuous playing: [(start_s, end_s)], split at quiet gaps of `gap` seconds or more."""
    import numpy as np, librosa
    hop = SR // 20
    db = 20 * np.log10(librosa.feature.rms(y=x, hop_length=hop)[0] + 1e-9)
    loud = db > db.max() - 30
    out, i, n = [], 0, len(loud)
    while i < n:
        if not loud[i]:
            i += 1
            continue
        j = i
        while j < n and (loud[j] or (j + int(gap * 20) < n and loud[j:j + int(gap * 20)].any())):
            j += 1
        if (j - i) / 20 >= 2:
            out.append((i / 20, j / 20))
        i = j + 1
    return out


def measure(x):
    import numpy as np, librosa
    r = {}
    r["tuning_cents"] = round(float(librosa.estimate_tuning(y=x, sr=SR)) * 100)
    env = librosa.onset.onset_strength(y=x, sr=SR)
    on = librosa.onset.onset_detect(onset_envelope=env, sr=SR, units="time")
    dur = len(x) / SR
    r["notes_per_s"] = round(len(on) / dur, 2) if dur else 0
    _, beats = librosa.beat.beat_track(onset_envelope=env, sr=SR, units="time")
    bi = np.diff(beats)
    r["steady_pct"] = round(float(bi.std() / bi.mean() * 100), 1) if len(bi) > 3 else None
    h, p = librosa.effects.hpss(x)
    r["tonal_db"] = round(float(10 * np.log10((h ** 2).sum() / ((p ** 2).sum() + 1e-12) + 1e-12)), 1)
    f0, v, _ = librosa.pyin(x, fmin=70, fmax=1100, sr=SR)
    m = librosa.hz_to_midi(f0[v]) if v.any() else []
    r["range"] = (librosa.midi_to_note(np.percentile(m, 5)), librosa.midi_to_note(np.percentile(m, 95))) if len(m) else None
    return r


def report(path, a=None, b=None):
    x, clipped = _load(path, a, b)
    print(f"{path}: {len(x) / SR:.1f} s, clipped samples {clipped}" + ("  (move the mic back)" if clipped else ""))
    rr = runs(x)
    gaps = [(round(rr[k][1], 1), round(rr[k + 1][0] - rr[k][1], 1)) for k in range(len(rr) - 1)]
    print("  whole take:", measure(x))
    print("  gaps (at s, length s):", gaps or "none")
    for s, e in rr:
        print(f"  {s:5.1f}-{e:5.1f} s ({e - s:4.1f} s):", measure(x[int(s * SR):int(e * SR)]))


def _pluck(midi, d, cents=0.0):
    import numpy as np
    t = np.arange(int(d * SR)) / SR
    f = 440 * 2 ** ((midi - 69 + cents / 100) / 12)
    return sum(np.sin(2 * np.pi * k * f * t) / k for k in range(1, 6)) * np.exp(-t * 4) * 0.3


def selftest():
    import numpy as np
    ok = True
    beat = 60 / 100 / 2                                         # eighth notes at 100 BPM = 3.33 notes per second
    seq = [52, 59, 64, 59, 55, 59, 62, 59] * 4
    a = np.concatenate([_pluck(m, beat, cents=-15) for m in seq])
    x = np.concatenate([a, np.zeros(int(1.5 * SR)), a])         # two stretches with a 1.5 s hesitation
    rr = runs(x)
    r = measure(a)
    ok &= len(rr) == 2 and abs((rr[1][0] - rr[0][1]) - 1.5) < 0.4
    ok &= -25 <= r["tuning_cents"] <= -5
    ok &= 2.6 <= r["notes_per_s"] <= 4.0
    ok &= r["steady_pct"] is not None and r["steady_pct"] < 5
    ok &= r["tonal_db"] > 0
    print(f"guitar_level selftest: {'PASS' if ok else 'FAIL'} (runs {len(rr)}, {r})")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    if not argv:
        print(__doc__)
        return 1
    a = float(argv[argv.index("--from") + 1]) if "--from" in argv else None
    b = float(argv[argv.index("--to") + 1]) if "--to" in argv else None
    report(argv[0], a, b)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
