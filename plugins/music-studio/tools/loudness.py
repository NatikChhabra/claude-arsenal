#!/usr/bin/env python3
"""loudness.py: measure a master (or a video's audio) the way the platforms do and say pass or fix. Needs ffmpeg.

    python loudness.py <file> [--target streaming|youtube|apple|club|ingame] [--json]
    python loudness.py <file> --vocal <vocal_stem.wav> --inst <instrumental_stem.wav>    + the phone-speaker vocal check
    python loudness.py --selftest

Reads ITU-R BS.1770 integrated loudness (LUFS), loudness range (LU) and true peak (dBTP) with ffmpeg's ebur128 filter
(peak=true), plus the loudest 3 s short-term window. Targets and their sources live in references/mix-master.md; the
table below must match it.

Phone-speaker check (--vocal/--inst): both stems band-passed to 400 Hz-8 kHz (what a phone speaker plays), short-term
loudness every 0.5 s; the vocal should sit at or above the instrumental where it sings. Reports the share of sung
windows where the vocal is more than 3 LU under the band-limited instrumental (house bar: <= 10%).
exit 0 = PASS, 1 = FIX (a target missed), 2 = error.
"""
import json, os, re, subprocess, sys, tempfile

TARGETS = {   # name: (integrated LUFS target, tolerance LU, max true peak dBTP)
    "streaming": (-14.0, 1.0, -1.0),   # Spotify/YouTube/Tidal/Amazon normalise to about -14; Apple Music about -16
    "youtube": (-14.0, 1.0, -1.0),
    "apple": (-16.0, 1.0, -1.0),
    "club": (-9.0, 2.0, -1.0),         # louder masters for DJ/club play; streaming turns them down
    "ingame": (-16.0, 2.0, -1.0),      # in-game radio/vehicle playback sits under voice chat; test in the game
}


def ebur128(path, extra_filter=""):
    chain = (extra_filter + "," if extra_filter else "") + "ebur128=peak=true:framelog=verbose"
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-loglevel", "verbose", "-i", path, "-vn", "-af", chain, "-f", "null", "-"],
                       capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip().splitlines()[-1] if p.stderr else "ffmpeg failed")
    err = p.stderr
    short = [(float(t), float(s)) for t, s in re.findall(r"t:\s*([\d.]+)[^\n]*?S:\s*(-?[\d.]+|-inf)", err)
             if s != "-inf" and float(s) > -70 and float(t) >= 3.0]
    summ = err.rsplit("Summary:", 1)[-1]
    def grab(label):
        m = re.search(label + r":\s*(-?[\d.]+|-inf)", summ)
        return float(m.group(1)) if m and m.group(1) != "-inf" else float("-inf")
    return {"integrated": grab("I"), "lra": grab("LRA"), "true_peak": grab("Peak"),
            "short_term_max": max((s for _, s in short), default=float("-inf")), "short": short}


def short_series(path, band=True):
    f = "highpass=f=400,lowpass=f=8000" if band else ""
    r = ebur128(path, f)
    out = {}
    for t, s in r["short"]:
        out[round(t * 2) / 2] = s
    return out


def phone_check(vocal, inst):
    v, i = short_series(vocal), short_series(inst)
    sung = [t for t, s in v.items() if s > -40 and t in i]
    if not sung:
        return {"sung_windows": 0, "buried_share": None}
    buried = [t for t in sung if v[t] < i[t] - 3]
    return {"sung_windows": len(sung), "buried_share": round(len(buried) / len(sung), 3),
            "worst": sorted(((round(i[t] - v[t], 1), t) for t in buried), reverse=True)[:5]}


def verdict(r, target):
    tgt, tol, tp = TARGETS[target]
    fixes = []
    if abs(r["integrated"] - tgt) > tol:
        fixes.append(f"integrated {r['integrated']:.1f} LUFS, target {tgt:.0f} +-{tol:.0f}")
    if r["true_peak"] > tp:
        fixes.append(f"true peak {r['true_peak']:.1f} dBTP, max {tp:.0f}")
    return fixes


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    for k in ("--target", "--vocal", "--inst"):
        if k in argv:
            args.remove(argv[argv.index(k) + 1])
    if not args:
        print(__doc__)
        return 2
    target = opt("--target", "streaming")
    try:
        r = ebur128(args[0])
    except (RuntimeError, FileNotFoundError) as e:
        print("ERROR", e)
        return 2
    fixes = verdict(r, target)
    out = {k: r[k] for k in ("integrated", "lra", "true_peak", "short_term_max")}
    out["target"] = target
    if opt("--vocal") and opt("--inst"):
        out["phone"] = phone_check(opt("--vocal"), opt("--inst"))
        bs = out["phone"]["buried_share"]
        if bs is not None and bs > 0.10:
            fixes.append(f"vocal buried on a phone speaker in {bs:.0%} of sung windows (bar <= 10%)")
    out["fixes"] = fixes
    if "--json" in argv:
        print(json.dumps(out, indent=2))
    else:
        print(f"integrated {r['integrated']:.1f} LUFS | LRA {r['lra']:.1f} LU | true peak {r['true_peak']:.1f} dBTP | "
              f"loudest 3 s {r['short_term_max']:.1f} LUFS")
        if "phone" in out:
            print("phone check:", out["phone"])
        for f in fixes:
            print("FIX", f)
        print("PASS" if not fixes else "FIX", f"({target})")
    return 1 if fixes else 0


def selftest():
    d = tempfile.mkdtemp()
    tone = os.path.join(d, "tone.wav")
    gen = lambda amp, f, out: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
        f"aevalsrc={amp}*sin(2*PI*{f}*t)|{amp}*sin(2*PI*{f}*t):s=48000:d=6", out], check=True)
    gen(0.2, 1000, tone)                                   # a steady 1 kHz stereo sine reads its peak level in LUFS
    r = ebur128(tone)
    ok = abs(r["integrated"] - r["true_peak"]) < 1.0 and len(r["short"]) > 10
    loud = os.path.join(d, "loud.wav")
    gen(1.0, 1000, loud)                                   # 0 dBFS: too loud, peak over -1
    hot = ebur128(loud)
    ok &= any("true peak" in f for f in verdict(hot, "streaming"))
    voc = os.path.join(d, "voc.wav"); ins = os.path.join(d, "ins.wav")
    gen(0.03, 1200, voc)                                   # a quiet "vocal" under loud noise = buried
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anoisesrc=duration=6:amplitude=0.3",
                    ins], check=True)
    pc = phone_check(voc, ins)
    ok &= pc["buried_share"] is not None and pc["buried_share"] > 0.5
    print(f"selftest {'PASS' if ok else 'FAIL'} (sine: {r['integrated']:.1f} LUFS vs peak {r['true_peak']:.1f}; buried {pc['buried_share']})")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
