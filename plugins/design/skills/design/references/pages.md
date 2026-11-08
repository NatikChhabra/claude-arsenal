# Persuade pages

Use when building or reviewing a website, landing page, marketing or product site, portfolio, event or local-business page: any surface whose job is to convince a stranger. App screens shown inside the page follow apps.md.

## 1. The argument comes before the layout

- Inventory 8-12 things only this client has before designing: the name and its meaning, the street or neighbourhood, its numbers, its constraint, materials, rituals and hours, printed artefacts, the product's own objects. The page is built from these, not from the category.
- Write the argument and claim list first (copy.md §1): one claim + its proof per section, a section with no claim is deleted, the argument's order is the page's order.
- Never default to hero → logos → 3 features → testimonial → pricing → FAQ → CTA. Include at least one section the category never ships (an inline demo, pricing as a comparison against the status quo, the real menu as the hero).
- Answer the visitor's question chain where each question arises: What is this? → Is it for me? → Why this one? → Can I trust it? → How does it work? → How much effort and money? → What next?
- Answering out of order is a defect both ways. Put price on the first screen only when price is the first question (one product, a ticket, a menu, a room rate). Tiered SaaS pricing comes after the value case.
- When the subject suggests no better order, a working spine: hook → the problem in the reader's words → the one-sentence difference → 3-5 benefits, each beside its proof → how it works in ≤3 steps → the real stakes (no fake scarcity) → the action.
- Copy deck before markup: every headline, sentence, button and caption written first, in tight copy (section paragraphs ≤25 words, headlines ≤8 words). Voice and wording rules live in copy.md.
- Deliver every section the brief asks for, complete: the whole menu with prices, every room, every speaker. Write plausible sample details where the brief gives only the shape, and list them in the report for the client to confirm.
- Page length follows content. Median strong site is ~9 screens and ~575 words; a quarter are 1-2 screens. Never add sections to look complete.

| Subject | The first screen must say |
|---|---|
| Product | what it is + what it does, or its price if single |
| Event | what, when, where, in the headline or the second size |
| Person / studio | who + what they make; the work itself leads |
| Restaurant / shop | what, where, hours, the booking or order action |
| SaaS / tool | the job it does for whom, + the real product visible |
| Case study | the work itself large, then client, role and outcome (a real number) in one line |

## 2. Idea sentence and the one live thing

- Write the idea as: "On this page, [thing from the subject] becomes [device]." Example: "the menu card becomes the page grid", "the shipment's real route becomes the scroll".
- Competitor test: swap in the nearest competitor's name. If the idea still works, it is a category idea; redo it.
- Memory test: what would someone describe an hour after one viewport? A mood means the concept never committed.
- Carry the idea to the last pixel. Ask of every section, pricing, FAQ and footer included: what does the idea do here? If the page is a menu, prices are menu lines; if the name is a monument, the footer is the name again; if the object's shape is the motif, masks and buttons carry it.
- Build exactly one live thing: an interactive piece with real content that proves the claim. Examples: the real search, a configurator, a playable sample, a calculator with real figures, a before/after slider of the product, a working fragment of the app.
- The live thing must be thumb-usable, keyboard-usable, work or degrade to readable content without JS, and never block reading or scrolling.
- Where possible the first viewport's primary action is the real action (a search field, add-to-cart, a booking date) rather than a link to it.

## 3. Hero and first screen

