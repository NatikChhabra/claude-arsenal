---
name: guitar-capture
description: >-
  Record and prepare the owner's guitar parts (DI or mic, to a click) so they can drive the song: a clean take, a beat
  and bar map, a chord chart and an optional MIDI sketch, plus the tone chain. Use when he has a riff, a progression or
  a full guitar part, for "record my guitar", "turn this riff into a song", or a take that drifts off tempo.
---

# guitar-capture

status: draft (full workflow; beat map tool tested; promote to beta after the first real take)

Sources and licences: research/04_production_and_video.md §2. The guitar is his voice in every song: it stays audible
and central.

## 0. Level check, then one play sheet
Write parts for the player he is, measured, not guessed. A first draft pitched by guesswork was called "sub par"; he
asked: "ask me more questions rather than guessing".
- Ask, a few words each: how long he has played; barre chords (can he switch to them in time?); thumb on the bass while
  fingers pick on top (Travis style); harmonics; notes past fret 5; thumb slap and chuck; can he play 3 minutes without
  stopping; pick or fingers; how long he will practise. Ask the feel too: what the ending should feel like and 1-2
  reference songs.
- Ask for about a minute of songs he already plays, then measure it:
  `uv run --with librosa --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/guitar_level.py <take.wav>`
  (tuning, clipping, notes per second, steadiness, picked vs strummed, range, hesitations, per stretch of playing).
  Write the part at about 60-70% of his best clean notes/s. Tell him to tune if it reads more than 10 cents off and to
  move the mic back if anything clipped.
- Sound big with moves a 2-4 month player can do, on the chord shapes he already knows (no barre chords): natural
  harmonics 12 frets above the capo for an intro; the hook as a single-string tune with hammer-ons and pull-offs;
  thumb on every beat with a pinch on 1 and a hammer-on inside each chord; palm-muted builds; chucks on 2 and 4;
  one bar of dead silence before the last chorus; a thumb slap (kick) plus chuck (snare) groove for the last chorus.
  For an ending that lifts, finish on the relative major (from Em-shape home to the G shape), not the home minor chord.
- Write every move as real 6-line tab (thin string on top, frets from the capo, counts under each bar, h/p, x for a
  chuck, <12> for a harmonic, T/i/m/r for fingers), not as named moves with a symbol key: he could not follow
  "TUNE / BELL / PICK / MUTE / STOP" boxes and asked for tabs. Check each tab note against the chord under it.
- Deliver ONE sheet, never several: chord diagrams with finger numbers (mark the bass string and the hammer finger),
  the tab of each move with a tick box, in the order they come, then the song top to bottom (one row per section,
  one coloured box per bar, the move and a feel word), then a short record checklist (take names). Add a slower
  practice play-along (about 20 BPM under) next to the real one, both in one clean FINAL folder.
- Layout that worked after three rejected ones: one card per section in play order, each holding its own tab, chord
  names over the bars, a feel word, the repeat count (x2) and one line of how. A key of moves plus a separate song map
  made him jump around ("garbled, disorganized"), and engraved notation with rhythm stems was unreadable to him. Build
  it as HTML (inline SVG tab, chord diagrams, a numbered strip of all sections) and render to PNG and PDF with
  Playwright; follow the design plugin for type and colour (his own tools default dark).
- Before sending: play the tab back as plain plucked notes over the click (Karplus-Strong in numpy, no samples) and
  check every row lands on its bar, the drop is silent and the last chorus is loudest; send that render as a slow
  "how the tab goes" guide. After copying to his PC, read the file back from the PC and compare pixels: a copy sent
  in the same batch as the write once delivered the old sheet ("it's the same").

