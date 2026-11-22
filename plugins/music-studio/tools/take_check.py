#!/usr/bin/env python3
"""take_check.py: check a raw recording the minute it is made, before anyone plays on or builds from it.

    uv run --with numpy --with soundfile python take_check.py <take.wav> [<take2.wav> ...] [--json]
    uv run --with numpy --with soundfile python take_check.py --selftest

A take that is clipped, too quiet, one-sided or humming costs a whole re-record if it is found a week later in the mix.
This reads the file as recorded and says, in plain words, what to change on the guitar, the interface or the DAW:

  format     sample rate, bit depth, channels, length (48 kHz / 24-bit is the house default; 44.1 kHz is fine)
  channels   a channel more than 30 dB under the other is dead (a mono input on a stereo track): FIX the routing,
             or fold to mono from the live channel before any processing
  peak       loudest sample in dBFS: aim for -12 to -6 (room for picking transients); over -3 is hot; under -24 is
             too quiet (raise input gain next time: makeup gain later raises the hiss with it)
  clipped    samples at full scale, and flat tops (3+ samples stuck near the take's own maximum when it is over
             -1 dBFS): a Windows input or a pickup preamp can soft-clip below 0 dBFS
  floor      noise floor (10th percentile of 50 ms RMS while not digital silence) and the gap to the playing level
             (95th percentile): under 30 dB is noisy, under 20 dB is not usable for a release
  hum        mains hum (50 or 60 Hz and its harmonics) in the quiet stretches, 15 dB or more over the bins
             beside it: a charger, a ground loop or a pickup near a monitor
  dc         a DC offset over 1% of full scale (a faulty input; a high-pass at 20 Hz removes it)

Verdict per file: PASS, WARN (usable, fix next time) or FIX (record again or repair before use).
Read-only on the input. Exit 0 = PASS or WARN, 1 = FIX on any file, 2 = error.
"""
import json
import sys

FRAME_S = 0.05


def db(x):
    import numpy as np
    return float(20 * np.log10(max(float(x), 1e-12)))


