---
name: mix-master
description: Mix vocal and instrument stems and master the song to streaming loudness, with a reference-matched check. Use when stems are ready.
---
# Mix and master

status: draft

## Steps
1. Gain-stage stems; vocal chain: EQ, de-ess, compression, short reverb/delay sends.
2. Balance against 1-2 reference tracks at matched loudness.
3. Master: target about -14 LUFS integrated, true peak <= -1 dBTP for streaming; louder only for in-game or club use.
   Optional reference matching (Matchering, GPL-3.0) as a starting point, never the final word.
4. Measure with ffmpeg `loudnorm`/`ebur128` and write the numbers in `songs/<slug>/MIX.md`.
5. Listen on headphones, a phone speaker and in-game (NDRP radio/vehicle) if that is where it will play.
