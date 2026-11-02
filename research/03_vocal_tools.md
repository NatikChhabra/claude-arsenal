# Vocals for a non-singer: tools, terms and platform rules (research, 2 Nov 2026)

Scope: a guitarist on Windows (RX 7800 XT 16 GB, ROCm 7.2 via ComfyUI, Ryzen 5 7600X, 32 GB) who wants
release-quality vocals in English / Hindi / Hinglish that keep HIS melody and phrasing, for public release
(YouTube, Instagram, Spotify).

Tags: **CONFIRMED** = read on a primary page (vendor site, docs, GitHub README, help centre, official newsroom).
**INFERRED** = secondary source (press, blog, vendor guide) or my reasoning from confirmed facts. "Not stated" means
I read the primary page and it did not say.

Pages I could not read: DistroKid help centre (all articles returned a client error, and a retry through the
Zendesk API was refused by the session's auto mode), TuneCore's "GenAI Music Content Framework" help page (client
error), Deezer's Oct 2026 "AI music toggle" newsroom post (redirect loop). The DistroKid and TuneCore rows below come
from secondary sources and are tagged INFERRED. Check those three pages by hand before a release.

---

## 1. Suno

**Model state (late 2026).** Suno **v6** launched 9 Sep 2026 as a family: v6 (flagship) and v6-wild are paid only,
and v6-mini is free. It adds plain-language editing of one section or one lyric line, mashups, and single-lyric edits
(release notes, CONFIRMED). v5.5 (26 Mar 2026) introduced **Voices** (your own voice), **Custom Models** (train
on your own catalogue, at least 6 tracks, up to 3 per account) and **My Taste** (CONFIRMED). v6 was built "with Warner
Music Group, BMG and Believe" (INFERRED, DataNorth).

**Features relevant to keeping his melody**
- **Voices** (Pro/Premier): upload or record 15 s to 4 min of *singing*, then pick the best 2 min. Acapella works best,
  and Suno strips backing via stems. A spoken verification phrase must match the singer, a rights checkbox is
  required, users must be 18+ and some regions are excluded (CONFIRMED, help 11362369). **Implication:** Voices
  clones *his* timbre from his own singing. It neither fixes his pitch nor takes someone else's voice. It replaces the
  default Suno singer (INFERRED).
- **Add Vocals** (beta, Pro/Premier): generates a vocal from your lyrics over an uploaded or generated
  instrumental. An "Audio Strength" slider sets how closely the song follows the instrumental. The help page **does
  not say it follows an uploaded melody or guide** (CONFIRMED). So it writes its own topline and won't keep his melody.
- **Cover / Extend / Remix** of uploads exist (v4.5 upgraded covers + personas, May 2025; remix with Cover / Extend
  / Reuse Prompt, May 2025; Extended Uploads up to 8 min, Jun 2025) (CONFIRMED, release notes). A cover of his own sung
  or hummed guide is the Suno route closest to keeping his melody, but adherence isn't documented (INFERRED).
- **Suno Studio 2.0** (Premier; Aug 2026): browser DAW with MIDI, synths, automation, built-in FX (no VST/AU),
  **audio-to-MIDI**, "generate an audio cover of a MIDI part", stem split, WAV/MIDI import, and 32-bit WAV stem
  export. Chrome is recommended (CONFIRMED, help 13670529). Rendering a MIDI melody he wrote as a sung part is a
  possible route, but how well the result follows the MIDI is not documented (INFERRED).
- **Stems**: Advanced Split (~100 instruments, Premier), Split from Mix, Auto Split (12 categories), released 11 Jun 2026
  (CONFIRMED).
- **Suno MCP (beta)**, 28 Oct 2026: create songs from Claude and other MCP clients, using credits (CONFIRMED).

**Hindi quality:** no Suno primary page lists supported languages or rates Hindi (CONFIRMED absence on v5.5 blog, v6
notes, help search). Only a community "Language/Accent Tests" playlist exists. **Must be tested on his own lyrics.**

**Plans and rights (CONFIRMED unless noted)**
| | Free | Pro | Premier |
|---|---|---|---|
| Price shown 2 Nov 2026 (may be regional) | $0 | $8/mo | $24/mo |
| Ownership | **Suno owns** the songs, non-commercial only | You own | You own |
| Commercial use / distribution | No (and subscribing later does not license old free songs) | Yes, any distributor, YouTube/TikTok OK, no attribution needed | Yes |
| Downloads (from 3 Sep 2026) | 7 lifetime trial downloads, personal use only | 20/month (+ buy more) | 60/month; unlimited in Studio |
| Voices / Custom Models | No | Yes | Yes (+ shareable custom models) |

- You must hold 100% of the rights to monetise. Someone else's lyrics can get a YouTube channel struck or a
  distributor blacklist (CONFIRMED, help 2410177).
- **Copyright caveat:** "may not be eligible for copyright protection". Fully AI music doesn't qualify in the US.
  Lyrics you wrote are yours. Some distributors exclude uncopyrightable songs (CONFIRMED, help 2746945).
- **Warner deal (25-26 Nov 2025):** settled the lawsuit. Under it, Suno launches licensed models in 2026, downloads
  require a paid account, paid tiers get monthly download caps, free songs are play/share only, Suno takes over
  Songkick, and artists opt in for name, likeness, voice and compositions (INFERRED, Music Week). The 10 Aug 2026 Suno
  blog put the download caps into effect from 3 Sep 2026 and says older models will be retired (CONFIRMED).

## 2. Udio

- UMG partnership 29 Oct 2025, then **downloading of audio, video and stems disabled** (CONFIRMED, Udio help article dated
  17 Feb 2026). Credits were raised as compensation: Standard 2,400/mo, Pro 6,000/mo, plus a one-off 1,000 bonus.
- Warner settled with Udio in Nov 2025. Udio moved to a "walled environment" while a licensed subscription
  platform is built. A 48-hour download window was reopened once (INFERRED, RouteNote).
- The Udio changelog has no 2026 entries (CONFIRMED). No launch of the new licensed platform found.
- A vendor guide (updated 26 Apr 2026) says Udio music made after Oct 2025 cannot be commercially distributed
  (INFERRED, Dynamoi).
- **Verdict: not usable for a release** (no file export).

## 3. ElevenLabs Music (Eleven Music)

- Models: **Music v2.5** (newest), v2 (default in the UI), v1 (still the API default, being phased out). Features:
  composition plans, section and lyric editing, **inpainting** (regenerate one section), **Audio Reference** (~30 s
  track steers style, paid plans, copyright-screened, "does not remix the audio"), **Music Finetunes** (train on
  tracks you own, ~5-10 min), vocal or instrumental output, 3 s to 5 min, MP3/WAV (CONFIRMED, docs).
- **There's no documented "sing my melody" or "upload my vocal guide" path.** Audio Reference shapes style only
  (CONFIRMED). It won't keep his melody (INFERRED).
- Languages: "multilingual", with English, Spanish, German and Japanese named. **Hindi is not named** (CONFIRMED).
- Commercial: "cleared for nearly all commercial uses" (film, TV, podcasts, social, ads, games). Terms vary by plan.
  Free plan = no commercial licence, and you must credit "Eleven Music". Paid = commercial licence. Content made with
  Beta Services can't be used commercially (CONFIRMED, help 13313564601361). Streaming distribution is not mentioned
  on the pages I read.
- Licensing: launched 5 Aug 2025 with **Merlin + Kobalt** deals. Prompts may not name artists or labels, and outputs
  may not mimic an artist's voice (INFERRED, MBW). The ElevenMusic app (29 Apr 2026, upd. 22 Sep 2026) lets people
  remix and earn on-platform (CONFIRMED, blog).

## 4. Vocal synths (keep his melody exactly: notes in, voice out)

**Synthesizer V Studio 2 Pro (Dreamtonics)**
- Editor $99 (perpetual, one-time). v2 voices $79 each. Upgrade from v1 Pro $49. Released 21 Mar 2025. Standalone +
  VST/AU/AAX. Speed-up "without requiring a dedicated GPU". Windows 8.1+, i5/AMD, 2 GB RAM (CONFIRMED, dreamtonics
  announcement + product page).
- Languages: Japanese, English, Mandarin, plus Korean (new in v2) for cross-lingual synthesis. Cantonese and Spanish
  were added during v1 (CONFIRMED for JP/EN/ZH/KO; INFERRED for Spanish/Cantonese via SOS review and forum). **Hindi: not
  supported** (not on any Dreamtonics page; a forum reply says a new language needs a partner company) (CONFIRMED absence).
- **Voice-to-MIDI** in Studio 2 Pro: turns a sung recording into notes + lyrics. Options include "Transfer pitch onto
  converted notes", with semitone rounding off by default to keep glides (CONFIRMED, Dreamtonics article). **This is the
  cleanest "his melody, a real singer's tone" route for English.**
- Commercial use: "Our commercial use policy has not changed". The licence panel is in the app, and terms are per
  voicebank (CONFIRMED that the page defers. Read each voice's licence before release).

**ACE Studio (Timedomain)**
- v2.0. Artist Lifetime $398 (Plugin Boutique), with 2,500 AI credits/mo for 2 years and then a subscription needed.
  160+ voices. Choir mode, voice changer, **voice cloning**, stem splitter, ACE Bridge 2 (VST3/AU/AAX). Windows 10 64-bit,
  8 GB RAM, **internet required** (CONFIRMED, Plugin Boutique listing + acestudio.ai).
- Languages: English, Spanish, Chinese, Japanese now. Italian, French, Portuguese and Korean "coming soon" (store page).
  The homepage says "8 languages". **Hindi not listed** (CONFIRMED).
- **Vocal to MIDI**: acapella in, MIDI with lyrics out. "Use Original Pitch" applies his pitch curve. V1 covers
  EN/ES/ZH/JA, V2 adds more (incl. Korean). **"MIDI only" mode for other languages**, one language per pass (CONFIRMED,
  docs). So Hindi melody transfers but Hindi lyrics won't be sung properly (INFERRED).
- Commercial: built-in voices are royalty-free for commercial projects. Custom-voice licensing depends on your own
  recordings (CONFIRMED, FAQ).

**OpenUtau + DiffSinger** (free, open source)
- OpenUtau supports DiffSinger (OpenVPI). On Windows set Machine Learning Runner = **DirectML** to use a discrete GPU
  (vendor not named, so AMD should work via DirectML) (CONFIRMED wiki; AMD = INFERRED).
- Languages are set by the voicebank and phonemizer. **No Hindi DiffSinger voicebank or phonemizer found** in the
  wiki or search (INFERRED, absence of evidence). Licence terms are per voicebank.

## 5. Singing voice conversion (sing or hum the guide, swap the timbre)

**Applio (RVC)**
- MIT code + weights. Commercial use is allowed with the necessary rights, and the project asks for contact at
  support@applio.org before commercial use. **"Applio will no longer receive frequent updates"** (security and
  dependency updates only) (CONFIRMED, GitHub README).
- AMD on Windows: the new desktop installer mentions "supported AMD configurations" and warns that "old CUDA or
  HIP/ZLUDA recipes may conflict" (CONFIRMED, docs). The legacy **ZLUDA guide** (Applio `assets/zluda/README.md`,
  read via a Hugging Face mirror) lists **gfx1101** (= RX 7800 XT) with HIP SDK 5.7.1. The first run compiles kernels
  for 15-20 min with no output (CONFIRMED in the mirror; Applio repo copy not read). DirectML/ROCm are not documented.
- Training data: the docs give **no minutes figure**. They ask for clean, varied pitches and delivery, and warn that
  clipping can't be undone (CONFIRMED). Community norm is ~10-30 min of clean singing (INFERRED, not read on a
  primary page). **Note: an RVC model trained on HIS voice keeps his off-key pitch. RVC transfers the guide's pitch
  as-is, so fix the pitch first (Melodyne) or convert to a licensed singer's model** (INFERRED).