def analyse(y, sr, subtype="", name="take"):
    """y: float array (samples, channels) in -1..1. Returns a dict of findings."""
    import numpy as np
    y = np.asarray(y, dtype=np.float64)
    if y.ndim == 1:
        y = y[:, None]
    n, ch = y.shape
    out = {"file": name, "sr": int(sr), "subtype": subtype, "channels": ch, "seconds": round(n / sr, 2),
           "issues": []}

    def issue(level, what, fix):
        out["issues"].append({"level": level, "what": what, "fix": fix})

    if n < sr * 2:
        issue("FIX", f"only {n / sr:.1f} s long", "record at least a few bars; this cannot be checked")
        out["verdict"] = "FIX"
        return out
    if sr not in (44100, 48000):
        issue("WARN", f"sample rate {sr} Hz", "set the DAW and the interface to 48 kHz (or 44.1 kHz) for every take of a song")
    if subtype.startswith("PCM_16"):
        issue("WARN", "16-bit recording", "record at 24-bit: quiet passages keep more detail and you can leave more headroom")

    # channels
    rms_ch = np.sqrt((y ** 2).mean(axis=0) + 1e-20)
    out["channel_rms_dbfs"] = [round(db(r), 1) for r in rms_ch]
    live = int(np.argmax(rms_ch))
    if ch > 1:
        for c in range(ch):
            if c != live and db(rms_ch[c]) < db(rms_ch[live]) - 30:
                issue("FIX", f"channel {c + 1} is dead ({db(rms_ch[c]) - db(rms_ch[live]):.0f} dB under channel {live + 1})",
                      f"record a mono track from input {live + 1} only (or fold to mono from channel {live + 1} before any processing)")
    x = y[:, live]

    # level
    peak = float(np.abs(y).max())
    out["peak_dbfs"] = round(db(peak), 1)
    full = int((np.abs(y) >= 0.999).sum())
    flat = 0
    if peak > 0.89:                                  # over about -1 dBFS: look for flat tops near the take's own max
        near = np.abs(x) >= peak * 0.998
        if near.any():
            edges = np.diff(np.concatenate(([0], near.astype(np.int8), [0])))
            starts, ends = np.where(edges == 1)[0], np.where(edges == -1)[0]
            flat = int(((ends - starts) >= 3).sum())
    out["clipped_samples"], out["flat_tops"] = full, flat
    if full > 0 or flat > 2:
        issue("FIX", f"clipped: {full} samples at full scale, {flat} flat tops near {db(peak):.1f} dBFS",
              "turn the input gain down (or the amp's USB level) until the hardest hit peaks around -6 dBFS, then record again")
    elif peak > 10 ** (-3 / 20):
        issue("WARN", f"hot: peaks at {db(peak):.1f} dBFS", "lower the input gain a little; aim for peaks between -12 and -6 dBFS")
    elif peak < 10 ** (-24 / 20):
        issue("FIX", f"too quiet: peaks at {db(peak):.1f} dBFS",
              "raise the input gain (interface knob or the amp's level) until the hardest hit reaches about -12 to -6 dBFS")

    # floor and playing level (50 ms frames, digital silence left out)
    hop = int(sr * FRAME_S)
    m = len(x) // hop
    fr = x[:m * hop].reshape(m, hop)
    frms = np.sqrt((fr ** 2).mean(axis=1))
    keep = frms > 1e-7
    if keep.sum() < 10:
        issue("FIX", "the take is silent", "check the input is armed and the cable is in the right input")
        out["verdict"] = "FIX"
        return out
    lv = frms[keep]
    floor, play = float(np.percentile(lv, 10)), float(np.percentile(lv, 95))
    out["floor_dbfs"], out["play_dbfs"] = round(db(floor), 1), round(db(play), 1)
    gap = db(play) - db(floor)
    out["floor_gap_db"] = round(gap, 1)
    if gap < 20:
        issue("FIX", f"noise floor only {gap:.0f} dB under the playing",
              "move away from fans and chargers, turn the input gain up and the amp/headphone volume down, and keep 2 s of silence before you play")
    elif gap < 30:
        issue("WARN", f"noise floor {gap:.0f} dB under the playing",
              "usable, but quieter room or more input gain helps (house aim: 30 dB or more)")

    # hum in the quietest fifth
    q = fr[keep][lv <= np.percentile(lv, 20)].ravel()
    if len(q) >= sr:
        q = q[: sr * 20] * np.hanning(min(len(q), sr * 20))
        spec = np.abs(np.fft.rfft(q)) ** 2
        freqs = np.fft.rfftfreq(len(q), 1 / sr)
        best = None
        for mains in (50.0, 60.0):
            excess = []
            for h in (1, 2, 3):
                f0 = mains * h
                band = (freqs > f0 - 1.5) & (freqs < f0 + 1.5)
                side = ((freqs > f0 - 12) & (freqs < f0 - 4)) | ((freqs > f0 + 4) & (freqs < f0 + 12))
                if band.any() and side.any():
                    excess.append(10 * np.log10(spec[band].max() / (np.median(spec[side]) + 1e-30) + 1e-30))
            if excess and (best is None or max(excess) > best[1]):
                best = (mains, max(excess))
        if best:
            out["hum_db"] = round(float(best[1]), 1)
            if best[1] >= 15:
                issue("WARN", f"{best[0]:.0f} Hz mains hum {best[1]:.0f} dB over its neighbours in the quiet parts",
                      "unplug the laptop charger, move the guitar away from the monitor, or plug the amp and PC into the same power strip")

    dc = float(np.abs(y.mean(axis=0)).max())
    out["dc"] = round(dc, 4)
    if dc > 0.01:
        issue("WARN", f"DC offset {dc:.3f}", "a 20 Hz high-pass on the track removes it; if it repeats, try another input")

    levels = [i["level"] for i in out["issues"]]
    out["verdict"] = "FIX" if "FIX" in levels else "WARN" if "WARN" in levels else "PASS"
    return out


