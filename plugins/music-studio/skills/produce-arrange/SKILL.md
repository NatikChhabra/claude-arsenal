---
name: produce-arrange
description: >-
  Build the full arrangement around his guitar and the vocal (drums, bass, keys, pads, ear candy) from an energy map of
  every section, in a DAW Claude can drive through MCP (REAPER by default), and bounce clean stems for the mix. Use after
  the song sheet and the guitar take exist, for "produce this", "make a beat", "arrange my song", or a demo that sounds empty.
---

# produce-arrange

status: draft (full workflow; promote to beta after the first real song)

DAWs, MCP servers and stem tools with their real abilities: [references/daw-and-stems.md](references/daw-and-stems.md).

## 1. Energy map before any sound
From SONG.md's form and the beat map, write one row per section: energy 1-10, what enters, what leaves, the one new
thing the ear gets. Rules:
- Every section change adds or removes at least one element a listener notices in its first second.
- The first chorus is the first 8+ of the song; the last chorus is the peak (a new layer, a lift, or a drop-out before
  it). The bridge differs in texture, not only chords.
- Leave one bar of space or a fill before each chorus (the pre-chorus tension the chorus releases).
Put the map in SONG.md under "## Arrangement".

## 2. Reference and palette
Pick the 2-3 reference songs from SONG.md; note per reference: tempo, kick/snare character, bass role (root notes,
808, picked), where the guitar sits, the vocal's space. Choose sounds that match the references, not presets by name.

## 3. Build (DAW via MCP or by hand)
1. Session at the SONG.md BPM, grid locked to the guitar take's beat map (or tempo-mapped to it).
2. Drums and bass first, locked to the guitar's groove; then harmony (keys, pads) staying out of the guitar's
   register; then the vocal's space: nothing dense at 1-4 kHz where the lead sings.
3. Ear candy only at section changes (a reverse swell, a drop-out, a fill), each with a reason in the energy map.
4. Generated material (ACE-Step Vocal2BGM, Suno stems): a starting point to replace or layer, never the final drums
   unchanged. Licence of each piece into CREDITS.md.
5. Save a new project version before each Claude-driven change; one change per step, listen, keep or revert.

### Stopgap: a backing from loose takes
When the only guitar audio is chord practice (not the song to a click), slice single strums by chord (chroma template
match per onset), re-sequence them at a fixed BPM, and place each vocal line on the next half-bar so the backing follows
his phrasing. It gets a demo out the same day, but say plainly that it is stitched: one played-through take to the
click is the real fix and always the next ask.

## 4. Check
- Play each section boundary: does the energy map's change happen and is it felt in the first second?
- Mute test: mute the guitar; if the song still works the guitar isn't central enough for this artist. Mute the
  vocal; the instrumental should still carry the hook.
- The owner listens to the arrangement against one reference at matched loudness (Claude cannot hear: never claim
  "it sounds" anything).

## 5. Hand-off
Bounce stems at 48 kHz / 24-bit from bar 1, same length, no master processing: drums (or kick, snare, rest), bass,
guitar(s), keys/pads, FX, lead vocal, doubles, harmonies. SONG.md Status: "produced"; next: mix-master.
