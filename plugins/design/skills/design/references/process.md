# Design Process

Use when: starting, building, checking, critiquing, redesigning or reporting on any design work. This file is the run order; the other references hold the craft rules each step points to.

## 0. Stance

- Work as the designer; the user is the manager. Finish the job: no hedging, no placeholders except assets only the user can supply.
- The medium follows the brief: a deck is designed like slides, an app like an interaction, a game like a game. HTML is the tool, not the format.
- The brief wins. Pinned fonts, eras, palettes and the user's standing taste rules (memory, CLAUDE.md, DESIGN.md) override every default here, even when they hit a tell. Steering a clear brief toward your own taste is a failure.
- Never ship the first version: build → critique with fresh eyes → refine → gate → ship.
- Track the run in a todo list and update it live (in_progress → completed per step, never batched at the end).

## 1. Read the brief

- Small jobs (a poster, a cover, a sign) still get a written brief before any pixels: where it lives and its size, who
  it is for and the one action, the brand file, 2-3 references, the exact must-have text, the deadline, and what would make
  it fail (reads as a template, unreadable at phone size).

- Extract: subject, audience, the ONE action or job, surface(s), stack, existing brand and assets, what imagery really exists, constraints, what must stay untouched, deadline/fidelity.
- Get context before designing. Look for a codebase, UI kit, design system, DESIGN.md, PRODUCT.md, screenshots, brand files. Mocking a product from nothing is the last resort and gives poor results; if there is no context, ask for some as a question.
- Decide what is already true:

| Situation | Move |
|---|---|
| Extending a surface in a living system | Inherit everything; invent nothing |
| New surface in an established world | Inherit tokens; derive 5-7 materially different structures |
| Incomplete brand | Expand it from its real values |
| No authority | Create a world (sections 4-6) |
| Redesign / review | Section 12 |

- Brand branches:
  - Brand source given (spec, URL, CSS, screenshot): extract the REAL values. Grep hex from CSS; never guess colours from memory. Copy exact values (5px stays 5px). Missing font → nearest licensed substitute, flagged.
  - "I have a brand" but nothing attached: ask for it and stop. Never invent tokens.
  - No brand: pick a direction yourself and bind it. Don't make the user pick twice. Exception: when the owner is present and the direction is open, it always goes to him as a visual pick (§5).

## 2. Design read and mode

- Set a mode per SURFACE, not per product. A tool's landing page is Persuade; its settings screen is Operate; its docs are Read.

| Mode | Surfaces | Boldness | Dials V / M / D |
|---|---|---|---|
| Persuade | landing, marketing, pricing, portfolio, product site | bold, committed | 7-9 / 6-8 / 3-5 |
| Operate | app screens, dashboards, tools, admin, settings | quiet, dense, native | 3-5 / 3-4 / 5-7 |
| Read | docs, articles, changelogs, long-form | calm, typographic | 5-6 / 3-4 / 3-4 |
| Experience | games, toys, art, immersive, celebrations | bold, the thing leads | 8-10 / 6-9 / 2-3 |
| Video | thumbnails, covers, in-video text, overlays, motion graphics, composites, edit feel | loud, one focal point per moment, read at phone size | 7-9 / 6-8 / 2-4 |

- Dials: VARIANCE (layout risk), MOTION (intensity), DENSITY (information per screen), 1-10. MOTION >3 requires a reduced-motion path; MOTION >4 means motion is actually present.
- Declare it in one line before any work:
  `Reading this as: <kind> for <audience>, <vibe>, leaning toward <system>. Mode: <mode>. Dials: V/M/D.`
- Mixed request (product site + its app): two runs, one palette and one typeface. Interface fragments on a page follow Operate rules inside (`data-ui`).
- Brief maps to a real design system (Material, Fluent, Carbon, Polaris, GOV.UK, USWDS, Radix, shadcn)? Use the real package, one system per project, never in its default state.
- Vague brief: state your reading in one line; ask only if blocked (section 3).

