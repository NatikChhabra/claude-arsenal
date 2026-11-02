#!/usr/bin/env python3
"""visualize.py - insert photos and diagrams into chapter notes. Run from the vault root.

Plan file (JSON):
{
  "<Subject>/<Book>/<Chapter>.md": {           (path under the notes folder)
    "photos":   ["subj-photo-slug"],               (need an entry in <images>/_attribution.json)
    "summary":  ["subj-chapter-timeline"],         (svgkit slugs in <diagrams>/)
    "sections": {"## 3. Integration": ["subj-section-diagram"]}
  }
}

What it writes into each note:
  1. A "Visual summary" block right after the header's closing '---' rule
     (photos in a collapsible callout, summary diagrams full width below).
  2. Section diagrams directly under the heading whose text starts with the key.
  3. An "Image credits" section at the end, rebuilt from _attribution.json.

Idempotent: every block is fenced by %% markers and is replaced, not duplicated,
on re-run. Section embeds already present in the note are skipped.

Folders come from study.json (`notes`, `images`, `diagrams`; see studycfg.py).
_attribution.json maps photo slug -> {file, title, artist, license, url}; it is optional
(no photos without it).

Usage:
  python visualize.py plan.json --dry       (exit 1 on any missing heading/file; check before --write)
  python visualize.py plan.json --write
"""
import io
import json
import os
import re
import sys

import studycfg

NOTES = SVG_DIR = ATTR = None        # set from the vault config in main()

VS_START, VS_END = "%% visuals:start %%", "%% visuals:end %%"
CR_START, CR_END = "%% credits:start %%", "%% credits:end %%"


def load_attr():
    if not os.path.exists(ATTR):
        return {}
    with io.open(ATTR, encoding="utf-8") as f:
        return json.load(f)


def strip_block(lines, start, end):
    out, skipping = [], False
    for ln in lines:
        if ln.strip() == start:
            skipping = True
            continue
        if skipping and ln.strip() == end:
            skipping = False
            continue
        if not skipping:
            out.append(ln)
    return out


def trim_blank_runs(lines):
    out = []
    for ln in lines:
        if ln.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(ln)
    return out


def clean_artist(name):
    words = name.split()
    half = len(words) // 2
    if half and len(words) % 2 == 0 and words[:half] == words[half:]:
        words = words[:half]
    name = " ".join(words)
    if len(name) > 70:
        name = name[:67].rstrip() + "..."
    return name.replace("|", "/").replace("[", "(").replace("]", ")")


def summary_block(photos, diagrams, attr):
    b = [VS_START]
    if photos:
        b.append("> [!abstract]+ 🖼️ Picture it")
        for i, slug in enumerate(photos):
            a = attr[slug]
            if i:
                b.append(">")
            b.append("> ![[%s|560]]" % a["file"])
            b.append("> *%s*" % a["caption"].rstrip("."))
            b.append("> <small>Photo: %s · %s · [Wikimedia Commons](%s)</small>"
                     % (clean_artist(a["artist"]), a["licence"], a["commons_page"]))
        b.append("")
    for d in diagrams:
        b.append("![[%s.svg]]" % d)
        b.append("")
    if b[-1] == "":
        b.pop()
    b.append(VS_END)
    return b


def credits_block(photos, attr):
    b = [CR_START, "## Image credits", ""]
    b.append("Photos from Wikimedia Commons, used under the licence shown. "
             "Diagrams are original to this vault, drawn from this note's own content.")
    b.append("")
    for slug in photos:
        a = attr[slug]
        artist = a["artist"] if len(a["artist"]) < 90 else a["artist"][:87] + "..."
        b.append("- **%s**: %s · %s · [Commons](%s)"
                 % (a["file"], artist, a["licence"], a["commons_page"]))
    b.append(CR_END)
    return b


def find_insert_point(lines):
    """Index just after the header's closing '---' rule (not the frontmatter)."""
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1
    first_h2 = None
    in_code = False
    for j in range(i, len(lines)):
        s = lines[j].strip()
        if s.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        if s == "---":
            return j + 1
        if s.startswith("## ") and first_h2 is None:
            return j
    return len(lines)


