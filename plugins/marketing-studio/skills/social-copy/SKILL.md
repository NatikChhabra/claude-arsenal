---
name: social-copy
description: >-
  Write captions, posts, Spotify pitches, YouTube titles and descriptions, Discord announcements and in-game adverts in
  the brand's or character's own voice, one version per platform, every piece carrying a concrete fact, linted by
  copy_lint and read by a fresh blind reader. Use for any words that promote a song, a character, a business or an
  event, for "write a caption", "post for this", "pitch text", or copy that sounds like AI.
---

# social-copy

status: draft (full workflow; copy linter tested; promote to beta after the first real campaign)

Platform rules: [../release-rollout/references/platforms.md](../release-rollout/references/platforms.md). Interface
words (buttons, errors) are the design skill's references/copy.md; this skill is promotional copy only. The banned
word list is the design skill's one list (references/tells.md): copy_lint reads it from there.

## 0. Voice first
Read the brand kit (`brands/<name>/BRAND.md`, design skill references/systems.md): three personality words, five lines
it would say, five it would never say. No kit for this character or business = make the small version first (those
three parts) with the owner, then write.

## 1. One fact per piece
Each piece carries at least one concrete, checkable thing only this release has: the character, the in-city event,
where it was recorded, who played the guitar, the date, a number that is true. A sentence that fits any song is cut.

## 2. Write per platform (never one caption pasted everywhere)
| Platform | What carries it |
|---|---|
| Instagram | the first line (it is all that shows); the rest can tell the story; no watermark from another app |
| TikTok / Shorts | the hook is in the picture and on-screen words in the first second; the caption is short |
| YouTube title | matches the video; song and artist first; caps and emoji rare; 100 characters max |
| YouTube description | first two lines: what it is, the story in one line; then credits, lyrics, links, AI disclosure where needed |
| Spotify pitch | who, what, why, when, where, how; the RP story; the marketing plan; mood and genre; no follower counts |
| LinkedIn | the first two lines (all that shows before "see more") state the result with a number; then short paragraphs, not emoji bullets or "What I learned:" headers; zero emoji; links on their own lines; 3 hashtags at most; limits stated plainly at the end |
| Discord | what, when, where, one link; a ping only when the owner says so |
| In-game advert | the server's ad format and rules; in character; never names other servers or real brands |

## 3. Three options, a pick
Write 3 versions per piece on different angles (the story beat, the guitar, the character's line). Say which one you'd
post and why in one line.

## 4. Gate
1. `python ${CLAUDE_SKILL_DIR}/../../tools/copy_lint.py <file> --platform <platform>`: 0 FAIL; each WARN fixed or
   defended in one sentence.
2. Fresh blind reader: give a fresh agent ONLY the copy (no brief) and ask: what is being promoted, would you click or
   listen, which phrase sounds machine-written or like any other post. A named machine phrase = rewrite it and use a
   new reader.

## 5. Hand over, never post
Deliver the pick plus the two alternates with the lint result. **Nothing is posted, scheduled, replied or sent without
the owner's explicit OK for that specific piece.**
