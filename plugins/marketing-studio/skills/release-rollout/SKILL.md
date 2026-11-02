---
name: release-rollout
description: >-
  Run the release of a song or music video end to end: rights and distributor check for AI-assisted vocals, a dated
  calendar from rollout.py with Spotify's pitch and Release Radar floors, assets checklist, per-platform posts, in-city
  RP moments inside the server's rules, and day 1, 7 and 28 read-outs with one change for next time. Use when a song or
  video is finished, for "release this", "when should I drop it", "pitch to Spotify", or a launch plan.
---

# release-rollout

status: draft (full workflow; rollout tool tested; promote to beta after the first real release)

Every platform rule, distributor AI policy and RP licence term with its source:
[references/platforms.md](references/platforms.md). Posts are written with skill social-copy; the campaign around a
bigger launch is skill campaign-plan.

## 0. Gate: is it releasable?
- Skill music-review passed (every row >= 8.5, gates clean). No exceptions for "just a single".
- CREDITS.md complete. The release intent in SONG.md matches every tool's plan (no free-plan generator output, no
  Udio). The distributor's AI policy fits the vocal route (references "Distributors"); CD Baby is out for any AI part.
- Artist identity: the owner is the real artist; art is in-game or clearly stylised, never a photoreal AI person
  (Spotify AI Persona badge).
- The video's rights path is written (skill music-video §0).
Any "no" = stop and tell the owner what blocks the release and the fix.

## 1. Date and calendar
`python ${CLAUDE_SKILL_DIR}/../../tools/rollout.py <release-date> --title "<song>" --out marketing/<slug>/CALENDAR.md`
- A FAIL line = the 7-day pitch and delivery floor is already missed: move the date (recommended) or accept no
  editorial pitch and no first-week Release Radar, in writing.
- Pick a Friday unless the owner's audience data says otherwise (global release day convention; INFERRED).

## 2. Assets (all final before T-10)
Master WAV + encode checked; cover 3000x3000 (design skill); 16:9 video; 3-4 vertical hook cuts from different
sections; Spotify Canvas; lyrics; credits; the RP story in two sentences; the Spotify pitch (social-copy).

## 3. Distribute and pitch
- Upload with honest AI-use answers, language, lyrics, ISRC; request YouTube Content ID whitelisting for his own
  channel (or keep Shorts at 60 s or under).
- Pitch in Spotify for Artists at T-14 (floor T-7): who, what, why, when, where, how; the RP story; the marketing
  plan; accurate mood and genre; no follower counts. Run copy_lint on it.

## 4. Teasers, release day, sustain
Follow CALENDAR.md. Each post is written for its app with skill social-copy; each app gets its own export (no
watermarked cross-posts). In-city moments only inside the server's rules (references "RP servers"). **Nothing posts,
replies or DMs without the owner's explicit OK for that post.**

## 5. Read-outs and the one change
- Day 1, 7, 28 per CALENDAR.md into `marketing/<slug>/RESULTS.md`: the numbers, the winning hook cut, what the
  comments say.
- Compare with his own last release, never with blog benchmarks. Write ONE change for the next release (a hook
  choice, a teaser timing, a format) and add it to this skill or social-copy if it held twice (skill
  workflow arsenal-update).
