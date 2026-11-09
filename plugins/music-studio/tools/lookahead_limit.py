#!/usr/bin/env python3
"""lookahead_limit.py: a mastering limiter that only touches the loudest hits, and a report of where it worked.

    python lookahead_limit.py <in.wav> <out.wav> [--ceiling -1.2] [--target -14.5] [--look 5] [--release 150]
    python lookahead_limit.py <in.wav> --report [--ceiling -1.2] [--target -14.5]     # gain-reduction map, no output
    python lookahead_limit.py --selftest

Why it exists: a limiter built as "centred minimum filter, then smooth" pulled the gain down 60-70 ms BEFORE every
hit and held it flat, then jumped back. On a guitar-only master that showed up as pumping through the last chorus
(median gain reduction 8.8 dB there). This one:
- finds the 4x oversampled peak of each sample (true-peak safe at the ceiling),
- looks ahead only forward: the gain starts falling at most 2 x look before a peak, never earlier,
- reaches the full reduction on the peak sample (a linear ramp of `look` ms),
- releases exponentially (`release` ms), and never lets a sample over the ceiling.
With --target it trims the input gain until the output reaches that integrated loudness (ffmpeg ebur128).

Use it as the chain's last stage (it writes the master), then gate that file with loudness.py. --report alone shows
what THIS limiter would do to a premaster; it says nothing about a master made with another limiter.
Report: gain reduction per 10 s window (median, 95th percentile, max) and the "swing" (range of the 50 ms-smoothed
gain inside each 0.5 s), plus the worst windows. House bar on a master: median 0-1 dB, max about 4 dB, swing under
3 dB in the loudest section. Over that, raise the ceiling (-1.2 dBTP is safe if the encoded file is re-measured) or
lower the target by 0.5 LU before touching the mix.
Needs numpy, scipy, soundfile (ffmpeg for --target). numba speeds up the release loop if installed.
exit 0 = done / PASS, 1 = report over the house bar, 2 = error.
"""
import argparse, re, subprocess, sys, tempfile, os
import numpy as np


def _release(gr, a):
    """instant attack, exponential release, on dB of reduction"""
    try:
        from numba import njit
        f = njit(cache=False)(_release_py)
        return f(gr, a)
    except Exception:
        return _release_py(gr, a)


def _release_py(gr, a):
    o = np.empty_like(gr); v = 0.0
    for i in range(len(gr)):
        v = gr[i] if gr[i] > v else a * v + (1 - a) * gr[i]
        o[i] = v
    return o


def limit(x, sr, ceiling_db=-1.2, look_ms=5.0, release_ms=150.0):
    """x: (n,) or (n, ch) float. Returns (y, gain_reduction_db per sample)."""
    from scipy.signal import resample_poly
    from scipy.ndimage import maximum_filter1d
    x2 = x if x.ndim == 2 else x[:, None]
    n = len(x2); c = 10 ** (ceiling_db / 20)
    up = resample_poly(x2, 4, 1, axis=0)
    pk = np.abs(up).max(1)[:4 * n]
    pk = np.pad(pk, (0, 4 * n - len(pk))).reshape(-1, 4).max(1)
    need = np.maximum(0.0, 20 * np.log10(pk / c + 1e-12))           # dB each sample needs
    L = int(look_ms / 1000 * sr); L += L % 2
    fwd = maximum_filter1d(np.pad(need, (0, L)), L + 1)[L // 2:L // 2 + n]   # max over [t, t+L]
    cs = np.concatenate([[0.0], np.cumsum(np.pad(fwd, (L, 0), mode="edge"))])   # edge, not zeros: a file that starts on a hit
    ramp = (cs[L + 1:L + 1 + n] - cs[:n]) / (L + 1)                   # mean over [t-L, t]: full value on the peak
    g = _release(np.maximum(ramp, 0.0), float(np.exp(-1 / (release_ms / 1000 * sr))))
    g = np.maximum(g, need)                                          # safety: nothing over the ceiling
    y = x2 * (10 ** (-g / 20))[:, None]
    return (y if x.ndim == 2 else y[:, 0]), g


def integrated(y, sr):
    import soundfile as sf
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "m.wav"); sf.write(p, y.astype(np.float32), sr)
        r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"],
                           capture_output=True, text=True).stderr
    i = re.findall(r"I:\s+(-?(?:inf|[\d.]+)) LUFS", r); p = re.findall(r"Peak:\s+(-?(?:inf|[\d.]+)) dBFS", r)
    if not i or not p:
        raise RuntimeError("ffmpeg ebur128 gave no reading (is ffmpeg installed, is the file silent?)")
    return float(i[-1]), float(p[-1])