## 3. Questions

- Ask only when an answer changes what you would build. Skip when the brief, codebase or memory already answers it, for small tweaks, follow-ups, "just build it", and complete briefs ("deck for Eng All Hands, 10 min, from this PRD").
- Ask hard when the brief is vague and large ("prototype onboarding for my food app"); ask lightly when it is vague and small ("6 slides on the history of butter").
- One batch, ≤5-7 questions, each with a suggested default and a "decide for me" option, so the user can submit unchanged.
- Second round only when answers open a real gap, holding only questions you could not have written before. If the open question is "which direction", show built options, not words.
- What to ask, in priority order:
  1. Starting point: UI kit, design system, codebase, brand files.
  2. References: apps, sites or screenshots they admire. Highest impact on quality.
  3. Output, fidelity, scale: deck/prototype/page/dashboard; how many screens or slides; deck length in minutes.
  4. Audience and success: who acts, what success looks like.
  5. Mode keys. Persuade: what they must believe, what proof exists. Operate: the task, the data, the states, frequency of use. Read: the reader's question, the wayfinding. Experience: what leads.
  6. Constraints: must-use elements, things to avoid, what must stay untouched, what would make a polished result feel wrong.
  7. Variations: how many, of what, divergent or by-the-book.
- Never ask for CSS values or offer canned aesthetic lanes. A remembered choice is offered only as a suggested default.
- No user present (autonomous run): take the defaults, list every assumption in the report.

## 4. Inventory and research

- **Page inventory: 8-12 things only this client has.** Name and its meaning; street, door, neighbourhood; its numbers; its constraint; materials; rituals and hours; printed artefacts; people; the product's own objects. The direction and idea must come from this list.
- **App inventory:** objects, magnitudes (realistic ranges: min, typical, max), people, jobs, frequency, the product's own things. Write the dataset as a file with `console.assert` reconciliations (totals add up, facts shown twice agree).
- **Content ranges:** collect the longest name, zero items, the 3-line title, the billion-sized number before layout.
- **Name the scene and the rut:** the audience scene and its cultural home; the page the category always ships, and its predictable opposite. Both are off the table as the default.
- **Research, bounded:** 3-5 references. For each, write the one discipline to steal (palette commitment, grid courage, density) and never its clothes (a button shadow, a face).
  - Brand references by need and how to fetch them: `systems.md` (Brand reference library).
  - New world: list 7 concrete visual systems or artefacts the audience knows by heart, spanning ≥3 material families. On Operate/Read never take them from the tools the audience operates (a terminal or cockpit returns as a costume). On Persuade the literal reading of the brief gets at most 1 slot.
  - Domain palette and font tables are starting points, never final (`colour.md`, `typography.md`).
  - Imagery research: search for the subject's physical object, not the category. Verify every URL resolves.
- Check candidates against the AI rendition clusters in `tells.md`. If the aesthetic could be guessed from the category alone, rework.

## 5. Three directions, then choose

- Make 3 directions that differ on a NAMEABLE axis ("Warm editorial" vs "Dense data-first" vs "Photo-led civic"). Five shades of one idea is no choice.
- Each direction states: colour strategy, type voice, layout posture, imagery source, signature move, light or dark.
- Pick the one that carries something only this client has; judge rivals on audience identification and product clarity, not novelty. Write why in one sentence. Redraw only for a stated reason: brand clash, missing asset, can't hold the real content. A losing direction may still donate its discipline.
- Offer a quiet "canon" exit (the category standard done straight) when presenting options; never recommend it.
- User present and the direction is open (look, hero, type pairing, colour stance, density): settle it BEFORE the full build. For the owner: 3 directions mocked on his REAL screen with his real data, sent as screenshots (plus the HTML), never described in words; he picks and may combine them. Mockup first: nothing past the mockup changes until he approves, and each change is checked on screen before it is reported. Otherwise show 2-4 candidates low-fi ("decision fidelity is not deliverable fidelity"), each with its motivation and main trade-off written in chat, not on the artboard. Arguing only for your favourite is a rigged vote.
- Keep option names and numbers stable across turns.
- Visual-only options: side by side on labelled artboards. Flows: one clickable prototype with an in-page variant toggle, not N files.
- Once settled, give 3+ variations across dimensions (layout, metaphor, scale, fills, texture, type treatment, with/without colour or icons), by-the-book first, growing novel. Goal: atomic pieces to mix, not the perfect option.
- Varying an existing element: first write an identity lock (one sentence of the real on-screen values). Vary one primary axis per variant: hierarchy, topology, type system, colour strategy, density, decomposition, using existing tokens only. Departure (3 aesthetic families, each with a real-world referent such as "a museum exhibition label system") only on an explicit "redesign".
- Never converge across projects: rotate light/dark, faces and palettes between generations.

