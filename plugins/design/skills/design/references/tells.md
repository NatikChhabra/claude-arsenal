# Anti-Slop Tells

Use when: building, reviewing or critiquing any surface (page, app screen, game UI, deck, prototype). Video, thumbnails and covers have their own tells in `video.md` and `edit.md`; the surface bans below are web and app rules unless a line says otherwise. Scan for every tell before showing work; each one found is a fix, not a style choice.

## Ground rules
- A tell is a default reached for without a reason. The brief, a project DESIGN.md, or the user's words override any item here; a pinned font, era or palette is honoured even when it matches a tell. Examples: a brand that owns neon on near-black keeps it (never add the glow); a pinned display face beats the font tells; the owner's own tools may use purple and pure-black grounds when he asks.
- Test for slop: could someone guess the look from the category alone, or from the category plus what it avoids? Swap in the nearest competitor's name: if the page still works, it is a template.
- Memory test: one hour after seeing the first viewport, a stranger should describe a thing, not a mood.
- Fix by removing. Never refill a removed tell with another ornament. A negative brief ("no hype", "minimal") removes devices, not energy.
- Mode matters: Persuade and Experience ban more decoration; Operate allows structural lines, labels and identical peer cards (see apps.md). Each bullet below states its exceptions.
- Score caps (process.md): a 3+ line headline, eyebrow, mono labels, 01/02/03, decorative gradient, resting shadow or visible hairline caps a Persuade page at 6.5 overall.

## The AI looks (clusters to escape when the aesthetic was left free)
| Look | Signature | Escape |
|---|---|---|
| SaaS indigo | white ground, indigo/violet accent, purple-to-blue hero gradient, glow, rounded icon cards | hue from product meaning, flat fills, one accent with a whitelist |
| Warm cream editorial | cream/beige ground, high-contrast or italic serif display, terracotta/rust/clay accent, espresso text | treat the palette as spent; colour from the subject's saturated materials (cloth, paint, packaging) |
| Broadsheet | hairline rules everywhere, italic display serif, tiny tracked mono labels, 01/02/03 sections | type hierarchy from size and space, no rules, no mono labels |
| Dark neon | near-black ground, one neon accent (cyan, lime, violet), glowing edges, grid background | tinted dark ground, depth by lighter surface steps, no glow. A pinned brand palette of this pairing is identity, not slop: keep it, drop the glow and the grid |
| Neobrutalist costume | flat saturated ink, black boxes, hard offset shadows `4px 4px 0`, heavy condensed display | only when the world is genuinely neobrutalist and the brief says so |
| Glass bento | frosted cards on a gradient blob, bento grid of rounded tiles, floating pill nav | solid surfaces, layout from content, plain text nav |
| Kit face | stock shadcn/Geist/Inter on `#f8f8f8`, white 12px-radius cards, no hue on data, or lime on black | rebuild every atom in the chosen form; a component library is never shipped in its default state |
| Category sticker | a neutral template with the brand accent dropped on it | colour and form commit at page scale |

- Warm, bookish, family or child subjects drift to cream, italic serif and lamplight by default. Start elsewhere.
- Choose light or dark from one written sentence about the physical scene (who, where, what light), never from the category ("fintech is dark").
- Vary light/dark, faces and aesthetic across projects; converging on one house look is itself a tell.

