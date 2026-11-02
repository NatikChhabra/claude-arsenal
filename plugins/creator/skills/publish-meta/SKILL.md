---
name: publish-meta
description: Package a finished long video for upload - 10 title candidates on the channel template linted and ranked, 3 title + thumbnail PAIRS for Test & Compare, a short description in the creator's voice with his own line first, chapters on milestones titled with his words, tags, the audience-language signal (title suffix, language fields, caption track), the store link and credits, all into one upload sheet. Use for "title and description", "upload details", "packaging", "chapters", "metadata".
---

# publish-meta <ep>

status: beta

Inputs: the final cut's word-timed transcript, its edit list, the beat sheet, the chosen thumbnail words. Output: one
human-readable metadata note + the upload sheet the project's tools read (for example `upload.json`). Nothing is
uploaded here; that is skill `release`.

## Language and the audience signal
- Description text in the language that reaches the widest search audience for the niche (often lowercase English),
  except line 1, which carries the creator's own words in his language. The hook + search terms sit in the first ~150
  characters (what search and the collapsed description show).
- For a non-English audience (measured on 4,403 videos of small channels in one language niche):
  1. long titles (not Shorts) end with the language word as a suffix, for example `| <Game> Hindi` ("hindi" 1.44x);
  2. description line 1 = the topic + the language word + his own words;
  3. the caption track in the spoken language (romanised if that is how the audience reads) uploaded on every long;
  4. video language + audio language set to what is spoken.
  If the project has an uploader with gates, it should refuse a long without them.
- Write in the note the number this video should move + its check date.

## Title
- Write 10 candidates. Topic names exactly as people search them (never translated).
- Long titles ~55-70 chars (<= 50 chars 0.83x; over 70 fine, 1.25x); the funny or stakes part in the first 40 (what
  mobile shows). Specific beats hype: a true number (1.23x), the topic, a situation.
- **The template** lives in the channel's config (skill `yt-package`, `title.py` `CONFIG`), for example
  `<first-person premise, a number if true> | <Topic> <language>`. Measured: a first-person premise ("I Became / I Tried /
  I Spent / I Forced Myself to") +24% in one niche's 582 videos and 1.31x in the larger set; CAPS optional; "vs" +17%.
  No emoji, hashtags or episode numbers (measured negative); "!" only when real. Keep the whole topic name even past 60
  chars (100 max).
- Lint: `python ${CLAUDE_PLUGIN_ROOT}/skills/yt-package/title.py titles.txt`; show the top 3 with scores.
- The premise comes from his own words (his recap lines, his brags), translated into the template, never a line he
  didn't say.
- A Part 2 or a recurring frame gets its own premise ("I Became a ___"), never "<Topic> #N" or "Part 2" as the hook
  (premise frames beat numbered series). No off-format uploads on the main channel (Q&A, vlogs, channel updates ran
  0.02-0.25x their channels' median).
- **Hard blocks:** zero profanity or slurs in title, description, tags and thumbnail text (check every word, including
  the audience's own slang).
- **A/B = 3 title + thumbnail PAIRS on every long:** 3 drastically different titles, each with its own thumbnail;
  title and thumbnail text never repeat each other. Log the pairs and, after day 7, the winner.

## Description (the creator's voice: short, dry, no hype)
- Line 1: `<topic> <language word>: "<a line he says in this video>"` (quoted as the captions have it).
- Line 2: what happened, plain, with true numbers.
- Then the chapters (below). Then, each on its own line: the topic's store link in full (Steam first; another store
  when it isn't there), a content warning if the channel uses one (for example language and age), the business contact
  line, 2-3 hashtags. No link walls, no hype adjectives, no emoji bullets, no "in this video".
- The store link is required for a game (it supports the developer); a non-game video records why it has none.
- Every CC BY credit line verbatim at the end; any line the publisher's video policy requires (check the publisher's
  policy page before the first video on a game).
- Run the project's voice checker if it has one; otherwise read it aloud against the creator's real lines.

## Chapters
- Valid times first: `python ${CLAUDE_PLUGIN_ROOT}/skills/yt-chapters/chapters.py <transcript>`.
- Put each chapter on a MILESTONE (the acts) and title it with HIS line at that moment, lowercase, 2-6 words. Start at
  0:00, >= 3 chapters, each >= 10 s. Each title must be words he says within ~45 s of it, or a title he approved.

## Tags
10-15: topic name variants and spellings, "<topic> <language>", "<topic> funny", the niche + language, the channel name.
No unrelated trending tags.

## Also in the note
Category; language; made for kids: no; altered or synthetic content: only what is true (an animated mascot is not
synthetic realism; an AI likeness is); the caption file; the publish plan (private until the scheduled slot, set in
skill `release`; never a publish time on an API upload that would make it public by itself); the topic playlist (named
as people search it); the end screen target (a real video id) and cards.

## The upload sheet (one per long; one per Short and per Reel from skill `shorts`)
Fields a release needs: the master file he watched, the title + 2 test titles, the thumbnail + 2 test thumbnails (each
paired), the incentive sentence per thumbnail, the description, tags, category, languages, the caption file, the
playlist, the end screen (target id + Subscribe), cards, the planned public time, the Part 2 decision ("none: <why>" or
"planned: <when>"; a possible Part 2 keeps every raw), the self-score + the computed blind score, and `creator_ok`,
stamped only by skill `final-review` 5.
- **Launch kit** on his "upload": a community post in HIS words, a poll, a note to the developer. Nothing in it is
  posted or sent until he says yes to that exact item.
- **Day 7:** a long under the channel median gets repackaged (the Test & Compare winner, or a new pair with his OK for
  that exact text). Never delete or re-upload a video. The day 1/3/7 numbers go in the project's metrics ledger; the
  retro is skill `retro`.