## 6. Commit the world

- Choose the colour strategy before colours (Restrained, Committed, Full palette, Drenched: `colour.md`).
- Pick light or dark from one written sentence about the physical scene (who, where, under what light), never by category. The owner's own tools start dark (pure black or near-black, surfaces stepped lighter).
- Choose faces like objects from the subject's world, never by association (books want a serif) (`typography.md`).
- **Idea sentence (Persuade/Experience):** "On this page, [thing from the subject] becomes [device]."
  - Competitor test: swap in the nearest competitor. If the sentence still works, it is a category idea; redo it.
  - One live thing: interactive, real content, thumb-usable, no-JS fallback, never blocks reading. Removal test: someone would notice it gone.
- **Screen sentence (Operate):** the screen's ONE question and ONE finding, plus the style, its face and one signature element.
- **Read:** the reader's question, the heading outline, the wayfinding answer (where am I, where can I go, how do I get out).
- **Soul budget:** ~80% proven patterns, ~20% distinctive: ONE bold move (type, colour or proportion), specific microcopy, one memorable micro-interaction, one detail only a real user would know. One flourish; three is noise.
- Soul test: someone outside the project can tell from one screenshot which product it is. Memory test: what would someone describe an hour after one viewport? A mood means the concept hasn't committed.
- Say the locked system to the user in one sentence so they can redirect cheaply: "deep navy canvas, single cyan accent oklch(68% .16 220), geometric display + system body".
- Record a ~150-word direction contract in working notes: THESIS, OWN-WORLD (recognisable with all content removed), STORY, FIRST VIEWPORT (exact composition), FORM, FINISH. Never put it in shipped code, comments, data-attributes or bundles.

## 7. Argument and copy before markup

- Write the argument: who reads, what it is as its maker would tell a friend, the one belief after one screen, the proof, the next step.
- One claim + proof per section. A section with no claim is deleted. The argument's order is the page's order (this kills the stock hero/logos/3-features/testimonial/pricing/CTA sequence).
- Write the copy deck before markup (`copy.md`). Deliver every requested section completely, in tight copy (landing paragraphs ≤~25 words).
- Deck: share the full title sequence in chat before building (`decks.md`).

## 8. Build order

| Mode | Order |
|---|---|
| Persuade | tokens → hero at desktop + phone → each section, carrying the idea into pricing, FAQ, footer → imagery → live thing → scroll scenes → fullness → frame (margins, edges) → states and semantics → motion layer last |
| Operate | dataset file → empty shell with the grid arithmetic in a comment (e.g. 3×372 + 2×17 = 1152) → render real data → empty, zero, loading, error → hover, selected, focus, disabled → responsive fold |
| Read | heading outline → measure and type scale → body with real content → wayfinding (TOC, linkable headings, prev/next) → frame and world → code/table styling |
| Experience | core interaction greyboxed → feel (input latency, timing, juice) → art → reward layer → pause, reduced motion, low-end fallback (`experience.md`) |
| Deck | type scale in `:root` → title list → slide skeletons → content → rhythm check (`decks.md`) |