## Layout and structure
- Centred headline + subtitle + two buttons + screenshot or card grid below. The single strongest weak-site signature.
- Stock order hero → logos → 3 features → testimonial → pricing → CTA. Order the page by the argument (pages.md); break the sequence with at least one section a template would not have.
- Three identical icon-topped feature cards; any row of identical cards on Persuade. Bento of rounded tiles as the feature section. Operate exception: identical cards for true peer objects or metrics, 3-6 across, no icon on top.
- Split hero: copy left, product right, badge row under it.
- Hero-metric template: big number, small label, row of stats, accent colour.
- Distinctive hero followed by stock blocks (three-up cards, accordion, link-column footer). Carry the idea into pricing, FAQ and footer.
- Neighbouring sections sharing a layout; the same layout used 3x on a page; 3+ consecutive zigzag image/text splits. Name each section's layout in one word: no repeats in a row, none 3x.
- Everything centred (>70% of text centred). Centred paragraphs over 3 lines.
- Container of 1100-1300px centred by reflex with full-width things squeezed into it. Constrain text measure, not pictures.
- Huddled sections: text in one half, the other half empty. Empty middle third. Blank stretch over half a screen; 2+ near-empty screens. Unequal outer margins; nav on a different inset than content.
- More than 3 distinct left edges for text on a page (6 means undecided).
- Body text closer than 16px to the viewport edge (12px at ≤480px wide); cards flush to the viewport edge.
- A text section with no heading; no `h1` on the first screen, or more than one `h1`.
- No focal point: largest type under ~4.5vw and no picture over 30% of the first screen.
- Broken integrity: overlapping elements, clipped or overflowing text, `white-space: nowrap` forcing a fit, display type wider than its column, sideways scroll.
- Nav as a boxed bar (fill, border, shadow), more than 5 links, or taller than ~1/10 of the first screen.
- Phone as a shrunken desktop: same line breaks and crops, a sidebar over 30% of the width.
- Floating explainer paragraph top-right of a big section headline with nothing tying them to one baseline.
- First-viewport multi-column layout where one column runs far below the fold.
- Nested cards: card inside card, panel inside panel. Always wrong; max 2 surface levels and the inner one switches strategy (see layout.md).
- `min-height: 100vh` on sections that are not real full screens; `h-screen`/`100vh` instead of `dvh`/`svh`.
- Preloaders, intro gates, entry pop-ups, newsletter modals on arrival, blank first paint, counters before content.
- Perfect symmetry with no tension anywhere on the page.
- A second element competing at the same scale as the lead. Busy is louder, not bolder.
- A modal for a task that needs neither interruption nor protected focus.
- A poster viewport with no working parts: Persuade's first viewport needs the real primary action (a search, an add-to-cart, a booking), not a link to it.

## Surface and decoration
- Decorative gradients: backgrounds, buttons, text (`background-clip: text`), blobs, mesh, aurora, two-stop purple→blue or blue→cyan heroes, `repeating-linear-gradient` stripes, gradient borders. Allowed only: a neutral scrim over a photo, and data ramps (heatmaps, sequential scales).
- Glow: zero-offset coloured halo, coloured blurred shadow on dark, radial "spotlight" washes, glowing buttons, `text-shadow` for effect. Exceptions: glow inside a display well that carries live data (an LED, a meter, a lit key); text over video and thumbnails, where an outline, stroke or hard offset shadow is how words read over moving footage (`video.md`).
- Shadows on resting elements on Persuade. Operate: resting card at most a small blur under 8% black; real shadows for menus, popovers, dialogs. Never border + soft shadow blur ≥16px together on every card ("ghost card").
- Glass/backdrop blur as card decoration; floating blurred pill nav. Allowed only for a functional translucent bar over scrolling content, with a `prefers-reduced-transparency` solid fallback.
- Hairline dividers, 1px outlined boxes, ruled grids, `border-top` + `border-bottom` on every row, crosshairs, crop marks, dashed guides, drawn grid backgrounds on Persuade. Operate allows 1px structure at ~1.1-1.3:1 contrast; dashed only for chart reference lines and empty slots.
- Coloured side stripe: `border-left`/`border-right` over 1px on cards, alerts, callouts, testimonials, especially with rounded corners. A thick accent edge never shares an edge with a radius.
- One medium radius (9-16px) on everything by reflex; card radius ≥32px; mixed radius families with no rule. Pick sharp, soft or pill once (layout.md).
- Hard offset shadows `4px 4px 0` outside a genuinely neobrutalist world.
- Faked physicality in CSS: bevels, emboss, stamped metal, chalk, paper texture, leather. Exception: a physical-material metaphor drawn from the subject's own gear (a pedalboard for a guitar tool, a lit keycap) when the owner picked it from shown options; even then no fake controls that do nothing.
- Neumorphism anywhere accessibility matters.
- Grain overlays, `feTurbulence` noise, vignettes, colour washes, duotone by default, tilted polaroids, scattered floating shapes, dot grids, wave dividers, blob dividers. Web and app rule. On video grades, thumbnails and photo composites, ONE light grain pass and one soft vignette over the whole frame is the unifying finish that stops the pasted, plastic look (`video.md`); a round sticker border is allowed there only on 1-2 graphic props, never on a character in its own scene (`video.md` §1.12).
- Custom cursors, cursor followers, magnetic buttons on every control.
- Pulsing status dots without live data ("Available for work"), blinking fake cursors, sparkle glyphs, rotating badges.
- Many-vertex `clip-path` or geometric masks faking an organic or photo edge; a hero-sized SVG assembled from primitive shapes.
- Gradients, glass, icon tiles, clip-paths, sparklines, progress rings or soft rounded rectangles standing in for real content or assets.
- Opacity used as a tint (`rgba(brand,.12)` fills) instead of real tint tokens; translucent stacks whose contrast depends on what sits behind.
- Unthemed browser surfaces: default `::selection`, caret, scrollbars, focus ring and link underline offset. The most-skipped tell.
- Hover or focus states that lower contrast or grey the text; `outline: none` with no `:focus-visible` replacement.

