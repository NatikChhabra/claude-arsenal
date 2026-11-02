# -*- coding: utf-8 -*-
"""
build_exam_deck.py: build an exam-focused Anki deck for one subject from hand-written card files.
Run from the vault root.

    python build_exam_deck.py --subject "Political Science" [--check [--only "3 "]] [--config study.json]

Scope (decks, textbook folders, chapters, word limits) comes from study.json "deck" (see decklib.py).
Card files: <deck.cards>/<Subject>/*.txt, format in skills/exam-deck/references/card-format.md.

Gate: the build stops if any card fails, unless the block carries OFFBOOK: <reason>:
  * every B: fragment and C: sentence must be found in the chapter's textbook PDF text,
  * every number in S:/W:/Q:/A:/R: must be found in the chapter's textbook text.
--check runs the gate only. Needs: pymupdf (gate), genanki (build).
"""
from __future__ import annotations

import datetime as dt
import glob
import html
import os
import re
import unicodedata

import decklib

STAMP = dt.datetime.now().strftime("%Y%m%d-%H%M")
DASH, EN = "\u2014", "\u2013"

# ---------------------------------------------------------------------------
# markdown -> html
# ---------------------------------------------------------------------------
WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
EMBED = re.compile(r"!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
TABLE_SEP = re.compile(r"^\|?\s*:?-{3,}")


def delink(s):
    s = EMBED.sub("", s)
    s = WIKILINK.sub(lambda m: m.group(2) or m.group(1).rsplit("/", 1)[-1].removesuffix(".md"), s)
    return MDLINK.sub(lambda m: m.group(1), s)


def inline(s):
    """One markdown line/fragment -> html."""
    s = html.escape(delink(s or "").strip(), quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\*\w])\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub("[\u2b50\U0001F534\U0001F7E1\U0001F7E2\U0001F7E0\U0001F195\u2705]|\u26a0\ufe0f?", "", s)
    s = re.sub(r"<b>\s*</b>", "", s)
    return re.sub(r"[ \t]{2,}", " ", s).strip()


def plain(s):
    s = re.sub(r"<[^>]+>", " ", delink(s or ""))
    s = re.sub(r"[`*_#>]", "", s)
    s = "".join(c for c in s if not unicodedata.category(c).startswith("So"))
    return re.sub(r"\s+", " ", s).strip()


def tagify(s):
    return re.sub(r"[^A-Za-z0-9]+", "-", plain(s)).strip("-")[:50] or "x"


def pill(label, cls):
    return f'<span class="pill {cls}">{label}</span>'


def _cells(ln):
    return [c.strip() for c in ln.strip().strip("|").split("|")]


def md(s):
    """card markdown -> html: **bold**, *italic*, '- ' bullet lines, '| a | b |' tables."""
    out, table = [], []

    def flush():
        if table:
            head, *rows = table
            out.append('<table class="t"><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows)
                       + "</table>")
            table.clear()

    for ln in (s or "").split("\n"):
        ln = ln.strip()
        if ln.startswith("- |"):
            ln = ln[2:]
        if ln.startswith("|"):
            if not TABLE_SEP.match(ln):
                table.append(_cells(ln))
            continue
        flush()
        if not ln:
            continue
        bullet = ln.startswith("- ")
        body = inline(ln[2:] if bullet else ln)
        if bullet and not re.match(r"^(<b>)?\(?\d+[.)]|^(<b>)?\([a-z]\)", body):
            body = "\u2022 " + body
        out.append(body)
    flush()
    return "<br>".join(out).replace("<br><table", "<table").replace("</table><br>", "</table>")


def cloze_html(s):
    return "".join(p if p.startswith("{{") else inline(p) for p in re.split(r"(\{\{c\d+::.*?\}\})", s))


# ---------------------------------------------------------------------------
# splitting long reference cards
# ---------------------------------------------------------------------------
# Reviewers keep folding gaps into existing blocks, so cards drift to 700+ words that nobody recalls.
# Reference blocks (anchor banks, key terms, timelines, tables, chapter maps) are lists of
# independent facts: they split into cards of <= SPLIT_WORDS words, each line's bold lead becoming
# the prompt. Model answers, PA and SQP cards stay whole: an answer is one unit.
SPLIT_LABELS = ("ANCHOR", "KEY TERMS", "CHAPTER MAP", "TIMELINE", "RECITATION", "DATES", "MEMORIZE",
                "COMPARE", "TABLE", "ANSWER SHAPE", "SKELETON", "CONFUSION", "SCENARIO", "PAIRS", "RULES",
                "BANK", "MAP", "THEME", "PROOF", "TECHNIQUE", "DEVICES")
