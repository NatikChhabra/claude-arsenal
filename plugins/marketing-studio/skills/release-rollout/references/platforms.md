# Platforms, distributors and RP rules for a music release (checked 2 Nov 2026)

Sources and the full claims table: research/05_release_marketing.md. CONFIRMED = read on the platform's own page;
CONFIRMED (2nd) = a credible secondary quoting it (the primary would not load); INFERRED = ours or unsourced.

## Spotify
- Pitch one unreleased song at least 7 days ahead in Spotify for Artists; the 2024 guide says two weeks. Delivery 7+
  days ahead for first-week Release Radar. CONFIRMED.
- Countdown Pages (pre-save): albums and EPs only, not singles; need 5,000 monthly active listeners; published 7+ days
  ahead they roughly double pre-saves. CONFIRMED.
- Marquee / Showcase: paid (USD 100 minimum, Marquee 250 via a rep), need 1,000 streams in 28 days, India-based teams
  not eligible. Discovery Mode: 25,000 monthly listeners, 30% commission. CONFIRMED.
- Canvas: 3-8 s, 9:16, no song or artist name. Clips: new uploads ended 17 Jun 2026. CONFIRMED.
- **AI Persona badge (mid-Sep 2026):** an artist whose visual identity is an AI-generated photoreal human gets no
  editorial or algorithmic recommendations and no Discovery Mode. Human artists using AI tools don't get it. Keep the
  owner as the real artist; use in-game GTA shots or clearly stylised art. CONFIRMED.
- AI tools allowed; voice impersonation needs the artist's authorisation; AI credits via the distributor (DDEX) don't
  rank tracks down. CONFIRMED.
- Evidence: ~75% of first-year streams come after day 28; a new release lifts catalogue streams 15-20%; music-video
  viewers stream the artist 57% more over the next 3 weeks (Spotify fan study). CONFIRMED.
- Editors ask for who, what, why, when, where, how; the story; the marketing plan; accurate mood and genre. Follower
  counts and press don't factor in. CONFIRMED. 500-character practical limit: INFERRED.

## Distributors (AI-assisted vocals decide this)
| Distributor | AI content | Notes |
|---|---|---|
| CD Baby | refuses any AI content, even partial | CONFIRMED |
| TuneCore | only if every GenAI tool was trained on fully licensed data; 100% AI songs rejected | CONFIRMED / INFERRED (help page unreadable) |
| Amuse, RouteNote | accepted, but AI releases skip YouTube Content ID (Amuse also skips Meta and Qobuz) | CONFIRMED; RouteNote Free keeps 85% |
| DistroKid | accepted with 100% rights, no impersonation, the AI box ticked; asks if lyrics, music, all or part of the audio is AI | CONFIRMED (2nd); USD 24.99 / 44.99 / 89.99 a year, splits on every plan |
Check the chosen distributor's AI page by hand on release week; policies moved monthly in 2026.

## RouteNote upload, hands-on (10 Nov 2026, Free plan)
- Audio: MP3 320 kbps or FLAC at exactly 44.1 kHz. There is no WAV option, and a 48 kHz FLAC is refused ("sample rate
  is too high"). Tested route: `ffmpeg -i master.flac -af "aresample=44100:resampler=soxr:precision=28:dither_method=triangular"
  -c:a pcm_s16le store.wav`, then `ffmpeg -i store.wav -c:a flac -compression_level 12 store.flac`; check the rate with
  ffprobe. Keep the upload copy alone in its own folder so the 48 kHz master can't be picked by mistake. CONFIRMED.
- Release date: the earliest sales start date offered was 14 days out (24 Nov when set on 10 Nov). "Originally
  Released" must be on or before the sales start date, so set both. Blank sales start = as soon as approved. CONFIRMED.
- Required fields: a contributor (the role list has instruments such as Guitar as well as Producer), a composer's first
  and last name, C and P lines, a label name (the artist's own name works). Language has no "Instrumental" entry: keep
  English, tick no lyrics, leave the track's Audio Language at None. The genre list does have Instrumental. CONFIRMED.
- A first release: the artist search offers "Create a new profile". Pick it rather than a lookalike name. CONFIRMED.
- Artwork: 3000 x 3000 px RGB JPG under 25 MB, no URL, contact details or prices on it. CONFIRMED.
- Stores: all 45 are ticked by default and YouTube Content ID is a separate box, also ticked. Untick Content ID when
  the artist or friends will use the song in their own videos, or the claims land on them. CONFIRMED.
- Preview start defaults to 0:30; set it to the hook. CONFIRMED.
- Distribute: a terms tick plus "Distribute Free" (the owner's own click). After that the audio is locked; metadata edits
  stay possible and take up to 30 days to reach stores. Status then reads "Pending Moderation". CONFIRMED.
- Through Claude in Chrome: the extension uploads at most 10 MB per call, so the owner picks the audio file (a 3-minute
  16-bit FLAC is about 13 MB). The cover uploads fine once copied into the session's working folder (delete the copy
  after). The date picker: a found ref can be the "Clear Date" button, so open the calendar image next to the input
  (id `button2` style) or dispatch a click on the day cell, then read the input's value back. Screenshots can time out
  while a calendar is open; read values with JavaScript instead. CONFIRMED.

## YouTube
- Official Artist Channel: 1+ release through a distributor, plus YPP or a Services Directory distributor; a strike
  suspends it. CONFIRMED.
- Disclose AI music that is the main focus of a video; his real vocal plus pitch correction is "No Gen AI"; cloning his
  own voice for voice-overs is exempt. CONFIRMED.
- Shorts: use the official song from the audio picker once distributed; post weekly (artists posting weekly got 60%+
  of new subscribers from Shorts); over 1 minute with a Content ID claim = blocked. CONFIRMED.
- Titles match the video, key terms first, caps and emoji rare; read CTR on Home/Suggested in the first 24 h. CONFIRMED.

## TikTok and Instagram
- TikTok New Release tag: 14 days before to 30 days after release. Business accounts see only the Commercial Music
  Library, so run the artist page as a personal or creator account. CONFIRMED / INFERRED.
- Instagram: copies and watermarked posts aren't recommended; Trial Reels go to non-followers first, metrics after
  24 h; realistic AI audio needs the AI label. CONFIRMED / CONFIRMED (2nd).
- Hook choice: no platform gives a rule; cut 3-4 different 15-30 s sections and let Trial Reels and Shorts pick.

## RP servers (Cfx.re licence + each server's rules)
- Cfx.re Creator Platform License (10 Sep 2026): no third-party ads or sponsorships in server content (3.1(7)); no
  third-party-licensed music (2.4); nothing implying Rockstar endorsement (2.3). CONFIRMED.
- Public server rules commonly ban advertising other businesses, communities or servers, and metagaming (OOC info used
  IC); some allow your own Twitch/YouTube in your name; some allow only DMCA-safe music in the city. Read the owner's
  server's rules and ask staff; never cite a server rule you didn't read.
- Playbook (INFERRED): perform IC (in-city radio, an event) only when the server allows custom audio and it is his own
  original; real-world links stay OOC where allowed; never name other servers; the RP story is the hook OOC.

## Measurement
- Spotify Release engagement = % of the monthly active listeners (day before release) who streamed the release in its
  first 28 days, UTC. Save rate is not a Spotify metric: saves / listeners per song. No primary benchmark exists:
  compare with his own last release (a vendor's "20-25% good" is INFERRED only). CONFIRMED / INFERRED.
