# Lessons from sirf-timepass (read-only reference, read 2 Nov 2026)

`NatikChhabra/sirf-timepass` is the owner's mature system for a YouTube channel (built over 1-2 months). We take its
patterns, not its content, and never write to it.

| Pattern there | Why it works | Arsenal version |
|---|---|---|
| CLAUDE.md "REPEAT RULES" table: each repeated owner instruction maps to the hook, script check or skill step enforcing it | stops him having to say things twice | CLAUDE.md standing instructions + GROWTH.md loop step 3 |
| `tool-change` skill + research/84 capability matrix for every repo he sends | full adoption, never cherry-picks | `tool-intake` skill + `registry/` |
| QUALITY.md self-scoring + blind review before anything reaches him | he judges finals, not drafts | `music-review`, `design-review` checklists |
| `selftest.py` guarding every gate | changes can't silently break old work | `scripts/validate.py` + CI (grows into real tests) |
| `beats.py` music map, `stems.py` vocal separation, research/83 lyric-MV pipeline | proven on his PC (AMD, DirectML/ROCm) | referenced by `music-video`, `guitar-capture`; rebuild here when music-video work starts |
| research/82 local-model setup (llama.cpp ROCm, ComfyUI ROCm, `F:\AI Models` layout) | his GPU works for local AI | `registry/local-models.md` |
| "No AI slop, not no AI" rule | AI allowed when a stranger can't tell | CLAUDE.md quality bar |
| Plugin marketplaces + `install_claude_tools.ps1` for user-scope installs | same tools in every project | this repo is itself a marketplace |
