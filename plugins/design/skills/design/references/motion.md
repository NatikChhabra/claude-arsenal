# Motion and Animation

Use when: adding, choosing, coding or reviewing any animation, transition, gesture, scroll effect or celebration, on a site, app, game or deck.

## 1. Decide first

- Motion is the last layer. Build the still version (motion off) first; it must read and work without a single animation.
- Every animation needs one purpose: spatial consistency (navigation, container morph), state change, explanation (where a thing went, what caused it), feedback, gesture follow-through, preventing a jarring jump, or the one signature moment. Never decoration. "Looks cool" is allowed only for the signature moment or a rare event.
- Removal test: if nobody would notice it gone, delete it. If you can't say why it exists, delete it.
- Motion is never the only signal of a state change; pair it with text, colour or shape.
- Content is visible by default. A failed or slow script never hides the page.

| How often the user sees it | Rule |
|---|---|
| 100+/day (keyboard shortcuts, command palette, typing) | No animation. Keyboard-initiated actions are instant. |
| Tens/day (hover, list navigation, tab switch) | Remove, or cut to a ≤200ms colour/opacity change with no travel. |
| Occasional (modal, drawer, toast, route change) | Standard motion, ≤300ms. |
| Rare or first time (onboarding, milestone, empty-to-first-item) | Delight allowed; longer, richer, skippable. |

- Mode sets the budget (see `process.md` for modes): Operate = feedback only; Read = almost none; Persuade = one signature + scenes + entrances; Experience = motion is the medium; Video = every move sits on a cue in the picture or the sound (`edit.md`).

## 2. Easing

- Entering or exiting: ease-out. Moving on screen (A to B): ease-in-out. Hover/colour: `ease`. Constant rate (marquee, spinner, progress, scroll-linked, scrub): `linear`. Unsure: ease-out.
- Never `ease-in` on UI; it feels laggy at the start where the eye is. Only exception: a permanent removal ≤200ms. This is a UI rule. In video (overlays, captions, graphics rendered into a frame) the exit mirrors the entrance and runs quicker: entrance `power3.out` with a long settle, exit `power2.in` / `power3.in` in 10-12 frames at 60 fps (~0.17-0.2s; only a snap exit runs shorter), holds and pushes `sine.inOut`, one curve shared by every channel of a move, linear only for a real clock or a constant-speed thing (`edit.md`).
- Never the weak built-ins (`ease`, `ease-in-out` keywords) for travel; use the tokens. Never bounce or elastic on standard controls.
- Reversible transitions (open/close) use the same path in both directions (in from the right, out to the right); mirror the curve.
- Multi-keyframe Web Animations: keep the animation's own `easing` linear and put the curve on each keyframe. An iteration easing warps time, so keyframe offsets stop being times, and any sound or effect scheduled at "offset x duration" lands off the visible hit (measured 220-350 ms off).
- Don't hand-roll new curves; pick from the set below or a curve tool (easing.dev, easings.co).

```css
:root {
  --ease-out:    cubic-bezier(0.23, 1, 0.32, 1);       /* default for UI enter/exit */
  --ease-expo:   cubic-bezier(0.16, 1, 0.3, 1);        /* arrivals ≥500ms: reveals, line rises, openings */
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);      /* on-screen travel, wipes, panels */
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);       /* sheets and drawers (iOS feel) */
  --ease-soft:   cubic-bezier(0.33, 1, 0.68, 1);       /* slow scale or drift on photos */
  --ease-exit:   cubic-bezier(0.55, 0.055, 0.675, 0.19); /* permanent removal only, ≤200ms */
  --dur-press: 140ms; --dur-hover: 180ms; --dur-ui: 220ms; --dur-overlay: 260ms;
  --dur-route: 400ms; --dur-reveal: 800ms; --dur-open: 1200ms;
  --stagger-item: 50ms; --stagger-line: 90ms;
}
```

- Material projects: M3 standard `cubic-bezier(0.2, 0, 0, 1)`. Never adopt the old framework default `(0.4, 0, 0.2, 1)` as a house curve.
- GSAP equivalents: `power2.out` / `power3.out` UI, `expo.out` reveals, `power2.inOut` travel, `"none"` for anything scrubbed; `back.out(1.7)` pop and `elastic` only in Experience, and never on a brand character. Overshoot by weight caps (character ≤5% / `back.out` ≤1.2, text and cards ≤10% / ≤1.7, a ≤5-frame snap ~16%) apply to brand characters and all video work (`experience.md` §3).
- Travel distance: UI entrances move 4-8px (popover, menu, tooltip) and never more than 20px; section reveals 16-24px. Sheets, drawers and toasts travel in from their own edge. 40px+ slides read cheap.
- One motion signature per product: the same easing and duration per transition type everywhere. Playful brands may run softer and longer; enterprise runs precise and short.

## 3. Durations by element

