---
name: study-note
description: Write an exam-facing chapter note, concept breakdown or case analysis for any board exam, anchored to the official syllabus and the marking scheme, aimed at the student's own logged leaks, in one fixed note format, filed and linked both ways. Use for "explain X", "notes on X", "make notes", "case analysis", "article on X", "break down this concept", or a named chapter or topic the student wants taught.
---

# Study note

Exam-facing material for a board exam (a national board exam is the worked example). **The bar is a note that converts into a marked answer**, not "covered the topic". Paths are under `<root>` (see `study-system`).

## Before writing

1. Read `<root>/How To Write/<Subject>.md` (after `_Universal Rules.md`): answer format, word limits, mark splits. The note teaches toward that format.
2. Confirm the topic is on the **current year's official syllabus** for the subject (the board's curriculum PDF for the session). Off-syllabus or unsure: say so in one line, write only what is on it. A chapter not in the curriculum gets no note.
3. Read the last ~15 rows of `<root>/Error Log/<Subject>.md`. **Aim the note at those leaks, not at generic coverage**; that is the whole edge.
4. If an undiagnosed paper or unlogged mistake is pending, say so and offer that first. Diagnosis outranks notes.

## Note format (every note, in this order)

```
---
type: note
subject: <Subject>
book: <full prescribed book name>
unit: <syllabus unit>
board-marks: <unit weight>
tags: [...]
status: draft | done
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
# <Chapter title>: <Subject>, <Book/Unit>
<- [[<root>/Notes/Notes.md]] . Rulebook: [[<root>/How To Write/<Subject>.md]] . Leaks: [[<root>/Error Log/<Subject>.md]] . Board weight: N marks

%% visuals %%            photo + diagrams (visualize.py, svgkit.py)
## Mind Map              mermaid skeleton + one-line colour key
## 1. ... ## n.          content in TEXTBOOK order, numbered points, tables for every comparison
## Key terms             the exact words markers scan for
## Likely questions      | Q | Marks | Answer skeleton |  (mark the ones a paper already asked)
## Where I lost marks    ONLY if a paper tested this chapter (written by note-sync)
## Memorize by Heart     rote facts only: dates, Acts, named thinkers, cases, movements, exact terms
```

`note_audit.py` and `vaultcheck.py` check this shape (frontmatter, `book:`, Mind Map, Likely questions, Memorize by Heart, backlink to the index).

**Never:** banners or callouts above the visuals, an "exam card" or "traps" block, decorative emoji or star spam, "verified <date>" stamps, struck-through or "not in the book" content (delete it), drills, re-test conditions or study plans, video embeds. Paper evidence goes in *Where I lost marks* near the end, never at the top.

## Subject add-ons (built from logged leaks; add your own the same way)

- **Wrong-term subjects** (a logged T leak, e.g. Psychology, Legal Studies): a **Confusable pairs** table; for named models, the **number of parts** in Memorize by Heart (the source vault lost a mark writing 3 of a 4-part model).
- **Literature** (English): an **Anchor Table** of named characters, incidents, quotations and figures. A theme with no named incident scored as half an answer.
- **Law** (Legal Studies): every case in this shape:

```
CASE: <name> (<year>) . COURT: <court>
FACTS: <2-3 lines, only what the ruling turns on>
ISSUE: <the legal question, as a question>
HELD: <the decision>
RATIO: <the principle; the part the board asks for>
WHY IT IS ASKED: <the unit it illustrates>
LIKELY QUESTION: <exam-style question + mark value>
```

## File and link it

- Path: `<root>/Notes/<Subject>/<Book>/<Chapter Title>.md` for subjects with several prescribed books (`book_folders` in study.json), `<root>/Notes/<Subject>/<Chapter Title>.md` for single-book subjects (`flat_subjects`).
- Add one bullet under the subject's heading in `<root>/Notes/Notes.md` (single-line edit, never rewrite the index). With the backlink line at the top, the note is linked both ways. A note nothing links to does not exist; `linkcheck.py` reports orphans.

## Rules

- **Cite the source** of every case name, year, Article, Section, amendment and statistic. Unverified gets `[unverified]` (counted by `note_audit.py`), never a plain statement: a wrong case name in a board answer costs the whole mark.
- A claim not in the prescribed textbook is **deleted**, not flagged.
- Every line earns a mark or explains how to earn one. Length is set by the mark value of the questions the note feeds.
- Diagrams draw only facts already in the note (`svgkit.py` specs, check with `svg2png.py` before embedding). Visual style: skill design.
- A written note is not a learned note; the note's job ends at being correct and exam-shaped.
