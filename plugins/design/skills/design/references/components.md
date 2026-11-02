# Components and UX

Use when building or reviewing any interactive surface: navigation, forms, buttons, overlays, feedback, notifications, loading, empty states, tables, search, onboarding, accessibility, icons and illustration. Applies in every mode; Operate leans on it hardest.

## 1. Information architecture and naming
- Name things in the user's words ("job", not `task_assignment`). No internal shorthand, codenames, IDs or process names in customer UI.
- Be specific: "Workspace settings", not "Settings". One name per thing on every surface (nav, breadcrumb, title, dialog, error).
- Name actions by effect: "Archive", not "Hide"; "Transfer ownership", not "Change user". Keep a glossary; cap coined terms at ~10 per product.
- Mirror the data model: each major entity gets a list view and a detail view. Show parent/child ("3 tasks in this project"). Show state changes as labels, verb buttons ("Mark as paid") and history.
- Group by user goal, not backend ("Developer → Webhooks", not "Settings → Integrations → Webhooks").
- One destination = one place and one label. One grouping principle per level (task OR audience OR object). Audit: list every link, sort by target; a repeated target or label is a finding.
- Adding a nav item has a cost: say what it replaces or extends.
- Low-use features: surface, remove, or hide behind an opener (accordion for inline detail, popover/drawer for a short side task, modal only for a must-interrupt sub-task).
- Cognitive load: working memory holds ~4 items (5-7 is the edge, 8+ overloaded). ≤4 visible options per decision, one decision at a time. 1 primary + 1-2 secondary actions visible, the rest in a menu. Top-level nav ≤5 items; groups ~7; doc sidebars ≤4 siblings per level. Never make users carry information between screens. The 8-point cognitive-load check: process.md §10.

## 2. Navigation and wayfinding
- Every screen answers: where am I, where can I go, what is here, how do I get out.
- Logo links home. Global header identical at every depth; nav placement never changes by page type.
- Depth ≤3 levels; past that add grouping and search, not levels. Global search mandatory beyond 3 levels.
- 1-2 levels deep: "← Back to [Parent]". 3+: breadcrumbs (current page plain text, `aria-current="page"`; on mobile collapse to `← Parent`). Name return links by destination; "Back" is history, up is hierarchy.
- Active item: background or indicator plus weight, never colour alone. Destructive items (sign out, delete account) spatially separated.
- Unavailable destination: show it with a reason; don't silently hide it. Role-gated items may be removed; sign-in-gated items stay visible with a quiet mark.
- Badges sparse, on actionable queues only; clear on visit.
- Deep-link every key screen; update the URL on view, tab, filter and step change. Back restores scroll, filters and input. Never reset the stack or jump home.
- Full-screen mobile overlays and sheets push a history entry so system Back closes them; never block iOS edge-swipe back or Android predictive Back.
- Patterns by surface: bottom nav 3-5 items, icon + label, top level only (mobile). Sidebar ≥1024px. Drawer = secondary nav, never primary actions. Never mix tabs + sidebar + bottom nav at one level.
- Phone (<768px): sidebar becomes a drawer with the same items and order; scrim, scroll lock, closes on navigation.
- On route change move focus to `<main>` or the `<h1>` and update `document.title`.
- Modals never carry primary navigation flows.
- Shell and estate rules (app launcher, rail collapse, status bar): see apps.md.

