---
name: roughcut
description: Turn a raw voice-led gameplay or commentary recording into a comedic rough cut. Transcribe the mic track, find setup/punchline pairs, reactions, callbacks and dead air, write a story map with BUT/THEREFORE links, then an EDL (edit decision list) with jump cuts, holds, captions, a brand character overlay and on-screen words taken only from the creator's speech or the game, then render and self-score before anyone sees it. Use for "rough cut", "edit this recording", "cut this gameplay", "make the first cut", "find the funny bits", "write the EDL", or any long-form edit of a commentary recording.
---

# Rough cut

status: beta

Input: one raw recording (or several blocks of one session) that went through skill `after-recording`: tracks checked,
privacy scanned, transcribed. Output: an EDL, a story map and a rendered rough cut in `<project>/cuts/<ep>/`, scored before
the creator sees it.

Visual, motion and sound rules (zoom budget, text, motion feel, SFX placement and caps, music levels) live in
**skill design, references/edit.md**. This skill decides WHAT happens WHEN; that file decides how it looks and sounds.
The edit rules this skill owns are in [references/edit-rules.md](references/edit-rules.md); the gate list is in
[references/gates.md](references/gates.md).

**Film or gameplay?** A cinematic VO story film (the creator's live mic out, a scripted VO carries every word) follows
skill `film`. Every gameplay device below (punch-ins, holds, slow-mo, stings, snaps, the rewind gag, still cards) is for
gameplay cuts only.

**Session split (saves context, same gates):** session A runs steps 0-2b: reads the transcript once, writes the story map,
the EDL draft and a STATUS block in `cuts/<ep>/BRIEF.md`. Every later session (render, notes, fixes, Shorts) starts from
BRIEF STATUS + the EDL and greps the transcript for the window it needs.

## 0. Context, concept and the game first
Before any edit, script or packaging:
1. Read the WHOLE transcript, start to end. Every claim about the video carries its timestamp and says WHEN it is true (a
   character's role, a plan, a number can change mid-recording).
2. Research the live context: news, collabs, updates and trends around the game and any creator the video references.
3. Write `cuts/<ep>/CONCEPT.md`: premise, the facts (with `@<seconds>` evidence from the start, middle AND end of the
   recording), the key beats, and a `## Flavour` block, one line each: opening montage (fails / chaos / best moments),
   signature device, music mood per act, chaos level, running gag, then `confirmed: <the creator's words + date>` (or
   `confirmed: by the recording @<s>` when the recording makes it unmistakable). Optional `## Glossary`: one
   `- term: meaning` per word a stranger could not place.
4. Write `cuts/<ep>/GAME.md` (researched, sources listed): the game in five lines, the mechanics that show in the footage,
   this episode's enemies and moments with the caption and SFX spelling for each, the jokes players already share. Check
   every caption, sound and joke against it.
5. Send the creator ONE concept message before the first cut: premise, why the video exists, the key beats, the spine, the
   flavour lines, their 3-4 style questions, and "is this right, or would you improve anything?". Keep working while they
   answer. Never ask what the recording or CONCEPT.md already answers.
Optional gate: make your render step refuse a cut whose folder has no CONCEPT.md (with a confirmed Flavour) and GAME.md.

## 1. Transcribe and read
- If there is no transcript yet, run one detached (`scripts/job.py`, see skill `after-recording`). Optional tools:
  Whisper or WhisperX with word alignment; a second ASR model as a "second ear" for low-confidence lines; a laughter
  detector (jrgillick/laughter-detection, MIT, CPU) over the mic track.
- Useful transcript markers to add or look for: loud windows (yells, laughs), game-audio spikes (explosions, deaths),
  silences, laughs, and lines the ASR may have invented in quiet or music stretches (outros like "subscribe" or "thank
  you" that were never said: listen before keeping one). A stretch where the ASR loops one word has fake word times:
  listen, caption by hand or cut.
- Captions are drafted in the creator's own script (for a Hindi gaming audience: Roman-script Hinglish, never
  Devanagari on screen; English words stay English).
- Read the pre-production pack if one exists (the story script, the bit pack, the plan) for the intended shape.

## 1b. Show what the creator names (optional)
Detect every moment where the creator names or finds an on-screen item (a cue detector over transcript + frames, or a contact
sheet with grid lines at 0.25/0.5/0.75). Where the item is really shown, split the segment there and aim a punch-in at it.
How big and how often: skill design, references/edit.md.

## 2. Find the comedy (not only the loud bits)
Start from the creator's spoken markers (skill `after-recording` step 5): every "clip" marker (the 20 s before it) is a top moment
and a first Short candidate; every about-to-try line followed by a yell, laugh or hit within 15 s is a setup/payoff pair
and a Short hook; every thumbnail marker goes to the thumbnail step; their last ~90 s per block are raw words for the title.
Tag every candidate with segment ids and times:
- **Setup -> punchline:** an expectation stated ("nothing will happen, trust me") then broken (death, fail, game spike,
  sudden loud). The gap between them is the edit's playground.
- **Reactions:** loud windows, laughs, swearing-adjacent outbursts right after a game spike.
- **Tangents:** keep the ones with a payoff line, cut the rest.
- **Callbacks / running gags:** a phrase or situation that recurs. Keep every instance.
- **Dead air / filler / retakes:** silences, "umm", restarted sentences, menu-browsing narration. The transcript must be
  verbatim (prompt the ASR to write fillers down; a model that normalises them away hides every cut point). Rules that
  hold up: a **retake** = an unfinished fragment followed by a sentence that opens the same way, or a spoken cue
  ("scratch that", "once more"): keep the last take. Two FINISHED sentences with the same opening are only listed for a
  listen, never cut automatically. A **stutter** = the same word twice under 0.25 s apart with no comma, or a repeated
  two-word phrase; words people repeat on purpose (very, really, no, yeah, and their equivalents in the creator's
  language) are excluded. In a comedy cut a stutter or fumble that IS the joke stays.

## 2b. Story map BEFORE the EDL
Write two files from the WHOLE recording (full transcript + a contact-sheet pass), not only the flagged lines:
- `progression.md`: every purchase, unlock, boss spawn, death, upgrade, with times (the story a stranger must follow).
- `missed_funny.md`: every funny line or moment, kept or cut, and why. Every marker and every detected laugh gets a row.
- **Links: BUT / THEREFORE, never AND THEN** (the South Park writers' rule). `progression.md` ends with `## Links`, one
  line per join between kept moments in cut order: `- 3:10 -> 3:42 BUT the rod snaps` / `THEREFORE they buy the net` /
  `AND THEN`. At most 1 in 5 links may be AND THEN; each extra one gets a cause shown (the creator's line or the game's screen),
  is merged into its neighbour, or is cut.
- Every callback in the cut lists the piece where its setup is on screen: a joke never plays without what it answers.
- **A beat that rests on one of the creator's lines is proven by ear, not by the ASR:** a second ear agrees (a second model scores
  the line >= 0.8) or someone plays the clip and writes what was said. A line that fails is a plain line at most, never a
  story beat, gag, bridge or Short hook.

## 2c. Watch-back VO (long videos)
A watch-back VO is a short scripted narration the creator records after seeing the picture cut: act openings, time jumps, the
plan before a big choice, the number at each act break. Script rules and template:
[../vo-session/references/vo-script.md](../vo-session/references/vo-script.md).
1. **Picture first:** cut the story (2b) with the live lines plus room for narration; render it as `<ep>_picture.mp4`.
2. **Script:** a beat board (`narration_plan.md`, the closing line written first), then `VO_SCRIPT.md` from the template:
   the creator's own live phrases first, every line sourced, 8-12 words, punch word last, never describing the picture. VO is at
   most 40-50% of the spoken words in a gameplay video, never over a live line.
3. **Record and place:** skill `vo-session`.
4. **Radio cut, then picture:** VO + live lines + game sound only (no music, no SFX), one eyes-closed listen at 1x; fix
   order and pauses; then re-cut picture to it (change picture on the VO's full stop, the VO enters right after the creator's own
   live reaction, 0.6-1.2 s of game sound after a setup line); then music, SFX, devices.
5. **Five review passes, one job each:** radio, 1x without stopping, a "why stay?" line per 30 s, devices + sound, a
   blind review.

## 3. Write the EDL
Rules for structure, cuts, comedy devices, on-screen words and safety: [references/edit-rules.md](references/edit-rules.md).
How each device looks and sounds: skill design, references/edit.md. The short version:
- **Shape:** cold open (the creator's funniest real moment that pays off the thumbnail, ends by 0:15) -> promise (starts by 0:30,
  over quick clips from the whole video) -> 4-6 acts on the game's own milestones, each opened by a bridge (where we are +
  the number) and ending on a turn -> payoff + callback + the creator's own live sign-off. They say the game's name by 0:30.
- **Mark beats in the EDL** so a checker can read the structure: `cold_open`, `promise`, `bridge`, `turn`, `new` (an
  upgrade, a purchase, a new number, a twist), `gag`, `callback`, `payoff`, `tease` + `tease_payoff`. Every piece also
  carries `quote` (the first and last words it keeps) and `reason` (why it stays): the paper read and every later
  session read the cut from these without re-opening the transcript.
- **Cuts:** keep whole moments (setup -> payoff), cut dead air, menus and retakes; tighten pauses over ~0.6 s; let
  sentences finish; ~1 s of the game situation before the line after a jump; cut to the reaction within 0-3 frames.
- **Calm baseline, density at the spikes:** the first 2 minutes are the densest; after that the creator's talk is the glue and
  devices sit on payoffs only. Something new at least every 90 s; a re-hook (turn or bridge) at least every ~4 min.
- **Every device answers one line the creator said or one thing the game did.** Nothing on a timer, nothing as wallpaper. If you
  cannot say what a device means HERE, cut it.
- **On-screen words = the creator's exact words or the game's real words.** Never editor labels, irony or summaries.
- **New devices are tried once:** a device type the channel has not shipped appears in ONE place, named with its
  timestamp in the review message; it spreads only after the creator has seen it.

## 4. Captions
- Every segment carries an automatic caption draft. Correct only the segments whose draft is wrong (a misspelt English
  word, a mishearing, a name), keeping the same word order and ideally the same word count so word timing still maps.
- Strong swears: a comedic bleep by default (audio muted + a tone, `****` in the caption); Shorts always bleeped; skip
  only when the creator says "no bleeps" for this video (log their words). Keep the first minute lighter.
- Captions big and high-contrast, readable on a phone (sizes and placement: skill design, references/edit.md).

## 4b. Brand character overlay (when the channel has one)
A faceless channel's brand character (an avatar or mascot) works as the face cam. The editing session places it; never
ask the creator to.
- **It is the creator,** not a separate character with its own lore. It has only the creator's real traits.
- **Source of truth:** only the brand's own approved asset source (vector build, rig or approved pose set). Never
  AI-generate, redraw or trace it.
- **Never deform it:** no squash, stretch, skew or non-uniform scale, anywhere, animation included. Uniform scale, tilt
  and move only. Retire any approved pose that is itself squashed.
- **Default look only:** no costumes, hats or outfit layers unless the creator approved them.
- **Placement:** a corner by default, away from HUD (minimap, speedometer); off only when every corner holds critical HUD.
- **Behaviour:** lip-syncs to the creator only; reacts to the REAL moment, timed to the word or game sound it answers
  (a reaction anchored on a word, not a whole-piece state); hides during stings, cards and inserted clips.
- **Size and motion** (the reaction ladder from corner to full screen, face changes, mouth sync): skill design,
  references/edit.md §2.7.
- **Never on a stock human body,** never in a VO film's body.

## 4c. Quotable moments
List every timestamp-able moment in the cut (a line, a fail, a reaction someone would quote in a comment). Any 60 s
stretch with none gets tightened or cut. Viewers comment timestamps of specific moments, so these are what the cut is for.

## 5. Render, self-score, report
1. **Paper read before the first full render:** a FRESH agent gets ONLY the cut list (each piece in order: time, the
   creator's words, what is on screen, the beat), your story rubric and the format above, and scores story and structure as a
   stranger would, naming the flattest stretch and anything heard twice. Fix structure on paper until it reads >= 7.
   Renders are for sound and picture, not for finding the story.
2. **Pre-render checks** (instant): missing files, typo'd keys, times past the source, bleeps outside their segment,
   wrong script on screen, monetization safety (commentary >= 35% of runtime, no 45 s silent stretch, <= 1.5 unbleeped
   strong swears a minute).
3. Render a draft (1080p fast); master later (1440p from a 1440p raw keeps punch-ins sharp).
4. **Run every gate in [references/gates.md](references/gates.md).** Never show the creator a cut that fails one.
5. **Self-score** against your quality rubric (each row 0-10; 8.5 = meets the published spec). Fix the weakest row in the
   EDL and re-render before showing anyone. Log the score row for THIS cut.
6. **Report:** the score, final runtime vs raw, the hook chosen, NEW THIS CUT (each new device + its timestamp), a table of
   stings, speed ramps and beats with output timestamps, moments cut that might be worth restoring, missing assets.
- Tweaks = edit the EDL and re-render, never start over. A revision the creator named: diff the new EDL against the cut they
  watched and revert every line that is not one of their notes.
- Keep a clean twin of the approved cut (no captions, no graphics) plus its word timings and overlay spans: Shorts,
  thumbnails and metadata read them in place.

## Done when
CONCEPT.md (confirmed Flavour) + GAME.md + progression.md (with `## Links`) + missed_funny.md exist; the EDL marks the
beats; every gate in references/gates.md passes; the score row is logged; the report is written.
