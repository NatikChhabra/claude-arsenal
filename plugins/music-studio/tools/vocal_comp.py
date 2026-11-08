#!/usr/bin/env python3
"""vocal_comp.py: real double-tracking and gentle note nudges from the singer's OWN takes. No AI, no voice models.
Used by vocal-route (Route D and F: a voice that is not a trained singer) and mix-master (doubles, light tuning).

    uv run --with librosa --with soundfile --with praat-parselmouth python vocal_comp.py double <lead.wav> <other.wav> <out.wav>
    uv run --with librosa --with soundfile --with praat-parselmouth python vocal_comp.py nudge <line.wav> <out.wav> --chord A:C#:E [--cap 1.0]
    uv run --with librosa --with soundfile --with praat-parselmouth python vocal_comp.py --selftest

double  Lines up another performance of the same line (another take, or the same lyric from another chorus) with the
        lead, syllable by syllable: DTW on MFCCs maps the two, then Praat's PSOLA duration tier stretches the other take
        locally. Prints the onset correlation before and after (0 = unrelated, 1 = identical timing). Use a double only
        at 0.3 or more; two doubles panned about 60% left and right, 7-8 dB under the lead, thicken a plain voice and
        hide small pitch wobbles. Measured on a real untrained voice: 0.2 (plain stretch) -> 0.5-0.85 (aligned).
nudge   Moves each sustained note (a voiced run of 120 ms or more) toward the nearest tone of the chord under it,
        only if it is 0.3 semitone or more off, by at most --cap semitones, keeping the singer's own slides and
        vibrato (the whole note shifts, its shape stays). PSOLA via Praat. This is the opposite of hard auto-tune:
        never use it on a melody-less chant or spoken lines (vocal-route Route F: that is what sounds robotic).
--chord  pitch classes as note names, colon separated (A:C#:E); notes off the chord go to the nearest of them within
        1.5 semitones, else stay.
Read-only on inputs. Exit 0, or 1 on a failed selftest.
"""
import sys

SR = 48000
NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLATS = {"DB": "C#", "EB": "D#", "GB": "F#", "AB": "G#", "BB": "A#"}


def pc(name):
    n = name.strip().upper()
    n = FLATS.get(n, n)
    return NAMES.index(n)


def _feats(x, sr):
    import numpy as np, librosa
    y = librosa.resample(x, orig_sr=sr, target_sr=16000)
    m = librosa.feature.mfcc(y=y, sr=16000, n_mfcc=20, hop_length=160, n_fft=512)[1:]
    return (m - m.mean(1, keepdims=True)) / (m.std(1, keepdims=True) + 1e-6)


def onset_corr(a, b, sr=SR):
    import numpy as np, librosa
    ea = librosa.onset.onset_strength(y=librosa.resample(a, orig_sr=sr, target_sr=16000), sr=16000, hop_length=160)
    eb = librosa.onset.onset_strength(y=librosa.resample(b, orig_sr=sr, target_sr=16000), sr=16000, hop_length=160)
    n = min(len(ea), len(eb))
    ea, eb = ea[:n] - ea[:n].mean(), eb[:n] - eb[:n].mean()
    return float(np.dot(ea, eb) / np.sqrt(np.dot(ea, ea) * np.dot(eb, eb) + 1e-9))


def double(lead, other, sr=SR, smooth=7):
    """Time-warp `other` so its syllables land with `lead`. Returns an array as long as lead."""
    import numpy as np, librosa, parselmouth
    from parselmouth.praat import call
    from scipy.ndimage import uniform_filter1d
    a, b = _feats(lead, sr), _feats(other, sr)
    _, wp = librosa.sequence.dtw(X=a, Y=b, metric="cosine", global_constraints=True, band_rad=0.25)
    wp = wp[::-1]
    n = a.shape[1]
    mj, cnt = np.zeros(n), np.zeros(n)
    for i, j in wp:
        mj[i] += j
        cnt[i] += 1
    mj = np.maximum.accumulate(uniform_filter1d(mj / np.maximum(cnt, 1), smooth, mode="nearest"))
    idx = np.arange(0, n, 5)
    fac = np.clip(np.diff(idx) * 0.01 / np.maximum(np.diff(mj[idx]) * 0.01, 0.003), 0.5, 2.0)
    snd = parselmouth.Sound(other.astype(np.float64), sr)
    man = call(snd, "To Manipulation", 0.01, 60, 400)
    dur = call("Create DurationTier", "d", 0, snd.duration)
    for k in range(len(fac)):
        t = (mj[idx[k]] + mj[idx[k + 1]]) / 2 * 0.01
        call(dur, "Add point", min(max(t, 0.001), snd.duration - 0.001), float(fac[k]))
    call([man, dur], "Replace duration tier")
    y = call(man, "Get resynthesis (overlap-add)").values[0]
    y = np.pad(y, (0, max(0, len(lead) - len(y))))
    return y[:len(lead)]