**Seed-VC**: **archived by the owner on 21 Nov 2025**, read-only. GPL-3.0. Has a 44.1 kHz singing model (f0-conditioned,
~200M params) and fine-tuning on 1-30 s clips. No successor named (CONFIRMED, GitHub).

**Maintained successor / 2026 best-in-class open SVC: YingMusic-SVC** (GiantNetwork AI Lab + Tsinghua, arXiv
2512.04793, Dec 2025). Built on Seed-VC, zero-shot. Robust on real songs with harmony and backing, ships its own
accompaniment separator plus a Gradio app. **Code MIT; weights licence not stated** (CONFIRMED, GitHub + arXiv). No AMD or
Windows notes, and no user fine-tune scripts. Needs testing for Hindi.

**Kits.ai**: artist voices are official models trained on partner artists' studio vocals. Default = **personal,
non-commercial** licence. For commercial use you submit the track, and **the artist approves or denies it at sole
discretion**. If approved: perpetual worldwide licence, you pay the artist the % of gross revenue on their page
(quarterly, you remit it yourself), and you must include their publishing info when distributing (CONFIRMED, Kits FAQ
+ Artist Model Licence PDF). Paid plans from $9.99/mo (CONFIRMED, FAQ).

## 6. Pitch correction (fix a weak guide vocal)

