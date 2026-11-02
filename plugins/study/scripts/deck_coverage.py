# -*- coding: utf-8 -*-
"""Structural coverage: does every chapter have every KIND of card it needs?

One of three checks every deck passes before it is called done:
    deck_coverage.py  structure: every chapter has a card file and every slot (this file)
    deck_entities.py  content: the cards carry the names the chapter keeps returning to
    deck_leaks.py     the marks the student actually lost each have a card

Not word-overlap with the textbook: that suits concept chapters and is meaningless for
narrative prose (a 9-card chapter neither can nor should reproduce a short story).

Slot set per subject in study.json deck.subjects.<S>.slots: "concept" (default),
"concept-no-timeline" (no dated events in the book), "literature", "none", or a list of
[name, regex]. "slot_map": {"<stem regex>": "<set>"} picks a different set per file
(e.g. poems or writing formats inside a language subject). A file whose stem matches
"technique_stems" (default "^0 ") is a craft deck and needs no chapter slots.

    python deck_coverage.py --subject "Political Science" [--config study.json]

Exit 1 if any chapter is missing a required slot.
"""
import os
import re
import sys

import decklib

SETS = {
    "concept": [
        ("overview", r"IN ONE LOOK|CHAPTER MAP"),
        ("answer shape", r"ANSWER SHAPE"),
        ("anchor bank", r"ANCHOR"),
        ("key terms", r"KEY TERMS|DEFINE"),
        ("compare table", r"COMPARE|CONTRAST"),
        ("timeline", r"TIMELINE|DATES"),
        ("sample-paper question", "needs-sqp"),
        ("model answer", r"(?m)^M: "),
    ],
    "literature": [
        ("plot/overview", r"IN ONE LOOK"),
        ("anchor bank", r"ANCHOR"),
        ("theme + proof", r"THEME"),
        ("title/technique", r"TITLE"),
        ("sample-paper question", r"(?m)^SQP: "),
        ("model answer", r"(?m)^M: "),
    ],
    "poem": [
        ("overview", r"IN ONE LOOK"),
        ("verbatim cloze", r"(?m)^C: "),
        ("phrase meanings", r"PHRASE"),
        ("devices", r"DEVICES"),
        ("model answer", r"(?m)^M: "),
    ],
    "writing": [
        ("format skeleton", r"skeleton"),
        ("marks + limit", r"marks.*(word limit|split)|limit\?"),
        ("confusion pair", r"CONFUSION PAIR"),
    ],
    "none": [],
}
SETS["concept-no-timeline"] = [s for s in SETS["concept"] if s[0] != "timeline"]
SQP_RE = r"(?m)^(SQP: |F: .*SQP)"


def has_sqp(d, subject, stem):
    """Require a sample-paper card only where sources.md offers an in-scope question for the chapter:
    whether the board happened to ask about a chapter is not a measure of deck quality."""
    src = os.path.join(d["cache"], subject, "sources.md")
    if not os.path.exists(src):
        return True
    text = open(src, encoding="utf-8").read()
    start = text.find("## " + stem)
    if start < 0:
        return True
    end = text.find("\n## ", start + 1)
    return "SQP" in text[start:end if end > 0 else len(text)]


def main():
    a, _cfg, d = decklib.args("Structural coverage of one subject's card files.")
    s = decklib.subject_cfg(d, a.subject)
    pick = lambda v: [tuple(x) for x in v] if isinstance(v, list) else SETS[v]  # noqa: E731
    default = pick(s.get("slots", "concept"))
    slot_map = [(re.compile(k), pick(v)) for k, v in s.get("slot_map", {}).items()]
    technique = re.compile(s.get("technique_stems", r"^0 "))
    files = decklib.card_files(d, a.subject)
    if not files:
        raise SystemExit(f"no card files for {a.subject!r}: write the cards first")
    stems = {os.path.basename(f)[:-4] for f in files}
    print(f"== {a.subject}: {len(files)} card files ==\n")
    problems = 0
    for ch in decklib.chapters(d, a.subject):
        if ch["stem"] not in stems:
            print(f"  MISSING CARD FILE for scope chapter: {ch['label']}  (expected {ch['stem']}.txt)")
            problems += 1
    for path in files:
        stem = os.path.basename(path)[:-4]
        text = open(path, encoding="utf-8").read()
        blocks = len([b for b in re.split(r"\n\s*\n", text) if b.strip()]) - 1
        slots = [] if technique.search(stem) else next((v for r, v in slot_map if r.search(stem)), default)
        missing = []
        for name, pat in slots:
            if pat == "needs-sqp":
                if has_sqp(d, a.subject, stem) and not re.search(SQP_RE, text):
                    missing.append(name)
            elif not re.search(pat, text, re.I):
                missing.append(name)
        problems += len(missing)
        print(f"  {blocks:>2} cards  {stem:<44} " + ("ok" if not missing else "missing: " + ", ".join(missing) + "   <-- GAP"))
    print(f"\n{'ALL SLOTS COVERED' if not problems else str(problems) + ' gap(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
