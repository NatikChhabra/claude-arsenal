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
Better than single strums: cut his continuous strumming into half-bar phrases (beat-track the take, keep phrases
whose chroma matches one chord), then slice each phrase at its onsets and drop every slice on the nearest 8th of the
grid (no time-stretch). Keep his own tempo as the song tempo so nothing slows down. To check timing, compare onset
offsets against a known-on-grid reference: librosa's onset times run about 25 ms late at hop 512, so judge the spread
(IQR), not the median.

A stitched backing is still held to the energy map: never send his guitar alone as "the song" (8 Nov 2026: "missing
everything").

### No DAW on hand: a band from CC0 sample libraries, played from code
Real recorded instruments, release-safe, no generator: VSCO 2 Community Edition (Versilian Studios, CC0: upright bass
pizz, cello and violin sections, upright piano, glockenspiel, tambourine, shaker) and Swirly Drums (Karoryfer, CC0: a
brush kit with kick, snare, hats, ride, floor tom and brush stirs). Salamander Drumkit is CC-BY-SA: skip it for releases.
GitHub zip downloads time out on his PC; shallow `git clone` works. Download into `<models-root>\arsenal\samples\`.
- Check every sample's pitch with pYIN before using its name: VSCO strings are named an octave low (a file called C1
  sounds C2) and its glockenspiel files sound an octave above their names.
- Write parts note by note on a fixed bar grid (sections in 2- or 4-bar multiples, chord loop per section), nearest
  sample pitch-shifted by resampling (3 semitones or less), velocity layers by dynamic, 5-8 ms timing and 6-8% velocity
  humanising, round-robins rotated. Lines of a spoken or free-time vocal go on the grid by their natural gaps, each
  start rounded to the nearest 8th; chorus lines start on 2-bar slots.
- Mix checks that caught real problems: per-section RMS arc (see music-review gates), octave-band balance against the
  1 kHz band (his low voice plus acoustic guitar ran 250 Hz +11 dB: cut 250 Hz on vocal, guitar, piano and cello),
  and a click scan (slices cut at an onset need a 3-5 ms fade-in, not only a fade-out).

## 4. Check
- Play each section boundary: does the energy map's change happen and is it felt in the first second?
- Mute test: mute the guitar; if the song still works the guitar isn't central enough for this artist. Mute the
  vocal; the instrumental should still carry the hook.
- The owner listens to the arrangement against one reference at matched loudness (Claude cannot hear: never claim
  "it sounds" anything).

## 5. Hand-off
Bounce stems at 48 kHz / 24-bit from bar 1, same length, no master processing: drums (or kick, snare, rest), bass,
guitar(s), keys/pads, FX, lead vocal, doubles, harmonies. SONG.md Status: "produced"; next: mix-master.
