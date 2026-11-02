---
name: topic-pick
description: Pitch the next video as 3-5 concept + format + topic ideas backed by data, unasked, with Claude's pick marked - candidates from store and trend lists, coverage gaps in the audience's language, small-creator outliers (channels under 50k, each video vs its own median), the demand slot, the creator's veto list and mission. Never a bare game or a plain playthrough. Use for "what should I play next", "next video", "pitch me videos", "concepts", "shortlist", or when the lineup has under 2 videos.
---

# topic-pick

status: beta

Claude picks from its own research; the creator chooses from a SHORTLIST and keeps the veto on every pick and on the
channel's direction. Every pitch = format + concept + situation + topic + data. Bring pitches before he asks (a creator's
complaint: "you did not give me this idea beforehand").

## 1. Candidates + data (if the project has a topic-prediction tool, run its steps; otherwise by hand)
1. **Candidates:** the store's new, top and upcoming lists for the audience's region (for games, Steam by country), trend
   lists, references he sent, his wishlist.
2. **Facts per candidate:** release date, review count and score, solo or co-op, genre, platform.
3. **Coverage gap:** videos on it in the audience's language vs globally (search both; "first in <language>" is a
   real edge).
4. **Lift:** do creators' videos on this topic beat their own normal? (each video's views / that channel's median).
5. **Small creators only:** channels under 50k subscribers, gameplay or topic videos (big channels' audiences watch
   anything, so their numbers say nothing about a small channel). Use skill `yt-viral` on public listings: >= 3x a
   channel's own median = an outlier.
6. **Search demand:** the platform's autocomplete for the topic + the audience's language word.
Rank to a 3-5 shortlist, each with its evidence line.

## 2. Filters (check the output, never from memory)
- The creator's veto list (a dropped topic stays dropped; skill `drop-topic` records it) and his hard nevers.
- His mission and format rules (for example solo only, no mobile games, no saturated games his audience already has).
- **Demand slot:** of every 2 long videos, >= 1 has live demand: out <= 14 days, or small-creator outliers >= 3x their
  median in the last 30 days. If the channel has a sub-pillar with proven pull (racing, a series), keep its rhythm (for
  example one in every 3-4).
- A FAST FOLLOW-UP from the weekly review (a long at >= 3x the median) beats everything: the next video stays on that
  topic or premise.

## 3. Concepts
For each topic: the format (from the channel's tested format set, for example "from zero to an empire", "the game's own question", "a launch-week film"), the premise as a long title on the channel template
(lint with skill `yt-package`), the situation that makes it funny or worth it for HIM (read his transcripts: how he
talks, what he enjoys), the thumbnail moment, and the data line (gap, lift, small-creator tier, demand).

## 4. Deliver
- Bullets, 3-5 pitches, Claude's pick marked with one line why. Say which format each is if the channel alternates.
- After he picks: the publisher's video policy for that topic (any required description line), the topic primer (HUD,
  mechanics, jargon), then skill `beatsheet`. On day 7 of each video log the outcome next to the prediction, so the
  ranking learns.
