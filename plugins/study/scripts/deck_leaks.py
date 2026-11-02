# -*- coding: utf-8 -*-
"""Every mark the student lost on a real paper, and whether a card in the deck fixes it.

The check that decides the score: in the source vault most lost marks were execution
(format, missing named anchors), not knowledge, and a deck that ignores them misses the point.

Losses live in <deck.losses>/<Subject>.txt, one row per real loss taken from the post-mortems:

    paper | question | marks | code | what went wrong | needle; needle; needle

`needles` are strings that must appear somewhere in that subject's card files for the loss to
count as addressed. Code NB = not board standard (outside the textbook / marking scheme):
recorded, deliberately not carded. Blank lines and `#` comments are ignored.

    python deck_leaks.py --subject "Political Science" [--config study.json]
"""
import os
import sys

import decklib


def load(path):
    if not os.path.exists(path):
        raise SystemExit(f"no loss table at {path}\nCreate it, one row per mark lost, from the post-mortems:\n"
                         "  paper | question | marks | code | what went wrong | needle; needle")
    rows = []
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 6:
            raise SystemExit(f"{path}:{n}: expected 6 fields separated by |, got {len(parts)}")
        paper, q, marks, code, what, needles = parts
        rows.append((paper, q, float(marks), code, what, [x.strip() for x in needles.split(";") if x.strip()]))
    return rows


def main():
    a, _cfg, d = decklib.args("Lost marks vs the deck.")
    files = decklib.card_files(d, a.subject)
    if not files:
        raise SystemExit(f"no card files for {a.subject!r}: write the cards first")
    low = "\n".join(open(p, encoding="utf-8").read() for p in files).lower()
    rows = load(os.path.join(d["losses"], a.subject + ".txt"))
    print(f"== {a.subject}: every mark lost on a paper, vs the deck ==\n")
    print(f"{'Paper':<8}{'Question':<28}{'Lost':>5}  {'Code':<6}Addressed by a card?")
    print("-" * 94)
    total = unaddressed = offboard = 0.0
    for paper, q, lost, code, _what, needles in rows:
        total += lost
        if code == "NB":
            offboard += lost
            print(f"{paper:<8}{q:<28}{lost:>5}  {code:<6}not board standard: left out on purpose")
            continue
        hits = [n for n in needles if n.lower() in low]
        if not hits:
            unaddressed += lost
        print(f"{paper:<8}{q:<28}{lost:>5}  {code:<6}" + (f"YES  ({len(hits)}/{len(needles)} anchors)" if hits else "*** NO CARD ***"))
    print("-" * 94)
    print(f"marks lost on the papers   : {total}")
    print(f"not board standard (NB)    : {offboard}")
    print(f"addressed by the deck      : {total - unaddressed - offboard}")
    print(f"NOT addressed              : {unaddressed}")
    print("\n*** gaps above must be fixed ***" if unaddressed else "\nEvery loss on every paper has a card behind it.")
    return 1 if unaddressed else 0


if __name__ == "__main__":
    sys.exit(main())
