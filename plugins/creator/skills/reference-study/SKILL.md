---
name: reference-study
description: Study a reference video or channel the creator sends (or research finds) before the next edit - measure it (cuts per minute, shot lengths, sound hits, loudness, pauses, thumbnail colours), watch it whole, read its hook, transitions and outro on dense frame sheets, list every device by what it does for the viewer, and write rules that change a tool, gate or skill step. Use for a pasted YouTube link, "study this", "look at this video", "how does X edit".
---

# reference-study <url or id>

status: beta

Every reference the creator sends gets a FULL study BEFORE the next edit; a link with no study note is an open to-do.
Reference, never copy: take the principles; the result must still feel like him.

## Steps
1. **Already done?** Search the project's research notes for the video id first. If it has a note, read it and only add
   what's new.
2. **Download** to its own fresh folder (public video only; `yt-dlp --js-runtimes node --remote-components ejs:github -f "bv*[height<=1080]+ba" <url>`; without the two flags YouTube downloads fail with "This video is not available" (yt-dlp 2025.12+, checked 2 Nov 2026) + subs if any).
3. **Measure:** if the project has a breakdown tool, run it; otherwise by hand with ffmpeg: cuts per minute and shot
   lengths (`select='gt(scene,0.3)'`), loudness (`ebur128`), pauses (`silencedetect`), added sound hits per minute (count
   by ear on 2-3 sample minutes), thumbnail colours. Time-labelled contact sheets of the whole runtime.
4. **Watch it whole:** picture + sound, the full runtime, never only the transcript or the sheets.
5. **Look (a helper, not the orchestrator):** one fresh agent reads ONLY the sheets for the hook (0:00-0:30), 2-3
   transitions and the outro, <= 12 tiles a sheet, <= 20 images, and writes findings to a file.
6. **Listen:** the transcript (subs or a speech-to-text pass): the hook words, how the premise is said by 0:30, the
   payoff lines.
7. **Device list:** every device with its time and what it does for the viewer (the feel, not the name). Mark what we
   already do, what we do worse, what we lack.
8. **Write it up:** one research note (header: id, url, date, why he sent it, his words verbatim) + a row in the
   research index. End with rules: each = what changes + which file (a tool, a gate, a skill step, the style log) + the
   number it should move.
9. **Adopt only what beats ours,** wired into the real tool or skill, never a one-off in one video's build.
10. Tell him in bullets: what the reference does that we don't, what changes next video.
