---
name: guitar-capture
description: >-
  Record and prepare the owner's guitar parts (DI or mic, to a click) so they can drive the song: a clean take, a beat
  and bar map, a chord chart and an optional MIDI sketch, plus the tone chain. Use when he has a riff, a progression or
  a full guitar part, for "record my guitar", "turn this riff into a song", or a take that drifts off tempo.
---

# guitar-capture

status: draft (full workflow; beat map tool tested; promote to beta after the first real take)

Sources and licences: research/04_production_and_video.md §2. The guitar is his voice in every song: it stays audible
and central.

## 0. Level check, then one play sheet
Write parts for the player he is, measured, not guessed. A first draft pitched by guesswork was called "sub par"; he
asked: "ask me more questions rather than guessing".
- Ask, a few words each: how long he has played; barre chords (can he switch to them in time?); thumb on the bass while
  fingers pick on top (Travis style); harmonics; notes past fret 5; thumb slap and chuck; can he play 3 minutes without
  stopping; pick or fingers; how long he will practise. Ask the feel too: what the ending should feel like and 1-2
  reference songs.
- Ask for about a minute of songs he already plays, then measure it:
  `uv run --with librosa --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/guitar_level.py <take.wav>`
  (tuning, clipping, notes per second, steadiness, picked vs strummed, range, hesitations, per stretch of playing).
  Write the part at about 60-70% of his best clean notes/s. Tell him to tune if it reads more than 10 cents off and to
  move the mic back if anything clipped.
- Sound big with moves a 2-4 month player can do, on the chord shapes he already knows (no barre chords): natural
  harmonics 12 frets above the capo for an intro; the hook as a single-string tune with hammer-ons and pull-offs;
  thumb on every beat with a pinch on 1 and a hammer-on inside each chord; palm-muted builds; chucks on 2 and 4;
  one bar of dead silence before the last chorus; a thumb slap (kick) plus chuck (snare) groove for the last chorus.
  For an ending that lifts, finish on the relative major (from Em-shape home to the G shape), not the home minor chord.
- Write every move as real 6-line tab (thin string on top, frets from the capo, counts under each bar, h/p, x for a
  chuck, <12> for a harmonic, T/i/m/r for fingers), not as named moves with a symbol key: he could not follow
  "TUNE / BELL / PICK / MUTE / STOP" boxes and asked for tabs. Check each tab note against the chord under it.
- Deliver ONE sheet, never several: chord diagrams with finger numbers (mark the bass string and the hammer finger),
  the tab of each move with a tick box, in the order they come, then the song top to bottom (one row per section,
  one coloured box per bar, the move and a feel word), then a short record checklist (take names). Add a slower
  practice play-along (about 20 BPM under) next to the real one, both in one clean FINAL folder.
- Before sending: play the tab back as plain plucked notes over the click (Karplus-Strong in numpy, no samples) and
  check every row lands on its bar, the drop is silent and the last chorus is loudest; send that render as a slow
  "how the tab goes" guide. After copying to his PC, read the file back from the PC and compare pixels: a copy sent
  in the same batch as the write once delivered the old sheet ("it's the same").

## 1. Record
- DI through an audio interface, 48 kHz / 24-bit, peaks around -12 to -6 dBFS (room for transients). A phone memo is
  fine for an idea, never for the release take.
- To a click at the SONG.md BPM whenever the part will be produced or the video cut to it. Free time only for a
  rubato intro, marked as such.
- Record 3+ full takes plus punch-ins per section; keep every raw file untouched in `songs/<slug>/guitar/raw/`.
- Give him a play-along, not only a click: click, a soft low note on each chord's root (so he hears every change), a
  bell at each new section, and his own vocal placed where it will sit. A bar chart (bars, chords, how hard to play)
  goes with it. Ask for the parts a beginner can play: the whole song once through (twice), a riff of the hook tune on
  2-3 strings with one finger, and body taps on the guitar (palm on the side = kick on 1 and 3, knuckles on the top =
  snare on 2 and 4) so even the drums are his guitar. He asked for this himself: "it should feel my own".

## 2. Map it
`uv run --with librosa --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/beatmap.py map <take.wav> --click <check.wav>`
- Prints tempo, beats, bars, sections; writes `<take>.beatmap.json`. Listen to the click file: the high click must sit on
  "one". Low downbeat confidence (< 0.05) = trust the beats, set bar lines by ear.
- A take that drifts more than a few BPM across the song: re-record to the click, or tempo-map the DAW to the take
  (a deliberate live feel), never both.
- Better downbeats: Beat This! (CPJKU, MIT code and weights, beats and downbeats, state of the art) is the upgrade
  path once it is installed on his PC (registry: TRIAL); madmom's models are non-commercial, never on released work.

## 3. Chords and notes
- He knows what he played: write the chord chart from him first (fast, exact).
- Spotify Basic Pitch (Apache-2.0; `basic-pitch <out-dir> <take.wav>`) gives a MIDI sketch: 79.0 onset F-measure on
  GuitarSet vs 91.2 for the best research model, so always clean it by hand. MIDI only, no tab.
- Tab export: Klangio Guitar2Tabs (commercial; Guitar Pro / MusicXML) when tab is the deliverable. No open audio-to-tab
  model is ready to use (2 Nov 2026).
- Put the chord chart in SONG.md, bar by bar.

## 4. Tone
- Neural Amp Modeler (MIT, VST3 on Windows) or the free TONE3000 plugin (launched 1 Sep 2026, 700,000+ captures, loads
  NAM captures and IRs) into a cab IR. If NAM crashes before its window opens, set it (or the DAW) to the dedicated GPU.
- Match the reference songs' tone by ear and by A/B at equal loudness, never by "louder sounds better".
- Commit the tone only at mix time: keep the DI so the tone can change.

## 5. Hand-off
Clean comp of the take (edits on the grid, crossfades, no clicks), DI and amped versions, beat map JSON, chord chart.
SONG.md Status: "guitar recorded"; next: song-from-idea (if lyrics are open) or produce-arrange.
