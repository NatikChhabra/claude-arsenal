# Typography

Use when: choosing faces, building a type scale, setting display or body text, sizing app UI text, loading fonts, setting type for RTL/CJK, or building Read-mode surfaces (docs, articles). Type is most of what makes a surface look designed rather than assembled.

## 1. Choosing faces

- Choose the face like an object from the subject's world (signage, a label, a manual, a ticket), never from a category association ("books want a serif", "tech wants mono" are not reasons).
- Choose by the job first: display face (large, voice), text face (reading), UI face (labels, controls, data). One family can do all three.
- Default to sans display. "Creative / premium / editorial" alone is not a reason for a serif; use a serif when the world or brief names one.
- Avoid the overused list below for display and brand type. A neo-grotesk for dense app UI is fine when chosen on purpose (say why in one line).
- The brief wins: a pinned font, era or brand face beats every rule here, including the overused list.
- Rotate between projects. A face you reach for every time is on your personal overused list.
- A display face drawn for large sizes never sets body text. Check the specimen at 16px before using one face for both.
- Never use the closest installed system font as a stand-in for a chosen face on a Persuade page; that is a failure, not a fallback. Never use Impact, Arial Black or bare `system-ui` as a display voice.
- Licensed brand faces (Söhne, Suisse Intl, Neue Haas, GT America, ABC Diatype, PP Neue Montreal, Aeonik, PP Editorial New, Migra): use them only when the client owns the licence; otherwise use the free stand-in from the table and flag it.

**Overused: do not default to these for display or brand type**
Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Arial, Helvetica, Geist / Geist Mono, Mona Sans, Space Grotesk, Space Mono, IBM Plex (as display), DM Sans, DM Serif, Plus Jakarta Sans, Outfit, Sora, Instrument Sans, Instrument Serif, Fraunces, Playfair Display, Cormorant, Lora, Crimson, Newsreader (as display), Syne, Recoleta. Sci-fi costume faces (Orbitron, Exo, Rajdhani, Russo One) only when the world truly is that.

**Recommended families by mood** (G = Google Fonts, F = Fontshare; claude.ai artifacts load stylesheets from Google Fonts only, so use a G face there)

| Mood / world | Display / text | Setting that makes it work |
|---|---|---|
| Exact, engineered, software/hardware | Switzer (F) alone; Hanken Grotesk (G) alone | 500-600, -0.04em, leading 0.95, sentence case; no second voice |
| Composed finance, institutions | Archivo (G) at 400 even at 88px; Albert Sans (G) 600 | regular weight carries authority; no bold |
| Warm, compact, media | Schibsted Grotesk (G) 800 / same 400-600 | -0.05em, leading 0.88 |
| Drawn, crafted, studio | Bricolage Grotesque (G) 600; Erode (F) 500 | let optical sizing run; -0.025 to -0.04em |
| Newspaper front page | Libre Franklin (G) 700 / Source Serif 4 (G) | caps title, serif for reading |
| Loud poster, sport, nightlife, drops | Anton (G) / Work Sans; Big Shoulders (G) 800 / Public Sans; Archivo at `font-stretch: 62%` 800; Barlow Condensed (G) 700 / Barlow | caps, leading 0.86-0.9, tracking near 0 |
| Wide, architectural | Panchang (F) 700 / Switzer; Unbounded (G) 800 / Onest; TikTok Sans (G) at `font-stretch: 150%` | caps, 4 words or fewer per line |
| Black, enormous-and-small | Chivo (G) 900; Epilogue (G) 900; Cabinet Grotesk (F) 800 | only two sizes on the page |
| Geometric, science, space | Jost (G) 700 caps; Red Hat Display / Red Hat Text (G); League Spartan (G) / Figtree | -0.03 to -0.04em |
| Friendly consumer, wellness, home | Chillax (F) 600; Roundo (F) 500; Pilcrow Rounded (F) 700 lowercase | generous text size, soft weight |
| Fashion, beauty, hotels | Bodoni Moda (G) 500 / Jost; Gambarino (F) / General Sans (F); Imbue (G) / Albert Sans; Boska (F) roman + italic | optical sizing on; 5:1 size jump, nothing between |
| Quiet literary, long-form | Literata (G); EB Garamond (G) roman + italic; Sentient (F); STIX Two Text (G) | headings are the text face larger; no bold |
| Hairline luxury | Zodiak (F) 100 above 96px, 300 at 28-36px / Hanken Grotesk | only at sizes where the hairline reads as drawing |
| Old-style warmth, essays, food | Young Serif (G) / Source Serif 4; Besley (G) 800 / Libre Franklin; Zilla Slab (G) | one heavy headline cut over a clear text face |
| Studio launch, name-led | General Sans (F) 700; Clash Grotesk (F) 400 | jump from 16px text straight to 10vw+ |
| Accessibility-first, public service | Atkinson Hyperlegible (G); Public Sans (G); Lexend (G) | larger body (18px), open spacing |
| Product UI (Operate) | system stack, or one deliberate neo-grotesk: Switzer, Hanken Grotesk, Albert Sans, Public Sans | one family, weights do the hierarchy |
| Code, IDs, keys | JetBrains Mono (G), Commit Mono, Source Code Pro (G) | code only; never as a label voice |

