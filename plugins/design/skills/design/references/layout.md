# Layout and Space

Use when: setting the frame, grid, spacing, surfaces, depth, stacking, scrolling or responsive behaviour of any page, screen, game UI or prototype. Type sizes live in typography.md, slide geometry in decks.md, section-by-section page design in pages.md, app shells in apps.md.

## 1. Frame and margins

- Use one grid and one pair of equal outer margins per surface. Unequal left/right margins are a defect, never a style.
- Margins: 16-32px. Never under 16px from the viewport edge, phone included; 16-20px on phone, 24-32px ideal on desktop.
- Put the nav, the content and the footer on the same inset. Logo and menu share the content edge.
- Bleeds start from a margin: a picture or field either sits inside the frame or runs to the viewport edge, never stops at a random inset.
- Keep asymmetry inside the frame. Anchor off-centre compositions on a third, on 42%, or on the midpoint; never on an arbitrary value.
- Never draw the grid (no visible column lines, crosshairs, crop marks, dashed guides).
- Write the grid arithmetic in a CSS comment and make it close: `3 x 372 + 2 x 17 = 1152`, `12 x 77 + 11 x 16 = 1100`.
- Pick the column count from the item count. Four equal tiles with one orphan on the next row means the wrong count. Mixed spans that change by row and land on the same column lines beat a uniform four-up.
- Columns per band: 4 on phone, 8 on tablet, 12 on desktop.
- Use CSS Grid for two-dimensional layout, never flex percentage maths. Use `gap` for sibling rhythm; never margins between siblings.

```css
:root {
  --margin: clamp(1rem, 2.2vw, 2rem);      /* 16-32px */
  --gutter: clamp(0.75rem, 1.4vw, 1.5rem); /* 12-24px */
  --columns: 12;
}
.grid { display: grid; grid-template-columns: repeat(var(--columns), minmax(0, 1fr));
        gap: var(--gutter);
        padding-left: max(var(--margin), env(safe-area-inset-left));
        padding-right: max(var(--margin), env(safe-area-inset-right)); } /* insets differ per side in landscape */
.auto  { display: grid; gap: var(--gutter);
         grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr)); }
```

## 2. Container widths

Choose by mode (see process.md for modes). A centred 1100-1300px box picked by reflex is a tell.

| Mode | Frame | What gets constrained |
|---|---|---|
| Persuade / Experience | Full width inside the margins; cap the frame at 1760-1920px on huge screens | Only text measure (see typography.md); pictures and fields run large |
| Operate | Fluid with padding 17-64px (median ~29), or centred 1088-1250px | Narrow tables (≤5 cols, ≤6 rows) ~760px wide and paired, never stretched to 1600 |
| Read | Text column 60-75ch (~640-720px), media may break out to the frame | The reading column, always |
| Email | 600px max, single column, table layout, inline CSS | Everything |
| Phone mock | 390x844 frame, radius ~44px, centred on desktop | Content inside safe-area insets; no drawn status bar or keyboard |

- Never let anything stretch to 4K: every surface has a maximum.
- Full-bleed is for grounds, fields and pictures. Text never runs edge to edge.
- Use the breakout grid for Read and editorial layouts:

```css
.flow { display: grid; grid-template-columns:
  [full-start] minmax(var(--margin), 1fr) [content-start] min(65ch, 100%) [content-end] minmax(var(--margin), 1fr) [full-end]; }
.flow > * { grid-column: content; }
.flow > .bleed { grid-column: full; }
```

## 3. Spacing scale

- Use a 4px base with an 8px rhythm. An 8-only scale misses the 4/12/20 steps dense UI needs.
- Copy exact source values when matching an existing product or brand (5px stays 5px). The scale is for new work.
- Space is relational: related items sit closer than unrelated ones, always. One repeated gap everywhere is monotony.

```css
:root {
  --space-1: 0.25rem;  /* 4  */   --space-6: 2rem;     /* 32  */
  --space-2: 0.5rem;   /* 8  */   --space-7: 3rem;     /* 48  */
  --space-3: 0.75rem;  /* 12 */   --space-8: 4rem;     /* 64  */
  --space-4: 1rem;     /* 16 */   --space-9: 6rem;     /* 96  */
  --space-5: 1.5rem;   /* 24 */   --space-10: 8rem;    /* 128 */
  --space-section: clamp(4.5rem, 2.25rem + 11.4vw, 15rem); /* ~80px at 390, ~200 at 1440, cap 240 (Persuade) */
}
```

