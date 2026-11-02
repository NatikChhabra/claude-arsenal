---
name: rp-graphics
description: Make posters, flyers, cover art, event graphics and social posts for RP characters, businesses and music releases, as editable HTML/SVG rendered to PNG. Use for any visual asset after a brief exists.
---
# RP graphics

status: draft

## Approach
- Build designs as HTML/CSS or SVG (exact text, real fonts, brand tokens from BRAND.md), render to PNG with headless
  Chromium/Playwright at each needed size. Editable, versionable, no AI-garbled text.
- AI images (local ComfyUI on the owner's GPU, or a service) only for backgrounds or textures, and only when a blind
  viewer wouldn't call it AI. Real in-game screenshots first for RP content.
- Anthropic's `frontend-design` and `canvas-design` skills (anthropics/skills) are TRIAL inspirations for layout craft.

## Steps
1. Read the brief and the brand kit. 2. Three thumbnail-size concepts (layout + hierarchy only). 3. Pick one, build at full
size. 4. Render every size (16:9, 1:1, 4:5, 9:16, cover 3000x3000). 5. Run `design-review`. 6. Deliver PNG + source.