- Comp-led (Persuade/Experience with image generation): 3 image comps → user approval → build to the chosen comp; the hero must match it before sections start; nothing absent from the comp appears. Code-led (always for Operate/Read): ambition lives in the first-viewport block plus one named signature interaction.
- Build still first: motion off until composition passes.
- Big new build with the user watching: do an early junior pass. Write the file with assumptions and reasoning at the top plus labelled grey placeholder blocks, show it as a wireframe, then build out and show again quickly.
- Rebuild every atom (nav, buttons, inputs) in the direction's vocabulary. A stock component inside a committed form is a lapse.
- When the world names a technique (WebGL, view transitions, scroll timelines), build the real thing, not a static imitation.
- Placeholders over bad attempts: a labelled grey block beats a hand-drawn person or fake icon. Never fake stats.
- Pace the scroll: vary density and scale, follow a dense passage with a quiet one, end on a real close.
- Keep files ≤~1000 lines; split by coupling. Serve over http://localhost, never file://. It must not crash on load.
- After the build, document the world (DESIGN.md is written from what was built, never before: `systems.md`).

## 9. Verification gate

Nothing is "done" until every line below passed on the final build. An unanswered line is not done; "n/a" only when the element does not exist. Commands and flags: `tools.md`.

**Static (every edit)**
- `lint.mjs` (+ `--app` for Operate) and `preflight.mjs` on changed files. Exit 0 or each finding justified.
- Unclosed tags, `<script>` without `</script>`, leftover `{{placeholder}}` / `[REPLACE]` / lorem, blank sections, em dashes in UI copy.
- Every `var(--x)` resolves to a defined custom property; raw hex outside `:root` ≤~12.
- Trace the main interaction once in code.

**Render (every renderable surface)**
- `inspect.mjs` at 1440 / 768 / 390 plus the real target viewport (deck 1920×1080, phone frame 390×844, Electron window, 720px laptop). `--app` for Operate. `--film` for scroll scenes.
- No inspect available (no Node 22 or Chrome)? Screenshot the same widths in the browser pane and say so in the report.
- Touch, CPU and browser chrome are invisible to DevTools: when a real phone is reachable, check there. Heavy effects (WebGL, scroll scenes) hold 60fps; simplify below 50.
- Open and look at EVERY screenshot after the last change. Judge pictures, not code. The numbers are a floor; the pictures are the judgement.
- Fix every FAIL. Each WARN is a defect unless defensible in one sentence written in the report. `--allow` only with that sentence (e.g. type-only page: `few-pictures,still-page,no-footage`).
- Console: zero errors, zero 404s.
- Run the final gate on the production build, not the dev server.

**Drive the states**
- Hover, focus (keyboard Tab through everything), active, disabled, loading, error, empty, success, overlong content, 0 and 1 items.
- Settle entrance motion before capturing. Reduced motion on: nothing hidden, reduced state = finished state.
- Both themes if both exist, each checked on its own; `forced-colors: active` keeps every control visible. 200% zoom and 320px reflow: no clipping, no horizontal scroll.
- Screen reader once through the main flow (VoiceOver or NVDA): names, roles, state changes announced, focus lands on the new content.
- Scroll pages: sample ≥16 scroll positions after reveals settle (animations idle, 3s cap); fail on a blank canvas, a background that never changes, copy under 4.5:1 against the real pixels behind it, sideways overflow; warn when distinct frames < samples/2 (steppy scrub). A scroll page fails silently; exit 0 proves nothing.
- Motion: watch at 0.25x (DevTools Animations panel) and frame by frame; review with fresh eyes (`motion.md`).

**P0 integrity (hard fails)**
- Accidental overlap; text clipped or overflowing; `white-space: nowrap` forcing fit; orphans (1-2 characters on the last line); display type wider than its column; headline over 2 lines at any width.
- Charts drawn as outlines without data; duplicate primary CTAs; anything covering a headline, statement or button at any scroll position.
- Hover or focus that LOWERS contrast; a focusable element without a `:focus-visible` ring.
- Blank band from an unfired reveal; content hidden at rest.

