# Colour

Use when: choosing or auditing a palette, writing colour tokens, theming light/dark, colouring status, data or photos, on any surface (page, app, game, deck).

## Decide before any hex

- Pick a strategy first, then colours. Write the system in one sentence the user can redirect cheaply ("bone ground, graphite ink, one bottle-green accent oklch(48% .11 160) on actions only").
- Hue comes from product meaning or the subject's own materials (its photo, its object, its place), never from a category association (blue = trust, green = money, mono = tech).
- Brand given: extract the real values (grep hex from its CSS, read the spec). Never recall brand colours from memory. Brand claimed but not attached: ask and stop. No brand: pick and bind it yourself.
- The brief, a project DESIGN.md or the user's stated dislikes beat every rule here. A pinned brand palette is kept even when it matches a tell (neon on near-black included), never with the glow added, and used on brand surfaces rather than as a default page look.
- This skill's owner: no red in UI (apps, dashboards, tools) unless asked; thumbnails, photos, album art, brand reaction art and a game's own death screen are exempt. His own tools default dark (pure black or near-black ground) and may use purple when he asks; the purple-blue AI gradient stays banned.
- Video, thumbnails and covers are not UI: their colour rules (colourfulness floor, separation from the feed, no gloss) live in `video.md`.
- Vary palettes across projects. Never converge on one house look.

| Strategy | What | Use |
|---|---|---|
| Restrained | Tinted neutrals + one accent | Operate floor, Read default |
| Committed | One saturated colour owns 30-60% of the surface, as whole regions | Persuade |
| Full palette | 3-4 named roles, each owning regions (60/30/10 across them) | Persuade, Experience, kids, games |
| Drenched | The surface is the colour | Posters, single-field pages, Experience |

- Colour commits at page scale: fields own regions. Scattered accents on a neutral template read as "the category default with a sticker".
- In Committed/Drenched, each field follows the proportion rule internally: field + its ink + nothing else.

## Roles and tokens

- Build roles, not swatches. Base set: `--bg --surface --ink --muted --accent --accent-ink`. Operate adds `--surface-2 --border --control --focus`, the status quartet and data slots. Persuade adds `--field-n` + `--field-n-ink` per section field.
- Two layers: primitives (ramps) + semantic aliases. Components reference semantic tokens only. Name by purpose (`--accent`), never by hue (`--blue-500`).
- A raw hex in a component is a second palette starting. A literal equal to a token is that token: replace it. More than ~12 raw hex values outside `:root` is drift; in product code the target is 0.
- No greys between roles. Quieter text is `--muted`; a quieter panel is `--surface`.
- Every text token carries a note naming the grounds it sits on ("body on bg and surface"); each pair passes in every theme.
- Accent fills get an `on-accent` (`--accent-ink`) token, never hard-coded white.
- Opacity is a state (disabled .4, loading .7, dragging .5), never a tint. Tints are real tokens. Never set opacity on an alpha background.
- Prefer explicit colours over translucent stacks so contrast never depends on what sits behind. The one alpha token is the modal scrim: canvas hue near-black at ~50% (`oklch(15% .02 var(--h) / .5)`).
- Every tone visibly distinct: two tokens that look alike merge into one.
- Token architecture, DESIGN.md format and drift CI: systems.md.

## Proportion

| Layer | Share of pixels |
|---|---|
| Neutrals (ground, surfaces, ink) | 70-90%; ground alone 70-90% on pages (UI only; thumbnails run on a colourfulness floor instead, `video.md`) |
| Accent (fields excluded) | Persuade <5% of any screen; Operate: all coloured pixels ~3%, warn >12% |
| Semantic (status) | 0-5%, only where a real state exists |
| Effects (scrims) | <1%; glows banned |

- Ink = text + at most one inverted section.
- Accent appears on at most 2 kinds of thing per screen: the primary action + one recurring thing (current selection, focus). The moment it is in five places it stops meaning "here".
- Check proportions on the screenshot, not in the code.

## Accent discipline

