"""lut.py - bake our own .cube LUTs (no stock LUTs: zero spend, nothing licence-bound) for an ffmpeg grade.

    python lut.py [look ...] [--out DIR]       # default: every look -> DIR/<look>.cube (DIR default ./luts)
    python lut.py --selftest
    use:  ffmpeg -i in.mp4 -vf "lut3d=file=luts/film.cube:interp=tetrahedral" ...

What a LUT does that an eq grade can't: eq contrast is a straight line around mid-grey, so a lifted contrast clips the
sky, the snow and the shadows flat. These looks are an S-curve on LUMINANCE (hue kept: RGB scaled by f(Y)/Y) whose slope
falls to (1 - s) at both ends: a film toe and a highlight shoulder, the same mid-tone contrast with bright and dark
detail kept. Bright colours roll toward white (film's highlight desaturation) instead of going neon, and a split tone
tints shadows and highlights. Built for game footage, music videos and phone clips; judge the result on the real
footage beside the ungraded frame (design references/edit.md, film look), never on a test chart.
"""
import os, sys, tempfile

N = 17                                     # 17^3 grid: the curves are smooth, tetrahedral error < 1/4 of an 8-bit step
LR, LG, LB = 0.2126, 0.7152, 0.0722        # Rec.709 luma weights

# s: S strength (0 = none; ends slope 1 - s, mid-grey slope 1 + s/2); hl: highlight desaturation above Y 0.75 (0-1);
# shadow / high: split-tone RGB offsets at the dark / bright end (0.02 is already visible); sat: overall saturation
LOOKS = {
    "film": dict(s=0.35, hl=0.45, shadow=(-0.012, 0.0, 0.015), high=(0.012, 0.004, -0.010), sat=0.96),
    "film_night": dict(s=0.30, hl=0.55, shadow=(-0.015, 0.0, 0.025), high=(0.004, 0.004, 0.0), sat=0.90),
    "warm_day": dict(s=0.25, hl=0.40, shadow=(0.0, -0.004, -0.010), high=(0.014, 0.006, -0.012), sat=1.0),
    "identity": dict(s=0.0, hl=0.0, shadow=(0, 0, 0), high=(0, 0, 0), sat=1.0),
}


def tone(y, s):
    return (1 - s) * y + s * y * y * (3 - 2 * y)


def look(r, g, b, s, hl, shadow, high, sat):
    y = LR * r + LG * g + LB * b
    k = tone(y, s) / y if y > 1e-6 else 1.0
    r, g, b = r * k, g * k, b * k
    y2 = LR * r + LG * g + LB * b
    d = sat * (1 - hl * max(0.0, (y2 - 0.75) / 0.25) ** 2)
    r, g, b = (y2 + (c - y2) * d for c in (r, g, b))
    ws, wh = (1 - y2) ** 2, y2 * y2
    return tuple(min(1.0, max(0.0, c + ws * sh + wh * hi)) for c, sh, hi in zip((r, g, b), shadow, high))


def bake(name, out_dir):
    p = os.path.join(out_dir, f"{name}.cube")
    os.makedirs(out_dir, exist_ok=True)
    rows = [f'TITLE "arsenal {name}"', f"LUT_3D_SIZE {N}"]
    for bi in range(N):                    # .cube order: red changes fastest
        for gi in range(N):
            for ri in range(N):
                rows.append("%.6f %.6f %.6f" % look(ri / (N - 1), gi / (N - 1), bi / (N - 1), **LOOKS[name]))
    with open(p, "w", newline="\n") as f:
        f.write("\n".join(rows) + "\n")
    return p


def selftest():
    assert all(abs(a - b) < 1e-9 for a, b in zip(look(0.3, 0.5, 0.7, **LOOKS["identity"]), (0.3, 0.5, 0.7)))
    f = LOOKS["film"]
    assert max(look(0, 0, 0, **f)) < 0.02                 # black stays black (a tiny tint)
    assert min(look(1, 1, 1, **f)) > 0.97                 # white stays white: nothing clips grey
    assert tone(0.95, f["s"]) - tone(0.9, f["s"]) < 0.05  # the shoulder: highlights compress
    assert tone(0.55, f["s"]) - tone(0.45, f["s"]) > 0.1  # the mid-tones gain contrast
    p = bake("film", tempfile.mkdtemp())
    lines = open(p).read().splitlines()
    assert lines[1] == f"LUT_3D_SIZE {N}" and len(lines) == 2 + N ** 3
    print(f"PASS  lut.py --selftest: identity is a no-op, black and white hold, shoulder compresses, mid-tones gain; a "
          f"{N}^3 .cube writes")


def main():
    a = sys.argv[1:]
    if "--selftest" in a:
        return selftest()
    out = "luts"
    if "--out" in a:
        i = a.index("--out")
        out = a[i + 1]
        del a[i:i + 2]
    for n in a or [k for k in LOOKS if k != "identity"]:
        if n not in LOOKS:
            sys.exit(f"unknown look '{n}' ({', '.join(LOOKS)})")
        print(bake(n, out))


if __name__ == "__main__":
    main()
