---
name: exam-deck
description: Build a capped, finishable Anki exam deck for one subject from the textbook and the student's own papers - scope in study.json, cache the textbook text, one drafting agent per chapter under a 9-10 card ceiling, a verbatim gate, an examiner agent per chapter, then structure, content and leak checks before the .apkg ships. Use for "make the deck for <subject>", "Anki for <subject>", "flashcards for my exam", "check the <subject> deck", or redoing a deck that grew too big to finish.
---

# Exam deck

status: beta

Subagents draft and check each chapter against the textbook text; the main thread only scopes, reviews and builds. Card syntax: [references/card-format.md](references/card-format.md). Agent briefs: [references/agent-briefs.md](references/agent-briefs.md). Scripts: `${CLAUDE_PLUGIN_ROOT}/scripts/`, run from the vault root, `PYTHONIOENCODING=utf-8` on Windows.

## The card ceiling overrides everything

**9-10 cards per chapter, about 150-200 for a whole subject.** Pack many facts into one card as bold-led numbered points; one dense card beats six thin ones.

Evidence: an uncapped 631-card deck in the source vault was never finished (the student got through 100-200 cards). An uncapped draft brief produced 73 cards for one chapter. A card the student never sees is worth nothing. When the examiner finds a gap, **add a line to an existing card**, never a new card. The builder splits long reference blocks into ~80-word cards by each line's bold lead, so write those blocks one fact per line, each under ~60 words.

The ceiling is per subject, not rigidly per chapter: spend the budget where that subject bleeds (12-15 cards on a 4-chapter subject; up to 12-14 on very large units).

## Build to the subject's failure profile

Read the subject's post-mortems first. Each subject fails differently, and the deck carries what fixes that failure:

| Profile (source-vault example) | What the deck must carry |
|---|---|
| Execution: paragraphs where points or a table were needed, no named example | an ANSWER SHAPE card and a COMPARE TABLE card per chapter |
| Knowledge: specific facts the notes never had; invented Acts and Article numbers when unsure | content completeness; every Act with its year, Section and Article number exactly as printed; CONFUSION PAIR lines; full TIMELINES so there is no gap to invent into |
| Recall: the facts sit in Memorize-by-Heart tables but were never recited | RECITATION cards straight off those tables; a "distinguish = table, never two definitions" card |
| Literature: theme with no incident, wrong format, under length | anchor banks, theme-to-proof, format skeletons, word-limit cards |

Teacher evidence is per subject: how one teacher sets papers transfers only to subjects that share that teacher. Where a teacher was proven to reuse earlier test questions verbatim (two exact matches in the source vault, both 1-mark objective items), card **every** earlier test question, including the ones answered correctly.

## Steps

1. **Ask once.** Paper date, portion (chapter list), card focus. One question, at the start.
2. **Scope.** Add the subject to `study.json` `deck.subjects` (deck name, `source_dirs`, `chapters`, `slots`, `word_limits`; see `scripts/decklib.py`). Then `python deck_text.py --subject "<S>"` caches each chapter's textbook text. Agents read the cache, never the PDF.
3. **Sources** (1 agent, brief 1): `<deck.cache>/<S>/sources.md`, every earlier test question with what was written and scored, the board's sample papers + marking schemes, the question bank, the textbook exercises. **Local files only; never download papers inside this step.**
4. **Draft** (1 agent per chapter, in parallel, brief 2). Each agent loops its own file through `build_exam_deck.py --subject "<S>" --check --only "<n> "` until it passes.
5. **Gate the whole subject:** `build_exam_deck.py --subject "<S>" --check`.
6. **Examiner check, never skipped** (1 agent per chapter, brief 3, each simulating ~20 real exam questions). The gate checks quotes and numbers; only a reader catches meaning. In the source vault it caught five factual errors that had passed the gate, including a reversed cause (who paid whom) and a character called "unnamed" whom the text names; a wrong name with no digits passes the gate silently. Fold every finding into an existing card.
7. **Build:** `build_exam_deck.py --subject "<S>"` writes the `.apkg` to `deck.out`.
8. **Three checks before it is called done** (they answer different questions):
   - `deck_coverage.py --subject "<S>"`: does every chapter have every *kind* of card (structure).
   - `deck_entities.py --subject "<S>"`: do the cards carry the names the chapter keeps returning to (content).
   - `deck_leaks.py --subject "<S>"`: does a card fix every mark the student actually lost (needs `<deck.losses>/<S>.txt`, one row per real loss from the post-mortems; adding a subject is adding a file).
   - Plus `deck_sizes.py` for wall-of-text cards and `deck_verify.py <file>.apkg` (the deck really imports: counts, empty cards, duplicate fronts). A deck that does not open is not a backup.
9. **Import** into Anki with the student's go-ahead. Back up and export the old deck **with scheduling** before deleting anything.

## Rules

- One subject per session. Agents get a one-line prompt pointing at the brief; never paste textbook or card text into prompts. Main-thread output stays small (counts, tails).
- Launch agents in waves of ~5 and save after each wave: session limits killed 8 agents mid-flight once.
- **Which coverage check:** word-overlap with textbook paragraphs suits concept subjects and is meaningless for narrative prose (a 9-card chapter cannot reproduce a short story). `deck_coverage.py` checks structure and works for both.
- Every table cell is a textbook statement, never an inference made to complete a row. Where the text is silent, write "not stated".
- Chapters earlier tests never covered are the likeliest new material on a full paper; keep full coverage, never narrow to "predicted" questions.
- The latest year's sample paper and marking scheme outrank older papers. Never state a mark split you have not read in the current sample paper.
