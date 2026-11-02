"""Dump the text layer of a PDF page range (1-based, inclusive).

    python pdfpage.py <file.pdf> <first> [last]
"""
import argparse

import fitz

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("pdf")
ap.add_argument("first", type=int)
ap.add_argument("last", type=int, nargs="?")
a = ap.parse_args()

doc = fitz.open(a.pdf)
for pno in range(a.first, min(a.last or a.first, doc.page_count) + 1):
    print("========== PAGE %d ==========" % pno)
    print(doc[pno - 1].get_text())