- One accent, locked across the product. A second needs a written job; 0-2 total. Write the accent's whitelist (where it may appear) into the system sentence or DESIGN.md.
- Accent is allowed only on primary actions, current selection, focus and state, and any one screen uses at most 2 of those kinds. Never on headings, icons, bullets, borders, underlines or decoration. A headline is ink.
- Inactive states never get full-saturation accent.
- Links count as accent; on a screen that already has an accent CTA, set links in ink with an underline.
- Hover and focus rings count toward the budget.
- Status colours never fill a primary CTA.
- A coloured button is a choice: 52% of strong sites use neutral (black/white/grey) buttons. Operate default: near-black primary.
- Primary fill is chosen per ground: brand on white, a dark same-hue variant on a light brand tint, black or white on photos. Each fill gets its own states and contrast check.
- Saturation: accent under ~80% HSL saturation (roughly OKLCH C ≤ .20 at mid L). To quiet a palette: saturation 70-85%, neutrals dominant, colour at ~10% of pixels; never strip it to grey.
- Brand colour plays one role per view: big background OR interactive elements, never both.

## OKLCH construction

- Use OKLCH for every new web palette: lightness (L 0-100%), chroma (C 0-~0.37), hue (H 0-360). L is perceptual, so equal L steps look equal.
- Ramps: 11 steps (50-950), L roughly .97 .93 .87 .78 .68 .58 .50 .42 .34 .26 .20. Peak chroma mid-ramp (L .5-.65), taper to ~30% of peak at both ends. Never keep high chroma at extreme L to make the maths uniform.
- Hue drift: yellows and greens turn olive when darkened; shift dark steps 10-20° toward orange. Blues may shift a few degrees toward cyan at the light end.
- Gamut: max chroma depends on hue and L (yellow h≈100 peaks near L .9; blue h≈265 peaks near L .45). Stay inside sRGB; boost only under `@media (color-gamut: p3)`.
- Extra colours: derive in OKLCH from the palette, sharing L and C, varying H. Never invent a fresh hex.
- Harmonies by hue rotation at fixed L/C: analogous ±20-40°, complementary 180°, split-complementary 150°/210°, triadic 120°. One dominant, the rest subordinate.
- States from the base: hover ΔL ∓0.06, active ∓0.12 (darken on light grounds, lighten on dark). Never grey the text on hover.
- Subtle tint (selected row, chip ground): same hue, L .95-.97, C × 0.3, built opaque with `color-mix(in oklch, var(--accent) 5-12%, var(--bg))`, never `rgba(accent,.12)`. Selection highlight: brand hue at L ≥ .90. Visited link: hue +20°, less chroma.
- Relative colour for states: `oklch(from var(--accent) calc(l - 0.06) c h)`.
- Focus colour: the accent if it clears 3:1 on every surface; otherwise a dedicated `--focus` (a clear blue, ≈ `oklch(55% .2 260)`).
- Contrast shortcut for neutrals (OKLab L³ ≈ luminance): on white, 4.5:1 needs L ≤ .56, 3:1 needs L ≤ .66, 7:1 needs L ≤ .46. On black, 4.5:1 needs L ≥ .57, 3:1 L ≥ .47, 7:1 L ≥ .67. Verify chromatic colours with a real checker.

## Neutrals

- Tint neutrals toward the brand hue at C 0.005-0.015; whites below C 0.02. Neutral grey is valid when the world wants it.
- One grey family. Never mix warm and cool greys. An Operate sidebar/toolbar layer is one step of the same family, hue shift ≤10°.
- Text tiers: ink, muted, and at most one lighter tier for meta that still passes. Three max.
- Grey text on a coloured ground is never allowed: use a darker shade of that hue, near-white, or the field's ink mixed 70% toward the ground as an opaque token, if it still passes.
- Shadows take the background hue (base ≈ `oklch(15% .02 H / a)`), never neutral black on a tinted page. Elevation scale: components.md.
- Pure `#000`/`#fff` only when deliberate (a stark two-tone, an app dark ground); otherwise tinted near-black ink (`#111`, `#1d1d1f`, a navy-tinted ink) and off-white.

## Both-mode tokens (copy this shape)

