# Blind review rubric: the long (3 reviewers, averaged) + every Short and Reel

Why 3 reviewers: one blind reviewer per cut steers the edit by its own scale (measured: the same cut moved 7.4 -> 6.8
when only the reviewer changed). Every long cut gets **3 fresh reviewers in parallel** (each a new agent; none sees
another's review), all on THIS row list. `ship_score.py` computes the score; no typed number ships.
Ship = **Ship score >= 8.5** and every row's average >= 8.5. Fix a weakness >= 2 of 3 reviewers name (their times overlap
within 3 s), or a measured gate fail; a point only one reviewer raises is weighed, not obeyed.

## Prompt (identical for all 3; fill the paths and the format line)
You are a fresh blind reviewer of a finished YouTube video (<one line: format + audience, e.g. "a faceless gaming comedy
for a Hindi-speaking audience">). Read ONLY: the render `<mp4>`, its QC report + minute frame sheets, its watch pack (if
the project makes one), the word-timed transcript, the template audit (numbers only), the music credits, and the
scorecards (skill final-review, references/scorecards.md). Never the build script, the edit list or any earlier review.
Pull your own evidence (frame sheets <= 12 tiles, <= 1536 px, <= 20 images; audio measures). Write `<out>.md` with:
§1 a table `| Row | Score | Evidence |` with EVERY row below, named exactly, score 0-10 (one number), evidence in output
times; §2 the overall; §3 the weakest moments ranked by retention impact, numbered, each with its time (m:ss or a span
m:ss-m:ss) and an exact fix; §4 a table of wrong captions; §5 the first 30 s second by second with a predicted % still
watching at 0:30; §6 what a top small channel in this niche would do better with this footage; §7 the CLOSE POINTS:
watch as a stranger who clicked the title, list every moment you would close the tab, why, and the fix, plus what in
the first 15 s keeps you to the end. Score gates from the numbers (8.5 = meets the spec), judgement rows as a stranger
who has never seen the channel.

**Density rows are judged on placement, never by count.** Every device (sound, camera move, speed change, freeze,
overlay, music change, text, a game gag) must land on a named moment (a spoken word, an on-screen event, a laugh); type,
slot and timing vary; nothing runs at a fixed rate (a device after every line is a metronome). More devices never raise
a row; a device that is not placed lowers it. **Readable density** = after every busy stretch a viewer can still repeat
the creator's line. **Music per section** = each section's music is audible, distinct and fits (one bed all the way = low).

## Rows (exact names)
Black picture · Frozen picture · Flashes · First 30 s · Format (long) · Voice-over lines · Ending · Rhythm · Readable density ·
Device placement · Pacing vs reference · Integrated loudness · True peak · Voice on a phone · Music bed · Music per section ·
Ending loudness · Cuts · SFX placement · Real sounds only · SFX density · Never silence · Swears · Caption accuracy ·
Caption severity · Caption track limits · Caption placement · Hook strength · Payoffs per minute · Dead air removed ·
Pacing contrast · Captions in the audience's script · Ending drag · Policy-safe · Story for a stranger · Body density ·
Overlay fit · Joke or insight quality

## AI-feel gate (same pass, before §1; it can only lower the overall)
Why (measured): a cut scored 8.29 on the plain row mean; the creator gave it 5 and called it machine-made. The reviewers
had SEEN the tells (repeating sticker pops, one template, cards echoing his words) but filed them under one row the mean
diluted; none could hear, yet the sound rows got 8-9.

**Before the reviewers (the session, numbers only, keeps the pack blind):** if the project has a template-audit tool,
run it on the edit list + transcript; otherwise count by hand from the edit list and write `<stem>_template.md`: per
tell below, the count, the times, HIT when it crosses the line.