def to_target(x, sr, target, **kw):
    gain = 0.0
    for _ in range(6):
        y, g = limit(x * 10 ** (gain / 20), sr, **kw)
        I, tp = integrated(y, sr)
        if abs(I - target) < 0.15:
            break
        gain += target - I
    return y, g, I, tp


def true_peak_db(y):
    from scipy.signal import resample_poly
    return 20 * np.log10(np.abs(resample_poly(y, 4, 1, axis=0)).max() + 1e-12)


def report(g, sr, win=10.0, tp=None, ceiling=None):
    from scipy.ndimage import uniform_filter1d
    g50 = uniform_filter1d(g, max(1, int(0.05 * sr))); w = int(win * sr); h = int(0.5 * sr); rows = []
    for a in range(0, len(g), w):
        s = g[a:a + w]; s50 = g50[a:a + w]
        sw = [s50[i:i + h].max() - s50[i:i + h].min() for i in range(0, max(1, len(s50) - h + 1), h)]
        rows.append((a / sr, float(np.median(s)), float(np.percentile(s, 95)), float(s.max()), float(max(sw))))
    for t, med, p95, mx, sw in rows:
        print(f"{int(t)//60}:{int(t)%60:02d}  GR median {med:4.1f}  p95 {p95:4.1f}  max {mx:4.1f}  swing {sw:4.1f} dB")
    bad = [r for r in rows if r[1] > 1.0 or r[3] > 4.5 or r[4] > 3.0]
    over = tp is not None and ceiling is not None and tp > ceiling + 0.05
    if over:
        print(f"FIX: true peak {tp:.2f} dBTP is over the ceiling {ceiling:.1f}")
    print("PASS" if not bad and not over else f"FIX: {len(bad)} window(s) over the bar (median > 1, max > 4.5 or swing > 3 dB)")
    return 0 if not bad and not over else 1


def selftest():
    sr = 48000; t = np.arange(int(sr * 2.5)) / sr
    x = 0.25 * np.sin(2 * np.pi * 220 * t)
    hits = [int(0.5 * sr), int(1.8 * sr)]
    for h in hits:
        x[h:h + 480] += 0.9 * np.hanning(960)[480:] * np.sign(np.sin(2 * np.pi * 3000 * t[h:h + 480]))
    y, g = limit(np.stack([x, x], 1), sr, -1.0, 5.0, 150.0)
    from scipy.signal import resample_poly
    tp = 20 * np.log10(np.abs(resample_poly(y, 4, 1, axis=0)).max())
    assert tp <= -0.95, f"true peak {tp:.2f} over the ceiling"
    for h in hits:
        first = np.argmax(g[h - int(0.1 * sr):h + 1] > 0.05) + h - int(0.1 * sr)
        assert h - first <= int(0.0105 * sr), f"gain fell {(h - first) / sr * 1000:.1f} ms before the hit"
        assert g[h + int(0.6 * sr) if h + int(0.6 * sr) < len(g) else -1] < 0.5, "release did not recover"
    assert g[int(0.2 * sr):int(0.45 * sr)].max() < 0.01, "quiet passage was limited"
    rng = np.random.default_rng(1); z = np.clip(rng.normal(0, 2.0, (sr, 2)), -2, 2)   # a file that starts on a loud hit
    yz, _ = limit(z, sr, -1.0, 5.0, 150.0)
    assert true_peak_db(yz) <= -0.95, f"loud start went over the ceiling: {true_peak_db(yz):.2f} dBTP"
    print("selftest PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp", nargs="?"); ap.add_argument("out", nargs="?")
    ap.add_argument("--ceiling", type=float, default=-1.2); ap.add_argument("--target", type=float)
    ap.add_argument("--look", type=float, default=5.0); ap.add_argument("--release", type=float, default=150.0)
    ap.add_argument("--report", action="store_true"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return 0
    if not a.inp or (not a.out and not a.report):
        ap.print_help(); return 2
    try:
        import soundfile as sf
        x, sr = sf.read(a.inp, always_2d=True)
        kw = dict(ceiling_db=a.ceiling, look_ms=a.look, release_ms=a.release)
        if a.target is not None:
            y, g, I, tp = to_target(x, sr, a.target, **kw); print(f"integrated {I:.1f} LUFS, true peak {tp:.1f} dBTP")
        else:
            y, g = limit(x, sr, **kw)
        tp4 = true_peak_db(y)
        if a.out:
            sf.write(a.out, y, sr, subtype="PCM_24"); print("wrote", a.out)
    except (RuntimeError, OSError, IndexError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr); return 2
    return report(g, sr, tp=tp4, ceiling=a.ceiling)


if __name__ == "__main__":
    sys.exit(main())