- **Melodyne 5** (Celemony shop, USD): Essential $99, Assistant $249 (list $299), Editor $399 (list $499, adds DNA
  polyphonic), Studio $699 (list $849, multitrack). Prices were matched to editions by page order (CONFIRMED with that
  caveat). Essential = basic pitch + timing for vocals. Assistant = full vocal toolkit (pitch, timing, vibrato, formants).
- **Auto-Tune (Antares)**: 2026 lineup is AutoTune Advanced, Pro 11 (Graph Mode, note-by-note), AutoTune (2026) and AutoKey 2.
  **AutoTune Unlimited** subscription costs $30/mo or $300/yr from 4 Apr 2025 (CONFIRMED). No free version, trial only.
- **Free:** **Graillon 3** (Auburn Sounds, v3.2): free edition includes pitch correction. The full edition ($29) adds PTM,
  keyboard tuning and a doubler. VST/AAX/AU/LV2, Windows/macOS/Linux (CONFIRMED). **MAutoPitch** (MeldaProduction): free, in
  MFreeFXBundle, has formant shift (CONFIRMED). Neither is graphical note editing. For a weak singer, Melodyne-style
  note editing is the step that matters (INFERRED).
- YouTube classes "standard pitch-correction software to correct minor tuning mistakes" as **No Gen AI** (CONFIRMED, see §8).