```css
:root {
  color-scheme: light dark;
  --h: 250;                                      /* neutral tint hue */
  --ah: 160;                                     /* accent hue */
  --bg:         oklch(99%  .003 var(--h));
  --surface:    oklch(96.5% .005 var(--h));      /* one step: 2-6 L points */
  --surface-2:  oklch(94%  .006 var(--h));       /* deepest nesting allowed */
  --border:     oklch(91%  .007 var(--h));       /* ~1.25:1, structure only */
  --control:    oklch(62%  .01  var(--h));       /* field outline: 3:1 on bg, surface, surface-2 */
  --ink:        oklch(20%  .012 var(--h));       /* ≥7:1 target */
  --muted:      oklch(50%  .012 var(--h));       /* ≥4.5:1 on bg and surface */
  --accent:     oklch(52%  .13  var(--ah));
  --accent-ink: oklch(99%  .01  var(--ah));
  --focus:      var(--accent);                   /* ≥3:1 on every surface */
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { /* repeat every dark value from the block below */ }
}
:root[data-theme="dark"] {
  --bg:         oklch(16%  .006 var(--h));
  --surface:    oklch(20%  .007 var(--h));
  --surface-2:  oklch(24%  .008 var(--h));
  --border:     oklch(28%  .008 var(--h));       /* ~1.3:1 */
  --control:    oklch(55%  .01  var(--h));       /* 3:1 up to surface-2 */
  --ink:        oklch(95%  .005 var(--h));
  --muted:      oklch(72%  .01  var(--h));
  --accent:     oklch(64%  .11  var(--ah));      /* L up, C down 10-15% */
  --accent-ink: oklch(16%  .02  var(--ah));
}
body { background: var(--bg); color: var(--ink); }
```

- Duplicate the dark values under both scopes: the media query follows the OS; `[data-theme]` lets a user toggle win both ways. Switching is one attribute flip, no ternaries in components.
- `light-dark(light, dark)` is a valid shorter form for colour values only; it resolves from `color-scheme`, so a toggle sets `color-scheme: light` or `dark` on `[data-theme]`.
- Set `color-scheme` so native controls, scrollbars and form fields follow; also `<meta name="color-scheme" content="light dark">` so the first paint is not white. Add `<meta name="theme-color">` per mode (`media="(prefers-color-scheme: dark)"`); on field pages it and the header ink follow the current field.
- A stored theme choice is applied by a tiny inline `<head>` script that sets `data-theme` before first paint; never a flash of the wrong theme.
- Theme the browser surfaces from the palette: `::selection`, `caret-color`, `accent-color` (native checkbox/radio/range), `scrollbar-color`, focus rings, link underline.
- Swap logo and image assets per theme (`<picture><source media="(prefers-color-scheme: dark)">` or token-driven SVG `fill: currentColor`); never invert them with filters.
- Native apps: iOS semantic system colours (`label`, `secondaryLabel`, `systemBackground`, `separator`) plus one tint; Android Material 3 roles (`primary`, `on-primary`, `primary-container`, `surface-container-*`) with Dynamic Color and a static fallback. Never hand-roll a second palette beside them.

## Light or dark, one or both

- Pick the primary mode from one written sentence about the physical scene (who, where, what light), never by category. Exception: the owner's own tools start dark (SKILL.md, My standing taste).
- Priors when the scene is unclear: light for marketing, e-commerce, editorial, mixed SaaS, education, healthcare, beauty; dark for trading, dev tools, media/creative editors, dense dataviz, entertainment, games.
- Ship both modes by default via `prefers-color-scheme` + `[data-theme]`. A single locked mode needs a one-sentence justification (cinema, a stark two-tone brand) and still sets `color-scheme`.
- Theme toggle: yes for tools used hours a day (dev, trading, analytics, creative, enterprise); no for marketing and shops. Place it near the account menu or in settings, never in primary nav.
- Persuade: hard-edged section fields are allowed, never fades. Operate: one theme locked per screen, no section inversion.
- Test both modes as separate designs. Never infer dark from light.

## Dark mode rules

