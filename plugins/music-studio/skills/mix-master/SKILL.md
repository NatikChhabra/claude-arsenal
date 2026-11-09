---
name: mix-master
description: >-
  Mix the vocal and instrument stems and master the song for streaming, video and in-game playback, gated by measured
  loudness, true peak, the encoded-file check and the phone-speaker vocal check, with the numbers written down. Use when
  stems are ready, for "mix this", "master my song", "it's too quiet", or a vocal that gets lost on a phone.
---

# mix-master

status: draft (full workflow; loudness tool tested; promote to beta after the first real master)

Targets, commands and sources: [references/targets.md](references/targets.md). Video-side levels (music under
voice, film loudness) live in the design skill, references/edit.md §4 and §7: this skill owns the song itself.

## 1. Prepare
- Check every raw take first: a mono mic on a stereo input often leaves one channel silent (a home take on 8 Nov 2026
  had its right channel 45 dB down). Fold such a take to mono from the live channel before any processing, or the
  part plays from one side only. Also check peak level per take: a take whose peaks sit near -24 dBFS needs more input
  gain next time, not more makeup gain now (the noise comes up with it).
- Import every stem at unity, same start. Name tracks by part. Session notes start `songs/<slug>/MIX.md`.
- Pick 1-2 reference tracks from SONG.md; level-match them to the mix before every comparison (louder always sounds
  better to the ear, so unmatched A/B is meaningless).

## 2. Mix (in order; save a version after each)
1. Static balance with faders only, vocal first: the lead sits on top, the guitar right under it (his instrument is
   central), drums and bass glued under both.
2. Subtractive EQ for space: high-pass everything that isn't bass or kick; carve 1-4 kHz in dense parts where the
   vocal sings.
3. Vocal chain: clean (no stacking of denoise on an already processed or converted voice: it goes robotic), EQ,
   de-ess, compression in two gentle stages, short plate or room plus a tempo-synced delay on sends.
4. Glue: drum bus compression light; parallel compression only when the reference asks for it.
5. Automation: ride the vocal so every word is heard; lift the last chorus.
6. Lifts into a chorus (an owner called the first try "underwhelming"): the build must end under the chorus, not
   at it. Hold the build's last bar about 1.5 dB under the chorus average, open a low-pass over its four bars, cut
   to silence for the last half beat, keep a reverse swell's peak a few dB under the chorus (a swell louder than the
   downbeat steals the hit), and land a short low thump plus a reverb burst on the downbeat. Measure K-weighted
   loudness in half-second steps across the join: aim for the downbeat 2 to 4 dB over the build's peaks, more after
   a drop.

## 3. Gate the mix
`python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <mix.wav> --vocal <lead.wav> --inst <instrumental.wav>`
- Phone-speaker check: vocal buried in at most 10% of sung windows (400 Hz-8 kHz is what a phone plays). Over that =
  more vocal level or less instrument in that band, then re-measure.
- Harshness check: count sample-to-sample jumps over 0.35 per 10 s window (scale the threshold with loudness) and
  compare 2-6.5 kHz band levels with the passage the owner likes best. Grit (the jumps) is what pinches the ear;
  a dynamic 2-6 kHz cut should only act when the band jumps above its own running level (threshold +4 dB over a
  0.4 s average). At a threshold below that level it cut 3 to 4 dB all the time and dulled the whole track.
- A spot the owner calls painful: compare its K-weighted loudness with the passage he likes before touching the
  tone. On one master the pain at 1:40 was the second chorus sitting 1.2 LU over the first (same strum, same
  spectrum); two independent checks refuted a 3 kHz dip, and 1.5 dB less level fixed it.
- A middle that "makes you sleepy": count onsets per bar and K-weighted loudness per bar. A stretch of one or two
  onsets a bar with no pulse for 20 s, right after two near-identical choruses, was exactly where the owner said it
  dragged. A groove from his own body taps fixed it (see guitar-capture).
- Long-kernel moving averages (a 0.4 s window is 19,200 taps at 48 kHz) must use `scipy.ndimage.uniform_filter1d`
  or a cumulative sum, never `np.convolve`: the convolve version hung a full build for over 30 minutes.
- Keep untouched sections bit-identical while you rework others: hold the master gain and the saturator's peak
  reference at the earlier version's values (measure them in a separate run with exactly the earlier settings: a
  reconstruction run with one new switch on gave 20.0 dB instead of 20.1 and moved the whole opening by 0.1 dB), and
  pin anything keyed to another section's level (a drum bus or a build keyed to the last chorus's RMS changed the
  bridge when only the chorus changed). Diff the new file against the old one sample by sample to prove it.
- Gates before a hit must ramp. A half-beat silence gate that re-opened every bus in one sample at the bar line
  switched the previous chord's ring back on right on the chorus downbeat: the largest click in the song (a 0.31
  step in two samples), present for three versions because a fade went onto the wrong layer. Ramp the gate over
  3 ms starting 4 ms before the bar, keep the previous part's bus shut 150 ms past the hit, and confirm a click fix
  by diffing the samples at that exact time.
- Check the balance per section: a melody bus panned right only in the choruses leaned them 1-2 dB right once the
  bed under it got quieter.
- Before calling a master final, run independent checks in parallel by lens (harshness and buzz; repetition and
  timing; musical fit and seams; preservation of the parts he loves plus the master and encodes), each asked to
  refute, with numbers against the previous version. On one song they found a free-time strum drifting 85-120 ms
  off the beat, choruses that still repeated their own first half, the click above, and a pan lean, none of which
  the build's own gates flagged.
- The owner listens on headphones, a phone speaker and (if it plays there) in the game. Claude reports numbers and the
  owner's words, never "it sounds".

## 4. Master
1. Chain per references; ceiling -1 dBTP (or -2 dBTP when the master is louder than -14 LUFS). End the chain with
   `python ${CLAUDE_SKILL_DIR}/../../tools/lookahead_limit.py <premaster.wav> <master.wav> --target -14 --ceiling -1`:
   it writes the master and prints gain reduction per 10 s (median, 95th percentile, max, swing). A limiter that
   pulled the gain down 60 to 70 ms before every hit and held it flat pumped the last chorus at a median of 8.8 dB;
   this forward-only one brought it to 0 (max 3.4 dB). With drums, accept a little more, but keep the swing under
   about 3 dB in the loudest section. On FIX, lower `--target` by 0.5 LU and render again before squeezing harder
   (one drum-led master settled at -15 LUFS). If another limiter is used, this report does not apply to it.
2. `python ${CLAUDE_SKILL_DIR}/../../tools/loudness.py <master.wav> --target streaming` (or `club`, `ingame`) on the
   file step 1 wrote; re-run it after any change in step 1.
3. Encode check: make the AAC/MP3 a platform would, measure it again; true peak over the ceiling = lower the ceiling.
4. Matchering is allowed as a starting point against a well-chosen reference; its output is measured like any other.

## 5. Write it down
MIX.md: references used, the final numbers (integrated, LRA, true peak, encoded true peak, phone-check share), the
chain, and what changed after each listening note. SONG.md Status: "mastered"; next: music-video and marketing-studio.

## Ship bar
Every row in skill music-review >= 8.5 for the audio rows; 0 FIX from loudness.py on the master and the encode.
