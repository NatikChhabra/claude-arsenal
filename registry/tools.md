# Tool registry

Every outside tool, Claude plugin, skill pack and MCP server we have looked at. Verdict meanings: GROWTH.md.
Facts checked 2 Nov 2026 unless the row says otherwise. `recheck` = when a TRIAL/WATCH row is due for a fresh look.

## Music
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| ACE-Step 1.5 (and 1.5 XL, Apr 2026) | local song generation with lyrics in 50+ languages; cover generation, repaint/edit, reference audio, track separation, Vocal2BGM, LoRA training on ~8 songs | MIT | AMD via ROCm 7.2 / ComfyUI on Windows; 2B turbo < 4-6 GB VRAM, XL 4B >= 12 GB with offload | TRIAL (first local generator to test on the RX 7800 XT; Hindi untested) | 2026-12-01 | github.com/ACE-Step/ACE-Step-1.5, amd.com blog 4 Feb 2026 |
| Suno | full songs from prompts; upload his guitar/audio as a starting point | commercial terms depend on plan, verify before release | cloud | TRIAL (fast demos) | 2026-12-01 | suno.com |
| ElevenLabs Music | prompt-to-song with vocals | verify plan terms | cloud | WATCH | 2026-12-01 | elevenlabs.io |
| Synthesizer V 2 / ACE Studio | vocal synthesis: draw notes, type lyrics, pro singer voices | paid, commercial use allowed per voice bank terms (verify) | Windows, CPU/GPU | TRIAL (route B) | 2026-12-01 | dreamtonics.com, acestudio.ai |
| OpenUtau + DiffSinger | free vocal synthesis editor + neural voices | MIT (OpenUtau); voice banks vary | Windows | TRIAL (free route B) | 2026-12-01 | github.com/stakira/OpenUtau |
| RVC / Applio | train a voice model, convert a guide vocal into it | MIT (Applio) | Windows; AMD support varies, verify | TRIAL (route A) | 2026-12-01 | github.com/IAHispano/Applio |
| Seed-VC | zero-shot singing voice conversion (v1.0 SVC model, 44.1 kHz) | GPL-3.0; repo archived 21 Nov 2025 | GPU recommended | WATCH (archived; use as reference, prefer a maintained fork) | 2027-01-01 | github.com/Plachtaa/seed-vc |
| Ableton MCP (`ahujasid/ableton-mcp`) | Claude drives Ableton Live: tracks, MIDI clips, instruments, arrangement, tempo | MIT | Live 10+, Python 3.8+, uv; telemetry on by default (set `ABLETON_MCP_DISABLE_TELEMETRY=true`) | TRIAL (if he uses Ableton) | 2026-12-01 | github.com/ahujasid/ableton-mcp |
| REAPER MCP servers | Claude drives REAPER | various | REAPER | WATCH (several young projects; pick one after a test) | 2026-12-01 | search "reaper mcp" |
| Spotify Basic Pitch | audio -> MIDI for his guitar parts | Apache-2.0 | CPU | TRIAL | 2026-12-01 | github.com/spotify/basic-pitch |
| UVR MDX-Net / Demucs | stem separation | MIT | CPU, DirectML/ROCm | ADOPT idea (already proven on his PC in another project) | - | github.com/Anjok07/ultimatevocalremovergui |
| Matchering | reference-matched mastering | GPL-3.0 | CPU | TRIAL (starting point only) | 2026-12-01 | github.com/sergree/matchering |
| Neural Amp Modeler | guitar amp/cab capture and playback | MIT | Windows plugin | TRIAL | 2026-12-01 | github.com/sdatkinson/neural-amp-modeler |

## Design
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| anthropics/skills (frontend-design, canvas-design, brand-guidelines, theme-factory, algorithmic-art) | craft guidance for layouts, posters and generative art | Apache-2.0 for most skills | Claude Code plugin: `/plugin marketplace add anthropics/skills` | TRIAL | 2026-12-01 | github.com/anthropics/skills |
| HTML/SVG + Playwright render | exact-text, editable posters and covers rendered to PNG | - | cloud container or PC | ADOPT (default method in `rp-graphics`) | - | - |
| ComfyUI (already on his PC, ROCm) | local image generation for backgrounds/textures | GPL-3.0 | RX 7800 XT | TRIAL (behind the no-AI-slop check) | 2026-12-01 | github.com/comfyanonymous/ComfyUI |

## Marketing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| coreyhaines31/marketingskills | ~40 marketing skills: copywriting, social, launch, ad-creative, marketing-psychology, ab-testing | MIT | `npx skills add coreyhaines31/marketingskills -a claude-code` | TRIAL (depth for campaign-plan; our voice rules win) | 2026-12-01 | github.com/coreyhaines31/marketingskills |

## Arsenal plumbing
| name | what it does for us | licence | runs on | verdict | recheck | source |
|---|---|---|---|---|---|---|
| skill-creator (claude-plugins-official) | write, test and tune skill descriptions | Anthropic | Claude Code plugin | ADOPT (already used in his other projects) | - | anthropics/claude-plugins-official |
