---
name: growth-gate
description: Score a finished video package (the long, every Short, every Reel and their links) against the growth funnel before the creator's review message and again before release - one row per lever, 0-10 with one line of evidence, ship at 8.5+, blind rows from a fresh reviewer. Use for the package score in final-review and release, "score the package", "growth check", "will this blow up".
---

# growth-gate (the funnel's score sheet; the why is skill `growth-funnel`)

status: beta

Run it on the exact files and the upload sheet, after QC passes and before the review message (skill `final-review`);
run sections C-D again in skill `release`. Score every row 0-10 with one line of evidence (a timestamp, a frame, a
number). **Every row >= 8.5**, else fix and re-score. Rows marked **(blind)** come from the FRESH blind reviewer, who
sees only that one file. Write the table into the video's brief under `## Growth gate`, first line `file: <hash or
size + mtime of the final long>` so a re-render shows the table is stale.

## A. Each YouTube Short
| Row | 10 = |
|---|---|
| stop | frame one shows the premise (the subject + the on-screen text), the creator's line + caption by 0.5 s; a claim -> test (H2) opener if it is the first Short out |
| standalone (blind) | the reviewer says what happened and why it works, with no topic or channel knowledge |
| finish (blind) | the reviewer wanted to see the end and says why; something new every <= 6 s; payoff at ~55-80% |
| want-the-long (blind) | the reviewer names the bigger question the long answers, from the creator's words or the picture, not our text |
| loop | the last beat runs back into frame one, or ends <= 1.5 s after the payoff |
| title | <= 40 chars, first person, carries the situation the picture can't, never explains the joke |
| language | the voice from 0.0 s, captions in the audience's script in frame one |
| link | related video = its long (set once the long is public), `full video: <link>` as description line 1 |

## B. Each Instagram Reel (its own file and edit list when a lever differs)
| Row | 10 = |
|---|---|
| hold-3s | voice from 0.0 s, motion in frame one, premise readable before 3 s |
| standalone (blind) | as A, judged on the Reel cut |
| send (blind) | the reviewer names who they'd send it to and the line that makes them send it |
| end | ends hard on the most quotable line |
| profile | cover inside the centre 3:4, the same mascot corner as the grid, part of a run of Reels on one topic |
| caption | the channel's caption rule (for example a store link + 5 tags, Instagram's cap), Meta AI translation off, posted at the audience's evening slot on a day without a Short (the first one on the long's day) |

## C. The long video
| Row | 10 = |
|---|---|
| click | 3 title + thumbnail pairs that pass skills `yt-package` and `thumbnail`, on the channel template |
| first-30 | cold open ends by 0:15, promise by 0:30, topic named by 0:30, the core loop shown in minute one |
| short-payoff | a viewer arriving from the first Short sees that Short's world within the first 10 s |
| re-hook | a fresh beat near 3:00 and 6:00; the payoff in the last quarter |
| next | end screen (last 20 s): the next video on that topic/premise, else the best performer by APV, + Subscribe; a card where the creator names an earlier video |
| chain | the next planned long continues this topic/premise when this one beat 3x the channel median, or the plan says why not |

## D. The links (release day)
| Row | 10 = |
|---|---|
| order | the strongest standalone claim -> test Short goes ~30 min after the long is public, its Reel that evening; the rest inside 7 days |
| playlists | the long is in its topic playlist (named as people search it), read back after a reload |
| related | every Short's related video set, read back after a reload |
| audit | skill `growth-funnel` §7 audit run on the whole channel; nothing points at a deleted video or playlist |

## After 7 days
Fill skill `growth-funnel` §6 for each piece. A row that scored >= 8.5 while its live metric missed the bar = the score
was wrong: write the lesson into this table (what 10 really looks like), so the gate gets stricter with every video.
