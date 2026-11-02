# study

A mistake-driven board-exam study system for any student and any Obsidian or plain-markdown vault: write papers, log every mistake by type, fix the mistake type, push each diagnosis back into the chapter notes. Built and measured on a real student vault (a national board exam is the worked example throughout); every board, subject and folder name is configurable.

Start with skill `study-system`: the loop, the routing table, the vault layout and `study.json`.

## Skills

| Skill | What it does |
|---|---|
| `study-system` | The loop, the router (which skill fires for what), standing rules, session-start checks, vault layout and config |
| `diagnose-answer` | Mark one answer, name the mistake type, write the full-mark model answer in the subject's format |
| `log-mistake` | Append mistakes to the subject error log, update the tally, cross-check other subjects, retire fixed rows |
| `marks-update` | Record a score in the Marks Log and recompute the average everywhere it appears |
| `mock-review` | Post-mortem of a whole marked paper: where the marks went, the knowledge vs execution split, ranked fixes, propagation |
| `paper-intake` | A new scanned script end to end: find it, render it, read every mark and comment, reconcile, diagnose, sync notes |
| `note-sync` | Write what a paper proved into each affected chapter note and fix what it contradicted |
| `study-note` | Write a syllabus-anchored, leak-aimed chapter note or case analysis in the fixed note format |
| `synthesize-improvement` | Rank skill-level weaknesses across all subjects from the logs |
| `exam-deck` | Build a capped Anki deck per subject with drafting and examiner agents and three coverage checks |
| `vault-audit` | Recompute every tally and average, verify every cross-subject claim, check links, filing and structure |

## Scripts (`scripts/`, run from the vault root, all read `study.json`)

| Script | What it does |
|---|---|
| `studycfg.py` | Shared config loader: every vault path and its default |
| `linkcheck.py` | Broken wikilinks, orphan notes, broken skill frontmatter |
| `vaultcheck.py` | Note filing, `book:` field, required blocks, undiagnosed scans, Marks Log vs Dashboard average |
| `tallycheck.py` | Recount each subject's error-log codes against its patterns table and the master tally |
| `note_audit.py` | Every textbook chapter has a note, every note has its blocks and an index link, open `[unverified]` flags |
| `outline.py` | Heading outline of every note, for picking diagram anchors |
| `svgkit.py` | Render exam-shaped SVG diagrams from a JSON spec, readable in light and dark themes |
| `visualize.py` | Insert photos and diagrams into notes from a plan file, idempotently |
| `svg2png.py` | Render SVGs to PNG to look at a diagram before it ships |
| `pdfgrep.py` | Find terms in a PDF's text layer with page numbers and context |
| `pdfpage.py` | Dump the text layer of a PDF page range |
| `md2pdf.py` | Markdown to a printable A4 PDF |
| `decklib.py` | Shared deck scope and card-file parser |
| `deck_text.py` | Cache each chapter's textbook PDF as plain text for the deck agents |
| `build_exam_deck.py` | Gate-check (`--check`) or build one subject's `.apkg` from card files |
| `deck_coverage.py` | Structure: every chapter has every kind of card it needs |
| `deck_entities.py` | Content: the names a chapter keeps returning to appear on its cards |
| `deck_leaks.py` | Leaks: every mark lost on a real paper has a card that fixes it |
| `deck_sizes.py` | Card length by label, to find wall-of-text cards |
| `deck_verify.py` | A built `.apkg` really imports: counts, empty cards, duplicate fronts |

## Requirements

Python 3.9+. `pymupdf` for anything that reads a PDF or renders an SVG; `markdown` for `md2pdf.py`; `genanki` to build decks; `anki` for `deck_verify.py` (imports into a throwaway collection, never a real profile). Set `PYTHONIOENCODING=utf-8` on Windows.

## Install
```
/plugin install study --marketplace NatikChhabra/claude-arsenal
```
Or `/plugin marketplace add NatikChhabra/claude-arsenal`, then `/plugin install study@claude-arsenal`. More options: the [marketplace README](../../README.md).