| Element | Duration | Notes |
|---|---|---|
| Press (`:active`) | 100-160ms | `scale(0.97)` (0.95-0.98), ease-out; never changes layout bounds |
| Hover colour / background | 150-200ms | gated by `(hover: hover) and (pointer: fine)` |
| Hover that moves | 200-300ms | rare; never lift/zoom on every card |
| Toggle, checkbox, switch thumb | 150-200ms | no overshoot |
| Tooltip | 125-200ms | 300-400ms delay on first hover, 0 on focus, instant for neighbours once one is open |
| Dropdown, select, popover, menu | 150-250ms | scale from the trigger's origin |
| Modal / dialog | 200-300ms in, 150-200ms out | stays centred; scale 0.96-0.98 + fade |
| Drawer / sheet | 250-300ms | `--ease-drawer`, or spring (section 5) |
| Toast | 200-300ms in, ~150ms out | CSS transition (retargets), not keyframes; ~5s visible, errors persist |
| Accordion | 250-300ms | `grid-template-rows` or `interpolate-size` (section 7) |
| Content replacing a skeleton | 150-200ms fade | no scale |
| Checkmark / line draw | ~300ms | |
| Route / view transition | 300-480ms | old out ~200ms, new in ~380ms with 60ms delay |
| Number count-up | 400-800ms | ease-out, `tabular-nums` so width never wobbles |
| Hold to confirm | 1.5-2s linear fill | release snaps back in 200ms ease-out |
| Spinner | 600-1000ms per turn, linear | only for <1s inline actions (`components.md`) |
| Persuade/Experience section reveal | 700-900ms | `--ease-expo`; never in Operate |
| Opening load sequence | finished by 1.2s | Persuade/Experience only |
| Celebration | micro ≤300ms, small ≤0.8-1.2s, medium 1.5-2s, rare 2-3s | tiers in experience.md §2; never block input; rare ones tap to skip |

- UI controls ≤300ms, always (user-paced hold fills excepted). A 180ms dropdown beats a 400ms one. Operate runs 150-250ms. Past 300ms on a control is a bug, not a style.
- Exit = 60-70% of the entrance. Phone UI may run 20-30% shorter.
- Asymmetric timing: slow where the user decides (hold, scrub), snap where the system responds (release, confirm).

## 4. Stagger and orchestration

- Between list items 30-60ms; between parts of a section (heading, text, picture) 60-90ms; between lines of a heading 80-110ms; characters 20-40ms only in 1-3 word headings.
- Cap total stagger at ~400ms: past 6-8 items, the rest arrive with the last step. ≤4 steps in a hero sequence.
- Stagger only real lists. Everything-at-once is wrong where items have order; staggering unrelated blocks is noise.
- Never block input during a stagger or entrance. Clicks land on the final position.
- One focal motion per region at a time; two things competing for the eye cancel out.
- Order of entry follows reading order: heading, then text, then picture, then action.

## 5. Springs and physics

- Use springs for: drag release, gesture-driven motion, interruptible position/scale/rotation, and "alive" elements. Use durations for predetermined UI fades and colour.
- Default UI spring is critically damped (no bounce). Bounce only when the gesture carried momentum, or in Experience/celebration moments.

| Use | Motion (`motion`) | Apple (damping, response) | react-spring |
|---|---|---|---|
| Default UI, reposition | `{ type: "spring", visualDuration: 0.35, bounce: 0 }` | 1.0, 0.3-0.4 | `{ tension: 170, friction: 26 }` |
| Large move / layout | `visualDuration: 0.4, bounce: 0` | 1.0, 0.4 | `{ tension: 120, friction: 22 }` |
| Sheet / drawer | `visualDuration: 0.3, bounce: 0` (0.2 after a drag release) | 1.0, 0.3 (0.8 after a drag release) | `{ tension: 210, friction: 29 }` |
| Rotation | `visualDuration: 0.4, bounce: 0.2` | 0.8, 0.4 | |
| Flick / drag release | `bounce: 0.15-0.2` | 0.8 | `{ tension: 200, friction: 25 }` |
| Playful pop (Experience only) | `bounce: 0.3-0.4` | 0.6-0.7 | `{ tension: 180, friction: 12 }` |

- Motion `bounce` ≈ 1 minus Apple's damping ratio. Motion's default spring is bouncy (ratio ~0.5): always set `bounce` explicitly. react-spring's default (170/26) is critically damped; more tension = faster, more friction = less overshoot, more mass = heavier; critical damping is `friction ≈ 2·√tension` at mass 1.
- Never spring functional data (charts, progress, numbers that must be read).
- Velocity handoff: the release velocity becomes the spring's initial velocity. Motion and react-spring take absolute px/s (`velocity`); APIs that want relative velocity get `v / (target - current)`. Never restart from zero velocity.
- Decide commit vs reverse by velocity sign when |v| is above threshold, else by position past 50%. Swipe-dismiss when velocity > ~0.11 px/ms regardless of distance.
- Split 2D motion into independent X and Y springs.

