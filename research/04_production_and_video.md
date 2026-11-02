# Production research: loudness, guitar capture, stems, DAWs, mastering, songwriting, GTA/FiveM video, photosensitivity

Research date: 2 Nov 2026. Tags: **CONFIRMED** = read on the cited page in this session. **INFERRED** = my reasoning, or read only on a secondary page. A claim marked "secondary" was read, but on a page that is not the platform or project's own.

Access notes: ffmpeg.org was blocked for curl, so the ffmpeg docs were read from the official FFmpeg GitHub mirror (`doc/filters.texi`). The GitHub API was blocked, so licences were read from each repo's raw LICENSE file. Star counts and push dates were **not** checked.

---

## 1. Loudness targets and measurement

| Platform | Normalisation target | True peak | Status |
|---|---|---|---|
| Spotify | -14 LUFS (ITU 1770). Premium users can pick Loud -11, Normal -14 or Quiet -19 | Below -1 dBTP. **Below -2 dBTP if the master is louder than -14 LUFS** | CONFIRMED (Spotify for Artists) |
| Apple Music | -16 LUFS (Sound Check, AES TD1008) | Apple asks for "at least 1 dB of headroom" and a check for inter-sample clipping (afclip) | -16 LUFS: secondary (MeterPlugs, Mar 2022). Headroom: CONFIRMED (Apple Digital Masters PDF) |
| YouTube | -14 LUFS (only turns loud songs down, per the article) | n/a | Secondary only (Production Advice). YouTube publishes no official LUFS figure that I could find |
| TikTok / Instagram | No official published target found | n/a | Not found. Only vendor and blog pages, which disagree |

Spotify details (CONFIRMED): albums are normalised as a unit; shuffled or playlist tracks are normalised one by one. The Loud setting adds a limiter at -1 dB (sample values) with 5 ms attack and 100 ms decay.

Apple Digital Masters (CONFIRMED): deliver 24-bit at the highest native sample rate. Do not upsample. Check the *encoded* file for clipping too, because "levels that don't show overs on PCM can still cause clipping when encoded".