**Craft floor (one batched look)**
- Contrast: body and placeholders ≥4.5:1, large text ≥3:1, controls, icons, focus ≥3:1.
- Targets ≥24×24 CSS px everywhere, 44×44 on touch; nothing sticky covers the focused control.
- Browser surfaces themed: `::selection`, caret, scrollbars, focus rings, underline offset, tabular numerals.
- Controls name their action; errors name the problem and the recovery.
- Coverage: every brief requirement findable within seconds.
- Verify answers cite a file, selector or computed value. A bare "yes" is not an answer.

## 10. Critique

- Critique on screenshots, with fresh context. Best: a fresh-context reviewer subagent, never forked from the build thread. Single-context critique is labelled "degraded" in the report.
- The ship score needs a FRESH blind review: a new agent given only the screenshots or the render (never the build notes, the brief's reasoning or earlier reviews). Builders score about 1.5 points above fresh readers. For video and thumbnails, use the blind-reader protocol in `video.md` (3 fresh readers averaged per row when a single reviewer's scale steers the edit).
- Do the design judgment BEFORE reading linter output, so the linter does not anchor it.
- Five-second stranger test: shown one viewport for 5s, a stranger can say what it is, who it is for, and what to do next.

**Quick self-score (every round, any mode, silent, 1-5; anything <3 is fixed and rescored; two passes is normal)**
1. Philosophy: posture matches the brief, no drift back to your default.
2. Hierarchy: one obvious place for the eye per screen.
3. Execution: type, spacing, alignment, contrast right, not close.
4. Specificity: every word, number and image belongs to THIS brief.
5. Restraint: one accent, on ≤2 kinds of thing per screen; one flourish.
6. Seasoning: one star element per screen with real character. A quiet, flat screen with nothing bold reads as "mid"; restraint is not an excuse for blandness.

**Round write-up (every critique round)**
`ROUND n / Seen in one second / Idea / Live thing / Star element / Layout word per section / Scores → overall / Looks AI-generated x/10 / Caps applied / Top 3 problems, each with screenshot + fix`.

**Page: 14 passes (Persuade; Read and Experience use the relevant ones)**
1. One second, then five: one focal thing; a stranger knows what, who, next.
2. Squint: 2-3 masses.
3. Cover the logo: could a competitor own it? Does the idea reach pricing, FAQ, footer?
4. Count left edges: 2-3 for all text.
5. Space and frame: gaps, holes vs rests, equal margins, no huddled halves, no empty stretch over half a screen.
6. Type: jump ≥3x between levels, ≤5 sizes, no orphans, measure ≤75ch, nothing centred over 3 lines.
7. Colour proportions and accent discipline.
8. Images: ≥4 real, one moving, shared ratios, one grade, no grey boxes or fake screens.
9. Sameness: one layout word per section; no repeat in a row; no word 3x.
10. Phone is its own composition, not a squeezed desktop.
11. Fullness: each screen a poster, not a wireframe.
12. Substance: every requested section complete and readable; a real first-screen button.
13. Collisions: nothing over headline, statement or button at any scroll; no sideways overflow.
14. Competitor test passes; name the live thing.

**Page score**
- `overall = 0.4·design + 0.3·usability + 0.2·creativity + 0.1·content`, each 0-10.
- Bands: 0-4 broken, 5-6 functional, 7-8 strong, 8.5 = meets the published spec or the pro reference it is compared with, 9-10 beats it with margin. Score against the named reference, not against the average site: a typical award-listed site scores ~7.5-8.0 on this scale, so 8.5 must be earned with evidence; rescore any 9.
- Measured rows (loudness, reading speed, contrast, sizes) score from the number: within the pro spec = 8.5, beats it with margin = 10, one tolerance step off = 7, fails = ≤5.
- Caps (apply the lowest; list every cap applied):