| Relationship | Gap |
|---|---|
| Icon to label, label to its value | 4-10px (label to field 8-10) |
| Inside a component (padding, rows of a list) | 8-16px |
| Between components in a group (fields, cards) | 16-24px (card gap default 16) |
| Between groups / blocks on a screen | 24-48px |
| Between sections, Operate | 32-64px (a 1px rule with 32px above and below is the settings pattern) |
| Between sections, Read | 64-96px |
| Between sections, Persuade | 120-240px desktop, 72-112px phone |

- Density dials (pick one per product, keep it): spacious 4/8/24/32/48/64/96; standard 4/8/16/24/32/48/64; dense 2/4/8/12/16/24/32.
- Card padding 12-32px (median 20, 24 on Persuade); 32px for quotes, 48px for a CTA band.
- Move row pitch, padding and type size together when changing density. Row pitch: sparse 56-92px, medium 44-56px, dense lists 28-36px, dense tables 36-42px.
- Desktop medium to high density, tablet medium, phone low. Power tools dense; consumer products airy.

## 4. Section rhythm

- The gap between sections is always clearly larger than any gap inside a section.
- Space above a heading ≥2x the space below it. A heading belongs to what follows.
- Rhythm comes from contrast between tight and generous intervals: follow a dense passage with a quiet one; alternate image/type, dense/open.
- Size each section to its content. `min-height: 100svh` only for a real full-screen moment.
- Content is present on first paint; no section is blank while waiting for a reveal.
- Every section opens with a heading placed on the margin or the anchor line, the same way each time.
- Repetition aids recognition. Break the system once, on purpose, where content or priority changes; never vary for variety's sake.
- Persuade section grounds may change with a hard edge (chapters); never a fade. Operate keeps one ground. Detail in colour.md.

## 5. Voids versus holes

- A void is deliberate empty space closed by something: the picture, a picture spanning the band, type spanning it, an element anchoring its corner. A hole is empty space nothing closes.
- Allow one deliberate rest per page.
- Holes, all defects:
  - more than 40% of a screen of plain ground between sections;
  - any blank stretch ≥60% of a screen;
  - two or more near-empty screens on one page;
  - text huddled in one half with the other half empty;
  - an empty middle third;
  - a single empty block ≥28% of the first screen;
  - a card with a blank band >40px because it was stretched to match a neighbour;
  - a first-viewport multi-column layout where one column runs far below the fold.
- Text in one half: put the picture, a second column, a list or a figure in the other half.
- When a section looks empty, make the main element bigger or cut the section. Never fill it with ornament.

## 6. Edges and alignment

- Limit the page to 2-3 left edges for all text. Six edges reads as undecided.
- Reuse the anchor line: headings, pricing, footer and captions return to the same edges.
- Align groups on one axis. A paragraph starting 40px left of its headline's edge is a finding.
- Operate screens: one left edge and one right edge for the whole canvas; ONE gutter value on both axes.
- Optical alignment beats box alignment, but only after looking at the render: pull display type left `-0.04em to -0.06em` on round or diagonal capitals (O C A T W); nudge play/arrow icons toward their visual centroid.
- Numbers right-aligned and tabular in columns; text left-aligned. Never centre paragraphs over 3 lines. More than ~72% centred text on a page is a tell.
- Visual order = DOM order = focus order. Never reorder with `order` or absolute positioning in a way that breaks reading order.

## 7. Grouping (gestalt)

- Proximity is the primary grouping signal. Group by space before adding any container.
- Escalate separators only as distance demands: space, then a fill change, then a hairline, then a box. Removing a line means adding space.
- Similar look means similar function. Things that behave differently must look different on ≥2 channels (fill, border, size, weight), never colour or height alone.
- Keep cause and effect close: content starts where the menu ends; the title and primary action sit level with the thing they act on. On wide screens split menu / list / detail into 3 narrow columns rather than one wide one.
- A borderless region needs padding at least one step larger than the gaps inside it, or it does not read as a region.
- Squint test: blur the screen. You should still find the primary element, then the secondary, then the groups in order, as 2-3 masses.
- One focal point per screen. A second element competing at the same scale is louder, not bolder.
- Working memory holds ~4 chunks: group into chunks of ≤4; 5-7 is the edge.

