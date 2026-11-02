# Film cut rules

Every shot in a VO film is picked under these rules. They come from a failed film cut ("rough zoom, rough camera, images
very bad, just cuts and bars", scored 3.5/10 by the creator after a frame-only review passed it) and a study of a
narrated game-film channel whose holds and scene changes drove its replay peaks.

## Hard rules (make the render step refuse a film EDL that breaks them)
1. **No synthetic zoom or push.** Digital zoom <= 1.3 only to hide HUD. No push, snap or whip. No crop above 1.3 (soft,
   pixelated).
2. **No slow-mo of any kind.** No frame-blended or frame-doubled slow-mo, no freezes. Every frame is a real frame.
3. **No stills.** No photo-mode pictures. Moving footage only (free-camera moving footage is fine).
4. **Camera moves are only the game's own:** cutscene glides and pans, rides, the player's own walks and turns. A smooth
   first-person turn is fine; a mouse flick is not (cut before it).
5. **No text-box close-ups.** The VO carries what people say. A person is shown WIDE at 1x in frames where no dialogue box,
   reply row, cursor, prompt, name tag or tracker is visible (a 2.39 letterbox hides a top bar; a HUD crop hides edge
   trackers; nothing hides a box: pick frames before it opens or after it closes).
6. **No menus, no HUD, no cursor** anywhere. A real number the story needs (money, debt, a day count) lands as a small
   chyron overlay (note `# CHYRON <number>` on the shot where it is said), never as a menu crop.
7. **No static wide over 2 s:** every shot longer than 2 s LIVES: the game's camera moves or the world moves in frame
   (people, traffic, water). A locked-off view with only rain is static. Measured, not judged: median shift >= 0.45
   px/frame at 480 px wide or median frame difference >= 3.0 = a living shot. A static insert (a newspaper, a sign) stays
   <= 2.0 s. (A frame-only cut failed at 35.8% static in its first 90 s; pro trailers measure 0%.)

## Edited, not cut
- **Every cut has a reason** written in the shot's note: it moves the story, answers the VO line, or lands on an action (a
  door, a turn, a vehicle passing). Cut ON motion where you can (the move starts in shot A, continues in B).
- **Match cuts / callbacks:** the same framing on two days (the window, the door, the counter), noted `MATCH: ...`.
- **Sound across every scene change:** a J-cut (the next scene's sound leads by ~0.25 s or more), an L-cut, or a shared
  bed. Two shots of the same place share one bed; a new place gets its own sound. The VO comes back with one short dry line
  after the event.
- **Breath:** after a heavy line, a wide holds 2-4 s with no VO. Never cut faster than the VO.
- **Breath holds:** 0.3-1.5 times a minute the VO stops for 8-14 s and the game's own picture and sound carry it, after a
  hand-over line. These were the reference channel's biggest replay peaks.
- **Day boundaries:** the day's first shot carries a ~1 s dissolve from the previous picture instead of a fade to black,
  except where a black is the story (the end).
- **One look per scene:** time of day and weather from the game, a light per-scene grade on top (nights a touch cooler and
  darker, a storm desaturated, golden hour warmer). A near-black shot gets gamma up (1.08-1.15) rather than being cut.
  Nights stay dark.
- **The picture changes inside every 10 s.**
- **Cutscenes cut to the one line that moves the story:** no uncut cutscene or NPC run over 30 s.
- **Slot length:** a VO slot needs lead (0.5 s, 0.3 on a hard cut) + the read + tail (0.5 s; slow lines 0.8) of REAL
  picture, in 1-3 shots. A 5-9 s wide with one move beats three 2 s snippets; a 3-shot slot that follows an action beats a
  9 s static wall.
- **Dread rule:** before each reveal the music goes out and the picture holds 1.5-2 s of room tone first.
- **Never digital silence:** a continuous game ambience bed under everything.

## Verify every shot before you write it down
- Grab frames with the crop and letterbox applied, exactly as the render will show them. Step 0.5 s across the whole span
  and 0.1 s at both edges. One leaked prompt, cursor or box = move the edge or drop the shot.
- Contact sheets of <= 12 tiles (3 a row, <= 1536 px wide) keep image reading cheap; detail = a zoomed tile.
- Write what you saw per shot: span, what is on screen, HUD state, the move, why it serves the line.
