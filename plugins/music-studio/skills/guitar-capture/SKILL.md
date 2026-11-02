---
name: guitar-capture
description: "Record and prepare the owner's guitar parts (DI or mic), clean them, extract chords, tempo and MIDI, so they can drive production or AI generation. Use when he has a riff or a full guitar part."
---
# Guitar capture

status: draft

## Steps
1. Capture: DI through an audio interface at 48 kHz/24-bit (amp sim later) or a phone memo for ideas. Play to a click
   when the part will be produced.
2. Tempo and grid: beat-track the take (librosa beat and downbeat map).
3. Chords and notes: audio-to-MIDI (Spotify Basic Pitch, Apache-2.0) for a MIDI sketch; Claude reads it to write the
   chord chart in the song sheet.
4. Clean: noise reduction, edits on the grid, light compression. Keep the raw take untouched.
5. Tone: amp/cab sim (free: Neural Amp Modeler) to match the reference songs.
6. Export stems for `produce-arrange` or as the reference audio for vocal-route C.
