---
name: studio-setup
description: >-
  Set up and check the owner's home recording rig so every take is usable the first time: the signal chain for an
  acoustic with a soundhole pickup and for an electric through a practice amp with a USB audio interface built in
  (Blackstar ID:Core V4 class), drivers, DAW settings, which inputs to record, monitoring without delay, levels, the
  song folder layout and a 1-minute rig check with take_check.py. Use for "set up my recording", "my amp arrived",
  "REAPER doesn't see my amp", "my takes sound bad", "it's crackling", a new guitar or interface, or before the first
  take of any song.
---

# studio-setup

status: draft (built from the amp's own manual and the problems found in the first single's takes; promote to beta
after the first session on the new amp)

The rig serves his playing: get it right once, check it in a minute, then forget it. Tone, effects and the rest are
his choices; this skill only makes sure what he plays arrives clean. Visual, sound-design and cover rules live in the
design plugin.

## 1. The chain
**A. Acoustic with a passive soundhole pickup (what the first single used).**
Pickup -> guitar cable -> the computer's input -> DAW. What it cost: band levels fell about 12 dB per octave above
300 Hz and everything over 5 kHz was hiss (guitar-capture §1, "Soundhole pickup takes"), and the Windows input
soft-clipped the loudest chucks near 0.98. A passive magnetic pickup wants a high-impedance instrument input; a
computer's mic or line jack is far lower, which dulls the top end (INFERRED from the measured roll-off, not tested
side by side). Until an instrument input is available: record in the DAW, not the Windows Sound Recorder (it saved
16-bit takes), turn off Windows "audio enhancements" and any mic boost or auto gain, and keep peaks under -6 dBFS.
If the owner's amp sim has an input treble fix for mic jacks (it measures how much top end the jack loses and puts it
back), run its setup once and put the sim on the guitar track as a track effect, not an input effect: the DAW still
records the bare pickup, so the tone stays his to change after the take. Its standalone app usually takes the sound
card for itself, so close the DAW before opening it.

**B. Electric (or the acoustic's pickup) into a USB practice amp.** Guitar -> guitar cable -> amp Input; amp USB-C
-> a rear USB port on the PC (front ports and hubs cause dropouts; the manual says the same). Checked in the
Blackstar ID:Core V4 manual (Feb 2026 edition):
- Windows needs Blackstar's own USB audio driver (from blackstaramps.com/idcorev4-welcome); a Mac needs none.
  Select that driver as the DAW's audio device (ASIO). If the DAW doesn't see the amp, try another cable first:
  a charge-only USB-C cable carries no audio.
- The amp sends four channels at once: 1 and 2 = the full stereo amp sound with cab emulation and its effects;
  3 = the preamp only (voice and EQ, no effects, no cab), for your own cab and effect plugins; 4 = the dry guitar
  exactly as it leaves the guitar.
- From the computer it plays 1 and 2 (click and backing through the amp or its headphone jack) and takes 3 as a
  reamp input. Reamp mode (switched on in Blackstar's Architect app; off again when the USB cable comes out or the
  amp powers off) sends a dry track back through the amp and returns the processed sound on 1 and 2.
- Plugging headphones into the CabRig and Phones jack mutes the speakers and carries the same cab-emulated sound.
- Try the acoustic's pickup through the amp too (cleanest voice, EQ flat, no effects) and record channel 4: a real
  instrument input instead of the computer's jack. Run take_check on one take each way and keep the better route.

## 2. DAW session (REAPER by default; any DAW has the same settings)
- 48 kHz, 24-bit, WAV. Buffer 128 samples (256 if it crackles). Same rate on the device and the project.
- Tracks for each guitar take: **AMP** (stereo, inputs 1+2, panned hard left and right as the manual advises for its
  wide stereo effects), **DI** (mono, input 4, always armed: it is the safety copy and lets the tone change later
  with an amp-sim plugin or reamp mode; the owner picks that tone, see song-cycle), **PRE** (mono, input 3) only when a cab plugin will be used. Acoustic through
  the computer's jack: one mono track from the live input (check both channels: a mono source on a stereo input once
  left one side 45 dB down).
- Voice: one mono track from the mic, 24-bit, peaks -12 to -6 dBFS, a pop filter, 15-20 cm away.
- Save this once as a project template named for the rig, so every song starts with the same tracks.

## 3. Monitoring without delay
- Listen to the guitar through the amp (speaker or its headphone jack), never back through the computer: input
  monitoring OFF on the guitar tracks, so nothing he hears is late.
- The click and any backing come from the DAW through the amp's USB playback (channels 1 and 2), into the same
  headphones. The click goes to his ears only, never to a speaker a mic can hear (a click caught by the mic gets
  looped with the part).
- Acoustic through the computer's jack: monitor the room sound of the guitar itself and keep DAW monitoring off; if he
  must hear the pickup, set the buffer to 64-128 and check that it doesn't crackle.

## 4. Levels
- Set gain with the hardest thing in the song (the loudest strum or chuck), not the average: peaks -12 to -6 dBFS.
- On the amp, the USB level follows the amp's gain and voice settings; on the dry channel 4, the guitar's own volume.
  Set the guitar's volume knob at full and leave it there for the whole song.
- Tune before every take (more than 10 cents off shows in guitar_level.py and in every chord after).

## 5. Song folder (one per song, everything in it)
```
songs/<slug>/
  SONG.md            the one sheet (templates/SONG.md), ## Cycle says where the song is
  raw/               every take exactly as recorded, never edited or overwritten
  sheets/            play sheet (PNG and PDF) and play-alongs
  build/             scripts or DAW projects that assemble the song from raw/
  mix/               premasters, MIX.md with the numbers
  cover/             photo or drawing, layouts, the picked cover
  FINAL/             master FLAC and MP3 (cover embedded), CREDITS.md, release kit
```
Name takes `<part>_<take>_<date>.wav` (`chorus_03_2026-12-02.wav`). Keep DAW projects next to their audio. On the
owner's PC, music lives in its own music folder, apart from other projects.

## 6. The 1-minute rig check (before the first take of a session)
1. Record 20 s: 2 s of silence, then the loudest part of the song, then 4 muted chucks exactly on four clicks.
2. `uv run --with numpy --with soundfile python ${CLAUDE_SKILL_DIR}/../../tools/take_check.py <file.wav>` on each
   recorded track (AMP, DI, voice). Fix every FIX before recording the song; WARNs get fixed before the next session.
3. Zoom in on the four chucks: they should sit within about 5 ms of the click lines. If all four are early or late by
   the same amount, set the DAW's recording offset (REAPER: Preferences > Audio > Recording, use the driver's
   reported latency, then a manual offset) and check again.
4. After every real take, run take_check again on that file and say the verdict in one line. A FIX means the next take
   happens now, while he is still warm, not after the build.
