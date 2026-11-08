---
name: mix-master
description: >-
  Mix the vocal and instrument stems and master the song for streaming, video and in-game playback, gated by measured
  loudness, true peak, the encoded-file check and the phone-speaker vocal check, with the numbers written down. Use when
  stems are ready, for "mix this", "master my song", "it's too quiet", or a vocal that gets lost on a phone.
---

# mix-master

status: draft (full workflow; loudness tool tested; promote to beta after the first real master)

Targets, commands and sources: [references/targets.md](references/targets.md). Video-side levels (music under
voice, film loudness) live in the design skill, references/edit.md §4 and §7: this skill owns the song itself.

## 1. Prepare
- Check every raw take first: a mono mic on a stereo input often leaves one channel silent (a home take on 8 Nov 2026
  had its right channel 45 dB down). Fold such a take to mono from the live channel before any processing, or the
  part plays from one side only. Also check peak level per take: a take whose peaks sit near -24 dBFS needs more input
  gain next time, not more makeup gain now (the noise comes up with it).
- Import every stem at unity, same start. Name tracks by part. Session notes start `songs/<slug>/MIX.md`.
- Pick 1-2 reference tracks from SONG.md; level-match them to the mix before every comparison (louder always sounds
  better to the ear, so unmatched A/B is meaningless).

## 2. Mix (in order; save a version after each)
1. Static balance with faders only, vocal first: the lead sits on top, the guitar right under it (his instrument is
   central), drums and bass glued under both.
2. Subtractive EQ for space: high-pass everything that isn't bass or kick; carve 1-4 kHz in dense parts where the
   vocal sings.
3. Vocal chain: clean (no stacking of denoise on an already processed or converted voice: it goes robotic), EQ,
   de-ess, compression in two gentle stages, short plate or room plus a tempo-synced delay on sends.
4. Glue: drum bus compression light; parallel compression only when the reference asks for it.
5. Automation: ride the vocal so every word is heard; lift the last chorus.

## 3. Gate the mix
`python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <mix.wav> --vocal <lead.wav> --inst <instrumental.wav>`
- Phone-speaker check: vocal buried in at most 10% of sung windows (400 Hz-8 kHz is what a phone plays). Over that =
  more vocal level or less instrument in that band, then re-measure.
- The owner listens on headphones, a phone speaker and (if it plays there) in the game. Claude reports numbers and the
  owner's words, never "it sounds".

## 4. Master
1. Chain per references; ceiling -1 dBTP (or -2 dBTP when the master is louder than -14 LUFS).
2. `python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <master.wav> --target streaming` (or `club`, `ingame`).
3. Encode check: make the AAC/MP3 a platform would, measure it again; true peak over the ceiling = lower the ceiling.
4. Matchering is allowed as a starting point against a well-chosen reference; its output is measured like any other.

## 5. Write it down
MIX.md: references used, the final numbers (integrated, LRA, true peak, encoded true peak, phone-check share), the
chain, and what changed after each listening note. SONG.md Status: "mastered"; next: music-video and marketing-studio.

## Ship bar
Every row in skill music-review >= 8.5 for the audio rows; 0 FIX from loudness.py on the master and the encode.
