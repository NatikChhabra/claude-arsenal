# Tools

Use when: running the design gate, or deciding which checker fits.

All checkers live under `${CLAUDE_SKILL_DIR}/tools/` (the skill folder printed as "Base directory" when it loads). Two are third-party MIT code, modified here; licences sit beside them and in the plugin's `NOTICE.md`. They read files and run a local headless browser. None call the network themselves. Need Node 22+. No Chrome on PATH (cloud containers): set `CHROME_PATH=/opt/pw-browsers/chromium` for `inspect.mjs`.

## Which one

| Situation | Run |
|---|---|
| Any HTML/CSS/JS/TSX edit | `lint.mjs` + `preflight.mjs` |
| Anything renderable (page, app screen, artifact HTML) | add `inspect.mjs` and open every screenshot |
| App/dashboard/tool screens | add `--app` to lint and inspect |
| HTML rendered into video or thumbnails (overlays, title cards, captions, motion graphics) | add `--video` to lint, preflight and inspect, then judge the rendered frames by `video.md` and `edit.md` |
| Finished stills and loops: thumbnails, posters, ads, in-game signs, covers, story frames, GIF/MP4 loops | `still_check.py --as <profile>` (0 FAIL), then the frame checks, feed test and blind readers in `video.md` / `ads.md`; rendered video also gets the video QC in `edit.md` |
| Anything that moves (entrances, rewards, game juice, idle loops, remote or key input) | add `motion.mjs` and open every sheet (`--tv` for anything shown on a television) |
| Code that can't render (fragments, templates) | lint + preflight only, and say so in the report |

## lint (static, zero deps)

