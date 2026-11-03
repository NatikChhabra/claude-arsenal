"""watch.py - WATCH a whole render as text. Claude reads pictures and text but can't play a video, so this turns the full
runtime into ONE time-aligned pack read top to bottom: every --every seconds, what is said, what the picture does and
what the sound does, with flags where the timing breaks. It catches the class a few still frames hide: a dead stretch,
a joke stepped on by a cut, a hit with nothing on screen, a flash run, a frozen picture, an unplanned silence.

    uv run --no-project --with numpy python watch.py <video> [--words words.json] [--beats beatmap.json]
        [--every 0.5] [--from S --to S] [--sheets] [--dead 4] [--out DIR] [--selftest]

Writes <out or <video>_watch>/watch.md: a summary (runtime, cuts, hits, words and flags per minute, the 10 worst
windows) then one row per window: time | words starting there | picture (cut, motion still/slow/fast, frozen) | sound
(peak momentary LUFS, a hit, silence) | flags. --sheets adds a 12-tile contact sheet (<= 1536 px wide) for each of the
worst flagged windows, listed in watch.md: read the text first, open sheets only where it points.

Inputs: the video (ffmpeg + ffprobe on PATH); optional words.json (a list of {"text"|"word", "start", "end"}, or
{"words": [...]}, or {"segments": [{"words": [...]}]}: whisper, WhisperX and our transcripts all fit); optional
beatmap.json from music-studio `beatmap.py map` (its "beats" and "downbeats" lists): cuts are then marked on/off beat.

FLAGS (each names its rule):
  DEAD      > --dead s with no word, cut, hit or motion change (an edit's flat stretch; a music video's held shot is
            fine when the brief says so: read the pack, don't obey the flag blindly)
  OVERLOAD  > 4 distinct events (cuts, hits, word starts) inside 1 s: nothing lands
  STEP      a cut inside the last word before a >= 0.6 s pause: it steps on the punchline
  UNCUED    a loud hit with no cut, motion onset or word within 0.15 s: the sound has no picture cause
  FLASH     more than 3 large luminance flips in 1 s (WCAG 2.3.1)
  FROZEN    >= 1 s of identical frames outside a planned hold
  SILENCE   >= 0.8 s of silence (below -40 dB) inside the cut
  OFFBEAT   (with --beats) a cut more than 1 frame from every beat
"""
import json, os, re, statistics, subprocess, sys, tempfile

DEAD_S, BURST_N, PUNCH_GAP, CONTACT_S, FROZEN_S, SIL_S = 4.0, 4, 0.6, 0.15, 1.0, 0.8


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace")


def span(a, b):
    return (["-ss", str(a)] if a else []) + (["-to", str(b)] if b else [])


def probe(v):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate:format=duration",
             "-of", "json", v])
    j = json.loads(r.stdout or "{}")
    n, d = (j.get("streams") or [{}])[0].get("r_frame_rate", "30/1").split("/")
    return float(j.get("format", {}).get("duration", 0) or 0), float(n) / float(d or 1)


def cuts(v, a, b, thr=10):
    r = run(["ffmpeg", "-hide_banner", "-nostats", *span(a, b), "-i", v, "-an", "-vf",
             f"scale=320:-2,scdet=threshold={thr},metadata=print:key=lavfi.scd.time:file=-", "-f", "null", "-"])
    ts = sorted(float(x) + a for x in re.findall(r"lavfi\.scd\.time=([\d.]+)", r.stdout + r.stderr) if float(x) > 0.05)
    merged = []
    for t in ts:                                   # a 1-3 frame double fire is one cut
        if not merged or t - merged[-1] > 0.1:
            merged.append(t)
    return merged


def loudness(v, a, b):
    """Momentary loudness every 0.1 s, silences, integrated LUFS."""
    r = run(["ffmpeg", "-hide_banner", "-nostats", *span(a, b), "-i", v, "-vn", "-af",
             "ebur128=metadata=1,ametadata=print:key=lavfi.r128.M,silencedetect=n=-40dB:d=0.3", "-f", "null", "-"])
    out, m, t = r.stdout + r.stderr, [], None
    for line in out.splitlines():
        k = re.search(r"pts_time:([\d.]+)", line)
        if k:
            t = float(k.group(1))
            continue
        k = re.search(r"lavfi\.r128\.M=(-?[\d.]+|-?inf)", line)
        if k and t is not None:
            try:
                m.append((t + a, max(float(k.group(1)), -70.0)))
            except ValueError:
                pass
    starts = [float(x) + a for x in re.findall(r"silence_start: (-?[\d.]+)", out)]
    ends = [float(x) + a for x in re.findall(r"silence_end: ([\d.]+)", out)]
    sil = list(zip(starts, ends + [b or 1e9] * (len(starts) - len(ends))))
    i = re.findall(r"I:\s+(-?[\d.]+) LUFS", out)
    return m, sil, float(i[-1]) if i else None


