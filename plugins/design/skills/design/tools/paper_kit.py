"""paper_kit.py - physical print textures for ads and posters that must look made, not generated.

Builds the layers for the "sheet on a wall" vernacular (ads.md section 8): a sheet of paper with a torn top edge,
tooth, fibres, a fold and grease stains; masking tape strips; and a rubber-stamp ink mask whose voids follow paper
tooth and an uneven hand pressure instead of a sprayed-on grunge overlay. Deterministic per --seed, so a redraw of the
same poster keeps the same paper.

    python paper_kit.py sheet OUT.png [--paper butcher|kraft|newsprint|bone] [--size 880x940] [--stains 2] [--seed 11]
    python paper_kit.py tape OUT.png [--size 190x58] [--seed 11]
    python paper_kit.py stamp OUT.png [--size 1400x420] [--voids 0.09] [--seed 5]
    python paper_kit.py mark OUT.png --text "OWNER NAME" [--size 1080x1080] [--angle -24] [--opacity .2] [--font F.ttf]
    python paper_kit.py --selftest

Use in HTML (render to PNG/GIF in headless Chrome as decks.md says):
  sheet as the background of a rotated div with a two-layer drop-shadow (contact + soft);
  printed brand art and type on it with mix-blend-mode: multiply, then the SAME sheet again on top at
  mix-blend-mode: soft-light, opacity ~0.75, so stains, fold and tooth run across the ink;
  stamp text as a CSS mask (inline it as a data: URI, a file:// mask is blocked by Chrome), mask-size 100% 100%;
  tape above everything at opacity ~0.9.
mark: a sample watermark, the owner's name tiled diagonally over the whole frame in a light fill with a dark stroke, so
  it shows on dark and light ground alike. Overlay it last; for a loop, drift it one tile per loop (ads.md section 8).
Needs numpy, pillow, scipy (re-runs itself under uv when they are missing).
"""
import argparse
import os
import subprocess
import sys

try:
    import numpy as np
    from PIL import Image, ImageDraw, ImageFilter
    from scipy import ndimage
except ImportError:  # same pattern as still_check.py
    if os.environ.get("PAPER_KIT_UV"):
        sys.exit("paper_kit: numpy, pillow and scipy are required")
    env = dict(os.environ, PAPER_KIT_UV="1")
    cmd = ["uv", "run", "--no-project", "--with", "numpy", "--with", "pillow", "--with", "scipy", "python", __file__]
    sys.exit(subprocess.call(cmd + sys.argv[1:], env=env))

PAPERS = {  # base RGB sampled from real stock, photographed in daylight
    "butcher": (214, 176, 142),   # peach / pink BBQ butcher paper
    "kraft": (190, 150, 106),
    "newsprint": (222, 216, 198),
    "bone": (232, 226, 210),
}


