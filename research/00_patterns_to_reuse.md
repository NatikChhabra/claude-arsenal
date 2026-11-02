# Patterns to reuse (2 Nov 2026)

Proven patterns from the owner's other, mature Claude setups. We take the patterns, not the content.

| Pattern there | Why it works | Arsenal version |
|---|---|---|
| CLAUDE.md "REPEAT RULES" table: each repeated owner instruction maps to the hook, script check or skill step enforcing it | stops him having to say things twice | CLAUDE.md standing instructions + GROWTH.md loop step 3 |
| a tool-change skill + a capability matrix for every repo he sends | full adoption, never cherry-picks | `tool-intake` skill + `registry/` |
| QUALITY.md self-scoring + blind review before anything reaches him | he judges finals, not drafts | `music-review`, `design-review` checklists |
| a selftest guarding every gate | changes can't silently break old work | `scripts/validate.py` + CI (grows into real tests) |
| a beat map, vocal stem separation and a lyric-MV pipeline | proven on his PC (AMD, DirectML/ROCm) | referenced by `music-video`, `guitar-capture`; rebuild here when music-video work starts |
| a local-model setup (llama.cpp ROCm, ComfyUI ROCm, `F:\AI Models` layout) | his GPU works for local AI | `registry/local-models.md` |
| "No AI slop, not no AI" rule | AI allowed when a stranger can't tell | CLAUDE.md quality bar |
| Plugin marketplaces + a user-scope install script | same tools in every project | this repo is itself a marketplace |