def hits(m, rise=6.0, win=30, maxlen=15):
    """Short spikes: momentary >= the local median (+-3 s) + rise, lasting <= 1.5 s."""
    vals, out, i = [x for _, x in m], [], 0
    while i < len(m):
        med = statistics.median(vals[max(0, i - win):min(len(m), i + win)])
        if vals[i] >= med + rise and vals[i] > -40:
            j = i
            while j < len(m) and vals[j] >= med + rise:
                j += 1
            if j - i <= maxlen:
                out.append(round(m[i][0], 2))
            i = j
        else:
            i += 1
    return out


def picture(v, a, b, fps=10):
    """Per decoded frame (fps): time, mean abs change vs the previous frame (0-255), mean luminance 0-1."""
    import numpy as np
    w, h = 160, 90
    raw = subprocess.run(["ffmpeg", "-v", "error", *span(a, b), "-i", v, "-vf", f"fps={fps},scale={w}:{h}",
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
    n = len(raw) // (w * h)
    f = np.frombuffer(raw[:n * w * h], np.uint8).reshape(n, h, w).astype(float)
    diff = [0.0] + [float(np.abs(f[i] - f[i - 1]).mean()) for i in range(1, n)]
    lum = [float((x / 255).mean()) for x in f]
    return [(a + i / fps, diff[i], lum[i]) for i in range(n)]


def load_words(p):
    if not p:
        return []
    j = json.load(open(p, encoding="utf-8"))
    if isinstance(j, dict):
        j = j.get("words") or [w for s in j.get("segments", []) for w in s.get("words", [])]
    out = []
    for w in j:
        t = (w.get("text") or w.get("word") or "").strip()
        s, e = w.get("start", w.get("s")), w.get("end", w.get("e"))
        if t and s is not None:
            out.append((float(s), float(e if e is not None else s), t))
    return sorted(out)


def load_beats(p):
    if not p:
        return []
    j = json.load(open(p, encoding="utf-8"))
    return sorted(float(x) for x in (j.get("beats") or []) + (j.get("downbeats") or []))


def analyse(v, words=None, beats=None, every=0.5, a=0.0, b=0.0, dead=DEAD_S):
    dur, fps = probe(v)
    b = b or dur
    W = load_words(words)
    B = load_beats(beats)
    C = cuts(v, a, b)
    M, S, I = loudness(v, a, b)
    H = hits(M)
    P = picture(v, a, b)
    frame = 1.0 / (fps or 30)
    # motion onsets: a jump in frame change; frozen runs: consecutive near-zero change
    onsets = [t for i, (t, d, _) in enumerate(P[1:], 1) if d > 6 and P[i - 1][1] < 2]
    frozen, run_start = [], None
    for t, d, _ in P[1:]:
        if d < 0.2:
            run_start = t if run_start is None else run_start
        else:
            if run_start is not None and t - run_start >= FROZEN_S:
                frozen.append((run_start, t))
            run_start = None
    if run_start is not None and P and P[-1][0] - run_start >= FROZEN_S:
        frozen.append((run_start, P[-1][0]))
    # flashes (whole frame, approximated): count luminance flips >= 0.1 in any 1 s
    flips, last, direction = [], (P[0][2] if P else 0), 0
    for t, _, L in P:
        d = L - last
        if abs(d) >= 0.1:
            nd = 1 if d > 0 else -1
            if nd != direction:
                flips.append(t)
                direction = nd
            last = L
    flash_t = [t for t in flips if sum(1 for u in flips if t <= u < t + 1) // 2 > 3]
    flags = []
    # DEAD
    events = sorted(C + H + [w[0] for w in W] + onsets + [a, b])
    for x, y in zip(events, events[1:]):
        if y - x > dead:
            flags.append((x, "DEAD", f"{y - x:.1f} s with no word, cut, hit or motion change"))
    # OVERLOAD
    ev = sorted(C + H + [w[0] for w in W])
    for i, t in enumerate(ev):
        n = len({round(u, 1) for u in ev[i:] if u < t + 1})
        if n > BURST_N and not any(f[1] == "OVERLOAD" and t - f[0] < 1 for f in flags):
            flags.append((t, "OVERLOAD", f"{n} events inside 1 s"))
    # STEP: a cut inside the last word before a pause
    for i, (s, e, t) in enumerate(W[:-1]):
        if W[i + 1][0] - e >= PUNCH_GAP:
            for c in C:
                if s < c < e:
                    flags.append((c, "STEP", f"a cut at {c:.2f} inside '{t}' before a {W[i + 1][0] - e:.1f} s pause"))
    # UNCUED
    causes = C + onsets + [w[0] for w in W]
    for h in H:
        if not any(abs(h - c) <= CONTACT_S for c in causes):
            flags.append((h, "UNCUED", "a loud hit with no cut, motion onset or word within 0.15 s"))
    if flash_t:
        flags.append((flash_t[0], "FLASH", f"more than 3 flashes in 1 s from {flash_t[0]:.1f} s (WCAG 2.3.1)"))
    for x, y in frozen:
        flags.append((x, "FROZEN", f"{y - x:.1f} s of identical frames"))
    for x, y in S:
        y = min(y, b)
        if y - x >= SIL_S and x > a + 0.2 and y < b - 0.2:
            flags.append((x, "SILENCE", f"{y - x:.1f} s below -40 dB"))
    if B:
        for c in C:
            if min(abs(c - x) for x in B) > frame * 1.01:
                flags.append((c, "OFFBEAT", f"cut at {c:.2f} is {min(abs(c - x) for x in B) * 1000:.0f} ms from the nearest beat"))
    flags.sort()
    # rows
    rows, t = [], a
    while t < b - 1e-6:
        u = min(t + every, b)
        said = " ".join(w[2] for w in W if t <= w[0] < u)
        pc = [p for p in P if t <= p[0] < u]
        mo = max((p[1] for p in pc), default=0)
        kind = "still" if mo < 1 else "slow" if mo < 6 else "fast"
        pic = ("CUT " if any(t <= c < u for c in C) else "") + kind + (" frozen" if any(x <= t < y for x, y in frozen) else "")
        lm = [x for tm, x in M if t <= tm < u]
        snd = (f"{max(lm):.0f} LUFS" if lm else "-") + (" HIT" if any(t <= h < u for h in H) else "") + \
              (" silence" if any(x <= t < y for x, y in S) else "")
        fl = ", ".join(sorted({f[1] for f in flags if t <= f[0] < u}))
        rows.append((t, said, pic, snd, fl))
        t = u
    return {"video": v, "duration": round(b - a, 2), "fps": round(fps, 3), "integrated": I, "cuts": C, "hits": H,
            "words": len(W), "flags": flags, "rows": rows, "every": every, "from": a, "to": b, "beats": bool(B)}


def mmss(t):
    return f"{int(t) // 60}:{t % 60:05.2f}"


def sheet(v, t0, t1, out):
    n = 12
    fps = max(n / max(t1 - t0, 0.5), 0.5)
    run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, t0)), "-to", str(t1), "-i", v, "-vf",
         f"fps={fps:.3f},scale=256:-2,tile=6x2", "-frames:v", "1", out])
    return out if os.path.exists(out) else None


