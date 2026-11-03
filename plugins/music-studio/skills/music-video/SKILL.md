---
name: music-video
description: >-
  Plan, shoot and edit a music video for a finished song (GTA RP footage, a lyric video, a performance, or stylised art):
  rights decision first, a treatment with one visual idea, a shot list per section, capture, a beat map and beat-locked
  edit measured cut by cut, a native 9:16 re-cut, Canvas and covers, then QC and blind review. Use when a song is mastered
  and needs a video, for "make a music video", "lyric video", "edit this to the beat", or vertical cuts of a song.
---

# music-video

status: draft (full workflow; beat and cut tools tested; promote to beta after the first real video)

Music videos are the top priority of this arsenal. Rights, capture, beat grammar and every platform spec with its
source: [references/footage-and-specs.md](references/footage-and-specs.md). Picture, text, motion and video QC rules
live ONLY in the design skill (references/video.md and edit.md): read the sections named below, never restate them.

## 0. Rights gate (before any shoot)
Read references §1. Record in SONG.md's decisions log which path this video takes (non-monetised GTA cut / licence
request / non-GTA video for the monetised release), the server's filming rules, and the consent of every player who
will appear. Unclear = ask the owner once with the three options and a recommendation. No path written = no shoot.

## 1. Treatment (one page, `songs/<slug>/video/TREATMENT.md`)
1. The thesis: "In this video, [a thing from the character's world] becomes [a visual device]". If another artist's
   video could use it unchanged, redo it.
2. The arc in three beats that follow the song's energy map (SONG.md "Arrangement"): where the character starts, what
   turns at the bridge, where they end.
3. Motifs with a state change (an object that appears in verse 1 and returns changed in the last chorus).
4. At least 3 held moments (a shot that stays 2+ bars) so the cuts mean something.
5. Locations, cast (characters and the real players behind them), props, time of day per section.
6. Three directions on a named axis (look, structure, or format) when the owner is present; pick one with a reason.

## 2. Shot list and shoot
- Per section: shots with angle, action, duration in bars, the lyric line they carry. Spares per references §2.
- Shoot day sheet: server, time, who is needed, the in-game time/weather, the capture settings, a test clip checked
  before the cast arrives.
- Never film people who did not agree; never on a server that forbids it.

## 3. Beat map and edit
1. `uv run --with librosa --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/beatmap.py map <master.wav> --click <check.wav>`;
   listen to the click; export the beat and downbeat times as markers for the editor.
2. Rough cut: structure first (which footage per section, the held moments), then cuts to the grid (references §3).
3. Text: lyrics only where they help (a lyric video, a hook line); exact sung words; on screen at least
   max(0.7 s, 0.09 s x characters); never over a face; type and motion per design references/video.md §3 and
   edit.md §2.
4. Grade per section with one look per section, never stacked (design edit.md §6).
5. Measure: `beatmap.py cuts <map.json> <cuts.txt|edl.json> --fps <fps>`: >= 90% on grid outside marked off-beat
   cuts; every off-grid cut either becomes on-grid or gets its reason in the edit list.

## 4. Vertical and extras
- 9:16 is its own edit, re-laid out (subject re-framed, text re-placed into the app's safe area), never a centre crop
  of the 16:9. 3-4 different 15-30 s hook cuts (chorus, the riff, the line tied to the RP story beat) for
  marketing-studio's tests. Shorts over 60 s only once Content ID is whitelisted for his channel.
- Spotify Canvas 3-8 s loop, no text naming the song or artist. Thumbnail and covers: design skill references/video.md
  §1 (click incentive, one focal point at phone size) and creator skill thumbnail's method.

## 5. QC and review
- Video QC table: design references/edit.md §7 (loudness, true peak, black and frozen frames, flashes <= 3 per
  second, A/V sync, identity redacted). The audio in the video is the mastered song: re-measure with
  `tools/loudness.py` on the rendered file.
- Watch the whole render, picture and sound, start to end, before any review ask. Then the watch pack with the beat
  map: `uv run --no-project --with numpy python ${CLAUDE_SKILL_DIR}/../../../video-edit/tools/watch.py <render.mp4>
  --beats <map.json> --sheets` (DEAD, FLASH, FROZEN, OFFBEAT flags; a held shot the treatment planned is defended in one line).
- Grade with our own LUTs only: `python ${CLAUDE_SKILL_DIR}/../../../video-edit/scripts/lut.py film --out luts`, A/B on the
  real footage (design references/edit.md, film look).
- Skill music-review: every row >= 8.5, plus a fresh blind review of the video by a reviewer with no build context.

## Deliver
16:9 master, each 9:16 cut, Canvas, thumbnail(s), the edit list and beat map, the rights note. Nothing reaches the
owner as "final" until every check above ran; the whole package at once.