def apply(path, plan, attr, missing):
    src = io.open(path, encoding="utf-8").read()
    lines = src.split("\n")
    lines = strip_block(lines, VS_START, VS_END)
    lines = strip_block(lines, CR_START, CR_END)

    photos = [p for p in plan.get("photos", []) if p in attr]
    for p in plan.get("photos", []):
        if p not in attr:
            missing.append("photo " + p)
    summary = []
    for d in plan.get("summary", []):
        if os.path.exists(os.path.join(SVG_DIR, d + ".svg")):
            summary.append(d)
        else:
            missing.append("svg " + d)

    added = 0
    # section diagrams
    for key, slugs in plan.get("sections", {}).items():
        idx = None
        in_code = False
        for j, ln in enumerate(lines):
            if ln.startswith("```"):
                in_code = not in_code
            if not in_code and ln.startswith(key):
                idx = j
                break
        if idx is None:
            missing.append("heading '%s' in %s" % (key, os.path.basename(path)))
            continue
        ins = []
        for sl in slugs:
            emb = "![[%s.svg]]" % sl
            if not os.path.exists(os.path.join(SVG_DIR, sl + ".svg")):
                missing.append("svg " + sl)
                continue
            if any(emb in ln for ln in lines):
                continue
            ins += ["", emb, ""]
            added += 1
        if ins:
            lines[idx + 1:idx + 1] = ins

    # visual summary
    if photos or summary:
        at = None
        key = plan.get("summary_at")
        if key:
            for j, ln in enumerate(lines):
                if ln.startswith(key):
                    at = j
                    break
            if at is None:
                missing.append("summary_at '%s' in %s" % (key, os.path.basename(path)))
        if at is None:
            at = find_insert_point(lines)
        block = [""] + summary_block(photos, summary, attr) + [""]
        lines[at:at] = block
        added += len(photos) + len(summary)

    # credits
    while lines and lines[-1].strip() == "":
        lines.pop()
    lines.append("")

    lines = trim_blank_runs(lines)
    return "\n".join(lines), added, src


def main():
    global NOTES, SVG_DIR, ATTR
    import argparse
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Insert photos and diagrams into notes."))
    ap.add_argument("plan")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry", action="store_true")
    mode.add_argument("--write", action="store_true")
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    NOTES, SVG_DIR = cfg["notes"], cfg["diagrams"]
    ATTR = os.path.join(cfg["images"], "_attribution.json")
    plan_path, write = a.plan, a.write
    attr = load_attr()
    with io.open(plan_path, encoding="utf-8") as f:
        plans = json.load(f)
    total = 0
    missing = []
    for rel, plan in plans.items():
        path = os.path.join(NOTES, rel)
        if not os.path.exists(path):
            missing.append("note " + rel)
            continue
        new, added, old = apply(path, plan, attr, missing)
        dropped = set(re.findall(r"!\[\[([^\]|]+)", old)) - set(re.findall(r"!\[\[([^\]|]+)", new))
        if dropped:  # notes rebuilt by hand (notes pass 2026-10) keep visuals the plan doesn't know
            missing.append("SKIPPED %s: would drop %s" % (rel, ", ".join(sorted(dropped))))
            new = old
        elif new != old and VS_START in old:  # already visualised: placement is hand-tuned, add by hand
            missing.append("SKIPPED %s: already has a visuals block" % rel)
            new = old
        changed = new != old
        total += added
        print("%-3d %s %s" % (added, "~" if changed else "=", rel))
        if write and changed:
            io.open(path, "w", encoding="utf-8", newline="").write(new)
    print("\n%s: %d visuals placed" % ("WROTE" if write else "DRY RUN", total))
    if missing:
        print("\nPROBLEMS (%d):" % len(missing))
        for m in missing:
            print("  - " + m)
        sys.exit(1)


if __name__ == "__main__":
    main()