## 7. ACE-Step 1.5 / 1.5 XL (local, open)

- **MIT licence**. Features: reference audio, **cover** from existing audio, **repaint** (local edit), stem separation,
  multi-track add layers, **Vocal2BGM** (makes an accompaniment for a vocal), BPM/key/time-signature control and LRC
  timestamps (CONFIRMED, GitHub).
- **LoRA on his own songs**: "from just a few songs". One-click training, "8 songs, 1 hour on 3090 (12GB VRAM)" (CONFIRMED).
- Languages: "50+ languages". **Hindi not named**. The project's own limitations list includes "multilingual lyrics
  support needs improvement" and calls vocal synthesis "coarse and lacking nuance" (CONFIRMED). So Hindi vocal quality
  is unproven and must be tested (INFERRED).
- **XL** (2 Apr 2026): 4B DiT (~9 GB bf16), variants base/sft/turbo. Base handles all tasks (cover, repaint, extract, lego,
  complete). VRAM: >=12 GB with offload + INT8, >=16 GB with offload, >=20 GB without (CONFIRMED, HF card).
  Training data is licensed + royalty-free/public domain + synthetic (INFERRED, Comfy blog 17 Apr 2026).
- **AMD Windows path**: ROCm supported. Windows ROCm needs **Python 3.12** (AMD ships only 3.12 wheels), and launchers
  `start_gradio_ui_rocm.bat` / `start_api_server_rocm.bat` are included (CONFIRMED). In ComfyUI it's in the template library
  (CONFIRMED, Comfy blog). On 16 GB: 2B turbo/SFT runs comfortably, XL needs CPU offload (CONFIRMED tiers).
- Best use for him: **Vocal2BGM** and cover/repaint for arrangement ideas around HIS vocal. It's not a melody-faithful
  singer (INFERRED from the stated limitations).

## 8. Platform rules for AI-assisted vocals

**Spotify**
- AI use is allowed: "We support artists' freedom to use AI creatively while actively combating its misuse" (CONFIRMED,
  newsroom 25 Sep 2025).
- **Impersonation:** "Vocal impersonation is only allowed in music on Spotify when the impersonated artist has
  authorized the usage" (CONFIRMED). His own voice, or a licensed voice (Kits approval, SynthV/ACE voicebank) = fine.
- **AI credits via DDEX** cover vocals, instrumentation and post-production, and are submitted by the distributor. Disclosure is
  "not meant to penalize" or downrank. The beta has shown credits in Song Credits since 16 Apr 2026 (CONFIRMED).
- **Spam filter:** tags and stops recommending mass uploads, duplicates, SEO hacks and artificially short tracks. 75M+
  spam tracks removed in 12 months (CONFIRMED).
