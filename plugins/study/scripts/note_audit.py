"""Note coverage + structure audit. Run from the vault root.

PART 1  every textbook chapter PDF (`textbooks`/<book folder>/*.pdf) has a matching note in the
        notes subfolder `bookmap` maps it to (title-word overlap >= 50%); `not_in_syllabus`
        fragments are skipped by design
PART 2  every chapter note carries the required blocks and none of the retired ones
PART 3  every note is linked from the notes index
PART 4  unverified flags ("[unverified]" or the yellow-circle emoji) still sitting in notes

    python note_audit.py [--config study.json]

Exit 1 when a chapter has no note, a note misses a block, or a note is unindexed.
"""
import argparse
import glob
import io
import os
import re

import studycfg

STOP = set("the a an of and in to for on is are as at by with its it his her".split())


def toks(name):
    name = re.sub(r"^Ch \d+ - ", "", name)
    name = re.sub(r"\.(pdf|md)$", "", name)
    name = re.sub("[\\u2013\\u2014-]", " ", name.lower())
    return {w for w in re.sub(r"[^a-z0-9' ]", " ", name).split() if w not in STOP and len(w) > 2}


def required(index_name):
    return [
        ("frontmatter", lambda t: t.startswith("---")),
        ("type:", lambda t: re.search(r"^type:", t, re.M)),
        ("subject:", lambda t: re.search(r"^subject:", t, re.M)),
        ("tags:", lambda t: re.search(r"^tags:", t, re.M)),
        ("backlink to index", lambda t: re.search(
            r"\[\[(?:[^\]|]*/)?" + re.escape(index_name) + r"(?:\.md)?[\]|#]", t)),
        ("Mind Map", lambda t: re.search(r"^## Mind Map", t, re.M)),
        ("Likely questions", lambda t: re.search(r"^## Likely questions", t, re.M)),
        ("Memorize by Heart", lambda t: re.search(r"^## Memorize by Heart", t, re.M)),
        ("no Exam-Facing Card", lambda t: "Exam-Facing Card" not in t),
        ("no Traps section", lambda t: not re.search(r"^## Traps", t, re.M)),
        ("no top-of-note callout", lambda t: not re.search(
            r"^> \[!(danger|warning|info|success|caution)\]", t.split("## Mind Map")[0], re.M)),
        ("no strikethrough", lambda t: "~~" not in t),
    ]


def main():
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Note coverage + structure audit."))
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    notes_dir, ref = cfg["notes"], cfg["textbooks"]

    print("=" * 78 + "\nPART 1: CHAPTER COVERAGE, every textbook chapter vs the notes folder\n" + "=" * 78)
    total_missing = 0
    for book, notedir in cfg["bookmap"].items():
        pdfs = sorted(os.path.basename(x) for x in glob.glob(os.path.join(ref, book, "*.pdf")))
        notes = [n for n in sorted(os.path.basename(x) for x in glob.glob(os.path.join(notes_dir, notedir, "*.md")))
                 if not n.startswith("_")]
        ntoks = [(n, toks(n)) for n in notes]
        print("\n### %s\n    notes dir: %s  (%d pdf chapters, %d notes)" % (book, notedir, len(pdfs), len(notes)))
        if not pdfs:
            print("    NO PDFs FOUND: check `textbooks` and the folder name (a silent 0 hides every gap)")
        matched = set()
        for pdf in pdfs:
            if any(x.lower() in pdf.lower() for x in cfg["not_in_syllabus"]):
                print("    SKIP    %-58s (not in syllabus)" % pdf)
                continue
            pt, best, score = toks(pdf), None, 0.0
            for n, nt in ntoks:
                ov = len(pt & nt) / max(1, min(len(pt), len(nt))) if pt and nt else 0
                if ov > score:
                    best, score = n, ov
            if score >= 0.5:
                matched.add(best)
                print("    OK      %-58s -> %s" % (pdf, best))
            else:
                total_missing += 1
                print("    MISSING %-58s -> best guess %s (%.0f%%)" % (pdf, best, score * 100))
        for e in (n for n in notes if n not in matched):
            print("    EXTRA   (note with no matching textbook pdf): %s" % e)
    print("\n  >>> chapters with no note: %d" % total_missing)

    print("\n" + "=" * 78 + "\nPART 2: STRUCTURE, does every note carry the required blocks?\n" + "=" * 78)
    index = cfg["notes_index"]
    allnotes = sorted(os.path.join(r, f) for r, _d, fs in os.walk(notes_dir) for f in fs
                      if f.endswith(".md") and os.path.join(r, f).replace("\\", "/") != index)
    checks = required(os.path.basename(index)[:-3])
    bad = skipped = 0
    for p in allnotes:
        t = io.open(p, encoding="utf-8").read()
        ty = re.search(r"^(?:type|status):\s*(.+)$", t, re.M)
        rel = os.path.relpath(p, notes_dir)
        if (any(b in rel for b in cfg["bank_dirs"]) or os.path.basename(p).startswith("_")
                or "Index" in os.path.basename(p) or (ty and ty.group(1).strip() in cfg["exempt_types"])):
            skipped += 1
            continue
        miss = [name for name, fn in checks if not fn(t)]
        if miss:
            bad += 1
            print("  %-72s  missing: %s" % (rel, ", ".join(miss)))
    print("\n  >>> %d of %d notes have every required block; %d incomplete"
          % (len(allnotes) - skipped - bad, len(allnotes) - skipped, bad))
    print("  >>> %d bank/index/reference files exempt by design" % skipped)

    print("\n" + "=" * 78 + "\nPART 3: INDEX, is every note linked from the index?\n" + "=" * 78)
    linked = set(re.findall(r"\[\[([^\]|#]+)", io.open(index, encoding="utf-8").read())) if os.path.exists(index) else set()
    linked |= {x[:-3] for x in linked if x.endswith(".md")}
    unlinked = [p.replace("\\", "/") for p in allnotes
                if p.replace("\\", "/") not in linked and p.replace("\\", "/")[:-3] not in linked
                and os.path.splitext(os.path.basename(p))[0] not in linked]
    for u in unlinked:
        print("  NOT LINKED FROM INDEX: %s" % u)
    print("  >>> %d unlinked" % len(unlinked))

    print("\n" + "=" * 78 + "\nPART 4: UNVERIFIED FLAGS still sitting in notes\n" + "=" * 78)
    flag = 0
    for p in allnotes:
        t = io.open(p, encoding="utf-8").read()
        n = t.count("\U0001F7E1") + t.count("[unverified]")
        if n:
            flag += n
            print("  %-72s  %d unverified flags" % (os.path.relpath(p, notes_dir), n))
    print("  >>> %d unverified flags total" % flag)
    return 1 if (total_missing or bad or unlinked) else 0


if __name__ == "__main__":
    raise SystemExit(main())
