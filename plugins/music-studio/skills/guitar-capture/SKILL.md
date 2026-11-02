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

## 1. Record
- DI through an audio interface, 48 kHz / 24-bit, peaks around -12 to -6 dBFS (room for transients). A phone memo is
  fine for an idea, never for the release take.
- To a click at the SONG.md BPM whenever the part will be produced or the video cut to it. Free time only for a
  rubato intro, marked as such.
- Record 3+ full takes plus punch-ins per section; keep every raw file untouched in `songs/<slug>/guitar/raw/`.

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