## Type
- Eyebrow or kicker: tiny uppercase tracked label above a heading; pill badge "New", "Beta", "Introducing", "v2.0 is here" above the hero. Banned on Persuade and Read. Operate allows grey sentence-case field and group labels, at most 1 tracked uppercase label per screen.
- Monospace as a "technical voice" for labels, captions, nav or eyebrows. Mono only for code, IDs/keys, or all figures as a deliberate tabular style. Never mono + uppercase.
- Index numbering as decoration: 01/02/03, (001), "Step 2", "Phase 02", `01 / 04`, `00 / INDEX`, zero-padded counters. Allowed only when the sequence is real information (actual steps, ranks).
- One accent word styled differently in a headline: italic serif, colour, underline, highlight, pill. Two families inside one headline.
- Headline as a 3-4 line sentence; full-sentence H1 at display size; hero headline over 8 words; an orphan word on its last line. Max 2 lines at every width (typography.md, copy.md).
- Timid hierarchy on Persuade: display under 4x body; adjacent sizes under a 1.25x step; 9+ near-equal sizes. Operate fails the other way: titles over 32px, any figure ≥48px.
- Body leading under 1.3; body lines over ~80ch.
- Everything bold; weight change on hover (reflow); 700+ used for more than one job.
- Overused faces as display or brand type (list: typography.md §1). A neo-grotesk for dense app UI is fine when chosen on purpose.
- The closest installed system font as the "fallback" for an own-world page; Impact or Arial Black as the display voice (unless the brand pins it).
- Subject cliché as the reason for a face: books get a serif, tech gets mono, kids get rounded.
- Vertical rotated text; `<br>`-split italic headlines; outlined or stroked display text (on pages; text over video and thumbnails is exempt).
- Display tracking tighter than -0.04em (-0.05em only on a tight grotesk checked by eye); positive tracking on body (over 0.05em fails); all-caps runs over ~3 words or 80+ characters.
- Justified text in narrow columns; straight quotes and `...` instead of curly quotes and `…`; proportional figures in tables, prices and timers.
- Body under 16px on pages; product UI default under 14px; anything under 11px; more than 3 roles at the 12px glance floor per screen.

