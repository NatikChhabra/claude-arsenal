---
name: song-from-idea
description: "Take a song from an idea (a character, an RP story beat, a mood, a guitar riff) to a written song with structure, lyrics and chords. Use when the owner wants to write a song or start a music project."
---
# Song from idea

status: draft

The front door of music-studio. Ends with a song sheet the other skills build on.

## Inputs to collect (ask only what the request doesn't answer)
- Purpose: character theme, RP event, ad jingle for an in-world business, diss track, personal song.
- Reference songs or artists (2-3), language (English, Hindi, Hinglish, Punjabi), mood, target length.
- His guitar part if one exists: a voice memo or DI recording, or the chords he plays.

## Steps
1. Concept in one line: who is singing, to whom, about what, and why now (the RP moment).
2. Structure: pick a form (e.g. intro, verse, pre, chorus, verse, pre, chorus, bridge, chorus) and a target BPM and key
   that suit his guitar (open chords in E, A, D, G, C are easiest; use a capo map for the singer's range).
3. Chords and hook: chorus hook first. If he has a riff, build around it.
4. Lyrics: concrete details from the character and the RP world, no stock phrasing, syllable counts that sit on the
   melody. Mark stressed syllables. Hinglish lines keep natural word order.
5. Melody guide: note the chorus melody as scale degrees or a hum-along reference so the vocal route can follow it.
6. Write the song sheet: `songs/<slug>/SONG.md` (concept, structure, BPM, key, chords per section, lyrics, melody notes,
   references) in the project using the skill.
7. Hand over to `vocal-route` to choose how the vocals get made.

## Review before showing
- Would a listener remember the chorus after one play? Is every lyric line specific to this character or moment?
- Read lyrics aloud at tempo: no tongue-twisters, no filler words added only for rhyme.
