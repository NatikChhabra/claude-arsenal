# -*- coding: utf-8 -*-
"""Cache each chapter's textbook PDF as plain text: <deck.cache>/<Subject>/<stem>.txt.
Drafting and checking agents read these, never the PDF. Run from the vault root.

    python deck_text.py --subject "Political Science" [--config study.json]
"""
import os
import re

import fitz

import decklib

a, _cfg, d = decklib.args(__doc__.splitlines()[0])
strip = decklib.subject_cfg(d, a.subject).get("strip_text", d.get("strip_text", []))
bad = 0
for ch in decklib.chapters(d, a.subject):
    if not ch["pdf"]:
        bad += 1
        print("NO PDF for", ch["label"], ": fix the pdf name or source_dirs in study.json")
        continue
    doc = fitz.open(ch["pdf"])
    t = "\n".join(pg.get_text() for pg in doc)
    for junk in strip:
        t = t.replace(junk, "")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"(?<![.:?!\n])\n(?=[a-z(,])", " ", t)       # re-join lines broken mid-sentence
    os.makedirs(os.path.dirname(ch["text"]), exist_ok=True)
    open(ch["text"], "w", encoding="utf-8").write(t)
    print(ch["stem"], len(doc), "pages", len(t), "chars")
raise SystemExit(1 if bad else 0)
