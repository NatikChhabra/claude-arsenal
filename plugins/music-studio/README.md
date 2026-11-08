# music-studio

Songs from an idea to a released music video, built for a guitarist who loves singing but can't sing: every step
offers a vocal route that keeps his melody and phrasing, in English, Hindi or Hinglish. Sourced research behind every
tool choice: research/03_vocal_tools.md, research/04_production_and_video.md.

Start with `song-from-idea`; it writes `songs/<slug>/SONG.md` (from `templates/SONG.md`), the one sheet every other
song skill reads and updates. `gear-pick` stands apart: buying an instrument or a playing setup.

| Skill | What it does |
|---|---|
| `song-from-idea` | Brief, inventory, form with first-chorus time, chords, hook first, lyrics gated by lyric_lint and a blind reader |
| `vocal-route` | Five routes picked by language, melody fidelity and release terms; one chorus proved with blind listeners first |
| `guitar-capture` | Record to a click, beat and bar map, chord chart, MIDI sketch, tone |
| `produce-arrange` | Energy map per section, arrangement in a DAW Claude drives through MCP (REAPER by default), clean stems |
| `mix-master` | Mix and master gated by measured loudness, true peak, the encode and the phone-speaker vocal check |
| `music-video` | Rights path first, treatment, shot list, beat-locked edit measured cut by cut, native 9:16, Canvas, QC |
| `music-review` | Gates plus scored rows with evidence, human blind listeners, fresh blind readers; ship at every row 8.5+ |
| `gear-pick` | One instrument or gear setup to buy: questions once, taste from his listening history, whole-setup budget, live prices, one pick |

Tools (`tools/`, each has `--selftest`):
- `lyric_lint.py <SONG.md> [--bpm N]`: dashes, the design plugin's banned words, AI-lyric cliches, syllable drift
  between matching lines, one-chorus songs, late first chorus. Stdlib.
- `loudness.py <file> [--target streaming|apple|club|ingame] [--vocal stem --inst stem]`: integrated LUFS, LRA, true
  peak, the loudest 3 s, and the phone-speaker vocal check. Needs ffmpeg.
- `beatmap.py map <audio>` / `beatmap.py cuts <map.json> <cuts>`: tempo, beats, downbeats, bars, sections, energy,
  a click track to listen-check, and the share of edit cuts on the grid. `uv run --with librosa --with soundfile`.
- `listening_taste.py <player-data-dir | file ...>`: the songs and artists he really plays, read from a desktop
  player's local cache (Feishin: play queue JSON and the Snappy + V8 query cache). Stdlib.

Claude cannot hear audio: anything audible is judged by people (the owner and blind listeners) and by the measurements
above, never by Claude's opinion. Picture, text and motion rules for videos and covers live in the `design` plugin.
Skills are `status: draft` until used on real work (`gear-pick` is `beta`).

## Install

```
/plugin install music-studio --marketplace NatikChhabra/claude-arsenal
```