## 2. Families and pairing

- Use 1 family (safest coherence) or 2. Never more than 2 text families; a mono is allowed on top only where code, IDs or keys appear.
- Pair on one clear contrast axis: serif vs sans, condensed vs normal width, heavy display vs light text. Never two similar sans.
- Match shape language and x-height: geometric with geometric, humanist with humanist. If x-heights differ, set both to one x-height with `font-size-adjust` (e.g. `font-size-adjust: ex-height 0.5`) or by eye at rendered size.
- Give each face one job and never swap them: display sets headlines, text sets everything else.
- No third face for labels, numbers or quotes. No two faces in one headline.
- Emphasis inside a headline = italic or bold of the same family. Never a serif word dropped into a sans headline, never a coloured or underlined accent word.
- Italic only for titles of works and real emphasis. Never `<br>`-split italic lines as decoration.
- Monospace: only for code, IDs/keys, or all figures as a deliberate, documented style. Never as a "technical voice" for labels, captions or eyebrows. Never mono in uppercase.

## 3. Scales

**Count and spacing of sizes**
- Persuade: 2-3 sizes do the visible work (display, text, small), far apart; lead and heading exist only when needed; 5 is the ceiling. Adjacent steps differ by ≥1.25x. Nine near sizes (16, 18, 20, 24, 28...) read as mush.
- Operate: 5-7 sizes in the system, ≤5 per view (title, answer figure, body, label, meta). Separate close steps with weight and ink, not 2px size bumps.
- If two sizes look almost the same, make them the same. Never 2px size steps.
- Persuade: ≤3 sizes above the fold. Every mode: one size dominant per screen.

**Ratios** (`size(n) = base × ratio^n`, base 16px)

| Ratio | Use |
|---|---|
| 1.067 | dense dashboards |
| 1.125 | mobile, compact UI |
| 1.2 | most product UI, internal tools |
| 1.25 | Read mode, default marketing body-to-heading |
| 1.333 | Persuade heroes |
| 1.414-1.5 | portfolios, posters |

Tighten the ratio on small screens (desktop 1.25-1.333 → tablet 1.2 → phone 1.125). Body never shrinks.

**Persuade: fluid tokens**
```css
:root {
  --step-small:   clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem);  /* 13-14px captions, legal */
  --step-body:    clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem);   /* 17-19px paragraphs */
  --step-lead:    clamp(1.25rem, 1.1rem + 0.7vw, 1.625rem);     /* 20-26px supporting line */
  --step-head:    clamp(2rem, 1.3rem + 3.2vw, 4rem);            /* 32-64px section headings */
  --step-display: clamp(3rem, 1rem + 9vw, 9rem);                /* 48-144px; set per hero */
}
```
- Wide fluid ranges only at the top of the scale (lead and up); small and body steps move ≤2px across viewports so adjacent steps never converge. Every clamp keeps a rem term so browser zoom still scales it (pure `vw` fails WCAG 1.4.4).
- Keep a clamp's max ≤2.5x its min and it is guaranteed to survive 200% zoom; anything wider (the display step is 3x) gets checked at 200% zoom.
- Slope for a clamp from `min` at viewport `vmin` to `max` at `vmax`: `slope = (max - min) / (vmax - vmin)`; `preferred = (min - slope × vmin) in rem + (slope × 100)vw`.
- Nothing sits between `--step-lead` and `--step-head` unless the design truly needs a sixth size.

