---
name: paper-intake
description: Ingest a newly added scanned exam script (unit test, mock, pre-board, PDF or photos) end to end - find it, render the pages as images, read every mark and the teacher's verbatim comments off the script, reconcile the total, run the post-mortem, propagate to every tracking file, and rewrite the affected chapter notes. Use for "I added a paper", "new paper is in", "check my paper", a PDF named in the papers folder, or when a session-start scan finds a scan with no matching post-mortem.
---

# Paper intake

status: beta

The whole pipeline for a new marked script. Standing instruction: when a new paper appears, do this without being asked. Paths are under `<root>` (see `study-system`).

## 0. Find the paper and check it is new

- Scans live in `<root>/Backend/Papers/<Subject>/`, named `<Subject> <Tag> <n>.pdf`. **Recurse:** `find "<root>/Backend/Papers" -name '*.pdf' | sort`. A flat listing of the parent returns nothing and reads as "no work".
- Compare against `<root>/Mock Review/`. A scan with no post-mortem carrying the same subject and tag in one filename is unprocessed (`vaultcheck.py` reports it).
- Folders of reference material (e.g. `_Reference/`, project files) are not scans; skip them.
- **One PDF may hold two papers** (an earlier test bound in front of the new one). Check page headers before diagnosing; diagnosing the wrong half corrupts every downstream file.

## 1. Render the scan; the text layer is not enough

The OCR layer reproduces the printed question paper adequately and the handwritten answers as word salad; red marks do not extract at all. **Look at the pages as images.** With PyMuPDF (no poppler needed):

```python
import fitz, os, tempfile
out = os.path.join(tempfile.gettempdir(), "paper"); os.makedirs(out, exist_ok=True)
d = fitz.open("<root>/Backend/Papers/<Subject>/<file>.pdf")
for i, p in enumerate(d):
    p.get_pixmap(dpi=150).save(os.path.join(out, "p%02d.png" % (i + 1)))
```

Write this to a `.py` file and run it; shell heredocs can mangle backslashes. Use a native temp path (on Windows, Python cannot see Git Bash `/tmp`). Then read each PNG. Pull the printed question wording and mark values separately with `scripts/pdfpage.py` or `pdfgrep.py`.

## 2. Read the marks off the script exactly

Per question:
- the mark awarded (margin), section subtotals, the total on page 1;
- **every teacher comment verbatim** ("wrong format", "elaborate how", "what??"). These are the highest-value data in the vault: they name the leak in the examiner's own words;
- anything struck through or circled in the answer;
- sub-marks where the teacher splits content / expression / format.

**Reconcile:** per-question marks must sum to the written total. If not, log an open marking discrepancy, in either direction, including when it favours the student.

## 3. Diagnose

Hand off to `mock-review` (question codes, split, cross-subject check, fixes, propagation). Do not duplicate its logic here.

## 4. Push it into the chapter notes

Run `note-sync`. This is the reason the pipeline exists: the other steps update the *tracking* files, this one updates the *teaching* files, so the next revision shows what the paper proved.

## 5. Report, in this order

1. The score and the delta, plainly.
2. The single most important finding, usually one question.
3. What changed system-wide (top-leak reshuffles, codes crossing thresholds).
4. Which notes changed and what was added.

## Rules

- Diagnosis outranks note-writing: an undiagnosed scan comes before any request for new notes.
- Never soften a bad result; a sugar-coated score makes the system useless.
- Quote the teacher. Their handwriting outranks any inference.
- Commit before bulk edits; an intake touches 8-12 files.
- Flag what you could not read (a blurred mark gets an "unverified" tag, not a guess).