## 8. Repeated components

- Cards in a row share top and bottom edges. Stretch a card only when it has content to fill; pin only the action or total to its foot.
- Pictures in a row: one aspect ratio (crop to it) or aligned bottoms. Use at most two ratios for ≥75% of a page's pictures.
- Button, input and select on one row share one height token (`min-height` in rem, `box-sizing: border-box`; borderless variants keep `border: 1px solid transparent`).
- Control heights: dense filters 28-32px, standard controls 32-40px (median 34), inputs 38-40px, phone inputs ≥44px.
- Joined controls (segmented, input + button): outer corners keep the radius, inner joints square, shared borders collapse to one.
- Long lists and grids get the same slots in the same place on every item: title, meta, status, action. Never let one item's missing field shift the others; keep the slot.
- Align the inner rows of sibling cards across the row with subgrid: parent `grid-template-rows` per slot, card `grid-row: span 4; grid-template-rows: subgrid`. A two-line title then pushes every card's meta down together.
- Wrapped rows (chips, stats) follow the alignment of their context (centred only where the context is centred).
- Give flex and grid children `min-width: 0` so long strings truncate instead of blowing out the track.
- Leave 30-40% slack for translation (German runs ~30% longer). Use logical properties (`margin-inline-start`, `padding-block`, `inset-inline-end`).

## 9. Cards versus grouping

- Use a card only when elevation or containment means something: a movable, selectable or independently actionable object. Otherwise group with space or a divider.
- Nested cards are always wrong. No panel inside a panel. Maximum two surface levels; a nested surface switches strategy (a card holds a fill, not another card).
- Persuade: no rows of identical icon-topped cards; no bento of rounded tiles as the feature section.
- Operate: identical cards are fine for peer metrics or peer objects, 3-6 across, equal widths, one gap, no orphan, edges aligned across rows, no icon on top. Prefer one container split by dividers for KPI rows.
- Past ~6 comparable items, use a table or list, not cards (exception: items carrying an image, chart, per-item controls or wrapping text).
- Separate a surface by ONE of: border (dense UI, tables, forms), elevation (floating things), or fill (belongs to a group). Never all three.
- The one legitimate pair: a 1px border plus a small shadow on a light-on-light card, border 1.5-2x darker than the shadow core.
- A 1px border plus a soft shadow ≥16px blur on every card in a row is the "ghost card" tell.
- Hairlines: banned as decoration on Persuade pages; allowed in Operate for structure at ~1.1-1.3:1 contrast. A ≥4px bar is a graphic element, not a hairline.

## 10. Radius system

Pick one grammar per product, write it down, and let it agree with the typeface (geometric with soft, grotesk with tight, serif with sharp or tight).

| Grammar | Controls | Cards / panels | Sheets, modals | Fits |
|---|---|---|---|---|
| Sharp | 0-2px | 0-2px | 0-4px | Dev, security, industrial, editorial, brutalist |
| Tight | 4-6px | 8-12px | 12px | Enterprise, finance, dense tools |
| Soft | 8-12px | 12-20px | 16-24px | SaaS, consumer apps |
| Pill | 9999px | 16-20px | 20-24px | Friendly consumer; buttons and tags only |

- One button radius for every button variant. One radius per role, never per instance.
- Nested radius: outer = inner + padding (8px button in 12px padding = 20px card). Inner never larger than outer.
- Cards top out at 20px radius; ≥32px on a card is a tell. Sheets and modals may go to 24px.
- One medium radius (9-16px) pasted on everything is the weak default. Choose, do not inherit.
- Pills only for tags, status and tabs, or as the whole control grammar. Never pill and 6px buttons on one screen.
- Images: square corners by default; if rounded, one radius everywhere (4px).
- A thick accent edge never shares an edge with a radius; clip an inner bar instead. Coloured side stripes >1px on cards are banned (tells.md).
- Wells and inputs inside cards: 2-8px.

## 11. Elevation and shadows

