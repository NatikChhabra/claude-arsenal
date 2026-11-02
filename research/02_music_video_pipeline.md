# Music video pipeline for GTA RP footage (outline, 2 Nov 2026)

To be filled when music-video work starts. Known building blocks:
- Beat map (beats, bars, phrases, drops) so cuts land on the music: sirf-timepass `tools/beats.py` method.
- Kinetic lyric layer rendered in headless Chromium (deterministic frame = f(song time)): sirf-timepass research/83.
- In-game capture: Rockstar Editor / server-allowed cinematic tools; check NDRP rules on filming in RP spaces.
- Native 9:16 re-layout rather than crop; photosensitivity cap (<= 3 flashes/s).
Open questions: which editor he wants (Premiere, Resolve, CapCut, or a scripted ffmpeg pipeline), what NDRP allows.