| Condition | Cap |
|---|---|
| Any inspector FAIL | overall ≤6.0 |
| Headline 3+ lines, eyebrow, mono labels, 01/02/03 numbering, decorative gradient, resting shadow, visible hairline | overall ≤6.5 |
| Pass 3 fails | creativity ≤6 |
| Idea fits a competitor | creativity ≤7 |
| No live thing | creativity ≤7.5 |
| <4 real pictures (unless a declared type-only direction) | design ≤6.5 |
| Still page or uniform fade on every block | design ≤7 |
| ≥2 mostly empty screens, small grey text, unequal margins, huddled sections, blank stretch over half a screen | design ≤6.5 |
| Placeholder content | content ≤5 |
| Missing or thin requested section | content ≤6 |
| Blank band from unfired reveal, clipped content | usability ≤5 |
| Five-second test fails, anything covering a headline | usability ≤6 |
| No first-screen primary action, untitled text section | usability ≤7 |

**App: 7 questions (Operate)**
1. The biggest thing answers the screen's question and is read first (largest figure answers the title row)?
2. Shared edges, no dead strip, no stretched card with a blank band?
3. Colour only on data, status and one primary; main data carries the hue; the chosen face visible?
4. Numbers add up and align digit for digit (facts shown twice agree, totals and deltas from displayed values, baselines named)?
5. Zeros look like zeros, missing like dashes, badges only on actionable queues?
6. Legend swatches = marks, no colliding labels, no caption explaining bars?
7. Phone: nav folded and each block still answers?

**Cognitive load (Operate, flows, forms; 8 checks)**
- Single focus; chunks of ≤4; grouping; clear hierarchy; one decision at a time; ≤4 visible options; nothing carried in memory between screens; progressive disclosure.
- Failures: 0-1 low, 2-3 moderate, 4+ critical. Working memory holds ~4 items: 5-7 is the edge, 8+ overloaded. 1 primary + 1-2 secondary actions, the rest in a menu; ≤5 top-level nav items; doc sidebars ≤4 siblings per level.
- Name violations by type: wall of options, memory bridge, hidden navigation, jargon barrier, visual noise floor, inconsistent pattern, multi-task demand, context switch.

**Personas (pick 2-3)**

| Persona | Checks | Use for |
|---|---|---|
| Alex, power user | core task <60s, shortcuts, Esc, skippable onboarding | dashboards, data-heavy |
| Jordan, first-timer | first action obvious in 5s, labelled icons, help | landing, onboarding, forms, checkout |
| Sam, accessibility | keyboard only, focus, 4.5:1, announcements, 200% zoom | dashboards, forms, data-heavy |
| Riley, stress tester | edge data, refresh mid-flow, emoji, silent failures | landing, checkout |
| Casey, mobile | thumb zone, state survives interruption, 3G, 44×44 | landing, checkout, onboarding, forms |

**Nielsen score (apps, flows, reviews; each 0-4: 0 absent/broken, 2 partial, 4 excellent)**
1. System status 2. Match with the real world 3. User control 4. Consistency 5. Error prevention 6. Recognition over recall 7. Flexibility/efficiency 8. Aesthetic-minimalist 9. Error recovery 10. Help/docs.
- Total /40. On Persuade/Experience, 7 and 10 may be n/a: renormalise to /32.
- Bands: 36-40 excellent, 28-35 good, 20-27 acceptable, 12-19 poor, 0-11 critical (on /32 use 90/70/50/30%). Most real interfaces score 20-32.

