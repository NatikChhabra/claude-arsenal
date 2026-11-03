"""still_check.py - THE pixel gate for a finished graphic: measures it at the size people really see it.

Thumbnails, posters, hiring and business ads (in game, Discord, socials), in-game billboards, covers, story frames, and
animated GIF / MP4 / WebP loops. It catches what makes work look cheap or machine-made before anyone else sees it:
text too small to read where it lives, a wall of words, weak glyph contrast, no single focal point, clutter, the
oversaturated "AI gloss", the AI palette, AI provenance metadata, sameness with the last pieces, and on animations the
stock-template motion (a particle field of embers or sparks, the whole frame moving), flashes over 3 a second, a loop
that jumps, and a file over its upload budget.

    uv run --no-project --with pillow --with numpy --with scipy --with rapidocr-onnxruntime python still_check.py \
        FILE [FILE ...] --as thumbnail|ad|ingame|cover|story
        [--words "<the exact words you put on it>"]   word count + slop use these instead of the OCR read
        [--title "<its video title>"]                 thumbnail: its words must add to the title, not repeat it
        [--numbers-ok "<where each number on it is true>"]
        [--frame <the real source frame or photo it was built from>]   AI palette check against the real colours
        [--vs a.png b.png ...]                        the brand's last pieces (or rivals): sameness + the --mock line-up
        [--mock out.png]                              ours among the --vs pieces at view size, dark and light, key printed
        [--budget-mb N]                               animation upload budget (ad default 10: Discord's free limit)
        [--json] [--selftest]
(re-runs itself under uv with those packages when they are missing; CPU only; ffmpeg needed for MP4/MOV/WEBM.)

Rows (PASS / WARN / FAIL + 0-10; overall = the mean, capped at 4.9 when a row FAILs; exit 1 on any FAIL):
  text_px    the headline (tallest text line) height at the profile's smallest view; fine print under 6 px at the
             largest view = WARN (nobody reads it). Text = RapidOCR lines (logos and UI words count: a viewer can't tell).
  words      words on the frame; the profile sets the wall.
  contrast   WCAG ratio of the headline's glyphs vs what is behind them (Otsu split inside the line box).
  subject    the largest salient region's height share (frequency-tuned saliency, a proxy).
  focal      salient regions >= 2% of the frame: one story, 1-3 things.
  clutter    the share of pixels on a strong edge at the largest view.
  pop        colourfulness (Hasler-Suesstrunk) at the smallest view; > 25% of pixels at HSV S > 0.9 = the AI gloss WARN.
  layout     a text line clipped by the frame edge, or text on text.
  badge, tv_top, title_dup   thumbnail only (the duration badge corner, the TV app's top half, a title repeat).
  slop       FAIL: an em or en dash, a banned word (design references/tells.md, the one list), faked platform UI on a
             thumbnail. WARN: a number with no --numbers-ok source, AI provenance in the file (report, never strip), the
             AI palette (teal+orange or purple far above the --frame's), dHash distance < 10 to a --vs piece or another file in the run (same template).
  Animation rows (GIF, APNG, WebP, MP4, MOV, WEBM; the still rows run on the rest frame, the one closest to the median):
  flash      WCAG 2.3.1 general flash, per quadrant: more than 3 flashes in any 1 s = FAIL.
  particles  small separate moving specks (embers, sparks, dust, snow, bokeh): median > 25 a frame = WARN, the
             stock-template tell; motion belongs to the product (steam off the food, a sign flicker that the place owns).
  motion     the median share of the frame changing per frame: > 40% = WARN (nothing holds still long enough to read).
  loop       last frame vs first: a jump far above the normal frame step = WARN (the loop shows its seam).
  size       bytes vs --budget-mb: over = FAIL, over 90% = WARN.
The pixel rows are a FLOOR, not taste: a card can pass every row and still be a stock idea. The stranger read and the
blind review (design references/process.md and ads.md) decide whether the idea lands.

Calibration: the thumbnail thresholds come from 290 real YouTube cards (role models' winners and losers, small channels'
best and worst, Oct 2026): every pixel feature moves <= 0.06 sd between winners and losers, but the FAIL rate falls from
41% (losers) to 19% (winners). So the rows stop unreadable work; they don't predict clicks. Other profiles scale the same
floors to their viewing size (re-tune each profile after 3-5 real pieces and log the numbers in ads.md).
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TELLS = os.path.normpath(os.path.join(HERE, "..", "references", "tells.md"))
TITLE_PY = os.path.normpath(os.path.join(HERE, "..", "..", "..", "..", "creator", "skills", "yt-package"))
DARK, LIGHT = (15, 15, 15), (255, 255, 255)
DASH = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
FAKE_UI = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\b|\bviews?\b|\bsubscrib\w*|\bwatch later\b|\blive now\b", re.I)
NUM = re.compile(r"[$+\-]?\d[\d,.]*\s?(?:%|k|m)?", re.I)
ANIM_EXT = (".gif", ".webp", ".apng", ".mp4", ".mov", ".webm", ".mkv")
PROV = ("c2pa", "jumbf", "trainedAlgorithmicMedia", "compositeSynthetic", "Midjourney", "DALL-E", "Firefly", "Gemini",
        "Imagen", "Stable Diffusion", "Nano Banana", "Ideogram", "Leonardo")

# Each profile: the long-side canvas the frame is measured on, the view widths people see it at (smallest first),
# the (fail, good) pairs that differ from the thumbnail floors, and which thumbnail-only rows apply.
PROFILES = {
    "thumbnail": dict(views={"suggested": 168, "search": 246}, words=(12, 3), head=(6.0, 11.0), thumb=True,
                      what="a 1280x720 video thumbnail in the phone feed"),
    "ad": dict(views={"scroll_past": 200, "phone_embed": 300}, words=(40, 18), head=(8.0, 14.0), thumb=False,
               what="a poster or ad posted in chat, a feed or a phone (Discord embed ~300 px on a phone)"),
    "ingame": dict(views={"across_street": 128, "passing": 256}, words=(16, 6), head=(5.0, 9.0), thumb=False,
                   what="an in-game billboard, sign or screen seen from the street"),
    "cover": dict(views={"playlist_row": 64, "grid": 180}, words=(10, 4), head=(3.0, 6.0), thumb=False,
                  what="a 3000x3000 single or album cover (64 px in a playlist row)"),
    "story": dict(views={"grid": 120, "phone": 390}, words=(20, 8), head=(5.0, 9.0), thumb=False,
                  what="a 9:16 story, Reel or Short cover"),
}
# (fail_at, good_at); score 3 at fail_at, 10 at good_at, linear. Thumbnail calibration, see the docstring.
BASE = {"contrast": (2.0, 4.5), "subject": (0.22, 0.40), "focal": (5, 3), "clutter": (0.42, 0.26), "pop": (35.0, 70.0),
        "ui_sep": (15.0, 35.0), "tv_top": (0.27, 0.50)}
HARD = {"text_px", "words", "contrast"}          # pixel rows that may FAIL; the rest WARN at most (ideas win, not pixels)
BADGE = (1100 / 1280, 620 / 720)                # YouTube's duration badge sits right of / below this


def deps():
    try:
        import numpy, scipy, PIL, rapidocr_onnxruntime  # noqa: F401
    except ImportError:
        if os.environ.get("STILL_CHECK_DEPS"):
            sys.exit("still_check.py: needs pillow numpy scipy rapidocr-onnxruntime")
        sys.exit(subprocess.call(["uv", "run", "--no-project", "--with", "pillow", "--with", "numpy", "--with", "scipy",
                                  "--with", "rapidocr-onnxruntime", "python", os.path.abspath(__file__)] + sys.argv[1:],
                                 env=dict(os.environ, STILL_CHECK_DEPS="1")))


def banned_words():
    try:
        block = open(TELLS, encoding="utf-8").read().split("Banned words", 1)[1].split("```", 2)[1]
    except (OSError, IndexError):
        return []
    out = []
    for line in block.splitlines():
        if line.lower().startswith("in instructions"):
            continue
        out += [w for w in (re.sub(r"\(.*?\)", "", x).strip().lower() for x in line.split(",")) if w]
    return out


_OCR = None
def ocr(img):
    """[(text, (x0, y0, x1, y1), box height px, read)] on the measured canvas. Every detected line counts for size,
    contrast and layout; only a confident read (>= 0.8) counts as words, an unread line's words are estimated from its
    width (~3 heights a word): heavy display type is often detected but misread."""
    global _OCR
    import numpy as np
    if _OCR is None:
        from rapidocr_onnxruntime import RapidOCR
        _OCR = RapidOCR(text_score=0.0)
    res, _ = _OCR(np.asarray(img))
    out = []
    for quad, txt, conf in res or []:
        q = np.array(quad, float)
        h = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
        if h < 12:
            continue
        read = float(conf) >= 0.8 and len(re.sub(r"\W", "", txt)) >= 1
        w = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
        out.append((txt if read else f"<unread x{max(1, round(w / (3 * h)))}>",
                    (q[:, 0].min(), q[:, 1].min(), q[:, 0].max(), q[:, 1].max()), h, read))
    return out


def lab(rgb):
    import numpy as np
    c = rgb / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    xyz = c @ np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]]).T
    xyz /= (0.95047, 1.0, 1.08883)
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def rel_lum(rgb):
    import numpy as np
    c = np.asarray(rgb, float) / 255.0
    c = np.where(c > 0.03928, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    return c @ np.array([0.2126, 0.7152, 0.0722])


def glyph_contrast(crop):
    import numpy as np
    px = crop.reshape(-1, 3).astype(float)
    if len(px) < 8:
        return 1.0
    L = rel_lum(px)
    best, th = -1, L.mean()
    for t in np.quantile(L, np.linspace(0.05, 0.95, 37)):
        a, b = L[L <= t], L[L > t]
        if len(a) and len(b):
            v = len(a) * len(b) * (a.mean() - b.mean()) ** 2
            if v > best:
                best, th = v, t
    l1, l2 = sorted((rel_lum(px[L <= th].mean(0)), rel_lum(px[L > th].mean(0))))
    return (l2 + 0.05) / (l1 + 0.05)


def saliency(img):
    """Centre-surround colour saliency (|Lab blur 3 - Lab blur 25|, after Achanta 2009) on a 160 px long side, plus the
    regions of its top 20% (>= 2% of the frame each), largest first."""
    import numpy as np
    from scipy import ndimage
    w, h = img.size
    sw, sh = (160, max(1, round(160 * h / w))) if w >= h else (max(1, round(160 * w / h)), 160)
    a = lab(np.asarray(img.resize((sw, sh)), float))
    s = np.linalg.norm(ndimage.gaussian_filter(a, (3, 3, 0)) - ndimage.gaussian_filter(a, (25, 25, 0)), axis=-1)
    s = (s - s.min()) / (np.ptp(s) + 1e-9)
    m = ndimage.binary_opening(ndimage.binary_closing(s > np.quantile(s, 0.8), iterations=2))
    lbl, n = ndimage.label(m)
    regs = [r for r in ((lbl == i) for i in range(1, n + 1)) if r.mean() >= 0.02]
    return s, sorted(regs, key=lambda r: -r.sum())


def palette(hsv):
    """Of the saturated pixels (S > 0.5, V > 0.3): the teal+orange share and the purple/magenta share."""
    h = hsv[..., 0] * 360
    sat = (hsv[..., 1] > 0.5) & (hsv[..., 2] > 0.3)
    n = max(int(sat.sum()), 1)
    return {"teal_orange": round(float((sat & (((h >= 170) & (h <= 200)) | ((h >= 20) & (h <= 40)))).sum() / n), 3),
            "purple": round(float((sat & (h >= 270) & (h <= 320)).sum() / n), 3)}


def dhash(im):
    import numpy as np
    g = np.asarray(im.convert("L").resize((9, 8)), int)
    return int("".join("1" if b else "0" for b in (g[:, 1:] > g[:, :-1]).ravel()), 2)


def canvas(im, prof):
    """The measuring canvas: thumbnails at 1280x720 (an hqdefault 4:3 card loses its letterbox), the rest at a 1280 px
    long side, aspect kept."""
    from PIL import Image
    im = im.convert("RGB")
    if prof == "thumbnail":
        if abs(im.width / im.height - 4 / 3) < 0.02:
            bh = round(im.height * 0.125)
            im = im.crop((0, bh, im.width, im.height - bh))
        return im.resize((1280, 720), Image.LANCZOS)
    k = 1280 / max(im.size)
    return im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)


# ---------- animation ----------

def load_frames(path, long_side=320, max_frames=360):
    """(frames as float arrays at a small size, durations s, the full-size rest frame as a PIL image)."""
    import numpy as np
    from PIL import Image, ImageSequence
    ext = os.path.splitext(path)[1].lower()
    full, durs = [], []
    if ext in (".gif", ".webp", ".apng", ".png"):
        im = Image.open(path)
        for fr in ImageSequence.Iterator(im):
            full.append(fr.convert("RGB"))
            durs.append(max(fr.info.get("duration", im.info.get("duration", 100)) or 100, 20) / 1000)
            if len(full) >= max_frames:
                break
    else:
        probe = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                                "-of", "csv=p=0", path], capture_output=True, text=True).stdout.strip().split(",")
        w, h = int(probe[0]), int(probe[1])
        fps = 15
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-t", str(max_frames / fps), "-vf", f"fps={fps}",
                              "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
        n = len(raw) // (w * h * 3)
        arr = np.frombuffer(raw[:n * w * h * 3], np.uint8).reshape(n, h, w, 3)
        full = [Image.fromarray(a) for a in arr]
        durs = [1 / fps] * n
    if not full:
        sys.exit(f"still_check.py: no frames in {path}")
    k = long_side / max(full[0].size)
    size = (max(1, round(full[0].width * k)), max(1, round(full[0].height * k)))
    small = [np.asarray(f.resize(size), float) for f in full]
    med = np.median(np.stack(small), 0)
    rest = int(np.argmin([np.abs(s - med).mean() for s in small]))
    return small, durs, full[rest], rest


def flashes(small, durs):
    """Max flashes in any 1 s window over the 4 quadrants (WCAG 2.3.1 general flash, approximated: a flash = a pair of
    opposing relative-luminance changes of >= 0.1 where the darker state is <= 0.8)."""
    import numpy as np
    h, w = small[0].shape[:2]
    worst = 0
    t = np.cumsum([0] + durs[:-1])
    for qy in (slice(0, h // 2), slice(h // 2, h)):
        for qx in (slice(0, w // 2), slice(w // 2, w)):
            L = np.array([rel_lum(f[qy, qx].reshape(-1, 3)).mean() for f in small])
            ext, times, last, direction = [L[0]], [t[0]], L[0], 0      # turning points that moved >= 0.1
            for i in range(1, len(L)):
                d = L[i] - last
                if abs(d) >= 0.1 and min(L[i], last) <= 0.8:
                    nd = 1 if d > 0 else -1
                    if nd != direction:
                        ext.append(L[i]); times.append(t[i]); direction = nd
                    last = L[i]
                elif (direction > 0 and L[i] > last) or (direction < 0 and L[i] < last):
                    last = L[i]
            tr = np.array(times[1:])
            for i in range(len(tr)):
                worst = max(worst, int(((tr >= tr[i]) & (tr < tr[i] + 1.0)).sum()) // 2)
    return worst


def anim_measure(small, durs, path, budget_mb):
    import numpy as np
    from scipy import ndimage
    g = [s.mean(-1) for s in small]
    steps = [np.abs(g[i] - g[i - 1]) for i in range(1, len(g))]
    area = g[0].size
    moving, specks = [], []
    for d in steps:
        m = d > 18
        moving.append(float(m.mean()))
        lbl, n = ndimage.label(ndimage.binary_opening(m) if m.sum() > 50 else m)
        if n:
            sizes = ndimage.sum(m, lbl, range(1, n + 1))
            specks.append(int(((sizes >= 2) & (sizes <= 0.0015 * area)).sum()))
        else:
            specks.append(0)
    step_mean = [float(d.mean()) for d in steps] or [0.0]
    seam = float(np.abs(g[-1] - g[0]).mean()) if len(g) > 1 else 0.0
    return {"frames": len(small), "seconds": round(sum(durs), 2), "flashes_per_s": flashes(small, durs) if len(small) > 2 else 0,
            "particles": int(np.median(specks)) if specks else 0, "motion": round(float(np.median(moving)) if moving else 0.0, 3),
            "seam": round(seam, 1), "step": round(float(np.median(step_mean)), 1),
            "bytes": os.path.getsize(path), "budget_mb": budget_mb}


def anim_rows(a):
    out = []
    f = a["flashes_per_s"]
    out.append(("flash", "FAIL" if f > 3 else "PASS", 0.0 if f > 3 else 10.0,
                f"{f} flashes in the worst 1 s (WCAG 2.3.1: never more than 3)"))
    p = a["particles"]
    out.append(("particles", "WARN" if p > 25 else "PASS", 5.0 if p > 25 else 10.0,
                f"median {p} small moving specks a frame" + (": a particle field (embers, sparks, dust, bokeh) is the stock "
                "template tell; move the product instead (ads.md)" if p > 25 else "")))
    mo = a["motion"]
    out.append(("motion", "WARN" if mo > 0.4 else "PASS", 5.0 if mo > 0.4 else 10.0,
                f"{mo:.0%} of the frame changes per frame (median)" + ("; nothing holds still to be read" if mo > 0.4 else "")))
    jump = a["seam"] > max(6.0, 4 * a["step"])
    out.append(("loop", "WARN" if jump else "PASS", 6.0 if jump else 10.0,
                f"last-to-first change {a['seam']} vs a normal step {a['step']} (0-255)" + ("; the loop jumps" if jump else "")))
    if a["budget_mb"]:
        mb, b = a["bytes"] / 1e6, a["budget_mb"]
        st = "FAIL" if mb > b else "WARN" if mb > 0.9 * b else "PASS"
        out.append(("size", st, {"FAIL": 0.0, "WARN": 7.0, "PASS": 10.0}[st], f"{mb:.1f} MB of a {b} MB budget"))
    return out


# ---------- the still measure ----------

def measure(path, prof="thumbnail", title=None, numbers_ok=None, given=None, frame=None, im=None):
    import numpy as np
    from PIL import Image
    P = PROFILES[prof]
    src = im if im is not None else Image.open(path)
    native = src.size
    im = canvas(src, prof)
    W, H = im.size
    a = np.asarray(im, float)
    lines = ocr(im)
    split = lambda t: [x for w in re.findall(r"\d[\d,.]*|[^\W\d_]+(?:'[^\W_]+)?", t)
                       for x in [w] * (round(len(w) / 4.5) if len(w) >= 10 and not w[0].isdigit() else 1)]
    read = given if given else " ".join(t for t, _, _, r in lines if r)
    views = list(P["views"].items())
    (sn, sv), (ln, lv) = views[0], views[-1]
    big = np.asarray(im.resize((lv, max(1, round(lv * H / W))), Image.LANCZOS), float)
    kx, ky = big.shape[1] / W, big.shape[0] / H
    contr = [glyph_contrast(big[int(y0 * ky):max(int(y1 * ky), int(y0 * ky) + 2), int(x0 * kx):max(int(x1 * kx), int(x0 * kx) + 2)])
             for _, (x0, y0, x1, y1), _, _ in lines]
    keep = [i for i, l in enumerate(lines) if l[3] or contr[i] >= 2.0]
    lines, contr = [lines[i] for i in keep], [contr[i] for i in keep]
    words = len(split(given)) if given else sum(len(split(t)) if r else int(t[9:-1]) for t, _, _, r in lines)
    s, regs = saliency(im)
    subj = 0.0
    if regs:
        ys = np.where(regs[0].any(1))[0]
        subj = (ys.max() - ys.min() + 1) / s.shape[0]
    gy, gx = np.gradient(lab(big)[..., 0])
    clutter = float((np.hypot(gx, gy) > 8).mean())
    sm = np.asarray(im.resize((sv, max(1, round(sv * H / W))), Image.LANCZOS), float)
    rg, yb = sm[..., 0] - sm[..., 1], 0.5 * (sm[..., 0] + sm[..., 1]) - sm[..., 2]
    pop = float(np.hypot(rg.std(), yb.std()) + 0.3 * np.hypot(rg.mean(), yb.mean()))
    hsv = np.asarray(im.resize((320, max(1, round(320 * H / W)))).convert("HSV"), float) / 255
    fpal = None
    if frame:
        fhsv = np.asarray(Image.open(frame).convert("RGB").resize((320, 180)).convert("HSV"), float) / 255
        fpal = palette(fhsv)
    raw = open(path, "rb").read() if path and os.path.exists(path) else b""
    bw, bh = max(1, int(0.05 * W)), max(1, int(0.05 * H))
    band = np.concatenate([a[:bh].reshape(-1, 3), a[-bh:].reshape(-1, 3), a[:, :bw].reshape(-1, 3), a[:, -bw:].reshape(-1, 3)])
    bl = lab(band.mean(0)[None, None])[0, 0]
    sep = {m: float(np.linalg.norm(bl - lab(np.array([[c]], float))[0, 0])) for m, c in (("dark", DARK), ("light", LIGHT))}
    tw = sum((x1 - x0) * (y1 - y0) for _, (x0, y0, x1, y1), _, _ in lines)
    ttop = sum((x1 - x0) * (max(0, min(y1, H / 2) - y0)) for _, (x0, y0, x1, y1), _, _ in lines)
    sal_top = s[: s.shape[0] // 2].sum() / (s.sum() + 1e-9)
    bx, by = int(BADGE[0] * s.shape[1]), int(BADGE[1] * s.shape[0])
    red = a[-10:]
    return {"file": path, "profile": prof, "native": native, "text": [t for t, _, _, _ in lines], "read": read,
            "text_px": {k: round(max(l[2] for l in lines) * v / W, 1) if lines else None for k, v in views},
            "head_read": bool(given) or (max(lines, key=lambda l: l[2])[3] if lines else False),
            "fine": [(t, round(float(h) * lv / W, 1)) for t, _, h, r in lines if r and h * lv / W < 6],
            "words": words, "contrast": round(contr[max(range(len(lines)), key=lambda i: lines[i][2])], 2) if contr else None,
            "subject": round(float(subj), 3), "focal": len(regs), "clutter": round(clutter, 3), "pop": round(pop, 1),
            "ui_sep": {k: round(v, 1) for k, v in sep.items()},
            "tv_top": round(float((sal_top + ttop / tw) / 2) if tw else float(sal_top), 3),
            "badge_text": [t for t, (x0, y0, x1, y1), _, _ in lines if x1 > BADGE[0] * W and y1 > BADGE[1] * H],
            "badge_sal": round(float(max((r[by:, bx:].sum() / max(r.sum(), 1) for r in regs[:3]), default=0)), 3),
            "edge_text": [t for t, (x0, y0, x1, y1), _, _ in lines if x0 < 0.012 * W or y0 < 0.012 * H or x1 > 0.988 * W or y1 > 0.988 * H],
            "overlap": [(lines[i][0], lines[j][0]) for i in range(len(lines)) for j in range(i + 1, len(lines))
                        if min(lines[i][1][2], lines[j][1][2]) - max(lines[i][1][0], lines[j][1][0]) > 4
                        and min(lines[i][1][3], lines[j][1][3]) - max(lines[i][1][1], lines[j][1][1]) > 0.3 * min(lines[i][2], lines[j][2])],
            "red_bar": bool((((red[..., 0] > 180) & (red[..., 1] < 70) & (red[..., 2] < 70)).mean(1) > 0.25).any()),
            "title": title, "numbers_ok": numbers_ok,
            "oversat": round(float(((hsv[..., 1] > 0.9) & (hsv[..., 2] > 0.3)).mean()), 3),
            "palette": palette(hsv), "frame_palette": fpal,
            "provenance": sorted({k for k in PROV if k.lower().encode() in raw.lower()}), "dhash": dhash(im)}


def score(v, pair):
    lo, hi = pair
    return max(0.0, min(10.0, round(3 + 7 * (v - lo) / (hi - lo), 1)))


def rows(m):
    P = PROFILES[m["profile"]]
    T = dict(BASE, words=P["words"], text_px=P["head"])
    (sn, _), (ln, _) = list(P["views"].items())[0], list(P["views"].items())[-1]
    out = []

    def pix(key, v, detail):
        sc = score(v, T[key])
        lo, hi = T[key]
        bad = v < lo if hi > lo else v >= lo
        st = ("FAIL" if key in HARD else "WARN") if bad else ("WARN" if sc < 7 else "PASS")
        out.append((key, st, sc, detail))

    if m["text"]:
        pix("text_px", m["text_px"][sn], f"headline {m['text_px'][sn]} px tall at the {sn} view, {m['text_px'][ln]} px at "
            f"{ln} (floor {T['text_px'][0]}, good {T['text_px'][1]}): {m['text']}")
        if not m["head_read"] and out[-1][1] == "FAIL":
            out[-1] = (out[-1][0], "WARN", out[-1][2], out[-1][3] + " (unread: texture or unreadable text; --words decides)")
        if m["fine"]:
            out[-1] = (out[-1][0], "WARN" if out[-1][1] == "PASS" else out[-1][1], min(out[-1][2], 6.0),
                       out[-1][3] + f"; fine print under 6 px at the {ln} view (nobody reads it): {m['fine']}")
        pix("contrast", m["contrast"], f"headline {m['contrast']}:1 glyph vs background (floor {T['contrast'][0]}, good {T['contrast'][1]})")
    else:
        out.append(("text_px", "PASS", 10.0, "no text (a valid design when the picture carries it)"))
    pix("words", m["words"], f"{m['words']} words on the frame (<= {T['words'][1]} target, {T['words'][0]}+ = a wall)")
    pix("subject", m["subject"], f"largest salient region = {m['subject']:.0%} of the height (a proxy; >= 35% reads as a subject)")
    pix("focal", m["focal"], f"{m['focal']} salient regions >= 2% of the frame (one story: 1-3)")
    pix("clutter", m["clutter"], f"{m['clutter']:.0%} of pixels on a strong edge at the {ln} view")
    pix("pop", m["pop"], f"colourfulness {m['pop']} at the {sn} view")
    if m["oversat"] > 0.25:
        out[-1] = ("pop", "WARN", min(out[-1][2], 6.0), out[-1][3] + f"; {m['oversat']:.0%} of pixels at HSV S > 0.9: the "
                   "oversaturated AI gloss; grade to the real source colours")
    if P["thumb"]:
        w_ = min(m["ui_sep"], key=m["ui_sep"].get)
        pix("ui_sep", m["ui_sep"][w_], f"outer band vs the feed: dark {m['ui_sep']['dark']}, light {m['ui_sep']['light']} delta-E (worst: {w_})")
        pix("tv_top", m["tv_top"], f"{m['tv_top']:.0%} of saliency + text in the top half (the TV app shows it first)")
        if m["badge_text"]:
            out.append(("badge", "FAIL", 0.0, f"text under the duration badge: {m['badge_text']}"))
        elif m["badge_sal"] > 0.15:
            out.append(("badge", "WARN", 5.0, f"{m['badge_sal']:.0%} of a main subject under the duration badge"))
        else:
            out.append(("badge", "PASS", 10.0, "duration badge corner clear"))
    lay = [f"clipped by the frame edge: {m['edge_text']}"] * bool(m["edge_text"]) + [f"text on text: {m['overlap']}"] * bool(m["overlap"])
    out.append(("layout", "WARN" if lay else "PASS", 5.0 if lay else 10.0, "; ".join(lay) or "no clipped or overlapping text"))
    txt = m["read"] or ""
    if P["thumb"] and m["title"] and txt:
        try:
            sys.path.insert(0, TITLE_PY)
            import title as TI
            dup = [d for k, d in TI.check(m["title"], txt)["issues"] if k == "duplicate"]
            out.append(("title_dup", "FAIL" if dup else "PASS", 0.0 if dup else 10.0, dup[0] if dup else "the words add to the title"))
        except Exception as e:  # noqa: BLE001  the creator plugin may not be installed beside this one
            out.append(("title_dup", "WARN", 6.0, f"title check unavailable ({type(e).__name__}); compare by hand"))
    slop = []
    if DASH.search(txt):
        slop.append(("FAIL", "an em or en dash in the text"))
    low = " " + re.sub(r"[^a-z0-9' -]", " ", txt.lower()) + " "
    hit = [w for w in banned_words() if f" {w} " in low]
    if hit:
        slop.append(("FAIL", f"banned words {hit} (tells.md)"))
    if P["thumb"]:
        fake = FAKE_UI.findall(txt) + (["a red progress bar along the bottom"] if m["red_bar"] else [])
        if fake:
            slop.append(("FAIL", f"fake platform UI {fake}: never re-draw the feed's own chrome"))
    nums = [n.strip() for n in NUM.findall(txt) if re.search(r"\d", n)]
    if nums and not m["numbers_ok"]:
        slop.append(("WARN", f"numbers {nums}: say where each is true with --numbers-ok (an invented number is what people catch)"))
    if m["provenance"]:
        slop.append(("WARN", f"AI provenance in the file {m['provenance']}: platforms may label it; log which element is AI, never strip it"))
    fp, p_ = m["frame_palette"], m["palette"]
    if fp and ((p_["teal_orange"] > 0.6 and fp["teal_orange"] < p_["teal_orange"] / 2) or (p_["purple"] > 0.25 and fp["purple"] < p_["purple"] / 2)):
        slop.append(("WARN", f"the AI palette: this {p_} vs the source {fp}; take the colours from the real source"))
    near = [(os.path.basename(h), d) for h, d in m.get("near", []) if d < 10]
    if near:
        slop.append(("WARN", f"looks like {near} (dHash < 10 of 64): same template; change the layout, not the shade"))
    st = "FAIL" if any(s == "FAIL" for s, _ in slop) else "WARN" if slop else "PASS"
    out.append(("slop", st, {"FAIL": 0.0, "WARN": 6.0, "PASS": 10.0}[st], "; ".join(d for _, d in slop) or
                (f"numbers sourced: {m['numbers_ok']}" if nums else "no dash, banned word, fake UI or unsourced number")))
    return out


def overall(rs):
    o = round(sum(s for _, _, s, _ in rs) / len(rs), 1)
    return min(o, 4.9) if any(st == "FAIL" for _, st, _, _ in rs) else o


def mock(ours, theirs, prof, out):
    """Ours shuffled among the --vs pieces at the profile's largest view, dark and light grounds side by side; the key is
    printed, never drawn (a blind reader gets the sheet only)."""
    import random
    from PIL import Image, ImageDraw
    cards = [(p, True) for p in ours] + [(p, False) for p in theirs]
    random.Random("|".join(map(os.path.basename, ours))).shuffle(cards)
    lv = list(PROFILES[prof]["views"].values())[-1]
    ims = []
    for p, _ in cards:
        im = Image.open(p).convert("RGB")
        ims.append(im.resize((lv, max(1, round(lv * im.height / im.width))), Image.LANCZOS))
    cols, g = 3, 12
    ch = max(i.height for i in ims)
    rws = -(-len(ims) // cols)
    pw, ph = g + cols * (lv + g), g + rws * (ch + g)
    sheet = Image.new("RGB", (pw * 2, ph))
    for mi, bg in enumerate((DARK, LIGHT)):
        pane = Image.new("RGB", (pw, ph), bg)
        d = ImageDraw.Draw(pane)
        for i, im in enumerate(ims):
            x, y = g + (i % cols) * (lv + g), g + (i // cols) * (ch + g)
            pane.paste(im, (x, y))
            d.text((x + 4, y + 2), str(i + 1), fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
        sheet.paste(pane, (mi * pw, 0))
    sheet.save(out)
    key = [i + 1 for i, (_, o) in enumerate(cards) if o]
    print(out)
    print(f"key (keep from a blind reader): ours = {key} of {len(cards)}")
    return key


def check(path, prof, title=None, numbers_ok=None, given=None, frame=None, budget=None, vs=()):
    """(rows, overall, raw metrics) for one file; animations add their rows."""
    from PIL import Image
    anim = None
    im = None
    if path.lower().endswith(ANIM_EXT):
        small, durs, im, rest = load_frames(path)
        if len(small) > 1:
            anim = anim_measure(small, durs, path, budget)
            anim["rest_frame"] = rest
    m = measure(path, prof, title, numbers_ok, given, frame, im)
    m["near"] = [(v, bin(m["dhash"] ^ dhash(canvas(Image.open(v), prof))).count("1")) for v in vs]
    rs = rows(m) + (anim_rows(anim) if anim else [])
    m["anim"] = anim
    return rs, overall(rs), m


def selftest():
    import tempfile
    from PIL import Image, ImageDraw, ImageFont
    font = next((f for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/arialbd.ttf",
                             "/System/Library/Fonts/Supplemental/Arial Bold.ttf") if os.path.exists(f)), None)
    F = (lambda s: ImageFont.truetype(font, s)) if font else (lambda s: ImageFont.load_default(s))
    tmp = tempfile.mkdtemp()

    def card(name, texts, bg=(30, 60, 110), size=(1280, 720)):
        im = Image.new("RGB", size, bg)
        d = ImageDraw.Draw(im)
        w, h = size
        d.ellipse((w * 0.3, h * 0.17, w * 0.7, h * 0.89), fill=(250, 200, 40))
        for s, xy, sz in texts:
            d.text(xy, s, font=F(sz), fill=(255, 255, 255), stroke_width=max(3, sz // 18), stroke_fill=(20, 20, 20))
        p = os.path.join(tmp, name + ".png")
        im.save(p)
        return p

    def res(p, prof="thumbnail", **kw):
        rs, o, _ = check(p, prof, **kw)
        return {r: st for r, st, _, _ in rs}, o

    good, og = res(card("good", [("HOLD UP", (60, 50), 150)]))
    assert good["text_px"] == "PASS" and good["contrast"] == "PASS" and good["badge"] == "PASS" and good["slop"] == "PASS" and og >= 6, (good, og)
    tiny, _ = res(card("tiny", [("hold up there", (60, 50), 26)]))
    assert tiny["text_px"] == "FAIL", tiny
    badge, ob = res(card("badge", [("HOLD", (60, 50), 150), ("oops", (1120, 640), 60)]))
    assert badge["badge"] == "FAIL" and ob <= 4.9, (badge, ob)
    fake, _ = res(card("fake", [("HOLD", (60, 50), 150), ("12:34", (560, 560), 110)]))
    assert fake["slop"] == "FAIL", fake
    wall, _ = res(card("wall", [("THIS IS WAY TOO MANY", (40, 40), 80), ("WORDS ON ONE CARD", (40, 180), 80),
                                ("NOBODY READS A WALL", (40, 320), 80), ("OF TEXT AT ALL", (40, 460), 80)]))
    assert wall["words"] == "FAIL", wall
    num, _ = res(card("num", [("+35,746", (60, 50), 150)]))
    assert num["slop"] == "WARN", num
    pm = card("prov", [("HOLD", (60, 50), 150)])
    open(pm, "ab").write(b"trainedAlgorithmicMedia")
    pv, _ = res(pm)
    assert pv["slop"] == "WARN", pv
    ban, _ = res(card("ban", [("UNLEASH", (60, 50), 150)]))
    assert ban["slop"] == "FAIL", ban
    # an ad (poster) profile: a portrait hiring card with a big headline passes; the same with only small type fails
    ad_ok, _ = res(card("ad_ok", [("NOW HIRING", (60, 80), 130), ("Line cook, cashier", (60, 1500), 60)], size=(1080, 1920)), "ad")
    assert ad_ok["text_px"] == "PASS" and "badge" not in ad_ok, ad_ok
    ad_bad, _ = res(card("ad_bad", [("now hiring apply inside", (60, 80), 22)], size=(1080, 1920)), "ad",
                    given="now hiring apply inside")
    assert ad_bad["text_px"] == "FAIL", ad_bad
    same, _ = res(card("s2", [("HOLD UP", (60, 50), 150)]), vs=[card("s1", [("HOLD UP", (60, 50), 150)])])
    assert same["slop"] == "WARN", same

    def gif(name, draw, n=24, ms=66):
        frames = []
        for i in range(n):
            im = Image.new("RGB", (600, 600), (40, 20, 15))
            d = ImageDraw.Draw(im)
            d.text((40, 40), "NOW HIRING", font=F(70), fill=(255, 240, 220), stroke_width=4, stroke_fill=(0, 0, 0))
            draw(d, i)
            frames.append(im)
        p = os.path.join(tmp, name + ".gif")
        frames[0].save(p, save_all=True, append_images=frames[1:], duration=ms, loop=0)
        return p
    import random
    rnd = random.Random(1)
    calm, _ = res(gif("calm", lambda d, i: d.ellipse((250 + i, 300, 350 + i, 400), fill=(200, 120, 60)), n=24), "ad", budget=10)
    assert calm["flash"] == "PASS" and calm["particles"] == "PASS" and calm["size"] == "PASS", calm
    embers, _ = res(gif("embers", lambda d, i: [d.ellipse((x, y, x + 4, y + 4), fill=(255, 140, 40))
                                                for x, y in ((rnd.randrange(600), rnd.randrange(150, 600)) for _ in range(80))]), "ad")
    assert embers["particles"] == "WARN", embers
    strobe, _ = res(gif("strobe", lambda d, i: d.rectangle((0, 150, 600, 600), fill=(255, 255, 255) if i % 2 else (0, 0, 0)),
                        n=30, ms=100), "ad")
    assert strobe["flash"] == "FAIL", strobe
    key = mock([card("m1", [("HOLD", (60, 50), 150)])], [card("t1", [], bg=(200, 200, 200))] * 3, "thumbnail",
               os.path.join(tmp, "mock.png"))
    assert len(key) == 1
    print("PASS  still_check --selftest: a clean card passes; tiny text, badge text, fake UI, a word wall and a banned word "
          "fail; unsourced numbers, AI provenance and sameness warn; the ad profile reads a portrait poster; a calm loop "
          "passes, an ember field warns and a strobe fails; the line-up mock builds")


def main():
    deps()
    a = sys.argv[1:]
    if "--selftest" in a:
        return selftest()

    def opt(k):
        if k not in a:
            return None
        i = a.index(k)
        v = a[i + 1]
        del a[i:i + 2]
        return v
    prof = opt("--as") or "thumbnail"
    if prof not in PROFILES:
        sys.exit(f"still_check.py: --as one of {', '.join(PROFILES)}")
    title, nums, out, given, frame, budget = (opt("--title"), opt("--numbers-ok"), opt("--mock"), opt("--words"),
                                              opt("--frame"), opt("--budget-mb"))
    budget = float(budget) if budget else (10.0 if prof == "ad" else None)
    as_json = "--json" in a
    vs = []
    if "--vs" in a:
        i = a.index("--vs")
        j = next((k for k in range(i + 1, len(a)) if a[k].startswith("--")), len(a))
        vs = a[i + 1:j]
        del a[i:j]
    paths = [p for p in a if not p.startswith("--")]
    if not paths:
        sys.exit(__doc__.split("Rows")[0])
    for p in paths + vs:
        if not os.path.exists(p):
            sys.exit(f"still_check.py: no such file {p}")
    bad = False
    print(f"profile {prof}: {PROFILES[prof]['what']}")
    for p in paths:
        rs, o, m = check(p, prof, title, nums, given, frame, budget, [v for v in vs + paths if v != p])
        if as_json:
            print(json.dumps(m, default=str))
            continue
        print(f"== {os.path.basename(p)}  overall {o}/10" + (f"  (rest frame {m['anim']['rest_frame']} of {m['anim']['frames']})" if m["anim"] else ""))
        for r, st, sc, d in rs:
            print(f"{st:4}  {r:10} {sc:4.1f}  {d}")
        bad = bad or any(st == "FAIL" for _, st, _, _ in rs)
    if out:
        if not vs:
            sys.exit("still_check.py --mock needs --vs <their pieces>")
        mock(paths, vs[:6], prof, out)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
