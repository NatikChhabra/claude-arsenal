---
name: retro
description: The post-upload retro and improvement loop - on day 1, 3 and 7 of every long video (and after the creator's review notes) pull the numbers, harvest his notes verbatim, compare with the last video, fix each problem at the root where every future video routes through, recalibrate the gates that disagreed with reality, log and tell him in bullets. Use for "retro", "what did we learn", "day 7", "improve the system", or on its own on those days.
---

# retro <ep> [--day 1|3|7]

status: beta

Each video better than the last, incremental, forever, by itself. Runs unasked on day 1, 3 and 7 (the release wrote the
dates into the hand-off) and after his review notes on any cut.

## Steps
0. **Self-updating, always:** any new preference, decision, plan or account change he gives is written to its file the
   moment he says it (the hand-off, the project rules, the style log, a skill). His words verbatim + time, then a clear
   rewrite. He never repeats himself; a thing he had to say twice becomes a check, a tool or a skill step that day.
1. **Numbers:** pull the day's stats (the project's analytics tool, else Studio + Instagram Insights by hand) into the
   metrics ledger: CTR, 0:30 retention, APV, average view duration, subs per 1k views, the target-country share, the
   Test & Compare winner, Shorts viewed-vs-swiped, Reels skip rate and sends. Compare against the bars (skill
   `growth-funnel` §1) and every earlier video. Read the retention export with skill `yt-retention`.
2. **Harvest:** every note he gave (review, upload day, after watching live) verbatim with its time, plus every problem
   we found. A rejection = the WRONG PLACE, not the thing: fix the placement or trigger; ban an element only when he
   says he dislikes it.
3. **Compare:** what beat the last video and what lost, each with its number. Where our blind scores disagreed with the
   real result, the gate was wrong: name it and recalibrate (skill final-review, references/scorecards.md §5: a gap
   > 1.0 adds a missing criterion).
4. **Root cause, not patch:** 1-3 changes, each where every future video routes through: a tool, a gate line, a skill
   step, the style log, a research note. A fix in one video's build script alone is not enough. Only proven wins (measured
   or his rating); remove rules that proved wrong. Each change ships with the number it should move and its check date.
5. **References:** fold in what the pros' editors do and any new reference (skill `reference-study`). Story beats
   funny: cut what the story doesn't need.
6. **Drift sweep:** if a rule file changed, check every other file that restates it still agrees (one pass, one helper).
7. **Log + tell him:** the video's retro file, one `## Day N` section per retro and the release's `## Post-mortem`. A
   day whose numbers can never be read: write `retro_waived: <why, date>`, never a blank. Test & Compare winner (too
   few impressions = `winner = inconclusive (<N> impressions, <date>)`) and the intro test's 0:30 cell. Commit + push if
   the project uses git. Him: 3-5 bullets, what worked, what changes next video.
