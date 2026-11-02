---
name: film
description: Make a cinematic VO story film from gameplay. A story script before recording, the creator's full VO read afterwards, a picture cut with the game's own camera only (no digital zoom, push, shake, slow-mo or stills), motivated transitions, a grade per scene, breath holds, then a motion-aware review where every row scores 8.5 or the film goes back. Use for "story film", "cinematic video", "film this game", "Day N saga", "narrated film", "make it feel like a movie", or any edit where a scripted VO replaces the live mic.
---

# VO story film

status: beta

The format: the creator's live mic is OUT; a full scripted VO they read carries every word; immersion never breaks; no
brand character in the film body. A day-count saga is a standalone film, never "Part N". The film must feel grand: graded
scenes, letterbox where it hides HUD, wide holds, the game's sound and music under the voice.

References in this folder:
- [references/film-script-template.md](references/film-script-template.md): the FILM_SCRIPT.md template.
- [references/recut-rules.md](references/recut-rules.md): the picture rules every shot is picked under.
- VO line rules: [../vo-session/references/vo-script.md](../vo-session/references/vo-script.md).
- Grade, letterbox, music levels, dissolves: skill design, references/edit.md.

## 1. Before recording
- Pick the game for a story it can carry; check the publisher's video policy (music in cutscenes is the usual Content ID
  risk).
- **Story script first** (the film version of a pre-production pack): the question the film answers, the creator's arc,
  the scenes they will play, the honest moments. They read it BEFORE they record and play to it, never off it.
- Plan the shots the film needs: an establishing wide for every new place or act, HUD off, recorded on purpose.

## 2. After recording
- Skill `after-recording` (tracks, privacy scan, transcription).
- **Shot libraries** per session (`footage/s<N>_library.md`): source seconds, a library id, the HUD fix each shot needs
  (clean / letterbox / letterbox + a crop <= 1.3), what moves in it. Times good to +-0.5 s on hero shots, +-2 s elsewhere.
- **Story map** (skill `roughcut` 2b): BUT/THEREFORE links between the scenes.

## 3. The VO script (FILM_SCRIPT.md)
- **Concept on top:** the film's one idea said as a visual mechanism; 1-3 motifs that change state each time they return;
  intensity rising by act with >= 3 real HOLDs; an ending that is an idea, never a fade because the music ended. When the
  music carries a scene, its bar lines decide where a cut or a hold lands (a beat tracker gives them).
- **Built from the creator's transcript:** how they would tell a friend what happened, in their everyday register. Every
  line sourced (`[src: <stem> <mm:ss> | their words]` / `[src: game ...]` / `[src: story <what it bends>]`). Day counts and
  money numbers stay real.
- **Per line:** SHOT (library id + seconds), CAM (`still`, or the game's own move), silences (no VO <= 4 s except planned
  HOLDs), music mood (well under the voice).
- **Rhythm:** 125-165 words per minute of runtime, sentence median 8-11 words, a "but" turn more than once a minute
  (measured on a narrated game-film channel).
- **Gates:** the vo-script checklist; a blind test if you run one. Every line the creator rejects goes into the
  ground-truth file.
- The creator reads it, then skill `vo-session` (record, sync, transcribe what they actually said).

## 4. Picture cut and render
- Mark the EDL as a film so the render step refuses gameplay devices: digital zoom over 1.3 (HUD hiding only), push,
  snap, whip, shake, tilt, slow-mo, freezes, stills, stings, any live mic.
- Cut by [references/recut-rules.md](references/recut-rules.md): the game's own camera only, a dissolve at day changes,
  J/L cuts at scene changes, a grade per scene, breath holds. Bare hard cuts under 60% of all cuts.
- Pre-render check, then preview renders of changed spans only, then one master.

## 5. Review (motion-aware, not frame-only)
A reviewer who judges stills passes films that move badly. Learned on a film cut the creator scored 3.5/10 ("rough zoom,
rough camera, just cuts and bars") after a frame-only review passed it.
- Measure motion, not just frames: per-shot motion (median shift or frame difference), static holds over 2 s, the share of
  bare cuts, VO words per minute, cutscene runs over 30 s, digital moves. Make strips (a row of frames per shot) so motion
  is visible.
- Seven rows, overall = the worst row: picture motion, transitions, grade and look, sound (VO, game, music), VO and story,
  pacing and holds, AI-feel (anything that reads machine-made).
- A FRESH reviewer gets only the strips and the measurements; every row >= 8.5 or it does not reach the creator.
- A re-cut must beat the cut it replaces head to head twice, order swapped (A/B then B/A, a fresh reviewer each time).
- Then the delivery oracle and the hand-off (skill `roughcut` references/gates.md items 2, 3 and 15).

## 6. Shorts from a film
Each Short is a complete mini-story that works with zero context (the film's question -> the turn -> the real number or
reveal), never a mood trailer.