def _noise(rng, w, h, scale, amp):
    n = rng.standard_normal((h // scale + 2, w // scale + 2))
    n = ((n - n.min()) / (np.ptp(n) or 1) * 255).astype(np.uint8)
    a = np.asarray(Image.fromarray(n).resize((w, h), Image.BICUBIC)).astype(float) / 255 - 0.5
    return a * amp


def sheet(w=880, h=940, paper="butcher", stains=2, seed=11):
    rng = np.random.default_rng(seed)
    base = np.array(PAPERS[paper], float)
    tone = sum(_noise(rng, w, h, s, a) for s, a in ((180, .10), (60, .06), (12, .035), (3, .03), (1, .025)))
    img = np.ones((h, w, 3)) * base * (1 + tone[..., None])
    fib = Image.new("L", (w, h), 128)
    d = ImageDraw.Draw(fib)
    for _ in range(int(w * h / 750)):  # short fibres, low contrast: a hairy sheet reads fake
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        L, a = rng.uniform(6, 26), rng.normal(0.15, 0.5)
        d.line([(x, y), (x + L * np.cos(a), y + L * np.sin(a))],
               fill=int(128 + rng.choice([-1, 1]) * rng.uniform(5, 12)), width=1)
    fib = np.asarray(fib.filter(ImageFilter.GaussianBlur(.6))).astype(float) / 128 - 1
    img *= 1 + fib[..., None] * 0.35
    yy, xx = np.mgrid[0:h, 0:w]
    # grease stains: irregular lobed outlines with a darker tide line, warmer than the paper (never grey circles)
    spots = [(0.15, 0.9, 70, .16), (0.86, 0.16, 44, .12), (0.19, 0.85, 34, .10), (0.89, 0.2, 22, .09)][:max(0, stains) * 2]
    for fx, fy, r, s in spots:
        cx, cy = fx * w, fy * h
        ang = np.arctan2(yy - cy, xx - cx)
        dist = np.sqrt((xx - cx) ** 2 + ((yy - cy) * 1.35) ** 2)
        wob = _noise(rng, w, h, 25, 1.0) * 70 + r * .22 * np.sin(3 * ang + cx) + r * .12 * np.sin(5 * ang + cy)
        m = np.clip((r + wob - dist) / 18, 0, 1)
        edge = np.clip(1 - abs(r + wob - dist) / 6, 0, 1) * .5
        k = (m * s + edge * s * .7)[..., None]
        img *= 1 - k * np.array([0.9, 1.25, 1.7])
    # one soft fold across the sheet
    x0, y0, x1, y1 = 0, int(h * .5), w, int(h * .485)
    p = np.abs((y1 - y0) * xx - (x1 - x0) * yy + x1 * y0 - y1 * x0) / np.hypot(y1 - y0, x1 - x0)
    img *= (1 + .05 * np.exp(-(p / 2.0) ** 2) - .04 * np.exp(-((p - 4) / 4) ** 2))[..., None]
    # torn top edge (torn off a roll), with the lighter torn fibres showing
    xs = np.arange(w)
    tear = 16 + 5 * np.sin(xs / 37.0 + 1) + 3 * np.sin(xs / 11.3) + \
        ndimage.gaussian_filter1d(rng.normal(0, 3, w), 1.5) + rng.normal(0, .9, w)
    tear = np.clip(tear, 4, 32)
    alpha = np.ones((h, w))
    alpha[yy < tear[None, :]] = 0
    torn = (yy >= tear) & (yy < tear + 3 + rng.random((h, w)) * 3)
    img[torn] = img[torn] * .4 + np.array([240, 226, 210]) * .6
    alpha[:, :2] = 0
    alpha[:, -2:] = 0
    alpha[-2:, :] = 0
    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).convert("RGBA")
    out.putalpha(Image.fromarray((alpha * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.7)))
    return out


def tape(w=190, h=58, seed=11):
    rng = np.random.default_rng(seed)
    t = np.ones((h, w, 3)) * np.array([226, 214, 180]) * (1 + _noise(rng, w, h, 8, .05)[..., None] +
                                                          _noise(rng, w, h, 2, .04)[..., None])
    a = np.ones((h, w)) * .82
    for side in (0, 1):  # torn, not cut, ends
        z = np.clip(np.cumsum(rng.normal(0, 1.5, h)) + 8, 2, 14).astype(int)
        for r in range(h):
            if side == 0:
                a[r, :z[r]] = 0
            else:
                a[r, w - z[r]:] = 0
    out = Image.fromarray(np.clip(t, 0, 255).astype(np.uint8)).convert("RGBA")
    out.putalpha(Image.fromarray((a * 255).astype(np.uint8)))
    return out


def stamp(w=1400, h=420, voids=0.09, seed=5):
    """White RGBA whose alpha is the ink: solid where pressed, voids where paper tooth or a fibre skipped the ink,
    lighter toward the bottom-left as if the stamp was rocked. No blurred blobs and no even speckle."""
    rng = np.random.default_rng(seed)
    tooth = ndimage.gaussian_filter(rng.standard_normal((h, w)), .9)
    tooth = (tooth - tooth.mean()) / tooth.std()
    mid = ndimage.gaussian_filter(rng.standard_normal((h, w)), 6)
    mid = (mid - mid.mean()) / mid.std()
    xs, ys = np.linspace(0, 1, w)[None, :], np.linspace(0, 1, h)[:, None]
    pressure = .55 + .27 * xs + .25 * (1 - ys)
    thr = 1.15 + (pressure - .8) * 2.2 + mid * .35
    hole = tooth > thr
    st = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(st)
    for _ in range(int(w * h / 2260)):
        x, y = rng.uniform(0, w), rng.uniform(0, h)
        L, a = rng.uniform(8, 30), rng.normal(.1, .6)
        d.line([(x, y), (x + L * np.cos(a), y + L * np.sin(a))], fill=255, width=1)
    hole |= np.asarray(st) > 0
    # thin the voids down to the target share, deterministically
    share = hole.mean()
    if share > voids:
        keep = rng.random((h, w)) < voids / share
        hole &= keep
    ink = np.where(hole, .08, np.clip(.82 + .07 * mid + (pressure - .8) * .4, .6, 1))
    a = Image.fromarray((ink * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.5))
    o = np.zeros((h, w, 4), np.uint8)
    o[..., :3] = 255
    o[..., 3] = np.asarray(a)
    return Image.fromarray(o)


def mark(w=1080, h=1080, text="SAMPLE", angle=-24.0, opacity=0.2, font=None, size=34, gap=112):
    """Tiled diagonal watermark: white text at `opacity` with a dark stroke, rows offset by half a tile so no clean
    column survives, rotated, cropped to w x h. Covers every region, so cropping or cloning one corner can't remove it."""
    from PIL import ImageFont
    try:
        f = ImageFont.truetype(font, size) if font else ImageFont.load_default(size)
    except (OSError, TypeError):
        f = ImageFont.load_default()
    label = "  ".join(text.upper())  # letter-spaced reads as a mark, not as copy
    tw = int(ImageDraw.Draw(Image.new("L", (1, 1))).textlength(label, font=f)) + size * 4
    side = int(np.hypot(w, h)) + tw * 2
    tile = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    fill, stroke = (255, 255, 255, int(255 * opacity)), (0, 0, 0, int(255 * opacity))
    for r, y in enumerate(range(0, side, gap)):
        for x in range(-tw + (r % 2) * tw // 2, side, tw):
            d.text((x, y), label, font=f, fill=fill, stroke_width=1, stroke_fill=stroke)
    tile = tile.rotate(-angle, resample=Image.BICUBIC)
    x0, y0 = (side - w) // 2, (side - h) // 2
    return tile.crop((x0, y0, x0 + w, y0 + h))


def _size(s):
    w, h = s.lower().split("x")
    return int(w), int(h)


def selftest():
    s = sheet(220, 240, seed=1)
    a = np.asarray(s)
    assert a.shape == (240, 220, 4)
    assert a[0, :, 3].max() == 0, "top row must be torn away"
    assert a[120, 110, 3] == 255, "middle of the sheet must be opaque"
    assert np.asarray(sheet(220, 240, seed=1)).tobytes() == a.tobytes(), "same seed, same sheet"
    body = a[60:200, 20:200, :3].reshape(-1, 3).astype(float)
    assert 5 < body.std(0).mean() < 40, "paper needs visible but quiet texture"
    m = np.asarray(stamp(400, 120, voids=.09, seed=2))[..., 3]
    hole = (m < 60).mean()
    assert .03 < hole < .14, f"stamp voids {hole:.3f} outside 3-14%"
    assert m.mean() > 150, "stamp must read as solid ink at a glance"
    t = np.asarray(tape(120, 40, seed=3))[..., 3]
    assert t[:, 0].max() == 0 and t[20, 60] > 150, "tape ends torn, middle opaque"
    wm = np.asarray(mark(300, 200, "TEST NAME", opacity=.2))[..., 3]
    assert wm.shape == (200, 300), "mark crops to the asked size"
    cells = [wm[y:y + 100, x:x + 100].max() for y in (0, 100) for x in (0, 100, 200)]
    assert min(cells) > 0, "mark must reach every region of the frame"
    assert wm.max() <= 255 * .25 and (wm > 0).mean() < .35, "mark stays a light layer"
    print("PASS  paper_kit --selftest: torn sheet, deterministic texture, stamp voids 3-14%, torn tape ends, "
          "watermark covers every region")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("what", nargs="?", choices=["sheet", "tape", "stamp", "mark"])
    ap.add_argument("out", nargs="?")
    ap.add_argument("--paper", default="butcher", choices=sorted(PAPERS))
    ap.add_argument("--size")
    ap.add_argument("--stains", type=int, default=2)
    ap.add_argument("--voids", type=float, default=.09)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--text", default="SAMPLE")
    ap.add_argument("--angle", type=float, default=-24.0)
    ap.add_argument("--opacity", type=float, default=.2)
    ap.add_argument("--font")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.what or not a.out:
        ap.error("give sheet|tape|stamp|mark and an output path, or --selftest")
    if a.what == "sheet":
        w, h = _size(a.size or "880x940")
        img = sheet(w, h, a.paper, a.stains, 11 if a.seed is None else a.seed)
    elif a.what == "tape":
        w, h = _size(a.size or "190x58")
        img = tape(w, h, 11 if a.seed is None else a.seed)
    elif a.what == "mark":
        w, h = _size(a.size or "1080x1080")
        img = mark(w, h, a.text, a.angle, a.opacity, a.font)
    else:
        w, h = _size(a.size or "1400x420")
        img = stamp(w, h, a.voids, 5 if a.seed is None else a.seed)
    img.save(a.out)
    print(f"wrote {a.out} ({w}x{h})")


if __name__ == "__main__":
    main()
