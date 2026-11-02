# VO script: rules and template

Used by skill `roughcut` (watch-back VO over a gameplay cut) and skill `film` (a full VO that carries every word). The
script is a guide, never the truth: the creator says each line their own way, and what they SAID is what gets placed.
Learned the hard way: two fully written scripts read as cringe; the creator's own re-worded read was the keeper.

## Every line
- **Sourced,** in an HTML comment after the line: `[src: <transcript stem> <mm:ss> | their live words]` (the moment it
  speaks for), `[src: game <what is on screen>]` (a number on the game's screen) and/or `[src: story <what it bends>]`.
  Creative license: a story may bend motives, backstory and game facts, but the day count and money/debt numbers said or
  shown are real (a fake "100 days" is what comments catch), and nothing clashes with the picture.
- **In the creator's words:** lift their own live phrases from the transcript first (a line they already said, retold in
  past tense, is the best line); new words only as glue. Their everyday register (for a Hindi gaming audience: urban
  Hinglish, never bookish Hindi), English share near their own.
- **No machine phrasing:** a line that could be in anyone's video, stock phrases ("little did I know", "and that's when",
  "let's just say"), a neat rule-of-three, a moral, an em or en dash, a word they would never say = cut. The test: did
  they say something like it on the recording, would they say it to a friend, does it carry a fact only this video has?
  Any no = rewrite from the transcript or cut. Unsure = cut.
- **Short:** 8-12 words (max ~20), at their own speed (a fast talker at 230-264 wpm says 10 words in ~3 s), the punch
  word LAST, nothing after it.
- **No delivery markup inside a line** (no `/` beats, no `*stress*`): every rejected line in testing had them. A plain
  "say it: hyped / tired / slow" note after the line instead.
- **Room to rephrase:** each line has its point in a few words; they read it once, look at the picture, and say it.

## The checklist (N1-N15, from film narration and measured YouTube narration, 11 English + 11 Hindi videos)
| Id | Rule |
|---|---|
| N1 | Say what the picture cannot: the plan before, the number, the thought, the irony after |
| N2 | Never describe the action or explain the joke. Test: mute the line; nothing lost = cut it |
| N3 | Counterpoint, >= 1 per act: the line states the plan or calm they really had, the next shot betrays it |
| N4 | Hindsight ("that was the last time...") max 2 a video, only if it pays off |
| N5 | Time jump in one line with what changed: "Day 4 to 9, same work. debt 38k down to 21k." |
| N6 | The clock at every act break, the real on-screen number; lines shorten as it runs out |
| N7 | Rules early, once: the 1-2 rules that later matter, the creator as the newcomer |
| N8 | Plant only what pays off in the cut; an unpaid plant gets deleted |
| N9 | Punch word last, nothing after it |
| N10 | Specific beats generic: a real name, number, dish, their own comparison |
| N11 | At the 2 emotional beats, say less, slower, lower; no moral, no lesson |
| N12 | Turns, not chains: >= 1 "but" a minute; "then / after that" < 0.5 a minute |
| N13 | Exaggerate tone, never facts: "worst decision ever" is fine; "50 customers left" must match the screen |
| N14 | Hand-off rhythm: 1.5-2.5 VO -> live hand-offs a minute; the VO line before a live joke <= 6 words; never over a live line, a scream, a game line or a payoff; >= 0.3 s of air before their line |
| N15 | Rhythm and order: per ~10 lines at least one <= 4 words and one >= 14; never 3 lines in a row within 2 words of each other; every context line meets a real "but" within ~60 s; two context lines in a row = cut one. Write the LAST line first, then the first line it answers, then the middle |

Also:
- Gameplay VO is at most 40-50% of the spoken words; a film is 100% VO.
- Recaps and callbacks read as written: a slot the creator's live words can fill gets the live line, not a VO. Keep the
  VO for what they never said.
- Beat kinds: SETUP, NUMBER/CLOCK (re-said at every act break), RULE (once), PLAN (only if they said or showed it then),
  BUT (the line promises, the next shot betrays), TIME JUMP, HINDSIGHT (max 2), FEEL (only at the 2 emotional beats).
  Never a DESCRIBE line.
- Optional gates: a script checker that refuses unsourced lines, dashes, delivery markup and bookish words, plus a blind
  test (judges shown script lines mixed with real transcript lines; a line they pick as written is rewritten or cut).
- Keep a ground-truth file: every line the creator changed or refused, with what they said instead. It calibrates the
  next script.

## Template (the creator's file; the beat board with reasons and alternatives stays in a separate plan file)
```
# <video> · <game> · VO script
Read a line once, look at the screen, say it your way. Past tense, to a friend. Say less, not more.
Pause or rewind any time; flub = say it again and keep rolling. A live line of yours is playing = stay quiet.

## Before you press record
- Same mic, same spot, same chain as gameplay; record 5 s and play it back
- Headphones on; the preview muted or low, subtitles = the guide file (each line shows in its slot)
- Numbers the way you say them live

## The promise (0:12-0:40)
1. **0:12 · 6 s · SETUP** "<line>" · say it: <hyped/flat> · point: <the game in 4 words>  <!-- [src: ...] -->
2. **0:19 · 5 s · NUMBER** "<line>" · point: <the debt/goal>  <!-- [src: <stem> <mm:ss> | ...] [src: game ...] -->
3. **0:25 · 6 s · QUESTION** "<line>" · point: <what the viewer will wait for>  <!-- [src: ...] -->

## Act 1 · <the game's own milestone> · ends on BUT <real turn>
4. **3:10 · 4 s · PLAN** "<line>" · point: <what they expected>  <!-- [src: ...] -->
5. **4:05 · 5 s · TIME JUMP** "<line>" · point: <Day 4 -> 9, the number before -> after>  <!-- [src: ...] -->

## The end (<mm:ss>)
N. **~6 s** "<line>" · say it: slow, low · point: <the result vs Day 1's number>  <!-- [src: ...] -->
```