**Practical target (INFERRED):** master to about -14 to -10 LUFS integrated with a true-peak ceiling of -1 dBTP, or -2 dBTP when louder than -14 LUFS (Spotify's rule). Every platform turns loud masters down, so extra loudness gains nothing. The extra peak headroom protects the lossy encodes.

### ffmpeg commands (option names, ranges and defaults CONFIRMED from FFmpeg `doc/filters.texi`)

**Measure only (EBU R128 integrated loudness, LRA and true peak):**
```
ffmpeg -hide_banner -nostats -i song.wav -af ebur128=peak=true:framelog=quiet -f null -
```
- The summary at the end of the output gives I (LUFS), LRA, and True peak (dBFS = dBTP).
- `peak=true` measures on an oversampled signal (logged as TPK).
- The ebur128 default `target` is -23 LUFS. That only affects the visual graph, not the measurement.

**loudnorm, pass 1 (analyse):**
```
ffmpeg -hide_banner -i song.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2> pass1.log
```
Read `input_i`, `input_tp`, `input_lra`, `input_thresh` and `target_offset` from the JSON block.

**loudnorm, pass 2 (apply):**
```
ffmpeg -i song.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:measured_I=<input_i>:measured_TP=<input_tp>:measured_LRA=<input_lra>:measured_thresh=<input_thresh>:offset=<target_offset>:linear=true:print_format=summary -ar 48000 out.wav
```

loudnorm defaults and gotchas (CONFIRMED from filters.texi):
- Defaults: I=-24, LRA=7, TP=-2, `linear`=true. `print_format` defaults to none.
- `linear` needs all four `measured_*` values. It falls back to **dynamic** mode if the target LRA is lower than the source LRA, or if the gain would push the true peak over the target TP.
  - INFERRED consequence: for a mastered song, set LRA at least as high as the measured LRA, or use a limiter first.
- Dynamic mode upsamples to 192 kHz. Always set `-ar` explicitly.
- `dual_mono=true` for mono files meant for stereo playback.
- The command pattern was also read on a secondary page (dev.to).
- INFERRED: for music, a real limiter in the DAW, followed by ebur128 *measurement*, beats loudnorm's dynamic mode. Dynamic mode is a compressor/AGC and changes the mix. Use loudnorm only in linear mode, as a trim.

---

## 2. Guitar capture

### Spotify Basic Pitch (CONFIRMED, GitHub README + LICENSE)
- **Licence:** Apache-2.0 (Copyright 2022 Spotify AB).
- **What it does:** polyphonic, "instrument-agnostic" audio-to-MIDI with pitch bends. It "works best on one instrument at a time".
- **Platforms:** Windows, macOS and Ubuntu. The README lists Python 3.7 to 3.11. ONNX is the default runtime on Windows.
- **CLI:** `basic-pitch <output-dir> <input-audio>`
  - Flags: `--sonify-midi`, `--save-model-outputs`, `--save-note-events` (CSV), `--model-serialization`.
  - Python: `from basic_pitch.inference import predict`, which returns `model_output, midi_data, note_events`. It takes min/max frequency limits.
- **Accuracy on guitar:** the GAPS paper (arXiv 2408.08653) reports Basic Pitch at **79.0 onset-only F-measure on the GuitarSet test split**.
  - The best model in that paper reaches 91.2.
  - The GAPS weights are **not released** ("carefully considering whether to make our model weights freely available").
  - CONFIRMED (paper).
- **Output:** MIDI only, no tab. INFERRED: string/fret assignment needs a separate step.

### Better or tab-producing options (2025-2026)
- **TART** (arXiv 2510.02597, Oct 2025): technique-aware audio-to-tab. Pipeline: audio to MIDI, technique classifier, string/fret Transformer, tab. The abstract shows **no code or licence**. CONFIRMED (abstract).
- **High-resolution guitar transcription** (Riley, Edwards, Dixon, QMUL): adapts the Kong piano model to solo guitar and outputs MIDI. The page claims state of the art zero-shot on GuitarSet but gives **no numbers and no code link**. CONFIRMED (project page).
- **gtrsnipe:** converts MIDI to and from ASCII tab, ABC and Vex, with a "fledgling" audio-to-tab pipeline.
  - Licence is "other" plus a LICENSE-COMMERCIAL file. 38 stars, last push 18 Nov 2025.
  - CONFIRMED (ecosyste.ms mirror page, secondary).
- **Klangio Guitar2Tabs (commercial):** exports PDF tab/sheet, MIDI, MusicXML and Guitar Pro (.gp). The free demo covers the first 20 s; prices are not listed. CONFIRMED (klang.io).
- **Recommendation (INFERRED):** he plays guitar, so the reliable path is to record DI plus MIDI notes he already knows. Basic Pitch is a sketch tool for ideas: always clean the MIDI by hand. Use Guitar2Tabs only if tab export matters.

### Neural Amp Modeler and free amp sims
- **NAM plugin:** MIT licence (Steven Atkinson). VST3/AU on Windows 10 64-bit or later and macOS 10.15 or later. Pre-built installers come via neuralampmodeler.com/users. CONFIRMED (README + LICENSE).
- Known rough edge (CONFIRMED): NAM can crash before its GUI appears if Windows runs it on the wrong GPU. Fix: set NAM or the DAW to use the dedicated GPU.
- **TONE3000 plugin:** free, open source (the licence is not named on the page). Formats: VST3/AU/AAX/CLAP/LV2 plus standalone, with Windows support.
  - Launched 1 Sep 2026. It loads NAM captures and IRs from a library of more than 700,000 tones.
  - NAM A2 launched 2 Jun 2026.
  - CONFIRMED (tone3000.com blog).
- INFERRED: NAM or TONE3000 into a free cab IR covers amp sims at zero cost. Other free sims were not researched.

### Beat and tempo tracking

| Library | Licence | Notes | Status |
|---|---|---|---|
| **Beat This!** (CPJKU, `pip install beat-this`) | MIT for code **and** published weights | ISMIR 2024. Abstract: "surpasses the current state of the art in F1" without DBN post-processing. Gives beats **and downbeats**. CLI: `beat_this in.wav -o out.beats`. Python: `File2Beats(checkpoint_path="final0", device="cuda")`. Models: `final0-2` (~78 MB), `small0-2` (~8 MB). Uses CUDA if present, else CPU (`--gpu=-1` forces CPU). Weaker on hard or underrepresented genres and on continuity metrics | CONFIRMED (README, LICENSE, arXiv 2407.21658) |
| **madmom** | Code BSD-style; **model/data files CC BY-NC-SA 4.0 (non-commercial)** | DBNBeatTracker CLI. Beat This! README says the PyPI madmom only supports Python <3.10 and numpy <1.20; install from git | CONFIRMED (LICENSE, beat_this README) |
| **librosa** `beat.beat_track` | ISC | Dynamic-programming tracker (Ellis 2007): onset strength, then tempo, then peak picking. Beats only, no downbeats | Licence and method CONFIRMED (LICENSE.md, beat.py). "No downbeats" INFERRED from the API |

**Pick (INFERRED):** Beat This! for beat and downbeat maps for video cuts. It is the most accurate and its licence is clean for commercial use. madmom's models are NC, so avoid them on monetised work.
- ROCm PyTorch should run it on the RX 7800 XT. Not tested; see §3.

---

## 3. Stem separation (2026)

- **Demucs v4**, MIT licence:
  - Models:
    - `htdemucs` is the default.
    - `htdemucs_ft` is fine-tuned, "4 times more time but might be a bit better".
    - `htdemucs_6s` adds guitar and piano stems ("piano ... not working great").
    - The README quotes 9.00 dB SDR on MUSDB HQ, or 9.20 dB with sparse attention and fine-tuning.
  - **Not maintained:** the facebookresearch repo says "not maintained anymore". The adefossez fork is "officially maintained" but gets no new features.
  - Memory: about 7 GB of GPU RAM with default arguments. Use `--segment` to cut it (Hybrid Transformer models max 7.8 s).
  - CONFIRMED (both READMEs + LICENSE).
- **python-audio-separator** (nomadkaraoke), MIT: a CLI and library that runs UVR models.
  - `audio-separator in.wav --model_filename model_bs_roformer_ep_317_sdr_12.9755.ckpt` (default is `bs_roformer`). List models with `audio-separator -l --list_filter=vocals`.
  - Listed vocal SDRs:
    - BS-Roformer-Viperx-1297: vocals 12.9, instrumental 17.0
    - MelBand Roformer Kim: 12.6
    - htdemucs_ft: vocals 10.8
  - CONFIRMED (README).
- **UVR5 GUI:** code MIT. Credit UVR when using its models. CONFIRMED.
- **ZFTurbo Music-Source-Separation-Training** (the RoFormer training repo): MIT. CONFIRMED (LICENSE).
- **Leaderboard:** MVSEP Synth leaderboard, vocals SDR, top entries:
  1. BS Roformer (MVSep.com, 2025.07.20): 14.58
  2. MVSep Ensemble: 14.47
  3. Other BS-Roformer variants
  - The newest entry seen was "BS PolarFormer Vocals" (2026.05): 14.03.
  - **The top MVSEP entries are MVSEP's own server-side models**, not all downloadable. Of the open models, BS-Roformer and Mel-Roformer are the best-scoring families.
  - CONFIRMED (mvsep.com leaderboard.php). The Multisong leaderboard was not visible on the page I fetched.
- **AMD / Windows:**
  - audio-separator supports DirectML as "experimental / community-supported".
  - **RoFormer models fall back to CPU** on DirectML: "DML allocator out of memory", an upstream limit. `AUDIO_SEPARATOR_FORCE_DML_MDXC=1` tries the GPU anyway.
  - **Demucs is not supported on DirectML** (no fused LSTM).
  - The UVR GUI has a DirectML build "for AMD Radeon or Intel Arc" and says AMD GPU support is "limited".
  - CONFIRMED (READMEs).
- **ROCm on Windows:**
  - AMD blog, 24 Sep 2025: PyTorch on Windows is a **public preview** for Radeon 7000/9000.
  - The ROCm 7.14.0 compatibility matrix (page dated 2026-09-02) lists "AMD Radeon RX 7800 XT (gfx1101)" and says it "Applies to Linux and Windows".
  - CONFIRMED.
  - INFERRED: ROCm PyTorch is the best route for RoFormer and Demucs on his GPU. He already runs ROCm 7.2 via ComfyUI, so reuse that environment. DirectML is the fallback.
- **Pick (INFERRED):** BS-Roformer (Viperx 1297) or Mel-Roformer Kim for vocals; htdemucs_ft or htdemucs_6s when he needs drums, bass or guitar stems.
  - Check each model's own licence before release. The audio-separator MIT covers the code, not necessarily every third-party checkpoint.

---

## 4. DAWs Claude can drive

- **ahujasid/ableton-mcp** (MIT):
  - How it connects: a socket link between the MCP server and an Ableton Remote Script. Needs Live 10 or later.
  - Can:
    - Create MIDI and audio tracks and clips, and add notes.
    - Load instruments and effects from Ableton's browser.
    - Control tempo and transport.
    - Build full arrangements in Arrangement View.
  - Stated limits:
    - Complex arrangements may need to be broken into smaller steps.
    - Designed for default devices and browser items.
    - "Always save your work".
  - **Anonymous telemetry is ON by default**. Dataset recording is opt-in.
  - Install: `claude mcp add AbletonMCP uvx ableton-mcp` + `uvx --from ableton-mcp ableton-mcp-install-script`.
  - CONFIRMED (README + LICENSE).
  - Ableton Live is paid. Price not checked.
- **REAPER MCP servers** (all go through python-reapy, which needs REAPER's distant API enabled via a ReaScript):
  - `reaper-mcp-server` (bonfire-systems/reaper-mcp, Youssef Hemimy), MIT, v0.4.0, **25 Oct 2026**:
    - About 60 tools: projects, tracks, templates, MIDI, FX/presets, audio import/recording, mixing/automation, **rendering (project, stems, regions)**, mastering chain/limiter/normalisation, **analysis (loudness, spectrum, clipping)**.
    - CONFIRMED (PyPI).
  - `reaper-mcp` (nbdy/reaper-mcp), v1.4.0, 30 Oct 2025: "115+ tools across 13 categories". Supports stdio/sse/http/ws. CONFIRMED (PyPI).
  - INFERRED: bonfire-systems is the most complete *for this workflow*: it covers render plus loudness analysis and was released a week ago. nbdy has more tools but no release in 12 months. Test both on a scratch project.
- **FL Studio:** rosasynthesiz/flstudio-mcp, MIT, beta, needs FL Studio 2025+:
  - About 67 tools over a loopMIDI virtual MIDI link.
  - It **cannot load plugins or audio files or render audio** (FL API limit).
  - Note writing must be armed once per session from a piano-roll script.
  - CONFIRMED (GitHub page).
- **REAPER licence:**
  - $60 discounted: personal use, or commercial use under $20k a year gross revenue.
  - $225 commercial.
  - 60-day full evaluation. Free upgrades through v8.99.
  - CONFIRMED (reaper.fm/purchase.php).
- **Free DAWs (Windows):**
  - **Cakewalk by BandLab is discontinued.** In June 2023 BandLab announced a non-free Sonar successor. Licence renewals stopped in **Aug 2025**. Last release 2024.02.
    - CONFIRMED (Wikipedia).
    - A current free Sonar tier is NOT confirmed. Reverb's headline "Cakewalk is back and now it's free" was seen in search results and not read: verify before relying on it.
  - **Tracktion Waveform Free 13.5** (article dated 25 Aug 2025): no limits on tracks, plugins or exports, and no watermarks. CONFIRMED (Mixdown Mag, secondary).
- **Pick (INFERRED):** REAPER ($60) plus the bonfire reaper-mcp. It is the only stack here where Claude can both build and **render and measure** a mix. Ableton MCP is stronger for MIDI sketching but cannot render.

---

## 5. Mastering

- **Matchering 2.0:**
  - Licence: **GPL-3.0**. Fine for using the tool; it only matters if Claude *redistributes* modified code.
  - How it works: you give it a TARGET and a REFERENCE track. It outputs the target with the reference's **RMS, frequency response, peak amplitude and stereo width**, using its own open-source "Hyrax" brickwall limiter.
  - Ships as a Python library, Docker image and ComfyUI node, and is built into UVR5.
  - The README cites a Benn Jordan blind test (472 judged entries) placing it 3rd of 12, behind two professional engineers, "by carefully selecting a proper song as reference".
  - CONFIRMED (README + LICENSE).
- No other credible open-source automatic mastering project was found in this pass. One search returned only Matchering forks.
- **Standard chain (INFERRED, general practice):** corrective EQ, then gentle bus compression (1-2 dB gain reduction), then tonal EQ, then optional saturation and stereo width, then a true-peak limiter (ceiling -1 dBTP), then measurement (ebur128) and an encode check.
- **Pitfalls:**
  - From Sage Audio (secondary, CONFIRMED read):
    - Assuming louder means better.
    - Doing all the work with a limiter instead of compression.
    - Trusting analysers over ears.
    - Treating -14 LUFS as a rule rather than a guideline.
    - Using the same chain on every master.
  - From Spotify and Apple (CONFIRMED): inter-sample overs appear after lossy encoding, so check true peak on the **encoded** file.

---

## 6. Songwriting rules you can check

- **Intros shrank:** Léveillé Gauvin (OSU), *Musicae Scientiae*, top-10 songs 1986-2015.
  - Intros went from more than 20 s in the mid-1980s to about 5 s (a 78% drop).
  - The title arrives about 18% sooner.
  - Tempo rose about 8%.
  - CONFIRMED (OSU press release).
- **Time to first chorus (Hit Songs Deconstructed):**
  - Q2 2014, 23 Hot 100 top-10 songs: average **0:42, 19% into the song**.
  - 2017 Hot 100 top 10:
    - Pop reached the chorus at **0:39** average; hip-hop/rap at **0:30**.
    - Intros: pop **9 s**, hip-hop 17 s.
    - First verse: pop 23 s, hip-hop 44 s.
    - 86% of hip-hop songs had a chorus before the first verse by Q4 2017.
  - CONFIRMED (HSD report pages).
- **2024 counter-trend:**
  - Average top-10 length rose by more than 20 s to **3:40** (HSD, via TheMusic.com.au, Mar 2025).
  - Songs taking more than a minute to reach the chorus rose 23%, a decade high. The article did not clearly attribute this figure.
  - CONFIRMED (secondary).
- **Prosody (Pat Pattison):**
  - "prosody is created when all musical and lyrical elements work together to support the central message".
  - "stressed syllables occur in strong positions of the measure". Unstressed syllables go on weak beats.
  - Sources cited: Pattison, *Writing Better Lyrics* (2009, p.179) and *Songwriting: Essential Guide to Lyric Form and Structure* (Berklee Press 1991, pp.19-33).
  - CONFIRMED (Wikipedia "Lyric setting", citing Pattison).
- **Keppie Coutts (Berklee):**
  - Keep the language's natural stress.
  - Verbs usually take the stress.
  - Compound words stress the first syllable.
  - Pronouns and words ending in -ty or -ly are often mis-stressed in songs.
  - Break a rule only on purpose.
  - CONFIRMED (Berklee article).
- **Checkable rules (INFERRED from the above):**
  1. Vocal by about 0:10.
  2. First chorus or hook by 0:30 to 0:45, or put a pre-verse hook first for rap/hip-hop.
  3. Title stated in the chorus.
  4. Every stressed syllable lands on beat 1 or 3 (or 2/4 in half-time feel). Flag any unstressed syllable on a downbeat.
  5. Matching lines across verses keep the same syllable count and stress pattern, within about 1 syllable.
  - The ±1 syllable tolerance is my heuristic, not a sourced number.

---

## 7. GTA V / FiveM music videos

### Rockstar policy (CONFIRMED, support.rockstargames.com, last updated 10 Jan 2025): **IMPORTANT**
- The policy allows footage "for non-commercial uses". "'Non-commercial' means that you don't make money through the game footage you post or use the material as part of a promotion for a product or service."
- **"It does not apply to the exploitation of Rockstar IP for film, TV, or streaming distribution; in music videos; ..."** Those uses need a licence request to copyright@take2games.com.
- It forbids isolated cutscene and cinematic uploads, in-game TV and comedy clips posted in isolation, unauthorised mods, and third-party mod menus in GTA Online / RDO.
- The page says nothing about FiveM, roleplay or YouTube ad revenue.
- **INFERRED implication:** a GTA-footage *music video* of his own song, posted to Spotify Canvas or monetised YouTube, sits **outside** Rockstar's fan-video permission.
  - Options: keep music videos non-monetised and flag the risk, email copyright@take2games.com, or check the FiveM/Cfx terms and his server's rules (not researched here).
  - This needs his decision before any monetised release.

### Recording in FiveM
- The community standalone resource "Recording Clips" (Jan 2022) uses:
  - **F1** to start or save a recording
  - **F2** for action replay
  - **F3** to cancel
  - `/rockstareditor` to open the editor
  - Keys are rebindable in Settings > Key Bindings > FiveM.
  - CONFIRMED (forum.cfx.re).
- Servers expose the editor through natives (forum thread, Dec 2021; native names not shown). Some servers do not enable it. INFERRED: ask the server.
- Known issues seen in forum titles (not read): the editor gets stuck at "Downloading assets (0 of 4)" on FiveM clips, and crashes on some game builds.
- **EVER (Extended Video Export Revived):** fork of EVE, published 11 Mar 2026, with a FiveM how-to. Export details and anticheat status were not on the page. Treat as untested.

### Capture
- **YouTube recommended upload settings** (CONFIRMED, support.google.com/youtube/answer/1722171):
  - MP4 with fast start, H.264 High Profile 4:2:0, progressive, at the native frame rate.
  - SDR bitrates:
    - 1080p: 8 Mbps (24-30 fps), 12 Mbps (48-60 fps)
    - 1440p: 16 / 24 Mbps
    - 2160p: 35-45 / 53-68 Mbps
  - Audio: AAC-LC, 48 kHz, 384 kbps stereo.
- **OBS** (CONFIRMED, obsproject.com KB):
  - **Hybrid MP4** (OBS 30.2+) "remains recoverable even if writing the file is aborted". Chapter markers are the exception.
  - The Standard Recording guide recommends MKV with auto-remux to MP4.
  - Separate audio tracks can be recorded, which is useful for keeping game music off the final mix.
- **INFERRED settings for his RX 7800 XT:**
  - Record at 1440p60 or 2160p60 with AMD AMF HEVC or AV1 at a high constant quality (CQP about 16-20). Recording well above YouTube's upload bitrate leaves room for grading and 9:16 crops.
  - Record game audio and mic on separate tracks.
  - Uploading at 1440p gets the better YouTube codec. This is widely reported but not confirmed on a primary page.

### Beat-syncing
- **DaVinci Resolve:** "Detect Music Beats" (formerly "Show Music Beats") overlays beat indicators that cuts snap to. It is **Studio only** per the 21.1 manual (secondary: davinciresolveclub). Markers are added manually with M.
- **Pro method (INFERRED):**
  1. Make a beat/downbeat map with Beat This! (`.beats` TSV).
  2. Convert it to markers: an EDL, Resolve marker import, or a Premiere marker CSV.
  3. Cut on downbeats for section changes and big moves; cut on beats for montage; hold shots across the chorus phrase (4 or 8 bars).
  4. Hit visual accents on snare and transient onsets.
- Commercial aids found (not evaluated): BeatEdit for Resolve (aescripts), Premiere plug-ins.

### 9:16 specs
- **YouTube Shorts** (CONFIRMED, support.google.com/youtube/answer/15424877):
  - Up to **3 minutes**. Square or vertical aspect ratio.
  - **Shorts over 1 minute with an active Content ID claim are blocked globally**: no plays, recommendations or monetisation. Applies to uploads after 15 Oct 2024; for Official Artist Channels, uploads from 8 Dec 2025.
  - INFERRED: this matters for his own songs if a distributor registers them in Content ID. Whitelist his own channel at the distributor, or keep Shorts at 60 s or under.
- **Instagram Reels:**
  - Up to 3 minutes, announced by Adam Mosseri on 21 Jan 2025 (Lindsey Gamble, secondary).
  - Buffer (21 Jan 2025, secondary) says in-app recording goes to 20 minutes, uploads to 15, with 1080x1920 recommended.
  - Not confirmed on a Meta page.
- **TikTok:** no primary page read. Secondary pages report 1080x1920, 9:16 and uploads up to 10 or 60 minutes. INFERRED.
- **Safe zones:** no primary (Meta or TikTok) page read. Vendor guides commonly say to keep text out of about the top 14% and bottom 35% on Reels. INFERRED; verify in the app preview.

---

## 8. Photosensitivity

- **WCAG 2.3.1 (Level A):** nothing may flash "more than three times in any one second period", unless the flashes stay below the general and red flash thresholds.
  - General flash: opposing changes in relative luminance of at least 10% of max, with the darker image below 0.80.
  - Red flash: any opposing transition involving saturated red.
  - Area limit: 0.006 sr within any 10° field, about 25% of that field, about **341x256 CSS px**.
  - "based on existing specifications in use in the UK ... for television broadcast"; ITU-R BT.1702 is cited.
  - Tools: PEAT (Trace Center) and Harding FPA.
  - CONFIRMED (w3.org WCAG22 Understanding).
- **Ofcom Guidance Note on flashing images and regular patterns** (re-issued Jul 2001, amended Jun 2002):
  - Potentially harmful when there are **more than three flashes in any one second** AND the flashes cover more than a quarter of the screen.
  - A flash is an opposing luminance change of at least 20 cd/m² with the darker image below 160 cd/m².
  - **Any transition to or from saturated red is potentially harmful.**
  - Patterns: more than 5 light-dark stripe pairs. Stationary stripes over 40% of the screen, or moving ones over 25%, are restricted.
  - Cites Harding & Jeavons (1994) and Harding (1998).
  - CONFIRMED (Ofcom PDF).
- **Practical rule (INFERRED):** strobe and flash edits on beats stay at 3 or fewer full-frame flashes per second, avoid red flashes, and run a PEAT or Harding-style check on the final render. At 120 BPM, flashing on every 8th note is 4 per second and **fails**.

---

## Claims table

| # | Claim | Tag | Source URL | Date |
|---|---|---|---|---|
| 1 | Spotify normalises to -14 LUFS (ITU 1770). Premium Loud -11 / Normal -14 / Quiet -19 | CONFIRMED | https://support.spotify.com/artists/article/loudness-normalization/ | read 2 Nov 2026 |
| 2 | Spotify: true peak below -1 dBTP; below -2 dBTP if the master is louder than -14 LUFS | CONFIRMED | same | read 2 Nov 2026 |
| 3 | Spotify Loud limiter at -1 dB, 5 ms attack, 100 ms decay. Album normalisation keeps gain constant within an album | CONFIRMED | same | read 2 Nov 2026 |
| 4 | Apple Sound Check normalises to -16 LUFS (AES TD1008) | INFERRED (secondary) | https://www.meterplugs.com/blog/2022/03/23/apple-switch-to-lufs.html | 23 Mar 2022 |
| 5 | Apple: leave at least 1 dB headroom, check inter-sample clipping with afclip, deliver 24-bit at native rate | CONFIRMED | https://apple.com/itunes/docs/apple-digital-masters.pdf | undated PDF |
| 6 | YouTube plays music at about -14 LUFS (since 2019 per the update) | INFERRED (secondary) | https://productionadvice.co.uk/youtube-loudness/ | 2015, updated |
| 7 | No official TikTok or Instagram LUFS target found | INFERRED | searches only | 2 Nov 2026 |
| 8 | loudnorm defaults I=-24, LRA=7, TP=-2, linear=true. Linear falls back to dynamic if target LRA < source LRA or TP would be exceeded. Dynamic mode upsamples to 192 kHz; set -ar | CONFIRMED | https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/doc/filters.texi | master, read 2 Nov 2026 |
| 9 | ebur128 `peak=true` gives oversampled true peak (TPK). Default target -23 LUFS is for display only | CONFIRMED | same | same |
| 10 | Two-pass loudnorm uses input_i/tp/lra/thresh and target_offset fed back as measured_* plus offset | CONFIRMED (secondary + texi options) | https://dev.to/masonwritescode/two-pass-loudness-normalization-with-ffmpeg-loudnorm-the-right-way-1nm3 | read 2 Nov 2026 |
| 11 | Basic Pitch is Apache-2.0, polyphonic, instrument-agnostic, MIDI with pitch bends. CLI `basic-pitch <out> <in>`. ONNX default on Windows | CONFIRMED | https://github.com/spotify/basic-pitch | read 2 Nov 2026 |
| 12 | Basic Pitch scores 79.0 onset-only F on the GuitarSet test split; best in the GAPS paper 91.2; GAPS weights unreleased | CONFIRMED | https://arxiv.org/html/2408.08653v2 | 2024 |
| 13 | TART: audio-to-tab with techniques; no code or licence in the abstract | CONFIRMED | https://arxiv.org/abs/2510.02597 | 2 Oct 2025 |
| 14 | High-resolution guitar transcription (QMUL) outputs MIDI; no numbers or code on its page | CONFIRMED | https://xavriley.github.io/HighResolutionGuitarTranscription | read 2 Nov 2026 |
| 15 | gtrsnipe: MIDI to/from ASCII tab, early audio-to-tab; licence "other" + commercial file; last push 18 Nov 2025 | CONFIRMED (secondary mirror) | https://awesome.ecosyste.ms/projects/github.com%2Fscottvr%2Fgtrsnipe | read 2 Nov 2026 |
| 16 | Klangio Guitar2Tabs exports PDF/MIDI/MusicXML/Guitar Pro; free demo is 20 s | CONFIRMED | https://klang.io/guitar2tabs/ | read 2 Nov 2026 |
| 17 | NAM plugin MIT, VST3/AU, Windows 10+; GPU-selection crash workaround | CONFIRMED | https://github.com/sdatkinson/NeuralAmpModelerPlugin | read 2 Nov 2026 |
| 18 | TONE3000 free open-source NAM A2 plugin (VST3/AU/AAX/CLAP/LV2), launched 1 Sep 2026; more than 700k tones | CONFIRMED | https://www.tone3000.com/blog/tone3000-launches-free-nam-a2-plugin | 1 Sep 2026 |
| 19 | Beat This! code and weights MIT; beats and downbeats; beats prior SOTA F1 without DBN; CLI `beat_this` | CONFIRMED | https://github.com/CPJKU/beat_this , https://arxiv.org/abs/2407.21658 | ISMIR 2024 |
| 20 | madmom models CC BY-NC-SA 4.0 (non-commercial); code BSD-style; PyPI version Python <3.10 only | CONFIRMED | https://github.com/CPJKU/madmom (LICENSE) | read 2 Nov 2026 |
| 21 | librosa ISC licence; beat_track = Ellis 2007 dynamic programming | CONFIRMED | https://github.com/librosa/librosa | read 2 Nov 2026 |
| 22 | Demucs MIT; facebookresearch repo unmaintained; htdemucs_ft takes 4x the time, "a bit better"; htdemucs_6s adds guitar/piano; about 7 GB VRAM default | CONFIRMED | https://github.com/facebookresearch/demucs , https://github.com/adefossez/demucs | read 2 Nov 2026 |
| 23 | audio-separator MIT; BS-Roformer Viperx 1297 vocals SDR 12.9; htdemucs_ft vocals 10.8 | CONFIRMED | https://github.com/nomadkaraoke/python-audio-separator | read 2 Nov 2026 |
| 24 | audio-separator DirectML experimental; RoFormer falls back to CPU (DML OOM); Demucs unsupported on DML | CONFIRMED | same | same |
| 25 | MVSEP Synth vocals top: BS Roformer (MVSep) 14.58 (2025.07.20); BS PolarFormer 14.03 (2026.05) | CONFIRMED | https://mvsep.com/quality_checker/leaderboard.php | read 2 Nov 2026 |
| 26 | UVR GUI MIT; DirectML build for AMD; AMD support "limited" | CONFIRMED | https://github.com/Anjok07/ultimatevocalremovergui | read 2 Nov 2026 |
| 27 | AMD: PyTorch on Windows public preview for Radeon 7000/9000 | CONFIRMED | https://www.amd.com/en/blogs/2025/the-road-to-rocm-on-radeon-for-windows-and-linux.html | 24 Sep 2025 |
| 28 | ROCm 7.14.0 matrix lists RX 7800 XT (gfx1101); applies to Linux and Windows | CONFIRMED | https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html | 2 Sep 2026 |
| 29 | ableton-mcp MIT; socket + Remote Script; Live 10+; tracks/clips/devices/arrangement; telemetry on by default | CONFIRMED | https://github.com/ahujasid/ableton-mcp | read 2 Nov 2026 |
| 30 | reaper-mcp-server (bonfire-systems) MIT v0.4.0, about 60 tools incl. render + loudness analysis, via python-reapy | CONFIRMED | https://pypi.org/project/reaper-mcp-server | 25 Oct 2026 |
| 31 | reaper-mcp (nbdy) v1.4.0, 115+ tools, python-reapy | CONFIRMED | https://pypi.org/project/reaper-mcp | 30 Oct 2025 |
| 32 | flstudio-mcp MIT beta, FL 2025+, loopMIDI; cannot load plugins/audio or render | CONFIRMED | https://github.com/rosasynthesiz/flstudio-mcp | read 2 Nov 2026 |
| 33 | REAPER $60 discounted (personal, or under $20k/yr revenue), $225 commercial, 60-day eval, upgrades to 8.99 | CONFIRMED | https://www.reaper.fm/purchase.php | read 2 Nov 2026 |
| 34 | Cakewalk by BandLab discontinued; renewals ceased Aug 2025; Sonar successor "no longer free" | CONFIRMED | https://en.wikipedia.org/wiki/Cakewalk_by_BandLab | read 2 Nov 2026 |
| 35 | Waveform Free 13.5: no track, plugin or export limits | CONFIRMED (secondary) | https://mixdownmag.com.au/news/tracktion-releases-waveform-free-13-5-the-only-truly-unrestricted-free-daw | 25 Aug 2025 |
| 36 | Matchering GPL-3.0; matches RMS, FR, peak and stereo width to a reference; Hyrax limiter; in UVR5 | CONFIRMED | https://github.com/sergree/matchering | read 2 Nov 2026 |
| 37 | Common mastering mistakes: louder-is-better, over-limiting, analysers over ears, -14 as dogma | CONFIRMED (secondary) | https://www.sageaudio.com/articles/7-mastering-mistakes-we-all-make | read 2 Nov 2026 |
| 38 | Top-10 intros fell from >20 s (mid-80s) to about 5 s; title about 18% sooner; tempo +8% (1986-2015) | CONFIRMED | https://news.osu.edu/has-music-streaming-killed-the-instrumental-intro/ | 2017 |
| 39 | Q2 2014 top-10 hits: first chorus at 0:42 average (19% in) | CONFIRMED | https://reports.hitsongsdeconstructed.com/articles/hit-song-choruses/ | 2014 |
| 40 | 2017 top 10: pop chorus 0:39, hip-hop 0:30; intros pop 9 s / hip-hop 17 s | CONFIRMED | https://reports.hitsongsdeconstructed.com/?p=42302 | 2017 data |
| 41 | 2024 top-10 average length 3:40 (+20 s); songs with chorus after more than 1 min up 23% | CONFIRMED (secondary) | https://themusic.com.au/features/are-hit-songs-getting-longer-in-2025/qb0Xvby_vqE/18-03-25 | 18 Mar 2025 |
| 42 | Pattison: stressed syllables in strong positions of the measure; prosody = all elements support the message | CONFIRMED (Wikipedia citing Pattison 1991/2009) | https://en.wikipedia.org/wiki/Lyric_setting | read 2 Nov 2026 |
| 43 | Coutts (Berklee): keep natural stress; verbs stressed; compounds stress the 1st syllable | CONFIRMED | https://www.berklee.edu/berklee-now/news/berklee-riffs-natural-music-in-language | read 2 Nov 2026 |
| 44 | Rockstar allows only non-commercial footage (no money made); policy excludes music videos and film/TV/streaming distribution | CONFIRMED | https://support.rockstargames.com/articles/200153756/Policy-on-posting-copyrighted-Rockstar-Games-material | updated 10 Jan 2025 |
| 45 | FiveM community resource: F1 record/save, F2 action replay, F3 cancel, /rockstareditor | CONFIRMED | https://forum.cfx.re/t/standalone-recording-clips/4802881 | 15 Jan 2022 |
| 46 | EVER (Extended Video Export Revived) fork exists, with a FiveM how-to | CONFIRMED (details not read) | https://forum.cfx.re/t/how-to-use-extended-video-export-revived-ever-fivem/5390036 | 11 Mar 2026 |
| 47 | YouTube upload: MP4, H.264 High 4:2:0; 1080p60 12 Mbps, 1440p60 24, 2160p60 53-68; AAC-LC 48 kHz 384 kbps | CONFIRMED | https://support.google.com/youtube/answer/1722171 | read 2 Nov 2026 |
| 48 | OBS Hybrid MP4 (30.2+) recoverable after an aborted write | CONFIRMED | https://obsproject.com/kb/hybrid-mp4 | read 2 Nov 2026 |
| 49 | OBS guide recommends MKV with auto-remux; multi-track audio | CONFIRMED | https://obsproject.com/kb/standard-recording-output-guide | read 2 Nov 2026 |
| 50 | Resolve "Detect Music Beats" is Studio only | CONFIRMED (secondary) | https://davinciresolveclub.com/davinci-resolve-beat-detection/ | read 2 Nov 2026 |
| 51 | Shorts up to 3 min, square or vertical; Shorts over 1 min with a Content ID claim blocked globally (from 15 Oct 2024; OAC from 8 Dec 2025) | CONFIRMED | https://support.google.com/youtube/answer/15424877 | read 2 Nov 2026 |
| 52 | Reels up to 3 min (Mosseri, 21 Jan 2025) | CONFIRMED (secondary) | https://www.lindseygamble.com/blog/instagram-three-minute-reels | Jan 2025 |
| 53 | Reels: in-app recording 20 min, upload 15 min, 1080x1920 | INFERRED (secondary, conflicts with #52 framing) | https://buffer.com/resources/instagram-reels-length | 21 Jan 2025 |
| 54 | TikTok 1080x1920, uploads up to 10/60 min; Reels safe zone about top 14% / bottom 35% | INFERRED (no primary read) | vendor pages via search | n/a |
| 55 | WCAG 2.3.1: no more than 3 flashes per second unless below thresholds; 10% luminance change, darker below 0.80; red flash; about 341x256 px area | CONFIRMED | https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html | read 2 Nov 2026 |
| 56 | Ofcom: harmful if >3 flashes per second and >25% of screen; 20 cd/m² change with darker <160 cd/m²; saturated red always risky; stripe-pattern limits | CONFIRMED | https://www.ofcom.org.uk/__data/assets/pdf_file/0021/16248/gn_flash.pdf | Jul 2001 / Jun 2002 |