```js
// where a flick lands (iOS-style deceleration); d = 0.99 for snappier
const project = (vPxPerS, d = 0.998) => (vPxPerS / 1000) * d / (1 - d);
const target = nearestSnapPoint(current + project(velocity));
// rubber-band past a boundary: resistance grows with overshoot
const rubber = (over, dim, c = 0.55) => (over * dim * c) / (dim + c * Math.abs(over));
```

- Boundaries get friction (rubber-band), never hard stops. Release past a boundary springs back with `bounce: 0`.

## 6. Gestures and interruptibility

- Respond on `pointerdown`, not on release. Feedback within 100ms of any input.
- Drags track 1:1 with the grab offset kept (the point under the finger stays under the finger). Use `setPointerCapture`.
- Claim a drag only after ~10px of travel (hysteresis) so taps and scrolls pass through. Keep the last ~100ms of positions to compute release velocity.
- `touch-action: pan-y` on horizontal swipers (`pan-x` on vertical); a swipe along the page's scroll axis must scroll the page.
- Clean up on `pointercancel`, `lostpointercapture`, a second pointer, release outside, and window `blur`: clear drag state and release capture. The next tap must work without a reload. Ignore extra touches mid-drag.
- Never lock input during a transition. A new input retargets the running spring from the current on-screen (presentation) value and keeps velocity; replacing the animation on a reversal hits a velocity "brick wall".
- CSS transitions retarget; CSS keyframes restart from zero. Use transitions for rapidly retriggered UI (toggles, toasts, hover); keyframes only for one-shot sequences.
- For drags and flicks use springs (Motion, react-spring, GSAP InertiaPlugin), never CSS transitions.
- Rapid repeat triggers cancel the running animation and set the final state. Never depend on `animationend`/`transitionend` for correctness.
- No double-tap delays unless double-tap is a real gesture. Haptics, sound and visual fire on the same frame.

## 7. Properties and CSS techniques

- Animate `transform` (or the individual `translate`, `scale`, `rotate` properties) and `opacity`. These stay on the compositor.
- Conditional: `clip-path` and `mask` (repaint; fine on medium elements, great for reveals); `filter: blur()` ≤8px on small regions, short, never on body text (≤2px blur masks a crossfade well); `backdrop-filter` only on a functional bar.
- Never animate `width`, `height`, `top`, `left`, `margin`, `padding`, `font-size`, `font-weight`, `letter-spacing`, `border-width`. Use FLIP or transforms. Only exception: a disclosure/accordion opening to its content height (grid trick or `interpolate-size`, below), short and local.
- Shadows: animate the `opacity` of a pseudo-element that carries the shadow, not `box-shadow` itself.
- Never `transition: all`. Name each property.
- Never enter from `scale(0)`. Start at 0.95-0.98 (0.9 minimum for tiny elements) plus opacity. A pure fade with no transform reads as a glitch on overlay entrances (popover, menu, modal, toast); content swaps and skeleton replacement stay pure fades.
- Popovers, menus and tooltips scale from the trigger: `transform-origin: var(--radix-popover-content-transform-origin)` (Radix), `var(--transform-origin)` (Base UI), or the library's equivalent. Modals stay centred and scale from centre.
- Don't drive child transforms through a parent CSS custom property in a hot path; it restyles the whole subtree every frame.
- Hover motion only inside `@media (hover: hover) and (pointer: fine)`.

```css
/* Entry and exit for popover/dialog without JS */
.pop { opacity: 1; translate: 0 0; scale: 1;
  transition: opacity 200ms var(--ease-out), translate 200ms var(--ease-out), scale 200ms var(--ease-out),
              display 200ms allow-discrete, overlay 200ms allow-discrete; }
.pop:not(:popover-open) { opacity: 0; translate: 0 4px; scale: 0.97; }
@starting-style { .pop:popover-open { opacity: 0; translate: 0 4px; scale: 0.97; } }

/* Accordion: grid trick works everywhere */
.acc { display: grid; grid-template-rows: 0fr; transition: grid-template-rows 280ms var(--ease-out); }
.acc[data-open] { grid-template-rows: 1fr; } .acc > * { overflow: hidden; }
/* Chromium 129+: native height: auto, e.g. <details> */
:root { interpolate-size: allow-keywords; }
details::details-content { height: 0; overflow: clip; transition: height 280ms var(--ease-out), content-visibility 280ms allow-discrete; }
details[open]::details-content { height: auto; }

/* Instant tooltips once one is open */
.tip[data-instant] { transition-duration: 0ms; }
```

- `@starting-style` gives first-render entry transitions; pair with `transition-behavior: allow-discrete` for `display` and `overlay`.
- CSS springs: `transition-timing-function: linear(...)` generated from a spring tool; fine for fixed UI springs, not for gestures.
- `@property` registers a typed custom property so it can animate (counters, angles, progress values).
- View transitions:
  - Same document: `document.startViewTransition ? document.startViewTransition(() => updateDOM()) : updateDOM()` (always feature-detect). Multi-page: `@view-transition { navigation: auto; }` in both pages.
  - Morph a shared element with a unique `view-transition-name`; group with `view-transition-class`. Style `::view-transition-old(root)` / `::view-transition-new(root)`.
  - Direction: `startViewTransition({ update, types: ["forward"] })`, then style under `:active-view-transition-type(forward)`.
  - ≤480ms. They do NOT respect reduced motion automatically: wrap the custom CSS in `@media (prefers-reduced-motion: no-preference)`; under reduced motion skip the transition or keep only the default root crossfade.
  - Spatial logic: forward = enters from right, back = from left; going deeper = from below; same-container swap = crossfade; modal close = fast fade.

