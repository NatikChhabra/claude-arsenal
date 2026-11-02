---
name: after-recording
description: Take in a fresh gameplay or commentary recording before any edit. Check the audio tracks and mic level, file and label the raws, scan every raw for the creator's identity on screen (account names, OS username in paths, real name, notifications), start the transcription detached so it survives the session, read the creator's spoken markers, score the performance, and write the hand-off for the rough cut. Use for "recording done", "I recorded", "new footage", "file the raws", "ingest this recording", or before skill roughcut or film on a new raw.
---

# After recording

status: beta

Run once per new recording, with the recorder stopped. Nothing here edits; it makes the raw safe and readable for the cut.

## 1. Tracks and level
- Probe the file (`ffprobe -show_streams`): resolution, frame rate, codec, and the audio tracks. Record with separate
  tracks so the edit can mix: 1 = the full mix, 2 = the mic only, 3 = the game only (more for a second voice or a second
  angle).
- Mic speech should sit around -22 to -26 dB RMS on its track. A track near -90 dB means the mic was muted (a hardware
  mute button, or another audio app grabbed the device): tell the creator at once, before they record again.
- Never edit or trust the recorder's config files: read what was recorded from the recorder's own log and the probe.

## 2. File and label
- Move each raw to `<project>/raw/<game>/<date>_<game>_part<N>_session<M>.<ext>` (plus any second-angle files) BEFORE
  transcribing, so every transcript and EDL carries the label. Non-game takes go in `raw/_channel/`.
- Screenshots the creator took for thumbnails are kept for good (stills are never deleted).
- When one session covers a long game, keep every raw until the Part 2 decision is settled.

## 3. Privacy scan (faceless creators)
- Scan every new raw for the creator's identity: platform account names and persona (Steam, Epic, Xbox, PSN), the OS
  username in file paths, their real name, Discord or messaging popups, phone notifications, friends' names. A practical
  method: sample frames (1-2 per second, plus every scene change), OCR them, and match against a private identity list
  kept OUTSIDE the project repo (a dotfile in the user's home), case-insensitive with fuzzy matching.
- Every hit becomes a blur box (fractions of the source frame) with its time span, handed to the EDL. Popups get a
  "look:" note to check by eye.
- Never print, log or commit an identity value; reports name the kind of hit and the time only.
- Optional gate: make the render step refuse a cut where a scan hit has no covering box, and the delivery check fail a
  readable one.

## 4. Transcribe, detached
Long jobs die with the session that started them, so run them detached with `scripts/job.py` (in this plugin):
```
python <plugin>/scripts/job.py start tx_<name> -- <your transcriber> <raw>
python <plugin>/scripts/job.py status tx_<name>     # running / done / FAILED (exit N) / DIED
```
- Transcribe the mic track. Optional tools: Whisper or WhisperX (word-aligned), a second model as a second ear, a laughter
  detector. Blocks recorded separately get transcribed per block, then merged into one transcript with part markers.
- When it ends, read the log tail plus any warning lines (hallucinated phrases, repeat loops). Never poll a running job;
  never re-run a passing one "to be sure".
- Free the GPU when done if the creator games on the same machine.

## 5. Read the creator's markers
Agree spoken markers with the creator before recording and pull them out of the transcript into a block at the top:
- "clip" right after a moment they would send a friend (the 20 s before it = a top moment, a first Short candidate)
- a thumbnail screenshot key press (a frame candidate)
- an about-to-try line followed by a yell, laugh or hit within 15 s (a setup/payoff pair, a Short hook)
- a short recap at the end of each block (raw words for the title, never rewritten)

## 6. Score the performance
Measure talk share, silences and words per minute against the creator's own recent median, plus mic level and clarity.
A weak number becomes one line in the next recording's plan and one bullet to the creator, never a lecture.

## 7. Index and hand off
- Add the raw to the project's file index (what, when, length, part).
- Write `<project>/cuts/<ep>/BRIEF.md` STATUS: what was recorded, length, markers, problems found.
- Then skill `roughcut` (gameplay) or skill `film` (VO film), in a fresh session.
