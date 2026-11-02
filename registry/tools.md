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
| ComfyUI (already on his PC, ROCm) | local image generation for backgrounds/textures | GPL-3.0 | RX 7800 XT | TRIAL (behind the no-AI-slop check) | 2026-12-01 | github.com/comfyanonymous/ComfyUI |

## Marketing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| coreyhaines31/marketingskills | ~40 marketing skills: copywriting, social, launch, ad-creative, marketing-psychology, ab-testing | MIT | `npx skills add coreyhaines31/marketingskills -a claude-code` | TRIAL (depth for campaign-plan; our voice rules win) | 2026-12-01 | github.com/coreyhaines31/marketingskills |

## Arsenal plumbing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| skill-creator (claude-plugins-official) | write, test and tune skill descriptions | Anthropic | Claude Code plugin | ADOPT (already used in his other projects) | - | anthropics/claude-plugins-official |
