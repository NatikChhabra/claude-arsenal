---
name: thumbnail
description: Make 3 drastically different high-CTR 1280x720 thumbnails for a long video (one Test & Compare pair each) - the click incentive named from the creator's own lines first, one audience per card, the stranger test, one felt focal point at phone size, a staged real frame, 0-3 words - then measured feed-size gates, fresh blind readers, a click floor and a harsh-scroller critique before his pick. Use for "thumbnail ideas", "make thumbnails", "my CTR is bad", or a Short/Reel cover.
---

# thumbnail <ep>

status: beta

This skill is the CLICK method: the order of work, what to decide, which gate runs when, what gets logged. Every visual
rule and number (incentive table, hook lifts per audience, stranger test, focal point, words, measured floors, build
tiers, the lit cut-out recipe, brand mascot rules, never-on-a-card list, file spec, U1-U12, reader prompts) lives in
skill design, `references/video.md` §1, §5 and §6. Read the sections each step names. The gate run order and the
prompts not in video.md: `references/gates.md`.

## 0. Context first
Read the whole transcript (or the final caption file) and the video's concept note (premise, facts, beats). Research the
live context (collabs, news, trends around the topic and any creator the video references). Never ask the creator what
the recording already answers.

## 0b. The click incentive, before any frame (video.md §1.1-1.7)
A card set that was one template (a big moment + the mascot reacting + a caption you only get after watching) was
skipped by the creator 9 times in a row: no reason to click. Before any pixel, for each of the 3 pairs:
1. Read the cut's captions start to end; list the creator's lines that carry a number, a confession, a rule or an
   absurd act. The incentive comes from his words; the monster or the scene is only the stage.
2. Pick ONE incentive per pair (§1.1), a different one each, and write the stranger's sentence: a verb, an open
   outcome, TRUE in the cut (the line + its time). Store it with the pair (for example
   `"incentives": {"<thumb>": "<sentence>"}` in the upload sheet).
3. List every card the creator rejected for this video: a new pair differs in the INCENTIVE, not only the frame or
   the caption.
4. Name the video's 3 audiences by WHY they'd watch and give each card one (§1.2, hooks per audience §1.3). Never three
   cards for one audience.
5. Run the stranger test on the picture alone (§1.4) and the focal-point check (§1.6, faces §1.7) on each idea.
6. Sketch the 3 ideas in words FIRST (subject, the question it leaves open, backdrop colour + why, words) and run the
   T1 blind read (gates.md) on the sketch before composing.

## 0c. The best-rated recipe: check every card (video.md §1.16)
One line per rule per card; a "no" = rebuild: one face, one emotion a stranger names in one word, >= 60% of the height,
the sharpest thing on the card · that face does something TO the other subject (the creator's avatar is the loser;
beside is not a relation) · the stake in the topic's own look · <= 4 words from the cut's captions that can't be
misread · one backdrop colour, 3 elements, native-res crisp.

## 1. Frames
- First the frames shot on purpose at record time (tier 1, video.md §1.10), then the episode's biggest moments (the
  edit's stings, loud spikes, the hook, any marker the creator said aloud). Grab ~8 candidates from the text-free
  version of the cut: never a frame inside a motion graphic, meme or card span. The frame just BEFORE the sting is
  usually the funny one; the picture leaves the question open (§1.5).
- Look at them; keep the 3 most readable at small size.

## 2. The mascot (if the channel has one)
Decide the pose yourself; never ask. Size, contact and the never-deform rules: video.md §1.12. Only the channel's own
approved mascot files. A missing emotion = a new pose made the channel's way, with the creator's approval.

## 3. Compose 3 cards
- 3 DRASTICALLY different ideas: a different hook mechanism, composition and palette each (§1.14). Layout free per
  video; the channel's fixed identity (its text style, its mascot) stays.
- Lint each title + words pair: skill `yt-package`, `title.py --title "<t>" --thumb "<words>"`. Each thumbnail is built
  for its own title (3 PAIRS per long, skill `publish-meta`).
- Finish and file: video.md §1.11, §1.13, §1.15 (a cut-out upscaled > 1.15x never ships; PNG over 2 MB = upload the
  JPG twin).
- **Approved = frozen:** copy the approved cards to a `final/` folder and never re-render them through changed shared
  code (an edge tweak re-rendered the creator's favourite and it came out worse). A tool change = render to a new name
  and compare side by side.

## 4. Check (`references/gates.md`)
4a the measured floors first; 4b fresh readers: U1-U12, T1 + T4, T3, T5, T10 (a log), T12 click floor (>= 2 of 3) with
its incentive sentence, T11; then the harsh-scroller critique per card. Every reader is a FRESH agent given ONLY the
image, never the title (except T12 and the critique), the video or our reasoning.

## 5. Deliver
Show all three with the gate results (T1 sentence, T12 clicks, the critique lines) + one line each; his pick ships. Log
the pairs and, after day 7, the Test & Compare winner (watch-time share) with each variant's reader ranks: readers that
predict 3 winners in a row may become a gate.

## Covers for Shorts and Reels
The same method at 1080x1920; the bands, sizes and shelf rules: video.md §3.5. Its own T1 read at 202 px and a 9:16
feed mock with 3 readers; under 8.5 = redo. Details: skill `shorts`.