### Tabs
- For 2-7 peer views of one context. >7 → sidebar. Sequential → stepper. Different header per view → separate pages. Never nest tabs.
- Types: underline (page level), contained (prominent), pill/segmented (view toggles like List/Grid/Map). Vertical tabs (5+ beside content): 200-240px, active = neutral fill + weight, like the sidebar active item (apps.md); never a coloured side stripe.
- Strip 40-48px tall, sticky on long pages (the panel scrolls, the strip doesn't); active indicator 2-3px bar under the selected tab only.
- Overflow: horizontal scroll with an edge fade, or "More ▾" relabelled with the active hidden tab; native `<select>` on narrow phones. Never wrap to 2 lines.
- Never disable the active tab; explain unavailability inside the panel.
- ARIA: `role=tablist/tab/tabpanel`, `aria-selected`, `aria-controls`, `hidden` on inactive panels. Roving tabindex (active 0, others -1); ←/→ (↑/↓ vertical), Home/End. Use manual activation (Enter) when switching fetches data.
- Persist in `?tab=` for deep links and back/forward, or localStorage for a preference; never sessionStorage.

## 3. Nielsen heuristics as pass/fail checks
| # | Heuristic | Check |
|---|---|---|
| 1 | System status | Every action shows a visible outcome within 100ms (ack) and 1s (result or progress). |
| 2 | Real-world match | No IDs, codes, jargon or process names; units and formats as users say them. |
| 3 | Control and freedom | Undo, visible close/cancel, Back in flows, Esc on overlays. |
| 4 | Consistency | Same label and behaviour everywhere; platform conventions; standard patterns keep standard names. |
| 5 | Error prevention | Constraints, sensible defaults, masks, consequences stated before acting, undo or confirm on irreversible acts. |
| 6 | Recognition over recall | Options in context, known data pre-filled, icons labelled, nav visible. |
| 7 | Flexibility | Shortcuts, saved views, bulk actions, guided and direct paths. |
| 8 | Minimalism | Every element earns its place; empty, loading and error states get equal design. |
| 9 | Error recovery | What happened + why + what next, in plain words, next to the problem. |
| 10 | Help | Self-explanatory UI > inline hint > tooltip > docs; help placed consistently. |
- Scoring bands, severity levels and personas: process.md §10.

## 4. Buttons and the 8 interaction states
Every interactive element ships all of these, designed, not inherited:

| State | Rule |
|---|---|
| Default | Role readable before interaction (squint test): button = fill or firm border + pointer; badge = muted, smaller, inert; input = empty interior + text cursor. Differ on ≥2 channels, never colour or height alone. |
| Hover | Inside `@media (hover: hover) and (pointer: fine)`. Background ΔL ∓0.06 in OKLCH (colour.md); on dark, lighten. Never lowers text contrast, never changes weight. |
| Focus | `:focus-visible` ring (section 5). Never relies on hover styling. |
| Active/pressed | ΔL ∓0.12 and/or `transform: scale(0.97)` (0.95-0.98), 100-160ms ease-out. Never changes layout bounds. |
| Disabled | Neutral grey fill (never a brand tint), same shape and size, `cursor: not-allowed`, still legible; say why (helper text or tooltip on a focusable wrapper). Prefer `aria-disabled="true"` when users must discover the reason. |
| Loading | Spinner replaces or precedes the label, width locked (no shift), repeat clicks ignored via `aria-disabled="true"` (not `disabled`, which drops focus to `<body>`), no double submit; cursor unchanged (never `wait`). Return to rest on finish. |
| Error | Inline message beside the control naming the fix; control keeps its value. |
| Success | Brief confirmation in place (check, "Saved"), auto-clears 2-3s; a one-way action (Send, Approve) replaces its button with the result in the same slot. |
- Plus selected and read-only where relevant. Read-only looks different from disabled (plain text or no field chrome, still selectable and focusable).
- Transitions: hover colour 150-200ms, press 100-160ms (motion.md §3), named properties only (`transition: background-color 180ms, transform 140ms var(--ease-out)`), never `transition: all`. Feedback within 100ms of input.
- Hierarchy: one primary (filled) per view or section, one per step in a flow. Secondary = outline/tonal; tertiary = text button or link. Size steps perceptible.
- Primary placement: bottom-right of dialogs and forms (Cancel to its left), top-right of a page header.
- Labels: verb + object, 1-3 words ("Save changes", "Delete project"). Never "OK", "Yes", "Submit", "Click here". Copy rules: copy.md.
- One radius for every button variant. Button, input and select on one row share one `min-height` token (desktop 32-40px, default 34, inputs 38-40; touch ≥44px; layout.md §8); borderless variants keep `border: 1px solid transparent`.
- Variants change colour only; one shared class owns box, padding and states. 3 variants cover ~90%. One interaction language product-wide: one hover response, one press, one focus ring, one selected treatment.
- `cursor: pointer` on `button, a, [role=button], label[for], summary`. Badges, tags and status chips are inert: no hover, no pointer.
- Status colours never fill a primary CTA. Destructive primary uses the danger token only in confirm contexts.
- Never hover-only reveals for primary actions; touch has no hover. Add `touch-action: manipulation`.
- `@media (pointer: coarse)`: bigger padding (e.g. 12×20 vs 8×16) and ≥44px targets.
- Icon-only buttons: `aria-label`, a tooltip, and an unambiguous standard glyph. Toggle buttons expose `aria-pressed`.

## 5. Focus
```css
:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }
```
- Ring ≥2px, ≥3:1 against both the component and its background; use outline (survives `forced-colors`), not box-shadow alone. On mixed grounds, a 2-colour ring (outline + inner box-shadow of the ground colour).
- Never `outline: none` without a replacement.
- Tab order = reading order = visual order = DOM order; never reorder with CSS `order`, `row-reverse` or absolute positioning in ways that break it. No positive `tabindex`. `tabindex="-1"` only for programmatic focus targets (headings, panels).
- Sticky headers, cookie bars, chat widgets and toasts never cover the focused element (WCAG 2.4.11; `scroll-padding-top` recipe in layout.md).
- Focus moves only in response to the user: into an opened overlay, back to its trigger on close, to the error summary after a failed submit, to the main heading after navigation. Never on blur, never on page load except to an error summary.
- When the focused item is deleted, move focus to its neighbour or the list heading, never to `<body>`.
- Closed drawers, collapsed panels and off-screen slides are `hidden` or `inert`, never just translated or `opacity: 0`, so Tab can't land inside them.
- Skip link is the first focusable element: "Skip to main content", visible on focus.

## 6. Links
- `<a href>` navigates; `<button>` acts. Never a click handler on a div, never `href="#"` for an action.
- Link text makes sense out of context: "View invoice 1042", not "Click here" / "Read more". Several identical "Edit" links need unique accessible names (visually hidden suffix).
- Inline links in body text are underlined (`text-underline-offset: .18em; text-decoration-thickness: .07em`); colour alone fails unless 3:1 against surrounding text plus a non-colour cue on hover/focus.
- Nav and button-like links may drop the underline when position makes the role obvious.
- Visited state on content sites (hue shift, less saturation); skip in apps.
- New tab only when leaving would lose work; mark it ("opens in new tab" icon + SR text). `target="_blank"` implies `noopener` in current browsers; add `rel="noopener"` only for legacy support.
- File links name type and size ("Annual report (PDF, 2.4 MB)").

## 7. Forms
- Visible label on every field, above the input (14px/500, 8-10px gap), `<label for>`. Never placeholder-as-label, avoid floating labels.
- Placeholder = optional realistic example in muted ink at ≥4.5:1 (`+44 7700 900123`). Helper text below the field, persistent, one sentence, not repeating the label; put format rules and limits there before the user types.
- Anatomy: label (+ "Optional" marker) → input → helper → error. Wire `aria-describedby="hint-id error-id"`, `aria-invalid="true"` on error.
- Mark the minority: if most fields are required, mark optional ones with the word "Optional"; else mark required with text or asterisk + legend. Never colour alone.
- Ask only what is needed now. Never ask for the same data twice in one process (WCAG 3.3.7); pre-fill what you know.
- One column. Group related fields with `<fieldset>/<legend>` (address, payment, radio and checkbox groups). Field width hints the expected length (postcode short, street long).
- Input types: `email, tel, url, number` (only for quantities, never IDs, cards or phones; use `type="text" inputmode="numeric"`, or `decimal` for amounts), `password, search, date`. Set `enterkeyhint`. Emails, usernames and codes: `autocapitalize="none" spellcheck="false"`.
- `autocomplete` on everything it fits: `name, given-name, family-name, email, tel, organization, street-address, address-line1, address-level2, postal-code, country, bday, cc-number, cc-exp, cc-csc, one-time-code, username, current-password, new-password`.
- Controls: toggle for an instant binary setting; checkbox for a binary that applies on save; radios for 2-5 visible options; select for 6-15; combobox with search beyond ~15 or for free entry; slider + number field for ranges. Unit suffix always shown.
- Switches: native checkbox or `role="switch"` + `aria-checked`, label tied to it, hit area ≥24px even when the track is smaller. Theme native checkboxes, radios and ranges with `accent-color`, don't rebuild them.
- Known dates (birthday, expiry): separate day/month/year text fields or one text field with a format hint, never a calendar picker. Scheduling: a picker plus typed entry.
- Length limits: show a counter ("212 / 280") from ~80% of the limit, announced politely only near it; never silently truncate pasted text.
- Accept any common format and normalise (spaces in card numbers, dashes in phones) instead of rejecting.
- Auth (WCAG 3.3.8): allow paste and password managers, show/hide password toggle, support passkeys/OAuth or magic links, `one-time-code` autofill; no CAPTCHAs or puzzles without an alternative.
- Inputs ≥44px tall on touch; input text ≥16px (iOS zooms below that). Inputs look like inputs: visible boundary ≥3:1 against the surface.
- Long forms autosave drafts; confirm before dismissing a sheet or dialog with unsaved changes. Wizard for 3+ dependent steps (section 15).

### Validation and errors
- Validate on blur by default. Real-time only for complex formats (password strength, IBAN, username availability), debounced 300-500ms, and only after the first blur. Never flag a field as wrong while the user is still typing it the first time.
- Clear an error as soon as the input becomes valid.
- Submit button: keep it enabled on anything longer than ~3 fields; validate on submit. Disable-until-valid only on very short forms, and then show what is missing.
- After a failed submit with 2+ errors: an error summary at the top with a heading, moved into focus (`tabindex="-1"`; don't also give it `role="alert"`, which double-announces), listing each error as a link to its field. One error: focus that field. Prefix the page `<title>` with "Error: ".
- Error text below the field, with an icon + text (never colour alone), danger colour ≥4.5:1, announced via `aria-describedby`.
- Error copy = cause + fix: "Enter a VAT number like FI12345678", never "Invalid input". Never blame; never clear what the user typed. Wording: copy.md.
- Always validate on the server too; show server errors inline on the same fields, with all input preserved. Submit button follows the Loading and Success states (section 4).

## 8. Overlays: tooltips, popovers, menus, drawers, modals
Pick the lightest that works: inline → tooltip → popover → menu → bottom sheet (mobile) → drawer → modal → full screen. Non-blocking if the user can keep working; modal only when the app must wait for a decision or protected focus.

| Overlay | Size | Rules |
|---|---|---|
| Tooltip | 1-2 lines | Supplementary only, no links/buttons inside. Show after 300-400ms hover, instantly on focus and for neighbours once one is open. Prefer above, auto-flip at viewport edges. Hoverable, dismissable with Esc, persistent while hovered (WCAG 1.4.13). `role=tooltip` + `aria-describedby`. Never the only place essential info lives (touch can't hover). |
| Popover | 280-360px max | Light interactive content. Focus moves in on open, returns to trigger on close. `aria-expanded`, `aria-controls`. Bigger content → drawer. |
| Menu / dropdown | ≥ trigger width, ≤280px | Trigger `aria-haspopup="menu"` + `aria-expanded`. ↑/↓, Home/End, Enter, Esc (focus back to trigger), type-ahead; Tab closes and moves on. Add search beyond 8-10 items. Action menus (`role=menu`) are separate from selects (persist a value). Destructive item last, separated. |
| Bottom sheet | mobile | Replaces centred dialogs on phones. Drag handle + title; dismiss by swipe down, scrim tap, Esc, close button. Respect safe-area insets. |
| Drawer | 320-480px desktop, full width mobile | Right = detail/edit/filters; left = mobile nav. `role=dialog aria-modal="true"` when it blocks. Scrim click doesn't dismiss if it holds unsaved input. |
| Modal | 360 / 480 / 640 / full | Header (title + ✕) and footer fixed, body scrolls; never taller than `100dvh` minus margins. Footer right-aligned: Cancel then primary. Below ~600px wide, go full screen or a bottom sheet. |
- Prefer native `<dialog>` with `showModal()` (top layer, Esc via the `cancel` event, inert background) and the `popover` attribute + `popovertarget` for popovers/menus. Overlays escape `overflow: hidden` via top layer, portal or `position: fixed`. Position anchored overlays with CSS anchor positioning or Floating UI: flip and shift to stay in the viewport.
- Modal ARIA: `aria-modal="true"`, `aria-labelledby` (title), `aria-describedby` (body). Background `inert`. Lock page scroll without layout jump (`scrollbar-gutter: stable`).
- Focus on open: first field for forms; the least destructive button for confirms; the title (`tabindex="-1"`) when the body is long content to read. Trap Tab/Shift+Tab. Return focus to the trigger (or a logical neighbour if the trigger is gone).
- Dismissal: non-destructive → Esc, scrim click, ✕, Cancel. Destructive or unsaved-data → ✕ or Cancel only.
- Never stack modals (a menu or popover inside a modal is fine). No modal on page load, no newsletter interrupts in apps.
- Scrim neutral `rgba(0,0,0,.4-.5)` or a tinted dark; measure content contrast against the real backdrop. No backdrop blur on scrims: blur is reserved for a functional translucent bar over scrolling content, with a `prefers-reduced-transparency` solid fallback.
- Popovers grow from their trigger (transform-origin at the anchor); modals stay centred. Enter 200-300ms, exit ~60-70% of that. Motion detail: motion.md.
- One shell for the family: same surface, radius, elevation scale (grows with modality), footer order.
- Lightbox: opens at the clicked index with focus on its close button, back to the thumbnail on exit; ←/→ page, Esc closes. Input by `pointer`, not width: fine = click to zoom at point + pan; coarse = pinch, double-tap, drag. Visible +/− (disabled at 1× and max), two zoom tiers (2×, 4×), movement >~5px is a pan not a click, zoom resets on image change. Close top-right, pager bottom-centre, zoom bottom-right. Announce scale ("Zoom in, currently 2×").
- Never design custom UI around `beforeunload`; gate unsaved work with an in-app prompt.

## 9. Destructive actions, undo and confirmation
- Prefer undo to confirm for reversible or low-stakes actions: act immediately, show a toast with Undo for ~8-10s, commit after.
- Confirm only for: permanent delete, bulk destroy, ownership/billing/permission changes, account-level actions, irreversible send/publish.
- Confirm dialog: title names action + object ("Delete project Website Redesign?"); body states consequences and "This can't be undone"; button repeats the verb + object ("Delete project") in danger colour; Cancel on its left. Default focus on Cancel; Enter must not destroy.
- Highest risk (delete a workspace, wipe data): require typing the name.
- Repeat scope in the dialog (tenant/account name, "240 subscribers") so the user sees what they hit.
- Never confirm save, navigation or reversible archive. Unsaved changes on navigate-away: in-app banner or dialog with "Discard changes" / "Keep editing".
- Prefer recoverable delete (Trash with restore, and say for how long: "Deleted items stay in Trash for 30 days") over hard delete.
- A failed destructive action says nothing was lost.

## 10. Feedback: toasts, banners, inline, errors
| Scope | Pattern |
|---|---|
| Field problem | Inline text under the field |
| Transient result of a user action | Toast |
| Persistent condition affecting a region | Banner at the top of that region |
| Blocking decision | Modal |
| Section failed to load | Inline error inside that section |
| Whole app unusable | Full-page error |
- Toast: bottom-centre (mobile) or bottom-right (desktop), never covering primary actions or focus. Icon + one sentence + ≤1 action (Undo, Retry, View) + close. Success auto-dismisses at ~5s, longer (~8-10s) with an action; pause the timer on hover, focus and hidden tab. Errors persist until dismissed. One visible at a time, the rest queued; never top-centre.
- Toasts never steal focus; announce via a persistent `aria-live="polite"` region (`role="alert"` only for errors). The action and close are keyboard-reachable. Never put the only route to a result in a toast.
- Banners: one per region; dismissible unless blocking. Semantic colours: red error, amber warning, blue info, green success/resolved; always icon + text.
- Every error has a way forward: Retry (spinner while retrying; after 3 failures offer "Contact support"), Undo, a fallback link, or a fix instruction.
- Graceful degradation: only the failed block shows an error, with when the data was last good + Retry; the rest of the screen works.
- Optimistic UI for likes, toggles, rename, reorder, delete: update instantly, retry silently, roll back with a message only if the retry fails.
- Autosave every 30-60s or on blur; show "Saved" / "Saving…" / "Couldn't save, stored locally [Retry]". On return with a local draft: "[Restore] [Discard]".
- Session expiry: warn ahead with "Stay signed in" and ≥20s to respond (WCAG 2.2.1; ~2 min is kinder), then sign in → return to the same place with input intact. 401 → sign in; 403 → explain and who to ask; 404 → search and a link up; 409 / concurrent edit → show both versions and let the user choose, never silently overwrite; 429 → when to retry; 5xx and timeout → Retry with input kept; offline → banner + queue actions.
- Error copy: what happened + why (if known) + what next. No codes, stack traces, "Something went wrong" or "Error 500" as the message. Never fake a cause the system can't know.
- Notification centre: bell → list → settings. Unread state, mark all read, clear all, mute; 1-3 categories each Off / Minimal / All.
- Push, email and OS notifications: opt-in per channel after a pre-prompt in context (never on first launch); each one actionable and deep-linked to the exact object; batch low-urgency items into a digest; respect quiet hours and the OS focus mode; one channel per event (no push + email + in-app for the same thing); dismissing in one place clears it everywhere. Wording: copy.md §13.
- Native: iOS interruption levels (passive, active, time-sensitive only for real deadlines) and Android channels per category so users mute by type; grouped by thread; never marketing in a transactional channel.
- Live counters read as complete phrases in one atomic region ("3 items in cart").

## 11. Loading and perceived performance
| Expected wait | Show |
|---|---|
| <100ms | Nothing; respond instantly |
| 100ms-1s | Pressed state; inline spinner in the triggering control (16-24px) once past ~300ms |
| 1-3s, content area | Skeleton at the final layout |
| 3-10s | Skeleton + status text naming the real operation |
| >10s | Determinate progress + Cancel; >30s users assume it's stuck; no spinner runs past 60s (escalate to progress or an error) |
| Irreducible job (export, render) | Run in background, release the user, notify with the result somewhere findable |
- Skeletons: flat blocks at the real final sizes and positions (round avatar, 2 text bars of different widths), no shimmer, no pulse. Content replaces them with a ≤150-200ms fade, zero layout shift. Charts load as a chart-shaped skeleton, never an empty axis frame.
- One container skeleton, not many spinners. Never a blank screen, never a global blocking spinner over content that could render.
- Delay showing any indicator ~300ms so fast responses don't flash; once shown, keep it ≥500ms to avoid flicker. Refreshing on-screen data keeps the old values visible and updates the freshness stamp.
- Load in value order; fetch only the current view (tabs and drawers load on open); prefetch the obvious next step on hover/intent.
- Never fake progress; a progress bar moves with real work. Name the step ("Uploading 3 of 12 files").
- Stream AI output token by token; label AI content; offer stop and regenerate.
- Reserve space for anything that loads late (images with width/height, ad slots, embeds) so nothing jumps. Performance budgets: layout.md and motion.md.
- Announce completion of long operations via `role="status"`; set `aria-busy="true"` on the region while loading.

## 12. Empty, zero, first-run, error, stale states
| State | Design |
|---|---|
| First use | What will appear here, why it matters, the first action as a button where the data will be; optional template or sample data. Keep the frame and header. |
| User cleared (inbox zero) | Short confirmation of done; no fake celebration on routine clears. |
| No results (search) | Echo the query; suggest fixes (spelling, broader terms); link to create or browse. |
| Filtered to nothing | "No results for these filters" + "Clear filters"; show which filters are active. |
| No permission | Say what it is and who can grant access; never a bare 403. |
| Error | Inside the failing block: what failed, when data was last good, Retry. Never collapsed into empty. |
| Stale / offline | Freshness stamp ("Updated 4 min ago"), refresh control, offline banner; keep showing last good data. |
| Partial | Show what loaded; mark what is missing with a reason. |
- Zero is data: print `0`, not a dash. Missing is a muted hyphen (`-`) with SR text "No value", never "N/A"; use "Pending" / "Not measured" when the reason matters.
- Empty charts: no illustration + "No data yet" floating in an empty axis frame; one sentence spanning the block and the next action.
- Design every state with real-length content: 100+ character names, empty and 1-character values, 0 / 1 / 1000+ items, 50+ options, numbers in the billions, 3-line title, emoji, RTL, CJK, German (+30% length).

## 13. Data display and selection
- Pick the paradigm from the task: table (compare fields), list (scan items), cards/gallery (visual items or per-item controls), board (stages), master-detail (list + selected), timeline, map. More than ~6 text items → table, not cards. Data both visual and detailed: grid/list/table toggle top-right beside sort and filter, icon buttons with tooltips, choice persisted; one view on phones.
- Tables: sticky header, sticky first column when wide; numbers right-aligned with `tabular-nums`, fixed decimals and thousand separators; identity column never truncated first; row actions in the rightmost column, visible on focus as well as hover (never hover-only on touch). Row heights, density and chart rules: apps.md.
- Sort: click asc → desc → clear; arrow on the active column only; `aria-sort` on the header; non-sortable headers get no hover.
- Filters: active filters as removable chips + "Clear all"; visible-of-total count ("24 of 1,284"); filter button shows a count badge. Server filters submit; client filters apply live.
- Pagination: "1-50 of 1,284" with page size; overviews use "View all (n)" instead. Infinite scroll only for feeds, never where users need the footer or to return to a position; keep position on Back.
- Virtualise long lists (50+ heavy rows, 1000+ simple rows); `content-visibility: auto` for long static ones. Virtualised lists keep `aria-setsize` / `aria-posinset` (or `aria-rowcount` / `aria-rowindex`) so screen readers know the true size.
- Selection: the whole row is the hit target; selected = subtle accent tint (opaque token, colour.md) + checkbox; never a coloured side stripe. A row that drives a detail pane takes the neutral `--active` fill instead (apps.md). Space toggles, Shift+click extends a range, Ctrl/Cmd+click toggles. Header checkbox selects the page, then offer "Select all 1,284 results".
- Bulk toolbar appears while a selection exists: "[3 selected] [Archive] [Export] [Delete] [Clear]"; only applicable actions; destructive confirm names the count. Feedback: <10 items inline, 10-100 toast with count, 100+ progress then summary.
- Drag to reorder or resize always has a single-pointer and keyboard alternative (move up/down buttons, menu, "Move to…") (WCAG 2.5.7). Drag starts after ~5-10px of movement; `touch-action` on the drag surface; announce moves ("Moved to position 3 of 8"). Interrupted-gesture cleanup: motion.md.
- Numbers carry a reference ("€48,900, +12% vs last month"). Locale-aware dates, numbers, currency via `Intl`. Relative time in feeds with absolute time on hover/title.
- Truncate identifiers with ellipsis and full text in `title`/tooltip only when actually truncated; never truncate prices, errors, legal text or instructions. `min-width: 0` on flex/grid children.
- Coordinated views (map + list, chart + table): one shared selection; hover = faint transient highlight, click = persistent selection, Esc clears; selecting in one scrolls the other into view.

## 14. Search
- Search box visible (not icon-only) when search is a primary task; `type="search"`, `role="search"` landmark, `/` or Ctrl/Cmd+K shortcut shown as a hint.
- Suggestions from the first character, debounced ~150-300ms; group by type with icon/thumbnail and the matched part bolded; recent searches when empty.
- Combobox pattern: `role="combobox"` + `aria-expanded` + `aria-controls` → `role="listbox"`; ↑/↓ moves `aria-activedescendant`, Enter selects, Esc clears/closes. Announce result count via a polite live region.
- "See all results for '…'" leads to a full results page with filters, sort and the query in the URL.
- Results page: echo the query and count; tolerate typos, plurals and synonyms; highlight matches; keep the query in the box.
- No results: say so, suggest corrections or broader terms, offer popular items; never a blank page.
- Command palette for power users in Operate tools: fuzzy match, actions + navigation, shortcuts listed beside items, no open/close animation.

## 15. Flows and onboarding
- Wizard for 3+ sequential, dependent steps: "Step 2 of 4" with titles in user language; Back keeps later progress; Continue validates only the current step; save and exit with an autosaved draft; optional steps marked and skippable; final review step before commit; deep link to a step opens that step.
- Flows may hide nav chrome but keep the brand header and an exit. After completion, land somewhere meaningful with the next step.
- Checkout: collect only what's needed now, guest option, persistent order summary, review step (items, delivery, total), confirmation with what happens next.
- Onboarding goal is time to value: get the user to the first real result, not through a tour.
- Teach in context at the moment of need; introduce 1-3 core concepts only. Empty states carry most onboarding.
- Tours (if any): 3-7 steps, skippable, replayable from Help, Back available, operating on real UI with sample data. Never a forced linear tour.
- Discovery cues (badge, dot) end on first use or after ~3 showings. Show onboarding once; respect dismissals across devices.
- Ask for permissions (notifications, location, camera) in context when the feature needs them, with a pre-prompt explaining the benefit; never on first launch.
- Sample data clearly labelled and removable in one action.

## 16. Accessibility: WCAG 2.2 AA concrete checks
| SC | Check |
|---|---|
| 1.1.1 | Informative images: alt describes the information. Functional: alt names the action. Decorative: `alt=""`. Complex (charts): short alt + text summary or table. |
| 1.2.2 / 1.2.4 / 1.2.5 | Captions on prerecorded and live video; audio description (or a text alternative) where visuals carry meaning; transcripts for audio. |
| 1.3.1 | Structure in markup: headings, lists, tables with `<th scope>`, labels tied to fields, fieldsets for groups. |
| 1.3.3 / 1.3.4 | Instructions never rely on shape, position or sound alone ("the round button on the right"); never lock orientation. |
| 1.3.5 | `autocomplete` tokens on personal-data fields. |
| 1.4.1 | Colour never the only signal: add icon, text, pattern or weight. |
| 1.4.3 | Text ≥4.5:1; large text (≥24px, or ≥18.66px bold) ≥3:1. Includes placeholders and text on images. |
| 1.4.4 / 1.4.10 | Works at 200% text and reflows to 320 CSS px width without horizontal scroll or clipping. |
| 1.4.11 | UI component boundaries, icons, focus rings, chart marks ≥3:1 against adjacent colours. |
| 1.4.12 | Survives line-height 1.5, paragraph spacing 2×, letter-spacing .12em, word-spacing .16em without loss. |
| 1.4.13 | Hover/focus content: dismissable (Esc), hoverable, persistent. |
| 2.1.1 / 2.1.2 | Everything works by keyboard; no traps. |
| 2.1.4 | Single-character shortcuts (`/`, `j`, `k`) can be turned off or remapped, or work only while the component has focus. |
| 2.2.1 | Time limits can be turned off, adjusted or extended (warn with ≥20s to respond). Action toasts pause while hovered or focused, and their action is reachable elsewhere too. |
| 2.2.2 | Anything moving >5s or auto-updating can be paused; carousels have pause and stop on hover/focus. |
| 2.3.1 | Nothing flashes >3 times per second. |
| 2.4.1 / 2.4.2 | Skip link; unique descriptive `<title>` per page/view. |
| 2.4.3 / 2.4.7 | Logical focus order; visible focus indicator. |
| 2.4.4 / 2.4.6 | Link purpose clear; headings and labels descriptive. |
| 2.4.5 | Two ways to reach each page (nav plus search, sitemap or related links). |
| 2.4.11 | Focused element never fully hidden by sticky UI. |
| 2.5.1 / 2.5.2 | Pinch, swipe and path gestures have a single-tap alternative; activate on pointer up, so sliding off cancels (games may act on down: experience.md). |
| 2.5.3 | Accessible name contains the visible label text. |
| 2.5.7 | Every drag has a single-pointer alternative. |
| 2.5.8 | Targets ≥24×24 CSS px (or spaced so a 24px circle doesn't overlap neighbours). Aim for 44×44 (iOS 44pt, Android 48dp). |
| 3.1.1 | `lang` on `<html>`; `lang` on inline foreign text. |
| 3.2.1 / 3.2.2 | Focus or input never triggers navigation or submission by itself. |
| 3.2.3 / 3.2.4 / 3.2.6 | Nav, component names and help location consistent across pages. |
| 3.3.1-3.3.3 | Errors identified in text, labels/instructions present, fix suggested. |
| 3.3.4 | Legal, financial, data-deleting submissions are reversible, checked or confirmed. |
| 3.3.7 | No re-entering data already given in the same process. |
| 3.3.8 | No cognitive test to sign in; paste and password managers allowed. |
| 4.1.2 | Custom controls expose name, role, state and value. |
| 4.1.3 | Status messages announced via live regions without moving focus. |
- Disabled controls are exempt from contrast, but must still be perceivable as disabled.
- Respect `prefers-reduced-motion` (drop travel, keep opacity/colour feedback), `prefers-contrast: more` (solid surfaces, stronger borders), `prefers-reduced-transparency`, `forced-colors: active` (use system colours, keep outlines), and OS text size.
- Test: keyboard-only pass, a screen reader pass (VoiceOver + Safari, NVDA + Firefox/Chrome), 200% zoom, 320px width, Windows high-contrast. Automated scan (axe/Lighthouse a11y 100) is a floor, not proof.

### Screen readers and ARIA
- First rule: native element beats ARIA. Wrong ARIA is worse than none.
- Every control has an accessible name: visible `<label>`, `aria-labelledby`, or `aria-label` for icon-only. Name matches the visible text.
- States: `aria-expanded` (disclosures, menus), `aria-pressed` (toggle buttons), `aria-selected` (tabs, options), `aria-checked` (custom checkboxes/switches), `aria-current="page|step"` (nav, steppers), `aria-invalid` + `aria-describedby` (fields), `aria-busy` (loading regions), `aria-sort` (tables).
- Live regions: `role="status"` / `aria-live="polite"` for updates; `role="alert"` for errors needing immediate attention. The region exists in the DOM before content is injected. Never announce every keystroke.
- Hide decoration with `aria-hidden="true"` (icons beside text, duplicate images). Never `aria-hidden` on focusable elements. Visually hidden text via a `.sr-only` clip class, not `display:none`.
- Patterns to copy exactly from the WAI-ARIA APG: disclosure, dialog, tabs, menu button, combobox, listbox, switch, accordion, tree, grid. Don't invent keyboard models.

## 17. Semantic HTML
- Landmarks: one page-level `<header>` and `<footer>`, `<nav>` (labelled if several: `aria-label="Primary"`), one `<main>`, `<aside>`. All content sits inside a landmark. `<section>` only with a heading; `<article>` for self-contained items.
- Headings: one `<h1>` per page or view, no skipped levels, describe the content below. Reaching for h4+ means split or simplify.
- Use the real element: `<button type="button">`, `<a href>`, `<input>` + `<label>`, `<select>`, `<fieldset>/<legend>`, `<details>/<summary>` for disclosure, `<dialog>`, `<table>` with `<caption>`, `<thead>`, `<th scope>` for data, `<ul>/<ol>` for lists, `<time datetime>`, `<abbr title>`, `<kbd>`, `<code>`.
- Forms submit with Enter: real `<form>` with a submit button and `action`, so they work before JS.
- Every image has `alt` and width/height (or aspect-ratio). Every icon SVG is `aria-hidden` or titled.
- `<meta name="viewport" content="width=device-width, initial-scale=1">`; never disable zoom.
- Progressive enhancement: content and core actions work in HTML, CSS styles them, JS enhances. Content visible by default even if JS fails.
- SEO and metadata (title length, OG, JSON-LD): pages.md.

## 18. Icons and illustration
**Icons**
- One library per product, one style (outline or filled), one stroke weight, version pinned (systems.md). Good sources: Lucide, Phosphor, Tabler, Material Symbols (variable weight/fill/grade), SF Symbols on Apple platforms, Fluent on Windows. Never mix sets or hand-roll paths for glyphs a set already has.
- Sizes on a 4px grid: 16px in dense UI and inline with 14px text, 20px default, 24px for nav and touch bars, 32-48px only for empty states and feature marks. Icon size ≈ cap height × 1.3-1.5 of the text beside it; centre on the text's x-height, not the line box.
- Stroke matches type weight: 1.5px beside 400-500 text at 16-20px, 2px at 24px; scale stroke with size (`vector-effect: non-scaling-stroke` or the set's weight axis). Shape language and stroke agree with the radius grammar (systems.md, Shape language).
- Outline for rest, filled for the active or selected state (tab bars, toggles) and for status glyphs. Colour: `currentColor`, inherits the label's ink; accent only when the icon IS the action.
- Icons support labels; they rarely replace them. Icon-only only for universal glyphs (close, search, menu, play, more) and always with an accessible name + tooltip. Decorative icons `aria-hidden="true"`.
- Optical alignment: nudge play/arrow glyphs toward their visual centre; a trailing icon in a button sits 6-8px after the label.
- Mirror directional icons in RTL (arrows, back, progress); never mirror clocks, checkmarks, media controls or logos (typography.md §12).
- Drawing a custom icon: 24px artboard, 2px padding live area (20px), strokes on whole or half pixels, round or square joins chosen once, keyline shapes (circle 20, square 18) so sizes match the set. Export SVG with `viewBox`, no fixed `width`/`height`, `fill="none" stroke="currentColor"`.
- Inline SVG or a sprite (`<use href="#id">`) over icon fonts (fonts fail, mis-announce and blur).

**Illustration**
- Use only when it explains something a photo or diagram cannot (a concept, a process, an empty state's next step) or when the brand owns an illustration style. Never as filler, never people or scenes hand-drawn in code (tells.md); a labelled placeholder beats a bad drawing.
- One style per product: one line weight, one corner treatment, palette taken from the tokens (ground, ink, accent, one support hue), one level of detail. Commissioned or licensed sets (unDraw, Open Peeps, Humaaans) only restyled to the tokens and flagged in the report.
- Spot illustrations in empty states and onboarding ≤160-240px, above the heading, never inside a chart frame. Operate screens rarely need them; never in dense tables or dashboards.
- Diagrams over illustration whenever the content is a real mechanism: boxes, arrows and labels as real text, the product's own nouns, one hue for the path that matters.
- SVG with `role="img"` + `aria-label` (or `aria-hidden` when decorative), themed through `currentColor` and CSS variables so dark mode works without a second file.

## 19. Ship checklist
- [ ] All 8 states on every interactive element; read-only distinct from disabled.
- [ ] Keyboard-only run completes every task; focus always visible and never hidden by sticky UI.
- [ ] Every field labelled, autocompleted, validated on blur, errors as cause + fix with summary on submit.
- [ ] Every overlay: correct type, focus in/trap/return, Esc, scrim rules, no stacking.
- [ ] Destructive actions: undo or confirm naming action and object, focus on Cancel.
- [ ] Toasts ~5s (errors persist), live-announced, never focus-stealing.
- [ ] Loading by duration table; flat skeletons at final layout; zero CLS.
- [ ] Empty, no-results, filtered, no-permission, error, stale and partial states designed with real-length data.
- [ ] Targets ≥24px (44px on touch), contrast 4.5:1 text / 3:1 UI, colour never alone.
- [ ] Semantic landmarks, one h1, no div buttons; axe clean; screen-reader spot check done.
- [ ] One icon set and stroke, sized to the text beside it, every icon-only control named; illustration (if any) in one tokenised style.
