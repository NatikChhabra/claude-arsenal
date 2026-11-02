---
name: yt-seo
description: >-
  Write the description, tags and search-facing text for a YouTube video,
  aimed at the query a real person types. Use for "write my description",
  "tags", "SEO", "help this video get found", "nobody is finding this".
---

# yt-seo

status: beta

Search is a smaller lever than packaging and a bigger one than people think for evergreen videos.
For a video aimed at the subscriber feed, say so and spend the effort on `/yt-package` instead.

## Before you write

1. Read the project's voice file (for example `voice.md`) if it has one, and run any public text through its
   voice checker if it has one. The project's own rules (its CLAUDE.md or equivalent) win over this generic skill, and
   nothing is posted or interacted with (comment, reply, heart, pin) without the creator's OK for that exact action.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## The description

- **The first two lines are the only ones anyone reads.** They show above "...more" and they are
  the search snippet. Say what the video gives them, in the words they would have typed.
- Then the link or the resource, if there is one, so it is above the fold.
- Then chapters (`/yt-chapters` writes them).
- Then stop: the rest is the game's store link, credits and the business line (`/publish-meta`); voice.py keeps it short.

## Tags, honestly

Tags are a weak signal and YouTube has said so. Use them for disambiguation - spellings, the tool
names, the abbreviations people actually type - and stop. Fifteen is plenty. A wall of tags is not
a strategy and stuffing unrelated ones is against the terms.

## The query test

Before handing anything over, write the three search queries this video should win, and check the
title and first two description lines contain the words in those queries. If they do not, the
problem is the title, not the description.

## The gate

The output goes into the video's package file (the upload sheet the project uses, or skill `publish-meta`); nothing is
published here. Posting or interacting needs the creator's OK for that exact action.

MIT licensed third-party skill, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
