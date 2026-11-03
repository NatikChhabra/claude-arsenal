# Patterns to reuse (2 Nov 2026)

Proven patterns from the owner's other, mature Claude setups. We take the patterns, not the content.

| Pattern there | Why it works | Arsenal version |
|---|---|---|
| CLAUDE.md "REPEAT RULES" table: each repeated owner instruction maps to the hook, script check or skill step enforcing it | stops him having to say things twice | CLAUDE.md standing instructions, GROWTH.md loop step 3, workflow `working-rules` and `templates/CLAUDE.template.md` |
| a tool-change skill + a capability matrix for every repo he sends | full adoption, never cherry-picks | workflow `tool-change` (verdict + repo capability matrix) + `registry/` |
| QUALITY.md self-scoring + blind review before anything reaches him | he judges finals, not drafts | `music-review`, design `process.md` scoring + blind review, creator `final-review` |
| a selftest guarding every gate | changes can't silently break old work | `scripts/validate.py`, `skill_lint.py`, `test_hooks.py`, all in CI |
| a beat map, vocal stem separation and a lyric-MV pipeline | proven on his PC (AMD, DirectML/ROCm) | referenced by `music-video`, `guitar-capture`; rebuild here when music-video work starts |
| a local-model setup (llama.cpp ROCm, ComfyUI ROCm, one models root) | his GPU works for local AI | `registry/local-models.md` |
| "No AI slop, not no AI" rule | AI allowed when a stranger can't tell | CLAUDE.md quality bar |
| Plugin marketplaces + a user-scope install script | same tools in every project | this repo is itself a marketplace |
| a thumbnail gate measured at feed size (headline px, words, glyph contrast, focal, gloss, badge) + a dHash sameness check | stops unreadable or same-template cards before a reader sees them | design `tools/still_check.py`, now for posters, ads, in-game signs, covers and GIF loops too (3 Nov) |
| a watch pack: the whole render as one time-aligned text timeline with flags | Claude can't play video; this is how it watches a cut whole | video-edit `tools/watch.py` (3 Nov) |
