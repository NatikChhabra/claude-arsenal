# -*- coding: utf-8 -*-
"""Does each chapter's cards carry the things the chapter is ABOUT?

deck_coverage.py proves every card SLOT exists; deck_leaks.py proves the student's own losses
are covered. Neither proves the cards carry the chapter's content. This pulls the recurring
named entities (people, places, things the text keeps returning to) out of the cached textbook
text and lists any that appear nowhere in that chapter's cards. Recurring NAMES, not paragraph
word-overlap, because names are what an answer has to cite.

    python deck_entities.py --subject "Political Science" [--min 3] [--config study.json]

Needs the text cache (deck_text.py). Review each hit: a genuine character / place / event
belongs on a card; a one-off mention or a textbook artefact does not.
"""
import collections
import os
import re
import sys

import decklib

STOP = set("""The A An And But For Nor Or So Yet In On At To Of By With From As It He She They We I You His
Her Its Their Our My Your This That These Those There Here When Where What Which Who Whom Whose Why How
If Then Than Now Once Again Also Just Only Even Still Very Too All Both Each Every Some Any No Not
Chapter Reprint Page Notes Activity Box Source Fig Figure Table Text Read Reading Insight Understanding
Think Talking Working Words Exercise Questions Answer Write Discuss Explain Describe Give Find Say
One Two Three Four Five Six Seven Eight Nine Ten First Second Third Last Next Other Another Such Same
Yes Let Do Does Did Have Has Had Was Were Been Being Will Would Shall Should Can Could May Might
Must Am Are Is Be Mr Mrs Dr Sir Madam However Therefore Thus Hence Because Since While During After
Before Between Among Through Against Without Within Into Over Under About Above Below Down Up Out Off
""".split())
WORD = re.compile(r"\b[A-Z][a-zA-Z'’-]{2,}\b")


def normalise(w):
    """Possessive -> the name; contraction -> drop (both were false 'missing' names on the first run)."""
    w = w.replace("’", "'")
    if "'" in w:
        head, _, tail = w.partition("'")
        return head if tail.lower() == "s" else None
    return w


def entities(text, min_count, extra_stop):
    counts = collections.Counter()
    for line in text.split("\n"):
        for m in WORD.finditer(line):
            w = normalise(m.group(0))
            if w and w not in STOP and w not in extra_stop:
                counts[w] += 0 if m.start() == 0 else 1     # a word that only starts lines is probably not a name
    return {w: c for w, c in counts.items() if c >= min_count}


def main():
    a, _cfg, d = decklib.args("Named-entity coverage of one subject's cards.",
                              extra=[(("--min",), {"type": int, "default": 3,
                                                   "help": "times a name must appear in the chapter (default 3)"})])
    extra_stop = set(decklib.subject_cfg(d, a.subject).get("entity_stop", []))   # e.g. book titles in running headers
    total, checked = 0, 0
    print(f"== {a.subject}: names appearing {a.min}+ times in the textbook but absent from the cards ==\n")
    for cf in decklib.card_files(d, a.subject):
        stem = os.path.basename(cf)[:-4]
        src = os.path.join(d["cache"], a.subject, stem + ".txt")
        if not os.path.exists(src):
            print(f"  {stem:<42} (no textbook text cached: skipped)")
            continue
        checked += 1
        cards = open(cf, encoding="utf-8").read().lower()
        ents = entities(open(src, encoding="utf-8").read(), a.min, extra_stop)
        missing = sorted(((c, w) for w, c in ents.items() if w.lower() not in cards), reverse=True)
        total += len(missing)
        shown = ", ".join(f"{w}({c})" for c, w in missing[:10])
        print(f"  {stem:<42} {len(ents):>3} names, {len(missing):>2} missing" + (f"  -> {shown}" if missing else "  -> none"))
    print(f"\n{checked} chapter(s) actually checked · {total} missing name(s).")
    if not checked:
        # a missing cache once skipped every chapter and reported a false "0 missing"
        print(f'NOTHING WAS CHECKED: the text cache is missing. Run: python deck_text.py --subject "{a.subject}"')
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