## Colour
- Violet, indigo, purple-blue, fuchsia accents and glows by default; cyan on dark; neon accent on near-black. By default only: a pinned brand palette, brand reaction art and the owner's own tools (purple on request) are exempt. The purple-blue AI gradient is never exempt.
- A third accent colour on one screen; red in UI when the owner has said no red (thumbnails, photos, brand reaction art and a game's own death screen are not UI).
- Cream or beige page ground by reflex; cream + terracotta/rust/clay/brass/oxblood accent + espresso text. Warmth is not beige: use low-chroma stone/bone/putty (saturation under ~15%), deep green/brown ink, photos, or a full flat warm field.
- Pure `#000` text on pure `#fff`. Allowed when deliberate (stark two-tone, app dark ground `#000`); otherwise tinted neutrals.
- Navy/slate dark grounds by reflex in apps. Dark app grounds are neutral near-black (`#000`, `#111`, `#171719`) unless the brand says otherwise.
- Accent sprayed everywhere: on headings, icons, bullets, borders, every button, every tab, inactive states. Accent is under 5% of any Persuade screen (~3% coloured pixels in apps) and sits on the action, selection and state only. Accent on more than 2 kinds of thing per screen is a warning (colour.md).
- Rainbow palettes; a coloured icon per category; more than 4 hues in one chart (over 6 fails).
- Grey text on a coloured ground. Use a darker shade of that hue or near-white.
- Red/green as the only signal; status colour on a primary CTA; orange for "pending"; status chips as saturated fills with white text.
- Light theme as a straight inversion of dark (or vice versa); glow for depth on dark.
- Raw hex in components; more than ~12 raw hex values outside `:root`; a second blue or grey on one surface; warm and cool greys mixed.
- Photos washed in brand colour; brand-coloured overlays on photography.
- A domain palette lifted unchanged from a lookup table (starting point only; colour.md).
- Section grounds that fade into each other. Persuade allows hard-edged field changes (chapters); Operate locks one theme.

```
Banned by default (brand or brief can override):
Tailwind indigo/violet/purple: #6366f1 #4f46e5 #4338ca #3730a3 #818cf8 #8b5cf6
                               #7c3aed #6d28d9 #a78bfa #a855f7 #9333ea #c084fc #d946ef
Cyan-on-dark glow:             #06b6d4 #22d3ee
Cream grounds:                 #f5f1ea #f7f5f1 #fbf8f1 #efeae0 #ece6db #faf7f1 #e8dfcb
                               #f0eee6 #faf9f5 #f5f4ed #eeece2 #e8e6dc
Terracotta/clay/brass/oxblood: #d97757 #da7756 #c15f3c #cc785c #bd5d3a #b6553a
                               #b08947 #9c6e2a #bc7c3a #7d5621 #9a2436
Espresso ink:                  #1a1714 #1a1814 #1b1814
Navy/slate app dark grounds:   #0f172a #020617 #1e293b
Untouched Tailwind defaults in app UI (warn): #3b82f6 #2563eb #1d4ed8 #60a5fa #22c55e #10b981
                                              #ef4444 #f59e0b
```

## Imagery and icons
- Fake product UI: dashboards, terminals, task lists, charts built from grey div bars or skeleton lines. Use a real screenshot, a real HTML interface fragment at true size with believable data, or nothing.
- Device mockups and browser-chrome frames around screenshots; fake iOS status bars and keyboards in phone mocks.
- Stock clichés: people at laptops, handshake, isometric clip art, line-art people, gradient 3D blobs, floating abstract shapes, spheres, abstract backgrounds behind a product launch.
- Hand-drawn or sketchy SVG people, scenery or doodles. A labelled placeholder beats a bad drawing. Real referents (products, places, people) get real images, never drawn or generated stand-ins.
- Placeholder image CDNs left in shipped work (picsum, placehold, random Unsplash); unverified stock URLs; broken images.
- Buried raster: an image under a 0.9+ opacity wash, or at near-zero opacity.
- Mixed treatments: some photos graded, some not; borders, shadows or rounded frames on photos; many small images where one dominant image would carry it; more than 2 aspect ratios across most pictures.
- A Persuade page with under 4 real pictures, unless a declared type-only direction.
- Stretched or distorted images, flags or OG cards; images without width/height (layout shift); video without a poster, with sound, or autoplaying under reduced motion.
- Hate or militarist motifs as decoration: Rising Sun rays, Confederate flag, Nazi insignia.
- Pills, badges or captions overlaid on photos, especially over faces; text on a busy photo area without a measured scrim. Web rule: burned-in video captions and thumbnail words follow `video.md` (outline or hard shadow, never over the face or the thing the joke is about).
- Photo-credit cosplay captions and explainer captions narrating the design.
- Emoji or Unicode as icons, bullets or greetings; an icon beside every heading; icons in saturated circles or tinted squares; mixed icon sets or stroke weights; hand-rolled icon paths.
- Icon-only controls without accessible names or tooltips; ambiguous icons without labels.
- A ✨ sparkle icon or shimmer to mean "AI".
- Invented logos for a logo wall; real logos used when they are not customers; category labels under logos.
- Drawn or reconstructed real logos. No logo in the sources: plain wordmark text plus a note.
- Generation is not mandatory; source order lives in pages.md §6.

## Copy and furniture
- Placeholder content shipped: lorem ipsum, John/Jane Doe, Acme, Nexus, example.com, 123 Main St, "User 1", "Feature One/Two/Three", `{{placeholder}}`, `[REPLACE]`. Missing facts become a marked slot like `[YOUR PRICE]` and are listed in the report.
- Invented proof: logos, quotes, star ratings, "10,000+ teams", "10x faster", "99.9% uptime", fake-precise specs (98.73%), invented prices or benchmarks. Demo data is allowed when labelled synthetic.
- Em dashes in UI copy (headings, buttons, labels, body). Use commas, colons, full stops. No spaced en dash as a separator either.
- Generic CTAs: "Get started", "Learn more", "Click here", "Read more", "Discover more", "Explore now", "Submit", "OK", "Yes/No" on confirms. Name the action and object ("Book a table", "Delete project").
- Duplicate CTA intents ("Get in touch" + "Let's talk"); the same primary twice in one viewport; 3+ buttons for one action; button labels over 3 words or wrapping to 2 lines; arrow glyphs on anything but the primary.
- A line of subtext under every label or heading; a tiny label above every header. AI hands you the big ball of clay; trim it away.
- Performative section labels: "Field notes", "Quietly trusted by", "On our desks", "From the field", "Currently on the bench", "Our philosophy", "The details", "Why us", "Our story". Use plain labels ("Testimonials", "Latest writing", "Customers include") or none.
- Furniture: local time/weather/coordinates strips, "Est. 2024", version stamps (`v0.6`, `Build 0048`, `BETA` eyebrows) unless the brief is a launch, "Brand · No. 01" micro-meta, "© 2026 / Scroll", scroll-down cues, mono-caps strip at hero foot ("BRAND. MOTION. SPATIAL."), live stock counters, middle-dot strings (max one `·` per line).
- Three of everything: three features, three stats, three testimonials, three adjectives.
- Micro-meta sentences under headings that restate the heading; intros that repeat the heading; the same text 3+ times in one card.
- Hedging ("consider", "perhaps", "may help"); generic whimsy; jokes about money, privacy, loss or blocked work.
- Cute-but-wrong wordplay, forced metaphors, mock-humble craft talk, unclear referents ("we plan to stay that way"); mono metrics, editorial prose and marketing punch mixed on one page.
- "Coming soon" on shipped features; broken plurals ("1 items"); strings concatenated from fragments.
- Interface-narrating copy in apps ("Here you can see your data"); "Welcome back, Alex 👋" on a work screen; "Items", "Records", "Status" instead of trade words.
- Raw error codes and "Something went wrong" / "Oops!" as the message; "Invalid input"; fake progress or fake loading messages.

Banned words (any surface; this is the one list, copy.md points here):
```
unlock, unleash, supercharge, turbocharge, seamless, elevate, empower, streamline, robust,
effortless, cutting-edge, next-gen, next-generation, world-class, best-in-class,
enterprise-grade, all-in-one, innovative, powerful, intuitive, magic, solution,
blazing fast, lightning fast, revolutionize, game-changer, delve, tapestry, testament,
realm, landscape (figurative), leverage, synergy, holistic, reimagine, redefine, harness,
embark, foster, pivotal, crafted, curated, meticulously, journey (non-literal), dive in
In instructions also: simply, just, easy, easily
```
Banned shapes:
- "Not just X, it's Y" / "More than a…" / "It's not X. It's Y." / "X. No Y." aphoristic cadence across 3+ sections.
- Tricolon slogans: "Fast. Simple. Secure."
- Mad-lib positioning: "The AI-powered platform for modern teams", "Your all-in-one X", "Built for X, by X".
- "X, reimagined", "X made simple", "Welcome to…", "Meet [Product]" for something nobody has met, "Say goodbye to…", "In today's fast-paced world", "Whether you're X or Y", "Ready to get started?", "Join thousands of…", "…is just theater", "actually X", "Take your X to the next level", "Transform the way you…", "The future of X", "Built for the modern X".
- Unasked questions as headlines ("Tired of spreadsheets?"); "Name: tagline" headlines (the name is in the nav).
- Confirmshaming declines ("No thanks, I like paying more").

## Motion
- The same fade-up on every block; content hidden at rest until a reveal fires; reveals that never fire (blank band); a dozen staggered hero entrances.
- Hover lift or zoom on every card; tilt on every card.
- Bounce, elastic or overshoot on standard UI controls. Allowed for momentum gestures (drag release) and Experience/celebration moments.
- `ease-in` on UI entrances; framework default `cubic-bezier(.4,0,.2,1)` used everywhere unexamined; `linear` on anything but constant motion and scrubs.
- UI control transitions over 300ms. Long reveals (700-900ms) and openings (to ~1.2s) belong to Persuade/Experience only. Exits as slow as entrances (exit ≈60-70% of enter).
- Stagger over 4 steps, or input blocked while it runs. First screen unreadable at 1.2s; anything in view hidden over 900ms; above-fold content waiting for scroll.
- Parallax over ~8% travel; anything moving across text being read; full-viewport moving backgrounds, slow ~0.2Hz oscillation, abrupt brightness jumps; flashing over 3 times per second.
- Transition blur over ~20px; blur-in on body text.
- `transition: all`; entering from `scale(0)` (start at 0.95-0.98 + opacity); animating `width/height/top/left/margin/padding` (grid-rows accordion excepted).
- Press feedback that changes layout bounds. `scale(0.97)` via transform is fine.
- Meaningless infinite loops: pulsing dots, floating shapes, shimmer text, rotating badges, orbiting icons, animated beams. Loops pause off-screen and in hidden tabs; anything moving over 5s gets a pause control.
- Scramble, typewriter or character-shuffle headlines; number tickers on invented stats.
- Scroll hijacking, wheel capture, smooth-scroll libraries on content or app UIs (Lenis only, Persuade only, off for touch and reduced motion).
- Main-thread scroll listeners driving animation; `setState` per frame.
- Orchestrated page-load choreography in apps; animating keyboard-initiated or 100+/day actions.
- Keyframes on toasts and toggles (they restart instead of retargeting); centre transform-origin on anchored popovers.
- Shimmer on skeletons. Skeletons are flat, at the real final layout, with no layout shift.
- Reduced motion handled by a global `0.01ms` kill switch only, or not at all. Design the reduced path: keep opacity and colour, drop travel, scale, parallax, autoplay.
- Hover effects not gated by `@media (hover: hover) and (pointer: fine)`; function available only on hover.
- More than one marquee per page; marquees that cannot pause.
- Identical fanfare on every reward; celebrations on routine saves; confetti on bulk repeats; rewards that delay completion or fake progress.

## 3D and scroll scenes
- Floating blob or gradient sphere in the hero; Vanta or particle background behind text; spinning logo; abstract 3D behind a product launch.
- 3D as decoration costing 150KB+ and battery when a 2D image says the same thing.
- A model that holds at 0° and reads as cardboard at 90°; a box that reads as a box (an honest absence is better).
- 3D WebGL photo galleries.
- Generated-site scroll story: every section centred, rise-in, ~1000px tall, 9-word heading; more than one mask reveal; sections under ~400px of scroll (flash past) or over ~2500px more than once.
- Pinned text over pictures with copy under 4.5:1 against the real pixels at that scroll position.
- A scroll page that "builds clean" but shows a black canvas or stale frame. Verify by sampling positions (motion.md).

## Operate: dashboards and app screens
- Dark, navy or saturated sidebar with a coloured active pill and a left accent bar. Sidebar sits on the page ground; active = neutral grey fill.
- 4 KPI cards with icons in tinted circles, green "+12.5%" pills and sparklines; KPI figures 36-48px bold in brand colour; a tile per metric where one divided container would do.
- Gradient-filled smoothed area chart with point dots; gridlines every 20px plus both axis lines; a legend for a single series; fat donut with slice labels; rotated x labels; charts with no hue on the main data.
- Cards with 16-24px radius + border + big soft shadow; equal 4-up grids with orphans; stretched cards with a blank band.
- Zebra tables with uppercase headers, a checkbox, avatar, chip and kebab on every row; left-aligned proportional numbers; "N/A" for missing values; pagination under a 5-row overview list.
- Saturated status chips with white text; more than one status mark per row; more than 5 states.
- Accent on every button and tab; a top bar of search + bell + avatar on every screen, or a mostly empty one; an Export / Share / date-picker cluster by reflex.
- Neon or glass dark dashboards.
- Illustration + "No data yet" inside an empty chart; spinners in the middle of content; blank screens while loading.
- Display fonts in labels or data; decorative motion; inconsistent components across screens.
- Reinvented standard controls: custom scrollbars, odd selects, non-standard modals.
- Tool costume: terminal F-key bars, bezels, cockpit gauges, ledger paper standing in for a table.
- A grey screen with one accent and nothing else (the category default without the polish).
- Designer Tweaks panels left in product UI; internal tools indistinguishable from the customer app.
- More than 3 radii on one screen; a logged-out state that mounts the app shell behind a blur.
- Deltas coloured by direction instead of good/bad; totals that do not add up from the displayed rounded parts; relative figures without a named baseline.

## Native and platform
- "Ported from a website": web buttons, custom back buttons, hover affordances, hamburger menus where a tab bar belongs.
- iOS controls on Android or Android controls on iOS; blocked edge-swipe back; broken Predictive Back.
- Hand-rolled glass instead of system materials; ignored Dynamic Type; targets under 44pt (iOS) or 48dp (Android).

## Decks and prototypes
- A web page where a deck was asked for: everything centred, scroll layouts, nav bars inside slides.
- Claude-isms in titles: verdict titles, fake tension ("It's not X. It's Y."), "The magic moment", punchline titles. A title introduces its slide.
- Titles in mixed grammatical styles; a title list that does not tell the story when read alone.
- Walls of bullets; two ideas on one slide; text that only fits under 24px on a 1920×1080 canvas; titles under 36px.
- Accent-bordered "takeaway" boxes; emoji; an icon on every bullet.
- 3+ consecutive slides on the same ground; no dark/light rhythm in a deck of 8+.
- A kicker stacked above every title, or a chrome label that repeats the title.
- Heading y-position drifting slide to slide; parallel section headers that do not match.
- Animation on more than 1-2 slides in 10, or where reveal order carries no meaning; infinite decorative loops; more than one effect per element.
- Screenshots and diagrams aspect-filled, cropped or overlaid; labels baked into images instead of real text.
- Full-bleed art that leaves a blank strip (collapsed wrapper).
- Prototypes: a title screen before the app; `onClick` on divs; static mocks with no states; fake stats instead of a grey dash or a labelled stub.

## Process tells
- Shipping the first version without a fresh critique pass.
- Claiming "done" without rendering and looking at 1440 / 768 / 390 screenshots.
- Claiming a check that was not run; "could be more polished" instead of a measured finding.
- Reviews without a separate "Looks AI-generated x/10" score beside the design score; the clearest template tell is every surface the same dark rounded card with the same padding and title size (fix: at most three surface treatments with a rule for each).
- Describing options in words when the owner asked to pick: show them as screenshots.
- Generic sampled colours guessed from memory instead of grepped from the brand source.
- Polishing a look that a redesign is replacing; silently changing copy, routes, form names or claims.
- Code tells: z-index 999/9999 instead of a token scale; `html { font-size: 62.5% }`; `var(--x)` that never resolves; leftover `{{placeholder}}`; judging the dev server instead of the production build.

## Fast scan (run on every screenshot before showing work)
1. Could a competitor's name replace ours and the page still work?
2. Centred headline + subtitle + two buttons + grid below?
3. Hero → logos → 3 cards → testimonial → pricing → CTA order?
4. Any row of identical icon-topped cards (Persuade)?
5. Eyebrow, kicker or "New" pill above a heading?
6. 01/02/03 numbering, mono labels, or a styled accent word in a headline?
7. Headline over 2 lines at any width or over 8 words; display under 4x body?
8. Any decorative gradient, glow, glass card or `background-clip: text`?
9. Hairlines, 1px boxes or side-stripe borders on a Persuade page?
10. Shadows on resting elements; one 9-16px radius on everything?
11. Purple/indigo, cyan-on-dark, or cream + terracotta from the banned hex list?
12. Accent on headings, icons or every button (over ~5% of the screen)?
13. Overused display face from the list, or a subject-cliché face?
14. Fake grey-div UI, device frame, stock people, blobs, or emoji icons?
15. Lorem, Acme, John Doe, invented logos, stars or user counts?
16. Banned buzzword, "Not just X", tricolon, "Get started" or "Learn more"?
17. Any em dash in UI copy?
18. Same fade-up on every block, bounce on UI, `transition: all`, `scale(0)`?
19. Huddled half, blank stretch over half a screen, unequal margins, more than 3 left edges, text within 16px of the edge?
20. Operate: dark sidebar, icon-circle KPI cards, gradient area chart, zebra uppercase table?
