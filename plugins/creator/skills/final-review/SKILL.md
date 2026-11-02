---
name: final-review
description: Hand a finished video package to the creator for one watch and one "upload" - QC pass on every exact file, scorecard self-score, 3 fresh blind reviewers with an AI-feel gate, a COMPUTED ship score (never typed), the growth gate, one message with the whole package (long + every Short + every Reel + 3 title/thumbnail pairs), then stamp his OK. Use for "is it ready", "send it for review", "final cut", "review message", or when an edit is done.
---

# final-review <ep>

status: beta

Never call a cut FINAL before the creator watched it and said "upload". ONE delivery per video = the WHOLE package:
the long + every Short + every Reel + the 3 title/thumbnail pairs, all at one bar. A missing piece = no message, never
a cut alone, never an interim clip or a "quick look?" ask. (Shorts that rode a long's OK unreviewed shipped at 8.0 with
no covers; since then every Short ships final WITH its long.)

Scorecards: `references/scorecards.md`. Blind rubric + the AI-feel gate: `references/blind-rubric.md`.
Score computer: `ship_score.py` (next to this file).

## 1. Make the files he will watch (they ARE the uploads)
- Long: if the project has an edit-list checker, run it (0 errors, every warning answered); render the master at the
  upload resolution. Shorts: skill `shorts` (every one rendered, both apps checked).
- QC every exact file: if the project has a QC oracle, it must PASS; otherwise check by hand with ffmpeg: loudness
  -14 LUFS +-1 and true peak <= -1 dBTP (`ebur128=peak=true`), flashes, black/frozen picture, clicks at cuts, silence in
  the body, the voice on a phone band, and that nothing identifying the creator is readable (a username, a profile, a
  path). No PASS = no message.
- Sound: every added sound on a chosen cue, density inside its caps, every spoken line intelligible (transcribe the
  render and compare), and for each sound: is its purpose THIS beat (a cheer on a failure is out of place).
- Long jobs (render, transcribe, QC) run detached; read the log tail and the FAIL/WARN lines when they end.

## 2. Score it, then have it scored blind
- Watch every file whole, picture + sound, full runtime. If the project has a watch-pack tool, read its report top to
  bottom and every flagged strip; otherwise pull a frame sheet per minute and listen through. Never score from the
  transcript or stills alone.
- Self-score on the scorecards rows that apply. Every row >= 8.5, else fix and re-render (the changed parts, then one
  full render).
- Before any reviewer: the template audit (blind-rubric "AI-feel gate"), for the long AND every Short/Reel edit list.
- FRESH reviewers (new agents) get ONLY the rubric's pack: the render, its QC sheets, the transcript, the template
  audit, the credits, the scorecards. Never the build, the edit notes or our reasoning. A long: **3 reviewers in parallel**
  (one reviewer's scale steered a cut down 0.6 with no edit change). Every Short and Reel: the "Short / Reel review"
  block, one file each. Fix what >= 2 reviewers name or a gate fails.
- Compute, never type: `python ship_score.py a.md b.md c.md > avg.md` (Shorts: `--short`, per cut). GATED MISSING =
  re-run that reviewer; RE-CUT = a Short failed a question. Ship score >= 8.5; our self-score at most 0.5 over it. If
  the project has an uploader that stamps the blind score onto the upload sheet, stamp the computed line.
- PLATEAU: two blind rounds in a row with no row up by >= 0.5 = stop rendering. Name the root cause (the concept, the
  flavour, a tool or gate) and fix that; never another render round on the same plan. A Short moment with 2 fresh
  rounds under 7.5 is dropped for the next candidate (10 rounds on the same moments stayed at 5.9-6.8).
- A revision cut: diff the edit list against the one he watched; the diff must show only his notes.

## 3. Needs before the gate
Skills `shorts` (every Short + Reel sheet), `thumbnail` (3 cards + feed mock, the covers) and `publish-meta` (the upload
sheet) done, the computed blind scores written into each sheet.

## 4. Gate + message
- Skill `growth-gate` on the whole package (long, Shorts, Reels, links): every row >= 8.5.
- Stage the finals in the project's ONE upload folder (for example `UPLOAD/video<N>_<ep>/`) the moment they pass; if the
  project has a staging tool, run it in review mode. The message names that folder.
- One message, bullet points: each file with its scores side by side (self, blind, QC), the 3 A/B pairs, what changed
  since the last cut. Ask one thing: "upload, or change?"

## 5. His answer
- "upload" (+ any dates): stamp his words + the time as `creator_ok` on the long and each Short/Reel sheet, then skill
  `release`. Any re-render after his OK removes the stamp: he watches the new file.
- Any verdict or number he gives on a cut: one row in the calibration ledger (blind-rubric, last section) the moment he
  says it.
- Notes: harvest every note verbatim with its time into the video's brief. A rejection = the wrong PLACE, not the thing:
  fix the placement or trigger at the root; ban an element only when he says he dislikes it. Then re-cut and return here.