- The first viewport is a thesis, not a header: one focal thing, legible within 1 second, and the stranger knows what, for whom and what next within 5.
- One `<h1>` on the first screen. ≥32px desktop (strong sites 50-150px, median 72px; phone median 40px), display ≥4x body, ≤2 lines at every width, sentence case, no full stop, no fixed size cap.
- Focal point check: the largest type is ≥4.5vw (strong sites 6-8vw) or one picture fills ≥30% of the first screen. Neither means no focal point.
- Headline budget, fit arithmetic and the supporting line: copy.md §3-4 (~32 characters; supporting line ≤22 words, 32-48px below). A bare-name headline needs an ≥18px line under it saying what it is.
- ≤4 text elements in the hero: headline, supporting line, primary action, optional secondary text link. No pill badge ("New", "Beta"), no eyebrow, no tagline under the buttons, no trust micro-strip, no scroll cue.
- One real primary button visible without scrolling at 1440×900 and 390×844. Most strong heroes carry 0-1 buttons; a second action is a text link.
- One primary action, one name page-wide. Repeat it once at the close of a long page, never twice in one viewport; other entry points are text links with different wording. Three or more same-action buttons is a failed page.
- Hero media takes ≥50% of the first screen on most strong sites. One dominant image beats six small ones.
- Hero top padding ≤96px; nav ≤~1/10 of the first screen. Content must not float halfway down the viewport.
- Size the hero to its content. When it is a real full screen use `min-height: 100svh` (never `100vh` / `h-screen`); the headline, sentence and action must still fit on a 390×664 visible phone screen.
- Paint headline, sentence and picture in HTML on the first frame. No preloader, gate, counter, entry pop-up or blank first paint.
- Banned hero templates: centred headline + subtitle + two buttons + screenshot or tile grid; split hero with copy left, product right, badge row under; centred headline over a row of cards; text + gradient blob; a first-viewport column that runs far below the fold.

Hero compositions that work (pick by subject):

| Composition | Geometry |
|---|---|
| Cut-out object on a flat field | object 35-60% width, field sampled from its own colours; the highest-scoring form |
| Full-bleed photo or loop | text in a calm corner ≥32px in; headline + one line + one action only |
| Split picture | picture 42-50% (or 2/3) width, full height, touching the viewport on its outer side; text on the 50% line |
| Monument type | headline or wordmark at viewport width (`font-size ≈ width ÷ (chars × k)`, nowrap), verified at 390 and 1440 |
| Opening window | small inset picture that grows to full bleed over ~1 screen of scroll, readable at progress 0 |

## 4. Section composition and variety

- Every section opens with a real heading in the heading face, on the margin or anchor line, consistent page-wide. Plain names are fine ("Prices", "The rooms", "How it works"). No eyebrow, kicker, mono label or 01/02/03 above it (tells.md).
- Default section shape: heading 2-5 words (≤8) + one paragraph ≤25 words + one visual or one action. More must be earned by the section's job.
- Name each section's layout family before building: statement, split, full-bleed, mosaic, list, index, table, strip, gallery, pinned scene, figure, quote.
- No two neighbours share a family. ≥4 families across 8 sections. Never 3 consecutive image-text splits. A family used 3 times anywhere is the template showing.
- Alternate dense and empty, image and type, light and dark, so the scroll has rhythm. Follow a dense passage with a quiet one.
- A repeated module (identical cards, rows) is for archives only: a work index, a menu, a schedule. Anywhere else it reads as a kit.
- Never three identical icon-topped feature cards. Never a bento as the feature section by reflex; if a bento is truly right, N items get exactly N cells with no empty cell, and cells differ in content type (image, figure, product fragment).
- Break the page's own system once, on purpose: one centred line, one inverted section, one picture at a different scale.
- More than 5 items is a different component, not a longer list: grouped 2-column split, picture + label grid, 3-5 highlights + "View the full list", a snap row. Never a 10-row spec table with a rule under every row; group into 2-3 headed clusters or feature 3-4 specs large and disclose the rest.
- No data dumps on a marketing page (20-row tables, 30 awards, a giant pricing matrix). Link to a page of their own.
- Section headers stack vertically (heading, then body). No big heading left with a small explainer floating top-right.
- Use the width: text in one half means a picture, second column or list in the other. No empty middle third, no huddled half.
- Every screen reads as a composed poster; never ≥2 near-empty screens; no plain-ground stretch longer than half a screen. If a section looks empty, make its main element bigger or cut the section.
- Size sections to content. One deliberate rest per page, and only where something closes the void (a picture across the band, type spanning it).
- Section grounds: chapters may change the whole ground with a hard edge, never a fade or gradient. Each field has its own ink; neighbours differ in lightness; `<meta name="theme-color">` and the nav follow the first field. Colour roles live in colour.md.
- Hairlines and 1px boxes are not used as decoration on Persuade pages; separate by space and tone.
- Gaps, margins and grid arithmetic live in layout.md (section gaps 120-240px desktop, 72-112px phone; between-section gap clearly larger than any within-section gap).