def write(r, out_dir, sheets=False):
    os.makedirs(out_dir, exist_ok=True)
    mins = max(r["duration"] / 60, 1 / 60)
    kinds = {}
    for _, k, _ in r["flags"]:
        kinds[k] = kinds.get(k, 0) + 1
    worst = sorted(r["flags"], key=lambda f: ["FLASH", "STEP", "DEAD", "UNCUED", "FROZEN", "SILENCE", "OVERLOAD", "OFFBEAT"].index(f[1]))[:10]
    L = [f"# Watch pack: {os.path.basename(r['video'])}", "",
         f"- Runtime {mmss(r['duration'])} ({r['from']:.1f}-{r['to']:.1f} s), {r['fps']} fps, integrated "
         f"{r['integrated']} LUFS", f"- Per minute: {len(r['cuts']) / mins:.1f} cuts, {len(r['hits']) / mins:.1f} hits, "
         f"{r['words'] / mins:.0f} words", f"- Flags: " + (", ".join(f"{k} {n}" for k, n in sorted(kinds.items())) or "none"),
         "", "## Worst windows", ""]
    L += [f"- {mmss(t)} {k}: {d}" for t, k, d in worst] or ["- none"]
    if sheets and worst:
        L += ["", "## Sheets (open only where the text points)", ""]
        for i, (t, k, _) in enumerate(worst[:6]):
            p = sheet(r["video"], t - 1.0, t + 2.0, os.path.join(out_dir, f"sheet_{i + 1:02d}_{k}.png"))
            if p:
                L.append(f"- {mmss(t)} {k}: {os.path.basename(p)}")
    L += ["", f"## Timeline (every {r['every']} s)", "", "| time | words | picture | sound | flags |", "|---|---|---|---|---|"]
    L += [f"| {mmss(t)} | {w.replace('|', '/')} | {p} | {s} | {f} |" for t, w, p, s, f in r["rows"]]
    path = os.path.join(out_dir, "watch.md")
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")
    return path


