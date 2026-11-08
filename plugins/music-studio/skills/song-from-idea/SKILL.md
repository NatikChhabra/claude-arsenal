---
name: song-from-idea
description: >-
  Take a song from an idea (a character, an RP story beat, a mood, a guitar riff) to a finished song sheet: brief,
  inventory, form, BPM and key, chords, a melody guide and lyrics that pass lyric_lint and a fresh blind read. Use when
  the owner wants to write a song, start a music project, write lyrics, or turn a riff into a song; it is the front
  door of music-studio and every other music skill reads its SONG.md.
---

# song-from-idea

status: draft (full workflow; tools tested; promote to beta after the first real song)

Ends with `songs/<slug>/SONG.md` (from `templates/SONG.md` in this plugin), the one sheet every other music skill reads
and updates. Craft rules and their sources: [references/songwriting.md](references/songwriting.md).

## 0. Read first, ask once
- Read the request, the character's notes and any earlier SONG.md for this character. Never ask what they answer.
- Ask the rest in ONE batch, each with a suggested default: who sings and to whom, the moment it belongs to, 2-3
  reference songs and what to take from each, language, release intent (private / in-city / public / monetised:
  it decides the vocal tools and licences later), deadline.
- If he has a riff or chords: get the recording first (skill guitar-capture), then write around it.

## 1. Brief and inventory
1. Fill the Brief block of SONG.md.
2. List 8-12 inventory items only this character or moment has (names, streets, objects, numbers, rituals, lines they
   really say in RP). Lyrics come from these. A song with no inventory items in a verse is a stock song.
3. One-line concept: "[who] tells [whom] [what] because [the moment]". If the nearest other song could carry the same
   line unchanged, it is a category idea: redo it.

## 2. Shape before words
1. Form with bar counts, BPM, key, capo, feel (references §1, §6). Compute the first-chorus time:
   bars before it x beats per bar x 60 / BPM. Over ~45 s needs a written reason in the decisions log.
2. Chords per section, bar by bar. Guitar-friendly keys first; the capo serves the voice range.
3. Hook first: the chorus title line and its melody shape (scale degrees per syllable, highest note marked) before
   any verse. Hum it over the chords; if it isn't singable after two listens, it isn't the hook.
4. Mark where the 15-30 s clip moment is (marketing-studio cuts Shorts and Reels from it).

## 3. Three directions, pick one
Write 3 chorus drafts that differ on a named axis (angle, image, or rhythm), each with its title line. Say which one
carries something only this character has, pick it, and log why. When the owner is in the conversation and the
direction is open, show all three (text only, one line of why each) and let him pick or combine.

## 4. Lyrics
0. **When he brings his own words (a personal song), they are the song.** Start from his sentences in his order; fix
   spelling and grammar only. No rhymes he didn't write, no images he didn't give, no new lines: a gap gets filled by
   asking him for a real memory and using his answer's words. A polished rewrite of a personal lyric reads as AI to
   him (8 Nov 2026: a rhymed, restructured version with invented details was called "AI af"; his raw words were not).
1. Verses from the inventory: at least two items per verse; one image per line; no line that fits any song.
2. Prosody pass (references §2): speak every line over a click at tempo; stressed syllables on strong beats.
3. Matching lines match: syllable counts and stress patterns line up across verses and repeated sections (§3).
4. Hinglish and Hindi in Roman script, spoken word order, casual spelling a singer reads at sight.
5. Gate: `python ${CLAUDE_SKILL_DIR}/../../tools/lyric_lint.py songs/<slug>/SONG.md --bpm <BPM>`.
   0 FAIL. Each WARN fixed or defended in one sentence in the decisions log.
6. Fresh blind read: give a fresh agent ONLY the lyrics (no brief, no reasoning) and ask: what is the song about, who
   is singing, which line would you quote, which line sounds machine-written or could be in any song. A wrong "about",
   no quotable line, or a named machine line = rewrite that part and read again with a new reader.

## 5. Melody guide and hand-off
- Record or describe the chorus melody (scale degrees, range lowest to highest). A hummed phone memo of the owner is
  the best guide; pitch accuracy does not matter at this stage (vocal-route fixes or replaces it).
- Set SONG.md Status to "written" and Next step to skill vocal-route.

## Report
Concept line, form with first-chorus time, the chosen chorus and why, lyric_lint result, the blind reader's answers,
and the one open question if any. Never claim a check that did not run.