## 5. Navigation and footer

- Nav: wordmark at one end, 3-5 single-noun text links (median 3), one action, at text size on the page ground. No bar chrome, border or pill container. One line, ≤80px tall.
- Less is normal: corner links, a single action, or the content's own section list as the index.
- Wordmark links home. `aria-current="page"` on the active link. A skip link is the first focusable element.
- Fixed or sticky nav never covers content at any scroll position; check every screenshot, phone first. Give it a solid ground once content scrolls under it and set `scroll-padding-top` to its height.
- A translucent blurred bar is allowed only as a functional bar over scrolling content, with a solid fallback under `prefers-reduced-transparency: reduce`. Never a floating blurred pill.
- With colour-by-chapter grounds, the fixed header's ink follows the chapter beneath (300ms).
- Phone: wordmark + one action in one row; links in a full-screen sheet opened by a text button "Menu" (focus trapped, Esc closes, closes on navigation), or moved to the footer when there are only 3.
- Footer is a designed close, never default link columns. Strong endings: the name at full width, the hero repeated inverted, one contact fact set as a headline, a closing scene (curtain footer: `position: sticky; bottom: 0` under a `main` with its own background and higher `z-index`), or one quiet line.
- Practical facts (address, hours, email as `mailto:`, phone as `tel:`, legal line, picture credits) in the text face at body size and full contrast, on the page's anchor lines.
- A site with 20+ pages may need a link index: set it as a designed index in the text face at readable size, not four grey 13px columns.
- No "©2026, Scroll", version stamps, local-time or weather strips, "Est. 2024", status dots.

## 6. Imagery

- Source order: the project's own assets → real, licensed pictures of the subject's world (Openverse, Wikimedia Commons, museum open-access; commercial licence; credited; never presented as the client's own) → generated (photographer's brief: subject, angle, light, background, ratio, "no text"; hero first, then match its light) → drawn in code from the subject → type and colour alone.
- Real referents (the product, the place, the people, the founder) get real photographs, never generated or drawn stand-ins. Missing ones get a labelled slot listed in the report.
- Never placeholder CDNs (picsum, random Unsplash), grey boxes left in, or invented portfolio work.
- Never draw or reconstruct a real logo. Without the file, set the name as a text wordmark and flag it in the report.
- Floor: ≥4 real pictures, usually 6-12. SVG drawings do not count; interface fragments count for software. A type-only page is a deliberate, stated exception.
- About a third of page area is picture (30-40%); ≥1 screen in 4 has none. A picture either leads its screen (≥60%) or stays under 10%.
- 3-5 placement types per page, no two neighbours alike. One moving picture per screen at most.
- Search for the subject's physical object, not the category. One decisive photo beats five mediocre ones. All pictures one family: same light, grade and kind of subject.

| Placement | Geometry |
|---|---|
| Split | 42-50% (or 2/3) width, full section height, touches the viewport on its outer side |
| Full-bleed band | 100% × 100-150vh, every 3-4 screens; oversize ≤10% for parallax; text in a corner ≥32px in |
| Opening frame | inset 35-50% → full bleed over 720-2,700px of scroll, once per page |
| Horizontal gallery | cards 25-35% width (phone 75-80%), 16-20px gaps, 3 visible + a cut 4th, native scroll-snap |
| Uneven mosaic | 2-3 widths, vertical offsets 120-190px |
| Even grid | archives only: one ratio, 8-16px gaps, caption under |
| Index with preview | text rows 45-80px pitch, hovered row shows its picture, swap ≤0.3s, works on tap |
| Chips in a statement | small pictures inline in large type, 2-4 max |

