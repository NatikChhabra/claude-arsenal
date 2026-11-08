---
name: music-review
description: >-
  Score a song or music video against the arsenal's bar before the owner sees it: measured gates (lyric_lint, loudness,
  encode, phone-speaker vocal, beat-locked cuts, flashes), scored rows anchored to a reference, human blind listeners
  for anything audible and fresh blind readers for text and picture, ship at every row 8.5 or more. Use before any music
  delivery, for "is this ready", "review my song", or before release-rollout.
---

# music-review

status: draft (full rubric; promote to beta after the first real review)

Claude cannot hear audio. Audible judgements come from people (the owner and blind listeners) and from measurements;
Claude scores the rows it can check and reports the listeners' words verbatim. Never write "it sounds great".

## 1. Gates (any FAIL = fix before scoring)
| Gate | Command | Pass |
|---|---|---|
| Lyrics | `python ${CLAUDE_SKILL_DIR}/../../tools/lyric_lint.py songs/<slug>/SONG.md --bpm <BPM>` | 0 FAIL, every WARN fixed or defended |
| Master | `python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <master.wav> --target <target>` | PASS |
| Encoded master | the same on the AAC/MP3 a platform makes (mix-master §4) | true peak under the ceiling |
| Phone-speaker vocal | `loudness.py <mix> --vocal <lead> --inst <instrumental>` | buried <= 10% of sung windows |
| Arrangement built | every layer in produce-arrange's energy map is in the bounce; per-section RMS of the master: each chorus 2+ dB over its verse, the last chorus the loudest section, the bridge or breakdown 3+ dB under the chorus | all true |
| Clicks | scan the master and each stem for single-sample jumps over 12x the local median (edit and slice edges need 3-5 ms fades) | none left unexplained |
| Credits and rights | `songs/<slug>/CREDITS.md` complete; release intent matches every tool's plan | complete |
| Video cuts | `beatmap.py cuts <map.json> <edl> --fps <fps>` | >= 90% on grid outside marked cuts |
| Video QC | design references/edit.md §7 table (flashes, loudness, black/frozen, sync, identity) | all pass |

Gates say a file is technically clean, never that the song is good. On 8 Nov 2026 a demo passed every gate above
and the owner rated it -1: "missing everything" (it was one stitched guitar and a thump). Nothing goes to the owner as a
song until the arrangement gate passes; a draft sent earlier is labelled a draft, with what is still missing.

## 2. Scored rows (1-10; 8.5 = meets the reference song or a pro release in its genre)
Score each with one sentence of evidence (a measurement, a listener's quote with its time, a frame). No evidence = no
score above 7.
| Row | 8.5 looks like |
|---|---|
| Hook | 2 of 3 blind listeners can hum or quote the chorus after one play |
| Lyrics | the blind reader names what it's about and quotes a line; no line flagged as machine-written |
| Vocal | no listener flags a fake or robotic spot; breaths and timing feel human |
| Guitar | his part is audible and central in the mute test and on a phone speaker |
| Arrangement | each section change is felt in its first second (listener notes at the boundaries) |
| Mix | vocal clear on a phone speaker (measured), level-matched A/B against the reference holds up for the owner |
| Master | targets met on WAV and encode; no listener notes distortion or pumping |
| Video idea | a stranger states the thesis after one watch; held moments land |
| Video craft | cuts on grid (measured), text readable at phone size, 9:16 re-laid out, no flash violations |
| Identity and rights | a real human artist identity (no photoreal AI persona: Spotify's AI Persona badge cuts all recommendations), disclosures ready |

## 3. Blind reviews
- Listeners: the owner plus at least 2 people not told how the song was made. Ask only: would you replay it; which
  part do you remember; does any moment sound fake, and where. Record their words with timestamps.
- Text and picture: a FRESH agent with only the lyrics (or only the video frames and lyric sheet), never our
  reasoning: what is it about, what would you quote, what reads machine-made.
- A "sounds AI" or "reads AI" with a location = fix that spot and re-test with a NEW listener or reader.

## 4. Ship bar and report
Every row >= 8.5, 0 gate FAIL, fresh blind reviews done. Iterate while scores rise; stop on plateau and report the
scores as found, never rounded up. Report: gates with numbers, the row table with evidence, listener quotes, the top 3
fixes made, anything still below the bar and why.
