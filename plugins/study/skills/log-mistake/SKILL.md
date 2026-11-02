---
name: log-mistake
description: Fast append of one or several mistakes to the right subject error log - the student's own words for what went wrong, an action-shaped fix, an optional mistake code, the master tally cell, a one-line cross-subject check, and retirement of rows the student has since fixed twice. Use for "log this", "add to error log", "I got this wrong", a mistake mentioned in passing, or a correct re-test of something previously logged.
---

# Log a mistake

status: beta

One row per mistake, no commentary unless a pattern just triggered. Paths are under `<root>` (see `study-system`).

## Steps

1. Open `<root>/Error Log/<Subject>.md`; read only the last ~15 rows.
2. Append `| date | source | question (short) | marks | code | what went wrong | the fix |`. **"What went wrong" is required, in the student's own words, not a paraphrase.**
3. **Code is optional.** Fill it from `<root>/reference/taxonomy.md` only if one cleanly fits the definition; never hunt for the closest match. A mistagged code silently corrupts the tally and every Universal Rules row it feeds. If the mistake matches a row in `How To Write/_Universal Rules.md`, say "system habit" in the fix column whether or not a code was assigned.
4. Increment the matching cell in `<root>/Error Log/Error Log.md` Cross-Subject Tally (single-cell edit).
5. **Cross-check every time a code was assigned** (skip when blank), touching only the two small tables: is it this subject's current top leak, is it a leak in another subject? One line, e.g. "F again, 5th time here, same format habit as History" or "New: first T in this subject".
6. Every 3rd entry since the last pattern check: recount that subject's tally and update **Current top leak**.
7. **Universal Rules:** append this subject's evidence to a matching row now, even for one occurrence. If the code now sits at 3+ in a second subject, mark the row confirmed and sync `Dashboard.md` (top-leak cell + "habit to kill" line, single-line edits). Do it, then say so in one line.
8. **Improvement check:** the same question type or code marked correct this time is re-test pass #1 or #2. On the **2nd consecutive pass**, move the original row(s) to **Fixed: Do Not Repeat** as a one-line summary.

## Rules

- The fix column is an **action**: "Write 4 bold points on every 4-marker", never "be more careful".
- Several mistakes in one message: one pass, one file open per subject, one pattern check at the end. Never ask for them one at a time.
- Improvement is data too; log a correct re-test as readily as a failure.