**Operate: fixed rem scale** (no clamp on headings)
```css
:root {
  --text-xs: 0.75rem;   /* 12 / 16  glance meta only */
  --text-sm: 0.875rem;  /* 14 / 20  default UI, cells, controls */
  --text-md: 1rem;      /* 16 / 24  body in consumer apps, inputs on mobile */
  --text-lg: 1.25rem;   /* 20 / 28  section titles (card titles use md) */
  --text-xl: 1.5rem;    /* 24 / 32  page title (median) */
  --text-2xl: 2rem;     /* 32 / 40  answer figure, top title ceiling */
}
```
Other clean app scales: 12/14/18/24, 12/14/16/30, 12/14/16/24.

**Read mode**: 4-5 sizes, body 18-21px, ratio 1.25 (e.g. 18 / 22.5 / 28 / 35 / 44), measure 60-70ch.

- Sizes and line heights in rem; line-height unitless for text. Never `html { font-size: 62.5% }`.
- Name tokens by purpose (`--text-body`, `--step-display`), never by value (`--16px`). Token format and DESIGN.md typography block: see systems.md.

## 4. Display type (anything over ~32px)

**Size**
- No fixed cap on hero size. Hero headline ≤2 lines at every width; display ≥4x body on Persuade (top sites 4.7x).
- Persuade largest type typically 6-10vw (strong sites median 8.4vw; weak 5.0vw); a monument wordmark 16-24vw. Largest type <4.5vw with no picture ≥30% of the screen = no focal point, a failure. Hero desktop median 72px, phone 32-59px (median 40). `h1` ≥32px desktop, ≥26px phone.
- Section headings ~3.5x body (median ~57px on pages). A confident hero followed by section headings almost as large is a failure: keep one size dominant.
- Operate page titles 18-32px (median 24), no figure ≥48px.
- Big type need not be bold: half of strong heroes are regular weight.
- A big intro sentence or quote is a statement, not a headline: `<p>` or `<blockquote>`, ≤~25 words, ≤36px desktop / 32 tablet / 24 phone, ≤3 lines (4 on phone).
- Fit check and the ~32-character headline budget: copy.md §3 (owner of the formula and the k values). Fix order: cut words, widen measure, then size; never a timid 28px nine-word headline.
- Viewport-wide line: size in `vw` from that formula, `white-space: nowrap`, let the container clip, verify at 390 and 1440.

**Leading and tracking by size**

| Size | Leading | Tracking |
|---|---|---|
| ≥96px | 0.88-1.0 | -0.03 to -0.04em (-0.05em only on tight grotesks, checked by eye) |
| 48-96px | 0.95-1.05 | -0.02 to -0.035em |
| 32-48px | 1.05-1.15 | -0.01 to -0.02em |
| 20-32px | 1.15-1.25 | -0.005 to -0.01em |
| 15-20px (body) | 1.45-1.6 | 0 |
| ≤13px | 1.4-1.5 | +0.01 to +0.02em |
| All caps, display | ~0.9 | 0 to +0.03em |
| All caps, ≤14px labels | 1.2-1.4 | +0.04 to +0.08em (default +0.06em) |

- Set tracking per step, never once for all headings: the value right at 120px chokes 32px.
- Tracking floor -0.04em by default. Letters touching or falling apart both fail.
- Leading below 1.0: check descenders against the next line's ascenders and accents. Italic display with descenders: leading ≥1.1 plus bottom padding so the descender is not clipped.
- Condensed and all-caps faces take the tighter end of the leading range; faces with tall ascenders take the looser end.
- Display weight ceiling 600 by default; 700-900 only as a chosen voice (poster, black grotesk), not by habit.