## 8. Scroll-driven design

**Reveals**
- Once per element, never on scroll back up. Fire when the element's top is 85-90% down the viewport: IntersectionObserver `rootMargin: '0px 0px -12% 0px'`, `threshold: 0.1`, then `unobserve`.
- Rise 16-24px (12-32px range) + opacity, or a line mask (`translateY(105-110%)` inside `overflow: clip`, padding-bottom 0.08-0.12em so descenders survive). Mask is the loudest reveal: once per page.
- Pick one reveal style and repeat it; break it once, at the peak. The same fade-up on every block is a tell.
- Nothing above the fold waits for scroll. Nothing in view stays hidden >900ms. A reveal that never fires (blank band) is the worst failure.
- Hidden start states only under `html.js` (one inline `document.documentElement.classList.add('js')` in `<head>`) AND `prefers-reduced-motion: no-preference`.
- For a mask reveal on a sticky child, observe the sticky parent; a zero-area target never intersects.

**Native scroll timelines (preferred for simple scrubs)**

```css
@supports (animation-timeline: view()) {
  @media (prefers-reduced-motion: no-preference) {
    .reveal { animation: rise linear both; animation-timeline: view(); animation-range: entry 0% cover 35%; }
    .progress { animation: grow linear both; animation-timeline: scroll(root block); transform-origin: 0 50%; }
  }
}
@keyframes rise { from { opacity: 0; translate: 0 24px; } }
@keyframes grow { from { scale: 0 1; } }
```

- The `animation` shorthand resets `animation-timeline`: declare the timeline after it. Use `linear` and `both` for scrubs.
- `overflow: hidden` on an ancestor breaks view timelines; use `overflow: clip`.
- Named timelines: `view-timeline-name: --card`, `scroll-timeline-name`; `timeline-scope` reaches across subtrees.
- Supported in Chromium 115+ and Safari 26; Firefox behind a flag. Keep the `@supports` guard so content is visible without it.
- Use native timelines for progress bars, reveals and simple parallax. Use GSAP ScrollTrigger for pinning, sequencing, snapping.

**Pins and scrub**
- ~1 screen of scroll per step, ≤3 screens per pinned stage, text on every held screen. Show progress as words ("2 of 4"), never a hairline bar or "01/08".
- 2-3 scroll scenes per page (never more than 4), each 1-3 screens, a quiet section between them, together ≤60% of the page.
- Scrub is linear (`ease: "none"`) and locked to the scrollbar: `scrub: true` when Lenis runs (it already smooths); without Lenis `scrub: 0.5-1` adds weight. Map story beats to timeline labels and snap to them.
- Prefer `position: sticky` over JS pinning when nothing transforms. Never pin inside a transformed ancestor.
- Pacing: <400px of scroll per section flashes past unread; 1200-1600px suits a heading plus 2 lines; >2500px reads broken, use once for the peak. ≤6 sections per story, ≤2 statement sections.
- Sideways gallery: pin only if the row is <3 screens, move 1:1 with scroll, support keyboard. Otherwise a native `scroll-snap-type: x mandatory` row.
- Canvas frame sequence: footage 4-12s of slow continuous camera motion, no hard cuts; frames = fps × seconds (~150KB each at 1920px). Sticky full-viewport canvas, DPR ≤2, cover-fit draw, `index = round(progress × (n - 1))`, redraw only when the index changes (GSAP: tween `{ frame }` with `snap: "frame"`, `ease: "none"`). Preload every 5th frame first, ship an 828px mobile set, cut fps before width, keep desktop + mobile under ~60MB, fall back to the nearest loaded frame.

**Parallax and effects**
- Parallax travel <8% of the element; pictures sit at 106-110% inside their frame. Scroll-linked scale 0.94-1.15.
- Nothing moves across text being read. Dims never below 40%. No full-viewport moving backgrounds, no slow ~0.2Hz oscillation, no abrupt brightness jumps.
- Colour by chapter = hard cuts at section boundaries, never an observer recolouring the whole page; header ink follows in 300ms. Ink-fill text: once per page, one statement of 3-5 lines, ≥32px, starts at 45% ink, full ink without scroll timelines or under reduced motion.