- Designed, never inverted. Surfaces and borders take the canvas hue.
- Depth = lighter surface steps (+3-5 L points per level, one elevation step higher than light), never shadows or glows. Borders as explicit tokens ≈1.2-1.4:1 (equivalent to `rgba(255,255,255,.08)`).
- Desaturate brand 10-15% and raise its L until text uses pass 4.5:1 and fills 3:1.
- Muted text is where dark fails: check it on every surface step.
- Status on dark: light status hue on a dark tint of the same hue (`#3fc07a` on `#172a1d`).
- Photos on dark pages: `filter: brightness(.85) contrast(1.05)` or leave untouched, one treatment for all.
- Scrims, states, disabled and focus rings re-checked in dark. Lighter type weights on dark: typography.md.
- Never navy or slate (`#0F172A`, `#1E293B`) as a reflex dark ground; a faint brand tint on near-black is fine.

## Accessibility preferences

- `prefers-reduced-transparency: reduce`: every translucent bar becomes solid `--bg`/`--surface`, no backdrop blur. Glass is allowed only as a functional bar over scrolling content, measured at worst-case contrast over whatever scrolls beneath, and always ships this fallback.
- `prefers-contrast: more`: solid backgrounds, borders ≥3:1, muted text promoted toward ink, no alpha layers.
- `forced-colors: active`: rely on system colours (`Canvas`, `CanvasText`, `LinkText`, `ButtonText`, `ButtonFace`, `Highlight`, `GrayText`). Use `outline` for focus (box-shadow rings vanish). Borderless controls keep `border: 1px solid transparent` so they get an edge; icons use `fill: currentColor`. Use `forced-color-adjust: none` only on swatches and data marks whose colour is the content.
- Test Windows high-contrast mode and a CVD simulation (DevTools Rendering → Emulate vision deficiencies).

## Contrast (WCAG 2.2 AA floor)

| Pair | Minimum |
|---|---|
| Body text, placeholders, error/success text | 4.5:1 (AAA 7:1) |
| Large text (≥24px, or ≥18.66px bold) | 3:1 |
| UI boundaries needed to identify a control, icons, focus indicators, chart marks | 3:1 against adjacent colours |
| Focus appearance (2.4.13, AAA, house floor) | ≥2px perimeter, 3:1 change between focused and unfocused |
| Disabled controls, logos | exempt |

- Target ink-on-ground ≥7:1 for body; "grey body" under 7:1 reads weak. Muted ≥4.5:1 on every surface it sits on.
- A field shown by outline alone needs that outline ≥3:1 (`#d1d5db`-style outlines fail): darken the outline or give the field a fill plus a persistent label.
- Never lower text opacity without measuring the result. Hover and focus raise contrast, never lower it.
- Never use colour as the only signal (1.4.1): pair with icon, text, shape, weight or underline. Links in body text get an underline.
- Measure real computed pairs in every state, both themes, on overlays and over images. Check the smallest text on the densest screen. 4.3:1 fails.
- APCA as a second opinion where perception matters: Lc 75 body, 60 other text, 45 large headlines, 30 non-text. WCAG 2 ratios remain the legal gate.

## Surfaces and fields

- Separate a surface from the ground by tone: 2-6 L points, one step. If a panel does not read, add padding or space before adding a second tone. No panel in panel.
- Persuade: no 1px lines as decoration. A ≥4px bar in ink or accent is a graphic element and allowed where the direction uses it.
- Operate: borders allowed for structure at ~1.1-1.3:1 (values in the app table below). Pick ONE of border, elevation or fill per surface; nested surfaces switch strategy; max 2 nesting levels.
- Background-change hover needs a defined edge; on a borderless card hover with a border or shadow.
- Fields (Persuade): a section changes the whole ground with a hard edge, never a fade. Each field has its own ink. Neighbouring fields differ in lightness, not just hue, or the page vibrates. Order fields like chapters: open strong, rest, surprise, close very dark or very light. Strong pages median 2 section grounds.
- Images need no frame. If a light photo melts into a light ground, recrop or set it on `--surface`.
- Operate colour does real jobs only: primary action, selection, state, data series. The shell stays on the page ground; its only colour is an environment strip (prod/staging). Tenants get a label, never a colour or theme.

## App exact values (house defaults)

