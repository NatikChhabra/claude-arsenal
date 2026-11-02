---
name: synthesize-improvement
description: Regenerate the cross-subject "where to actually improve" synthesis - read the master tally and each diagnosed subject's pattern table, convert incident counts to marks-weighted totals, and rank skill-level gaps (format, precision, named anchors, real content gaps) by marks recoverable rather than by subject; overwrite one synthesis file. Use for "where should I improve", "what's my overall pattern", "combine my logs", "what am I actually bad at", or automatically after a post-mortem once 2+ subjects are diagnosed.
---

# Cross-subject synthesis

status: beta

The error logs say *what* went wrong on *which* question. This answers: across everything diagnosed, what is the **skill** gap, not the topic gap? Output goes to one file. Do not restate individual mistakes. Paths are under `<root>` (see `study-system`).

## Steps

1. `<root>/Dashboard.md` "Right Now": which subjects are diagnosed.
2. `<root>/Error Log/Error Log.md` Cross-Subject Tally: incidents per code.
3. Per diagnosed subject, read only its Recurring Patterns table and, if present, the post-mortem's "split that matters" table. Not the raw logs.
4. **Convert incident counts to marks-weighted totals per code** across subjects; incident counts over-weight cheap half-mark MCQ slips against expensive long-answer losses. Show the arithmetic.
5. Rank codes by **total marks lost**. State the top lever: "fix only X and you recover ~Y of the Z marks lost so far."
6. Flag codes that are genuinely **subject-specific** (one subject K-dominated while others are F/T-dominated); do not force a universal fix where the data says "revise content in this one subject".
7. **Watch list:** habits seen 2x across subjects but not at the 3+ threshold in `How To Write/_Universal Rules.md`.
8. **Overwrite** `<root>/Error Log/Cross-Subject Synthesis.md`: data table, marks-weighted headline, ranked levers, subject exceptions, watch list, one "fix exactly one thing" recommendation.
9. Confirm it is linked from `Dashboard.md` and from `Error Log.md` near the tally; add the links if missing, never twice.

## Rules

- A re-derivation, not an append: overwrite the whole file every run so it never holds old numbers.
- Only with 2+ diagnosed subjects; one paper has no cross-subject pattern.
- If the weighted totals do not reconcile with total marks lost across all papers, show the gap; never force round numbers.
- No study plan in the output: the levers name skills, not schedules.