**Smooth scroll**
- Default: none. Native scroll plus `scroll-behavior: smooth` for anchor links; it and JS `scrollTo`/`scrollIntoView({ behavior: "smooth" })` go instant under reduced motion.
- If a Persuade/Experience page truly needs inertia (WebGL sync, heavy parallax): Lenis only, `lerp` 0.1-0.14, native on touch, never initialised under reduced motion. Never on app, docs or content UIs.
- Never scroll hijacking, wheel capture, scroll-jacked section snapping, or transform-based scrollers (they break `position: fixed`, sticky, find-in-page, anchors and keyboard).
- Never a main-thread `scroll` listener for effects; use IntersectionObserver, CSS timelines, ScrollTrigger or `useScroll`. If a listener is unavoidable: `passive: true`, coalesced into one rAF.

## 9. Motion budget by mode

**Persuade (pages)**
- First frame: headline, sentence and picture painted in HTML. Readable within 0.5s; load sequence done by 1.2s, ≤4 elements (lines rise ~100-990ms, picture opens ~150-1150ms, sentence + button ~420-980ms).
- Parts: one signature move tied to the page's idea, 2-3 scroll scenes, per-section entrances varied by content, feedback on every control, one moving picture per screen. ≥8 moving elements across the page.
- The nav never animates in. One marquee max, pausable. Carousels never auto-rotate without prev/next/pause. One extraordinary moment, never several.
- No preloaders, loading-percentage counters, entry gates, scramble or typewriter headlines, custom cursors, infinite decorative loops (pulsing dots, floating shapes, shimmer text, rotating badges).

**Operate (apps, dashboards, tools)**
- Motion is feedback only: press, hover, focus, state change, overlays, reorder, optimistic update. No entrances, no load choreography; the screen loads straight into the task.
- Status bars and data never animate for show. Charts are readable at first paint: no draw-in, or ≤300ms and none under reduced motion. Row highlight on remote change fades over 1-2s; a 2-4px non-looping shake marks an error or remote conflict.
- Onboarding and empty-to-first-item may carry one richer moment.

**Read (docs, articles)**: no entrances; smooth anchor scroll and focus moves only.

**Experience (games, toys, celebrations)**: motion is the medium; bounce, squash and stretch, overshoot allowed on non-brand objects. A brand character or mascot never squashes, stretches or deforms: uniform scale, tilt and move only. Full juice rules (hit-stop, trauma shake, combos, particles) live in `experience.md`.
- Celebrations scale with consequence (tiers, layered timeline, confetti rules: experience.md §2). Never delay completion for a flourish.

**Video (thumbnails in motion, overlays, captions, motion graphics)**: rules in `edit.md`. Exits mirror entrances (ease-in allowed there), overshoot by weight, no elastic or bounce, nothing moves while words that matter are on screen.

**Decks and video-style pieces**: most slides need no animation (1-2 in 10, only when reveal order carries meaning; `decks.md`). For motion pieces, write the scene list first, key everything to one clock, use exactly 3 helpers (enter, draw, pop) and no other easing. Something is always moving except deliberate held beats; text holds long enough to read twice. Verify with a filmstrip at each scene boundary ±0.15s.

## 10. Reduced motion and accessibility