SKELETONS = ("ANSWER SHAPE", "SKELETON")   # one bold-led template per question type; follow-on lines stay with it
SPLIT_WORDS = 80
TB_WORDS = 70                              # the TEXTBOOK WORDS box: enough wording to copy, not a second answer
VERB = (("KEY TERMS", "Define"), ("ANCHOR", "What do you know about"), ("RECITATION", "Recite"),
        ("MEMORIZE", "Recite"), ("TIMELINE", "What happened in"), ("DATES", "What happened in"),
        ("CHAPTER MAP", "Explain, in order"), ("ANSWER SHAPE", "Plan the answer"), ("SKELETON", "Plan the answer"))
CAPS_TITLE = re.compile(r"^[A-Z0-9][A-Z0-9 \u2019'&/()%s-]{3,}(?:\s+%s\s+|:\s+)" % (EN, DASH))


def trim_tb(t, cap=TB_WORDS):
    """Keep whole '...'-separated textbook fragments, in order, up to ~cap words."""
    out, n = [], 0
    for fr in (f.strip() for f in re.split(r"\s*\u2026\s*", t or "") if f.strip()):
        w = len(fr.split())
        if out and n + w > cap:
            break
        out.append(fr if w <= cap else " ".join(fr.split()[:cap]) + " \u2026")
        n += w
    return " \u2026 ".join(out)


def nwords(s):
    return len(re.sub(r"[*|_`>-]", " ", s or "").split())


def cue(item):
    """The prompt for one line: its bold lead, else a short plain lead, else None."""
    item = re.sub("^(\\d+[.)]|[\U0001F534\u2b50]+)\\s*", "", item.strip())
    m = re.match(r"^\*{2,3}(.{1,240}?)\*{2,3}", item)
    if m:
        lead = m.group(1).strip(" %s:\u2192*" % DASH).strip()
        return lead if len(lead) <= 110 else lead[:110].rsplit(" ", 1)[0] + "\u2026"
    m = re.match("^([^%s\u2192:]{2,60}?)\\s(%s|\u2192|:)\\s" % (DASH, DASH), item)
    return m.group(1).strip(" *") if m else None