| Light | Value |
|---|---|
| Ground | white on off-white (`#f3f5f7`-`#fdfdfd`), grey on white, or a framed sheet |
| Sidebar | on the page ground; never dark or saturated |
| Active nav item | neutral pill `#e9e9e9`-`#ededed` |
| Lines | cards `#eaeaea`; bands `#e5e7eb`-`#ededed`; row rules `#efefef`-`#f4f4f4`; controls `#d1d5db` (with fill) |
| Text | `#111` / `#5f6368` / lightest that holds 4.5:1 ≈ `#6b6b6b` |
| Positive text | `#247b50` (5.2:1) |
| Pills | positive `#dcfae5` / `#04250e`; negative `#ffedea` / `#831c1e` |
| Notice | `#fffbeb` ground, `#fde68a` border, `#92400e` text |
| Count badge | `#c4242a` |
| Settings panel | `#fafafa` |

| Dark | Value |
|---|---|
| Ground | `#000`, `#111` or `#171719`; never navy/slate |
| Surfaces | one lighter step (`#111` on `#000`); nested `#222`-`#2a2a2a` |
| Structural lines | `#1a1a1a` on `#000`; `#2e2e2e` on `#111` |
| Interactive outlines | `#373737`-`#4c4c4c` |
| Text | `#fff`, greys `#b4b4b4` / `#949494` |
| Active nav | brightness step (`#bbb` → `#fff`) |

- Persuade dark default: tinted deep ground with soft light ink (neutral version `#0f0f0f` / `#f0f0f0`), not `#fff` on `#000` unless the direction is a stark two-tone.
- If the accent is green, positive IS the accent: give negatives a distinct hue and keep the accent off neutral controls.
- Disabled fills are neutral greys, never brand tints. Selected row: the subtle accent tint (opaque token).
- The main data element carries the hue; chrome (nav rows, tab pills, every button) never does.

## Status and semantic colour

- Four roles max, each meaning one thing everywhere: danger (error, destructive), warning, success, info. Neutral grey beats a misused semantic colour.
- Hues in OKLCH: danger h≈25-30, warning h≈70-85, success h≈145-155, info h≈240-260. Match the brand's L and C (a muted brand gets muted semantics); warning sits one L step darker than the others.
- Orange/amber means warning only: never pending, progress, neutral, info or brand. Pending and draft are grey or blue. An orange brand needs a distinct amber for warnings.
- Danger red is for errors and destruction only. When a user rejects red in UI, keep the danger role but shrink it to icon + text and ask which hue carries it.
- Always pair status colour with icon + label. Avoid red/green-only pairs. Operator tables: 2-3 labelled states, never >5.
- Pills: pale tint ground + dark same-hue text, never saturated fills with white text. One status mark per row.
- Warning fills (amber, yellow) take dark text; their text-only form needs a darker step (`#92400e`) to pass 4.5:1.
- Banners: danger error, amber warning, blue info, green resolved. Status never follows the theme's accent.
- Status dots only for live data; a decorative "Available" dot is a tell.

## Deltas and numbers

- Colour encodes good/bad, not up/down: latency up is negative, cost down is positive.
- Zero or undefined change is grey. From zero write "+4 (new)", not a percentage.
- Sign on every change; colour is the second channel after the sign.
- Missing values: muted dash with screen-reader text, zero printed as `0`.

## Colour in data viz

