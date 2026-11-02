# Vocal routes: tools, terms and what each really does (checked 2 Nov 2026)

Full sources and the claims table: research/03_vocal_tools.md. CONFIRMED = read on the vendor's own page.
INFERRED = secondary or our reasoning. Prices in USD as shown on 2 Nov 2026 (may be regional). Re-check before buying.

## The one question that sorts every tool: does it keep HIS melody?
| Tool | Keeps his exact melody? | Hindi lyrics? | Release terms |
|---|---|---|---|
| Synthesizer V Studio 2 Pro (Voice-to-MIDI) | yes: his sung guide becomes notes, "transfer pitch" keeps his glides | no (JP, EN, ZH, KO; ES, Cantonese in v1) | per voicebank licence, read in the app |
| ACE Studio 2.0 (Vocal to MIDI, "Use Original Pitch") | yes | no for lyrics ("MIDI only" mode carries the melody, the words won't be sung right) | built-in voices royalty-free for commercial use |
| Voice conversion (Applio/RVC, YingMusic-SVC) on a pitch-fixed guide | yes: the guide's pitch and timing pass straight through | yes (the guide is in any language) | only a voice he owns or has written permission for |
| His own vocal + pitch correction (Melodyne, Graillon free) | yes | yes | his voice: counts as "No Gen AI" on YouTube |
| Suno v6 cover of his guide (with his own Voices profile) | partly: adherence not documented, test it | test it (no Suno page rates Hindi) | paid plan only: he owns output; free plan: Suno owns it, non-commercial |
| Suno Add Vocals over his instrumental | no: writes its own melody | test it | paid plan only |
| ElevenLabs Music v2.5 | no: reference audio shapes style only | not named | paid plans commercial; free must credit, non-commercial |
| ACE-Step 1.5 / XL (local, MIT) | no for lead vocals (its own limits call vocals "coarse"); great for arrangement around a vocal (Vocal2BGM) | 50+ languages claimed, Hindi not named | MIT |
| Udio | n/a | n/a | downloads disabled since the UMG deal (help page 17 Feb 2026): not usable for release |

## Route A: guide + pitch fix + voice conversion (any language, his phrasing)
1. He sings or hums the guide over the guitar take, with the real words, in his phrasing. Pitch can be off.
2. Pitch-fix the guide to the melody: Melodyne (Essential $99 / Assistant $249 / Editor $399 / Studio $699) for note
   by note; free: Graillon 3.2 (free edition includes pitch correction) or MAutoPitch. Keep vibrato natural; hard-tune
   only as a style choice.
3. Convert the timbre with a model of a voice he OWNS or has WRITTEN permission for:
   - Applio (RVC): MIT, "no longer receives frequent updates". AMD: its ZLUDA guide lists gfx1101 (RX 7800 XT) with
     HIP SDK 5.7.1; the first run compiles silently for 15-20 min. Training data: docs give no minutes figure;
     community norm 10-30 min of clean, varied singing (INFERRED).
   - YingMusic-SVC (Dec 2025): open, built on Seed-VC, handles songs with backing and harmonies; code MIT, weights
     licence NOT stated (WATCH until it is). Seed-VC itself is archived (21 Nov 2025).
   - A model of HIS OWN voice copies his tone, and keeps whatever pitch the guide has: that is why step 2 comes first.
4. Kits.ai artist voices: personal use only until each track is approved by the artist, then a revenue share.
5. Disclosure: a converted lead vocal is at least "Partly Gen AI" on YouTube; label it.

## Route B: vocal synthesis (exact control, English and East Asian languages)
- Synthesizer V Studio 2 Pro: editor $99 one-time, v2 voices $79 each, runs without a GPU (Windows 8.1+).
  Voice-to-MIDI turns his sung guide into notes and lyrics; "Transfer pitch onto converted notes" keeps his slides
  (semitone rounding off by default). Then pick the voice, tune phonemes, breaths, vibrato, tension per phrase.
- ACE Studio 2.0: Artist Lifetime $398 (2,500 credits a month for 2 years, then a subscription), 160+ voices, internet
  required, built-in voice cloning and a choir mode.
- OpenUtau + DiffSinger: free; DirectML runner for an AMD GPU (INFERRED that AMD works). No Hindi voicebank found.
- The craft that makes a synth sound human: breaths before phrases, slight timing pushes and pulls against the grid,
  vibrato that starts late in long notes, consonant timing, varied note attacks. A flat, on-grid synth reads as AI.

## Route C: generate from his guitar (fast demos, sometimes the release)
- Suno v6 (9 Sep 2026; v6 and v6-wild paid, v6-mini free): Voices (Pro/Premier) clones HIS singing timbre from 15 s
  to 4 min of his singing with a spoken verification phrase; Cover/Extend/Remix of uploads; Suno Studio 2.0 (Premier)
  has audio-to-MIDI and stem export; Suno MCP (beta, 28 Oct 2026) can be driven from Claude.
  Downloads: 20 a month on Pro ($8), 60 on Premier ($24) from 3 Sep 2026. Free: 7 lifetime downloads, Suno owns them.
  Fully AI-made music may not be copyrightable; his own lyrics are his.
- ACE-Step 1.5 / XL (local, MIT, ROCm on Windows with Python 3.12 and its own launch scripts; XL 12 GB+ with CPU
  offload and INT8): cover, repaint, reference audio, Vocal2BGM; a LoRA on ~8 of his songs in ~1 h on a 12 GB card.
  Best use: arrangement ideas and backing around his real or converted vocal, not the lead.

## Route D: rap or spoken delivery in his own voice
No pitch needed. Rhythm, breath and diction carry it; record many takes and comp the best syllables.

## Route E: a real singer
An RP community singer or a hired session vocalist with the guide and lyric sheet. Credit them, get written consent for
the release, agree on any revenue split before recording.

## Release rules that bind every route (research/03 §8, research/05 §2)
- Spotify: AI tools allowed; impersonating an artist's voice needs their authorisation; AI credits go via the
  distributor (DDEX) and do not rank tracks down. The "AI Persona" badge removes artists whose identity is an
  AI-made photoreal person from all recommendations: keep a real human as the artist and use in-game or stylised art.
- YouTube: disclose AI music that is the main focus; his real vocal plus pitch correction is "No Gen AI"; a
  synthesised or converted lead is at least "Partly".
- Distributors: CD Baby refuses any AI content; TuneCore only if every tool trained on fully licensed data; Amuse and
  RouteNote accept but AI releases skip Content ID; DistroKid accepts with 100% rights, no impersonation and the AI box
  ticked (DistroKid, TuneCore and Deezer pages could not be read: check by hand before a release).
