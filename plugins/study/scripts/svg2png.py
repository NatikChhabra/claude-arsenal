"""Render SVG files to PNG so a diagram can be looked at before it ships (PyMuPDF).

    python svg2png.py "Study/Backend/Media/diagrams/*.svg" [--out DIR] [--scale 1.6]

Default output folder: the system temp folder.
"""
import argparse
import glob
import os
import tempfile

import fitz

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("svgs", nargs="+", help="files or glob patterns")
ap.add_argument("--out", default=tempfile.gettempdir())
ap.add_argument("--scale", type=float, default=1.6)
a = ap.parse_args()

os.makedirs(a.out, exist_ok=True)
bad = 0
for p in [p for pat in a.svgs for p in (glob.glob(pat) or [pat])]:
    try:
        pix = fitz.open(p).load_page(0).get_pixmap(matrix=fitz.Matrix(a.scale, a.scale), alpha=False)
        dest = os.path.join(a.out, os.path.splitext(os.path.basename(p))[0] + ".png")
        pix.save(dest)
        print("PNG " + dest)
    except Exception as e:  # noqa: BLE001 - report every file, keep going
        bad += 1
        print("ERR " + p + " " + repr(e))
raise SystemExit(1 if bad else 0)
