---
name: marks-update
description: Thirty-second update when one or more new scores arrive with no paper to diagnose yet - append to the marks log, update the dashboard table and status, recompute the subject average in both places with the sum written out, and offer the full diagnosis. Use for "got 14/20 in history", "new marks", "paper back", or several bare scores in one message.
---

# Marks update

status: beta

Fast, no analysis. Paths are under `<root>` (see `study-system`).

## Steps

1. Append to `<root>/Marks/Marks Log.md`: date, subject, score, %, source (unit test / mock / pre-board).
2. Update `<root>/Dashboard.md` "Right Now" table: score, %, status (under 50% red, 50-70% amber, 70%+ green), top leak = "awaiting paper" until diagnosed.
3. **Recompute the average; it lives in TWO places** (Dashboard and Marks Log Current Standing). Update both; they must match. Write the arithmetic out (`(a + b + c) / n = X`) before committing the figure: a hand-typed average with no visible sum is how two copies drifted apart. Count only subjects with a real %.
4. If the paper itself is available, say so and offer `diagnose-answer` or `mock-review`: a bare score with no diagnosis is a placeholder, not done.

## Rules

- Never invent a top leak without a paper; write "(paste to diagnose)".
- Several scores in one message: all Marks Log rows, one Dashboard pass, one average recompute.
