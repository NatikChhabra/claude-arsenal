"""Markdown file -> printable A4 PDF (markdown + PyMuPDF Story), for copy-ready write-ups.

    python md2pdf.py <file.md> [--out file.pdf]

A line "<!-- pagebreak -->" starts a new page. Tables are supported.
"""
import argparse
import os

ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
ap.add_argument("src")
ap.add_argument("--out", help="default: <src>.pdf next to it")
a = ap.parse_args()

import fitz  # noqa: E402  (after parse_args so --help works without the deps)
import markdown  # noqa: E402

parts = [markdown.markdown(p, extensions=["tables"])
         for p in open(a.src, encoding="utf-8").read().split("<!-- pagebreak -->")]
css = """
body { font-family: sans-serif; font-size: 11pt; line-height: 1.35; }
h1 { font-size: 18pt; text-align: center; margin-bottom: 2pt; }
h2 { font-size: 14pt; text-align: center; margin-top: 0; }
h3 { font-size: 12pt; margin-top: 10pt; margin-bottom: 3pt; text-decoration: underline; }
table { border-collapse: collapse; margin: 4pt 0; width: 100%; }
td, th { border: 0.6pt solid #444; padding: 2pt 5pt; font-size: 10pt; text-align: center; }
li { margin-bottom: 1pt; }
"""
out = a.out or os.path.splitext(a.src)[0] + ".pdf"
writer = fitz.DocumentWriter(out)
page = fitz.paper_rect("a4")
where = page + (50, 50, -50, -50)
for html in parts:
    story = fitz.Story(html=html, user_css=css)
    more = True
    while more:
        dev = writer.begin_page(page)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
writer.close()
print(out, fitz.open(out).page_count, "pages")
