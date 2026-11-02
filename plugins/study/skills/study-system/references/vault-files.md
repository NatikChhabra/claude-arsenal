# Vault files: shapes the skills and scripts rely on

All paths are under the study folder `<root>` (study.json `root`, default `Study`). Keep the headings and column names exactly: `tallycheck.py` and `vaultcheck.py` parse them.

## study.json (vault root)

```json
{
  "root": "Study",
  "book_folders": {"Political Science": ["Book 1 - Contemporary World Politics", "Book 2 - Politics in India Since Independence"]},
  "flat_subjects": ["Psychology", "Legal Studies"],
  "bookmap": {"Political Science - Book 1": "Political Science/Book 1 - Contemporary World Politics"},
  "not_in_syllabus": ["Suggestions for Project Work"],
  "bank_dirs": ["Banks"]
}
```

Every other key and its default: `scripts/studycfg.py`. The `deck` block: `skills/exam-deck/references/card-format.md`.

## Error Log/<Subject>.md

```
# Error Log: <Subject>
## Log
| Date | Source | Q (short) | Marks | Code | What went wrong | The fix |
## Recurring Patterns
| Code | Count | Verdict |          (Current top leak named under the table)
## Known Suspects (pre-diagnosis)
- [ ] <suspected habit before any paper was diagnosed>   ([x] + one line once a paper confirms or clears it)
## Fixed: Do Not Repeat
- <one-line summary of a row retired after 2 consecutive correct re-tests>
```

The Log table is the source of truth. Recurring Patterns must equal a recount of it.

## Error Log/Error Log.md (master)

```
## Cross-Subject Tally
| Code | <Subject A> | <Subject B> | **Total** |
| K | 3 | 1 | **4** |
```

Single-cell edits only; never recount the whole table by hand (`tallycheck.py` does it).

## How To Write/_Universal Rules.md

```
| # | Habit that loses marks | Evidence | Fix |
```

One row per cross-subject habit. Evidence cites subject + paper + question. Append each new subject's evidence the moment it recurs, even below the 3+ threshold; a row that only names the first subject goes stale silently. Skills check this file **before** the subject rulebook.

## Mock Review/_Template.md

```
---
type: mock-review
subject:
date:
score:
---
# <Subject>: <Test name>: <Date>
Score: __ / __ . Full-fix ceiling: __ . Realistic next target (must match Marks Log milestones): __

## 1. Where the marks actually went
| Q | Marks lost | Code | One-line reason |
Total lost: __ . Biggest single leak: __

## 2. The split that matters
| Cause | Marks lost |
| Did not know it (K) | |
| Knew it, wrote it badly (R/D/F/T/E/S) | |
| Time / careless (P/C) | |

## 3. Question by question
### Q_ (__ marks, scored __)
Asked: . Wrote: . Full-mark answer: . Teacher's words (verbatim): . Code: . Fix:

## 4. Timing audit
## 5. Three fixes, ranked by marks recoverable
## 6. Propagated?
- [ ] Error log rows  - [ ] Master tally  - [ ] Marks Log + average  - [ ] note-sync
```

Name each post-mortem `<YYYY-MM> <Subject> <Tag>-<n> (<score>).md` so `vaultcheck.py` can match it to its scan (subject word and paper tag in the same filename).

## Marks/Marks Log.md

```
## All Scores
| Date | Subject | Score | % | Source |
## Current Standing
| Subject | Latest % | ... |
Average: (a + b + c) / n = X%
```

The average appears here and in `Dashboard.md`; both must match, with the sum written out.

## Dashboard.md

"Right Now" table (subject, latest score, %, status, top leak), the cross-subject habit to kill, links to every tracking file. Status: under 50% red, 50-70% amber, 70%+ green.