- Every chart colour does one job: categorical (identity), ordinal (order), sequential (magnitude), diverging (polarity around a baseline), status (state).
- One hue per chart on the main data element by default; one series needs no legend. Warn >4 hues, fail >6. Never a rainbow.
- Nominal bars (teams, products) all take the same slot-1 hue; never colour bars by their value.
- Categorical slots: fixed order, assigned in sequence, never cycled. OKLCH L .43-.77 on light, .48-.67 on dark; C ≥ 0.10 or the hue reads grey. Adjacent pairs ΔE ≥8 (OKLab ×100; 6-8 only with a secondary encoding) under protanopia/deuteranopia simulation, ≥15 for normal vision (hard gate). Run a validator, never eyeball.
- A series keeps its colour across every chart and view on the screen and in the product.
- Validated default order (light / dark): blue `#2a78d6`/`#3987e5`, orange `#eb6834`/`#d95926`, aqua `#1baf7a`/`#199e70`, yellow `#eda100`/`#c98500`, magenta `#e87ba4`/`#d55181`, green `#008300`, violet `#6250d6`/`#9085e9`, red `#e34948`/`#e66767`.
- Scatter, bubble, maps and small multiples: any two marks can touch, so cap at 3 series; past that fold into "Other" or facet.
- Ordinal and sequential: one hue, monotone lightness, light → dark (blue `#cde2fb` → `#0d366b`); on dark grounds the anchor flips (more = lighter). Ordinal end nearest the surface still ≥2:1 (start no lighter than `#86b6ef` on light, no darker than `#184f95` on dark). Data ramps are the one place gradients belong.
- Diverging: two opposed hues (default blue ↔ red) + a grey midpoint (light `#f0efec`, dark `#383835`), equal steps per arm. Never red → green for magnitude.
- When a series means good/bad (error rate, pass/fail) it wears status colours; otherwise categorical. Never both in one chart. Chart status scale, never themed: good `#0ca30c`, warning `#fab219`, serious `#ec835a`, critical `#d03b3b`, always with icon + label (warning and serious fall under 3:1 on light, so they need the label or an outline).
- Marks ≥3:1 against the surface or ship direct labels / a table view. Labels ≥4.5:1. Never colour alone: add direct labels, line styles, patterns or position. Colours that must be told apart also differ in lightness. Prefer blue/orange over red/green.
- Gridlines faint (`#e5e5e5`; dark `#2b2b2b`), 3-5 of them. Fills under lines none or ≤14%. Forecasts dashed. Chart forms and anatomy: apps.md.

## Photos and colour

- When photos carry colour, the UI stays neutral and takes its ink from the darkest tone in the imagery.
- Never wash photos in brand colour. One treatment for every image: untouched (default), all greyscale (`grayscale(1) contrast(1.05)`), multiply on a light field, or the dark-page dim.
- A flat field sampled from a photo (its sky, its shadow) seats a section with that image.
- Text on a photo: only headline + one line + one action, on a calm area. Scrim = flat 40-55% black (or ink) block, or a 55% → 0 fade over the lower third only: the one decorative-looking gradient allowed. Measure 4.5:1 (3:1 at ≥24px) against the real pixels, across the whole video loop. Text-shadow never substitutes for a scrim on a page. Text burned into video or a thumbnail uses an ink outline or hard offset shadow instead (`video.md`).
- Never bury a raster under a 0.9+ wash or at near-zero opacity.
- Product shots on tinted tiles: cutouts or multiply blend so the white box disappears.

## Warmth without slop

- Banned by reflex (the AI rendition clusters): cream/yellow-cream/peach ground (HSL hue ~22-62, noticeably saturated) with terracotta (HSL hue ~6-30), rust, clay or signal-red accent; violet/indigo and purple-blue glow; near-black with one neon accent and glowing edges; two-stop purple→blue or blue→cyan heroes. Either half of cream+terracotta alone is suspect. Full hex list: tells.md.
- Warm, bookish, family and child subjects default to cream and lamplight: treat that palette as spent and work from the subject's saturated materials (book cloth, thread, endpapers, wood, enamel).
- Warmth sources that work: low-chroma stone, bone or putty grounds (C ≤ ~0.03, under ~15% saturation); deep green, brown or oxblood ink; real photographs; or one full warm field (mustard, tomato, pink) used flat and with conviction. Warmth is not beige.
- Pairings to rotate: cold luxury (grey-blue + silver ink), forest (deep green + bone), black + tan, cobalt + off-white, olive + brick + paper, monochrome + one pop.
- A brand that owns a banned colour keeps it; note the exception.
- Gradients: banned as decoration (backgrounds, buttons, text, blobs, mesh, stripes). Glows, coloured halos and radial spotlights banned. Colour washes, duotone and vignettes banned on web and app surfaces. Video grades and photo composites may take one soft vignette and one light grain over the whole frame as the unifying finish (`video.md`).

## Domain starting points

