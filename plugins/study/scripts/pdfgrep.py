"""Find terms in a PDF's text layer: page number plus surrounding context per hit.

    python pdfgrep.py <file.pdf> <term> [term ...] [--context 700]

Reads the OCR/text layer, so it suits PRINTED text (textbooks, question papers).
Handwriting extracts as word salad; render pages to images instead (paper-intake skill).
"""
import argparse

import fitz

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("pdf")
ap.add_argument("terms", nargs="+")
ap.add_argument("--context", type=int, default=700, help="characters shown before each hit (after: +200)")
a = ap.parse_args()

doc = fitz.open(a.pdf)
terms = [t.lower() for t in a.terms]
for pno in range(doc.page_count):
    txt = doc[pno].get_text()
    low = txt.lower()
    for t in terms:
        i = low.find(t)
        if i < 0:
            continue
        while i >= 0:
            print("=== p%d [%s] ===" % (pno + 1, t))
            print(txt[max(0, i - a.context):i + a.context + 200].replace("\n", " "))
            print()
            i = low.find(t, i + len(t))
        break