- Reduced means fewer and gentler, not none. Keep opacity, colour and state feedback; drop travel, scale, parallax, springs, overshoot, autoplay, smooth scroll and view-transition movement (a crossfade may stay).
- The reduced state is the finished state: every reveal shows, every loop stops, videos show their poster, Lottie shows its final frame.
- Author motion inside `@media (prefers-reduced-motion: no-preference)` so the default is still. A global `0.01ms` kill switch is a backstop, never the design (shipping it alone is a finding; it still fires `transitionend`).
- JS libraries: Motion `<MotionConfig reducedMotion="user">`; GSAP `gsap.matchMedia()` condition; react-spring `Globals.assign({ skipAnimation: true })`; Lenis never initialised; canvas/WebGL loops render one still frame.
- `prefers-reduced-transparency: reduce` → solid surfaces, no blur. `prefers-contrast: more` → solid ground and defined borders.
- WCAG: anything that moves, blinks or auto-updates for >5s gets pause/stop (2.2.2); ≤3 flashes per second (2.3.1); motion from interaction can be disabled (2.3.3). Carousels pause on hover, focus and reduced motion.
- No sound without opt-in. Autoplay video is muted and off under reduced motion.
- Listen for changes: `matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', ...)`.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important; scroll-behavior: auto !important; } /* backstop only */
}
```

## 11. Performance

- Budget: 60Hz = 16.7ms per frame, plan ~10ms of your own work; 120Hz = 8.3ms. Simplify any effect that drops below 50fps. INP <200ms, CLS <0.1, LCP <2.5s.
- Compositor only: `transform`, `opacity`. Layout triggers: size, position, margin, padding, font-size. Paint triggers: colour, background, box-shadow.
- `will-change`: set on start, remove on complete; static only on a few long-lived animated elements. Each layer costs GPU memory; never as a blanket rule.
- Read all DOM measurements, then write; never interleave. Use FLIP for layout moves.
- Continuous values live in motion values or refs, never component state (`useState` per frame re-renders).
- rAF loops scale every step by elapsed time (`dt`), never a per-frame constant: on a 120Hz screen a per-frame step runs double speed. Never allocate objects inside the loop.
- Heavy canvas work (frame decoding, particles, WebGL) can move off the main thread with `OffscreenCanvas` in a Worker.
- `Save-Data` or a slow connection: drop autoplay video, frame sequences and heavy runtimes; serve the poster or still.
- Pause everything off-screen and in hidden tabs: rAF loops, video, Lottie, Rive, canvas, WebGL (`visibilitychange` + IntersectionObserver). Pause toast timers while the tab is hidden.
- Cap DPR at 2 for canvas, WebGL and Lottie; 1 on low-end. Detect low-end by measured fps, not UA sniffing.
- Lazy-load heavy runtimes (Lottie, Rive, three) near the viewport behind a sized placeholder; code-split with dynamic `import()`. Defer non-critical animation until after load.
- One JS library per animated property; two libraries on one `transform` fight.
- Under main-thread load, give Motion a full `transform` string rather than `x`/`y` shorthands so it can hand off to WAAPI.
- Profile in DevTools Performance (long tasks, layout thrash) and Rendering (paint flashing, layer borders, fps) on a real mid-range phone.

## 12. Library choice

| Job | First choice | Instead of |
|---|---|---|
| Hover, press, toggle, simple enter/exit | CSS transitions + `@starting-style` | any JS library |
| Imperative one-off, sequenced in JS | WAAPI `el.animate()` | a library for 3 tweens |
| React enter/exit, layout, shared element | Motion (`motion/react`) | hand-rolled FLIP |
| Gesture physics, drag, momentum | Motion springs / react-spring | CSS transitions |
| Page / route transition | View Transitions API | Barba (only for legacy MPA + GSAP) |
| Scroll reveal, progress, light parallax | IntersectionObserver or CSS `view()`/`scroll()` | AOS, scroll listeners |
| Scroll story: pin, scrub, snap, sequence | GSAP + ScrollTrigger | native timelines (can't pin) |
| Line splitting for type reveals | GSAP SplitText (`autoSplit`) | manual span splitting |
| Smooth scroll (rare) | Lenis | Locomotive v4, custom lerp |
| Designer-made linear vector animation | dotLottie | lottie-web JSON, GIF |
| Interactive, stateful vector (game UI, reward states) | Rive state machine | Lottie segments + code |
| SVG line draw / morph, small bundle | anime.js v4 or GSAP DrawSVG/MorphSVG | |
| 2D particles, many sprites | PixiJS v8 (raw Canvas2D under ~300 particles) | DOM nodes |
| 3D | Three.js / R3F, only when depth is the subject (`experience.md`) | Vanta or blob backgrounds |

- CSS first. React-only libraries only when the project already uses React. No-bundler single page: GSAP, Motion vanilla, anime, Lenis, dotLottie, Rive canvas from a pinned CDN version.
- Rough gzip cost: CSS 0; Motion vanilla `animate` ~2.5KB; Motion React ~30KB (~5KB with `LazyMotion` + `m`); GSAP ~25KB + ScrollTrigger ~12KB; anime core ~10KB; react-spring ~20KB; Rive and dotLottie ship WASM runtimes (hundreds of KB, lazy-load them).

## 13. Current API patterns

**WAAPI**
```js
const a = el.animate([{ opacity: 0, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }],
  { duration: 220, easing: 'cubic-bezier(0.23, 1, 0.32, 1)', fill: 'both' });
