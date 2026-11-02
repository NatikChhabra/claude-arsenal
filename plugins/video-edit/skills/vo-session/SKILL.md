---
name: vo-session
description: Run a creator's voice-over recording from a finished script to placed, verified takes. The creator reads the script first and says every line their own way; then record with the live setup copied, keep a verified copy, sync to the picture, check level and clarity, transcribe what was ACTUALLY said, re-check every kept line for truth, split per-line files and place them with the live mic muted underneath. Use for "record the VO", "voiceover done", "VO session", "narration", "watch-back", "pickup line", or after a VO script passes its gates.
---

# VO session

status: beta

Every long video can carry a watch-back VO; a VO film's VO carries every word (skill `film`). Script rules and template:
[references/vo-script.md](references/vo-script.md). The script is a guide; the transcript of the take is the truth.

## 1. Before recording
- **Script gate:** every line sourced and passing the checklist in references/vo-script.md; the blind test if you run one.
- **Send the script to the creator to READ FIRST.** They say every line their way. Give them a preview of the picture with
  a guide subtitle file (one cue per line, in its slot) so each line shows when it is due.
- **Copy the live setup:** same mic, spot, angle, gain and the same voice chain they use for gameplay (film ADR practice:
  match the live recording; no corrective EQ afterwards). A 5 s test, played back, before every session.
- **Performance help for a non-actor:** tell it to one friend, more energy than feels normal; read a line once, look at
  the screen, say it; flub = say the whole line again and keep rolling; each important line twice (full, then shorter);
  a break every 10-15 min; a 2-3 min warm-up.

## 2. After "voiceover done"
1. **Keep a verified copy:** every source file into `<project>/cuts/<ep>/vo/`, bytes and duration equal to the original.
   Files named by their slot (`0008.wav` = the 0:08 line) place themselves. Agree a retention rule for the originals with
   the creator; default: remove them from the recorder's folder only after the video is live and verified.
2. **Sync** each take to the picture. If the take carries the picture's audio (the preview played into a monitored track),
   cross-correlate ~5 s windows of it against the picture's own audio so pauses, rewinds and re-takes all map right;
   otherwise place by slot name. Output: one VO track + a JSON of offsets.
3. **Level and clarity:** the take sits at the same level and clarity as the live mic (VO and live speech within about
   +-1.5 LU).
4. **Never post-process a disguised voice back toward natural,** and add nothing the live voice does not have.
5. **Transcribe the take** (detached: `scripts/job.py start tx_vo -- <your transcriber> <vo.wav>`). What they SAID is the
   line from now on, not the script.
6. **Truth re-check per kept take:** it still matches the picture and the real day/money numbers (else re-say or cut).
   Best take per line = the last clean one by default; trim words after the punch; never join two takes into a claim the
   creator did not make.
7. **Per-line files:** split the VO track into one file + transcript per line; each goes on its slot in the EDL with the
   live mic muted under it (one voice at a time; the game keeps playing). A strong swear in a VO line is bleeped like a
   live one.
8. **Ground truth:** every line they changed or refused, plus what they said instead, goes into the ground-truth file.

## 3. Then
Radio cut first (VO + live lines + game sound, no music or SFX, one eyes-closed listen at 1x), then picture to it (skill
`roughcut` 2c), then the rest of the edit and its gates.

## Single pickup line
Cut that stretch of the rough cut to `vo/<line>.mp4`, the creator records the one line over it, then steps 2.1-2.7 for that
file only.
