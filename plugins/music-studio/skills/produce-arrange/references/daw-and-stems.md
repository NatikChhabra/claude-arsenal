# DAWs Claude can drive, and stem separation (checked 2 Nov 2026)

Sources: research/04_production_and_video.md §3-4. CONFIRMED = read on the project's own page.

## DAW + MCP (pick by what Claude must do)
| Stack | Build tracks/MIDI | Load plugins | Render | Measure loudness | Notes |
|---|---|---|---|---|---|
| REAPER + `reaper-mcp-server` (bonfire-systems, MIT, v0.4.0, 25 Oct 2026) | yes | yes (FX, presets) | yes (project, stems, regions) | yes (loudness, spectrum, clipping) | about 60 tools via python-reapy (enable REAPER's distant API with its ReaScript). **Default pick.** CONFIRMED (PyPI) |
| REAPER + `reaper-mcp` (nbdy, v1.4.0, 30 Oct 2025) | yes | yes | yes | not listed | 115+ tools, no release in 12 months; second choice. CONFIRMED (PyPI) |
| Ableton Live + `ableton-mcp` (ahujasid, MIT) | yes, strong MIDI sketching, arrangement view | browser items | **no render tool listed** | no | telemetry ON by default: set `ABLETON_MCP_DISABLE_TELEMETRY=true`. Live is paid |
| FL Studio + `flstudio-mcp` (MIT, beta) | yes via loopMIDI | **no** | **no** | no | FL 2025+; note writing armed per session from a piano-roll script |

- REAPER licence: $60 discounted (personal, or commercial under $20k a year gross), $225 commercial, 60-day full
  evaluation, free upgrades through v8.99. CONFIRMED (reaper.fm).
- Free DAWs on Windows: Cakewalk by BandLab is discontinued (renewals stopped Aug 2025); a free Sonar tier is NOT
  confirmed. Waveform Free 13.5: no track, plugin or export limits (secondary). No MCP server for Waveform found.
- Every MCP server above is third-party: install it through skill workflow tool-change (licence, telemetry, what it
  can touch), test on a scratch project, save before every Claude session in the DAW.

## Stems from a mix or a generated song
- Best open families for vocals: BS-Roformer and Mel-Roformer (python-audio-separator, MIT code:
  BS-Roformer-Viperx-1297 vocals 12.9 SDR, MelBand Roformer Kim 12.6). Demucs htdemucs_ft vocals 10.8; `htdemucs_6s`
  adds guitar and piano stems (piano weak). Demucs is unmaintained. Each checkpoint has its own licence: check it.
- MVSEP's leaderboard top (14.58 vocals SDR) is its own server models, not all downloadable.
- AMD on Windows: DirectML is weak here (RoFormer falls back to CPU on "DML allocator out of memory"; Demucs not
  supported). ROCm PyTorch (the RX 7800 XT, gfx1101, is on AMD's ROCm 7.14 matrix for Windows) is the better route,
  reusing the ComfyUI ROCm environment. Untested on his PC: test before relying on it.
