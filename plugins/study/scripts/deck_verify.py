# -*- coding: utf-8 -*-
"""Verify built .apkg files actually import: note/card counts, empty cards, duplicate fronts,
cards per chapter deck and the first new card of each. Run before deleting any other copy of a
deck: a deck that does not open is not a backup.

    python deck_verify.py                       # every .apkg in deck.out
    python deck_verify.py path/to/deck.apkg ... [--config study.json]

Needs the official `anki` package (pip install anki); it imports into a throwaway collection
and never touches a real Anki profile.
"""
import argparse
import collections
import glob
import os
import re
import sys
import tempfile

import decklib
import studycfg


def verify(path):
    from anki.collection import Collection, ImportAnkiPackageOptions, ImportAnkiPackageRequest
    col = Collection(os.path.join(tempfile.mkdtemp(), "v.anki2"))
    try:
        col.import_anki_package(ImportAnkiPackageRequest(package_path=path, options=ImportAnkiPackageOptions()))
        fronts = collections.Counter(re.sub(r"<[^>]+>|\s+", " ", col.get_note(n).fields[0]).strip().lower()
                                     for n in col.find_notes(""))
        dups = [f[:70] for f, c in fronts.items() if c > 1]
        empty = len(col.get_empty_cards().notes)
        print(f"{'OK ' if col.note_count() and not empty and not dups else 'BAD'} {os.path.basename(path)}: "
              f"{col.note_count()} notes, {col.card_count()} cards, {empty} empty, {len(dups)} duplicate fronts")
        for f in dups:
            print("      DUP  " + f)
        for dk in sorted(col.decks.all_names_and_ids(), key=lambda x: x.name):
            if dk.name.count("::") >= 2:
                first = col.find_cards(f'did:{dk.id} is:new', order="c.due asc")[:1]
                lead = re.sub(r"<[^>]+>", "", col.get_card(first[0]).note().fields[0])[:50] if first else "-"
                print(f"      {dk.name.split('::')[-1]}: {len(col.find_cards(f'did:{dk.id}'))} cards · first: {lead}")
        return bool(col.note_count()) and not empty and not dups
    finally:
        col.close()


def main():
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Verify built .apkg files import cleanly."))
    ap.add_argument("apkg", nargs="*")
    a = ap.parse_args()
    studycfg.utf8()
    out = decklib.deck_cfg(studycfg.load(a.config))["out"]
    files = a.apkg or sorted(glob.glob(os.path.join(out, "*.apkg")))
    if not files:
        print(f"NO DECKS in {out}")
        return 1
    bad = 0
    for p in files:
        try:
            bad += 0 if verify(p) else 1
        except Exception as e:  # noqa: BLE001 - one broken package must not hide the others
            bad += 1
            print(f"FAIL {os.path.basename(p)}: {type(e).__name__}: {e}")
    print(f"\n{len(files)} deck(s) · {bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
