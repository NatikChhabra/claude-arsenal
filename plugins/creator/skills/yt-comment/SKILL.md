---
name: yt-comment
description: >-
  Draft replies to YouTube comments in the creator's voice, triaged by which
  ones are worth answering. Use for "reply to my comments", "handle the
  comment section", "someone asked X", or a pasted comment thread.
---

# yt-comment

status: beta

The comment section is a retention surface, not a chore. Replies in the first few hours are what
decide whether a thread becomes a conversation other people read.

## Before you write

1. Read the project's voice file (for example `voice.md`) if it has one, and run any public text through its
   voice checker if it has one. The project's own rules (its CLAUDE.md or equivalent) win over this generic skill, and
   nothing is posted or interacted with (comment, reply, heart, pin) without the creator's OK for that exact action.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## Triage first, always

Sort what the user pastes into four piles and say how many are in each before writing anything:

1. **Questions** - answer them. These are your next video's topics, so note the repeats.
2. **Corrections** - if they are right, say so plainly and thank them. Never argue a fact you
   cannot check.
3. **Praise** - reply to a few, briefly, with something specific from their comment. A wall of
   identical "thank you!" replies reads as automated because it is.
4. **Bait** - do not reply. Say so and move on. Never write a comeback, however deserved.

## Writing the reply

- Under 30 words. A long reply in a comment thread is a blog post nobody asked for.
- Answer the actual question in the first sentence.
- One question back, only when it is real.
- No emoji unless the user's own replies use them. Check their voice file.
- Never promise a video you have not agreed to make.

## The heart and the pin

Say which one comment to pin (if the channel pins at all; some creators prefer none) and which few to heart. Nothing is
hearted, pinned or replied to until the creator says yes to that exact action: draft, show, wait.

## The gate

The output goes into the video's package file (the upload sheet the project uses, or skill `publish-meta`); nothing is
published here. Posting or interacting needs the creator's OK for that exact action.

MIT licensed third-party skill, adapted; see `../../LICENSE-yt-skills-MIT.txt`.