## 1. Record
- **Record once, loop the rest** when he would rather play each part one time ("I just want to play one time and
  you repeat that"). Every sound stays his own playing; only the copying is done for him.
  - Sheet: one card per distinct part (4 bars each, all bars written out, no repeat counts), in record order, plus a
    strip of the song showing which part plays where ("5+2" = part 5 with the melody part on top).
  - One record track for all parts in card order: 8 count-in clicks, the part's 4 bars with the click, 2 bars of rest
    to let it ring. Print each part's start time on the sheet so one part can be redone alone. The click goes in his
    earphones only: a click caught by the mic gets looped with the part.
  - Reuse the parts for everything else. Repeats of verses and choruses come straight from them. The melody part is
    layered over later choruses and a bridge. A silent drop is just an empty bar. An ending can be single bars sliced
    from a part (rolled chords, the last bell bar of the intro). A part's last bar keeps its recorded ring, so pick the
    slice that ends a part to ring out.
  - Build: `python ${CLAUDE_SKILL_DIR}/../../tools/loop_assemble.py plan.json song.wav` (finds each part and each bar,
    crossfades 25 ms before each downbeat, keeps his feel inside the bar). It fails on a weak match, more than 0.5% drift,
    clipping or a quiet take: re-record that part, don't edit it. Set section loudness per part toward targets
    (the last chorus loudest), then pan the melody layer off-centre, add a short room, glue, and limit to the
    streaming target, with an encode check as in mix-master.
  - Before he records, test the whole plan on a Karplus-Strong render of the record track with human timing (latency,
    0.2% slow, 6 ms jitter). Check that every bar lands within 20 ms of the grid, that loop joins have no gaps, that
    the drop bar is silent, and that the times printed on the sheet match the track.
  - Then stress it before trusting it: late and early starts, a player 0.4-0.8% fast or slow, 15 ms sloppiness,
    noise, 50 Hz hum, quiet, clipped, one dead channel, 48 kHz, click in the mic, a missing part, the wrong part,
    missed notes, one bar 90 ms late, and one part redone in its own file, plus random mixes of these. Each case must
    pass clean or be caught with the right fix. The first run caught real bugs: on a whole take, a 0.4% tempo error
    let parts slip by an eighth note (now one offset and one tempo for the whole take), and a roll bar locked onto a
    later string.
  - Check the guide synth too: plain Karplus-Strong with an integer delay was up to 36 cents sharp on high notes,
    and white-noise excitation made it far brighter than a real acoustic (compare long-term spectra with his own
    take). Resample to the exact pitch, low-pass the excitation, and add a body resonance.
  - Slice an ending from contiguous bars of one part (C, G, D straight through) so the ring is never cut mid-part.
    Set section loudness after mastering and correct it in a loop until each section is within 0.75 LU of its target.
  - **When the takes don't follow the click** (first real use, 8 Nov 2026: one file per part, free tempo, the verse
    at about 6 s a bar with long pauses, the bells and chugs faster than the click), `loop_assemble.py` can't lock on.
    Don't stretch whole takes 2-6x and don't ask for a re-record he has ruled out. Re-play the part hit by hit from
    his own take instead:
    - Find each tab event in his take: onsets with a CQT "new energy" vector (after minus before), matched in order to
      the tab's expected notes (sounding pitch = open string + capo + fret). Check every match by the new
      pitches it adds, not by onset strength.
    - Cut each hit from its attack (8 ms pre-roll) to his next real hit, and place it on the grid. Let it ring until the
      same string is played again or the chord changes; later slices carry the ring of earlier strings, so let-ring
      parts stay continuous. Only when his next hit came sooner than the grid needs, lengthen that one slice with
      Rubber Band R3 (`rubberband -3 -t`, at most 2.5x). Palm-muted chugs never stretch: they just decay.
    - For a strum, the next hit is the next strum, not the next string inside the roll: onset detectors fire on every
      string, which cuts strums to 50 ms. List the strums by hand once, from a spectrogram.
    - A wrong or missing note becomes the same note from another bar of his (same string and fret); a missing
      thumb bass can come from the verse's thumb notes. Where he played a different chord than the tab (Em7 for
      Cadd9, a finger on fret 2 not 3), keep his chord if it is consonant, and say so.
    - Strum parts: render two different hit orders for a left/right double (wide, real). Render the chucks alone as
      a percussion stem (thump around 95 Hz, crack around 3.2 kHz, first spike clipped about 7 dB).
  - **Soundhole pickup takes** (magnetic, into the PC): band levels fell about 12 dB per octave above 300 Hz, and
    everything above 5 kHz was hiss (signal-to-noise 2-6 dB there, 13-25 dB at 2.5-5 kHz). Low-pass at 5.2 kHz,
    expand only the band above 1.5 kHz in quiet passages, boost 1.7 to 4 kHz (up to +12 dB), and make the air with
    an exciter (saturate the 1.8-5 kHz band, keep only what lands above 5.2 kHz). Compare band levels with a
    bright acoustic target until each band is within about 5 dB. The Windows input soft-clipped the loudest chucks
    at about 0.98: spline them back before use.
    Keep the crunch, lose the grit: on the first master the owner said "very good but too crunchy, pinching in
    the ear" at 2:00 to 2:30. The cause was not overall brightness but grit: sample-to-sample jumps over 0.35 (at a
    -3.5 dB ceiling) from the rectified part of the exciter and from the chucks, 311 per 10 s at the spot he named
    and 51 at the chorus he liked. The fix that kept his "crunch" was half the rectified part (0.3 of abs(band),
    not 0.6), a broad presence peak (+11 dB at 2.9 kHz, Q 0.7, not +12 at 2.7 kHz, Q 0.9), chucks EQ'd at +2 dB
    near 3 kHz with a 4.5 kHz low-pass, and a fast look-ahead limiter on the chuck stem in place of a clipper. Count
    the jumps per 10 s on every master (aim for single digits) and ask him which timestamp sounds best, then match
    that passage's band levels within about 2 dB up to 4.5 kHz.
    Hiss gates chatter on long rings: the above-1.5 kHz expander that cleans the quiet verse made a buzz on the
    bridge's long, quiet ringing strums (the owner heard "strings buzzing" in the middle; the raw take was clean). Leave
    the expander off on parts whose raw take has a quiet floor, or slow its release well past 50 ms.
    Make the air harmonic, not noisy. An exciter of `tanh(band) + 0.45*abs(band)` on the 2-5 kHz band gave air above
    5.5 kHz with a spectral flatness of 0.15-0.35 (noise-like; the dry notes measure 0.02-0.035). The owner heard it
    as a slight "fizzy" sound on the opening bells on earbuds, less on the phone speaker. A square law on the band over
    its own 10 ms RMS envelope (`band**2 / env`), high-passed 8th order at 6 kHz and level-matched to the old air, keeps
    the same brightness at a flatness of about 0.06-0.09. A 4th-order 5.5 kHz high-pass let its sum tones leak into
    3-5.5 kHz and raised the floor there by about 2 dB, so use the steep one. Never use `abs()` (a corner at zero)
    in an exciter: it makes high-order products, heard as fizz or grit.
    Three more things the square law needs (found by an independent check before the final, not by the build's gates):
    the 10 ms boxcar envelope lags every pick attack, so `band**2 / env` jumps for a few ms and made 144 short air
    ticks in one master (a 2 ms burst above 5 kHz within 10 dB of the 300 Hz-3 kHz body; the old exciter had 55).
    Normalise by a peak-held envelope instead (1 ms RMS, 12 ms running max, 4 ms mean, times 1.41), cap the air at
    4 dB over its own 40 ms RMS, and level-match it to the old air in 5.5-8 kHz minus 2 dB: 0 ticks in the whole song.
    Gate the air off in quiet ring tails (a ramp from 30 to 20 dB under the part's 95th-percentile band level, which
    touches about 20% of frames and 0.01 dB of energy): air made from a tail's hiss is hiss. The square law alone
    leaves almost nothing above 10 kHz (about 17 dB under the old air at 10 kHz), which darkens a part the owner
    loves; add a third-harmonic layer (Chebyshev `4u**3 - 3u` on the band over the same envelope) high-passed 8th
    order at 10 kHz, 12 dB under the old air's 10-14 kHz level. With that layer at 8 kHz the 6-10 kHz flatness rose
    from 0.04 to 0.14; at 10 kHz it stayed near 0.1 (the old air: 0.24 there and 0.38 above 10 kHz).
  - **Retime only with slices, never with a time map on bells or harmonics.** Rubber Band's `-M` key-frame map (to
    keep each attack 1:1 while stretching the ring) made faint second attacks on the bell notes the owner loved
    (onset strength 0.41 against 0.14). Check every source hit's tuning before placing it: two up-strums rang an E4
    about 57 cents flat; swap in the same strum from another bar and keep the left and right doubles different.
  - **A drum kit from his own guitar, when he will record a little more** (9 Nov 2026, through the same soundhole
    pickup, about a minute of single hits): fist thumps on the body for the kick, palm slaps on muted strings for
    the snare body, and his existing chucks for the crack and the hi-hat ticks.
    - Pick hits by sound, not by count: kick = most energy under 150 Hz (over half the spectrum), no clipping;
      snare = a clean slap whose strings ring at least 40 dB down after 120 ms.
    - Cut each hit short (kick about 0.1 s decay, snare 0.07 s, tick 0.02 s): his strings ring through the pickup in
      standard tuning (A, B, D, E) under a capo-2 song, and a short envelope keeps that out of the key.
    - Every hit gets a 1 to 2 ms fade-in. Without it the ticks were near-clicks (sample step 0.64 of their peak) and
      the master's sharp-jump count went from 22 to 191, the same grit that pinched his ear on the first master.
    - Play it like a person: a light swing on the off-beat eighths (about 22 ms at 90 BPM), the snare about 7 ms
      late, 4 to 5 ms random spread, a kick pattern that changes bar to bar, ghost notes now and then. He hates music
      that sounds AI-made, so no grid-perfect drums.
    - Where the kit plays, pull his chucks back about 4 dB: they land on 2 and 4 with the snare and double the peak.
    - Round the hits with a soft tanh set about 10 dB over the kit's own 2 s level (not a fixed level: a fixed one
      crushed the loud chorus and left the quiet bridge spiky).
    - Hi-hat ticks cut from his chucks carried the chucks' 2-8 kHz rattle on every eighth note and added to a
      "buzz" the owner heard. His finger taps on the body (high-passed at 600 Hz, low-passed at 7 kHz) give a soft tick
      without it. Pick each hit at random with no immediate repeat, from a random stream of its own, so the kit's
      timing and velocity stay as they were when only the hit choice changes.
  - **Chorus strums that buzz: re-take and score, don't EQ.** A rattle the owner called "crunchy, gives me a
    headache" came from chucked strums (slap-mutes rattling the strings). EQ, de-essing and notches did not remove it.
    Ask for brushed strums of each chord, many takes, then score every phrase by its between-harmonic noise: the
    median level in 1.5-6 kHz between the chord's partials, against the take's hiss floor. Over 3 dB is rattle; hard
    strums scored 5-9 dB, his clean brushed phrases 0.5 or less. Also check each phrase's chord-tone share (0.85 or
    more of the chroma), its tuning (drop phrases 9 cents or more off the rest) and cut it before any slap at its end.
  - **Free-time strum phrases onto the grid.** He strummed the re-takes freely (stroke spacing 75-107 BPM), so a
    phrase dropped whole onto a 90 BPM half bar drifted up to 120 ms behind the snare by its end. Cut each phrase at
    the quiet point just before its first stroke (the last 1 ms envelope minimum within 15 ms before the rise), find
    the stroke nearest beat 2 (the steepest rise of the 1 ms log envelope, not a threshold crossing, which locked
    onto the previous stroke's ring 86% of the time), and stretch the whole phrase once with Rubber Band R3 so that
    stroke lands on beat 2 (ratio 0.82-1.22). His timing inside the phrase stays his. Splitting the phrase into two
    separately stretched pieces made a 4 dB dip at the join: stretch it in one piece unless it ends early.
  - **Never copy a chorus.** He hated a second chorus that repeated the first. Assign phrases slot by slot (bar, half
    bar, left or right) with hard rules: the two sides never play the same phrase, no slot repeats the slot four bars
    back or the half bar just before on the same side, phrases used in an earlier chorus come last, and at least one
    side rings past the next half bar (two short phrases together left 100-300 ms holes). Cut the outgoing phrase 3 ms
    before any stroke of its own that lands in the 70 ms before the next on-grid strum (it flammed). Put the long
    phrase on a random side, or one side always carries the same few long phrases.
  - **Hit-by-hit parts need a player's feel.** Every note of the opening had been placed exactly on the eighth grid,
    with levels pulled 60% toward one target, and one A-note recording played four times in each melody pass: the
    owner heard it as "a little robotic". Render each placement of a part as its own variant: a slow push and pull
    (about 6 ms over 16 beats plus 3 ms over 6.5), 4-5 ms random spread, a light off-beat lilt (5 ms late) except on
    quick bell runs (3 ms early), an accent shape (beat 1 up, off-beats down, a phrase arch), level pull 40%, and
    rotate repeated notes through his other takes of the same pitch (within 30 cents).
    Give every part the same push-and-pull curve (one player), with only its own small spread on top (3 ms, clipped
    at 7 ms): separate curves let the melody and the bells drift apart. Rotate held notes only through his long
    takes of that note and short notes only through his short ones: a short take on a held note was stretched 2.4x
    and dropped out. Ease the last two notes of each pass back toward the grid, keep each pass's first note on the
    downbeat, and match each variant's K-weighted level to the original stem (the variants came out 0.2-0.7 dB hot).
- DI through an audio interface, 48 kHz / 24-bit, peaks around -12 to -6 dBFS (room for transients). A phone memo is
  fine for an idea, never for the release take.
- To a click at the SONG.md BPM whenever the part will be produced or the video cut to it. Free time only for a
  rubato intro, marked as such.
- Record 3+ full takes plus punch-ins per section; keep every raw file untouched in `songs/<slug>/guitar/raw/`.
- Give him a play-along, not only a click: click, a soft low note on each chord's root (so he hears every change), a
  bell at each new section, and his own vocal placed where it will sit. A bar chart (bars, chords, how hard to play)
  goes with it. Ask for the parts a beginner can play: the whole song once through (twice), a riff of the hook tune on
  2-3 strings with one finger, and body taps on the guitar (palm on the side = kick on 1 and 3, knuckles on the top =
  snare on 2 and 4) so even the drums are his guitar. He asked for this himself: "it should feel my own".

## 2. Map it
`uv run --with librosa --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/beatmap.py map <take.wav> --click <check.wav>`
- Prints tempo, beats, bars, sections; writes `<take>.beatmap.json`. Listen to the click file: the high click must sit on
  "one". Low downbeat confidence (< 0.05) = trust the beats, set bar lines by ear.
- A take that drifts more than a few BPM across the song: re-record to the click, or tempo-map the DAW to the take
  (a deliberate live feel), never both.
- Better downbeats: Beat This! (CPJKU, MIT code and weights, beats and downbeats, state of the art) is the upgrade
  path once it is installed on his PC (registry: TRIAL); madmom's models are non-commercial, never on released work.

## 3. Chords and notes
- He knows what he played: write the chord chart from him first (fast, exact).
- Spotify Basic Pitch (Apache-2.0; `basic-pitch <out-dir> <take.wav>`) gives a MIDI sketch: 79.0 onset F-measure on
  GuitarSet vs 91.2 for the best research model, so always clean it by hand. MIDI only, no tab.
- Tab export: Klangio Guitar2Tabs (commercial; Guitar Pro / MusicXML) when tab is the deliverable. No open audio-to-tab
  model is ready to use (2 Nov 2026).
- Put the chord chart in SONG.md, bar by bar.

## 4. Tone
- Neural Amp Modeler (MIT, VST3 on Windows) or the free TONE3000 plugin (launched 1 Sep 2026, 700,000+ captures, loads
  NAM captures and IRs) into a cab IR. If NAM crashes before its window opens, set it (or the DAW) to the dedicated GPU.
- Match the reference songs' tone by ear and by A/B at equal loudness, never by "louder sounds better".
- Commit the tone only at mix time: keep the DI so the tone can change.

## 5. Hand-off
Clean comp of the take (edits on the grid, crossfades, no clicks), DI and amped versions, beat map JSON, chord chart.
SONG.md Status: "guitar recorded"; next: song-from-idea (if lyrics are open) or produce-arrange.