```bash
node ${CLAUDE_SKILL_DIR}/tools/taste/lint.mjs <files|dirs ...> [--app] [--video] [--json]
```
- Banner: `DESIGN · LINT`. Exit codes: 0 clean, 1 any FAIL, 2 bad path.
- Scans: html, css, scss, less, js, jsx, ts, tsx, vue, svelte, astro, mdx. Skips node_modules, dist, build, dot-dirs (including `.design-check/`), `*.min.*`, files >4MB.
- FAIL: mono, gradients and gradient text, shadows, 01-09 numbering, eyebrow classes, tiny tracked uppercase, purple/violet/indigo, the Claude-palette hexes, emoji, lorem, hairlines.
- WARN: 1px outlined boxes, backdrop blur, buzzwords, generic CTAs, default fonts, `transition: all`, `ease-in`, `scale(0)`, `100vh`/`h-screen`, bounce/ping/pulse, `padStart(2, '0')` zero-padding, >4 em dashes outside comments.
- Does not read `.md` (only `.mdx`): run preflight on prose docs.
- `--app` drops hairlines, boxes, default fonts, CTA copy and `100vh`, downgrades mono, shadow, numbering and eyebrow to WARN, and adds placeholder-data FAIL plus Tailwind default status hexes WARN.
- `--video` (motion graphics rendered to video): `text-shadow` and `drop-shadow()` filters stop being findings (text over footage needs them; `-webkit-text-stroke` and `paint-order` are never flagged); any `box-shadow` still FAILs (a static scan can't tell rest from motion); the first gradient per file whose every stop is grey, black, white or transparent on one line passes as the scrim or vignette; `ease-in` is not reported at all, so check by eye that it sits only on exits; `scale(0)` stays a WARN (fine for particles). Everything else is unchanged.
- Escapes:
  - selectors under `[data-ui]` keep borders and shadows (interface fragments on pages);
  - `<pre>` and `<code>` keep mono;
  - a pinned brand palette or font that trips a colour or font rule (neon on near-black, a purple brand hue, a pinned heavy display face) gets `design-ignore` on its token line, naming the brand source;
  - a line with the comment `design-ignore` is skipped (the old `taste-skill-ignore` is still accepted). Use it only with a stated reason.
- Reads an optional `./.design-check/direction.json` (the old `./.taste-skill/direction.json` still works). `"kind": "app"` or `"kind": "video"` switches that mode on automatically.

## preflight (static, zero deps)

```bash
node ${CLAUDE_SKILL_DIR}/tools/preflight.mjs <files|dirs ...> [--video]
```
- Exit 0 clean (WARNs never fail), 1 on any hard violation or no arguments, 2 on a missing path. No banner: one `file:line  RULE  snippet` per hit, then a total. Node 22+.
- Skips `.git`, `node_modules`, `.design-check/`, `.taste-skill/` and `*.min.*` files; does not follow symlinks.
- Patched locally to also scan `.js` and `.mjs`. `.md` and `.mdx` files get only the two prose rules (em dash, spaced en dash), so reference docs that show a banned pattern don't trip it.
- `--video` (or `"kind": "video"` in `.design-check/direction.json`): `scale(0)` drops to a WARN (particles) and pure white is not reported (white text over footage); pure black still is.
- HARD:
  - em dashes;
  - `transition: all`;
  - `scale(0)`;
  - `outline: none` (or `outline-none`) on a selector with no `:focus-visible` ring when the file rings other selectors (no ring anywhere in the file is only a WARN);
  - z-index 999/9999;
  - `addEventListener('scroll'`;
  - gradient text;
  - side-stripe borders ≥2px;
  - `repeating-linear-gradient`;
  - `feTurbulence`;
  - custom cursors.
- WARN:
  - spaced en dash;
  - >3 font families;
  - too many tracked uppercase labels;
  - `100vh`;
  - z-index ≥1000 without tokens;
  - pure `#000`/`#fff`;
  - Google Fonts links (fine for prototypes and artifacts; self-host in production).
- Em dashes inside code comments and `.md` docs also trip it. Fix them anyway: the house rule bans em and en dashes in all visible text, and docs ship too.

## inspect (real browser)

```bash
node ${CLAUDE_SKILL_DIR}/tools/taste/inspect.mjs <url | path/to/index.html> [--app] [--video] [--widths 1440,768,390 | 1920x1080,1080x1920] [--allow rule,rule] [--out DIR] [--film] [--json]
```
- **Runs:**
  - Finds Chrome, Edge, Brave or Chromium (or `CHROME_PATH`), runs it headless over CDP, and serves local files on `127.0.0.1:<random>`.
  - The page may still load its own CDN assets.
  - Kills only the Chrome process it started (it marks its own profile with `design-check-owner.json`; profiles left by older runs are swept too).
  - Banner: `DESIGN · INSPECT`. Exit 0 with no FAIL, 1 with any FAIL, 2 on a missing file or no target.
  - `--widths` takes plain widths (heights: 1440x900, 1280x800, 1024x768, 768x1024, 390x844, 375x812, else 0.625 of the width) or `WxH` for an exact frame.
  - `--film` (desktop widths only, on by itself when `direction.json` lists `scenes`) also photographs the scroll every third of a screen into `<viewport>-film-NN.jpg` sheets.
  - `--allow` ids and `direction.json` `"allow"` lists drop those findings.
- **Writes:**
  - `.design-check/inspect/` in the current folder: `<viewport>-fold.jpg`, `<viewport>-page-NN.jpg`, `report.json`.
  - A temporary Chrome profile in the OS temp folder, removed on exit.
  - Delete `.design-check/` afterwards, or add it to `.gitignore` (projects that ignored the old `.taste-skill/` add the new name too).
- **Read the screenshots with the Read tool before saying anything about quality.** The numbers are a floor; the pictures are the judgement.
- **Measures:**
  - headline lines and hero word count;
  - eyebrows, mono, numbering, gradients, resting shadows, hairlines, boxes;
  - palette tells and contrast;
  - fonts and sizes, body size and contrast;
  - first-screen button, picture count, video;
  - centring and measure;
  - overflow and broken images;
  - focal point;
  - equal margins, lopsided sections, blank stretches, h1 presence and size, untitled sections, first-screen void, text too close to the edge;
  - title readable at 1.2s, covered text, moving-element count, empty screens, reduced-motion leaving text hidden.
- **`--app` swaps in app rules:**
  - sidebar >30% on phone;
  - heavy shadows and glass;
  - dark borders, >3 radii, icon chips;
  - left-aligned or proportional numbers;
  - chart hue count, colour share >12%;
  - placeholder data;
  - tiny text;
  - blocks above the fold;
  - card blank bands;
  - title >34px, figure ≥48px.
- **`--video` (or `"kind": "video"`):** text-shadow is allowed. Neutral scrims and vignettes pass in every mode; a coloured gradient still fails. Use it for overlay and title-card pages at the exact frame they render at (`--widths 1920x1080` or `1080x1920`).
- **Page-mode floors are Persuade taste:** ≥4 real pictures, ≥8 moving elements, video. For Read, Experience and Video surfaces, or a deliberately type-only page, pass `--allow few-pictures,still-page,no-footage` and say why in the report. A video overlay or title card is not a page: also allow `first-action,name-only-title`, which it trips by design (tested on a bare title card at 1920x1080 and 1080x1920: 0 FAIL). The picture and motion floors only run at widths ≥1100.
- **Ignore any `scripts/assets.mjs` advice in its output.** That fetcher was deliberately not vendored because it uses the network. Source images per the imagery order in `pages.md`.

## motion (real browser, frame by frame)

```bash
node ${CLAUDE_SKILL_DIR}/tools/taste/motion.mjs <url | path/to/index.html[#hash]> [--size 1920x1080] [--fps 10] [--seconds 6] [--at "ArrowDown@3.4,Enter@4.2,js:startMove()@2"] [--tv] [--out DIR] [--keep-frames]
```
- **What it is for:** motion.md §14 asks for motion reviewed frame by frame. This films the page on a virtual clock and lays the frames out as contact sheets (6 x 5 tiles, each stamped with its time), so an entrance, a reward or a key press can be judged beat by beat instead of from memory.
- **How the clock works:** a shim injected before the page's own scripts drives `setTimeout`, `setInterval`, `requestAnimationFrame`, `performance.now`, `Date.now` and every CSS and Web Animation from one clock that only moves between captures. Every frame is exactly on its beat and screenshots never jitter. Chrome's own virtual-time policy is not used: new headless stops painting while it is paused. Not virtualised: Workers, audio clocks, `document.timeline.currentTime`, and an animation the page itself paused (the shim drives it anyway).
- **Events:** `--at` fires keys (`ArrowDown`, `Enter`, `Escape`, `" "`, a letter) or `js:<expression>` (no commas) at page-clock seconds, for remote and keyboard paths, or to trigger an idle move on cue.
- **`--tv`:** also writes `tv-NN.jpg`, the same frames as an old television shows them: soft and with 5% overscan cut from every edge. Use it for any 10-foot surface (layout.md, experience.md §7).
- **Output:** `sheet-NN.jpg` (and `tv-NN.jpg`) in `--out` (default `.design-check/motion/`), plus every page error. Exit 0 clean, 1 on any page error, 2 on bad arguments. Full-size frames are kept only with `--keep-frames`.
- **Read the sheets for:** a frame where the focal point is hidden or covered; particles crossing text being read; a character squashed or stretched (SKILL.md, Characters); overshoot beyond the weight limits; a beat that lands with no visible cause; an entrance that leaves the first screen blank too long; anything still moving at rest that should not be.

## still_check (finished graphics, Python)

```bash
python ${CLAUDE_SKILL_DIR}/tools/still_check.py FILE [FILE ...] --as thumbnail|ad|ingame|cover|story \
  [--words "<exact words>"] [--title "<video title>"] [--numbers-ok "<where each number is true>"] \
  [--frame <real source frame>] [--vs <last pieces or rivals>] [--mock lineup.png] [--budget-mb 10] [--json]
python ${CLAUDE_SKILL_DIR}/tools/still_check.py --selftest
```
- Re-runs itself under `uv` with pillow, numpy, scipy and rapidocr-onnxruntime when they are missing (CPU, ~1 s a
  still); ffmpeg reads MP4/MOV/WEBM.
- Measures the graphic at the profile's real viewing sizes: headline height, fine print, word count, glyph contrast,
  one subject, focal regions, clutter, colourfulness and the oversaturated AI gloss, clipped or overlapping text,
  thumbnail-only rows (duration badge, TV top half, title repeat, faked platform UI), and slop (dashes, the banned
  words in `tells.md`, unsourced numbers, AI provenance, the AI palette vs `--frame`, dHash sameness vs `--vs`).
- Animations add: WCAG flashes, particle fields, whole-frame motion, the loop seam and the upload budget; the still rows
  run on the rest frame.
- A floor, not taste: calibrated on 290 real YouTube thumbnails, where no pixel feature separated winners from losers
  but the FAIL rate halved. The stranger read decides the idea. First real use: the rejected BBQ hiring poster scored
  4.9 (58-word wall FAIL; particle field, fine print, no subject, text on text and AI provenance WARN).
- `--mock` builds a line-up of ours among the `--vs` pieces (dark and light grounds) for a blind reader; the key is
  printed, never drawn.

## Other checks without a script

- **Raw values outside tokens** ("a raw value in a component is a second system"): list colours, radii and z-indexes
  set outside the token block, then move each into a token or justify it. CSS files: `grep -nE
  '#[0-9a-fA-F]{3,8}\b|rgba?\(|oklch\(|z-index:\s*[0-9]{3,}' <css files>` and ignore the hits inside `:root` /
  `[data-theme]` blocks; any `border-radius` or spacing value off the project's scale is the same finding (idea from
  educlopez/ui-craft `tokens_lint`, MIT; no code taken).