**Setting**
```css
.display {
  font-size: var(--step-display);
  line-height: 0.95;
  letter-spacing: -0.035em;
  font-kerning: normal;
  font-optical-sizing: auto;
  text-wrap: balance;
  max-width: 14ch;           /* choose the measure so lines break where you want */
  margin: 0;
  hyphens: none;
}
```
- `text-wrap: balance` on h1-h6, blockquote, figcaption, dt, titles, toasts, tooltips. Cap headings with `max-width` in ch.
- Author the break between phrases, never inside one ("Stools for small / kitchens" fails). No one-word orphan on line two. Re-check every break at 390, 768, 1440; a `<br>` that works at one width breaks at another, so prefer `balance` plus `max-width`.
- Optical alignment: round or diagonal left edges (O C A T W V Y) look indented at display size. Pull left `margin-left: -0.05em` (0.04-0.06em) so the glyph aligns with text below.
- Hang opening quotes outside the text edge on pull quotes (`hanging-punctuation: first` in Safari, or a negative `text-indent` of the quote's width).
- Trim box whitespace to the cap height and baseline where supported (`text-box: trim-both cap alphabetic`) so type aligns to images and edges; otherwise nudge by eye after rendering.
- Space above a heading ≥2x the space below it.
- Never on display type on pages and apps: text-shadow, outline stroke, gradient or image fill, `background-clip: text`, vertical rotated text, scramble or typewriter effects. Text over video and thumbnails is the exception: ink outline, `paint-order: stroke fill` stroke and a hard offset shadow (no blur) are allowed there (`video.md`).
- A pinned brand display face (Impact, Arial Black or any other) is honoured over the font tells.
- Sentence case for headlines and buttons. All caps only for ≤3 words, or for a display headline in a caps face chosen as the voice (poster, wide rows in the table).
- Line-mask reveals need bottom padding for descenders: see motion.md.

## 5. Body text

- Size: Persuade body 16-19px (fluid 17-19 token); Read 18-21px; Operate 14px default (13px in dense tables, 16px in consumer apps and all mobile inputs). Never body <16px on web pages.
- Smallest text: product UI ≥14px by default; 12px only for glance meta (timestamps, axis labels, badges, table meta), ≤3 such roles per screen; never <11px anywhere. Secondary text on pages never <13px.
- Measure 45-75ch, target 60-70 (`max-width: 62-66ch`); phone 35-60ch; warn past ~80ch. Dense tables may run to 120ch.
- Leading grows with measure:

| Measure | Body leading |
|---|---|
| ≤45ch | 1.4-1.45 |
| 55-66ch | 1.5 |
| 75ch | 1.6-1.7 |
| Lead / large body | 1.3-1.4 |

  Body never <1.4. Leave headroom for a user override to 1.5 line height, 2x paragraph spacing, 0.12em letter, 0.16em word spacing (WCAG 1.4.12) without clipping.
- Body tracking 0. Never above +0.05em on body.
- Paragraph spacing OR first-line indent, never both. Default `p + p { margin-top: 0.9em }`.
- Left-aligned. No centred paragraphs over 3 lines. No justified text on the web.
- `text-wrap: pretty` on p, li, dd.
- Secondary text = same face, same or heavier weight, softer ink (`--muted`). Never a lighter weight for de-emphasis. Contrast: see colour.md.
- Run the real copy at every breakpoint; lorem hides measure and break problems.

```css
body { font-size: var(--step-body); line-height: 1.5; font-kerning: normal; -webkit-text-size-adjust: 100%; text-size-adjust: 100%; font-synthesis: none; }
p    { max-width: 62ch; text-wrap: pretty; margin: 0; }
p + p { margin-top: 0.9em; }
.lead { font-size: var(--step-lead); line-height: 1.35; max-width: 40ch; }
small, .caption { font-size: var(--step-small); line-height: 1.45; }
```

## 6. Weights

- 2-3 weights per project: 400 body, 500 labels and UI emphasis, 600 headings. 700 does one job if used at all. Everything bold means nothing is bold.
- Load only the weights you use. With a variable font, use in-between values deliberately (450, 550) instead of loading more files.
- Never change weight on hover or selection; the line reflows. Use colour, underline or a background instead.
- Light text on dark: at display sizes drop one weight step (light-on-dark reads heavier); at ≤16px keep the weight or go up one step (thin strokes fade), add +0.01em tracking and +0.05 leading.
- Hairline and 100-300 weights only at sizes where the stroke still reads (≥28px for 300, ≥96px for 100).
- Never let the browser fake bold or italic: `font-synthesis: none`, and load the real cut.

## 7. Details

- Quotes and apostrophes curly (‘ ’ “ ”), never straight. Real ellipsis (…). Real multiplication sign for dimensions (1920 × 1080). True minus (−) for negative figures in tables. Primes (′ ″) for feet and inches.
- Ranges: unspaced hyphen in data and specs (10-20 kg); "to" in sentences. No em or en dashes in visible text; see copy.md for punctuation.
- Non-breaking space between number and unit (10&nbsp;kg, 5&nbsp;min) and inside short fixed phrases. Prefer `text-wrap: pretty` to manual widow fixes.
- Figures:
  - `font-variant-numeric: tabular-nums` on prices, tables, dates in columns, timers, counters, scores, count-ups. Verify the face actually changes digit widths.
  - `lining-nums` in UI; `oldstyle-nums` in serif body text; `proportional-nums` on a single static display figure (a hero stat) so its digits keep their drawn spacing.
  - `slashed-zero` on IDs and codes; `diagonal-fractions` for recipes and specs.
  - Right-align numbers in tables with fixed decimals; see apps.md.
- Use `font-variant-*` properties first; `font-feature-settings` only for stylistic sets (`"ss01"`) or features with no property. Variable axes through `font-weight`, `font-stretch`, `font-optical-sizing`; `font-variation-settings` only for custom axes (it overrides as one block, so redeclare every axis).
- Tracking in em, never px, so it scales with the size.
- Real small caps (`font-variant-caps: all-small-caps`) for acronyms in body text only when the face has them; never synthesised.
- Links in running text stay underlined: `text-underline-offset: 0.18em; text-decoration-thickness: 0.07em; text-decoration-skip-ink: auto`. Colour alone is not a link cue.
- `hyphens: none` on headings. `hyphens: auto` only with a correct `lang` and a narrow column. `overflow-wrap: anywhere` only for URLs, emails, IDs; never `word-break: break-all` on prose.
- Browser surfaces belong to the design: `::selection` in the accent with its ink, `caret-color: var(--accent)`, `:focus-visible` ring, underline offsets, tabular numerals.
- Eyebrows, kickers, tracked micro-labels above headings, 01/02/03 numbering: banned on Persuade. Operate allows ≤1 tracked uppercase label per screen; group labels are 12-13px sentence case. Full list: tells.md.
- Truncation: shorten copy first, then drop a step, then change the layout. Truncate identifiers, never explanations, prices, errors, legal or instructions. Titles single-line ellipsis; descriptions `line-clamp` 2-3; `min-width: 0` on flex and grid children; full text in a tooltip only when actually truncated.
- Labels plus explanation in one slot: separate by weight and ink (600 primary over 500 muted), not size.

## 8. Font loading

- Production: self-host WOFF2. Prototypes and claude.ai artifacts: a Google Fonts `<link>` is fine (Fontshare for local prototypes only): `css2?family=Name:wght@400;600&display=swap` with only the used weights, plus `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`. In a framework use its loader (`next/font`), which self-hosts and computes fallback metrics.
- Request only used weights (usually 2-3 files). Use a variable font when you need 3+ weights or a width axis (`font-stretch`); static files for 1-2 weights.
- Subset to the scripts used (Latin cuts 60-80% of size) with `unicode-range` splits.
- `font-display: swap` for display and brand faces; `optional` for body text when layout shift matters more than the face. Never invisible text.
- Preload only the 1-2 critical files (the hero display face, the body regular). Preconnect to any third-party font origin.
- Fallback stack of the same kind (sans for sans, serif for serif), with a metric-matched fallback face so swap does not shift layout (CLS ≤0.1).
- A screenshot rendered in a fallback face proves nothing. Confirm the face loaded before judging any render: after `await document.fonts.ready`, some entry of `document.fonts` with that family has `status === "loaded"` (`document.fonts.check()` also returns true for a family no `@font-face` declares), or read the rendered fonts in devtools.

```html
<link rel="preload" href="/fonts/display-600.woff2" as="font" type="font/woff2" crossorigin>
```
```css
@font-face {
  font-family: "Display";
  src: url("/fonts/display-var.woff2") format("woff2");
  font-weight: 400 700;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02C6, U+2000-206F, U+20AC, U+2122, U+2212;
}
@font-face {                       /* metric-matched fallback; compute overrides with a tool, never guess */
  font-family: "Display Fallback";
  src: local("Arial");
  size-adjust: 104%; ascent-override: 92%; descent-override: 24%; line-gap-override: 0%;
}
:root {
  --font-display: "Display", "Display Fallback", "Helvetica Neue", Arial, sans-serif;
  --font-text: "Text", Georgia, "Times New Roman", serif;
  --font-ui: -apple-system, BlinkMacSystemFont, "Segoe UI Variable", "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
```

## 9. App UI type (Operate)

| Role | Size | Weight | Notes |
|---|---|---|---|
| Page title | 24px (18-32) | 600 | a noun ("Analytics"); warn >34 |
| Answer figure / KPI | 24px (16-40); the one answer 30-36 | 500-600 | ≥1.3x sibling figures, tabular, value ~1.7x its label; no figure ≥48 |
| Card / section title | 16px (14-24) | 500-600 | |
| Body, table cells | 14px (13-16) | 400 | line height 20px |
| Controls, buttons, nav labels | 14px | 500 | inputs 16px on mobile (iOS zooms below 16) |
| Field labels, helper text | 14px (13 in dense views) | 400-500 | sentence case, grey that passes 4.5:1 |
| Table headers, axis labels, timestamps | 12px | 400-500 | each counts as a glance-meta role |
| Pills, badges | 11-12px | 500 | floor 11px; counts as a glance-meta role |

- One neo-grotesk or the system stack. A second face only for one job: mono for IDs and figures, or a serif for one personal greeting.
- Display fonts never in labels, data or controls.
- Move density as a set: dense = 13px body with 28px list rows / 42px table rows; changing type size alone breaks rhythm. Density detail: see apps.md.
- Figures that update live (timers, scores, prices) are tabular so the width never wobbles.

## 10. Platform and system type

- Default to the system font for native apps and product UI unless there is a reason. Respect the user's text size: sizes in rem/em, spacing in rem, layouts survive 200% text and Dynamic Type without truncation.
- Web Safari can follow iOS Dynamic Type: `font: -apple-system-body` on `html`, then size everything in rem.
- Never disable zoom; never `text-size-adjust: none`.

**iOS (SF Pro, Dynamic Type default sizes, pt)**

| Style | Size / leading | Weight |
|---|---|---|
| Large Title | 34 / 41 | Regular (Bold in nav bars) |
| Title 1 / 2 / 3 | 28 / 34, 22 / 28, 20 / 25 | Regular |
| Headline | 17 / 22 | Semibold |
| Body | 17 / 22 | Regular |
| Callout | 16 / 21 | Regular |
| Subheadline | 15 / 20 | Regular |
| Footnote | 13 / 18 | Regular |
| Caption 1 / 2 | 12 / 16, 11 / 13 | Regular |

- SF switches Text/Display optical cuts at 20pt and applies size-specific tracking itself (positive below 12pt, negative around body). Never add your own tracking to the system font.
- Hierarchy comes from weight, size and leading together; leading runs inverse to size.
- iOS floor 11pt; body 17pt (Apple's own web body is 17px / 1.47). Test at the largest accessibility size (Body grows to 53pt at AX5): text wraps, never truncates; stack side-by-side layouts.

**Android (Material 3, sp; Roboto / Roboto Flex)**

| Role | L | M | S |
|---|---|---|---|
| Display | 57/64 | 45/52 | 36/44 |
| Headline | 32/40 | 28/36 | 24/32 |
| Title | 22/28 | 16/24 (500) | 14/20 (500) |
| Body | 16/24 | 14/20 | 12/16 |
| Label | 14/20 (500) | 12/16 (500) | 11/16 (500) |

- Type in sp so it follows the user's font scale; test at 200%.

**Windows (Segoe UI Variable, Fluent ramp)**: Caption 12/16, Body 14/20, Body Strong 14/20 semibold, Body Large 18/24, Subtitle 20/28, Title 28/36, Title Large 40/52, Display 68/92.

**Slides**: never below 24px at 1920×1080, titles ≥48px, 4-5 sizes; full rules in decks.md.

## 11. Experience mode (games, toys, celebrations)

- The display face comes from the world (arcade cabinet, stage poster, instrument panel), set big and confident; UI text stays a clean sans at app sizes.
- Scores, combos, timers, count-ups: tabular figures; in canvas use bitmap text for counters (re-rasterising text each frame stutters).
- Text over moving or busy scenes may use a 1-2px dark stroke (`paint-order: stroke fill; -webkit-text-stroke`) or a solid backing plate for legibility. Never as decoration on pages. In video and thumbnails the stroke may be heavier (scaled to the frame, `video.md`).
- Pixel faces (Press Start 2P, VT323) only for genuine pixel art, at integer multiples of their design size.

## 12. International: RTL and CJK

**All scripts**
- `lang` on `<html>` and on inline foreign text: it picks glyph variants, hyphenation and screen-reader voice.
- Leave 30-40% room for translation (German runs ~30% longer); no fixed-width text boxes.
- Logical properties (`margin-inline-start`, `padding-inline`, `text-align: start`) everywhere.
- Full translatable strings with named placeholders; never concatenated fragments or `count !== 1 ? 's'`. Format numbers and dates with `Intl.NumberFormat` / `Intl.DateTimeFormat`.
- Test with 100+ character names, emoji, RTL and CJK strings, and numbers in the billions. Before translations exist, run a pseudo-locale (accented and padded ~35%: "[Šéttîñgš ŵîţĥ éẋţŕà]") to catch hard-coded strings, clipping and concatenation.
- Never auto-redirect by IP or browser language without a visible way back; remember the user's choice (switcher wording: copy.md §7).
- Scripts with tall marks (Thai, Devanagari, Vietnamese stacked diacritics) need leading ≥1.6 and no clipped line boxes; never `overflow: hidden` on single-line labels without checking them.

**RTL (Arabic, Hebrew, Persian, Urdu)**
- `dir="rtl"` on `<html>`; mirror layout, navigation, back chevrons, progress and directional arrows. Do not mirror numbers, logos, media playback controls, clocks, checkmarks or embedded LTR code.
- Never letter-space Arabic (it breaks the joining); no uppercase exists; avoid italics, emphasise with weight or colour.
- Arabic sets optically smaller than Latin: size up 10-20% and use leading 1.6-1.8.
- Keep ZWNJ (U+200C); treat ی/ي and ک/ك as equal in search while storing the original; use locale digits where expected; support Jalali and Hijri calendars where relevant.
- Fonts: Noto Naskh Arabic / Noto Sans Arabic, IBM Plex Sans Arabic, Vazirmatn (Persian), Readex Pro; Hebrew: Noto Sans Hebrew, Heebo, Assistant. Pair the Latin face with one of matching weight and x-height.

**CJK (Chinese, Japanese, Korean)**
- Tracking 0. Body leading 1.7-1.8, display 1.3-1.4. Body ≥16px; measure ~35-45 full-width characters.
- No italics (no true italic exists); emphasise with weight or `text-emphasis`. Never faux bold.
- Line breaking: Japanese `line-break: strict`; Korean `word-break: keep-all`; keep punctuation from starting a line (default kinsoku, check it renders); `text-spacing-trim: normal` collapses doubled full-width punctuation where supported.
- Space between CJK and Latin runs: `text-autospace: normal` where supported, otherwise a thin space; never a full space.
- Set `lang` correctly (ja, zh-Hans, zh-Hant, ko): Han unification renders the wrong regional glyphs otherwise.
- Fonts are huge (5-20MB): prefer the system stack (`"PingFang SC", "Hiragino Sans", "Noto Sans CJK", "Microsoft YaHei"`) or Google's auto-sliced Noto Sans / Serif JP, KR, SC, TC; never preload a full CJK file.
- Vertical text (`writing-mode: vertical-rl`) only for genuinely Japanese or traditional Chinese editorial work.

## 13. Read mode: docs, articles, changelogs

- Calm and typographic: body 18-21px, measure 60-70ch, ratio 1.25, 4-5 sizes, no entrances (motion.md §9). The reader's question decides the heading outline; write the outline before styling.
- Article: title (≤2 lines), one standfirst sentence, byline + date (+ "Updated" when changed), body, then related reading. Images break out to the frame on the breakout grid (layout.md §2); captions in the text face at the small step.
- Docs shell at ≥1280px: left nav 240-280px (≤4 siblings per level, current page marked by weight + neutral fill), content column ~65ch, right on-page TOC 200-240px of h2/h3 with the current section highlighted on scroll. 1024-1279px: drop the TOC to a disclosure under the title. Phone: nav in a sheet, TOC as a "On this page" disclosure.
- Every h2/h3 linkable: `id` slug + an anchor link revealed on hover and focus (always present for keyboard and touch), `scroll-margin-top` clear of the sticky header.
- Wayfinding: breadcrumbs, prev/next at the foot naming the destinations, "Edit this page" and last-updated date where content is community-maintained, version switcher when versions exist, search on `/` and Cmd/Ctrl+K.
- Code blocks: the mono face at 14-15px (0.875em of body), line height 1.5-1.6, horizontal scroll, never wrapped for code (wrap only for prose-like output), language label + copy button (announces "Copied"), a syntax theme built from the tokens with every token ≥4.5:1 in both themes, line highlights as a tinted band, not colour on text alone. Inline `code` on a one-step tint, no border.
- Callouts (note, tip, warning, danger): icon + bold label + text on a one-step tint of the status hue (colour.md), no coloured side stripe; at most one per screen of reading, never nested.
- Tables in prose: caption, left-aligned text, right-aligned numbers, horizontal scroll inside a frame on phone. Footnotes link both ways. `<kbd>` styled as a key; `<abbr title>` on first use.
- Changelogs: newest first, date as the heading, entries grouped Added / Changed / Fixed / Removed, each entry one line starting with the user-visible effect.

## 14. Type checklist

- [ ] Faces chosen from the world, not the overused list or a category cliché; each face has one job; ≤2 families.
- [ ] Persuade: 2-3 working sizes, ≤5 total, adjacent ≥1.25x, display ≥4x body. Operate: fixed rem scale, ≤5 sizes per view, title 18-32px.
- [ ] Hero ≤2 lines at 390 / 768 / 1440, breaks authored, balanced, no orphan.
- [ ] Tracking set per step; display leading checked for collisions; optical left pull on round or diagonal capitals.
- [ ] Body ≥16px (pages) / ≥14px (UI), measure 45-75ch, leading matched to measure, left-aligned, not justified.
- [ ] Nothing <11px; 12px only for ≤3 glance-meta roles.
- [ ] Tabular figures on every numeric column, price, timer and counter.
- [ ] Curly quotes, real ellipsis, nbsp before units, links underlined with offset.
- [ ] Only used weights loaded, fallback metric-matched, the real face confirmed rendering before judging screenshots.
- [ ] Survives 200% zoom and WCAG 1.4.12 text spacing; `lang` set; RTL and CJK strings tested where the product ships them.