**Audit (technical review; each 0-4, /20; reports, does not fix)**
- Accessibility: 0 fails WCAG A, 3 mostly AA, 4 full AA approaching AAA.
- Performance: layout thrash, layout-property animation, lazy loading, `will-change` overuse, bundle size, re-renders, Core Web Vitals (LCP ≤2.5s, INP ≤200ms, CLS ≤0.1).
- Theming: hard-coded colours, broken dark mode, token misuse.
- Responsive: fixed widths, targets <44/24px, broken touch gestures, horizontal scroll, text scaling.
- Integrity (critical): system drift, and whether the result is interchangeable with an unrelated product. 0 systemic drift, 4 coherent.
- Bands: 18-20 excellent, 14-17 good, 10-13 acceptable, 6-9 poor, 0-5 critical.
- Native apps swap in: VoiceOver/TalkBack, performance (startup, virtualisation, jank), appearance (semantic colours, Dynamic Color), platform conformance (critical), adaptivity (size classes, orientation, IME, multi-window, foldables).
- Report order: integrity verdict, summary, findings tagged P0-P3 (location, category, impact, WCAG reference, fix), systemic patterns, positives. Keep P3s few.

**Finish reviewer (fresh context, no build history; returns ship | fix | rebuild | recapture)**
- Checks in order: 0 evidence (captures exist, current, valid, else recapture); 1 persistence (state survives reload and navigation); 2 fidelity matrix vs direction and references (match, adaptation, missing, contradicted, added; TYPE, MATERIAL and GROUND rows mandatory; hunt warm-cream and blue-black drift); 3 ceiling vs the references; 4 direction contract kept, promise by promise; 5 truth (synthetic data labelled, no invented claims, every promised asset shipped); 6 floor (any `tells.md` item is always a fix).
- Output ≤8 ordered fixes plus a "keep" line. Calibrate against the direction, never against how much effort the build shows.

**Severity (all findings)**
- P0 blocks the task. P1 major difficulty or a WCAG AA failure; fix before release. P2 annoyance with a workaround. P3 polish.
- Tiebreak: would someone contact support about it? Then ≥P1.

## 11. Fix order and round limits

- Fix in this order; never polish above an unfixed level:
  1. Broken tasks, data loss, inaccessible paths (P0).
  2. Missing states: loading, empty, error, success, disabled, permission.
  3. Idea.
  4. Flow and hierarchy.
  5. Composition, frame, responsive and system drift.
  6. Typography.
  7. Imagery.
  8. Colour.
  9. Detail.
  10. Motion (`motion.md` has its own order: delete → reduce → easing → origin → interruptible → GPU → asymmetric → polish → a11y).
  11. Code cleanup: remove debug output, dead code, churn.
- Removing something never gets refilled with an ornament. A section that looks empty gets a bigger main element or gets cut.
- Fix at the narrowest correct level: missing token → add token; one-off implementation → replace with the system's component; conceptual mismatch → rethink the block; local defect → local fix.
- Per round: fix the top 3 problems, batched per look (not a screenshot per tweak), then re-run the gate.
- No fixed round cap: keep iterating while the score rises. Stop when every row clears the ship bar and no stranger-visible problem remains.
- Stop and report on oscillation (a fix brings back an earlier defect) or plateau (score unchanged across a round); ask for input instead of looping.
- Ship bar: every scored row ≥8.5 with 0 FAIL, plus a fresh blind review (§10); Operate also Nielsen ≥28/40 with no open P0/P1. Stopped below the bar on a plateau: report the score as found and the reason, never rounded up, and never call it shippable.

## 12. Redesign, refinement and review

- Classify first:
  - **Refinement** preserves identity, copy, behaviour and everything out of scope. Ask before changing factual copy or claims.
  - **Redesign** keeps product truth and function, replaces the look entirely.
  - Never split the difference by polishing a look you are about to discard.