await a.finished; a.commitStyles(); a.cancel();   // keep the end state without a lingering fill
```

**Motion** (package `motion`)
- React: `import { motion, AnimatePresence, MotionConfig } from "motion/react"`. Vanilla: `import { animate, scroll, inView } from "motion"`.
- `<MotionConfig reducedMotion="user">` at the root; `useReducedMotion()` per component.
- AnimatePresence needs a direct child with a unique `key` and an `exit` prop; `mode="wait"` for swaps, `mode="popLayout"` for lists.
- `transition` inside `whileHover` applies on hover-in; the outer `transition` applies on hover-out.
- `layout` is expensive: prefer `layout="position"`, use `layoutId` sparingly, never on every list item.
- Motion owns `transform`: don't also set a CSS `transform` (e.g. `translate(-50%,-50%)`) on an element it animates; centre with flex/inset or Motion's `x: "-50%"`.
- Scroll: `useScroll({ target, offset: ["start end", "end start"] })` → `useTransform` → `style`. `whileInView` with `viewport={{ once: true, amount: 0.3 }}`.
- Bundle: `import * as m from "motion/react-m"`, then `<LazyMotion features={domAnimation} strict><m.div /></LazyMotion>`.

**GSAP + ScrollTrigger** (3.13+, every plugin free in the `gsap` package)
```js
gsap.registerPlugin(ScrollTrigger, SplitText);           // forgetting this fails silently
const mm = gsap.matchMedia();
mm.add({ desk: "(min-width: 800px)", motion: "(prefers-reduced-motion: no-preference)" }, (c) => {
  if (!c.conditions.motion) return;
  const panels = gsap.utils.toArray(".panel");
  gsap.timeline({ scrollTrigger: { trigger: ".story", pin: true, scrub: 1, end: () => "+=" + innerWidth * (panels.length - 1),
      anticipatePin: 1, invalidateOnRefresh: true, fastScrollEnd: true, snap: { snapTo: "labels", duration: { min: 0.2, max: 1 } } } })
    .addLabel("a").to(panels, { xPercent: -100 * (panels.length - 1), ease: "none" }).addLabel("b");
});  // reverts automatically when a query flips
```
- ScrollTrigger goes on the timeline, never on tweens nested inside it. Many elements: loop with one trigger each, or `ScrollTrigger.batch(".x", { onEnter: b => gsap.to(b, { autoAlpha: 1, y: 0, stagger: 0.06 }), once: true })`.
- Animate `x, y, xPercent, scale, rotation, autoAlpha`. Scrubbed tweens use `ease: "none"`.
- Two scroll tweens on one property jump: use `fromTo`, `immediateRender: false`, or one timeline.
- Viewport-dependent values are functions (`end: () => ...`) with `invalidateOnRefresh: true`. Call `ScrollTrigger.refresh()` after images, fonts or DOM changes; `ScrollTrigger.config({ ignoreMobileResize: true })`; `markers` in dev only.
- Cleanup: vanilla `gsap.context(() => {...}, root)` then `ctx.revert()`; React `useGSAP(() => {...}, { scope: ref })` from `@gsap/react`.
- Type reveal: `SplitText.create(el, { type: "lines", mask: "lines", autoSplit: true, onSplit: s => gsap.from(s.lines, { yPercent: 105, stagger: 0.09, duration: 0.8, ease: "expo.out" }) })`.

**Lenis** (package `lenis`)
```js
import Lenis from "lenis"; import "lenis/dist/lenis.css";
if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
  const lenis = new Lenis({ lerp: 0.1, autoRaf: false });   // touch stays native by default
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((t) => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);
}   // without GSAP: new Lenis({ lerp: 0.1, autoRaf: true })
```

**dotLottie** (`@lottiefiles/dotlottie-web`, web component `@lottiefiles/dotlottie-wc`)
- `const d = new DotLottie({ canvas, src: "/a.lottie", autoplay: true, loop: false })`; scroll-driven `d.setFrame(p * d.totalFrames)`; `d.destroy()` on unmount.
- Budget: <100KB ideal, <200KB acceptable, ready <500ms, <50MB memory per instance (`.lottie` is up to ~90% smaller than JSON). SVG renderer (lottie-web) only for a few simple icons; canvas for complex or many; `DotLottieWorker` for files >100KB, several at once, or scroll playback. `renderConfig: { devicePixelRatio: 1 }` on low-end.
- After Effects export: no expressions, merged shapes, solid fills, no raster layers. Lazy-load via IntersectionObserver. Reduced motion: one static frame.

**Rive** (`@rive-app/canvas`, React `@rive-app/react-canvas`)
- `const r = new Rive({ src, canvas, stateMachines: "Main", autoplay: true, onLoad: () => r.resizeDrawingSurfaceToCanvas() })`; `r.cleanup()` on teardown.
- Inputs (boolean, number, trigger) match editor names exactly; null-check before `input.value = true` / `input.fire()`. React: `useRive` + `useStateMachineInput`, preload with `useRiveFile`. Bind data through ViewModels (`autoBind: false` for manual control).
- Files <2MB, vector over raster. Best for designer-authored reward states where code only fires triggers.

**anime.js v4**
- `import { animate, createTimeline, stagger, svg, onScroll, createScope } from "animejs"`.
- `animate(".el", { x: 250, duration: 800, ease: "outQuad", loop: true, alternate: true })`. Ease names drop the prefix (`"inOutQuad"`, `"outElastic(1, .5)"`); `ease` not `easing`.
- Line draw: `animate(svg.createDrawable("path"), { draw: ["0 0", "0 1"] })`. Grid stagger: `stagger(80, { from: "center", grid: [c, r] })`. Scroll: `autoplay: onScroll({ sync: true })`.
- One call with many targets beats a loop of calls. Callbacks are `onComplete`/`onUpdate`; timelines are `createTimeline().add(target, params, position)`.
- React cleanup: `const scope = createScope({ root }).add(() => {...})`, then `scope.revert()`.

**Do not copy outdated APIs**

| Outdated | Current |
|---|---|
| `import ... from "framer-motion"` | `"motion/react"` (package `motion`) |
| `useViewportScroll`, `AnimateSharedLayout` | `useScroll`, `layoutId` / `LayoutGroup` |
| `ScrollTrigger.matchMedia()` | `gsap.matchMedia()` + `gsap.context` / `useGSAP` |
| `gsap-trial`, "Club plugins are paid" | every plugin ships free in `gsap` 3.13+ |
| `new SplitText()` + manual re-split on resize | `SplitText.create({ autoSplit: true, onSplit })` |
| anime v3 `anime({ targets, easing })`, `anime.timeline()`, `complete:` | v4 `animate(targets, { ease })`, `createTimeline()`, `onComplete:` |
| `@studio-freight/lenis` | `lenis` |
| Locomotive Scroll v4 (`data-scroll-container`, `scrollerProxy`) | Lenis (native scroll position) |
| `@lottiefiles/lottie-player`, `@dotlottie/player-component` | `@lottiefiles/dotlottie-web` / `-wc` |
| `rive-react` | `@rive-app/react-canvas` |
| `max-height: 9999px` accordions | `grid-template-rows` or `interpolate-size` |
| scroll listener + `getBoundingClientRect` reveals | IntersectionObserver or `view()` timelines |
| PixiJS v7 `cacheAsBitmap`, `baseTexture`, `ParticleContainer(count, …)` | v8 `cacheAsTexture()`, `textureSource`, `Particle` + `addParticle` |
| `renderer.setPixelRatio(devicePixelRatio)` | `Math.min(devicePixelRatio, 2)` |
| `setInterval` animation loops | `requestAnimationFrame` / `setAnimationLoop` |
| `gsap.config({ nullTargetWarn: false })` "for reduced motion" | does nothing; use `gsap.matchMedia` |

- Pin every CDN version; never `@latest`.

## 14. Verify motion

- Review motion in slow motion (2-5x via DevTools Animations panel) and frame by frame; review again the next day with fresh eyes. Test gestures on a real phone.
- Frame by frame without DevTools: `tools/taste/motion.mjs` films the page on a virtual clock into time-stamped contact sheets, with key presses and scripted moves on cue (`tools.md`). Open every sheet.
- Before screenshots, wait for reveals to finish: `document.getAnimations()` idle (3s cap). Capture with motion on and with reduced motion on; reduced motion must leave no first-screen text hidden.
- Scroll pages fail silently: sample ≥16 scroll positions per process.md §9 (Drive the states). A clean build proves nothing here.

## 15. Review standard

Non-negotiables: justified motion; frequency-appropriate; responsive easing; UI ≤300ms; correct origin, no `scale(0)`; interruptible; compositor-only properties; reduced motion + hover gating; asymmetric enter/exit; cohesion (one signature; when unsure, delete).

Escalate on sight: `transition: all`; `scale(0)` or transform-less fade on an overlay entrance; `ease-in` on UI (video exits excepted) or a built-in keyword curve on movement; animated keyboard or 100+/day actions; UI >300ms; centre origin on an anchored popover; keyframes on toasts/toggles; layout properties; bounce on a control; Motion shorthands under load; parent CSS var driving children; missing reduced motion; ungated hover; symmetric press/hold timing; everything-at-once where a 30-60ms stagger belongs; main-thread scroll listeners; reveals that can leave a blank band; motion as the only signal of a state change; loops >5s with no pause.

Fix order: delete → reduce → easing → origin → interruptibility → GPU properties → asymmetric timing → polish (blur mask, stagger, `@starting-style`, spring) → accessibility and cohesion.

Output format, always a table, never a bullet list:

| Before | After | Why |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out)` | Names properties; under the UI cap; ease-out |
| Menu scales from centre, `scale(0)` | `scale(0.97)` + fade from `--radix-popover-content-transform-origin` | Origin-aware; never from nothing |