- Depth only to clarify state or hierarchy. Default depth is a surface ladder (lighter or darker tone steps, 2-6 lightness points apart), not shadows.
- Persuade: no shadow on resting elements. Operate: resting card ≤ level 2 (blur <8px, ≤8% black). Real shadows belong to things that float: menus, popovers, toasts, dialogs.
- Shadows always have an offset and a soft blur. A zero-offset coloured halo or glow is decoration and banned. Hard offset shadows (`4px 4px 0`) only in a genuinely neobrutalist world.
- Tint shadows toward the ground hue instead of pure black.
- Dark mode: raise surfaces by lightness steps, not shadows; add a `1px rgb(255 255 255 / .08)` edge; go one elevation step higher than light mode.
- Shadow grows with modality: card < dropdown < drawer < modal < command palette.

```css
:root {
  --shadow-ink: 220 15% 8%; /* hue-tinted near-black; swap H for the ground hue */
  --elev-0: none;
  --elev-1: 0 1px 2px hsl(var(--shadow-ink) / .06);                                       /* row hover */
  --elev-2: 0 1px 3px hsl(var(--shadow-ink) / .07), 0 1px 2px hsl(var(--shadow-ink) / .05);   /* resting card, Operate only */
  --elev-3: 0 4px 6px hsl(var(--shadow-ink) / .08), 0 2px 4px hsl(var(--shadow-ink) / .06);   /* dropdown, popover, toast */
  --elev-4: 0 10px 15px hsl(var(--shadow-ink) / .08), 0 4px 6px hsl(var(--shadow-ink) / .05); /* drawer, modal */
  --elev-5: 0 20px 25px hsl(var(--shadow-ink) / .08), 0 8px 10px hsl(var(--shadow-ink) / .04); /* command palette */
}
```

- Never `0 8px 16px rgb(0 0 0 / .4)`-style heavy shadows.
- Hover that changes only background needs a defined edge; on a borderless flat card, add the border or level 1 on hover instead.
- Glass / backdrop blur: never as card decoration. Only for a functional translucent bar over scrolling content, with an opaque fallback under `prefers-reduced-transparency: reduce`.

## 12. Stacking (z-index)

- Use semantic tokens. Never 999 or 9999. Document the scale next to the colour tokens.

```css
:root { --z-base: 0; --z-raised: 10; --z-dropdown: 100; --z-sticky: 200; --z-header: 300;
        --z-scrim: 390; --z-modal: 400; --z-toast: 500; --z-tooltip: 600; }
```

- Prefer the top layer over z-index: native `<dialog>` (`showModal()`) and the `popover` attribute escape every stacking context and every `overflow: hidden` ancestor.
- Otherwise overlays escape clipping ancestors via `position: fixed` or a portal to `body`.
- Tether popovers and menus to their trigger with CSS anchor positioning (`anchor-name` / `position-anchor`, `position-try-fallbacks: flip-block, flip-inline`) where supported, else Floating UI; never hand-computed `top/left` that ignores viewport collision.
- `transform`, `opacity < 1`, `filter`, `will-change` and `contain` create stacking contexts. Contain a component's internal z-order with `isolation: isolate` so it never leaks.
- Sticky table corner cell (sticky top + left) sits one step above both sticky header and sticky column.

## 13. Sticky, fixed and scroll areas

