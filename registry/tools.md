# Tool registry

Every outside tool, Claude plugin, skill pack and MCP server we have looked at. Verdict meanings: GROWTH.md.
Facts checked 2 Nov 2026 unless the row says otherwise. Repos studied for the design, creator, study and workflow
plugins, with what was adopted and why the rest was not: `UPGRADES.md`. `recheck` = when a TRIAL/WATCH row is due for a fresh look.

## Music
Facts and sources: research/03_vocal_tools.md (vocals), research/04_production_and_video.md (production, video).
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| Synthesizer V Studio 2 Pro | vocal synthesis; Voice-to-MIDI turns his sung guide into notes and keeps his pitch curve; $99 + $79 a voice | per voicebank licence (in app) | Windows, no GPU needed | TRIAL (route B default for English; no Hindi) | 2026-12-01 | dreamtonics.com |
| ACE Studio 2.0 | vocal synthesis, Vocal to MIDI with original pitch, 160+ voices, voice cloning; $398 lifetime | built-in voices royalty-free commercial | Windows, internet required | TRIAL (route B alternative; Hindi lyrics not sung) | 2026-12-01 | acestudio.ai |
| OpenUtau + DiffSinger | free vocal synthesis | MIT (OpenUtau); voicebanks vary | Windows, DirectML runner | TRIAL (free route B; no Hindi voicebank found) | 2026-12-01 | github.com/stakira/OpenUtau |
| Applio (RVC) | voice conversion of a pitch-fixed guide into a voice he owns or licensed | MIT | Windows; AMD via ZLUDA (gfx1101 listed, HIP SDK 5.7.1) | TRIAL (route A; "no longer receives frequent updates") | 2026-12-01 | github.com/IAHispano/Applio |
| YingMusic-SVC | singing voice conversion that handles backing and harmonies (built on Seed-VC, Dec 2025) | code MIT; weights licence not stated | GPU | WATCH (until the weights licence is stated) | 2026-12-01 | research/03 §5 |
| Seed-VC | zero-shot singing voice conversion | GPL-3.0; archived 21 Nov 2025 | GPU | SKIP (archived; YingMusic-SVC is the successor to watch) | - | github.com/Plachtaa/seed-vc |
| Kits.ai artist voices | licensed artist voice models | personal use until the artist approves each track, then a revenue share | cloud | WATCH | 2027-01-01 | kits.ai |
| Melodyne 5 | note-level pitch and timing correction; Essential $99 to Studio $699 | commercial | Windows | TRIAL (route A pitch fix; pitch correction is "No Gen AI" on YouTube) | 2026-12-01 | celemony.com |
| Graillon 3 (free) / MAutoPitch | free pitch correction | free | Windows plugin | TRIAL (free route A pitch fix) | 2026-12-01 | auburnsounds.com, meldaproduction.com |
| Suno v6 (Sep 2026) | full songs; Voices clones HIS singing timbre; cover of uploads; Studio 2.0 audio-to-MIDI and stems; Suno MCP (beta) | free plan: Suno owns output, non-commercial; Pro $8 / Premier $24: he owns, 20 / 60 downloads a month | cloud | TRIAL (route C demos; paid plan only for anything released; Hindi untested) | 2026-12-01 | suno.com |
| Udio | song generation | downloads disabled since the UMG deal (17 Feb 2026) | cloud | SKIP (no file export, can't release) | 2027-01-01 | udio.com help |
| ElevenLabs Music v2.5 | prompt-to-song; reference audio shapes style only (won't keep his melody) | paid plans commercial; free must credit, non-commercial | cloud | WATCH (no Hindi named, no melody input) | 2027-01-01 | elevenlabs.io |
| ACE-Step 1.5 / XL | local generation: cover, repaint, reference audio, Vocal2BGM, LoRA on ~8 songs | MIT | ROCm on Windows (Python 3.12); XL 12 GB+ with offload and INT8 | TRIAL (arrangement and backing around a real vocal; its own docs call vocals "coarse") | 2026-12-01 | github.com/ACE-Step/ACE-Step-1.5 |
| REAPER + reaper-mcp-server (bonfire-systems) | Claude builds, renders and measures a mix (~60 tools incl. render and loudness analysis); REAPER $60 | MIT (server) | Windows, python-reapy | TRIAL (default DAW stack; test on a scratch project) | 2026-12-01 | pypi.org/project/reaper-mcp-server |
| Ableton MCP (`ahujasid/ableton-mcp`) | Claude drives Live: tracks, MIDI clips, instruments, arrangement; no render tool | MIT | Live 10+; telemetry on by default (`ABLETON_MCP_DISABLE_TELEMETRY=true`) | TRIAL (if he uses Ableton) | 2026-12-01 | github.com/ahujasid/ableton-mcp |
| flstudio-mcp | Claude writes notes in FL Studio via loopMIDI; can't load plugins or render | MIT, beta | FL 2025+ | WATCH | 2027-01-01 | research/04 §4 |
| Cakewalk by BandLab | free DAW | discontinued (renewals stopped Aug 2025) | Windows | SKIP | - | research/04 §4 |
| Waveform Free 13.5 | free DAW, no track/plugin/export limits | free | Windows | TRIAL (if REAPER is not wanted; no MCP) | 2027-01-01 | tracktion.com |
| Beat This! (CPJKU) | beats AND downbeats, state of the art without DBN | MIT code and weights | CPU or GPU (torch) | TRIAL (upgrade path for tools/beatmap.py downbeats; install on his PC) | 2026-12-01 | github.com/CPJKU/beat_this |
| librosa beat tracker | beats (no downbeats) | ISC | CPU | ADOPT (tools/beatmap.py, selftest median beat error 11 ms) | - | librosa.org |
| madmom | beat and downbeat tracking | code BSD; models CC BY-NC-SA (non-commercial) | CPU | SKIP (non-commercial models) | - | github.com/CPJKU/madmom |
| Spotify Basic Pitch | audio -> MIDI sketch (79.0 onset F on GuitarSet; best research model 91.2, unreleased) | Apache-2.0 | CPU (ONNX on Windows) | TRIAL (sketch only, clean by hand) | 2026-12-01 | github.com/spotify/basic-pitch |
| Klangio Guitar2Tabs | audio -> tab (Guitar Pro, MusicXML) | commercial | cloud | WATCH (only when tab is the deliverable) | 2027-01-01 | klang.io |
| python-audio-separator (BS-Roformer, Mel-Roformer) | best open vocal stems (Viperx-1297 vocals 12.9 SDR) | MIT code; each checkpoint its own licence | ROCm PyTorch preferred (DirectML falls back to CPU) | TRIAL | 2026-12-01 | github.com/nomadkaraoke/python-audio-separator |
| Demucs v4 (htdemucs_ft, htdemucs_6s) | multi-stem separation incl. guitar | MIT; unmaintained | GPU ~7 GB; not on DirectML | TRIAL (when drums/bass/guitar stems are needed) | 2026-12-01 | github.com/adefossez/demucs |
| Matchering 2.0 | reference-matched mastering (3rd of 12 in a 472-entry blind test) | GPL-3.0 | CPU | TRIAL (starting point only) | 2026-12-01 | github.com/sergree/matchering |
| Neural Amp Modeler | amp/cab captures | MIT | Windows plugin | TRIAL | 2026-12-01 | github.com/sdatkinson/neural-amp-modeler |
| TONE3000 plugin | free amp sim loading 700,000+ NAM captures and IRs (1 Sep 2026) | free, open source (licence not named) | Windows | TRIAL | 2026-12-01 | tone3000.com |
| Guitar Rig 7 Player | free amp sim with 2 amps, chorus/flanger, delay and reverb in one plugin; the quickest clean indie tone for a beginner in his DAW (gear-pick) | free, Native Instruments account | Windows VST3/AAX, standalone | TRIAL | 2027-01-08 | native-instruments.com/products/guitar-rig-7-player |
| EVER (Extended Video Export Revived) | high-quality GTA video export | unknown | GTA/FiveM | WATCH (anti-cheat risk unknown; never on a live server without staff OK) | 2027-01-01 | research/04 §7 |

## Distribution
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| DistroKid | distribution; accepts AI-assisted with 100% rights, no impersonation, AI box ticked; USD 24.99+ a year, splits | commercial | web | TRIAL (default if the vocal route uses AI; check its AI page on release week) | 2026-12-01 | research/05 §2 |
| CD Baby | distribution | refuses any AI content | web | SKIP (for AI-assisted songs) | - | research/05 §2 |
| TuneCore | distribution | AI only if every tool trained on fully licensed data | web | WATCH | 2027-01-01 | research/05 §2 |
| Amuse / RouteNote | distribution; RouteNote Free keeps 85% | AI accepted but skips Content ID | web | TRIAL (budget option; no Content ID for AI releases) | 2027-01-01 | research/05 §2 |

## Design
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| anthropics/skills (frontend-design, canvas-design, brand-guidelines, theme-factory, algorithmic-art) | craft guidance for layouts, posters and generative art | Apache-2.0 for most skills | Claude Code plugin: `/plugin marketplace add anthropics/skills` | TRIAL | 2026-12-01 | github.com/anthropics/skills |
| HTML/SVG + Playwright render | exact-text, editable posters and covers rendered to PNG | - | cloud container or PC | ADOPT (design skill, references/decks.md; the inspector renders in real Chrome) | - | - |
| rembg + BiRefNet (`birefnet-general-lite`) | clean cut-outs of characters from cartoon and CGI video frames | MIT (rembg), MIT (BiRefNet) | CPU, ~200 MB model on first use | ADOPT (design video.md §1.11b; beat isnet-general-use on green-on-green and glow edges, 2 Nov 2026) | - | github.com/danielgatis/rembg |
| yt-dlp with EJS (`--js-runtimes node --remote-components ejs:github`) | download public YouTube sections for references and frames | Unlicense | any, needs Node | ADOPT (creator reference-study; without the flags downloads fail "video not available", 2 Nov 2026) | 2026-12-01 | github.com/yt-dlp/yt-dlp/wiki/EJS |
| ComfyUI (already on his PC, ROCm) | local image generation for backgrounds/textures | GPL-3.0 | RX 7800 XT | TRIAL (behind the no-AI-slop check) | 2026-12-01 | github.com/comfyanonymous/ComfyUI |
| hallmark v2 (nutlope) | a page dealer for Persuade sites: 50 themes with a finished-page picture each, 21 page shapes, a job-first anatomy, 755 credited Wikimedia photos, `sloplint --before/--kept` so a redesign keeps every link, field and handler; checked 11 Nov 2026 (v2 of 10 Nov; v1 judged ideas only on 20 Oct); installed and run 11 Nov: plugin install adds no hooks, `sloplint --render` needs `puppeteer-core` via `HALLMARK_PUPPETEER` or it skips the render tier with only a last-line note | MIT | Node 18+, Chrome for `--render`; `/plugin marketplace add nutlope/hallmark` | TRIAL (companion for landing pages and site redesigns, below the design skill: house rules, tokens and checkers still win; leave `TOGETHER_API_KEY` unset, its image generation is a paid API; its photo library fetches from Wikimedia only) | 2027-01-01 | github.com/nutlope/hallmark |
| Astryx (Meta) | React 19 design system: 150+ accessible components, 7 themes, dark mode, templates, and an `astryx` CLI whose docs are written for coding agents to read (`astryx component --list`, `astryx docs`); checked 10 Nov 2026 | MIT, beta | npm `@astryxdesign/core` + theme + `@stylexjs/stylex`; needs React 19 | WATCH (none of his current builds has a React front end: the web apps are Gradio, the amp sim is JUCE; first choice of component kit if a project ships a React UI, still behind the design skill's rules) | 2027-02-01 | github.com/meta/astryx |

## Video
Facts checked 10 Nov 2026 (each repo's code read; earshot run on a 391-file licensed SFX bank). The owner's PC already has
a full video engine (EDL render, QA oracle, CLAP sound search, beats, mattes, motion graphics): call it before building
anything here (video-edit README, "The full engine").
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| raea ("Render Anything Engine") | React/TS compositions (Remotion-style API) drawn on the GPU: motion graphics, 3D (Bevy, glTF, splats), games, physics, local foley models; `raea check` (text in app UI zones, contrast, flashes, reading time, loudness), `raea cut` by speech | FSL-1.1-ALv2 (any use except a competing engine; Apache-2.0 after 2 years) | Windows x86_64 (least tested), DX12 or Vulkan GPU; Windows encode is CPU only, so render `--alpha` PNGs and encode with ffmpeg | TRIAL (the route to 3D layers, particles, springs and building charts; canary, changes daily: pin a release, bakeoff against HyperFrames on the PC first) | 2026-12-01 | github.com/shinyobjectz/raea |
| earshot | lets an agent hear audio: describe, match, rank files by a description, find moments in a long recording, real vs code-made, listening timeline sheet, launch-film critique, code-made SFX bank | MIT; CLAP + AST weights Apache-2.0 / BSD (~1.1 GB, CPU) | CPU, Python 3.10+, torch CPU | TRIAL (`find`: 10 of 19 sounds found in a 30-sound mix, the same as a plain CLAP window scan; `realness` too noisy for a gate: 5 of 20 code-made sounds read real; the code-made bank breaks the "real sounds only" rule; never feed it Sonniss files, their licence bans ML) | 2027-01-01 | github.com/Leonxlnx/earshot |
| huashu-art-motion | 36 painted art styles and 9 explainer grammars as code (brush/medium libs, v1.3 paints one scene in 16 styles), anti-slideshow gates (film_gate, storyboard_lint) | MIT | Node + headless Chrome | TRIAL (painted looks for music videos and personal edits; characters in its demos come from image models, so run the no-AI-slop blind check) | 2026-12-01 | github.com/alchaincyf/huashu-art-motion |
| argo | a Playwright web-app walkthrough turned into a narrated demo MP4: TTS (Kokoro, local), overlays, cursor ring, camera moves | MIT | Node, Chromium; Kokoro ~410 MB | TRIAL (demo videos of the owner's own web apps; narration is TTS, so voice-led channels keep his voice) | 2026-12-01 | github.com/shreyaskarnik/argo |
| Director (VideoDB) | chat agents that search, clip, summarise, dub and subtitle videos | MIT code, but every agent runs on VideoDB's paid hosted index | cloud | SKIP (paid key and raw footage uploaded to a third party; local transcripts + the engine's watch pack do the same search) | - | github.com/video-db/Director |

## Marketing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| coreyhaines31/marketingskills | ~40 marketing skills: copywriting, social, launch, ad-creative, marketing-psychology, ab-testing | MIT | `npx skills add coreyhaines31/marketingskills -a claude-code` | TRIAL (depth for campaign-plan; our voice rules win) | 2026-12-01 | github.com/coreyhaines31/marketingskills |

## Developer tools
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| Rune IDE (Unstable Build) | keyboard-driven, GPU-rendered IDE in Go with terminals, a REPL, a debugger and its own coding agent; open-sourced 12 Sep 2026; checked 10 Nov 2026 | GPL-3.0-or-later (extension SDK Apache-2.0) | macOS and Linux only, no Windows build or timetable | SKIP (his PC is Windows; first-class languages are Go and Python, C++ not listed; Claude Code is already the agent, Rune has no Claude Code or MCP hook) | 2027-03-01 | github.com/unstablebuild/rune |

## Arsenal plumbing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| skill-creator (claude-plugins-official) | write, test and tune skill descriptions | Anthropic | Claude Code plugin | ADOPT (already used in his other projects) | - | anthropics/claude-plugins-official |
