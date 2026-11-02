---
name: yt-script
description: >-
  Score a video's opening line (the first 15 seconds) on five properties and
  match it against 21 hook formulas with worked examples and failure modes.
  Use for "is my hook good", "score this intro", "why do people leave at
  0:08", "hook ideas", or to rank real openings pulled from a transcript.
---

# yt-script

status: beta

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-script/hookscore.py hooks.txt           # one hook per line, ranked
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-script/hookscore.py --hook "one line"   # a single hook
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-script/hookscore.py --json hooks.txt
```

Five properties, 0-100 each; the verdict is 60% the mean and 40% the weakest one (a hook leaks at its dead property,
and an average hides that). `hooks.json` holds the 21 formulas: the shape, a worked example, when it fails, and the
patterns the scorer classifies speech against, plus five rules (confirm the title in the first sentence; one idea;
specific beats big; show the artifact inside 20 s; never open with who you are).

## How to use it honestly
- Measured on 74 real short-form hooks (top 8 and bottom 8 by views across five channels): it separates deliberately
  bad hooks from real ones well, and a creator's own hits from their own misses barely at all. A low score is a reason
  to look again; a high score is never a promise.
- An unscripted creator: score REAL openings pulled from their transcripts and pick the strongest to open the cut.
  Never write a hook for them to read.
- A scripted creator: write 5 openings, score them, keep the best 2, then read them aloud in the creator's voice.

MIT licensed third-party tool, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
