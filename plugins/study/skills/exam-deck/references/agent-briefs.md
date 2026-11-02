# Exam deck: agent briefs

Copy each brief into the vault (e.g. `.study/briefs/`) once per subject, fill the `<...>`, and spawn each agent with a one-line prompt: "Follow .study/briefs/<brief>.md for SUBJECT=<S> CHAPTER=<n>." Paths are relative to the vault root. Card syntax: `card-format.md` (copy it beside the briefs).

## Brief 1: sources (one agent per subject)

Write ONE file, `<deck.cache>/<S>/sources.md`. Edit nothing else.

1. **Chapters:** study.json `deck.subjects.<S>.chapters` (stem = `<n> <label>`).
2. **The student's own papers:** the post-mortems in `<root>/Mock Review/` for this subject. Per question: number, marks, exact wording, what was written, marks got, the right answer. If a post-mortem lacks the wording, render only the printed question page of the scan with PyMuPDF (dpi 110, a native temp folder) and read the image.
3. **Board sample papers + marking schemes, local files only.** Never download. Newest year first. MCQ answers in a marking scheme may be bold spans or "Answer:" lines. A missing paper is reported, not fetched.
4. **Question bank:** past board questions on these chapters only.
5. **Textbook exercises:** the end-of-chapter questions in the cached text (grep for "Exercise" in every chapter; do not assume a chapter has none).

Format, one section per chapter stem:

```
## <stem>
### Unit Test 2 Q5 . 2 marks
Q: <exact wording>
Y: <what was written> . L: <marks got>/<max>
A: <right answer / marking-scheme points>
### SQP <year> Q27 . 4 marks
Q: ...
A: <marking-scheme answer, compressed>
```

For literature subjects, add a `## Paper pattern` section at the top: mark value and word limit per question type, and the writing marking split (format / content / expression) from the marking scheme.

Reply under 100 words: counts per chapter and anything not found.

## Brief 2: draft one chapter (one agent per chapter)

**Hard ceiling: 10 blocks, 9 is the target.** Write the fewest cards that, memorised cold, earn full marks on anything the board can ask from this chapter. Pack facts into bold-led numbered points. Reference blocks: one fact per line, bold lead first, under ~60 words per line.

Read, in order, stopping when you have enough: `card-format.md`; this chapter's section of `sources.md` (the prediction evidence, it decides what you card); the cached text `<deck.cache>/<S>/<stem>.txt` (the only source for `B:` and `C:` lines); the chapter note; `<root>/How To Write/<S>.md`.

What this student loses marks on (fill from the post-mortems; every card fights one): `<top 3-5 leaks with codes and marks>`.

Concept chapter recipe (skip a slot the chapter has nothing for; never pad):
1. CHAPTER IN ONE LOOK: the 5-8 big ideas, each with its date, name or place.
2. ANSWER SHAPE: the skeleton for the likeliest 4- and 6-markers (definition line, then the bold keyword leads in order). If this chapter owns a logged loss, name it: "you wrote this as a paragraph and scored 1/4; write it as a table".
3. ANCHOR BANK: every named person, treaty, organisation, place and headline number, one line each.
4. KEY TERMS: `term -> definition` in the textbook's exact phrasing.
5. COMPARE TABLE: the chapter's contrasts. Any "differ / compare / distinguish" question is answered as a table. Every cell is a textbook statement; where the text is silent write "not stated".
6. TIMELINE: year -> event for every date the chapter turns on.
7. `PA:` every earlier test question on the chapter, with `Y:` and `L:`; include the ones answered right (no `L:`).
8. `SQP:` sample-paper question(s) + marking-scheme answer.
9. `AR:` 2-3 Assertion-Reason cards from textbook lines, mixing all four keys.
10. `M:` model answer for the likeliest long question: points = marks, bold leads, a definition opening, a closing line, a named anchor in every point. Mark value and word limit in the header.

Literature chapter: IN ONE LOOK (plot in 6-8 points with names), ANCHOR BANK (the single most important card), THEME -> PROOF (never a theme alone), TITLE + TECHNIQUE, `PA:`, `SQP:`, one compressed question-bank traps card (`prompt -> **answer**` lines), a 2-mark and a long `M:` with a named incident in every point.
Poem: IN ONE LOOK, 2-3 verbatim `C:` clozes of the lines that get extracted, PHRASE -> MEANING, DEVICES (each with its line), `PA:`, `SQP:`, one `AR:`, `M:`.
Writing format (`PDF: *`, every block `OFFBOOK: writing format`): SKELETON, MARKS + LIMIT, MUST-HAVE CHECKLIST, CONFUSION PAIR (e.g. invitation vs letter), WHAT COSTS MARKS ("write X, never Y"), `PA:`, two full `M:` answers laid out as on the answer sheet, OPENING + CLOSING LINES.
Law: cases as facts -> issue -> held -> ratio, named in full; every Act with its year and every Section or Article with its number as printed; CONFUSION PAIR lines for look-alike Articles; "if X happens -> Y applies, under Z" lines for scenario MCQs.

Before finishing, check three things the first drafts in the source vault missed (they caused almost all of 48 examiner gaps): every textbook exercise question is answerable from your cards; source-based passages and cartoons are carded (people named); the textbook's own content boxes are carded. Do not join two true facts into a false claim; do not contradict your own file; report any fact you did not read in the chapter text.

Gate, loop until it passes: `python build_exam_deck.py --subject "<S>" --check --only "<n> "`. Fix only your own file. Reply under 60 words: block count, gate status, what the ceiling made you leave out.

## Brief 3: examiner check of one chapter (one agent per chapter, read-only)

You are a strict board examiner. The student will study ONLY these cards. Do not edit any card file. Read the cached chapter text and the card file fully. `B:` / `C:` lines and numbers are machine-verified; focus on `S:`, `W:`, `K:`, `M:` and coverage. `OFFBOOK:` blocks are allowed school questions.

1. **Errors:** answers that are factually wrong or contradict the textbook (wrong person, year, Act, Article, case, A-R key, list item, a definition that changes the meaning). Definite errors only.
2. **Exam simulation:** write ~20 realistic questions on this chapter for the current paper pattern (1-mark MCQ and A-R, short, long, case or source-based, textbook exercises). Report only those a student knowing only these cards could not answer for full marks, naming the missing point. Exam-relevant only.

Write findings to `<deck.cache>/<S>/findings/<n>.txt` and reply with the same text, under 450 words:

```
ERRORS
E1 | card front (first 10 words) | what is wrong | correct fact | textbook quote (verbatim, 8+ words)
GAPS
G1 | marks | question | missing point | textbook quote (verbatim, 8+ words)
```

"none" under an empty heading; at most 10 gaps, likeliest first; every quote copied character for character from the text file.
