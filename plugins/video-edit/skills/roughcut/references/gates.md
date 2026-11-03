# Rough cut gates

Never show the creator a cut that fails a line. Tools are optional: each gate names what to measure, and any tool that
measures it will do. Where a gate needs a visual, motion or sound judgment, the rule is in skill design,
references/edit.md.

1. **Pre-render check: zero errors,** and every warning answered in the report (fixed, or one line why it stays). A gap
   filled by a meaningless sound is worse than the warning. Warnings worth checking: dead stretch (> 1.2 s with no words,
   sound, overlay, text or game event), flat stretch (> 4.5 s with no orienting event; an error in the first 30 s),
   overload (> 3 events in 1 s outside a payoff burst), fast-forward, bare jump, cadence (minute one < 20 cuts), talk
   < 70%, nothing new for > 90 s, zoom and device budgets, boss rules, the same sound file twice within 60 s.
2. **Delivery QC:** every row of skill design, references/edit.md §7 (loudness -14 LUFS +- 1, true peak <= -1 dBTP,
   <= 3 flashes a second, A/V sync and length, black or frozen picture, clicks and holes at cuts, silence, the voice on a
   phone speaker). ffmpeg's `ebur128`, `blackdetect` and `freezedetect` filters cover most of it. Fixes: a click at a cut
   (a loud sound starting within ~20 ms of the piece's end) = end the piece ~0.05 s earlier or keep the sound whole; a
   sound hole is filled with the game's own sound, not a louder bed.
3. **Watch it whole:** picture and sound, full runtime, at 1x, never only the transcript or stills. Then a 1 fps contact
   sheet end to end: no menus or HUD junk left, memes land on meaning, the brand character's faces match the creator's
   mood, text readable on a phone. Then the watch pack: `uv run --no-project --with numpy python
   ${CLAUDE_SKILL_DIR}/../../tools/watch.py <render.mp4> --words <words.json> --sheets` and read watch.md top to
   bottom (DEAD, STEP, UNCUED, FLASH, FROZEN, SILENCE flags; each fixed or defended in one line).
   **Every join, on the RENDER:** a strip of frames + waveform at each cut, +-1.5 s, read from the rendered file (not
   the source): no visual jump the cut did not mean, no waveform spike, no caption hidden under an overlay, no overlay
   off its moment. Read consecutive frames (not a sparse sheet) around every cut, entrance, exit and flash: a 1-3 frame
   error only shows frame by frame. The rendered duration matches the EDL within one frame. A shot boundary time is
   frame / fps rounded DOWN (frame 83 at 30 fps = 2.766666 s; 2.767 lands a frame late). Captions burn last in the
   filter chain so no overlay covers them.
4. **Swears and safety:** every strong swear and every flagged clean-spelled swear bleeped (or the creator's "no bleeps"
   logged); monetization numbers inside the limits.
5. **Voice:** the edit adds NOTHING on top of the recorded voice (no denoise, pitch or EQ by default; never post-process a
   disguised voice back toward natural); no clipping; a clarity problem on the raw is told to the creator before the next
   recording, not fixed by stacking filters.
6. **Meaning-first table** in the report: moment / what the creator means / device, for every meme, text and sound. No
   editor-invented irony.
7. **Human-feel audit:** for every device, what should the viewer FEEL, and would a real person feel that? Checked twice
   (the table + the contact sheet). A device that could read as random, cringe or robotic is cut.
8. **Caption proof:** a second ASR model re-hears every caption; every line under 0.8 agreement and every line where the
   two models disagree is listened to and fixed or hidden; no open swear. Every aside keeps its setup.
9. **Contact sounds sit on the game's own hit frame** (0 off-hit); no same-sound repeat (rules: skill design,
   references/edit.md §4.2-4.3).
10. **Story:** progression.md + missed_funny.md exist, every callback's setup piece is in the timeline, `## Links` has
    <= 1 in 5 AND THEN.
11. **Template tells:** the counted tells T1-T7 in skill design, references/edit.md §8.2 (T1 emoji or sticker pops, T2 a
    persistent meter, T4 echo cards block the cut; the rest need a fix or one line why it stays) plus the judged tells
    J1-J7 in §8.3, whose count caps the AI-feel score.
12. **On-screen words:** every slam, card and hook is what the creator says around it or marked as the game's words or a
    callback. A card that only repeats the line is still an echo.
13. **New devices:** a device type not shipped before appears ONCE in this cut.
14. **The algorithm's read:** the game's name said by 0:30, the promise shown by 0:30, minute one shows the core loop, the
    cold open's tease pays off in the last third, fresh beats near 3:00 and 6:00. Watch the first 5 minutes twice as a
    viewer: cut where it gets boring, keep the breathers (slow is fine, boring is not).
15. **Blind review:** a FRESH reviewer (no access to your notes) watches the render and scores it with your rubric; a
    separate fresh listener judges sound alone (fake, glue, buried words, silence). Every row >= 8.5 or it does not reach
    the creator. A re-cut must beat the cut it replaces head to head twice, order swapped, a fresh reviewer each time.