Starting points only: check the user's own rules first. Values are Tailwind defaults (a tell themselves): take the hue direction, then rebuild the ramp in OKLCH.

| Domain | Mode | Primary | Accent | Ground | Ink |
|---|---|---|---|---|---|
| General SaaS | light | `#2563EB` | `#EA580C` | `#F8FAFC` | `#1E293B` |
| Productivity | light | `#0D9488` | `#EA580C` | `#F0FDFA` | `#134E4A` |
| CRM / inventory | light | `#334155` | `#059669` | `#F8FAFC` | `#0F172A` |
| Analytics | light + toggle | `#1E40AF` | `#D97706` | `#F8FAFC` | `#1E3A8A` |
| Trading / finance dash | dark | near-black | `#22C55E` | `#020617` → neutral | `#F8FAFC` |
| Status page | light | `#16A34A` | `#DC2626` | `#F0FDF4` | `#14532D` |
| Dev tool / IDE | dark | `#1E293B` | `#22C55E` | neutral near-black | `#F8FAFC` |
| Docs / KB | light | `#475569` | `#2563EB` | `#F8FAFC` | `#1E293B` |
| Banking | light | `#0F172A` | `#A16207` | `#F8FAFC` | `#020617` |
| Healthcare (16px+) | light | `#0891B2` | `#059669` | `#ECFEFF` | `#164E63` |
| Senior care (18px+) | light | `#0369A1` | `#16A34A` | `#F0F9FF` | `#0C4A6E` |
| Fitness | dark | `#F97316` | `#22C55E` | `#1F2937` → neutral | `#F8FAFC` |
| Kids learning | light | `#2563EB` | `#EC4899` | `#EFF6FF` | `#0F172A` |
| Video / OTT | dark | `#0F0F23` | `#E11D48` | `#000000` | `#F8FAFC` |
| Social | light | `#E11D48` | `#2563EB` | `#FFF1F2` | `#881337` |
| E-commerce | light | `#059669` | `#EA580C` | `#ECFDF5` | `#064E3B` |
| Luxury | light | `#1C1917` | `#A16207` | `#FAFAF9` | `#0C0A09` |
| Food delivery | light | `#EA580C` | `#2563EB` | `#FFF7ED` | `#0F172A` |
| News | light | `#DC2626` | `#1E40AF` | `#FEF2F2` | `#450A0A` |
| Magazine / portfolio | light | `#18181B` | `#2563EB` | `#FAFAFA` | `#09090B` |
| Government / B2B | light | `#0F172A` | `#0369A1` | `#F8FAFC` | `#020617` |
| Legal | light | `#1E3A8A` | `#B45309` | `#F8FAFC` | `#0F172A` |
| Insurance | light | `#0369A1` | `#16A34A` | `#F0F9FF` | `#0C4A6E` |

- Tinted grounds (`#FFF7ED`, `#FEF2F2`, `#FFFBEB`) read as peach/cream: use a near-neutral ground.
- Sources give violet/indigo primaries for AI chat, meditation, micro-SaaS, education, gaming and beat-makers: that is the AI cluster; pick hue from the product's own world.
- Music-instrument learning: sources give red + amber on cream, which is the cream + signal-red cluster and red this owner dislikes. Start from the instrument's materials (rosewood, maple, nickel, the LED colour) with energetic contrast.
- Domain energy: no AI purple/pink on trust domains (bank, gov, legal, health, insurance, logistics); no muted low-energy palettes on games, habits or food delivery; no light default on dev/trading/OLED tools.

## Verify

- Every colour has a stable role; attention lands on the intended action, content or state.
- Greyscale screenshot: hierarchy and states still read.
- Accent counted per screen (≤2 kinds of thing); coloured-pixel share within budget.
- Computed contrast for every text/ground pair, placeholders, focus rings, field outlines and chart marks, in both themes and all states (hover, disabled, error, selected, over images).
- CVD simulation passed; nothing relies on colour alone.
- Literal-hex grep: 0 in components; nothing off-token.
- Reduced transparency, increased contrast and forced colours each render legibly.
- Palette holds across quiet, dense, empty and error states, and is recognisably this product, not a category default.
