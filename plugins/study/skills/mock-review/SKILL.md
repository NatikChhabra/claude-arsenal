---
name: mock-review
description: Full question-by-question post-mortem of a marked test paper - marks lost per question with a mistake code, the three-way split (did not know / knew but wrote badly / time and careless), the cross-subject conclusion, three fixes ranked by marks recoverable, and propagation into the error log, master tally, marks log, averages, Universal Rules and the chapter notes. Use for "post-mortem this", "review my test", "go through my paper", or a whole paper pasted with marks.
---

# Post-mortem a paper

status: beta

Paths are under `<root>` (see `study-system`). Template and file shapes: `study-system/references/vault-files.md`.

## Steps

1. Copy `<root>/Mock Review/_Template.md` to `<root>/Mock Review/<YYYY-MM> <Subject> <Tag>-<n> (<score>).md`.
2. **Question by question:** marks lost, code, one-line reason. No code fits: write `NEW: <plain label>` rather than forcing one. Check each loss against `How To Write/_Universal Rules.md` first; if a cross-subject habit explains it, name that.
3. **Three-way split:** did not know (K) vs knew it but wrote it badly (R/D/F/T/E/S) vs time/careless (P/C).
4. If the middle bucket is largest, say so loudly: the fix is answer format, not revision.
5. **Cross-subject conclusion:** for each code appearing 2+ times in this paper, check the master Cross-Subject Tally for a match in other subjects. State it plainly: "same F habit already logged in Economics" or "isolated to this subject so far". This is the point of the system: one root cause, several subjects, one fix.
6. **Timing audit:** blanks, rushed sections.
7. **Three fixes**, ranked by marks recoverable per hour.
8. **Propagate:**
   - every mistake into `<root>/Error Log/<Subject>.md`; each code into the master tally (single-cell edits; read only the last ~15 log rows);
   - the score into `<root>/Marks/Marks Log.md`;
   - **recompute the subject average in BOTH the Marks Log Current Standing and `Dashboard.md`**, with the arithmetic written out (`(a + b + c) / n = X`) before writing it. Adding a score without recomputing staled the average every time.
9. **Universal Rules, every recurrence:** append this subject's evidence to any matching row, even one occurrence. A code now at 3+ in a second subject gets the row header updated and the Dashboard synced (top leak + habit to kill); tell the student in one line.
10. **Improvement check:** a previously logged question type that scored well is a re-test pass; on the 2nd consecutive pass move the old rows to **Fixed: Do Not Repeat**.
11. **Known Suspects:** go through the subject's "Known Suspects (pre-diagnosis)" list. `[x]` + one line if this paper confirms it; leave `[ ]` with a one-line reason if untested or contradicted. Nothing else in the workflow touches this list, so it goes stale unless this step does it.
12. **Re-synthesize:** if 2+ subjects are diagnosed, run `synthesize-improvement`.
13. **Stale counts:** a newly diagnosed subject changes every hand-written count ("4 of 4 diagnosed", "average across 4 subjects"). Grep and fix them all now.
14. **Run `note-sync`.** Not optional: every note the paper touched gets the real question, the real mark and the teacher's verbatim comment in its *Where I lost marks* section.

## Rules

- Rank fixes by marks recoverable per hour, not by interest.
- A score with no post-mortem does not count.
- Suggest new chapter notes only when the split shows a real K majority; always `note-sync` the notes that exist.
- No study planning: no re-test queues, drills or schedules in the post-mortem.
