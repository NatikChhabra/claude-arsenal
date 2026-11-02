---
name: campaign-plan
description: >-
  Plan a campaign for a bigger launch (a debut, an EP, a character's arc across several songs, an RP business opening or
  a server event): a goal in numbers, the audiences by why they'd care, one message and three angles to test, channels
  in and out of the server, a dated calendar, measures and the decision each read-out triggers. Use when something
  needs promoting beyond one release, for "marketing plan", "how do I grow this", or "promote my character/business".
---

# campaign-plan

status: draft (full workflow; promote to beta after the first real campaign)

One song's release is skill release-rollout; this skill is the plan around it. Platform facts and RP rules:
[../release-rollout/references/platforms.md](../release-rollout/references/platforms.md).

## Output: `marketing/<slug>/PLAN.md`

1. **Goal in numbers with a date**, and the baseline today (his current listeners, followers, views; or the business's
   current customers in RP). A goal without a baseline is a wish.
2. **Audiences by why they'd care** (2-3): people in the server who know the character; RP viewers outside it who
   follow the story; music listeners who never heard of the server. Each gets its own hook; never one message for all.
3. **One message** (a sentence the owner would say) and **three angles to test** (the story beat, the guitar, the
   character's line), each tied to one audience.
4. **Channels** per audience: in-city (events, in-game radio, adverts within the server's rules and the Cfx.re
   licence), Discord, YouTube (video + Shorts weekly), Instagram (Reels, Trial Reels), TikTok (the official sound),
   Spotify (pitch per release). Zero paid promotion until the owner sets a budget; Marquee/Showcase aren't available
   to India-based teams anyway.
5. **Calendar**: each release in the campaign gets its own `rollout.py` calendar; the plan lists them with the gaps
   between (a release lifts catalogue streams 15-20%, and ~75% of first-year streams come after day 28: space releases
   so each gets its 28 days).
6. **Measures and decisions**: per read-out (day 7, 28 of each release) the number to read, the bar, and what changes
   if it misses (the angle, the hook cut, the posting rhythm). Compare with his own previous numbers.
7. **Risks**: rights (the video path, the vocal route's licences, AI disclosures), server rules, the AI Persona badge.

## Check before showing
- Every angle carries a fact only this character or release has (social-copy §1).
- Every channel line names who does it, when, and the rule that allows it.
- The plan fits his real capacity (posts per week he will actually make); a plan he can't keep is cut down, not
  padded.
- Run copy_lint on the message and angles.

## Review
At each release's day-28 read-out, update PLAN.md: what worked (with the number), what is dropped, the next test.
