---
name: shorts
description: Cut 2-3 vertical 9:16 YouTube Shorts AND separately packaged Instagram Reels from a finished long video - each a standalone zero-context mini-story (hook, turn, payoff) that also leaves one bigger question only the long answers, cut for its own app's levers, with a designed cover, the long's whole quality bar and a fresh blind review, delivered WITH the long. Use for "make shorts", "clip this", "reels", "vertical cut", or when a long's cut is final.
---

# shorts <ep>

status: beta

## The rule (it beats every older habit)
Every Short and Reel is a standalone hit that sells the long. Understandable is not enough: a stranger must stop,
watch to the end, feel paid off, AND want the long. Evidence: a context-free trailer Short got 13 views and 0% from the
Shorts feed while the claim -> test Shorts topped every list.
1. **Zero-context story:** hook (premise readable in frame one, the creator's line by 0.5 s) -> turn -> payoff that
   closes it. A moment that needs the long's context is not a Short. No mood montage, no trailer, no "watch the full
   video" ending.
2. **A reason to watch the long, inside the Short:** it closes ITS loop and opens a bigger one only the long answers
   (the bigger stakes: the debt, the day count, the plan about to fail), in the creator's words or the picture, never
   our added text. YouTube carries the click (related video = the long); Instagram carries the follow. Name it per cut:
   the words + their source time, or what the picture shows; a standalone Short says why it has no long.
3. **Two products, cut separately:** the same moment, its own edit list + render whenever a lever differs (length,
   opening line, end tail, cover). Never the payoff: a Reel that lost its Short's payoff lost its point.
4. **Gate before render:** each candidate gets one line "the standalone story" + one line "why watch the long". Then the
   fresh blind review (skill final-review, references/blind-rubric.md "Short / Reel review": the AI-feel audit and 4
   questions What happened / Why is it funny / Want to finish it / Watch the full video; a blank, "not sure" or "no" =
   RE-CUT) and `ship_score.py --short` per cut.
5. **The first Short after the long** = the strongest standalone claim -> test Short, ~30 min after the long is public,
   related video = the long; its Reel that evening.

**Same bar as the long, delivered with it.** Each Short gets the long's whole bar: every scorecard row >= 8.5, a fresh
blind review, QC pass (loudness, clicks, the phone-voice band, the creator's identity unreadable), the sound placement
and truth rules, both apps checked, a designed cover. Run this skill the moment the long's cut is final, in that
session, unasked; the review message carries the long + its Shorts with scores side by side. A creator override on a
Short's sheet waives its score rows only, never the cover/click tests, safe zone, QC or privacy.

## Hooks (frame one is the thumbnail on both apps)
The first second hooks with the PICTURE + the creator's own voice (his line by 0.5 s, the subject in frame). No added
hook-text bar (a coloured bar of our words "feels AI", and third-person editor lines break the on-screen-words rule).
The 5 patterns:
| | Hook | Turn | Payoff |
|---|---|---|---|
| H1 | the game's or world's own order (a speech bubble, a task card) over its target, his reaction from 0.0 s | what he does about it | goal + obstacle |
| H2 | **claim -> test:** his plan or brag from 0.0 s over the thing it's about | the answer: it works hilariously, or he dies | the strongest (3 of 5 broke out vs 0 of 5) |
| H3 | the absurd mechanic, mid-action in frame one | his reaction + a bigger second use | |
| H4 | status flip: on top (a win, a record) | knocked to the bottom | loops to frame one |
| H5 | the big win, then the floor | loses to something trivial | end on his line |
Every video gets at least one H2 and an H2 posts first on both apps (Instagram: 3 of 5 H2 Reels left the first test
pool, 0 of 5 others; the skip rate decided it every time). Vary patterns across Shorts (a templated look is an
"inauthentic content" risk).

## Pick 2-3 moments
- Start from a scored list: if the project has a moment scorer, use its top windows; otherwise list 15-35 s windows
  from the transcript and score each /100 on hook, emotion, payoff, density, coherence (a term only the long explains
  costs coherence). Check each window's picture: dark scenes, menus and HUD walls fail at phone size.
- Then the retention export's rewatch spikes, and the creator's own markers ("clip that"): the moments he'd send a
  friend go first as Reels.
- **His voice carries the joke.** A joke that lives in small on-screen text, a chat bubble or an NPC voice does not
  survive at phone size, however it is cropped (3 pairs x 4 blind rounds, best 7.2, all dropped). Pick moments where his
  spoken line is the joke and the picture shows the stakes in frame one.
- **Stop rule:** a moment with 2 fresh blind rounds under 7.5 is DROPPED for the next candidate; no third polish round.
- Prefer moments that already had stings or cards in the long edit: proven beats. Trim dead air inside the moment.
- 2-3 Shorts per long; never more to chase views. Judge them on engaged views + viewed vs swiped, not raw views.

## Structure (mark each piece's beat in the edit list)
1. **hook = piece 0:** his strongest line + the picture that IS the premise, PULLED TO THE FRONT (never the moment's
   first second, never "so basically"). Words on screen and his voice in the first 0.5 s (motion and the mascot don't
   count). Goal + obstacle in the first sentence.
2. **turn, mid-way (25-75%):** the BUT / SO that changes the situation and re-hooks. Without one it's a clip.
3. **payoff:** the one moment, then END within 1.5 s. A last line that loops into frame one is a bonus.
15-35 s, aim 20-30 (7,444 Shorts within channel: > 45 s loses); NEVER over 60 s (any Content ID claim blocks a longer
Short worldwide). One moment, never a compilation, never the long's own order straight through.

## Framing and cover (rules + numbers: skill design, references/video.md §3.2-3.5)
- Default full height (the 0.316 crop, a saliency camera per piece); wide only when the joke needs width, bars that do
  a job, never empty blur on a Reel. Watch every auto pan; one mid-frame grab per Short to confirm the crop.
- Source = the highest-resolution raw, not a 1080p export (soft at full-height crop).
- The mascot in a TOP corner, moved when it covers the subject; everything clear of each app's UI bands (§3.2).
- Captions: the long's captions and bleeps carried over, bleeps per the channel's swearing policy (the source channel
  bleeped every strong swear on Shorts). Sounds only where earned, on a cue (default max(2, 6 a minute)); one big text
  slam on the payoff at most.
- Every render: if the project has a vertical checker, run it for both apps; otherwise check by hand: 1080x1920, fps,
  length, -14 LUFS, frame-one words + voice, bands, no dark frame one, no > 3.5 s stretch with no cut and no caption,
  no trailing tail, the last word not clipped. FAIL = fix; every WARN answered before the blind review.
- Cover, every Short + Reel: a designed 1080x1920 cover built like a long thumbnail (skill `thumbnail`, video.md §3.5),
  the same file serving the Reel; plus a `cover_at` second (the best real frame IN the Short) where a custom Short
  thumbnail is not available (partner-gated, desktop only in 2026). Tests: the T1 + T4 read at 202 px, a 9:16 feed mock
  with 3 readers; score it as a "cover" row; under 8.5 = redo.

## Packaging per app
- **YouTube Short:** title = his hook moment, English (or the audience's language), first person, <= 40 chars visible,
  no hashtag stack, no `#shorts` (Shorts are classified by shape + length; title features measured 0.94-1.15x).
  Description line 1 `full video: <long link>`, then the channel's standing lines (store link, credits, business line),
  2-3 tags. Language fields set like the long's. A release day inside the long's first 7 days, never before the long is
  public.
- **Instagram Reel:** caption per the channel's rule (short; for example the store link + exactly 5 tags, Instagram's cap
  since Dec 2025). Rules: I1 order Reels by SENDABILITY (the moment someone would DM goes first), not by the Shorts
  order · I2 a fixed tag set per topic · I3 the first Reel the evening of the long's day, the rest at the evening peak
  on days without a Short · I4 two hook cuts of one moment = a Trial Reel (non-followers first; keep the winner after
  24-72 h) · I6 Meta AI translation/dubbing OFF, checked in the app and logged (never an AI voice on the creator) · I7
  within 48 h log each Reel's skip rate, avg watch, sends and non-follower % with the number the next change should move.
- Neither render carries the other app's watermark. Every CC BY credit line goes into the description and the caption.
- Scheduling and posting: skill `release` (LONG FIRST).

## Report
Table: short, source range, duration, hook pattern, why it stands alone, why watch the long, cover, scores (self,
blind), suggested day. After release, log each Short's viewed-vs-swiped and each Reel's 3-s skip next to its hook
pattern and framing (alternate full and square across the next 8-10 to decide on the trend).