def split_block(label, chapter, s, textbook):
    """[(front, back_md, textbook_md)] for a long reference block, or None to keep it whole."""
    has_table = any(TABLE_SEP.match(ln.strip().lstrip("- ")) for ln in s.split("\n"))
    if not (has_table or any(k in label for k in SPLIT_LABELS)) or nwords(s) <= SPLIT_WORDS * 1.3:
        return None
    raw = [ln.strip()[2:] if ln.strip().startswith("- ") else ln.strip() for ln in s.split("\n")]
    raw = [ln for ln in raw if ln]
    items, head_of, header = [], {}, None          # a row followed by |---| is that table's header
    for i, ln in enumerate(raw):
        if TABLE_SEP.match(ln):
            continue
        if ln.startswith("|") and i + 1 < len(raw) and TABLE_SEP.match(raw[i + 1]):
            header = ln
            continue
        if not ln.startswith("|"):
            header = None
        items.append(ln)
        head_of[len(items) - 1] = header
    if any(k in label for k in SKELETONS):
        merged = []
        for it in items:
            if merged and not it.startswith("**"):
                merged[-1] += "\n- " + it
            else:
                merged.append(it)
        items, head_of = merged, {i: None for i in range(len(merged))}
    chunks, cur = [], []
    for i, _it in enumerate(items):
        if cur and (nwords(" ".join(items[j] for j in cur + [i])) > SPLIT_WORDS or head_of[i] != head_of[cur[0]]):
            chunks.append(cur)
            cur = []
        cur.append(i)
    chunks.append(cur)
    heads = [head_of[ch[0]] for ch in chunks]
    chunks = [[items[i] for i in ch] for ch in chunks]
    # ponytail: each textbook fragment goes to the chunk sharing most content words with it (>= 3);
    # a fragment matching nothing is dropped. Upgrade path: B: lines per item.
    frags = [f.strip() for f in re.split(r"\s*\u2026\s*", textbook or "") if f.strip()]
    keyw = lambda t: set(re.findall(r"[a-z]{4,}", t.lower()))  # noqa: E731
    fr_for = [[] for _ in chunks]
    for fr in frags:
        scores = [len(keyw(fr) & keyw(" ".join(c))) for c in chunks]
        if max(scores) >= 3:
            fr_for[scores.index(max(scores))].append(fr)
    verb = next((v for k, v in VERB if k in label), "Recall")
    out, n, done = [], len(items), 0
    for i, ch in enumerate(chunks):
        cues = [re.sub(r"[*_]", "", _cells(it)[0]).strip() or None if it.startswith("|") else cue(it) for it in ch]
        span = f"{done + 1}-{done + len(ch)}" if len(ch) > 1 else f"{done + 1}"
        hcells = [re.sub(r"[*_]", "", c) for c in _cells(heads[i])] if heads[i] else []
        cols = hcells[1:]
        # "| Basis | A | B |" compares the columns; "| Test | How it works | Example |" compares the rows
        cols_compared = not hcells or hcells[0].lower() in ("", "basis", "feature", "features", "point", "aspect",
                                                          "criterion", "basis of difference", "parameter")
        if len(cols) >= 2 and all(cues) and cols_compared:
            front = f"{chapter}: {' vs '.join(cols)}, compare on " + " \u00b7 ".join(cues)
        elif len(cols) >= 2 and all(cues):
            front = f"{chapter}: {hcells[0]}, give the {' and '.join(c.lower() for c in cols)} for " + " \u00b7 ".join(cues)
        elif all(cues) and "CHAPTER MAP" not in label and len(" \u00b7 ".join(cues)) <= 170:
            front = f"{chapter}: {'Define' if heads[i] else verb} " + " \u00b7 ".join(cues)
        else:
            front = f"{chapter}: {label.lower()}, points {span} of {n}"
        body = "\n".join(([heads[i], "|---|"] if heads[i] else []) + ch)
        out.append((front, body, trim_tb(" \u2026 ".join(fr_for[i]))))
        done += len(ch)
    return out if len(out) > 1 else None