- **"AI Persona" badge** (announced 13 Aug 2026, live mid-Sep 2026): for artists whose *public identity* is AI-generated.
  Such profiles are **excluded from editorial and algorithmic recommendations**. "La etiqueta AI Persona habla de la
  identidad pública del artista, no de cómo fue creada su música": a human artist using AI tools does not get it
  (CONFIRMED). Keep a real artist identity. A photoreal AI persona kills reach.

**YouTube**
- Disclosure is required when content "Creates music that's the main focus of the video". "AI generated music" is a
  listed example. "Cloning one's own voice to create voice overs or dubs" and "voice or audio repair" do NOT need
  disclosure. AI music may get a **label on the player**. Disclosure alone doesn't limit reach or monetisation, but
  repeated non-disclosure can mean removal or YPP suspension (CONFIRMED, help 14328491, undated).
- Music-specific disclosure: **Fully Gen AI / Partly Gen AI / No Gen AI**. "Partly" = AI layers under live human
  vocals, or AI-co-written lyrics or melody. Standard pitch correction and AI mastering = **No Gen AI**. Set via DDEX ERN
  4.3.2+, CSV `contains_ai`, or YouTube Studio attributes (CONFIRMED, help 17124251).
- Implication: his real vocal + Melodyne = No Gen AI. A synth or converted vocal of his melody = at least Partly, and
  probably label-worthy as AI music (INFERRED).

**DistroKid** (help centre unreadable from here, INFERRED via Jack Righteous, reviewed 25 Oct 2026): the upload asks
whether any part is AI-generated. If yes, tick at least one of "The lyrics / The music / All of the audio / Part of the
audio". "All of the audio" adds a human-or-AI-persona question. Credits can be edited later at distrokid.com/credits.
Pitch correction, AI mixing and mastering don't need AI credits.

**TuneCore / Believe** (primary page unreadable, INFERRED via Dynamoi, 28 Oct 2026): Believe's CEO aims to "not
distribute any content that is 100% created by AI". Fully prompted songs are likely rejected, while AI-assisted work with
human vocals or arrangement is accepted case by case. Detection plus manual review applies. Authorised voice models
only (GrimesAI pilot).

**Deezer** (CONFIRMED, deezer.com AI-labelling page): detection fingerprints generators such as Suno and Udio, and
fully AI tracks get an on-track label and are **excluded from Flow, recommendations and editorial playlists**. Up to 85% of AI-music
streams are flagged as fraud and demonetised. The page names no separate label for partly AI tracks. The Oct 2026 "AI music
toggle" post could not be read.

---

## What this means for his workflow (INFERRED synthesis)

1. **Route A, English, most melody-faithful:** sing a rough guide to a click, then SynthV Studio 2 Pro Voice-to-MIDI with
   "Transfer pitch" (keeps his phrasing and glides), quantise the bad notes to the scale, and render with a licensed v2
   voice. Disclose on YouTube as Partly/Fully Gen AI. Spotify allows it (not impersonation).
