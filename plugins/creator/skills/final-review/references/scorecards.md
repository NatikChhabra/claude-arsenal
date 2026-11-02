# Scorecards: the external bar

Why: home-made /10 self-ratings drift high (every row 8.5-9.0 while the real numbers said CTR 2% and 27% at 0:30). Every
score here is anchored to a published standard or a real number. The creator's taste is a separate layer that can only
BLOCK, never raise a score. G = gate (pass/fail), S = scored, O = outcome (after release).

## 1. How a score is made (4 layers, in this order)
- **L1 Gates, pass/fail on external specs.** Any fail = not shippable. Use the project's QC tools when it has them (an
  edit-list checker, a render QC oracle, a caption proofer, a swear scanner, an uploader dry run); otherwise measure by
  hand with ffmpeg (`ebur128` for loudness and true peak, `blackdetect`, `freezedetect`, `silencedetect`). Paste the
  verdict lines into the score row.
- **L2 Measured score, 0-10 from numbers only.** 10 = beats the pro spec with margin, **8.5 = meets the spec**, 7 =
  within one tolerance step, <= 5 = fails it. Example bands: loudness |I+14| <= 0.5 -> 10, <= 1 -> 8.5, <= 2 -> 7, else 4.
  Caption reading speed p95 <= 17 cps -> 10, <= 22 -> 8.5, <= 25 -> 7, else 4 (Shorts: 2-word chunks timed to audible
  words are scored on flip rate instead, every chunk up >= 0.4 s).
- **L3 House style, the creator's taste as pass/fail lists** (the project's style file: no machine-made look, the
  brand mascot's rules, the voice, swearing policy). Never raises a score; any fail blocks.
- **L4 Outcome, after release, overrides L2 for calibration.** A gap > 1.0 between L2 and L4 adds a missing criterion
  the same day (section 5).
Judgement rows (story, emotion, jokes) use Walter Murch's Rule of Six weights (emotion 51, story 23, rhythm 10,
eye-trace 7, 2D/3D 9), are labelled "judgement", and can't be self-scored above 8 without an outcome number.

## 2. Ship rule
All L1 gates pass + every L2 row >= 8.5 + every L3 list passes + the blind Ship score >= 8.5 (skill final-review) + the
creator's OK on the exact file. Our self-score may sit at most 0.5 over the blind score. A low blind score is fixed,
never argued.

The thresholds below point at the one home of each rule (skill design, `references/edit.md` and `references/video.md`);
this file keeps only the scoring structure: which row is a gate (G), a scored row (S) or an outcome (O).

## 3.1 Long edit
| | Criterion | Threshold |
|---|---|---|
| G | Black, frozen picture; flashes | skill design, references/edit.md §7 (QC table) + §2.8 |
| G | Edit list sanity | zero errors; every warning read and answered |
| G | First 30 s + format | skill design, references/edit.md §1.5 [YouTube Help 9314415] |
| G | Ending | skill design, references/edit.md §1.5 (no recap montage) |
| S | Rhythm | skill design, references/edit.md §1.3 (cadence + attention gates) |
| S | Readable density | skill design, references/edit.md §1.2 (readable chaos) |
| S | Device placement | skill design, references/edit.md §1.2 + §8.3; AI-feel P = 0 (judged, never counted) |
| G | Motion | skill design, references/edit.md §2.1-2.7 |
| S | Pacing vs reference | cuts/min, median shot, added sounds/min vs the project's role-model edit; caps are ceilings, never targets |
| O | Intro | >= 50% still watching at 0:30 = above typical [YouTube Help 12942217]; < 35% fails |
| O | APV, 10-20 min gaming | 35-45% strong, 37% mean [Retention Rabbit 2025, n > 10k] |

## 3.2 Sound
| | Criterion | Threshold |
|---|---|---|
| G | Loudness, true peak, A/V sync, clicks and holes at cuts, phone-speaker voice, never silence | skill design, references/edit.md §7 (QC table) |
| G | Music bed | skill design, references/edit.md §4.7 |
| G | Ending loudness | the last 10 s median short-term loudness <= the body's + 3 LU |
| G | SFX placement, real sounds only, density | skill design, references/edit.md §4.1-4.3 |
| S | Swears | 100% of strong swears bleeped where the channel's policy says so (skill design, references/edit.md §5) |

## 3.3 Captions
| | Criterion | Threshold |
|---|---|---|
| G | Accuracy, severity, track limits | skill design, references/edit.md §5 + §7 [FCC 47 CFR 79.1(j)(2); Netflix TTSG] |
| G | Placement + script | skill design, references/video.md §4 (never over the mascot, censor boxes or the game's own subtitles; the audience's reading script) |

## 3.4 Shorts and Reels (two products)
| | Criterion | Threshold |
|---|---|---|
| G | Format + structure | skill design, references/edit.md §1.6 (house 15-35 s, never > 60) |
| G | Safe zone + frame one | skill design, references/video.md §3.2-3.3 |
| G | Parity | the long's whole bar: scores >= 8.5, a fresh blind review, QC pass; reaches the creator WITH the long |
| G | Cover | skill design, references/video.md §3.5; its own feed test |
| S | Shelf frame | skill design, references/video.md §3.5 |
| O | Shorts viewed vs swiped | >= 70% good, < 60% fails [5,400 Shorts study] |
| O | Reels | 3-s skip rate below the account median; sends per 100 reach logged |

## 3.5 Thumbnails + titles
File 16:9, >= 1280x720, <= 2 MB; read at 168x94; title per the channel template (skill yt-package `CONFIG`), <= 100
chars, no profanity, no `<` `>`; the blind reads and click floor of skill thumbnail. O: CTR inside 2-10% [YouTube Help
7628154], < 2% fails, then >= the channel's own median.

## 3.6 Publish
| | Criterion | Threshold |
|---|---|---|
| G | API limits | title <= 100, description <= 5000 BYTES, tags <= 500 chars [YouTube Data API] |
| G | Chapters | 0:00 first, >= 3, each >= 10 s [YouTube Help 9884579] |
| G | Consent + credits | the creator's OK on this exact file; every CC BY credit line present |
| G | Schedule + links | no Short or Reel dated before the long's public time + 30 min; the end screen names a real video id; each Short's related video = the long, read back after a reload |
| G | Language | video, metadata and audio language set to what is spoken; a caption track in that language |

## 4. Outcome bands (L4)
0:30: >= 50% -> 9, 40-50 -> 7.5, 30-40 -> 6, < 30 -> 4 · CTR: >= 8% -> 9, 5-8 -> 8, 3-5 -> 6.5, 2-3 -> 5, < 2 -> 3 ·
APV (10-20 min): >= 45 -> 9, 35-45 -> 8, 25-35 -> 6, < 25 -> 4 · Shorts viewed: >= 80 -> 9.5, 70-80 -> 8.5, 60-70 ->
6.5, < 60 -> 4. After 5 videos re-base every band on the channel's own median (YouTube compares the last 10 of similar
length).

## 5. Calibration rule
After day 7: |L2 self-score - L4 outcome| > 1.0 -> find the missing criterion, add it here with a number and a source,
log it. A self-score without an outcome is "unvalidated". Decide rule changes on 3-5 videos, never one.