# ---------------------------------------------------------------------------
# gate: textbook text is the only source of truth
# ---------------------------------------------------------------------------
def gnorm(s, hyphen_space=False):
    s = re.sub("([\ufb01\ufb02\ufb00\ufb03\ufb04]) (?=[a-z])", r"\1", s)   # PDF ligature + stray space
    s = unicodedata.normalize("NFKC", s).lower().replace("\u00ad", "")
    s = re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", s)
    s = re.sub("[-%s]\\s*" % EN, " ", s) if hyphen_space else re.sub(r"-\s*", "", s)   # line-break hyphenation
    s = re.sub(r"(?<=\d),(?=\d)", "", s)
    s = re.sub(r"(?<=\d)\.(?=\d)", "p", s)              # keep decimals: 1.33 -> 1p33
    s = re.sub("[\u2018\u2019'\u201c\u201d\"`*_]", "", s)
    s = re.sub(r"[^a-z0-9%]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


class Gate:
    NUM = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)(?!st|nd|rd|th)")

    def __init__(self, dirs, strip=()):
        import fitz
        self.chapter, self.spaced, self.all, self.errors, self._nonum = {}, {}, "", [], {}
        for d in dirs:
            for p in sorted(glob.glob(os.path.join(d, "*.pdf"))):
                pages = [pg.get_text() for pg in fitz.open(p)]
                freq = {}                                # running headers + bare page numbers
                for pg in pages:
                    for ln in {l.strip() for l in pg.split("\n")}:
                        freq[ln] = freq.get(ln, 0) + 1
                drop = {ln for ln, c in freq.items() if c >= 3 and len(ln) < 70 and not re.fullmatch(r"[\d.,%s-]*" % EN, ln)}
                t = "\n".join(" ".join(l for l in pg.split("\n") if l.strip() not in drop) for pg in pages)
                for junk in strip:
                    t = t.replace(junk, " ")
                self.chapter[os.path.basename(p)] = gnorm(t)
                self.spaced[os.path.basename(p)] = gnorm(t, hyphen_space=True)
                self.all += " " + gnorm(t)

    def text(self, where, pdf, s):
        corpus = self.all if pdf == "*" else self.chapter.get(pdf, "")
        nonum = lambda x: re.sub(r"\b\d{1,3}\b ?", "", x)     # noqa: E731  stray page numbers mid-sentence
        for frag in re.split(r"\u2026|\.\.\.", s):
            f = gnorm(frag)
            if len(f.split()) < 3 or f in corpus:
                continue
            if pdf not in self._nonum:
                self._nonum[pdf] = nonum(corpus)
            if nonum(f) in self._nonum[pdf]:
                continue
            w = f.split()          # a box or header mid-sentence: accept when ~all 6-word runs are found
            if len(w) >= 8:
                runs = [" ".join(w[i:i + 6]) for i in range(0, len(w) - 5, 2)]
                if sum(r in corpus for r in runs) >= 0.85 * len(runs):
                    continue
            k = 0
            while k < len(w) and " ".join(w[:k + 1]) in corpus:
                k += 1
            self.errors.append((where, "not in textbook text",
                                f"\u2026{' '.join(w[max(0, k - 4):k + 8])}\u2026 (matched {k}/{len(w)} words)"))

    def numbers(self, where, pdf, s):
        corpus = self.all if pdf == "*" else self.chapter.get(pdf, "")
        spaced = " ".join(self.spaced.values()) if pdf == "*" else self.spaced.get(pdf, "")
        plain_s = re.sub(r"\{\{c\d+::(.*?)\}\}", r"\1", s)
        plain_s = re.sub(r"\b(?:SQP|PA)[- ]?\d[\d-]*|\b20\d\d-\d\d\b|Q\d+|\b\d+\s*marks?\b|\b\d/\d\b|\(\d\)|^\s*\d{1,2}\.|\s\d{1,2}\.\s",
                         " ", plain_s)   # list numbering only (1-2 digits): a year ending a sentence is still checked
        for n in self.NUM.findall(plain_s):
            v = n.replace(",", "").rstrip(".").replace(".", "p")
            if len(v) < 2:
                continue
            pat = r"(?<![0-9p])0?%s(?![0-9p])" % re.escape(v)            # tables print 06.2 for 6.2
            if not (re.search(pat, corpus) or re.search(pat, spaced)):
                self.errors.append((where, "number not in textbook", n))


# ---------------------------------------------------------------------------
# Anki note types + decks
# ---------------------------------------------------------------------------
CSS = """
.card { font-family: "Segoe UI", -apple-system, Inter, system-ui, sans-serif; font-size: 19px; line-height: 1.55;
  text-align: left; color: #1b2430; background: #fbfaf6; padding: 12px 8px; max-width: 760px; margin: 0 auto; }
.night_mode .card { color: #e6ebf2; background: #14181e; }
.meta { font-size: 12px; letter-spacing: .05em; text-transform: uppercase; opacity: .55; margin-bottom: 8px; }
.pill { display: inline-block; font-size: 11.5px; font-weight: 700; letter-spacing: .07em; padding: 3px 10px;
  border-radius: 999px; margin-bottom: 10px; }
.anchor { background: #dbe8fb; color: #0f3a66; } .night_mode .anchor { background: #16324f; color: #a6cbff; }
.lost { background: #ffe5c7; color: #7c3d00; }   .night_mode .lost { background: #3d2a0c; color: #ffc77a; }
.text { background: #e9e5da; color: #4a4232; }   .night_mode .text { background: #2a2720; color: #d9cfb8; }
.asked { background: #ffd9d9; color: #8a1d1d; } .night_mode .asked { background: #431a1a; color: #ffa3a3; }
.model { background: #dcf0e1; color: #155a31; } .night_mode .model { background: #133625; color: #8fe0ac; }
.ar { background: #fde2f1; color: #7a1f55; } .night_mode .ar { background: #3f1730; color: #ffb0dc; }
.sqp { background: #e0e7ff; color: #2b3a8f; } .night_mode .sqp { background: #1c2450; color: #b7c3ff; }
.q { font-size: 21px; font-weight: 600; }
.hint { font-size: 14px; opacity: .6; margin-top: 10px; }
hr { border: 0; border-top: 1px solid #d8d2c4; margin: 14px 0; } .night_mode hr { border-top-color: #2c3440; }
b { color: #0d3b66; } .night_mode b { color: #86bdff; }
code { background: #ece6d8; padding: 1px 5px; border-radius: 4px; font-size: .9em; } .night_mode code { background: #232b35; }
.book { margin-top: 14px; padding: 10px 12px; border-left: 3px solid #b9ad92; background: #f3efe5; font-size: 16px;
  line-height: 1.5; border-radius: 4px; }
.night_mode .book { background: #1f252e; border-left-color: #5a6472; }
.booklabel { font-size: 10.5px; font-weight: 700; letter-spacing: .08em; opacity: .55; margin-bottom: 4px; }
table.t { border-collapse: collapse; margin: 6px 0; font-size: 16px; }
table.t td, table.t th { border: 1px solid #d8d2c4; padding: 4px 8px; vertical-align: top; text-align: left; }
table.t th { background: #f0ece2; } .night_mode table.t th { background: #222a34; }
.night_mode table.t td, .night_mode table.t th { border-color: #2c3440; }
.cloze { font-weight: 700; color: #b4461b; } .night_mode .cloze { color: #ff9c6e; }
"""


