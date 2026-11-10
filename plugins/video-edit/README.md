# video-edit

Method skills for editing a voice-led gameplay or commentary channel: from a fresh recording to a scored rough cut, a
cinematic VO film, and a recorded voice-over. Built from a working faceless gaming-comedy pipeline, with the channel's
identity and project tools removed. Every tool step is optional: each one names what to measure, so any tool that
measures it will do.

How things look and sound (zoom budget, text, motion feel, SFX placement, music levels, grade) is not here: it lives in
the design plugin, **skill design, references/edit.md**. These skills decide what happens when; that file decides how.

## Skills
| Skill | Use for | Output |
|---|---|---|
| `after-recording` | a new recording: track and level check, filing, privacy scan for the creator's identity on screen, detached transcription, spoken markers, performance score | labelled raws, transcript, blur boxes, BRIEF.md |
| `roughcut` | a gameplay commentary edit: concept + game research first, find the comedy, story map with BUT/THEREFORE links, EDL rules, captions, brand character overlay, quotable moments, gates, self-score | CONCEPT.md, GAME.md, progression.md, missed_funny.md, EDL, rough cut, report |
| `film` | a cinematic VO story film: story script, full VO, the game's own camera only, motion-aware review | FILM_SCRIPT.md, shot libraries, film cut |
| `vo-session` | recording a VO from a script: read first, record with the live setup, verified copy, sync, transcribe what was said, truth re-check, per-line placement | per-line VO files, ground-truth log |

Flow: `after-recording` -> `roughcut` (gameplay) or `film` (VO film) -> `vo-session` when a VO is scripted -> back to
the cut for its gates.

Shared references:
- `skills/roughcut/references/edit-rules.md`: structure, cuts, comedy engines, on-screen words, safety.
- `skills/roughcut/references/gates.md`: the 15 gates a cut passes before anyone sees it.
- `skills/vo-session/references/vo-script.md`: VO line rules N1-N15 and the script template.
- `skills/film/references/recut-rules.md` and `film-script-template.md`.

## scripts/job.py
Runs a long command (transcription, render, caption check, test suite) detached from the agent session, so it survives
the session ending. Stdlib only, Python 3.8+, Windows, macOS and Linux.
```
python scripts/job.py start <name> -- <command...>   # writes <jobs>/<name>.log and <name>.json, returns at once
python scripts/job.py status [<name>]                # running / done / FAILED (exit N) / DIED (re-run it)
python scripts/job.py selftest                       # starts two tiny jobs, checks done + FAILED (exit 3)
```
- `<jobs>` = `$JOB_DIR`, else `./logs/jobs` under the current directory. Run `status` from the same directory or set
  `JOB_DIR`.
- The command's `TMP`/`TEMP`/`TMPDIR` point at `<jobs>/../tmp` (or `$JOB_TMP`), so big renders fill the project's drive,
  not the system drive. `PYTHONUTF8=1` is set for the command (non-Latin transcripts print safely on Windows).
- `DIED` = the status file says running but the process is gone (the machine slept or rebooted); `DIED (never started)`
  = no pid was written within 30 s.
- Read the log tail and its warning lines when a job ends. Never poll a running job; never re-run a passing one.

## tools/watch.py (the watch pack)
Claude can't play a video, so this turns a whole render into one time-aligned text pack: every 0.5 s, the words, the
picture (cut, still/slow/fast, frozen) and the sound (momentary LUFS, hits, silence), with flags where timing breaks
(DEAD, OVERLOAD, STEP, UNCUED, FLASH, FROZEN, SILENCE, OFFBEAT with a beat map). Needs numpy and ffmpeg.
```
uv run --no-project --with numpy python tools/watch.py <video> [--words words.json] [--beats beatmap.json] [--sheets]
uv run --no-project --with numpy python tools/watch.py --selftest
```
Read watch.md top to bottom before any review; open a sheet only where the text points. It adds to watching the render
at 1x, never replaces it.

## scripts/lut.py (our own LUTs)
Bakes film-style .cube LUTs (luminance S-curve with toe and shoulder, highlight roll-off, split tone): `film`,
`film_night`, `warm_day`. Stdlib only. `python scripts/lut.py film --out luts`, then
`ffmpeg -vf "lut3d=file=luts/film.cube:interp=tetrahedral"`. A/B each on its own footage first (design edit.md).

## Optional tools the skills mention
ffmpeg / ffprobe (probe, cut, `ebur128` loudness, `blackdetect`, `freezedetect`), Whisper or WhisperX (word-aligned
transcripts), a second ASR model as a second ear, jrgillick/laughter-detection (MIT), an OCR engine for the privacy scan,
a beat tracker, a CLAP model to search a sound library by meaning, frame interpolation (RIFE). None is required.

## Rules these skills hold
- Read the whole recording before any claim about it; every claim carries its timestamp.
- On-screen words are the creator's exact words or the game's real words.
- Every device answers one line the creator said or one thing the game did.
- A brand character is the creator, comes only from its approved source, and is never squashed, stretched or deformed.
- A disguised voice is never post-processed back toward natural.
- Nothing reaches the creator before it passes the gates and a fresh blind review.

## Install
```
/plugin install video-edit --marketplace NatikChhabra/claude-arsenal
```
Or `/plugin marketplace add NatikChhabra/claude-arsenal`, then `/plugin install video-edit@claude-arsenal`. More options: the [marketplace README](../../README.md).

## The full engine (reuse it, never rebuild)
These skills carry the method. The working engine they came from runs on the owner's PC: a JSON-EDL renderer with
captions, SFX on cues, ducking and 9:16, an acceptance oracle, a watch pack, transcription, beat tools, CLAP sound
search (also inside a recording), stems, mattes, motion graphics, LUTs, thumbnails and Shorts checks, each with a
selftest. Its own reuse guide (`tools/REUSE.md` in that project) lists every tool and how another project calls it.
On the owner's PC, call those tools instead of writing new ones; a missing feature goes in there as an opt-in flag,
then a lesson worth sharing comes back here.
