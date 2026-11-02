---
name: yt-edit
description: >-
  Find dead air, filler-only lines and restarted sentences in a timestamped
  transcript and print them as an edit decision list with the runtime saved.
  Use for "cut the dead air", "tighten this", "remove the ums", "random
  pauses", or before a rough cut of a talking or commentary recording.
---

# yt-edit

status: beta

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-edit/deadair.py transcript.srt            # or .vtt, or whisper .json
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-edit/deadair.py transcript.srt --floor 0.35 --json
```

It finds three things and prints the cuts newest problem first:
- **DEAD:** gaps between spoken cues longer than the floor (default 0.45 s).
- **FILLER:** cues that are only filler ("um", "so yeah", "basically").
- **REPEAT:** a sentence restarted (the second take of the same opening).

It never touches media. It prints an EDL, the total it would remove and the runtime you would land on; apply it in
the project's editor or render tool.

## Reading it
- A gap is dead only when nothing happens on screen either. A long silence over a payoff, a reveal or the game's own
  sound is a beat, not dead air: watch the span before cutting it.
- For a gameplay or commentary edit, more than 1 voiceless stretch over 5 s per 3 minutes reads as "random pauses" to
  viewers; aim under that.
- Keep the better take of a REPEAT, usually the second.

MIT licensed third-party tool, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
