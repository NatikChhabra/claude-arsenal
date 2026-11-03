# Video edit: feel, motion graphics, camera, sound, captions, film look, QC, slop tells

Use when: cutting or reviewing a video edit (long video, Short, Reel, film, personal edit), placing devices, animating overlays or a character, mixing sound and music, burning captions or bleeps, grading, or running QC before delivery. Packaging (thumbnails, covers, text look and sizes, composites, blind-review methods) lives in `video.md`.

Scope and overrides. These rules are for rendered video, timed in frames. Where they differ from the web and game references, the video rule wins on video:
- Overlay exits ease IN (`power2.in` / `power3.in`) and run quicker than the entrance (timings in §2.2). motion.md's "never ease-in" is a UI rule.
- Overshoot caps are lower than experience.md's `back.out(2.5)` pop: past §2.3's caps reads as the preset zoom-and-bounce look.
- Squash and stretch never applies to a brand character or any character that stands for the creator. It is fine on non-brand game objects.
- A character's face changes through drawn in-betweens, never the opacity crossfade used for UI state changes.
- UI sounds (ticks, pops, blips, 50-200 ms synth tones) from experience.md are banned in video edits; video uses real nameable sounds only (§4).
- Music sits 10-18 LU under a voice (§4.7), not experience.md's 3-6 dB duck under effects.
- Light grain, glow and grades are allowed in video grades (§6). The web grain ban does not apply.

## 1. Edit feel and devices

