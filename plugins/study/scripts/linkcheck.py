#!/usr/bin/env python3
"""Vault link + structure checker. Run from the vault root.

Reports:
  * broken [[wikilinks]] (resolved by full path, path without .md, or bare basename, as Obsidian does)
  * attachment embeds (![[photo.jpg]], ![[chart.svg]]) resolved by bare filename
  * .md files nothing links to (orphans), excluding `link_roots`, `_`-prefixed files and skill files
  * skill files missing YAML frontmatter / name / description

Expected baseline: 0 broken, 0 orphans, 0 broken frontmatter. Any non-zero number is a real finding.
Template placeholders like [[Error Log/<Subject>.md]] are ignored (they are prose, not links).

    python linkcheck.py [--config study.json]
"""
import argparse
import io
import os
import re
import sys

import studycfg

LINK = re.compile(r"\[\[([^\]|#]+)")


def walk(skip):
    md, allfiles = [], set()
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            p = os.path.relpath(os.path.join(root, f), ".").replace(os.sep, "/")
            allfiles.add(p)
            if f.endswith(".md"):
                md.append(p)
    return md, allfiles


def is_skill(p):
    return "/skills/" in "/" + p and p.endswith("SKILL.md")


def main():
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Vault link + structure checker."))
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    md, allfiles = walk(set(cfg["skip_dirs"]))
    stems = {p[:-3] for p in allfiles if p.endswith(".md")}
    by_base = {}
    for p in allfiles:
        if p.endswith(".md"):
            by_base.setdefault(os.path.basename(p)[:-3], []).append(p)
    attach_names = {os.path.basename(p) for p in allfiles if not p.endswith(".md")}

    broken, linked = {}, set()
    for fp in md:
        try:
            s = io.open(fp, encoding="utf-8").read()
        except Exception as exc:  # noqa: BLE001
            print("UNREADABLE %s: %s" % (fp, exc))
            continue
        for m in LINK.finditer(s):
            target = m.group(1).strip()
            if not target:
                continue
            cand = target[:-3] if target.endswith(".md") else target
            base = os.path.basename(cand)
            if not target.endswith(".md") and "." in base and base in attach_names:
                continue
            if target in allfiles:
                linked.add(target)
            elif cand in stems:
                linked.add(cand + ".md")
            elif base in by_base:
                linked.update(by_base[base])
            else:
                broken.setdefault(target, set()).add(fp)

    placeholders = {t for t in broken if "<" in t or ">" in t}
    for t in placeholders:
        del broken[t]

    roots = set(cfg["link_roots"])
    orphans = [p for p in md if p not in linked and p not in roots
               and not os.path.basename(p).startswith("_") and not is_skill(p)]

    bad_skills = []
    for p in md:
        if is_skill(p):
            s = io.open(p, encoding="utf-8").read()
            head = s.split("---")[1] if s.startswith("---") else ""
            if "name:" not in head or "description:" not in head:
                bad_skills.append(p)

    print("markdown files : %d" % len(md))
    print("broken links   : %d   (expected 0; %d template placeholder(s) ignored)" % (len(broken), len(placeholders)))
    for t, srcs in sorted(broken.items()):
        print("  BROKEN  %s   <- %s" % (t, ", ".join(sorted(srcs)[:3])))
    print("orphan notes   : %d" % len(orphans))
    for p in sorted(orphans):
        print("  ORPHAN  %s" % p)
    print("skills checked : %d  (broken frontmatter: %d)" % (sum(map(is_skill, md)), len(bad_skills)))
    for p in bad_skills:
        print("  BAD SKILL  %s" % p)
    return 1 if (broken or bad_skills) else 0


if __name__ == "__main__":
    sys.exit(main())
