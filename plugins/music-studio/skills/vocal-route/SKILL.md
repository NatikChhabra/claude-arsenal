---
name: vocal-route
description: >-
  Choose and run the way a song gets its lead vocal when the writer (a guitarist who can't sing) won't be the final sung
  voice: guide plus pitch fix plus voice conversion, vocal synthesis, generation from his guitar, rap, or a real singer,
  picked by language, melody fidelity and release terms, proved on one chorus with blind listeners before the full song.
  Use whenever a song needs vocals, for "make it sing", "AI vocals", "voice for my song", or a vocal that sounds fake.
---

# vocal-route

status: draft (full workflow; promote to beta after the first real song)

The owner loves singing and can't sing well. The vocal must sound great AND keep the song his: his melody, his words,
his phrasing. Every tool's real abilities, prices and terms: [references/routes.md](references/routes.md). Sources:
research/03_vocal_tools.md.

## 0. Inputs
SONG.md (lyrics passing lyric_lint, melody guide, language, release intent) and the guitar take if one exists. No
SONG.md = run skill song-from-idea first.

## 1. Pick the route (one table lookup, then a reason)
| Situation | Default route |
|---|---|
| English, he wants his exact melody | B (Synthesizer V 2 Pro Voice-to-MIDI from his guide), or A |
| Hindi, Hinglish or Punjabi lyrics | A (his guide, pitch-fixed, converted to a voice he owns or licensed) or his own vocal pitch-fixed; no commercial singing synth sings Hindi (2 Nov 2026) |
| A fast demo to hear the song | C (Suno cover of his guide, or ACE-Step locally) |
| The style allows rap or spoken word | D (his own voice) |
| The song is the centrepiece of a release and a willing singer exists | E |
| Monetised release | never a free-plan generator (Suno free: Suno owns it; Eleven free: non-commercial); never Udio (no downloads) |
Write the pick and the reason in SONG.md's decisions log. Unclear between two = run both on the chorus in step 3.

## 2. Range and key
- Find the chosen voice's comfortable range (the synth voicebank's stated range, the converted voice's model, the
  singer's own). Transpose the song (capo for guitar) so the chorus peak sits 1-2 semitones under the top of it.
- Update Key, Capo and Range in SONG.md before any guide is recorded: a re-key later means a new guide.

## 3. Chorus first, blind
1. Make ONLY the first chorus with the chosen route (two routes if step 1 was unclear).
2. Clean it: timing to the grid where it should sit, breaths kept, no clicks, de-ess.
3. Measure: `python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <chorus mix> --vocal <vocal stem> --inst <inst stem>`
   (the phone-speaker check: the vocal must not sit under the band-limited instrumental in more than 10% of sung
   windows).
4. Blind listen. Claude cannot hear audio, so the judges are people: the owner plus at least 2 listeners who were not
   told how it was made. Ask them only: "Would you replay it? Does any part sound fake or robotic, where?" One "sounds
   AI" with a timestamp = fix that phrase (breaths, timing, vibrato, consonants) and re-test with a new listener.
   A text-only fresh agent can still read the lyric sheet for mis-stressed words before the listen.
5. Pass = every listener would replay it and nobody flags a fake spot. Then the full song.

## 4. Full vocal
- Same route, same settings and voice for every section (a voice change mid-song is a bug, a feature only when it is a
  second character). Doubles and harmonies from the same voice, panned and lower.
- Comp, tune, time, de-ess; keep 2-3 natural breaths per phrase group. Export the dry lead, doubles, harmonies and
  ad-libs as separate stems for skill mix-master.

## 5. Credits and rights (before the song leaves the machine)
Write `songs/<slug>/CREDITS.md`: route, tool and version, plan tier, voice model or voicebank and its licence, who
owns the guide voice, any human singer and their written consent, the disclosure each platform needs (references
"Release rules"). Missing licence = the song stays private.

## Rules
- Only voices he owns or has written permission for. Never clone or imitate a real artist, never prompt with an
  artist's name.
- The release intent in SONG.md decides the tool tier. A song made on a free plan cannot be "upgraded" to commercial
  later on Suno.
- A vocal that a blind listener flags as AI does not ship, however good the rest is.

## Report
Route and reason, range and key, the chorus result with each listener's words, loudness numbers, open rights items.