**§0a AI-feel audit**, under the heading `## §0a AI-feel audit`: table `| Tell | 0/1/2 | Times | Why it reads as template |`,
one row per tell, the first cell starting with its id. 0 = absent; 1 = once or twice and motivated; 2 = a PATTERN (>= 3
times, the same asset / slot / sound reused, or not motivated by the picture or the creator's words).
- Measured (copy from `<stem>_template.md`, a HIT = 2): T1 emoji/sticker pops · T2 a persistent HUD/meter/counter we
  added · T3 inserts in one fixed slot/frame · T4 word cards that repeat what was just said · T5 one stock-library
  composer for all the music · T6 an SFX preset (one sound family, the same file again and again, a sound on every card) ·
  T7 a device after the line (> 40% of the creator's lines end in an added device).
- Judged from your own frames: J1 a meme where it does not belong (generic, not about THIS picture or line) · J2 an
  effect nothing on screen or in the words asked for · J3 one device as a metronome (you can predict the next) · J4 preset
  transitions (glitch/RGB/flash as glue) · J5 one visual language for every insert (same border, tilt, font, entry) ·
  J6 the edit labels or explains the joke instead of building it · J7 anything a stranger would call "AI-made" at first
  glance (name it).
- **AI-feel cap** from P = the number of tells at 2: P = 0 none; 1-2 -> 7; 3-5 -> 6; >= 6 -> 5.

**§0b Human side by side.** Frame sheets at the SAME fps and tile count of 3 of our minutes (the first, the middle, the
last full one) and 3 minutes from human-edited reference videos the project keeps (its role models). Per pair, forced
choice: which one looks made by a person; which one you would keep watching; one line why, naming the device.

**§0c Gate rows** under `## §0c Gate rows`, table `| Gate row | Score | Evidence |` (a reference minute = 8):
| Gate row | What it asks |
|---|---|
| Feels made by a person | from §0a + §0b: would a stranger guess a person cut this, for this moment? |
| Fun to a stranger | a stranger who clicked the title: finish it AND send it to a friend? |
| Sound quality | if you cannot hear, judge from the measures, the template audit and the credits, write "(not by ear)"; max 7 unheard; -1 each for a T5 / T6 HIT |

**§0d Anchor (when the project has one).** The same sheets from a cut the creator rated low (an anchor, with his number).
For each gate row: better / same / worse than the anchor and by how much; not clearly better = <= 5.5 on that row.

**Unheard rows:** Music bed, Music per section, SFX placement, Real sounds only, SFX density, Swears and Caption accuracy
judged without listening carry "(not by ear)" and score at most 8.

**Overall:** `Gated overall = min(row mean, AI-feel cap, Feels made by a person, Fun to a stranger, Sound quality)`.
Write `**Gated overall: X** (row mean Y; capped by <row>)`; `ship_score.py` recomputes it (TYPED != COMPUTED = the
computed one ships). Validated: 2 fresh reviewers blind to the creator's 5 gave gated 4 and 5 on that cut (row means 7.56
and 7.51) and named the meter, emoji, framed memes, echo cards, stock music and SFX preset unprompted.

## Short / Reel review (every Short AND every Reel cut, one file each)
A fresh reviewer per file (one agent may take several files; more reviewers per file are averaged) reads ONLY that
render, its QC sheets, its transcript, its template audit, its credits, its cover and the Shorts scorecard. Never the
long or the brief. One file per Short with:
- `## §0a AI-feel audit`: T1-T7 + J1-J7 exactly as above (P sets the same cap).
- `## §0c Gate rows`: Feels made by a person · Fun to a stranger (watches to the end in the feed AND sends it).
- `## §1`: `| Row | Score | Evidence |` with every Short row below; sound judged unheard carries "(not by ear)", max 8.
- `## Questions`: `| Question | Answer |` with 4 rows named exactly: What happened · Why is it funny · Want to finish it ·
  Watch the full video. A blank, "not sure" or "no" = RE-CUT, whatever the score. For a non-comedy channel ask
  "Why is it worth it" in the second row and name it so in the rows below too.
- `## §3`: the weakest moments, each with an exact fix in output times.

## Short rows (exact names)
Hook 0-1 s · Zero-context payoff · Pace · Readable lines · Picture cleanliness · Sound · Loop or ending ·
Reason to watch the long · Platform fit · Cover

## Calibration ledger
Keep a table in the project: `| Cut | Date | Gated | Row mean | His words | His number |`, one row the moment the
creator rates a cut. When the latest |gated - his number| > 1.5, re-check the cap ladder before the next stamp.
