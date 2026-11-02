# FILM_SCRIPT.md template

Copy to `<project>/cuts/<ep>/FILM_SCRIPT.md`. Every line is how the creator would tell a friend what happened, built from
what they actually said while playing (most lines quote them). The live mic is OUT of the film: this VO carries every word.
Times (m:ss) are estimates from the line order; the picture cut re-stamps them.

```
# <ep> · FILM SCRIPT (Day <a> to Day <b>) · the full voiceover, <N> lines

## How to read this
- Read the whole thing once before you record. Then say every line YOUR way: change any word, the order, anything that
  isn't you. What you actually say goes in the film (we transcribe your take, never assume the script).
- Calm, your normal talking speed, your usual voice chain. `slow` = that line can breathe, the picture holds there.
- A text box on screen = stay quiet until it has been read. Numbers the way you say them.
- Headphones on, the picture muted in front of you. One take per day is fine.

## For the picture cut
- SHOT = what plays under the line, from the shot libraries: `s1 404.0-410.0 (H03)` = session, source SECONDS, library id.
  Check the edge frame before you lock a cut.
- HUD fix per the library: clean / LB (2.39 letterbox) / LB+C (+ the HUD crop, <= 1.3). Box beats only where the box IS
  the beat, each <= 4 s.
- CAM = the game's own camera only: `still`, or the move the game makes. No push, snap or whip.
- Silences are marked `(no VO, n s)`; each <= 4 s except the planned HOLDs (8-14 s).
- Music = moods named per section, well under any line; a continuous game ambience bed under everything.
- Dread rule: before each reveal the music goes out and the picture holds 1.5-2 s of room tone.

## COLD OPEN · <what the world is> · <music> · beat cold_open 0:00-0:12
(no VO, n s) SHOT <s a-b (id)> <what is on screen> · <HUD fix> · CAM <move>
1. **0:02 · W1** "<line, the game's name early>"  <!-- [src: <transcript stem> <mm:ss> | their words] -->
   - SHOT <s a-b (id)> <what is on screen> · <HUD fix> · CAM <move>

## PROMISE · <the question the film answers> · <music> · beat promise starts by 0:30
4. **0:21 · PR1** "<line>"  <!-- [src: ...] -->
   - SHOT ...

## DAY <n> · <what the day is about> · <music>
(DAY <n> card, dissolve 1.0 from the last day)
9. **0:55 · V1a** "<line>"  <!-- [src: ...] -->
   - SHOT ...

## THE END · <the real number> · <the question>
<N>. **m:ss · VQ · slow** "<the open question, no sign-off after it>"  <!-- [src: ...] -->
    - SHOT ... · held 2 s after the last word, then cut to black.

## The arc
- Hook (0:00-0:45): the world's rules, the real number, the question, a flash-forward if the film has one.
- Rise / Loss / The trap closes / Fall: one line each, with the day range.
- End: the real number + the open question.

## Open loops (opened -> paid)
- <loop>: <line id> -> <line id> -> <line id>.

## Counts + gates (<date>)
- <N> lines; every line fits its picture slot at <= 2.9 words/s.
- Script checker: 0 problems; no "/" beats or *stress* marks; 0 em/en dashes; every line sourced.
- Blind judges: <n>/<N> lines read as the creator's own.
```
