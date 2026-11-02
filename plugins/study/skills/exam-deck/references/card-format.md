# Exam card files: format

One file per chapter: `<deck.cards>/<Subject>/<n> <prefix> <chapter name>.txt`, read in file-name order by `build_exam_deck.py`. Blocks are separated by a blank line. A line that does not start with a known `KEY:` continues the previous field.

Header block (first block of the file):

    DECK: B1 Ch 2: Demographic Structure
    PDF: Ch 02 - The Demographic Structure of the Indian Society.pdf

`PDF: *` for a chapter with no textbook text (writing formats); every block in it then needs `OFFBOOK:`.

## Block kinds (the first line decides)

| First line | Card | Other keys |
|---|---|---|
| `Q:` question | Recall: short answer + textbook wording | `S:` short answer . `B:` textbook wording, verbatim (fragments joined by an ellipsis, `...` or the single character) . `P:` pill label |
| `C:` sentence with `{{c1::...}}` | Textbook-line cloze, verbatim | `H:` hint above the sentence |
| `AR:` (optional note) | Assertion-Reason | `A:` assertion . `R:` reason . `K:` key letter . `W:` why |
| `PA: Unit Test 2 Q5 . 1 mark` | A question from the student's own paper | `Q:` . `S:` . `B:` . `Y:` what the student wrote . `L:` marks got (makes it a MARKS LOST card) |
| `SQP: 2025-26 Q27 . 4 marks` | Board sample-paper question | `Q:` . `S:` the marking-scheme answer |
| `M: 6 marks` | Model answer to a long question | `Q:` . `S:` full pointed answer . `F:` where the question comes from |
| any block + `X:` | Cross-chapter card: gated against the whole book, not one chapter | |

Assertion-Reason keys: a = both true and R explains A . b = both true, R does not explain A . c = A true, R false . d = A false, R true. The trap is (b).

## Reference blocks split automatically

A `Q:` block whose prompt carries one of these labels is a list of independent facts and is split into cards of at most 80 words, each line's bold lead becoming the prompt: ANCHOR, KEY TERMS, CHAPTER MAP, TIMELINE, RECITATION, DATES, MEMORIZE, COMPARE, TABLE, ANSWER SHAPE, SKELETON, CONFUSION, SCENARIO, PAIRS, RULES, BANK, MAP, THEME, PROOF, TECHNIQUE, DEVICES. So write them one fact per line, each starting with a bold lead (`- **Term** -> definition`, `| **Row** | a | b |`), each under ~60 words. Model answers, `PA:` and `SQP:` blocks stay whole.

## Gate (the build fails until fixed)

- Every `B:` fragment and every `C:` sentence must appear in the cached textbook text.
- Every number in `S:` / `W:` / `Q:` / `A:` / `R:` must appear in the chapter text.
- `OFFBOOK: <reason>` on a block skips the gate; only for a question a real paper asked outside the book, or a writing format.

Never invent a line to pass the gate; shorten it or re-copy it.

## What gets a card

Exam-relevant only: definitions, named lists in full, cause-effect and contrast pairs, thinker / Act / Article / case with the number exactly as printed, every earlier test question, sample-paper questions, 2-3 Assertion-Reason, the model answer for the likeliest long question. Textbook content boxes (flashback, fast-forward, legacy) and source-based passages and cartoons count (name every person in a cartoon). Never: do-this-activity boxes, photo captions, one-off trivia, anything outside the portion, anything foldable into a card already written.

## Slot sets (`deck_coverage.py`, study.json `slots`)

- `concept`: overview (IN ONE LOOK / CHAPTER MAP), ANSWER SHAPE, ANCHOR, KEY TERMS, COMPARE, TIMELINE, a sample-paper question where sources.md has one, a model answer (`M:`).
- `concept-no-timeline`: the same without TIMELINE.
- `literature`: IN ONE LOOK, ANCHOR, THEME, TITLE, `SQP:`, `M:`.
- `poem`: IN ONE LOOK, a `C:` cloze, PHRASE, DEVICES, `M:`.
- `writing`: skeleton, marks + word limit, CONFUSION PAIR.
- `none`: no slot check. A per-stem override list is also accepted (see the script docstring).