def selftest():
    d = tempfile.mkdtemp()
    v = os.path.join(d, "t.mp4")
    # 0-3 s red with a tone, 3-9 s blue still and silent (a dead stretch + silence), 9-10 s white/black strobe at 10 Hz
    r = run(["ffmpeg", "-v", "error", "-y",
             "-f", "lavfi", "-i", "color=c=red:s=320x180:r=30:d=3", "-f", "lavfi", "-i", "color=c=blue:s=320x180:r=30:d=6",
             "-f", "lavfi", "-i", "color=c=white:s=320x180:r=30:d=1",
             "-f", "lavfi", "-i", "sine=f=440:d=3:sample_rate=48000", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono:d=6",
             "-f", "lavfi", "-i", "sine=f=440:d=1:sample_rate=48000",
             "-filter_complex", "[2:v]geq=lum='if(lt(mod(N\\,6)\\,3)\\,255\\,0)':cb=128:cr=128[s];"
             "[0:v][3:a][1:v][4:a][s][5:a]concat=n=3:v=1:a=1[v][a]",
             "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", v])
    assert os.path.exists(v), r.stderr[-400:]
    wj = os.path.join(d, "w.json")
    json.dump([{"text": "hello", "start": 0.5, "end": 0.9}, {"text": "there", "start": 2.8, "end": 3.2},
               {"text": "ok", "start": 4.5, "end": 4.8}], open(wj, "w"))
    res = analyse(v, words=wj)
    kinds = {k for _, k, _ in res["flags"]}
    assert any(abs(c - 3.0) < 0.15 for c in res["cuts"]), res["cuts"]
    assert {"DEAD", "SILENCE", "FROZEN", "FLASH", "STEP"} <= kinds, kinds
    p = write(res, os.path.join(d, "pack"))
    assert "| time | words |" in open(p).read()
    print("PASS  watch.py --selftest: the cut at 3 s is found; DEAD, SILENCE, FROZEN, FLASH and STEP each fire on a "
          "synthetic clip; the pack writes")


def main():
    a = sys.argv[1:]
    if "--selftest" in a:
        return selftest()

    def opt(k, cast=str, default=None):
        if k not in a:
            return default
        i = a.index(k)
        v = a[i + 1]
        del a[i:i + 2]
        return cast(v)
    words, beats, out = opt("--words"), opt("--beats"), opt("--out")
    every, t0, t1, dead = opt("--every", float, 0.5), opt("--from", float, 0.0), opt("--to", float, 0.0), opt("--dead", float, DEAD_S)
    sheets = "--sheets" in a
    vids = [x for x in a if not x.startswith("--")]
    if len(vids) != 1 or not os.path.exists(vids[0]):
        sys.exit(__doc__)
    v = vids[0]
    r = analyse(v, words, beats, every, t0, t1, dead)
    p = write(r, out or os.path.splitext(v)[0] + "_watch", sheets)
    kinds = {}
    for _, k, _ in r["flags"]:
        kinds[k] = kinds.get(k, 0) + 1
    print(p)
    print(f"{mmss(r['duration'])}, {len(r['cuts'])} cuts, {len(r['hits'])} hits, flags: "
          + (", ".join(f"{k} {n}" for k, n in sorted(kinds.items())) or "none"))


if __name__ == "__main__":
    main()