### 1.1 What "chaotic" means
- Chaos = many high-quality layers stacked where a beat lands: sound + camera + speed + freeze + text + the character + a music shift + game-based gags, each placed ON something. Cuts per minute alone is not chaos. Memes are rare and only where they belong.
- Smooth chaos: energy comes from cuts, pacing and design, not loudness, with one beat per punchline. "High but not loud": each punchline gets a beat to land.
- Toolkit to place well (never one device as wallpaper): snap punch-in, slow push, pull-out reveal, decaying shake, speed ramp on real action, freeze frame, hit-stop, key-word slam, caption size change, beat look (§6.1), letterbox slide, character reaction, music drop or snap-back, a real sound, a voice FX on one line, a glitch only where the game really broke, a callback replay, a meme still.
- Comedy devices that work: make the expectation explicit before it breaks (the brag captioned, a slow push on the setup, the UI's promise punched in); contrast (a flat lowercase caption on a disaster, `dramatic` on something trivial, the sound dropping out on the violation); rule of three (show it twice, break it the third time; repeated fails get shorter each round); reaction first (the reaction on its frame BEFORE the cause, then the cause wide, as a hard-cut reorder).

### 1.2 Placement
- Every device answers one line the speaker said or one thing the game did. Nothing on the clock, nothing as wallpaper. One focal point per moment; a pop never covers what the joke is about.
- Human-feel audit per device: moment -> what the speaker means -> what the viewer should feel -> would a person actually feel that? Unsure = cut.
- Timing is the joke: cut to the reaction 0-3 frames after the surprise, cut away right after a visual punch, land the cut on the last syllable. Payoffs are never pre-announced by text.
- Deadpan hold 0.5-0.9 s only on a real deadpan, never freeze-silence after an ordinary fail.
- Read before energy: no zoom, shake or RGB split while text that matters is on screen. A punch-in snaps in and HOLDS.
- Readable chaos: no new element from 0.3 s before the punchline word to its end (the stack lands on the REACTION); at most 3 transient layers; SFX peaks >= 6 dB under the voice while it speaks.
- When a specific meme is named, use that exact meme and research it first. A contradiction joke hits FULL screen (a hard cut to the near-death), never a zoom-down into a box under a word.

### 1.3 Density and rhythm
- In the body, something new for the eye or ear about every 2-3 s, from the MIX of device types (cut, text, zoom, meme, speed), not from added sounds. Irregular gaps, varied types. A body with "the cheese removed" bored the owner at 2-4 min.
- Attention gates: no window over 4.5 s of output without an orienting event (cut, zoom start, pop, motion, SFX, flash, speed change; talk alone does not count; in the first 30 s this is an error). After 2:00 in a long video, talk counts as the calm glue. At most 3 events in any 1 s except a deliberate payoff burst. The same device type never 4x in a row.
- Cadence: warn when a minute's shot lengths are too uniform (coefficient of variation < 0.35) or no shot in a minute runs over 6 s. Long takes for setups and the game, bursts for payoffs (1/f shot-length variation, Cutting 2010).
- The rush only rises or holds; the climax is the densest minute (in events and stakes, not necessarily cuts) and the end is a high (peak-end).
- No dead switches: every non-speech moment over 1.2 s has a reason (an action peak, a meme, text) or is cut. A sag is not a deadpan.

### 1.4 Cutting
- Keep whole moments (setup -> payoff), cut only dead air, menus and retakes: about 8-15 cuts/min in the body. Measured: 29 cuts/min at a 1.1 s median was choppy AND flat; a pro reference ran 8/min at 2.8 s.
- Auto-tighten pauses over 0.6 s inside a piece. A tightened pause shrinks to a beat, never to zero, and the beat is the recording's own room or game sound, never digital silence. Talking-head defaults that read natural: 0.30 s mid-sentence, 0.45 s after a sentence, 0.9 s before a card or a turn. Skip a tighten that saves under ~0.4 s: a tiny jump looks nervous. A real deadpan hold (§1.2) is not a pause.
- Where a cut may fall: a gap of >= 400 ms between words is a clean cut point; 150-400 ms only after a look at the frames and waveform; under 150 ms never. Never cut inside a word: snap every edge to word boundaries, then pad it 30-200 ms for timestamp drift (about 50 ms before the first kept word, 80 ms after the last). A laugh, sigh or breath at an edge stays whole: extend past it.
- After any jump, keep ~1 s of the situation BEFORE the line. Keep 5-15 s of setup with every punchline. A piece ends where the bit ends plus a beat, never mid-riff, and no joke is cut mid-flow.
- J-cut at every jump between moments: the next voice or game sound leads the picture by 0.2-0.5 s (0.25 s default on jumps > 2 s). A jump to another place or time (> 8-10 s of source) is never a bare hard cut: a dissolve, a line, or a real card with a true number.
- Never chop a sound with a cut. The one marked exception, at most once a video: cut a scream at onset + 80-200 ms, hard into the aftermath. Every cut gets a 10-30 ms audio crossfade.
- No fast-forward on menus, selecting or routine actions: jump-cut them. A sped montage keeps the game's real audio. Slow-mo only through real frames (never frame-blended or AI-interpolated, which warps fast motion and world text) and never on a boss kill.
- Bosses and big subjects: no intro or name cards, counters or celebrate cards unless the owner asks. Kills get, at real speed, 1-3 white flash frames + a decaying shake + a heavy hit, never confetti (confetti on a kill read as underwhelming).

### 1.5 Long-video structure
- The first 2 minutes are the densest part: ~20-30 visual changes in minute 1 (a pro reference: 29 cuts in minute 1, then 0-16 a minute, one 4-min shot uncut). Burst, then breathe; the 8-15 cuts/min body rate starts after it.
- The first 30 s is built, not trimmed: the cold open (the funniest real moment, <= 10 s) ends by 0:15, the promise starts by 0:30, the game's name is said by 0:30, no flat stretch. Minute one shows the core loop for viewers who never saw the game. Outcome bar: >= 50% still watching at 0:30 (a video at 27% is the failure case).
- Cold open -> promise -> 4-6 acts, each opened by a bridge -> turn -> payoff -> callback -> sign-off. A re-hook at least every ~4 min, something new at least every 90 s, talk >= 70% of runtime, at most one voiceless stretch over 5 s per 3 min. Every callback has its setup on screen earlier.
- No intro sting or branded intro: open cold on the best moment. The brand lives in the corner character, thumbnails and voice.
- Ending: the last real moment, then a motivated transition into the creator's own live sign-off within ~30 s. No recap montage of earlier lines (scored 3/10), no voice-sting stack, no produced outro. The ending never runs more than 3 LU over the video.
- The last 20 s carries the end screen: keep its element areas readable and point it at a live video.

### 1.6 Shorts and Reels structure
- Hook (piece 0, the strongest line pulled to the front) -> turn (25-75%, best ~45%) -> payoff (~55-80%, typically ~70%) -> end within 1.5 s. Never a straight slice of the long cut in its own order. One moment per Short, never a compilation.
- Something new by ~6 s and then at least every 6 s until the payoff; a gap over 6 s warns, over 10 s is refused; a stretch over 3.5 s with no cut and no caption is a sag. Measured Shorts held the hook ~4.5 s and lost about half by 10 s where nothing changed.
- Length 15-35 s, aim 20-30, never over 60 s on YouTube (a Short over 1 min with any Content ID claim is blocked worldwide). Within channel on 7,444 Shorts: < 20 s 1.16x, 20-35 s 1.11x, 35-45 s 0.97x, 45-60 s 0.91x, > 90 s 0.77x.
- YouTube ending: the last beat flows back into frame one so the replay is seamless (replays count as views; the 3 highest measured lifts all loop). Instagram ending: a hard stop on the most quotable, sendable line; a loop is a bonus.
- Claim -> test opener first: the speaker's confident claim over the thing, then the game's answer. One per video, posted first on both apps (3 of 5 such Reels left the first test pool at 21-39% skip; 0 of 5 others did; every Reel with skip >= 50% stalled at 110-183 views). Vary the other hook patterns (the game's own order, an absurd mechanic, a status flip, a big win then a fall) so no two Shorts look templated.
- Frame one and the vertical frame: `video.md` §3.

### 1.7 New devices
- Try a new device once, on a real-footage before/after (the same span with and without it), a full watch pass and a fresh reviewer, every row >= 8.5, before it enters real work. Pass = the reviewer calls the "after" better for that moment and never a gimmick.
- Picture devices: no black corner or edge shows, the move eases, an impact <= 2 frames, <= 3 flashes/s; world-locked layers drift <= 2% of the frame.
- Drop what fails and keep a warning on it. Dropped after the bar: a 2-frame ink impact frame (lost the subject on a busy canvas), AI-interpolated ramp and smooth slow-mo, stickers that sit behind or follow a subject.
- The owner's feedback on a clean first personal edit was "more chaotic, more in your face, more punch", with better sound design and transitions, plus screen spins and funny SFX for comedy. Clean is not the target; placed density is.

## 2. Motion graphics for video

### 2.1 Easing set (one grammar per video)
- No linear move except a real clock or a truly constant-speed thing. Entrances fast-in with a long settle (`power3.out`, or smootherstep `p^3(6p^2 - 15p + 10)`); exits mirror the entrance and run quicker (`power2.in` / `power3.in`); holds and pushes `sine.inOut`. All channels of one move share one curve.
- Typical eased move: in 0.15-0.25 s, settle 0.3-0.5 s, cubic S-curve.
- The same curves and durations for the same job across the whole video. But vary the LOOK of inserts (border, tilt, font, entry, slot, size): timing stays consistent, appearance varies (tell T3/J5, §8).

### 2.2 Frame timings
| Job | ms | @30 fps | @60 fps |
|---|---|---|---|
| Snap / punch-in | one frame | 1 f | 1 f |
| Impact flash | <= 33 | <= 1 f | <= 2 f |
| Hit-stop (scaled with impact) | 40-100 | 1-3 f | 3-6 f |
| Word slam in (accelerating INTO the hit, `power4.in`) | 117-133 | 4 f | 7-8 f |
| Exit | 167-200 | 5-6 f | 10-12 f |
| Character face change (drawn in-betweens) | ~130 | 4 f | 8 f |
| Character entrance | 233-333 | 7-10 f | 14-20 f |
| Micro reward | <= 300 | <= 9 f | <= 18 f |
| Push / pull | 500-1000 | 15-30 f | 30-60 f |
| Anything to be read, minimum hold | 500 | 15 f | 30 f |
| Overlap between elements of one graphic | 33-200 | 1-6 f | 2-12 f |

### 2.3 Overshoot by weight
- A solid character or object: <= 5% (`back.out` <= 1.2, or none). Text, cards, glints: <= 10% (`back.out` <= 1.7). Only a snap of <= 5 frames may reach ~16%.
- No elastic or bounce eases. A brand character's pop-in: easeOutBack <= 5%, uniform scale, a mirrored exit.

### 2.4 Shake
- Decays: biggest on the hit frame, two axes, alternating, gaps lengthening, settled to 0. A word settles in ~0.25 s, the screen in ~0.8 s. Never a constant-amplitude buzz.
- Word shake recipe: offsets as a fraction of a 10x6 px amplitude, [1, -0.5], [-0.7, 0.8], [0.4, -0.45], [-0.2, 0.15], [0, 0], with gaps of 30, 35, 45, 60, 75 ms.
- Celebration screen shake: rotation +-0.5 -> +-0.3 -> 0 deg, position +-5 -> +-3 -> 0 px, gaps doubling.
- Budget: only on real impacts (a hit, launch, crash, rage slam). About 1 per minute in a talk-led body; pro comedy edits measured 0.7-5/min where impacts justify it.

### 2.5 Anticipation, overlap, arcs, blur
- Anticipation (a 2-4 frame counter-move) only before a big hit, exit or spin, never on every move. The wind-up of a slam is its scale: start big and slam down, not scale up from zero.
- Elements of one graphic land 2-12 frames apart (the card, then the character ~11 frames later); nothing stops together.
- A slide-in carries a little rotation that settles (e.g. 14 deg -> 0); straight-line character slides read robotic.
- Motion blur on any move faster than ~10% of the frame per frame (snaps, whips, spins, fast pops), sub-frame samples averaged only while the move runs. Otherwise keep the move short enough not to strobe.

### 2.6 Recipes
- Key-word slam: scale 1.9 -> 1 and rotation -4 -> -2 deg over 0.12 s `power4.in`, a decaying shake, a 0.9 s `sine.inOut` breathe to 1.04 from 0.35 s, out to 0.6 over 0.12 s `power2.in` from 1.55 s (~1.67 s on screen; a snap exit, the one place an exit runs under 10 f at 60), silent (the camera and type carry emphasis), the speaker's own 1-4 words on a real peak line, at most ~1 a minute on live talk. In VO stretches, word by word (~0.4 s per spoken word), ~1.5-2/min.
- Spin transition, used ON a cut: ease-in 180 deg on the out-piece's end, ease-out 180 deg on the in-piece, so the cut frame rolls at its neighbours' speed. Scale the frame by a cover hull so no corner or edge shows (rises with the roll, holds ~2.08x through the cut, falls as it lands, no zoom pump). Average 48 sub-angles per frame for real rotational blur (8-16 left rings at the outer edge).
- Glitch / RGB split / signal drop 0.1-0.3 s, the game sound cut under it: only where the game or PC really froze or broke.

### 2.7 Characters and mascots
- Never squash, stretch or deform a brand character, in any medium. Weight comes from timing, overshoot and rotation: uniform scale, position, rotation and opacity only.
- Face and expression changes take ~0.13 s (~8 frames at 60) with real drawn in-betweens on ones (3 drawings at 1/24 s). Never a flip-book swap, an opacity crossfade, a morph, or two copies overlaid. States go anticipation -> overshoot -> settle; idle is never frozen (two periods, small random holds).
- Cue sync: the mouth moves only while the voice sounds (a voice gate); a face change lands ON its cue with in-betweens before it; no blink near a reaction.
- Reaction ladder: corner = default; mid (~33% width) = a clear laugh or shout; big (~50% width, full-body mid-screen) = the biggest moments; full screen at most twice a video. The face matches the speaker's real emotion, never a random reaction. Hidden during stings and cards, never over HUD or captions.

### 2.8 Flashes
At most 3 flashes in any 1 s, measured on whole-frame luma (ITU-R BT.1702, Ofcom 2.12 / Harding). No abrupt full-screen brightness jumps. Harding also limits saturated-red flashes and counts flashes over 25% of the screen; whole-frame luma is the simple stricter check.

## 3. Camera
- Zoom budget: outside hits and finds, at most 1 punch-in or push per ~20 s; the rest plays wide. No constant pushes. This beat the older "a zoom every 5-10 s" (over-edit backlash).
- A zoom never loses the subject: a boss stays whole in frame (a zoom that hid the fish: "you can't even see the fish"). The first shot of a zoom chain is a readable wide; close -> extreme close -> back to wide resets.
- Snap punch-in: a 1-frame jump 1.0 -> 2.0 (stepped to 2.5 on a second beat), held 0.5-1.5 s, cut back. Visible scale (>= 1.25x) or none: a 1.1x reframe nobody sees is cheap. A camera punch only with a hit on screen.
- A hit's visual partner: the game's hit + a 1-frame punch-in + a small decaying shake on the contact frame.
- Slow push 1.0 -> 1.2-1.3 eased across a tense build, a plan or a stare. Pull-out reveal 1.4 -> 1.0 over 0.5-1 s ease-out. Find zoom 1.6-2.0 onto the named item.
- Jump cuts inside one moment alternate framing 1.0 / 1.12.
- Letterbox slide 0 -> 15% eased over ~0.5 s on a real dramatic game moment, or as mock drama on a trivial standoff.
- 9:16 reframing camera: `video.md` §3.4.

## 4. Sound

### 4.1 Real, nameable sounds only
- Every added sound is a real, recognisable recording whose source you can name (real app tones, known meme audio, CC0 field foley, the creator's own voice). Cannot name its source = it does not ship.
- Banned: stock whooshes and sweeps, risers, choirs, sparkles, dramatic stings, record stop or scratch, sad trombones, buzzers, clown horns, crickets, synth UI pops and blips, chiptune, canned audience (laugh track, claps, gasps, cheers), long cinematic booms on jokes, announcer voices on deaths, overused meme sounds, cheesy game-show sounds. A birthday edit with stock SFX was called "AI as fuck"; with only real sounds left the same edit was "perfect".
- The creator's own recorded reaction stings (3 takes each, rotated) beat any stock meme sound: one per real reaction beat, never a montage.
- No TTS or AI voice where a human voice is expected. Instruments and reference tones are real samples, never synth stand-ins.

### 4.2 On its cue, on its frame
- Every added sound sits ON an on-screen cue chosen by hand (a motion, reveal, zoom, gag beat, the game's hit), named in the edit list as its cue. Nothing auto-placed on a cut or time skip. A spoken word is not a cue. (The fault in a bad mix was placement: 16 of 19 sounds sat on words.)
- A hit lands within +-1 frame (17 ms at 60 fps) of the contact frame read from the frame strip, never from word timing alone (83% of impacts had come from word timings). Hits run 0.15-0.5 s with the onset at sample 0. A whoosh PEAKS on its cue frame: offset late-onset files by their lead silence.
- Never one whose onset .. +0.25 s lands on a narration or VO word. Never two added sounds within 0.4 s (80-90 ms doubles read as mistakes): one moment, one sound; a punch-in, shake or flash adds the size. The one exception is a deliberate stack in a chaos edit: up to 3 onsets within 0.15 s, built as one layered hit (transient + body + bass tail), counts as 1.
- No sound on emphasis alone; slam text and camera carry emphasis silently. A word gets a sound only when it names an action happening on screen.
- No sound on a transition by default: a whip, spin, zoom-through or dissolve rides the music or the game's sound. A time skip gets a device (a card or a hard cut), not a whoosh on every jump.
- Purpose: a cut whoosh peaks <= 0.12 s on a big camera move, in a gap in the talk, >= 5 s from another whoosh; a cinematic build only on a title or reveal graphic (one that swelled 1.07 s after its cut read as random); a card sound only with a card.
- Intent matches the beat (win, fail, joke, punch, action, reveal, tension, move). Cheer and celebration sounds only on a real win, never on a correction, roast or fail. Sound undercuts the brag, never hypes it: the boom on the frame that disproves the claim, never a power-up on the brag.

### 4.3 Density and variety
- About 2-5 added sounds per minute in a talk-led body, <= 6 in any 60 s, mean <= 5/min; zero in a deadpan beat. A "chaos" edit caps at 24 in any 60 s and 18/min, a stack within 0.15 s counting as 1. Caps are ceilings, never targets. 8.2 hits/min is the ceiling to avoid.
- No file twice within 60 s; >= 4 variants per hit type; repeats of one file get a ±3-5% pitch and ±10% gain spread so they never read as a preset. A one-file rotation over 35%, one family >= 40%, one file >= 10 uses or a sound on >= 80% of cards = preset tell (T6, §8). A pro reference repeats 2-9%. Only a named running gag repeats.
- Asset hygiene: files normalised to -3 dBFS peak at 48 kHz, named `<tag>__<name>`, each with a stated purpose; CC BY files carry a credits line.

### 4.4 Levels
- A hit is audible at -6 to 0 dB vs the voice, or absent. Only the single biggest payoff goes over (+5 to +9 dB). Never a 0.2-gain whisper of a sound.
- Loud spikes ~3-6 per minute overall, clustered at bits (a pro reference ~4/min; a fix took ours from 13.2 to 4.3).

### 4.5 The game is the first sound effect
- Game bed -15 to -20 dB under the voice; physical moments peak -6 to 0 dB vs voice with the game's own sound. Dip the game per piece so its loudest 10% under talk sits 6 dB under the voice. A pro reference: ~80% of audible events are the game, bed -11.6 to -20.5 dB vs ours at -36.9 dB.
- Add a library sound only where the game is silent or weak.

### 4.6 Never silence
- A bed (music or room tone) under everything; nothing under -50 dBFS in the mix. The quietest 10% of seconds stays above about -24 LUFS outside marked beats, filled with game sound rather than a louder bed. (A video at -29.6 LUFS p10 vs references at -22 to -27 felt empty.)
- A deliberate dropout is a device, not silence: the whole mix cut to near-silence for 0.3-0.6 s right before a hit or after a death (pro comedy references do it 7-9 times a minute; ours did 4 and felt flat). Mark each one as a beat.

### 4.7 Music under voice
- Music is background: the bed sits 10 LU under speech level in gaps and 18 LU under while the voice talks (listeners prefer background 13-18 LU under speech, Fraunhofer QoMEX 2023). An outro bed sits at the 18 LU talk level.
- At 18 LU nobody hears a section change (an edit with 4 beds read as "one music" to the owner). When the music changes are part of the edit, dip ~13 LU while talking, or split the bed at 350 Hz and duck only the band above it the full depth, so the beat stays felt while the voice stays on top (a phone plays 400 Hz-8 kHz).
- Envelope from word times: down 0.4 s before the first word, held across gaps < 1.5 s, back up over 1 s, no pumping, with a 2.5 kHz dip for the voice. No transcript: a gentle 3:1 sidechain with 900 ms release.
- A bed per section that clearly changes with its mood, never one bed under the whole video. Music only to lift an emotion, never wall-to-wall under talk. Beds from more than one composer (one composer >= 60% of music time = tell T5). Beat-snapped montages cut every 2 beats (~1.2-1.3 s at ~95 BPM); off-beat spacing feels wrong.

### 4.8 Voice
- Check clarity at the source before editing: 2-6 kHz consonant energy vs the 100 Hz-1 kHz body over the talk (one voice's working floor was about -15 dB; a cut 6 dB under a clear reference read "not understandable"). Fix muddiness at recording, not with post EQ.
- Never stack AI denoise, pitch correction or extra EQ on an already-processed voice (a voice changer or heavy chain): it goes robotic. Clean lightly.
- Voice FX on one line, 1-2 per video, as a comic beat, never as cleanup: echo (260/520 ms taps), radio (highpass 420 Hz, lowpass 3.2 kHz, bitcrush 10), deep (pitch 0.62), chipmunk (pitch 1.6), mock-epic (short echo + bass +5 dB at 110 Hz).

## 5. Captions and bleeps
- Captions are the speaker's exact words as spoken, proofread by a second ear (two ASR passes; every line they disagree on is resolved) before every render. A misheard caption is worse than none: hide an unclear fragment, never guess; the speaker's own correction beats the transcriber.
- Uploaded caption track: <= 22 characters per second, 2 lines x 42 characters, each event 0.83-7 s, WER <= 5% (Netflix timed-text guides; FCC 47 CFR 79.1). Upload the native-language track for every long video.
- Look, size, timing and placement: `video.md` §4.
- Bleeps: strong slurs bleeped by default, comedic in long videos, always in Shorts, unless the owner says "no bleeps" (log it). Swearing is fine in the video, never in titles or thumbnails; avoid wall-to-wall strong profanity.
- A bleep sits INSIDE the swear's own word timestamps, widened to the word's true start (often ~0.15 s before the caption word). Running 20 ms into a neighbour means that word gets starred too. The tone's level = the voice as heard in that piece, never one file-wide level. Skip phone-band checks within 0.05 s of a bleep.
- Captions star the bleeped word. A swear is shown and bleeped at the severity spoken, never silently softened.

## 6. Film look

### 6.1 Beat looks (one per beat, never stacked, ~1 per 2 min)
| Look | Recipe | Beat |
|---|---|---|
| dramatic | B&W + reverb | realisation, a dead joke, a death |
| intense | contrast 1.25, sat 1.1, cool shift, 10% letterbox + push | a tense build |
| epic | contrast 1.15, sat 1.3, vignette PI/5 | the big win |
| deepfried | contrast 1.7, sat 3.2, unsharp, noise 14 + clipped-bass audio | a scream or rage peak, max 1 per ~3 min |
| glam | 50% screen-blended bloom + warm + vignette | a mock compliment |

### 6.2 Story films ("edited, not cut")
- A per-scene grade (contrast, saturation, gamma, balance, vignette, grain) that follows the game's time of day and weather: nights cooler and darker; a near-black shot gets gamma 1.08-1.15 rather than being cut.
- 2.39 letterbox. A 1 s dissolve at day changes instead of a fade to black.
- No synthetic zoom, push, snap, whip, shake or tilt (crop <= 1.3x only to hide HUD); no slow-mo or freezes (every frame a real frame); no stills; camera moves are only the game's own. A film with "rough zoom, rough camera, just cuts and bars" scored 3.5/10.
- Bare cuts under 60%; every cut has a written reason; cut on motion; match cuts on repeated framings. Sound carried across every scene change (J/L cut or a shared bed). No uncut cutscene over 30 s.
- Breath holds 0.3-1.5 times a minute where the VO stops for 8-14 s (a reference's biggest replay peaks were exactly these). No static wide over 2 s: a living window = median shift >= 0.45 px/frame at 480 px wide, or median frame diff >= 3.0. Pro trailers measured 0% static holds.
- VO rhythm: 125-165 words per minute of runtime, sentence median 8-11 words, a "but" turn more than once a minute. VO slot = 0.5 s lead (0.3 on a hard cut) + the read + 0.5-0.8 s tail of real picture.
- Films feel grand: grade, bars, wide holds, the live voice under game and music; a brand mascot stays out of the film body.
- LUTs: only your own baked LUTs (an S-curve with toe, highlight shoulder and roll-off, split tone), never stock, each A/B'd on its footage first (a "film" LUT crushed night shadows from 43.7% to 45.5%, so that film kept a plain EQ grade). Bake them with video-edit `scripts/lut.py` (film, film_night, warm_day).
- Personal edits: punchy grade, light grain and glow are fine.

## 7. Video QC (before any review ask)

| Check | Pass |
|---|---|
| Black picture | none longer than 1 s (except the last 15 s of an outro) |
| Frozen picture | none longer than 3 s; a deliberate hold stays short |
| Integrated loudness | -14 LUFS +-1 (ITU-R BS.1770) |
| True peak | <= -1.0 dBTP |
| Click at a cut | no peak more than 6x the level around it, at any cut |
| Holes at cuts | +-15 ms under 50% of the surrounding level at <= max(1, 10%) of cuts |
| Silence | nothing under -50 dBFS in the mix; p10 seconds above ~-24 LUFS outside marked beats |
| Voice on a phone speaker | through a 400 Hz-8 kHz band the voice sits under the rest of the mix <= 2% of talk time and <= 25% in any 10 s window |
| A/V sync | within +40 / -60 ms (EBU R37), house bar 1 frame, checked by a flash/beep test; streams end within 2 frames of each other |
| Flashes | <= 3 in any 1 s (§2.8) |
| Captions | <= 22 cps, 2 x 42, 0.83-7 s per event, WER <= 5% |
| Identity | identifying names and details in frame redacted (`video.md` §5.5), OCR proves it |
- The phone-speaker row is the most direct measure of "the voice is on top": a draft that passed an older 10% rule at 2.2% still sounded low to the owner; the fix measured 1.3% with the worst 10 s at 17.2%.
- Decode every file and check duration and sample rate before sending it (a mixed 48/192 kHz A/B wasted a review). Watch the whole render, picture and sound (`video.md` §6.7).
- Per-app check on every vertical render: size, fps, length, loudness, words in frame one, structure beats, character and text vs that app's bands, cover size and luma, last word not clipped, a Reel not ending mid-sentence, game text not hidden under a band or our caption. FAIL = re-render; every WARN gets an answer before the blind review. Text detectors that look for one caption style miss light text without an outline and anything on screen under 0.5 s.

Master specs:
- Long video: 1440p master (720p previews only while testing), x264 slow CRF 16; at least 1440 tall unless deliberately low-res.
- Vertical: 1080x1920, 60 fps, H.264, AAC 48 kHz, faststart (moov first), -14 LUFS, true peak <= -1 dBTP. Instagram accepts H.264/HEVC, 23-60 fps, VBR up to 25 Mbps, up to 300 MB, and recommends only >= 30 fps and >= 720p.
- Personal edits: a 1440p60 big-screen master (4K for a TV), a 1080p copy and a phone copy under 20 MB. Review = a fresh blind review plus separate design and sound reviews, every row >= 8.5.
- Nothing reaches the owner until it is final: the whole package at once (the long, every Short and Reel, the 3 title + thumbnail pairs), each file through QC. Any re-render after the owner's OK voids the OK; they watch the new file.

## 8. Video slop tells

### 8.1 On-screen devices that read AI-made
- Emoji stickers or pops, a persistent HUD / meter / counter / tally, sticker-framed meme cards, word cards that echo the line just said, inserts parked in one slot, a device after every line, identical stings on every beat, an added hook-text bar, editor labels that explain the joke or describe the edit ("BEFORE/AFTER", "LESSON COMPLETE"). Any of these needs an explicit ask.
- A blind review of one cut found 32 emoji pops, 49 of 59 cards echoing at 11/min and a corner meter: "this looks AI slop".

### 8.2 Template tells (counted)
| # | Tell | HIT when |
|---|---|---|
| T1 | Emoji / sticker pops | 3+ overlays that are stickers or emoji (the brand mascot exempt) |
| T2 | Persistent HUD / meter / counter | one image family on screen >= 50% of runtime |
| T3 | One fixed slot | an overlay position + size used 8+ times, or by >= 50% of overlays (with >= 4 uses); a character alternating between two slots still hits |
| T4 | Echo cards | a card is an echo when >= 60% of its tokens are in the speaker's transcript; HIT = echoes >= 50% of cards AND >= 6 cards/min. A source tag does not hide an echo |
| T5 | One stock composer | one composer >= 60% of music time while music runs > 30% of runtime |
| T6 | SFX preset | with >= 20 sounds, one category >= 40% or one file >= 10 uses; or with >= 6 cards, a sound on >= 80% of cards (ambience and beds not counted) |
| T7 | Metronome | with >= 10 line ends (a gap >= 0.6 s after a line), an added device within -0.1 to +0.6 s of more than 40% of them |
T1, T2 and T4 block a long cut; T3, T5, T6 and T7 warn and need an answer.

### 8.3 Judged tells (reviewer's own frames)
Score each 0 = absent, 1 = once or twice and motivated, 2 = a pattern (3+, the same asset, slot or sound reused, or unmotivated):
- J1 a meme not about THIS picture or line
- J2 an effect no moment asked for (sprinkled, not placed)
- J3 one device as a metronome (the next one is predictable)
- J4 preset transitions (glitch, RGB, flash used as glue)
- J5 one visual language for every insert (same border, tilt, font, entry)
- J6 the edit labels or explains the joke instead of building it
- J7 anything a stranger would call AI-made at first glance (name it)

AI-feel cap from P = the number of tells scored 2: P = 0 no cap; 1-2 caps the score at 7; 3-5 at 6; 6+ at 5. With the cap, two fresh reviewers gave gated 4 and 5 to a cut the owner rated 5, where the plain 39-row mean had read 8.29.

### 8.4 Premium vs cheap
| Premium | Cheap |
|---|---|
| lands on the frame of the hit or word (frame-checked) | near-the-beat placement |
| eased motion with blur and overshoot-settle | linear moves, preset zoom-and-bounce |
| a layered sound (transient + body + bass tail) levelled under the voice | one stock boom at full level |
| one visual language per video, varied inserts | mixed fonts, or one template for every insert |
| silence and contrast before the hit | a constant wall of sound |
| visible scale (>= 1.25x snap) | 1.1x reframes nobody sees |

### 8.5 Words a person would say
- Written lines (VO scripts, bits) are grounded in the speaker's own corpus: word pairs >= 25% the speaker's own (rejected scripts scored 0.15-0.21, the speaker's own re-read 0.47); no bookish words the speaker would say in English; every line tagged with its source (transcript timestamp, game file, or what the story bends).
- A laugh-judge pass is not a voice pass. Drop voice judges who cannot tell the speaker's real lines from rejected ones.
- If a line or effect could be in anyone's video, cut it. Unsure = cut.

### 8.6 Public text around a video (titles, descriptions, captions, posts)
Adds to tells.md's buzzword and contrast-cadence bans:
- Error: ultimate, epic, insane, must-watch, must see, unmissable, don't miss, smash that, hit the bell, like and subscribe, don't forget to, buckle up, get ready, you won't believe, dive in / let's dive, in this video, join me, journey, unleash, next level, elevate, level up your, stay tuned, without further ado, jaw-dropping, mind-blowing, hilarious, legendary, iconic, roller coaster, vibes only, masterpiece, you'll love, seamless(ly), in the world of. Match case-insensitively with curly apostrophes normalised.
- Warn (some are real game names): deep dive, crucial, pivotal, vibrant, showcase, underscore, intricate, meticulous, garner, additionally, interplay, enduring, breathtaking, renowned, nestled, "i hope this helps", "great question", "let me know if", "certainly!".
- No em dash, en dash or " -- " in any public string, titles included. Verbatim third-party lines (licence credits, publisher notices) are exempt.
- Shape: no bullet or emoji-bullet lines; <= 2 emoji; <= 5 hashtags; warn on "!!" or more than 2 "!"; warn when > 25% of words are Capitalised. Length caps: caption 300, post 280, description 900, channel about 250, comment 200 characters.

### 8.7 Platform AI processing
Off by default: auto translation and AI dubbing on Reels, YouTube's AI visual enhancement and Stable Volume. They make an AI copy of the voice or alter the picture and the mix after QC.