- Record "before": run `inspect.mjs --out .design-check/before` and keep the screenshots and numbers.
- Read the code, then list what must survive, and never change it silently: routes and URLs, SEO slugs, forms and field names, data and API contracts, analytics IDs and event names, nav labels, logo, legal copy, accessibility features, keyboard shortcuts.
- Keep the stack. No framework migration; check existing dependencies before adding one; reuse existing components and tokens first.
- Scope is sovereign: touch only the named target. Add no new colours, fonts, radii or shadows unless asked; if the system cannot express the change, ask.
- Redesign levers, in order, stopping when satisfied: type → colour → frame (spacing, grid) → states → motion → hero recomposition → replace stock components → full block replacement.
- Revisions after delivery: change ONLY what was named; leave layout, spacing, fonts and copy untouched. Suggest a broader change; don't apply it. Locked tokens persist every turn. Copy the file to `v2` before a major revision. Reopen modified files to confirm edits landed.
- Prove it: before/after measurements from the same inspect run; click every link and submit every form that worked before; diff the source and remove leftovers.
- **Review-only request** stops at critique + the 3 biggest changes. Edit the user's files only on an explicit go-ahead; musing ("maybe lighter?") is not one.

**Critique report (reviews of existing work)**
1. Method line (what was looked at, at which widths, which tools, fresh or degraded context).
2. Specificity verdict: could an unrelated product use this unchanged?
3. Overall impression, then 2-3 strengths ("what's working").
4. 3-5 priority issues, biggest first, each: P-level, element, observation → consequence for THEIR goal → fix.
5. Score: Nielsen table (Operate) or page score with caps (Persuade); audit /20 when technical; a separate "Looks AI-generated x/10" beside it; trend against the previous round when one exists. A full review (not a build round) ranks the top 8-15 problems, each with its fix.
6. Persona red flags.
7. Small stuff and quick wins (5-15 min each), folded into one list.
8. 2-4 targeted questions with 2-3 options each, last (skippable only with <3 priority issues).
- Phrase findings like a designer ("paragraph starts 40px left of the headline's edge"), never "could be more polished". Pin each to an element; don't average away an interesting failure.

## 13. Report format

Report only when: 0 FAIL at 1440/768/390 (+ target) on the final build; every screenshot opened after the last change; five-second test passes; every section headed, margins equal, no empty stretch; critique written.

```
Built: <what> at <path or URL>
Read: <design-read line>
Direction: <name>; why; redraws and their reasons
Idea: <idea or screen sentence>. Live thing: <what>
Checks: lint <n FAIL/WARN>, preflight <n>, inspect <n FAIL> at <widths>; justified WARNs: <one line each>
Score: round <n>, overall <x.x> (D/U/C/C) or Nielsen <n>/40; caps applied: <list>; critique context: fresh or degraded
Assumptions: <every default taken without an answer>
Credits: <image, footage and font sources with licences>
Replace before shipping: sample content, stand-in images and drawings, font/icon substitutions, flagged checkout/mailto stubs
Not verified / known gaps: <list>
Next: <1-3 items>
```

- Keep it brief: caveats and next steps, no narration of tool calls, no feature tour.
- Delete `.design-check/` scratch output or add it to `.gitignore`.

## 14. Honesty rules

- Never claim a check you did not run, a screenshot you did not open, or a width you did not render.
- Never invent proof: logos, quotes, stars, user counts, prices, benchmarks, capabilities, "10× faster". Real customer logos only when they are customers. Unknown facts become marked slots (`[YOUR PRICE]`).
- Demo data is design material: author it at full fidelity, realistic and reconciled, and label it synthetic.
- Flag every substitution: font, icon set, image, logo (no logo in the sources → plain wordmark plus a note; never redraw a real logo).
- Say what you could not read or observe (dark mode, error states, motion timings) under "Known gaps"; never fill it with guesses presented as fact.
- Real referents (products, places, people) get real images, never drawn or generated stand-ins presented as real. Drawn art that could pass for a photo is labelled.
- Never fake a payment form; with no checkout, the primary goes to a real destination or a prefilled `mailto:`, flagged.
- State the score as found. Below the bar, say so. Never claim 0.9+ fidelity for a 3D model rebuilt from one image.
- Provenance stays out of shipped UI; it goes in the report and asset metadata.
