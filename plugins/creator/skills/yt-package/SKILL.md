---
name: yt-package
description: >-
  Write and lint the title and thumbnail for a YouTube video as one pairing,
  checking truncation, duplication and vagueness before publish. Use for
  "title ideas", "what should I call this", "thumbnail text", "my CTR is
  bad", packaging, or any request to rename or repackage an existing video.
---

# yt-package

status: beta

The title and the thumbnail are ONE unit. Writing them separately is why most packaging fails: the
thumbnail repeats the title, and half the click surface says the same thing twice.

```bash
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-package/title.py --title "..." --thumb "AI RAN IT"
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-package/title.py titles.txt            # one per line, ranked
python ${CLAUDE_PLUGIN_ROOT}/skills/yt-package/title.py --short titles.txt    # a Short's titles
```

## Before you write

1. Read the project's voice file (for example `voice.md`) if it has one, and run any public text through its
   voice checker if it has one. The project's own rules (its CLAUDE.md or equivalent) win over this generic skill, and
   nothing is posted or interacted with (comment, reply, heart, pin) without the creator's OK for that exact action.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## Rules the tool enforces, and why

- **Long video (default):** the channel's title template lives in the `CONFIG` dict at the top of `title.py` (a
  suffix such as `| {topic} Hindi`, the first-person rule, the length band). Set it once per channel. The tool flags a
  missing suffix, <= 50 chars (0.83x on 4,403 small-channel videos) and no first-person premise (1.31x).
- **The premise** (the part before the suffix) should fit the ~40 chars a mobile feed shows.
- **Short (`--short`):** 60 chars desktop / 40 mobile, no suffix, no `#shorts` or hashtag stack, two all-caps words is
  the ceiling.
- **The thumbnail must not repeat the title** (the premise; the game name may sit on both). Different words, same promise.
- **Three words maximum on the thumbnail.** At feed size a fourth word is a grey smear.
- **Specific beats vague:** the game, a true number, a situation beat every adjective available to you.

## Write ten, keep two

Generate ten titles, rank them all with `title.py` yourself and keep the best; the final 3 title + thumbnail pairs follow
skill `publish-meta`. A thumbnail brief starts from the click incentive named from the creator's own lines (skill
`thumbnail` 0b), never from a reaction face. The thumbnails themselves are skill `thumbnail`.

## The gate

The output goes into the video's package file (the upload sheet the project uses, or skill `publish-meta`); nothing is
published here. Posting or interacting needs the creator's OK for that exact action.

MIT licensed third-party skill, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
