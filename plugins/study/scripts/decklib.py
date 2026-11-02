"""Shared scope + card-file parser for the exam-deck scripts (no genanki needed).

The deck lives under the "deck" key of study.json:

    "deck": {
      "root_deck": "Boards",                      top Anki deck
      "tag_root": "BOARDS",                       every tag nests under it
      "cards": ".study/cards",                    <cards>/<Subject>/<n> <label>.txt
      "losses": ".study/losses",                  <losses>/<Subject>.txt (deck_leaks.py)
      "cache": ".study/cache",                    <cache>/<Subject>/<stem>.txt textbook text
      "out": "Study/Backend/Anki",                built .apkg files
      "source_note": "Textbook",                  shown on every card as its source
      "subjects": {
        "Political Science": {
          "deck": "1 . Political Science",
          "source_dirs": ["Study/reference/Textbooks/Political Science - Book 1"],
          "chapters": [["Ch 1: The Cold War Era", "Ch 01 - The Cold War Era.pdf"]],
          "slots": "concept",                     concept | concept-no-timeline | literature | none
          "word_limits": {"2": "50-60", "4": "100-120", "6": "170-180"}
        }
      }
    }

A chapter label is "<prefix>: <chapter name>" (a long dash also works as the separator).
The card file stem is "<n> <prefix> <chapter name>".
"""
import argparse
import glob
import os
import re

import studycfg

KEYS = ("DECK", "PDF", "Q", "S", "B", "P", "C", "H", "AR", "A", "R", "K", "W", "PA", "Y", "L",
        "SQP", "M", "F", "OFFBOOK", "X")
KEYLINE = re.compile(r"^(%s):\s?(.*)$" % "|".join(KEYS))
LABEL_SEP = re.compile("\\s*(?:\\u2014|\\u2013|:)\\s+")


def deck_cfg(cfg):
    d = {"root_deck": "Exam Decks", "tag_root": "EXAM", "cards": ".study/cards", "losses": ".study/losses",
         "cache": ".study/cache", "out": cfg["root"] + "/Backend/Anki", "source_note": "Textbook", "subjects": {}}
    d.update(cfg.get("deck", {}))
    return d


def label_parts(label):
    """'B1 Ch 2: Demographic Structure' -> ('B1 Ch 2', 'Demographic Structure')."""
    parts = LABEL_SEP.split(label, maxsplit=1)
    return (parts[0], parts[1]) if len(parts) == 2 else ("", label)


def stem(n, label):
    pre, name = label_parts(label)
    return f"{n} {pre} {name}".replace("  ", " ").strip()


def subject_cfg(d, subject):
    if subject not in d["subjects"]:
        raise SystemExit(f"subject {subject!r} not in study.json deck.subjects (have: {sorted(d['subjects'])})")
    return d["subjects"][subject]


def chapters(d, subject):
    s = subject_cfg(d, subject)
    out = []
    for n, (label, pdf) in enumerate(s.get("chapters", []), start=1):
        st = stem(n, label)
        pdfs = [p for sd in s.get("source_dirs", []) for p in glob.glob(os.path.join(sd, glob.escape(pdf)))] if pdf else []
        out.append({"n": n, "label": label, "stem": st,
                    "cards": os.path.join(d["cards"], subject, st + ".txt"),
                    "pdf": pdfs[0] if pdfs else None,
                    "text": os.path.join(d["cache"], subject, st + ".txt")})
    return out


def card_files(d, subject):
    return sorted(glob.glob(os.path.join(d["cards"], subject, "*.txt")))


def apkg(d, subject):
    return os.path.join(d["out"], f"{d['root_deck']} - {subject} (exam deck).apkg")


def args(description, subject_required=True, extra=()):
    """Parse --config/--subject (+ extra) and return (args, vault cfg, deck cfg)."""
    ap = studycfg.config_arg(argparse.ArgumentParser(description=description))
    ap.add_argument("--subject", required=subject_required)
    for a, kw in extra:
        ap.add_argument(*a, **kw)
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    return a, cfg, deck_cfg(cfg)


def parse(path):
    """Card file -> [(kind, {KEY: text})]. Blocks are separated by a blank line; a line with no
    known KEY: continues the previous field. The first block is the DECK:/PDF: header."""
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    out = []
    for b in (b for b in re.split(r"\n\s*\n", text) if b.strip()):
        fields, order, last = {}, [], None
        for ln in b.split("\n"):
            m = KEYLINE.match(ln)
            if m:
                last = m.group(1)
                if last in fields:
                    raise SystemExit(f"{os.path.basename(path)}: duplicate {last}: in block\n{b[:200]}")
                fields[last] = m.group(2).strip()
                order.append(last)
            elif last:
                fields[last] += "\n" + ln.strip()
            else:
                raise SystemExit(f"{os.path.basename(path)}: text before any KEY:\n{b[:200]}")
        kind = next((k for k in order if k not in ("H", "OFFBOOK", "P", "F", "X")), order[0])
        out.append((kind, fields))
    return out