- **Contrast:** compute it with the WCAG formula, or use the browser's DevTools.
- **Fonts:** confirm the real font loaded with `document.fonts.check('16px "Face"')` in the page.
- **Reduced motion:** use the browser pane's emulation or `matchMedia` overrides; the reduced state must equal the finished state.
- **Real viewport:** when the product targets a specific screen (an Electron window, a 720px laptop, a phone), add that width to `--widths`.
- **Animation review:** see the Before | After | Why standard in `motion.md`; video motion is reviewed frame by frame per `edit.md`.
- **Thumbnails and covers:** `still_check.py` first, then the safe-zone check and blind readers in `video.md`.

## Not adopted (and why)

- **impeccable CLI and hooks:** its new-design step always calls their server, the hooks download and run a binary, and session hooks run unsandboxed. Its rules are folded into these references instead. If its 62-rule detector is ever wanted:
  - run a pinned version once with `DO_NOT_TRACK=1`, `npx impeccable@<pinned> detect --json <path|url>`;
  - never install its hooks;
  - never open Claude Code inside a clone of that repo (its `.claude/settings.json` hooks fire).
- **dembrandt extractor:** unpinned `npx -y`, a stealth anti-bot mode, and loose robots.txt handling. Extract design systems by hand (`systems.md`).
- **img2threejs installer:** an unpinned `@latest` install that edits `~/.claude/settings.json` permissions. The pipeline and gates are in `experience.md`.
- **The upstream `assets.mjs` / `draw.mjs` and an `upstream-drift.sh` script:** network or maintainer-only.
