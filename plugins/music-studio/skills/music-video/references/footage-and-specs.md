# Music video: footage rights, capture, beat-sync and delivery specs (checked 2 Nov 2026)

Sources: research/04_production_and_video.md §7-8, research/05_release_marketing.md §4-5, §7. CONFIRMED = read on
the owner's or platform's own page.

## 1. Rights first (decide before shooting)
- **Rockstar's video policy** (support.rockstargames.com, updated 10 Jan 2025): game footage is allowed "for
  non-commercial uses" (you don't make money through it or use it to promote a product or service), and the policy
  "does not apply to the exploitation of Rockstar IP ... in music videos". A GTA-footage music video is outside the fan
  permission; a licence request goes to copyright@take2games.com. CONFIRMED. It also bans isolated cutscene uploads and
  third-party mod menus in GTA Online.
- **Cfx.re Creator Platform License (10 Sep 2026)**: no third-party ads or sponsorships in server content (3.1(7)); no
  uploading music "subject to license by a third party" and no remixing Rockstar's licensed music (2.4); nothing may
  suggest Rockstar endorses the server (2.3). CONFIRMED.
- **The server's own rules**: filming in public RP spaces, other players' consent to appear, custom audio in the city,
  advertising. Read them; ask staff when they are silent. Other players in shot = their consent or blur them.
- So the owner chooses per video, in SONG.md's decisions log: (a) non-monetised upload, risk accepted; (b) ask Take-Two
  for a licence; (c) a non-GTA video (lyric video, live guitar performance, stylised art) for the monetised release and
  the GTA cut as a non-monetised companion. Never decide this for him.
- Only his own original music in the video and in the city (2.4 above).

## 2. Capture
- FiveM recording: the community "Recording Clips" resource uses F1 start/save, F2 action replay, F3 cancel,
  `/rockstareditor` to open the editor (rebindable). Some servers disable the editor: ask the server. Forum reports of
  the editor stuck at "Downloading assets" and crashes on some builds: test before the shoot day. EVER (Extended Video
  Export Revived, Mar 2026) is untested: anti-cheat risk unknown, never on a live server without staff OK.
- OBS: Hybrid MP4 (OBS 30.2+) survives a crash mid-recording; game audio and mic on separate tracks; record at 1440p60
  or 2160p60 with AMD AMF HEVC or AV1 at high constant quality (CQP ~16-20; INFERRED) so grading and 9:16 crops hold up.
- Shoot list per section with spares: 3+ angles of every key moment, 2 s handles before and after every action, wide
  establishing shots of each location, close-ups of the character for the chorus, cutaway details (hands on a wheel,
  a phone screen) for lyric lines.

## 3. Beat-sync
- `beatmap.py map <master.wav>` gives beats, downbeats and sections; `beatmap.py cuts <map.json> <cuts.txt|edl.json>
  --fps <fps>` measures every cut against the grid (on grid = within one frame).
- Grammar (INFERRED from editing practice): section changes and big moves on downbeats; montage cuts on beats (every
  2 beats at mid tempos reads natural); hold shots across a chorus phrase (4 or 8 bars) when the picture has its own
  motion; visual accents on snare and transient hits. Off-beat cuts are a device: mark them in the edit list.
- House bar: >= 90% of cuts on grid outside marked off-beat moments.
- DaVinci Resolve's "Detect Music Beats" is Studio-only (secondary); markers can be added by hand with M.

## 4. Photosensitivity (hard rule)
- WCAG 2.3.1 and Ofcom: no more than 3 flashes in any 1 s unless below the general and red flash thresholds; any
  change to or from saturated red counts. Flashes on every 8th note at 120 BPM = 4 a second = FAIL. Flash on quarter
  notes at most, and never at full-screen red. Check with the design skill's flash count (references/edit.md §2.8, §7).

## 5. Delivery specs
- YouTube master (recommended upload settings, CONFIRMED): MP4 fast start, H.264 High 4:2:0, native frame rate;
  1080p60 12 Mbps, 1440p60 24 Mbps (1440p gets the better YouTube codec: widely reported, not confirmed); audio
  AAC-LC 48 kHz 384 kbps stereo; the mastered song re-measured in the rendered file.
- YouTube Shorts: up to 3 minutes; **a Short over 1 minute with an active Content ID claim is blocked worldwide**,
  which can hit his own song once a distributor registers it: whitelist his channel at the distributor or keep Shorts
  at 60 s or under. Use the official song from the audio picker once it is distributed (YouTube's artist guide).
- Instagram Reels: up to 3 minutes (announced 21 Jan 2025, secondary); 1080x1920; no visible watermarks (a TikTok
  export with its watermark is not recommended). TikTok: 9:16 1080x1920 (secondary). Safe zones: keep text out of the
  top ~14% and bottom ~35% on Reels (vendor guides, INFERRED): check in each app's preview.
- Spotify Canvas: 3-8 s loop, 9:16, no song or artist name on it (Spotify guidelines).
- Spotify Clips: new uploads ended 17 Jun 2026.
- YouTube Song Rollup pools the official video, art track, lyric video and live versions into one song number: every
  format feeds the same count.