- Crops: two ratios cover ≥75% of pictures (defaults 4:5 portrait, 3:2 or 16:9 landscape). `object-fit: cover` with a per-image `object-position` chosen by eye. Go large, touch edges, bleed from a margin.
- Rows of mixed pictures: align bottoms or crop to one ratio. Overlap at most one pair per screen, by 40-80px.
- Corners square (the large majority of strong sites); if rounded, one small radius everywhere. No borders, shadows, device mockups or browser chrome.
- Captions: one short line, small, soft ink, left-aligned under the picture. No pills or labels overlaid on pictures, no fake photo-credit captions.
- One treatment for all pictures, text on photos and scrims: colour.md (Photos and colour). Never duotone, grain or vignette on pages (video grades and photo composites follow `video.md`).
- Markup: `width` + `height` always; `alt` that carries the picture's information (`alt=""` if decorative); a ground-colour `background-color` on frames; files downloaded, never hotlinked; 2x the CSS width, capped ~2400px.
- Formats: `<picture>` AVIF → WebP → JPEG, `srcset` with w-descriptors (e.g. 640/960/1280/1920/2400) and an honest `sizes` (never a 2000px file into a 400px slot); WebP ~80 quality or the lowest that stays clean at 2x; `<picture>` media sources for art-directed phone crops.
- Hero image: `fetchpriority="high"`, never `loading="lazy"`; everything below the fold `loading="lazy" decoding="async"`.
- Credit found pictures in one footer line at body size, with links.

## 7. Video

- Loops: 5-20s seamless (median 10s), slow continuous motion, no hard cuts.
- `<video autoplay muted loop playsinline preload="metadata" poster="…" width height aria-hidden="true">`. Poster required; it is the LCP element, so preload it like a hero image.
- Sources: WebM (AV1 or VP9) then MP4 H.264; strip the audio track.
- Budget: ≤5MB per section loop, ≤10MB for the hero; ≤720p behind type.
- Play only while in view (IntersectionObserver pause/play); pause when the tab is hidden.
- Loops longer than 5s beside other content get a visible pause control (WCAG 2.2.2).
- Under `prefers-reduced-motion: reduce`: no autoplay, show the poster.
- Found footage: 1-2 clips per page. Nothing important lives only on hover or only in the video.
- Video with speech or meaning gets controls, captions and a transcript, and never autoplays with sound.

## 8. Software shown on the page

- Show the real product. Build interface fragments as real HTML at true size with believable data: numbers add up, names have real lengths, one item is selected, the state is mid-task.
- Crop to the point: show the part that proves the section's claim, not the whole app shrunk. Never scale a fragment so its text renders under 11px; crop instead.
- Mark the root `data-ui`; inside it app rules apply (apps.md): 1px structural lines, small labels, tabular figures, the product's real radius and type.
- Seat a fragment on the page ground or a one-step tonal panel. No device frame, browser chrome, resting shadow or floating tilt.
- Make a static fragment `inert` with a text alternative on the figure (`role="img"` + `aria-label`, or a caption). If it is the live thing, make it fully operable instead.
- A real screenshot is acceptable: 2x resolution, cropped, never upscaled, with real data.
- Never fake screenshots from grey div bars, decorative terminals, typewriter code, sparkles or faux-AI shimmer.
- Never claim "coming soon" on a shipped feature or show a feature that does not exist.

## 9. Scroll stories and scenes

