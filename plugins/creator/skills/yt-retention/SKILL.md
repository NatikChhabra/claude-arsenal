---
name: yt-retention
description: >-
  Read a YouTube Studio audience-retention export and find where viewers
  actually leave, then say what to change. Use for "why do people stop
  watching", "my retention is bad", a pasted retention chart or CSV, or "fix
  my pacing".
---

# yt-retention

status: beta

The retention graph is the only honest feedback YouTube gives you. Almost nobody exports it.

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-retention/retention.py retention.csv --duration 600
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-retention/retention.py retention.csv --transcript transcript.srt
```

Getting the file: if the project has an analytics tool that writes `retention.csv`, run it.
By hand: Studio -> a video -> Analytics -> Engagement -> the audience-retention chart -> the download icon ->
"Audience retention".

## Three different problems

- **HOOK LEAK** - what is lost in the first 30 seconds. Under 25% is healthy. This is always the
  first thing to fix. For an unscripted creator the levers are the EDIT (the cold open, what the intro cuts to), the
  promise line (live or a voice-over), and the audience signal (wrong-language viewers leave at the first spoken word:
  fix the packaging that sent them).
- **CLIFFS** - single steep drops. A cliff is a moment: a topic change with no signposting, a
  sponsor read, a long setup. With `--transcript` the tool prints what was being said there, which
  is what makes the report actionable instead of interesting.
- **SLIDE** - the steady bleed across the middle. A flat slide is pacing. The fix is cutting, not
  rewriting.

## What to hand back

Name the single biggest leak and one change for it. Not a list of five. Then, only if asked, the
rest. And if the hook leak is healthy and the slide is flat, say the video is fine and the problem
is packaging - send them to `/yt-package`.

## The gate

The output goes into the video's package file (the upload sheet the project uses, or skill `publish-meta`); nothing is
published here. Posting or interacting needs the creator's OK for that exact action.

MIT licensed third-party skill, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