def models(genanki):
    exam = genanki.Model(
        1733100111, "Exam \u00b7 Card",
        fields=[{"name": n} for n in ("Front", "Short", "Textbook", "Pill", "Meta", "Source")],
        templates=[{"name": "Recall",
                    "qfmt": '<div class="meta">{{Meta}}</div>{{Pill}}<div class="q">{{Front}}</div>',
                    "afmt": '{{FrontSide}}<hr><div class="a">{{Short}}</div>{{#Textbook}}<div class="book">'
                            '<div class="booklabel">TEXTBOOK WORDS</div>{{Textbook}}</div>{{/Textbook}}'}],
        css=CSS)
    lost = genanki.Model(
        1733100103, "Exam \u00b7 Marks I Lost",
        fields=[{"name": n} for n in ("Question", "Scored", "Detail", "Meta", "Source")],
        templates=[{"name": "Answer it properly this time",
                    # front = the question only; paper code and score on the front read as clutter
                    "qfmt": '<div class="meta">{{Meta}}</div><span class="pill lost">MARKS ALREADY LOST</span>'
                            '<div class="q">{{Question}}</div>',
                    "afmt": '{{FrontSide}}<hr><div class="hint" style="margin:0 0 10px 0">{{Scored}}</div>'
                            '<div class="a">{{Detail}}</div>'}],
        css=CSS)
    side = ('<div class="meta">{{Meta}}</div><span class="pill text">TEXTBOOK</span><div class="hint" '
            'style="margin-top:0">{{Context}}</div><div class="q" style="font-weight:500">{{cloze:Text}}</div>')
    cloze = genanki.Model(
        1733100104, "Exam \u00b7 Textbook Cloze",
        fields=[{"name": n} for n in ("Text", "Context", "Meta", "Source")],
        templates=[{"name": "Cloze", "qfmt": side, "afmt": side}], css=CSS, model_type=genanki.Model.CLOZE)
    return exam, lost, cloze


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------
def main():
    a, _cfg, d = decklib.args("Build or gate-check one subject's exam deck.", extra=[
        (("--check",), {"action": "store_true", "help": "run the gate only"}),
        (("--only",), {"help": "with --check: gate just the card file starting with this prefix, e.g. '3 '"}),
        (("--out",), {"help": "output folder (default: deck.out)"})])
    subject = a.subject
    scfg = decklib.subject_cfg(d, subject)
    gate = Gate(scfg.get("source_dirs", []), scfg.get("strip_text", d.get("strip_text", [])))
    if not gate.chapter:
        print("WARNING: no textbook PDFs found in", scfg.get("source_dirs"), "(every gated card will fail)")
    files = decklib.card_files(d, subject)
    if not files:
        raise SystemExit(f"no card files in {os.path.join(d['cards'], subject)}")
    if a.only:
        if not a.check:
            raise SystemExit("--only works with --check (a real build needs every chapter)")
        files = [f for f in files if os.path.basename(f).startswith(a.only)]
    limits = scfg.get("word_limits", {})
    root, src = d["root_deck"], d["source_note"]
    base = f"{root}::{scfg.get('deck', subject)}"

    pos, counts, notes = 0, {}, []                  # notes: (deck, kind, fields, tags, guid_key, order)
    for ci, path in enumerate(files):
        blocks = decklib.parse(path)
        kind0, head = blocks[0]
        if kind0 != "DECK":
            raise SystemExit(f"{path}: first block must be DECK:/PDF:")
        label, pdf = head["DECK"], head.get("PDF")
        if pdf != "*" and pdf not in gate.chapter:
            raise SystemExit(f"{path}: PDF not found in source_dirs: {pdf}")
        dname = f"{base}::{label}"
        chapter = decklib.label_parts(label)[1]
        meta = inline(f"{subject} \u00b7 {label}")
        ctag = [tagify(subject), f"chapter::{tagify(label)}"]
        for bi, (kind, f) in enumerate(blocks[1:], start=1):
            where = f"{os.path.basename(path)} #{bi} {kind}: {(f.get('Q') or f.get('C') or f.get('A') or f.get(kind) or '')[:60]}"
            gpdf = "*" if "X" in f else pdf           # X: cross-chapter card, check against the whole book
            if "OFFBOOK" not in f:
                for k in ("B", "C"):
                    if f.get(k):
                        gate.text(where, gpdf, f[k])
                for k in ("S", "W", "Q", "A", "R"):
                    if f.get(k) and kind != "SQP":
                        gate.numbers(where, gpdf, f[k])
            tags = list(ctag)
            if kind == "Q":
                p = f.get("P") or ("LIST" if f["S"].count("\n- ") >= 2 else "KNOW IT")
                parts = split_block(p.upper(), chapter, f["S"], f.get("B", ""))
                if parts:
                    for j, (front, body, tb) in enumerate(parts, start=1):
                        pos += 1
                        fields = [inline(front), md(body), md(tb), pill(f"{p} \u00b7 {j}/{len(parts)}", "anchor"), meta, src]
                        notes.append((dname, "exam", fields, tags + ["kind::exam", "split"],
                                      f"{dname}|exam|{bi}|{j}|{front[:150]}", (ci, 1, pos)))
                        counts[(label, "exam")] = counts.get((label, "exam"), 0) + 1
                    continue
                q = CAPS_TITLE.sub("", f["Q"]) if f.get("P") else f["Q"]   # the pill already names the card type
                fields, k2 = [inline(q), md(f["S"]), md(trim_tb(f.get("B", ""))), pill(p, "anchor"), meta, src], "exam"
            elif kind == "C":
                fields, k2 = [cloze_html(f["C"]), inline(f.get("H", "Textbook line: fill the gap")), meta, src], "cloze"
            elif kind == "AR":
                front = (f"<b>Assertion (A):</b> {inline(f['A'])}<br><br><b>Reason (R):</b> {inline(f['R'])}"
                         '<div class="hint">(a) both true, R explains A \u00b7 (b) both true, R does not explain A \u00b7 '
                         "(c) A true, R false \u00b7 (d) A false, R true</div>")
                fields = [front, f"<b>{html.escape(f['K'])}</b>: {inline(f['W'])}", "", pill("ASSERTION-REASON", "ar"), meta, src]
                k2 = "ar"
            elif kind == "PA":
                paper = f["PA"]
                tags.append("asked-in-paper")
                if "L" in f:
                    detail = (f"<b>You wrote:</b> {inline(f.get('Y', '-'))}<hr><b>Full marks:</b><br>{md(f['S'])}"
                              + (f'<div class="book"><div class="booklabel">TEXTBOOK WORDS</div>{md(trim_tb(f["B"]))}</div>'
                                 if f.get("B") else ""))
                    fields = [inline(f["Q"]), f"{html.escape(paper)} \u00b7 got {html.escape(f['L'])}", detail, meta,
                              "Your own paper + its post-mortem"]
                    k2 = "lost"
                    tags.append("my-mistake")
                else:
                    fields = [inline(f["Q"]), md(f["S"]), md(trim_tb(f.get("B", ""))),
                              pill(f"ASKED IN {paper.upper()}", "asked"), meta, "Your own paper"]
                    k2 = "pa"
            elif kind == "SQP":
                fields = [inline(f["Q"]), md(f["S"]), "", pill(f"SAMPLE PAPER {f['SQP'].upper()}", "sqp"),
                          meta, "Board sample question paper + marking scheme"]
                k2 = "sqp"
            elif kind == "M":
                mk = re.match(r"\s*(\d+)\s*marks?", f["M"])
                head_m = f["M"]
                if mk and mk.group(1) in limits and "word" not in head_m:
                    head_m += f" \u00b7 {limits[mk.group(1)]} words"     # the limit belongs on the pill
                fields = [inline(f["Q"]), md(f["S"]), "", pill(f"MODEL ANSWER \u00b7 {head_m.upper()}", "model"), meta,
                          inline(f"Model answer: {f.get('F', 'likely question')} \u00b7 points = marks, textbook wording")]
                k2 = "model"
            else:
                raise SystemExit(f"{where}: unknown block kind {kind}")
            pos += 1
            notes.append((dname, k2, fields, tags + [f"kind::{k2}"], f"{dname}|{k2}|{fields[0][:200]}",
                          (ci, 0 if k2 in ("lost", "pa") else 1, pos)))
            counts[(label, k2)] = counts.get((label, k2), 0) + 1

    if gate.errors:
        print(f"GATE FAILED: {len(gate.errors)} problem(s)")
        for w, what, det in gate.errors:
            print(f"  [{what}] {w}\n      {det}")
        raise SystemExit(1)
    print(f"gate OK: {len(notes)} notes")
    if a.check:
        return

    import genanki
    m_exam, m_lost, m_cloze = models(genanki)
    model_for = {"lost": m_lost, "cloze": m_cloze}
    decks = {}

    def deck(name, desc=""):
        if name not in decks:
            h = 0
            for ch in name:
                h = (h * 131 + ord(ch)) & 0xFFFFFFFF
            decks[name] = genanki.Deck(1_600_000_000 + h % 390_000_000, name, description=desc)
        return decks[name]

    deck(root, "Study from this top deck: new cards rotate across every subject.")
    deck(base, f"{subject}: hand-picked exam cards from the textbook, your own papers and sample papers.")
    tr = d["tag_root"]
    seen = set()
    for i, (dname, k2, fields, tags, key, _) in enumerate(sorted(notes, key=lambda n: n[5]), start=1):
        if key in seen:
            raise SystemExit(f"duplicate card: {key}")
        seen.add(key)
        deck(dname).add_note(genanki.Note(
            model=model_for.get(k2, m_exam), fields=[str(x) for x in fields],
            tags=sorted({f"{tr}::{t}" for t in tags + [f"build::{STAMP}", "exam-deck"] if t}),
            guid=genanki.guid_for("exam|" + key), due=i))

    out_dir = a.out or d["out"]
    os.makedirs(out_dir, exist_ok=True)
    apkg = os.path.join(out_dir, os.path.basename(decklib.apkg(d, subject)))
    genanki.Package(list(decks.values())).write_to_file(apkg)

    order = lambda l: next((i for i, p in enumerate(files) if decklib.label_parts(l)[0] in os.path.basename(p)), 99)  # noqa: E731
    labels = sorted({l for l, _ in counts}, key=order)
    kinds = ["lost", "pa", "exam", "cloze", "ar", "sqp", "model"]
    lines = ["---", "type: reference", "tags: [exam-deck]", "---", "", f"# Exam deck build: {subject}, {STAMP}", "",
             f"**{len(notes)} notes** \u00b7 `{os.path.basename(apkg)}` \u00b7 textbook gate passed.", "",
             "| Chapter | Lost | Paper | Q&A | Line | A-R | SQP | Model | Total |", "|---|---|---|---|---|---|---|---|---|"]
    for l in labels:
        row = [counts.get((l, k), 0) for k in kinds]
        lines.append(f"| {l} | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    open(os.path.join(out_dir, f"exam-deck-report {subject}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines[6:]))
    print(apkg)


if __name__ == "__main__":
    main()