- A scene is a tall section whose stage holds still while the page scrolls: stage `position: sticky; top: 0; height: 100svh`; section height = (hold + 1) screens; a timeline is scrubbed 0→1 by that scroll. Sticky beats JS pinning when nothing transforms.
- Count, length and pacing: motion.md §8 (2-3 scenes, 1-3 screens each, ≤60% of the page). Pick scenes from different families, each on the section of the argument it can carry. ~1 screen per story beat with a line of text on every held screen; a hold with nothing new is cut, not padded.
- Words: a held statement is 4-12 words, captions 1-4 words, one statement on screen at a time, readable whole at every rest point. Nothing passes over text while it is being read.
- Pictures: one family, decoded before they move (gallery reveals: start loading one screen ahead, add the reveal class only after `img.decode()`, or a lazy image wipes in blank). The scene must say something about the subject (the real route, the four rooms, the product changing state). Unrelated pictures make it a gimmick. Too few real pictures means a different scene, never stand-ins.
- Native scroll only: no wheel capture, no scroll locking, no click-to-advance scenes.
- Counts, when needed, are plain ("2 of 4"). No hairline progress bars, no "01/08".
- A scene on the first screen is fully readable at progress 0 and starts moving only when the visitor scrolls.
- Every scene section has a heading (or `aria-label` plus a real heading in the finished composition).
- Design the finished composition first, in CSS. It is what reduced motion, no JS, a failed CDN and some phones see; the live version goes under `.scene.is-live`. Nothing is hidden waiting for a script.
- Each scene has a phone plan: same scene with changed numbers, a simpler version, or the finished composition at rest. Touch scroll is never smoothed.
- Mechanics (reveal style, scrub, native timelines vs GSAP, smooth scroll, sideways tracks, canvas frame sequences, compositor-only properties): motion.md §8. Verify at 0, 10 … 100% progress per process.md §9.

## 10. Page motion budget

- A Persuade page moves: one signature move chosen by subject (table below), 2-3 scroll scenes, per-section entrances varied by content, feedback on every control, ≥8 moving elements (aim 16). Load sequence, reveal mechanics, parallax, marquee, view transitions and the never-list: motion.md §8-9. A still page or one uniform fade-up reads unfinished unless the direction is deliberately static and says why.

Signature moves, picked by subject (one per page):

| Move | Fits | Build |
|---|---|---|
| Masked headline | type-led brands | lines rise from behind their baselines on load |
| Shutter image | a product's hero object | picture opens from an edge, settling from 1.12 scale |
| Opening window | a product or place with one great photo | inset frame → full bleed over ~1 screen |
| Sheet over a held picture | chapters that each own a photo | 100svh sticky figure, next section slides over with its own ground, no script |
| Index with preview | portfolios, collections | text rows, hovered row shows its picture |
| Slow crossfade | restaurants, places | 3-4 photos, 5-6s each, visible pause control, paused when hidden, first photo static under reduced motion |
| Sideways gallery | a short set of rooms or pieces | pinned row under 3 screens, or native snap row |
| Pushed line | a brand whose claim is one word | `view()` timeline, `translateX` 12% → -12%, linear |
| Rolling figures | a report, a fund, a handful of real numbers | count up once, `tabular-nums`; the real number stays in the HTML for readers and search |
| Curtain footer | a page that should end as a scene | sticky footer revealed from under `main` |

## 11. Social proof

