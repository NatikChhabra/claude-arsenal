---
name: diagnose-answer
description: Diagnose one exam answer the student wrote - mark it like the examiner, say in plain words why each mark was lost, tag a mistake code only if one clearly fits, show the full-mark version in the subject's exact format, log it, cross-check other subjects, then push it into the chapter note. Use for a pasted question plus the student's answer, "diagnose this", "mark my answer", "why did I lose marks", "is this a full-mark answer".
---

# Diagnose an answer

status: beta

Say exactly why the answer lost marks, by mistake **type**, not just by content. Paths are under the study folder `<root>` (see `study-system`).

## Steps

1. **Read the rulebooks first:** `<root>/How To Write/_Universal Rules.md` (cross-subject habits), then `<root>/How To Write/<Subject>.md`. Every judgement traces to a rule in one of the two.
2. **Mark it like the examiner.** Count valid distinct points; award marks per point, not per paragraph. State the score and why.
3. **Name the mistake in plain English. This is the required part.** Only then add a code from `<root>/reference/taxonomy.md` if the reason you just wrote matches that code's definition. Do not tag a code because it feels adjacent: a directive skip once got tagged "careless" instead of "directive misread" and sat unnoticed for weeks. A blank code is fine.
4. **Show the full-mark version** in the exact format the rulebook demands: bold leads, word count, keywords, closing line.
5. **Diff it** in three bullets: what was there, what was missing, what to do differently.
6. **Log it:** append a row to `<root>/Error Log/<Subject>.md`. For pattern checks read only the last ~15 rows (offset read or tail), never the whole log.
7. **Master tally:** increment the matching cell in `<root>/Error Log/Error Log.md` Cross-Subject Tally. Single-cell edit; never recount the table.
8. **Cross-check, only if a code was assigned** (two small tally tables, never raw logs): is it this subject's top leak, and does it show in another subject's tally row? One output line.
9. **Universal Rules:** if the code matches an existing row in `_Universal Rules.md`, append this subject's evidence to that row now, even for a single occurrence. A row that only shows the first subject goes stale silently. If the code now sits at 3+ in a **second** subject, update the row header and say so. Treat 3+ as "worth a look", not a confirmed pattern.
10. **Run `note-sync`** if the question belongs to a chapter that has a note. Not optional: correct generic notes did not stop the same losses on re-test.

## Output

```
SCORE: x / y
WHY: <plain-English reason per lost mark>
CODES: <only if one obviously fits, else "none yet">

FULL-MARK ANSWER:
<in exam format, inside the word limit>

THE DIFF:
- Had: ...
- Missing: ...
- Next time: ...

CROSS-CHECK: <same habit as X in <subject> / new, no match yet>   (only when a code was assigned)
```

## Rules

- Never say "good attempt". Say what the marker would deduct.
- Never give a model answer that breaks the subject's word limit or format.
- If the loss is format, say so plainly; do not send the student to revise content they already knew.
- No drills or re-test plans in the output.