- Then findings in tiers: feel-breaking, missed simplifications, performance, interruptibility/timing, origin/cohesion, accessibility. Cite `file:line`.
- End with one word on its own line: **Block** (any feel-breaking, performance or accessibility finding) or **Approve**.

## 16. Vocabulary (use exact words in briefs and prompts)

- Entrances: fade, slide in, scale in, pop in (overshoot), reveal (clip/mask), enter/exit.
- Sequencing: keyframes, tween, stagger, orchestration, delay, duration, fill mode, stepped.
- Transforms: translate, scale, rotate, skew, 3D tilt, flip, perspective, transform origin, origin-aware.
- State: crossfade, continuity transition, morph, shared element transition, container transform, shared axis, fade through, layout animation, accordion, direction-aware.
- Scroll: scroll reveal, scroll-driven, scrub, pin, snap, parallax, page transition, view transition.
- Feedback: hover, press/tap, hold to confirm, drag, drag to reorder, swipe to dismiss, rubber-banding, shake, ripple.
- Easing: ease-out, ease-in, ease-in-out, linear, cubic-bezier, asymmetric easing.
- Springs: stiffness, damping, damping ratio, mass, bounce, response / perceptual duration, momentum, velocity, projection, interruptible.
- Ambient: marquee, loop, alternate (yoyo), orbit, pulse, float, idle.
- Polish: blur mask, clip-path vs mask (soft edges), before/after slider, line drawing, text morph, number ticker, tabular numbers.
- Game feel: anticipation, follow-through, squash and stretch (never on a brand character), hit-stop, screen shake, juice.
- Performance: fps, jank, dropped frame, compositing, layer, will-change, layout thrashing, FLIP.
- Principles: perceived performance, frequency of use, spatial consistency, causality.
