---
name: note-sync
description: Push a fresh diagnosis back into the chapter notes - write what the paper proved into each affected note's Where I lost marks section, fix anything the paper contradicted, add the missing facts and model answers, and retire stale framing across the vault. Use after any diagnosis (mock-review, diagnose-answer, paper-intake), or for "update the notes with my mistakes", "make the notes match my paper", "change the notes according to what I got wrong".
---

# Note sync

status: beta

Diagnosis updates the *tracking* files. This skill updates the *teaching* files. It runs after every diagnosis without being asked. Paths are under `<root>` (see `study-system`).

**Why it exists:** in the source vault two subjects fell on re-test while correct, generic chapter notes sat in the vault, including a finished note on a writing format whose question then scored zero. The notes were generic; the papers were specific. Each note has to carry its own failure history.

## Steps

1. **Map every question to a note.** Include writing-skill notes and the subject rulebook (`How To Write/<Subject>.md`): the biggest loss is often a format question, not a chapter one.
2. **Write *Where I lost marks*** after *Likely questions* and before *Memorize by Heart*, never at the top. One compact entry per question:
   - the question, the mark, and **the teacher's comment verbatim**;
   - what was written, in one or two lines the student will recognise;
   - what full marks needed, concretely: the names, dates and shape;
   - a link to the post-mortem.
3. **Fix the teaching content.**
   - Missing fact: into the body in textbook order, and into Memorize by Heart.
   - Wrong term: add the pair to the Confusable pairs table.
   - Wrong format: add a worked model answer in the right shape (a table for "differentiate", numbered points where points carry marks).
   - Mark the question as asked in *Likely questions*, e.g. "*(asked Unit Test 2, 1/4)*".
4. **Correct what the paper contradicted.** Fix the claim and leave a dated one-line note saying what was corrected and why. Never overwrite silently; the correction history is how the vault stays trustworthy.
5. **Retire stale framing across the vault.** A diagnosis often falsifies prose written after an earlier paper ("English is my strongest subject", "format is not the main leak"). Grep for it and mark it **superseded** with the date rather than deleting it.
6. **Update the hubs.** If a note's status changed materially (a chapter that just produced a zero), one line each in `Notes/Notes.md` and `Dashboard.md`.

## Rules

- **Specific beats general.** "Learn the anchors" is worthless; naming the three incidents the answer needed is the note doing its job.
- **Quote the teacher inside the note.** Their two words in the margin teach more than any paraphrase.
- Never delete a correct explanation to make room; add the evidence beside it.
- No re-test conditions, drills or study instructions (see `study-system`, no study planning).
- Ask before restructuring a note; adding the sections above is part of this skill.