- Proof rules (never invent, sample-content fallback, no fake scarcity): copy.md §5. Layout rules here.
- Real customer logos only when they really are customers and permission exists. Logo wall sits under the hero, never inside it; logos only, no category labels under them; one monochrome treatment at matched optical size; 4-8 logos in one row (phone: 2-3 per row or a slow marquee); `alt` is the company name. Heading plain ("Customers include") or none, never "Quietly trusted by".
- Proof sits next to the claim it proves, not in a separate "testimonials" ghetto.
- Demonstration beats testimony: show the thing working, large, then state how it works specifically, then use brief facts (price, place, year, materials, what's included).
- A quote is real, ≤3 lines of body, attributed with full name, role and organisation (a face photo only if real and permitted). Set it as `<blockquote>` + `<cite>`, at statement size (≤36px desktop, ≤24px phone).
- Numbers carry their source and date ("4.8 from 2,140 App Store ratings, Oct 2026"). Rounded honest figures beat fake-precise ones.

## 12. Pricing and forms

- Carry the page's idea into pricing: a menu prices as menu lines, a studio prices as a short written offer, a product prices on its own picture.
- 1-4 plans. Name plans by who they are for, not by metals or gems.
- The price is set at heading size in the display or text face, with `tabular-nums`, the currency symbol, and the billing period and tax status stated plainly ("€12 per seat / month, billed yearly, excl. VAT").
- Mark one recommended plan by position and fill, not by a shouting badge; at most one short label naming why ("Most teams pick this").
- Each plan lists only what differs from the previous one ("Everything in Starter, plus…"), ≤5-7 lines.
- Each plan has one action naming the outcome ("Start free trial", "Book a call"); the top tier for sales-led products is "Talk to sales" with what happens next.
- A monthly/yearly toggle shows the real saving in currency or months, defaults to the period most buyers choose, and never fakes a strikethrough price.
- The full feature comparison table goes below the plans or on its own page; on the phone it becomes one plan per screen with a plan switcher, never a sideways-scrolling matrix.
- Put the 2-3 objections that block purchase (cancellation, refunds, data ownership, trial terms) directly under the plans.
- Missing prices and missing checkout: copy.md §5 (`[YOUR PRICE]`, real destination or flagged stub, never a fake payment form).
- Sign-up and contact forms ask only what the next step needs (a newsletter is one email field), labels above fields, a real `action`; on success the form is replaced in place by what happens next and when.

- A price calculator: ticking a row adds it; totals count up once (~400 ms, none under reduced motion); every money
  line a buyer will be told on the phone is in the total block (total, deposit, and the deposit after any launch
  discount), worked the same way as the quotes the business sends. A sticky total bar shows while the table is in
  view and the total block is not.
- Say shared terms once under the plans ("On both: ...") and let each plan list only what is its own.

### Contact without leaving the page (in-game and roleplay businesses)
When the visitor can't dial from the browser (a game phone, a roleplay number), the number is a `<button>` that copies
it: `navigator.clipboard.writeText` in a secure context, a hidden-textarea `execCommand('copy')` fallback, and an
on-page `role=status` note ("Copied 834-...: paste it in your phone"). No `tel:`, `mailto:` or links that open another
app. The same button sits in the sticky header, the hero and the footer, each at least 44 px tall on a phone.

## 13. FAQ

- Questions come from real sales, support or search queries, in the visitor's words. 4-8 questions; fewer, sharper beats more.
- Answer in 1-3 sentences that state the fact first, with a link for depth. No hedging, no marketing.
- ≤6 questions: show them all open (questions as headings, answers visible, two columns on desktop). Hiding six short answers behind an accordion is the stock block.
- More than 6: native `<details>` / `<summary>`, each question a real heading level, animated with `grid-template-rows: 0fr → 1fr` over ~320ms, open state indicated by more than an icon rotation.
- FAQ structured data rarely earns rich results now (Google limits them to authoritative government and health sites); add `FAQPage` JSON-LD only when it is cheap and honest.

## 14. Semantic HTML and SEO

- Landmarks: `header`, `nav`, one `main`, `section` with a heading, `article` where content stands alone, `aside`, `footer`. One `<h1>`; no skipped heading levels; visual order = DOM order = focus order.
- `<a href>` for navigation, `<button>` for actions, `<details>` for disclosure, real `<form action>` that submits without JS. No clickable divs.
- `<html lang>`; `lang` on inline foreign-language text; `<meta name="viewport" content="width=device-width, initial-scale=1">` without zoom locks.
- `<title>` 50-60 characters, unique per page, the reader's phrase first ("Stools for small kitchens | Brand"). Meta description 120-160 characters, a real sentence.
- `<link rel="canonical">` on every indexable page. `hreflang` (plus `x-default`) on multilingual sites. `noindex` on staging and preview hosts.
- Open Graph `og:title`, `og:description`, `og:image`, `og:url`, `og:type` + `twitter:card` = `summary_large_image`. OG image design and sizes: decks.md (Social and OG images).
- Favicon set: `favicon.svg` (with a dark-mode media query if needed), a 32px `favicon.ico` fallback, a 180×180 `apple-touch-icon`, a web manifest with 192 and 512px icons (plus a maskable 512). Drawing them: systems.md (Brand identity).
- JSON-LD where true: `Organization`, `Product` (+ `Offer` with real price), `LocalBusiness` (address, hours, geo), `Event`, `Article`, `BreadcrumbList`.
- Content is in the HTML. SPAs server-render or pre-render indexable pages and update `document.title` and meta per route.
- URLs are short readable slugs. On a redesign keep every existing slug, or 301 it; keep analytics IDs and form field names.
- `sitemap.xml` and `robots.txt` for multi-page sites. A designed 404 that returns a real 404 status, says what happened in one line, and links home and to the main sections.
- Cookie banner: compact, bottom, never covering the hero action; Accept and Reject equal in weight; nothing non-essential runs before consent.

## 15. Core Web Vitals and performance

- Targets at the 75th percentile on a mid-range phone: LCP ≤2.5s, INP ≤200ms, CLS ≤0.1. Lighthouse Performance ≥90, Accessibility 100, Best Practices ≥95, SEO ≥95.
- Budget for first view: ≤~1MB transferred excluding video; ≤~150KB compressed JS; 2-3 font files.
- LCP: hero image or poster sized to its slot, AVIF/WebP, `fetchpriority="high"`, `<link rel="preload" as="image" imagesrcset imagesizes>` when it is not discoverable in HTML; inline critical CSS; no render-blocking scripts.
- CLS: `width`/`height` or `aspect-ratio` on every image, video, embed and ad slot; reserve space for late content; inject nothing above existing content; size-matched font fallbacks (`size-adjust`) so the swap doesn't shift lines.
- Fonts: typography.md §8 (2-3 woff2 files, subset, preload the display face, metric-matched fallback).
- INP: `defer` scripts, `async` third parties, split long tasks, no main-thread scroll listeners (IntersectionObserver, CSS scroll timelines, ScrollTrigger), passive pointer listeners coalesced into one rAF.
- Below-the-fold sections: `content-visibility: auto; contain-intrinsic-size: auto 900px`.
- Heavy pieces (3D, Lottie, scene libraries, embeds): load on approach via IntersectionObserver or dynamic `import()`, with a sized placeholder or the finished composition; pause off-screen and in hidden tabs; cap DPR at 2. 3D only when the object is the subject (motion.md and experience.md).
- Third-party embeds (maps, video players, chat widgets) load as a click-to-load facade with a static preview.
- Measure before and after on the production build, not the dev server; on a real site enforce the Lighthouse targets in CI.

## 16. Marketing system vs product system

- One chassis, two expressions: systems.md (Marketing vs product systems). A mixed request (site + app) is two builds on one palette and one type family; product fragments on the page use the product system inside `data-ui`, unchanged.

## 17. Before calling a page done

- Render and screenshot at 1440, 768, 390 and the real target viewport; open every picture after the last change. Phone is its own composition: re-authored line breaks, re-cropped pictures, 16-20px margins, ≥44px targets.
- 5-second stranger test passes: what, for whom, what next.
- Competitor test passes; the idea reaches pricing, FAQ and footer.
- Every requested section is present and complete; every sample detail and flagged placeholder is listed in the report.
- No headline over 2 lines, no covered or clipped text at any scroll position, no blank band from an unfired reveal, no horizontal overflow.
- Reduced motion and no-JS both show the full finished page.
- Vitals and Lighthouse targets met on the production build; title, description, canonical, OG image and one `<h1>` present.
- Critique process, scoring and fix order live in process.md; the full anti-slop list lives in tells.md.
