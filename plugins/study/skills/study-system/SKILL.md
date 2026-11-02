---
name: study-system
description: The operating loop and routing table for a mistake-driven board-exam study vault (Obsidian or plain markdown) - write papers, log every mistake by type, fix the mistake type, push each diagnosis into the chapter notes; covers the vault layout, study.json config, session-start checks and which study skill fires for what. Use for the start of any study session, setting up a new study vault, "where were we", "what do I do with this paper", or whenever it is unclear which study skill applies.
---

# Study system: the loop and the router

status: beta

A board-exam vault that improves scores by fixing **mistake types**, not by re-reading content. Diagnosis first, notes second, no study planning.

## The loop

1. **Diagnose.** The student pastes a wrong answer; name the *mistake type*, not just the right answer.
2. **Log.** Append one row to `<root>/Error Log/<Subject>.md` in the existing table format.
3. **Pattern-hunt.** Every 3rd log entry, name the top recurring type per subject.
4. **Model answer.** A full-mark answer to the exact question, in the exact format from `<root>/How To Write/<Subject>.md`.
5. **Post-mortem** of every whole paper into `<root>/Mock Review/` from `_Template.md`.
6. **Push it into the notes** (`note-sync`). A tracking file that knows the leak is not enough: in the source vault two subjects fell on re-test with correct, generic notes already written, and a finished note on a writing format sat unopened while that exact format scored zero. A written note is not a learned note; say so, but do not prescribe drills.

## Routing: fire without being asked

| The student does or says | Skill |
|---|---|
| a question + their answer, "mark this", "why did I lose marks" | `diagnose-answer` |
| a bare score, "got X/Y", "paper back" | `marks-update` |
| a whole marked paper, "post-mortem", "review my test" | `mock-review` |
| a single slip, "log this", "add to error log" | `log-mistake` |
| "explain X", "notes on X", "case analysis", "article on X" | `study-note` |
| a new scan in the papers folder, "I added a paper", "check my paper" | `paper-intake` |
| "update notes with my mistakes", and after ANY diagnosis | `note-sync` |
| "where should I improve", "overall pattern", "what am I actually bad at" | `synthesize-improvement` |
| "make the deck for <subject>", "Anki for <subject>" | `exam-deck` |
| "audit the vault", "is anything broken", numbers stopped adding up | `vault-audit` |

There is no drill or quiz skill on purpose: the source vault retired drills once the student planned study in another tool.

## Standing rules

- **No study planning.** No drills, re-test queues, schedules or "this week" lists in post-mortems, notes, dashboards or any skill output, unless the student asks for planning in this vault. Diagnose, record, fix the notes, stop.
- **Diagnosis outranks note-writing.** An undiagnosed paper or unlogged mistake comes before a new note; say so and do it first.
- **Tie all feedback to a mistake type.** "Forgot the definition" beats "good try". Never soften a bad result.
- **Every model answer obeys the subject's word limit and format.** Right content in the wrong format is wrong for boards.
- **Verify paper patterns against the board's current sample paper.** Mark splits shift between years; flag what is unverified, never state a stale split as fact.
- **Cite the source of any legal, political or historical fact** (case name, year, article, section, statistic). Unverified gets a tag, never a plain statement.
- **Ask before editing an existing file** unless a skill step says to edit it. New files are fine.
- **Commit before any bulk rewrite** of `Error Log/`, `Marks/` or `Mock Review/` when the vault is a git repo; local history may be the only backup.
- **Never track a credential.** Before committing `.obsidian/`, grep the staged tree for tokens (`git grep -InE "ghp_|github_pat_"`). A sync plugin once wrote a token into a tracked plugin `data.json`.

## Session start (unprompted)

1. Read `<root>/Dashboard.md` only, not the logs: per-subject top leak, any score with no post-mortem, any code at 3+ in a second subject. Surface it.
2. **Recurse the papers folder** for scans: `find "<root>/Backend/Papers" -name '*.pdf'`. Papers are nested per subject; a flat listing returns nothing and looks like "no work". Any PDF without a matching post-mortem is unprocessed: run `paper-intake` without being asked. One PDF can hold two papers; check page headers.
3. Repeated workflow (2+ times) becomes a skill; tell the student.
4. Hand-written counts ("4 of 4 diagnosed subjects", "average across 4 subjects") go stale when a new subject is diagnosed. Grep and fix every instance in the same pass.
5. The "3+ occurrences = pattern" threshold is a guess, not tuned. Flag when it fires; never state its output as certain.

## Layout and config

Default layout under the study folder `<root>` (set in `study.json` at the vault root; every key has a default, see `scripts/studycfg.py`):

```
<root>/
  Dashboard.md            start here: live state + per-subject leaks
  How To Write/           answer-writing rulebook per subject + _Universal Rules.md (checked first)
  Error Log/              Error Log.md (master tally) + <Subject>.md + Cross-Subject Synthesis.md
  Mock Review/            _Template.md + one post-mortem per paper
  Marks/Marks Log.md      every score over time
  Notes/<Subject>/<Book>/ chapter notes (book subfolders only for multi-book subjects) + Notes.md index
  Backend/Papers/<Subject>/  raw scans, named "<Subject> <Tag> <n>.pdf" (e.g. "History PA 2.pdf")
  reference/taxonomy.md   the mistake codes, defined once
```

File shapes (tables the scripts parse), the post-mortem template and the taxonomy: [references/vault-files.md](references/vault-files.md), [references/taxonomy.md](references/taxonomy.md).

## Scripts

Run from the vault root; `python` may be `py -3` or `uv run --with pymupdf python` on your machine. Set `PYTHONIOENCODING=utf-8` on Windows: vault filenames carry emoji and long dashes, and a cp1252 console crashes mid-report, hiding the findings it just computed.

| Script | Job |
|---|---|
| `linkcheck.py` `vaultcheck.py` `tallycheck.py` `note_audit.py` | integrity checks (`vault-audit`) |
| `pdfgrep.py` `pdfpage.py` | search / dump a PDF's printed text |
| `svgkit.py` `visualize.py` `svg2png.py` `outline.py` | diagrams into notes (`study-note`) |
| `md2pdf.py` | markdown to printable A4 PDF |
| `build_exam_deck.py` `deck_*.py` | Anki exam decks (`exam-deck`) |

Skill files need YAML frontmatter (`name` + trigger-rich `description`) in `.claude/skills/<name>/SKILL.md` at the vault root; a nested or flat `.md` skill does not load.
