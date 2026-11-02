#!/usr/bin/env python3
"""Study-vault structure audit; complements linkcheck.py. Run from the vault root.

Checks:
  1. chapter notes sit in the right book subfolder (`book_folders`) or flat (`flat_subjects`)
  2. every chapter note has a `book:` frontmatter field
  3. every chapter note has a Memorize by Heart section and none of the retired blocks
  4. every paper scan under `papers` has a post-mortem in `mock_reviews` whose filename carries
     the same subject word AND the same paper tag (e.g. "PA-2"), in ONE filename
  5. the Marks Log average and the Dashboard average agree

    python vaultcheck.py [--config study.json]
"""
import argparse
import io
import os
import re
import sys

import studycfg


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def frontmatter(body):
    return body.split("---")[1] if body.startswith("---") else ""


def main():
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Study-vault structure audit."))
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    notes_dir = cfg["notes"]
    books, flat = cfg["book_folders"], set(cfg["flat_subjects"])
    problems, notes, audited = [], [], 0

    for root, _dirs, files in os.walk(notes_dir):
        if any(b in root for b in cfg["bank_dirs"]):
            continue
        for f in files:
            if f.endswith(".md"):
                notes.append(os.path.join(root, f).replace(os.sep, "/"))
    notes = sorted(n for n in notes if n != cfg["notes_index"])

    for p in notes:
        parts = p[len(notes_dir) + 1:].split("/")
        subject = parts[0]
        body = io.open(p, encoding="utf-8").read()
        head = frontmatter(body)
        t = re.search(r"^type:\s*(.+)$", head, re.M)
        if (t and t.group(1).strip() != "note") or "Index" in os.path.basename(p) or os.path.basename(p).startswith("_"):
            continue
        audited += 1
        if subject in books:
            if len(parts) < 3:
                problems.append("MISFILED (needs a book subfolder): %s" % p)
            elif parts[1] not in books[subject]:
                problems.append("UNKNOWN BOOK FOLDER '%s': %s" % (parts[1], p))
        elif subject in flat and len(parts) != 2:
            problems.append("SHOULD BE FLAT: %s" % p)
        if "book:" not in head:
            problems.append("NO book: FIELD  %s" % p)
        if "Memorize by Heart" not in body:
            problems.append("NO Memorize-by-Heart section  %s" % p)
        if "Exam-Facing Card" in body or re.search(r"^## Traps", body, re.M):
            problems.append("RETIRED BLOCK (Exam-Facing Card / Traps)  %s" % p)

    # Scans are nested <papers>/<Subject>/; a flat listdir silently sees none, so recurse.
    scans = []
    for r, _d, fs in os.walk(cfg["papers"]):
        if any(s in r for s in cfg["papers_skip"]):
            continue
        scans += [os.path.join(r, n) for n in fs if n.lower().endswith(".pdf")
                  and not any(w in n.lower() for w in cfg["paper_skip_words"])]
    reviews = [norm(f) for f in os.listdir(cfg["mock_reviews"])] if os.path.isdir(cfg["mock_reviews"]) else []
    tag_re = re.compile(cfg["paper_tag"], re.I)
    for full in scans:
        name = os.path.basename(full)[:-4]
        m = tag_re.search(name)
        subj = (name[:m.start()] if m else name).strip() or os.path.basename(os.path.dirname(full))
        key = norm(subj.split()[0]) if subj.split() else ""
        tag = norm(m.group(1) + m.group(2)) if m else ""
        # subject AND tag in the SAME filename; across all filenames joined, one subject's PA-1
        # plus another's PA-2 would wrongly clear an undiagnosed scan.
        if not any(key in rf and tag in rf for rf in reviews):
            problems.append("UNDIAGNOSED SCAN: %s  -> run paper-intake" % full.replace("\\", "/"))

    avgs = {}
    for f in (cfg["marks_log"], cfg["dashboard"]):
        avgs[f] = set(re.findall(r"(\d{1,3}\.\d)%", io.open(f, encoding="utf-8").read())[:6]) if os.path.exists(f) else None
    ml, db = avgs[cfg["marks_log"]], avgs[cfg["dashboard"]]
    if ml and db and not (ml & db):
        problems.append("AVERAGES MAY DISAGREE: Marks Log %s vs Dashboard %s (check by eye)" % (sorted(ml)[:4], sorted(db)[:4]))

    print("chapter notes : %d  (audited: %d)" % (len(notes), audited))
    print("scans         : %d" % len(scans))
    print("problems      : %d" % len(problems))
    for x in problems:
        print("  " + x)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