2. **Route B, Hindi/Hinglish:** no commercial synth sings Hindi (SynthV, ACE and ElevenLabs don't list it). Best bets are
   (a) his own vocal + Melodyne Assistant/Essential (counts as No Gen AI), or (b) his pitch-fixed guide, then voice conversion
   (Applio/RVC via ZLUDA on gfx1101, or YingMusic-SVC) to a voice he owns or has written permission for, or (c) a Suno
   v6 cover of his guide with his own Voices profile. Every option needs a blind test on his lyrics.
3. Never release from a free Suno or ElevenLabs plan: no commercial rights, and Suno owns free songs.
4. Udio is out (no downloads). Kits artist voices need per-track artist approval plus a revenue share.
5. Keep a real artist identity on Spotify (the AI Persona badge removes recommendations). Deezer hides fully AI tracks
   from recommendations, so a human vocal keeps him out of that bucket.

---

## Claims table

| # | Claim | Tag | Source URL | Date on page |
|---|---|---|---|---|
| 1 | Suno v6 family (v6, v6-wild paid; v6-mini free) launched; section/lyric edits, mashups | CONFIRMED | https://suno.com/release-notes | 9 Sep 2026 |
| 2 | v6 built with WMG, BMG and Believe | INFERRED | https://datanorth.ai/news/suno-launches-v6-v6-wild-and-v6-mini | 10 Sep 2026 |
| 3 | v5.5 introduced Voices, Custom Models (Pro/Premier, up to 3), My Taste | CONFIRMED | https://suno.com/blog/v5-5 | 26 Mar 2026 |
| 4 | Custom models need at least 6 tracks | CONFIRMED | https://suno.com/release-notes | 26 Mar 2026 |
| 5 | Voices: 15 s-4 min singing clip, best 2 min, spoken verification, rights checkbox, 18+, region limits | CONFIRMED | https://help.suno.com/en/articles/11362369 | undated ("Edited") |
| 6 | Add Vocals: beta, Pro/Premier, lyrics over an instrumental; no melody-guide adherence stated | CONFIRMED | https://help.suno.com/en/articles/6882817 | undated |
| 7 | Suno Studio 2.0: Premier, MIDI, audio-to-MIDI, stems, WAV export, no VST/AU | CONFIRMED | https://help.suno.com/en/articles/13670529 | 2026 (Studio 1.x deprecated early Sep 2026) |
| 8 | Stem separation: Advanced Split (~100 instruments, Premier) | CONFIRMED | https://suno.com/release-notes | 11 Jun 2026 |
| 9 | Suno MCP beta | CONFIRMED | https://suno.com/release-notes | 28 Oct 2026 |
| 10 | Free plan: Suno owns songs, non-commercial; paid: you own | CONFIRMED | https://help.suno.com/en/articles/2746945 | undated |
| 11 | Paid songs distributable to Spotify etc.; free not, no retroactive licence | CONFIRMED | https://help.suno.com/en/articles/2410177 | undated |
| 12 | AI-only songs may not be copyrightable; lyrics you wrote are yours | CONFIRMED | https://help.suno.com/en/articles/2746945 | undated |
| 13 | Downloads from 3 Sep 2026: Free 7 lifetime (personal), Pro 20/mo, Premier 60/mo, Studio unlimited | CONFIRMED | https://suno.com/blog/suno-updates-tos | 10 Aug 2026 |
| 14 | Pricing shown: Pro $8/mo, Premier $24/mo; free 50 credits/day | CONFIRMED (may be regional) | https://suno.com/pricing | read 2 Nov 2026 |
| 15 | WMG-Suno settlement: licensed models 2026, downloads need paid account, artist opt-in, Songkick | INFERRED | https://www.musicweek.com/labels/read/warner-music-group-settles-lawsuit-and-signs-ai-licensing-deal-with-suno/093129 | 26 Nov 2025 |
| 16 | No Suno primary page lists languages or rates Hindi | CONFIRMED (absence) | https://suno.com/blog/v5-5 | 26 Mar 2026 |
| 17 | Udio: audio, video and stem downloads disabled after UMG partnership (29 Oct 2025) | CONFIRMED | https://help.udio.com/en/articles/12683565-changes-associated-with-the-universal-music-group-umg-partnership | 17 Feb 2026 |
| 18 | Udio changelog has no 2026 entries | CONFIRMED | https://help.udio.com/en/articles/10748731-changelog-what-s-new-with-udio | page 28 Jan 2026 |
| 19 | Udio post-Oct-2025 music cannot be commercially distributed | INFERRED | https://dynamoi.com/learn/faqs/can-i-distribute-udio-music | 26 Apr 2026 |
| 20 | Udio walled garden; Warner also settled; 48 h download window | INFERRED | https://routenote.com/blog/udio-stops-user-downloads-after-umg-deal-heres-why/ | 24 Nov 2025 |
| 21 | Eleven Music v2.5/v2/v1; inpainting, Audio Reference (style only), Finetunes, 3 s-5 min | CONFIRMED | https://elevenlabs.io/docs/overview/capabilities/music | undated |
| 22 | Eleven Music languages: EN, ES, DE, JA named; Hindi not named | CONFIRMED | https://elevenlabs.io/docs/help-center/product/core-capabilities/music/what-is-eleven-music | undated |
| 23 | ElevenLabs free = no commercial licence (credit "Eleven Music"); paid = commercial; Beta = no commercial | CONFIRMED | https://help.elevenlabs.io/hc/en-us/articles/13313564601361-Can-I-publish-the-content-I-generate-on-the-platform | undated |
| 24 | Eleven Music launched with Merlin + Kobalt deals; no artist names or voice mimicry in prompts | INFERRED | https://musicbusinessworldwide.com/eleven-music-new-ai-rival-to-suno-launches-with-merlin-kobalt-licensing-deals-in-the-bag | 5 Aug 2025 |
| 25 | ElevenMusic app: remix + earn on platform | CONFIRMED | https://elevenlabs.io/blog/introducing-elevenmusic | 29 Apr 2026 (upd. 22 Sep 2026) |
| 26 | SynthV Studio 2 Pro $99, v2 voices $79, v1 Pro upgrade $49, perpetual, no GPU needed, VST/AU/AAX | CONFIRMED | https://dreamtonics.com/announcing-synthesizer-v-studio-2-pro/ | release 21 Mar 2025 |
| 27 | SynthV languages JA/EN/ZH (+ Korean in v2); Hindi not listed | CONFIRMED | https://dreamtonics.com/synthesizerv/ | undated |
| 28 | Spanish added to SynthV in a v1 update | INFERRED | https://www.soundonsound.com/node/4933676 | Jul 2025 |
| 29 | SynthV Voice-to-MIDI with "Transfer pitch onto converted notes", optional semitone rounding | CONFIRMED | https://dreamtonics.com/?p=4669 | undated |
| 30 | A new SynthV language needs a partner company; Cantonese was "coming soon" | CONFIRMED (forum) | https://forum.synthesizerv.com/t/topic/8137/2 | undated |
| 31 | ACE Studio 2.0 Artist Lifetime $398, 2,500 credits/mo for 2 years, 160+ voices, internet needed, Win10 64-bit | CONFIRMED (reseller) | https://www.pluginboutique.com/products/15411-ACE-Studio-2-0-Artist-Lifetime-License | read 2 Nov 2026 |
| 32 | ACE Studio languages EN/ES/ZH/JA (IT/FR/PT/KO soon); homepage "8 languages"; no Hindi | CONFIRMED | https://acestudio.ai/ | read 2 Nov 2026 |
| 33 | ACE Vocal to MIDI: lyrics per note, "Use Original Pitch", V1 EN/ES/ZH/JA, V2 more, "MIDI only" for others | CONFIRMED | https://docs.acestudio.ai/ai-tools/vocal-to-midi | undated |
| 34 | ACE built-in voices royalty-free for commercial projects | CONFIRMED | https://acestudio.ai/ | read 2 Nov 2026 |
| 35 | OpenUtau runs DiffSinger; DirectML runner for a discrete GPU on Windows | CONFIRMED | https://github.com/stakira/OpenUtau/wiki/DiffSinger-support | undated |
| 36 | No Hindi DiffSinger voicebank found | INFERRED (absence) | (search) | 2 Nov 2026 |
| 37 | Applio: MIT, commercial use with rights, no longer frequent updates | CONFIRMED | https://github.com/IAHispano/Applio | read 2 Nov 2026 |
| 38 | Applio desktop: "supported AMD configurations"; old HIP/ZLUDA recipes may conflict | CONFIRMED | https://applio-docs.pages.dev/getting-started/installation | undated |
| 39 | Applio ZLUDA guide lists gfx1101 with HIP SDK 5.7.1; 15-20 min first compile | CONFIRMED (mirror) | https://huggingface.co/spaces/jlopez00/tts-service/blob/main/assets/zluda/README.md | undated |
| 40 | Applio training docs give no minimum minutes; ask for clean, varied audio | CONFIRMED | https://applio-docs.pages.dev/getting-started/training | undated |
| 41 | Seed-VC archived 21 Nov 2025, GPL-3.0, 44k f0 singing model, fine-tune on 1-30 s clips | CONFIRMED | https://github.com/Plachtaa/seed-vc | archived 21 Nov 2025 |
| 42 | YingMusic-SVC: Seed-VC-based zero-shot SVC robust to harmony/backing; code MIT, weights licence unstated | CONFIRMED | https://github.com/GiantAILab/YingMusic-SVC | 25-26 Nov 2025 |
| 43 | YingMusic-SVC paper (GiantNetwork, Tsinghua) | CONFIRMED | https://arxiv.org/html/2512.04793v1 | 4 Dec 2025 |
| 44 | Kits artist voices: personal licence default; commercial needs artist approval + revenue share + publishing info | CONFIRMED | https://app.kits.ai/static/legal/artist-model-license.pdf | undated |
| 45 | Kits paid plans from $9.99/mo | CONFIRMED | https://kits.ai/blog/voice-artist-library-faq | undated |
| 46 | Melodyne 5: Essential $99, Assistant $249, Editor $399 (DNA), Studio $699 | CONFIRMED (order-matched) | https://shop.celemony.com/cgi-bin/WebObjects/CelemonyShop.woa | read 2 Nov 2026 |
| 47 | AutoTune Unlimited $30/mo or $300/yr | CONFIRMED | https://www.antarestech.com/blog/autotune-evolves-new-pricing-structure | eff. 4 Apr 2025 |
| 48 | AutoTune lineup: Advanced, Pro 11 (Graph Mode), AutoTune 2026, AutoKey 2 | CONFIRMED | https://www.antarestech.com/products/pitch-correction | ©2026 |
| 49 | Graillon 3.2 free edition has pitch correction; full $29; Win/Mac/Linux | CONFIRMED | https://auburnsounds.com/products/Graillon.html | read 2 Nov 2026 |
| 50 | MAutoPitch is free (MFreeFXBundle), has formant shift | CONFIRMED | https://www.meldaproduction.com/MAutoPitch | read 2 Nov 2026 |
| 51 | ACE-Step 1.5: MIT; cover, repaint, reference audio, Vocal2BGM, stems; LoRA "8 songs, 1 hour on 3090" | CONFIRMED | https://github.com/ACE-Step/ACE-Step-1.5 | read 2 Nov 2026 |
| 52 | ACE-Step: 50+ languages, Hindi not named; ROCm on Windows needs Python 3.12; ROCm .bat launchers | CONFIRMED | https://github.com/ACE-Step/ACE-Step-1.5 | read 2 Nov 2026 |
| 53 | ACE-Step limitations: multilingual lyrics need work; vocals "coarse"; seed sensitivity | CONFIRMED | https://ace-step.github.io/ace-step-v1.5.github.io | undated |
| 54 | ACE-Step 1.5 XL: 4B DiT, base/sft/turbo; >=12 GB with offload + INT8, >=20 GB without | CONFIRMED | https://huggingface.co/ACE-Step/acestep-v15-xl-base | XL released 2 Apr 2026 |
| 55 | ACE-Step XL in ComfyUI, MIT, licensed + royalty-free + synthetic training data | INFERRED (Comfy blog) | https://blog.comfy.org/p/ace-step-15-xl-commercial-grade-music | 17 Apr 2026 |
| 56 | Spotify: vocal impersonation only with the artist's authorisation; AI use allowed | CONFIRMED | https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/ | 25 Sep 2025 |
| 57 | Spotify DDEX AI credits (vocals/instrumentation/post-production), not used to downrank; spam filter | CONFIRMED | https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/ | 25 Sep 2025 (beta 16 Apr) |
| 58 | Spotify "AI Persona" badge: AI-identity artists excluded from recommendations; AI-assisted humans not labelled | CONFIRMED | https://newsroom.spotify.com/2026-08-13/presentamos-una-nueva-etiqueta-para-identificar-perfiles-de-artistas-generados-por-ia/ | 13 Aug 2026 |
| 59 | YouTube: disclose AI music that is the main focus; own-voice clone for VO/dubs exempt; player label | CONFIRMED | https://support.google.com/youtube/answer/14328491?hl=en | undated |
| 60 | YouTube music disclosure: Fully / Partly / No Gen AI; pitch correction + AI mastering = No Gen AI; DDEX ERN 4.3.2+ / CSV / Studio | CONFIRMED | https://support.google.com/youtube/answer/17124251?hl=en | undated |
| 61 | DistroKid AI question: lyrics / music / all audio / part audio; AI-persona question; pitch correction exempt | INFERRED | https://jackrighteous.com/blogs/ai-music-distribution-guide/spotify-ai-credits-distrokid-ai-music-uploads | reviewed 25 Oct 2026 |
| 62 | TuneCore/Believe: no 100% AI content; AI-assisted with human vocals case by case | INFERRED | https://dynamoi.com/learn/ai-music-distribution/does-tunecore-accept-ai-music | 28 Oct 2026 |
| 63 | Deezer: fully AI tracks labelled, excluded from Flow, recommendations and editorial; up to 85% of AI streams demonetised as fraud | CONFIRMED | https://www.deezer.com/explore/en-us/features/ai-labelling/ | figures to Apr 2026 |
| 64 | Applio ZLUDA guide's gfx list includes gfx1101; RX 7800 XT = gfx1101 | INFERRED (GPU id from general knowledge, not read this session) | https://huggingface.co/spaces/jlopez00/tts-service/blob/main/assets/zluda/README.md | undated |