def check_file(path):
    import soundfile as sf
    info = sf.info(path)
    y, sr = sf.read(path, always_2d=True, dtype="float64")
    return analyse(y, sr, info.subtype, path)


def show(r):
    lines = [f"{r['file']}: {r['verdict']}",
             f"  format   {r['sr']} Hz, {r.get('subtype') or '?'}, {r['channels']} ch, {r['seconds']} s"]
    if "peak_dbfs" in r:
        lines.append(f"  level    peak {r['peak_dbfs']} dBFS, playing {r.get('play_dbfs', '?')} dBFS, "
                     f"floor {r.get('floor_dbfs', '?')} dBFS (gap {r.get('floor_gap_db', '?')} dB)")
    for i in r["issues"]:
        lines.append(f"  {i['level']:<4}     {i['what']}\n           -> {i['fix']}")
    if not r["issues"]:
        lines.append("  ok       levels, channels, floor and hum all inside the house bar")
    return "\n".join(lines)


def _pluck_take(sr=48000, secs=8.0, amp=0.35, seed=0):
    import numpy as np
    rng = np.random.default_rng(seed)
    t = np.arange(int(sr * secs)) / sr
    y = np.zeros_like(t)
    for k, start in enumerate(np.arange(1.0, secs - 1, 0.5)):
        f = 110 * 2 ** (rng.integers(0, 12) / 12)
        i = int(start * sr)
        tt = t[: len(t) - i]
        y[i:] += amp * np.exp(-tt * 3) * (np.sin(2 * np.pi * f * tt) + 0.4 * np.sin(4 * np.pi * f * tt))
    y += rng.normal(0, 10 ** (-70 / 20), len(t))
    return y


def selftest():
    import numpy as np
    sr, ok = 48000, True

    def expect(label, y, verdict, must=None):
        nonlocal ok
        r = analyse(y, sr, "PCM_24", label)
        text = " | ".join(i["what"] for i in r["issues"])
        good = r["verdict"] == verdict and (must is None or must in text)
        ok &= good
        print(f"{'ok  ' if good else 'FAIL'} {label}: {r['verdict']} {text}")

    clean = _pluck_take(sr)
    clean = clean / np.abs(clean).max() * 10 ** (-8 / 20)
    expect("clean take", np.stack([clean, clean], 1), "PASS")
    expect("clipped", np.clip(clean * 6, -1, 1), "FIX", "clipped")
    soft = np.clip(clean * 4, -0.98, 0.98)
    expect("soft-clipped at -0.2 dBFS", soft, "FIX", "flat tops")
    expect("dead right channel", np.stack([clean, clean * 10 ** (-45 / 20)], 1), "FIX", "channel 2 is dead")
    expect("too quiet", clean * 10 ** (-22 / 20), "FIX", "too quiet")
    t = np.arange(len(clean)) / sr
    expect("50 Hz hum", clean + 10 ** (-52 / 20) * np.sin(2 * np.pi * 50 * t), "WARN", "50 Hz")
    noisy = clean + np.random.default_rng(1).normal(0, 10 ** (-33 / 20), len(clean))
    expect("noisy room", noisy, "FIX", "noise floor")
    expect("short", clean[: sr], "FIX", "long")
    print("selftest", "passed" if ok else "FAILED")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__)
        return 2
    results, rc = [], 0
    for f in files:
        try:
            r = check_file(f)
        except Exception as e:  # noqa: BLE001
            print(f"{f}: error: {e}")
            return 2
        results.append(r)
        if r["verdict"] == "FIX":
            rc = 1
    if "--json" in argv:
        print(json.dumps(results, indent=1))
    else:
        print("\n\n".join(show(r) for r in results))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
