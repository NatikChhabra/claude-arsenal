"""Heading outline (## and ###) of every note, for choosing diagram anchors.

    python outline.py [subject-or-path-fragment] [--config study.json]

[M] marks a note that already has a mermaid mind map.
"""
import argparse
import io
import os
import re

import studycfg

ap = studycfg.config_arg(argparse.ArgumentParser(description=__doc__.splitlines()[0]))
ap.add_argument("filter", nargs="?", default="")
a = ap.parse_args()
studycfg.utf8()
root = studycfg.load(a.config)["notes"]

for dp, _d, fs in sorted(os.walk(root)):
    for fn in sorted(fs):
        p = os.path.join(dp, fn).replace("\\", "/")
        if not fn.endswith(".md") or a.filter not in p:
            continue
        lines = io.open(p, encoding="utf-8").read().split("\n")
        mm = "M" if any(ln.startswith("```mermaid") for ln in lines) else "-"
        print("\n### [%s] %s  (%d lines)" % (mm, p[len(root) + 1:], len(lines)))
        code = False
        for ln in lines:
            if ln.startswith("```"):
                code = not code
            elif not code and re.match(r"^#{2,3} ", ln):
                print("  " + ln[:120])