def nudge(x, chord_pcs, sr=SR, minrun=0.12, thr=0.3, cap=1.0):
    """Shift sustained notes toward the nearest chord tone. Returns (audio, [(time_s, shift_semitones)])."""
    import numpy as np, parselmouth
    from parselmouth.praat import call
    snd = parselmouth.Sound(x.astype(np.float64), sr)
    pitch = snd.to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=600)
    f, ts = pitch.selected_array["frequency"], pitch.xs()
    v = f > 0
    m = np.where(v, 69 + 12 * np.log2(np.where(v, f, 1) / 440), 0)
    shifts, log = np.zeros(len(f)), []
    i, n = 0, len(f)
    while i < n:
        if not v[i]:
            i += 1
            continue
        j = i
        while j < n and v[j] and abs(m[j] - m[max(i, j - 1)]) < 1.2:
            j += 1
        j = max(j, i + 1)
        if (j - i) * 0.01 >= minrun:
            med = float(np.median(m[i:j]))
            near = [k for k in range(int(med) - 2, int(med) + 3) if k % 12 in chord_pcs and abs(k - med) <= 1.5]
            if near:
                tg = min(near, key=lambda k: abs(k - med))
                if abs(tg - med) >= thr:
                    shifts[i:j] = np.clip(tg - med, -cap, cap)
                    log.append((round(float(ts[i]), 2), round(float(shifts[i]), 2)))
        i = j
    if not log:
        return x.copy(), log
    man = call(snd, "To Manipulation", 0.01, 70, 600)
    pt = call(man, "Extract pitch tier")
    call(pt, "Remove points between", 0, snd.duration)
    for k in range(n):
        if v[k]:
            call(pt, "Add point", ts[k], float(f[k] * 2 ** (shifts[k] / 12)))
    call([man, pt], "Replace pitch tier")
    y = call(man, "Get resynthesis (overlap-add)").values[0]
    y = np.pad(y, (0, max(0, len(x) - len(y))))
    return y[:len(x)], log


def _read(p):
    import soundfile as sf, librosa
    y, sr = sf.read(p)
    y = y.mean(1) if y.ndim > 1 else y
    return (librosa.resample(y, orig_sr=sr, target_sr=SR) if sr != SR else y)


def _voice(notes, sr=SR, seed=0):
    """A crude voiced test signal: (midi, seconds) notes with a small vibrato and gaps between syllables."""
    import numpy as np
    rng = np.random.default_rng(seed)
    out = []
    for midi, d in notes:
        t = np.arange(int(d * sr)) / sr
        f = 440 * 2 ** ((midi - 69) / 12) * (1 + 0.004 * np.sin(2 * np.pi * 5.5 * t))
        ph = 2 * np.pi * np.cumsum(f) / sr
        s = sum(np.sin(k * ph) / k for k in range(1, 12)) * np.minimum(1, t / 0.02) * np.minimum(1, (d - t) / 0.03)
        out += [s * 0.2, rng.normal(0, 0.002, int(0.08 * sr))]
    return np.concatenate(out)


def selftest():
    import numpy as np
    ok = True
    lead = _voice([(57, .30), (59, .18), (57, .42), (55, .22), (57, .50)])
    other = _voice([(57, .24), (59, .26), (57, .33), (55, .30), (57, .40)], seed=1)
    before = onset_corr(lead, np.pad(other, (0, max(0, len(lead) - len(other))))[:len(lead)])
    after = onset_corr(lead, double(lead, other))
    ok &= after > before + 0.15 and after > 0.4
    sharp = _voice([(57.45, 0.6)])                                 # A3 sung 45 cents sharp
    y, log = nudge(sharp, {pc("A"), pc("C#"), pc("E")})
    import parselmouth
    f = parselmouth.Sound(y, SR).to_pitch_ac(time_step=0.01, pitch_floor=70, pitch_ceiling=600).selected_array["frequency"]
    f = f[f > 0]
    got = 69 + 12 * np.log2(np.median(f) / 440)
    ok &= len(log) == 1 and abs(got - 57) < 0.15
    _, log2 = nudge(_voice([(57.1, 0.6)]), {pc("A")})            # 10 cents off: left alone
    ok &= log2 == []
    print(f"vocal_comp selftest: {'PASS' if ok else 'FAIL'} (double {before:.2f}->{after:.2f}, nudge -> {got:.2f})")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    import soundfile as sf
    if len(argv) >= 4 and argv[0] == "double":
        lead, other = _read(argv[1]), _read(argv[2])
        w = double(lead, other)
        pad = other[:len(lead)] if len(other) >= len(lead) else __import__("numpy").pad(other, (0, len(lead) - len(other)))
        print(f"onset correlation {onset_corr(lead, pad):.2f} -> {onset_corr(lead, w):.2f}"
              + ("" if onset_corr(lead, w) >= 0.3 else "  (under 0.3: don't use this double)"))
        sf.write(argv[3], w, SR)
        return 0
    if len(argv) >= 3 and argv[0] == "nudge" and "--chord" in argv:
        chord = {pc(n) for n in argv[argv.index("--chord") + 1].split(":")}
        cap = float(argv[argv.index("--cap") + 1]) if "--cap" in argv else 1.0
        y, log = nudge(_read(argv[1]), chord, cap=cap)
        print("nudged notes (time s, semitones):", log or "none")
        sf.write(argv[2], y, SR)
        return 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
