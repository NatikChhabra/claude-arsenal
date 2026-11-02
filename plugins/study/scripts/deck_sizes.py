# -*- coding: utf-8 -*-
"""How long is each card, by label? Finds the wall-of-text cards worth splitting.

    python deck_sizes.py                          # every subject with card files
    python deck_sizes.py --subject Psychology --worst 15
"""
import os
import re
from collections import defaultdict

import decklib

a, _cfg, d = decklib.args(__doc__.splitlines()[0], subject_required=False,
                          extra=[(("--worst",), {"type": int, "default": 0})])
root = d["cards"]
subjects = [a.subject] if a.subject else sorted(x for x in os.listdir(root) if os.path.isdir(os.path.join(root, x))) \
    if os.path.isdir(root) else []
if not subjects:
    raise SystemExit(f"no card folders under {root}")


def words(s):
    return len(re.sub(r"[*|_`>-]", " ", s or "").split())


for subj in subjects:
    by, rows = defaultdict(list), []
    for path in decklib.card_files(d, subj):
        for kind, f in decklib.parse(path)[1:]:
            label = (f.get("P") or kind).split("·")[0].strip().upper()
            back = words(f.get("S")) + words(f.get("B")) + words(f.get("W")) + words(f.get("Y"))
            items = len([ln for ln in (f.get("S") or "").split("\n") if ln.strip()])
            by[label].append((back, items))
            rows.append((back, items, label, os.path.basename(path)[:28], (f.get("Q") or f.get("A") or "")[:50]))
    print(f"\n== {subj}: {sum(len(v) for v in by.values())} cards")
    print(f"  {'label':26s} {'cards':>5s} {'avg words':>9s} {'max':>5s} {'avg lines':>9s}")
    for label, v in sorted(by.items(), key=lambda kv: -sum(x[0] for x in kv[1]) / len(kv[1])):
        print(f"  {label[:26]:26s} {len(v):5d} {sum(x[0] for x in v) / len(v):9.0f} {max(x[0] for x in v):5d}"
              f" {sum(x[1] for x in v) / len(v):9.1f}")
    for r in sorted(rows, reverse=True)[:a.worst]:
        print(f"    {r[0]:4d}w {r[1]:3d} lines  {r[2][:18]:18s} {r[3]}  {r[4]}")