- `position: sticky` for section-scoped things (table headers, tab strips, in-page toolbars, a section's side rail). `position: fixed` only for global UI (header, bottom bar, one floating action).
- At most 1 fixed top + 1 fixed bottom + 1 floating action per screen.
- Header height: Operate 44-64px; Persuade ≤80px and ≤1/10 of the first screen. Solid ground plus level 1 shadow (or an Operate hairline) once content scrolls under it.
- Offset anchors and focus: `html { scroll-padding-top: calc(var(--header-h) + 1rem); }`. Sticky or fixed UI must never cover the focused control (WCAG 2.2 SC 2.4.11).
- Sticky silently fails inside an ancestor with `overflow: hidden | auto | scroll`. Use `overflow: clip` for clipping that keeps sticky and scroll timelines working.
- Default to page scroll. Inner scroll only for: long fixed sidebars, tables with sticky headers, chat and logs, code panes, master lists in master-detail. Otherwise paginate, load more, collapse, or route.
- One axis per scroll container: `overflow-y: auto; overflow-x: hidden`. Never bare `overflow: auto` on a layout region. No nested scroller fighting the page on the same axis.
- Inner scrollers and modals get `overscroll-behavior: contain` so scroll does not chain to the page.
- Reserve the scrollbar: `scrollbar-gutter: stable` on scrolling regions and on `html` when modals lock scroll, so content never jumps sideways.
- Show scrollability: a partially cut item at the edge (horizontal rows show 3 items plus a cut 4th; phone 75-80% card width), or a visible thin scrollbar. Never a hidden scroller with no cue.
- No scroll hijacking, wheel capture or auto-scroll. Scroll-to only to restore position or answer an action (first error, TOC link). Chat auto-scrolls only when the user is already at the bottom; otherwise show a "new messages" pill.
- Tab strip sticky on long pages; the panel scrolls, the strip does not.
- Never horizontal swipe on main content; horizontal rows use native `scroll-snap-type: x mandatory` with keyboard access.

## 14. Responsive paradigms

The layout paradigm follows the information architecture and the task, never a default grid. Different task kind, different paradigm; different content only, same paradigm.

| Paradigm | Use for |
|---|---|
| Feed | Temporal stream |
| Board | Items moving through stages |
| Table | Comparing fields across many items |
| Gallery | Visual items |
| Master-detail | List plus selected item; detail starts where the list ends |
| Coordinated views | Map + list, chart + table: 60-70% to the primary view, or 50/50 with a draggable, persisted divider; one view at a time on phone |
| Dashboard | Monitoring many metrics (not single-task users) |
| Canvas / Map / Timeline | Spatial or temporal content |
| Single focus / Wizard | One task at a time, 3+ dependent steps |
| Narrative long-scroll | Persuade pages only |

- Comparable pages use one template: title, filters, view toggle, primary action and collection in the same spots every time. Nav, primary action and feedback never move between comparable pages.
- Mobile-first CSS with `min-width` queries. Breakpoints come from the content: add one where the layout breaks, not where a device lives.
- Default breakpoints, written in em: `40em` (640), `48em` (768), `64em` (1024), `80em` (1280), `96em` (1536).

| Band | Width | Composition |
|---|---|---|
| Phone | <768px (design at 390) | Single column, vertical scroll only, bottom bar or menu sheet, no hover |
| Tablet | 768-1023px | Its own composition: two columns, master-detail, drawer nav in portrait, rail or sidebar in landscape |
| Desktop | ≥1024px | Persistent sidebar or top nav, multi-column, hover, shortcuts |
| Wide | ≥1280-1536px | More columns or a side panel, never wider text; frame cap applies |

- Stack by default. Reposition only within the same region (sidebar content becomes an accordion below main); never move a control into a different scope.
- Never change the information architecture or remove core functions between widths. Collapse secondary things; do not shrink them. Native window classes (Material compact/medium/expanded) live in apps.md.
- Print: every web page gets an `@media print` block that drops nav and fixed UI, prints link URLs and keeps figures and rows whole; recipe in decks.md (Print and PDF basics).
- Choose input affordances by capability, not width: `@media (hover: hover) and (pointer: fine)` gates hover; `@media (pointer: coarse)` enlarges padding (12x20px vs 8x16px).
- Verify by rendering and screenshotting at 1440 / 768 / 390, plus the real target viewport, plus a 320px reflow check, and look at the pictures (process.md).

## 15. Phone as its own composition

- Author the phone layout; never squeeze the desktop one.
- Re-author headline line breaks and re-crop pictures portrait per breakpoint (`<picture>` for art direction).
- Nothing horizontal-scrolls except deliberate snap rows.
- Primary actions in the thumb zone: full-width bottom button or bottom bar; secondary actions in a menu or sheet.
- Navigation: wordmark (18-24px tall, sized by height) + one action + "Menu" opening a full-screen sheet, or a 3-5 item bottom bar with icon + label. An app sidebar folds to a 48px top bar plus sheet; a sidebar over 30% of phone width fails.
- What collapses on phone: secondary actions into a menu or sheet; filters reachable but not persistent; bulk actions hidden; advanced settings on their own screen; toolbars move to the bottom.
- Operate on phone (titles, filters, KPIs, charts, tables, panes): apps.md (Phone and tablet adaptation).
- Bottom sheets replace centred dialogs; drawers go full width.
- Safe areas: `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`, then `padding-bottom: max(1rem, env(safe-area-inset-bottom))` on bottom bars and CTAs. Keep targets clear of notch, Dynamic Island and gesture bar. Never disable zoom.
- Test on a real iPhone and a cheap Android; DevTools misses touch, CPU and browser chrome.

## 16. Sizing units

| Unit | Use for |
|---|---|
| rem | Font sizes, line heights, text-adjacent padding, control heights, gaps between text blocks, spacing tokens |
| em | Media and container query breakpoints; padding that must scale with its own text (chips, badges, kbd) |
| ch | Text measure (`max-width: 65ch`) |
| px | Borders, hairlines, shadow offsets, small fixed icons, 1px optical corrections |
| % / fr / minmax() | Layout tracks and widths |
| clamp() | Fluid margins, section gaps, top-of-scale display type (always with a rem term) |
| vw | Only inside clamp(); never alone for type (breaks zoom) |
| svh | Full-screen hero or section heights (stable, no jump when browser bars collapse) |
| dvh | Fixed app shells and full-screen overlays that must track the visible viewport |
| cqi / cqb | Sizes inside a container-query component |

- Never `html { font-size: 62.5% }`. Never `height: 100vh` or `h-screen`. Write `min-height: 100vh; min-height: 100svh;` (fallback first).
- Inside iframes and auto-height previews (artifacts, prototype frames) viewport units resolve against the frame and can grow without end; size heroes there in rem or px.
- `min-height`, never `height`, on anything holding text. `max-width: 20rem`, not `width: 320px`. Sidebars `clamp(13rem, 22%, 18rem)`.
- Reserve media slots with `width`/`height` attributes or `aspect-ratio` so nothing shifts (CLS <0.1).
- Use container queries for any component that appears in more than one context (card in a sidebar vs main column); media queries for page-level layout only.

```css
.card-list { container-type: inline-size; }
@container (min-width: 36em) { .card { display: grid; grid-template-columns: 8rem 1fr; gap: var(--space-4); } }
```

- Everything survives 200% browser text size (WCAG 1.4.4) and reflows to one column at 320 CSS px without two-axis scrolling (WCAG 1.4.10).
- Script-measured containers need a definite size independent of their child; observe the box with `ResizeObserver`, not window resize.

## 17. Touch and hit targets

| Platform | Minimum | Recommended | Spacing |
|---|---|---|---|
| Web (WCAG 2.2 SC 2.5.8) | 24x24 CSS px | 44x44px | A smaller target passes only if a 24px circle centred on it overlaps no neighbour; aim for ≥8px |
| iOS | 44x44pt | 44x44pt | ≥8pt |
| Android | 48x48dp | 48x48dp | ≥8dp |

- The hit area may exceed the visible mark: extend with padding or a `::before { inset: -8px }` overlay. A 16px icon still gets a 44px target.
- Whole rows and cards are one target when they lead to one place; a second destination inside gets its own clearly separate target.
- Phone rows and list items ≥44px pitch; sidebar rows on desktop 32px hit / 34px pitch.
- Never rely on hover for function. Hover-only reveals are banned for primary actions.
- `touch-action: manipulation` on tappable controls stops double-tap zoom from swallowing fast taps.
- Drag surfaces declare `touch-action` so a swipe along the page's scroll axis still scrolls the page; every drag has a tap or keyboard alternative.

## 18. Fixed-canvas and game frames

- Games, decks and fixed-art pieces use a logical canvas (e.g. 1920x1080, or 390x844 portrait) scaled with `transform: scale()` into a letterboxed stage filled with the ground colour. Controls sit outside the scaled element. Deck specifics in decks.md.
- Keep critical UI inside the central ~90% (title-safe) so any aspect ratio crops nothing important.
- HUD anchors to corners inside safe-area insets: status top, actions bottom in the thumb zone. Nothing covers the play focus or the thing being read.
- Canvas DPR capped at 2 (`canvas.width = cssW * dpr`). Experience-mode detail in experience.md.

## 19. Layout checks before claiming done

- Equal outer margins at every width; nav, content and footer on one inset.
- 2-3 text edges; grid sum closes; no orphan tiles.
- Between-section gap > every within-section gap; space above headings ≥2x below.
- No holes (section 5); no stretched card with a blank band; rows share edges.
- One radius grammar, one elevation scale, one gutter, z-index tokens only.
- No nested cards; one surface-separation strategy per level.
- Nothing fixed covers focus or content; anchors land below the header.
- No horizontal overflow at 320, 360, 390, 430, 768, 1024, 1440 and phone landscape; phone is a recomposition, not a shrink.
- Targets ≥24px (web) and ≥44px on touch; safe areas respected.
- Text survives 200% zoom and translation slack without clipping.
