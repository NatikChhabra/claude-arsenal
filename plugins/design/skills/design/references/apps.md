# Operate-mode screens

Use when building or reviewing any screen people work in repeatedly: app screens, dashboards, admin, tools, settings, chat and AI surfaces, native mobile and desktop apps. A product's marketing page is Persuade (pages.md); its interface fragments inside that page still follow this file.

## Stance
- Scanability, consistency and platform convention beat expression. Familiarity is a feature. Brand lives in precise details, one face and one signature element, never in decoration.
- Quiet and dense: titles 18-32px, colour ~3% of pixels, motion only as feedback, no entrances, no load choreography. Product UI loads straight into the task.
- One theme locked per screen (no section inversion). A user theme toggle is fine and expected in tools used hours a day.
- Mock content is design material: real-length names, real magnitudes, totals that add up, labelled synthetic. Never Acme, John Doe, "User 1", lorem, vanity totals, growth on a week-old account.
- Never dress a tool as an instrument (terminal F-key bars, bezels, ledger paper standing in for a table). Never reinvent standard controls (scrollbars, selects, modals).

## The run for a screen
1. Inventory objects, magnitudes, people, jobs, and the product's own things (its nouns, units, rhythms). Write the dataset once, compute every total from rows, and assert the reconciliations (`console.assert`).
2. Name the screen's ONE question in one line ("Which deploy broke?", "Who is waiting for a reply?"). It decides what is biggest, what is read first, what is left out.
3. Name the ONE finding in today's data ("the 23:28 deploy doubled the error rate"). Put it in the line under the title or the subline of the headline figure, next to the action it drives. Never in a 14px caption at a card's foot.
4. List blocks as answers to the next questions, one line each. A block with no question is deleted. This kills the stock order KPI row, big chart, two small charts, table.
5. Name the most frequent job and put its control where the answer shows (primary in the title row, action on the row that needs it, "View logs" on the failed item). A screen with no control for its main job is a report, not a tool.
6. Choose the style by how it is used (long sessions or a glance, money or media, team or solo, day or night), its face, and one signature element only this product has. Two products must not get the same face.
7. Build the empty shell, write the grid arithmetic in a comment, check 1440 and 390, then render data, then every state (empty, zero, loading, error, hover, selected, focus, disabled).
8. Critique with the 7 app questions (process.md §10). Max 3 rounds.
- Show evidence beside the answer: "Error rate 0.28%, peaked at 3.9% after the 23:28 deploy, reverted" beats the bare number and beats a second chart.
- Do not rebuild a famous screen of the same kind; take the structure from the product's own things (a couple's budget as Mia / Joint / Tom columns).

## Paradigm
- Pick from IA and task, never a default grid: Table (compare fields), Master-detail (list + selected), Board (stages), Feed (temporal), Gallery (visual items), Dashboard (monitor many metrics; wrong for single-task users), Canvas (spatial), Timeline, Map, Wizard (3+ dependent steps).
- Each major entity gets a list view and a detail view. Templates, not one-offs: list page puts title, filters, view toggle, primary action and collection in the same spots; detail page runs header (name + status + actions) → key attributes → related → activity; editor keeps body, validation summary and save/cancel fixed.
- Different task kind → different paradigm. Different content only → same paradigm. Deviate fully (a distinct mode) or not at all.

## App shell
| Archetype | Values | Use for |
|---|---|---|
| Open plane | labelled sidebar on the page ground (within 1-2%), no top bar, fluid canvas | most apps; the default |
| Tinted frame, white sheet | sidebar + top bar share one tint (#f6f6f6-#f9fbfc), page on a white sheet inset 8px right/bottom, radius 10-16, 1px #eaeaea edge, no shadow | B2B analytics, dev platforms, builders |
| Ruled T-frame | 210-240px sidebar + 64px top bar on one ground, split by 1px rules only | dense dark tools |
| Icon rail | 50-60px rail, 15-18px icons on 34-49px pitch, tooltips + accessible names, product mark on top | only ≤5 destinations on width-hungry views; else label the sidebar |
| No sidebar | 46-48px top bar over a centred 1088-1208px column | reports, viewers, few destinations |

**Sidebar**
- Width 210-292px (default 230; `clamp(13rem, 18%, 18rem)`). Rows: 32px hit on 34px pitch; roomy 40-52 on 42-60.
- Icons 16px outline at 1.5px stroke, grey; labels 14/400, ~8-10px after the icon.
- Active item: neutral grey pill `#e9e9e9`-`#ededed`, radius ~8, inset 8px, label unchanged. On dark: brightness only (#bbb → #fff). Never colour alone, never a coloured fill + left bar.
- Never dark or saturated against a light canvas. Never navy or slate on dark.
- Group labels 12-13px grey sentence case, 22-56px air above. Utilities (settings, help) pinned to the bottom.
- Top: product mark + name + scope switcher (workspace/team/project). A screenshot that cannot name the product reads as a template. The mark is drawn for this product (monogram or symbol in the accent, from its name or object), never a black square with a letter; swap the asset per theme, never invert it. Logo links home.
- The shell may shrink to one return line only when entry is always via a parent app; deep links, emails and bookmarks need a home affordance.
- Footer order: scope → preferences (one row) → identity/sign-out. Identity in the footer OR the page header, never both.
- Counts only on queues that need action, noun clear from the label ("Requests 5").
- Nav items are other screens, never anchors into one long page. ~7 items per group; nav ≤3 levels, then grouping + search.
- Role-gated items removed; sign-in-gated items visible with a quiet mark; unavailable destinations explained, not hidden.
- Rail collapse: icons must carry meaning alone (label as SR text + `title`), hide group headers. Default collapsed below ~1024px; the user's choice persists across sessions and tabs. Toggle on the seam, opaque on hover.

**Top bar**
- Optional. Heights 44-51px (light chrome) or 64px with a 1px rule.
- Must hold something real: search, the switcher, or the page/object name. A mostly blank top bar, or search + bell + avatar on every screen by reflex, is a tell.
- Search: centred ~548×32 with a shortcut hint, or 457-537×36 in a no-sidebar bar. Right cluster inset 24-46px.

**Estate rules**
- Top bar is estate-level (tenant, region, locale, identity, launcher): same position, behaviour and wording in every app. The app owns everything below.
- App launcher once a user has >3 tools: only what they can open, spoken names, ordered by use then A-Z.
- Environment earns a colour strip (prod/staging). Tenant never gets a colour; show it as a label and repeat it in destructive confirms.
- Internal tools carry a persistent quirk (env badge) so they cannot be mistaken for the customer app. "Acting as" mode: persistent banner naming the account + always-visible exit.
- Status bar (heavy tools only): sync, env, active filters + match count, selection count, last saved, one key hint. Muted, no animation, colour only on a real fault.

**Right rail and floating**
- Right rail only for a stable secondary stream (details of the selected object, recent items): fixed ~384px in a `1fr 384px` grid, 24px gap, top level with the first card, not the title.
- Pinned left column only for a figure that must stay in view (net worth while the rest scrolls).
- Floating button only if it is the screen's one primary and covers nothing at any width.

## Canvas and grid arithmetic
- Fluid padding 17-64px (common 24, 32-40), content ~1120-1312px; or centred 1088-1250px for data pages. Narrower than ~1000px wastes the width. A centred column centres on the area beside the sidebar, not on the window.
- Spacing on a 4px base: card gap 6-24 (default 16), card padding 12-34 (default 20), section gap 24-64.
- Top offset canvas → title: tools 20-36px, personal homes 50-88px.
- ONE gutter value on both axes. Mixed 12/16 or 20/24 gutters are flagged.
- One left edge and one right edge from header to last row. Indent the page header by the card padding so title, card titles, numbers and charts share one line. Row rules may bleed 7-8px past the text column.
- The sum must close. Write it in a comment:
```
/* 1152 canvas: 3×372 + 2×17 = 2×568 + 16 = 1152
   1100 canvas: 12×77 + 11×16 = 1100
   second-row card = two cards above + gap: 251 + 24 + 515 */
```
- Column count comes from item count: four KPIs get four columns; a lone card spans the row. Never an equal 4-up grid with an orphan.
- Cards in a row share a bottom edge. Balance by content first (equal row caps, paired heights); else `align-items: start`, or stretch only with the action/total pinned to the foot. A blank band >40px inside a card is a hole.
- Narrow blocks (≤5 columns or ≤6 rows) run ~760px at 1440 and pair with the next block; stretched to 1300px they open 400-600px voids.
- At 1440×900 every block the brief names shows its header and first rows or figure. Headline block 200-360px tall; lists capped at 4-6 rows + "View all"; time-sensitive blocks (bills due, SLA breaches, failed deploy) before long tables.
- A chart flat for most of its window gets two-thirds width, ~140px tall, or a range capped at ~2× its reference line with the off-scale peak labelled; the next answer sits beside it.
- Empty space must come from the grid and repeated gaps. A column empty in every row, a mostly blank top bar or a stretched card is leftover space: fix the grid.

## Title row, tabs and filters
- One h1 per screen: a noun ("Analytics", the object's name) at 24/600 (range 18-32). Greeting only on personal or team homes, never with emoji. If the top bar or breadcrumb names the page, its last item is the h1.
- Optional second line: one 14-16px grey sentence about the data (finding, period, scope), never about the interface ("This page shows…").
- Right of title: real actions only, plus a freshness stamp ("Updated 16:09" + refresh). No reflex Export/Share/date-picker cluster.
- One filled primary per screen, usually near-black (`#1d1f20`) or inverted white on dark; secondary white with a 1px border; tertiary text. Controls in one row share one height. Primary sits top-right of a page header, bottom-right of a form or dialog.
- Date range at page level OR per card, never both. A card's own period goes right-aligned in its header in grey.
- Tabs (rules and ARIA: components.md §2): underline style with a 2px indicator as wide as the label; the strip may sit on one full-width 1px rule at border contrast.
- Segmented control as wide as its options; full width only below ~480px.
- Control height in title/filter rows 28-40px (default 32-34). Order: scope left (date, then filters), utility and refresh right. Title row → first card 24px.

## Density
| Level | Data points | Rows | Card padding | Body |
|---|---|---|---|---|
| Sparse | 6-25 (homes, settings, one object) | 56-92px | 20-24px | 14-16px |
| Medium | 25-50 (overviews, finance, lists) | 44-56px | 16-24px | 14px |
| Dense | ~120 (monitoring, research, ops) | list 28px, table 28-42px | 32px, ~100px gutters, 64px between bands | 13px |
- Density is three settings moved together: row pitch, padding, type size. Never shrink type and keep padding.
- Desktop medium-high, tablet medium, phone low. Power users high; consumers low. Offer a density toggle in enterprise tools.
- Size blocks to the data the account has now, not the data the product hopes for.
- Cut words before shrinking type; front-load the scanned word or number.

## KPIs
- No tile of their own by default: one container split by 1px dividers into equal columns (or a bare strip with 48-52px tall vertical dividers), or each headline number inside the card that explains it.
- Count 1-6 per row (typically 3-4), matching the columns.
- Label above value, grey, sentence case, 12-14px. Value 16-40px (default 24), ~1.7× the label. Large regular weight under a semibold label; bold for money only. Nothing ≥48px.
- The answer figure leads: 30-36px and ≥1.3× its siblings (18-24px). No other figure on the screen is larger.
- No icon in a tinted circle, no sparkline, no tinted tile. An info icon beside the label is fine. Units as a smaller grey suffix ("5 mins", "2 m 24 s").
- One figure, one place. A KPI strip that only names the panels below is dropped; lead each panel with its number.
- KPIs as series tabs: selected gets a 2px rule or active fill + ink label; others keep values in ink (grey reads disabled). As a list's type filter, the selected card takes a 1.5px border. Metrics the brief asks to see over time get their own chart on the first screen; KPI tabs switch only between the rest.
- Never show an internal score as %. +/− only for before/after, never across peers.
- Deltas optional, 12-15px, never larger than the label, window in words ("vs prior 30 days").
- Colour = good/bad, not up/down: latency, errors, cost, churn rising is negative. Good direction positive or grey. Colour only the number.
- Zero or undefined change is grey. From zero write "+4 (new)"; nothing to compare → grey dash. Never ">999%" or green "+0".
- Every relative figure names its baseline ("45 m earlier than last Sunday"). Totals and deltas are computed from the displayed rounded parts.

## Charts
**Form by question**
| Question | Form |
|---|---|
| Moving over time? | one 2px straight line; area only with flat fill ≤14% |
| How much per period? | square-cornered columns (≤4px top radius, square base) |
| Distribution? | histogram, equal bins |
| Who ranks? | sorted horizontal bar list; or the row fill as bar in a one-figure list |
| What share? | thin ring or 100% stacked bar with 2px seams, ≤5 parts; parts differing by <5% → bar |
| How far to target? | progress bar, both ends labelled, fill = true ratio |
| How much of plan used? | track = plan length, spent filled, committed lighter, overrun past the end in negative |
| Drift from target? | bar per part with a 1px target tick (bullet); never two stacked bars |
| Flow in/out? | diverging columns on one zero line, signed axis captioned each side |
| Who is away when? | people-by-day timeline, one mark per kind |
| Enough cover? | team-by-day matrix, one hue ramping toward negative |
| When in the day vs last time? | time strip: 2px grey track, ink dot today, hollow tick comparison |
| Where? | map + list; the list carries magnitudes |
- Few numbers → no chart. Under 4 points → stat, not line. Bars up to ~15 categories, sorted, horizontal once labels are long; more → table.
- Limits: waterfall 4-12 bars; radar 5-8 axes, ≤3 sets; treemap ≤3 levels; box plot ≥20 points per group; network ≤100 nodes SVG, ≤500 canvas, else cluster; streaming on canvas with a 60-300s buffer.
- Per-period bars + running total pair: once per screen, only when the total crosses a line that matters.
- Forecast after today: dashed, end value labelled, gap to target bracketed.

**Styling values**
- One series per chart, three max. Switch metrics with a control, never overlay.
- Plot 112-264px tall (default ~195), aspect 1.8-5.2.
- Gridlines: 3-5, horizontal, 1px solid `#e5e5e5` (dark `#2b2b2b`). Dashed allowed only in chart grids and empty slots.
- No y-axis line; the baseline is the one heavier line. Zero baseline for bars and counts.
- Y ticks 4-7, round even steps, top tick above the max, integers for counts, 12px grey, never louder than the data. Never a chart without a scale.
- X labels 4-8, flat, never rotated, one step that lands on the end (or leave the end unlabelled), first and last pulled inside. Time on a time scale. Units and time granularity named on the axis or in the title.
- Lines 2px straight segments (smoothing invents values). No point markers except an 8px hover dot.
- One hue per chart, on the screen's main data element (today's series, the current period). One subject keeps one hue across the screen. Warn >4 hues on a screen, fail >6. Status colours only for status.
- Neutral series are often better: near-black line, signs instead of colour.
- Legend: none for one series (the title names it). Else ≤5 items as 5-8px dot + 12-14px grey label in the card header, or a small table (dot, name, value, change). Swatch = the mark scaled down (a hatched bar's swatch is hatched); build legend and marks from one style object. Never list a series with no data. Multi-series legend items toggle their series.
- Rings 3-8px stroke, no slice labels, total in the centre or beside. Never redraw figures already listed next to it.
- Progress bars 4-24px (default 8), fully rounded, both ends labelled; zero has no stub.
- Annotate a step >~3× the usual change: 1px marker + 12px label naming the cause. Reference lines 1px dashed, label at the end. Labels never collide; lay out after fonts load.
- Tooltips: plain box, no arrow, label + value on one line; on hover, tap and keyboard focus.
- Draw short and empty histories honestly: flat zero line, missing bars, no padded range, no "No data" illustration. Never give a lone point the biggest plot.
- Magnitude scale = one hue near-black → accent; never red→green. Data marks ≥3:1, labels ≥4.5:1. Never colour alone: direct labels, line styles, patterns. Simulate colour-vision deficiency.
- Provide a text summary or data table; chart elements focusable; ≥44px touch areas on phone.
- Volume: SVG <1000 points; canvas + downsample ≥1000; aggregate >10k with drill-down breadcrumb. Scatter needs ≥20 points (500-5000 on canvas at 0.6-0.8 opacity, >5000 hexbin); heatmap 20-10k cells; funnel 3-8 stages; 3+ gauges → bullet grid.
- Data products offer CSV export of what the chart shows.
- Chart loading = skeleton of the plot, not an empty axis frame. Chart error = message + Retry inside the frame.
- Draw with your own SVG or a library restyled to these values, never library defaults, never a picture of a chart.

## Tables
- Rows: single-line 36-53px (default 45); two-line with media 56-92px (media height + 24-32); key-value rows in cards 21-32px. Two-line labels need ≥40-44px pitch; line 2 is 12-14px grey ~21px below line 1.
- Header row 36-40px, 12-14px grey sentence case, regular weight. No fill band, no zebra, no uppercase tracking. If there is a header rule it is the strongest line (#e5e7eb over #f3f4f6 row rules).
- Row rules 1px, 3-7% darker than the surface (#ededed-#f4f4f4 on white; #161616 on #000), or none with ≥61px pitch. One rule extent per screen.
- Markup: `<table>` with `<caption>` and `<th scope>`; `role="grid"` only when cells take arrow-key navigation or editing.
- Numbers right-aligned, `tabular-nums` (verify the face actually changes digit widths). Fixed decimals: money 2, % 1-2, counts 0. Thousands separators. Sign on every change. No space after currency. Abbreviate only in capacity lines ("12.7k of 20.0k"). Format through `Intl.NumberFormat` / `Intl.DateTimeFormat` in the user's locale, never string concatenation.
- Numeric headers right-aligned flush with their values. Sort glyph on the active column only; asc → desc → clear; `aria-sort`.
- Identity column gets 1/3-1/2 of the width and is never the one truncated; shorten names editorially first.
- One right edge per row or card. Two measures stack in one cell (count over 12px grey %) on one right edge.
- Missing = grey en dash with SR text "No value", never "N/A"; a real zero is printed ("$0", "0%"). "Pending"/"Not measured" when the reason matters.
- Only identity and the key number in primary ink; the rest grey. Sign in the text, not red on every negative. Rows that are fine stay grey; colour only the rows at risk or over (never a green "left" on every budget row). Link colour on the name cell only, no underline.
- Dates ISO and right-aligned when compared; words for recency ("Today", "6 days"). Absolute time + timezone in expert tools.
- IDs in mono at body size, truncated ~8 chars + ellipsis + 12px copy icon. Truncate titles to one line; never break inside a word; `min-width: 0` on flex/grid children. An inline breakdown ("Headingley 6 · Meanwood 3") goes in mini-columns or `nowrap` items with the separator attached to the next item, so no line ends on "·".
- Status pills 16-24px tall, 12px/500, pale tint + dark same-hue text (`#dcfae5`/`#04250e`, `#ffedea`/`#831c1e`), `flex: none; white-space: nowrap`. One status mark per row. Saturated fill + white text only for a rare call to action (<~1/5 of rows); otherwise the pale pair or a 6px dot with an ink label. Neutral states are monochrome chips with a glyph ("Public" + globe). A state machine uses one hue at three intensities: grey off, full hue for the call to action, dark tint running. Operator tables: 2-3 labelled states, never >5.
- Edited cells show they changed (dot or tinted border) and name the baseline.
- Media: 16px logos in dense rows, 24-32px avatars, 48px in two-line rows; circles for people/companies, 2-3px radius for artwork, 8px for photos; one fixed media slot so text starts on one edge, 10-16px gap.
- People as themselves: a stable initial on a pale tint of their own hue, people shown together ≥60° apart in hue. Identity tints stay pale and out of chart legends.
- Row actions: one kebab at far right, or, when the row needs doing (bill to pay, failed deploy), a visible ghost button or ink text action in one fixed trailing column at the same pitch for every row. Reserve that column only when most rows carry the action; else an ink text action on line 2. Never muted grey, never stacked under the amount, never hover-only for anything essential.
- Checkboxes only where bulk actions exist: 18px, 2px stroke, 3px radius.
- Sticky header; sticky first column on wide tables (corner cell higher z). Resizable/reorderable columns persisted. Virtualise per components.md §13.
- No pagination on overviews: cap rows, "View all" + total. Full list screens: total above, sticky header, "1-50 of 1,284" with page or load more.
- More than ~6 comparable items: cards become a table, unless each item holds an image, chart, controls or wrapping text.

## Spreadsheets, ledgers and record books

A sheet someone else will open (a licence office, an auditor, a client) is a document, not a database dump. It should
read like a small business's own books.

- **Blank stays blank.** Every filler formula is guarded so an unused row shows nothing:
  `=IF(AND(I5="",J5=""),"",SUM(I$5:I5)-SUM(J$5:J5))`. Never a column of `0`, never a formula that reads the header row
  (the `#VALUE!` in row 1 of a running balance). Fill guarded formulas far enough for years of use (~1000 rows).
- **Money sits at the right edge** in the order in, out, balance, right-aligned in one currency format with negatives in
  brackets (`$#,##0;($#,##0);$0`). A right-aligned number never touches a left-aligned text column: reorder, or
  centre the text column after it.
- **Header block, then one frozen header row.** Business name (one size up, bold), one quiet owner and scope line,
  totals top right (small grey label over a bold value), a short spacer, then the column headers. Freeze through the
  header row so names and totals stay on screen.
- **Brand at ~3%.** A pale tint of the brand colour on the header row and one rule in the full colour under it and
  under the headline total. Gridlines off, one hairline per row. No zebra stripes, no dark slab headers, no dashed
  borders, no all-caps.
- **Dropdowns for every closed set** (In/Out, category, status, pay basis) with a plain-words error. Amounts validated
  as non-negative numbers; direction comes from the column or the In/Out cell, never a minus sign.
- **Catch mistakes without red.** Conditional format in a pale amber: money typed in the wrong column for its In/Out,
  and dimmed or struck-through rows for cancelled jobs and staff who left.
- **Link the tabs instead of double entry.** A job's "paid so far" is a `SUMIF` over the ledger by job number, so a
  payment is typed once.
- **Plain headers in sentence case** ("Client or payee", "Still owed"), no units in brackets when the format already
  shows them.
- **Google Sheets delivery:** build the .xlsx (openpyxl), keep to formulas both apps share (no `ARRAYFORMULA`,
  no open ranges like `H5:H`), then in the live sheet use File, Import, Upload, "Replace spreadsheet": the share link
  stays the same. Before handing over, fill a copy with test rows, recalculate (LibreOffice headless) and look at a
  render of every tab.

## Lists and list-detail
- Overview lists show 2-5 rows; dashboards per card 2-3 figures + ≤2 example rows + "View all (n)".
- Selection: whole row is the hit target; selected row in a list that drives a detail pane takes the `--active` fill (same as the nav pill), distinct from hover and focus ring. Space selects, Shift-click extends, Ctrl/Cmd toggles.
- Hover: 1px outline or slightly darker border; never a fill change without a defined edge.
- Master-detail: detail starts where the list ends; title + primary action level with the selected row. Wide screens: 3 narrow columns (menu / list / detail). Draggable divider persisted.
- Bulk selection, toolbar and feedback thresholds: components.md §13.
- Data lists: row fill as bar only in one-figure ranking lists (radius 8, 44px rows, 2px gaps). Bar list: 64px pitch, 10px pill bar, longest ~88% width, one colour. Inline bars in secondary lists 2-3px grey, top item in ink.
- Feed rows ~63px, 8px gaps, relative date right. Tree: no dividers, ~8-16px indent per level, ~30px pitch, ~45px between groups. Key-value well: tinted, radius 8, 32px rows, label left, figure right.
- Chat/log: auto-scroll only if already at the bottom, else a "New messages" pill.

## Filters and search
- Workflow-scope filters (persistent bar) separate from transient search.
- Loaded-row filters in a toolbar above results with visible-of-total count; active filters as removable chips; "Clear all"; `Filter (3)` badge. Server filters submit as a form.
- Counts in scope (tabs, KPIs, "12 open") recompute from the current view on every switch; a filtered block shrinks to its rows.
- Toolbar search 30-36px tall, ~256-316px wide; debounce 300ms.
- Grid/list/table toggle only when items are both visual and detailed: top-right beside sort and filter, icon buttons with tooltips, choice persisted; phone keeps the one view that works.
- Global search mandatory past 3 nav levels (pattern: components.md §14).
- Every view is deep-linkable: filters, sort, tab and selection in the URL. Back restores scroll, filters and input.
- Persist filters, column widths, views and panel sizes across sessions in expert tools. Saved views beat re-filtering.

## Forms and settings
- Field anatomy, validation timing and error copy: components.md and copy.md. App values: label above, 14/500, 8-10px gap; inputs 38-40px, radius 8-10, white with 1px `#e5e7eb` even on grey panels; filter/select controls one step darker (`#d1d5db`).
- Spacing: 24px description → first label, 16px between fields, 16px to Save. Leading icon 14px, 13px in, text at 38px. No floating labels. A joined input + action (link + Copy) share one border with square inner corners.
- Toggles 28×16 to 33×20; on = semantic green or near-black, not the brand accent. Toggle for binary, radio/select for named options, slider + number for %.
- Disabled stays legible and says why. Read-only looks different from disabled.
- Settings layout: section row = ~450px label column (16/500 title + 14px grey description) beside a ~700px panel (`#fafafa`, radius 16, padding 16, no border, no shadow); the title's cap top level with the panel's first line. Sections split by a full-width 1px rule, 32px above and below. Never an empty label column beside a tall panel: put help or a summary of current values there.
- A usage strip opens a settings view only when usage is its question (plan, quota); its figures stay smaller than the h1.
- Switch row: 14/500 title, status badge 8px after, 14px grey description, toggle right, 16px from the edge, centred on the title line.
- One view per area (General, Members, Billing, Notifications), area name as h1. Never one long page with anchor-scrolling nav.
- One save model per view: autosave with a quiet "Saved" stamp, OR one Save per panel bottom-right. Never both.
- Preview what the setting produces beside the control (the invite email, the notification, the next invoice).
- Domain config: labels with units ("Maximum wait per request (s)"), visible defaults with "Reset to default (15 s)", unit suffix always shown, dependencies explained ("When retry is off, max attempts has no effect"). Primary settings cover 80% of tasks; Advanced collapsed; system params never in UI. Saved config vs session override made explicit.
- Plan-gated feature: a 48px tinted strip with a 32px button above the panel; the panel stays readable.
- Destructive actions last, own section, negative-colour text or outlined button, consequence in words, confirm names the object, focus defaults to Cancel.
- Narrow containers stack: label, 10px, field, 26px to the next pair.

## Coordinated views
- One shared selection store across map + list, chart + table. Click in either highlights both and scrolls the row into view. Hover = transient faint highlight; click = persistent strong selection; Esc clears.
- Colour encodes state, the label encodes identity. Colours from one source, one shared legend.
- Split 60-70% to the primary view, or 50/50 with a draggable persisted divider. Phone: one view at a time.
- View-only controls (zoom, layers, reset) live in the visual panel; shared filters sit above both. Analysis panels are non-modal beside the data.
- Debounce hover to target changes.

## Calendars and timelines
- People down a fixed 160-220px left column, grouped under team subheaders (never the team repeated per row). Pitch 32px for one-line names, 40-44px with a subline.
- Days across at equal widths with faint 1px day lines; weekends one tone step darker; today a 1px line in the data hue with its date in ink. A calendar grid changes column count, never cell size.
- Bars 20-24px tall, radius 4. Each booking kind its own mark: holiday pale fill, sick 1px diagonal hatch, long leave a darker grey step, working away an outline, pending a dashed outline. Full colour only for what needs a decision (a request that breaks cover).
- Label inside its bar; a bar too short shows the kind's code inside (full label in the tooltip) or the label after the bar's end, never over earlier days. Legend lists only kinds on screen, each swatch the mark itself.

## Expert and operational tools
- Table rows 28-36px; inline status, never hover-only; text labels over icon-only; layout follows workflow order.
- Flat rows + group-header rows + a group-by switch when the line is the unit users act on; in-place accordions for true hierarchy.
- Right-click is never the only path. Every drag has keyboard and single-pointer alternatives.
- Keyboard first: `Cmd/Ctrl+K` command palette, `/` focuses search, `j/k` or arrows move rows, `Enter` opens, `Esc` closes, `?` opens the shortcut sheet. Show the shortcut in tooltips and menu items. Preserve browser and OS shortcuts.
- Command palette: 560-640px wide, ~20% from the top, fuzzy match, recent first, shortcut shown per command, no open/close animation (used 100+ times a day).
- Error tone terse and specific ("Row 412: VAT number missing"). Absolute timestamps with timezone.
- Long jobs (export, transcode) run in the background: accept → release the user → notify with the result somewhere findable. Up to ~10s the skeleton carries it (spinner only for <1s inline actions); beyond, real progress + cancel; past ~30s users assume it is stuck.
- Optimistic UI with silent retry and rollback; surface an error only if the retry fails. Never lose input.
- Multiplayer: presence avatars in the title row (≤3 + "+n"), live cursors and selections labelled with the person's name in their identity tint, conflicts shown on the field that clashed (with both values), never a blocking modal.
- Expert pages that look thin get pulled relevant data, not imagery.

## Global toolbar
- Controls 13-14px muted regular. Group what-is-shown (region, tenant, date scope) apart from how-shown (language, theme, units).
- Language switcher shows the current language by endonym ("Suomi"), never a flag or bare globe.
- Theme toggle top-right near the account or in settings, never in primary nav. Sync preferences across tabs (`storage` event).

## States
- Shared state rules live in components.md; app-specific values here.
- Real zero printed normally; may dim to grey when the caption beside it becomes the next step.
- Missing = grey dash at label size, never "--" at value size (reads as loading).
- Empty block keeps its frame and header plus one sentence spanning the block (`grid-column: 1 / -1`), optionally a 1px dashed box, radius 8, ~38px tall, with an add link. Empty side card fills with reference data ("Nothing sold out yet today" over last Sunday's times).
- No access: name who can grant it and offer "Request access"; never a bare 403 or a silently empty list.
- First run: frame and title kept; first action where data will appear; setup progress at its true percentage.
- Filtered empty: "No results for these filters. Clear filters".
- Loading: final layout, every value a flat grey bar at its real size, headers shown at once, no shimmer, no layout shift. Refresh of on-screen data keeps old values and updates the freshness stamp.
- Error inside the failing block only: what failed + when data was last good + Retry ("Couldn't load deployments. Last updated 09:14. Retry"). Negative colour on a small icon only.
- Stale snapshot: one quiet notice (`#fffbeb`, 1px `#fde68a`, 12px `#92400e`). A notice tint is never a ground.
- Red is a signal: one red mark per object at most, on the failing fact.

## App type and colour values
- Type: typography.md §9 owns the role sizes (title 24, KPI 24, body 14, glance meta 12, ≤5 sizes per view, ≤3 sub-14 roles, never <11). One neo-grotesk chosen on purpose (Inter acceptable here when deliberate); a second face only for one job (mono for IDs or every figure, a serif for one greeting); axis ticks stay in the text face. Weights ~3 per screen, 700 does one job. Sentence case; ≤1 tracked uppercase label per screen. `tabular-nums` on every number.
- Colour: colour.md (App exact values, Status) owns the light and dark values. ~3% of pixels (warn >12%); accent on the main data + at most one control, never on chrome. Lines in three steps: row rules lightest, card edges ~1.2:1, control borders one step darker; `#cbcecd` on cards reads heavy, `#f5f5f5` disappears. Border OR shadow, never both. A second neutral layer (≤10° hue shift) allowed for sidebar/toolbar. Dark emphasis without colour: inverted white pill, `#212121` grey-filled button, outline.
- Radius bimodal, chosen once (layout.md §10): tight 4-8 (buttons and toolbar controls 6, inputs 8-10) or soft 12-20 for cards (buttons pill, inputs ~14). Nested radii step down (20, 10, 8, 5, 4); outer = inner + gap. Warn >3 panel radii.
- Status: the sign carries the meaning, so the negative hue is swappable for owners who ban red; pending/draft grey or blue, never orange.
```css
:root {
  --ground:#f9fafb; --surface:#fff; --raised:#f9f9f9; --active:#eee;
  --border:#e8e8e8; --rule:#f2f2f2; --control:#d1d5db;
  --text:#111; --muted:#5f6368; --faint:#6b6b6b;        /* placeholders use --faint */
  --primary:#1d1f20;                                     /* near-black fill, white label */
  --accent:/* one hue, ~3% of pixels: main data + ≤1 control */;
  --positive:#247b50; --pill-pos-bg:#dcfae5; --pill-pos-ink:#04250e;
  --negative:#c4242a; --pill-neg-bg:#ffedea; --pill-neg-ink:#831c1e;
  --pill-warn-bg:#fffbeb; --pill-warn-ink:#92400e;       /* border #fde68a */
  --grid:#e5e5e5;
  --radius-card:8px; --radius-control:6px; --radius-chip:4px;   /* soft: card 20, inputs 14, buttons and chips 999 */
  --gap:16px; --card-pad:20px; --pad:24px;
  --nav-row:34px; --control-h:32px; --row-h:48px;
  --fs-title:24px; --fs-section:16px; --fs-kpi:24px; --fs-body:14px; --fs-meta:12px;
}
:root[data-theme="dark"] {   /* repeat inside @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) } */
  --ground:#000; --surface:#111; --raised:#222; --active:#222;
  --border:#1a1a1a; --rule:#161616; --control:#444;     /* on a #111 ground: border #2e2e2e */
  --text:#fff; --muted:#b4b4b4; --faint:#949494; --primary:#fff;   /* white fill, black label */
  --positive:#3fc07a; --pill-pos-bg:#172a1d; --pill-pos-ink:#3fc07a;
  --negative:#e5566f; --pill-neg-bg:#2c1a20; --pill-neg-ink:#e5566f;
  --grid:#2b2b2b;
}
.num { font-variant-numeric: tabular-nums; } td.num, th.num { text-align: right; }
```

## Allowed in Operate, banned on pages
| Allowed | Limit |
|---|---|
| 1px borders and row rules | ~1.1-1.3:1 on light; no zebra, no header band |
| Dashed lines | chart grids and empty slots only |
| Small grey labels | 12-14px sentence case at 4.5:1 |
| Identical cards | peer metrics/objects only, 3-6 across, no icon on top; prefer one divided card |
| Mono | IDs, keys, code, or all figures as a style |
| Pills | inside rows, 16-24px, pale tint + dark same-hue text; never above a heading |
| Index numbers | only as data (rank, node number) |
| Icons | 14-20px outline, one set, grey; never in a saturated circle or tinted square |
- Still banned: decorative gradients, glows, glass cards, icon-in-circle KPIs, sparklines on KPIs, rainbow charts, emoji, dark/saturated sidebars, accent on chrome, uppercase tracked headers, left-aligned numbers, hero headers, pagination under short lists, titles >32px or figures ≥48px. Full catalogue: tells.md.

## Motion in apps
- Feedback only, 150-250ms, never >300ms; no entrances, staggered load or scroll reveals; nothing on keyboard or 100+/day actions. Values: motion.md §9 (Operate).

## Phone and tablet adaptation
- Same items, same order, same IA as desktop, recomposed; never hide core functions.
- Nav folds: sidebar (fail if >30% width) → 48px top bar with screen name + menu opening a full-screen sheet (nav, switcher, account) + ≤1 action; or a 4-5 item bottom bar with icon + label (an icon rail always becomes this bar). Drawer trigger in a bottom corner inside safe-area insets; scrim, scroll lock, closes on navigation.
- Margins 16-20px; targets ≥44px; data and labels 14px; sublines ≥12px; inputs 16px (prevents iOS zoom).
- Title stays at 20-24px. Header actions → kebab, except the one primary.
- Filters → one row of chips or a Filters sheet; tabs scroll sideways in their own row. First list row starts in the top 60% of the screen.
- KPIs → 2-column grid (even count after a full-width lead; odd last cell spans) or a label-left/value-right list. Never four squeezed columns.
- ≤1 control row above a chart. Charts full width, 160-200px tall, 3-4 x labels, legend dots above (2-column grid or a "Key" disclosure if it would wrap to 3 lines), y ticks in their own lane, never on the line. KPI series tabs become a 2-up grid with the selected cell filled, or a sideways-scrolling row.
- Tables below ~640px → two-line rows: identity + key number on line 1, other fields in 13px grey on line 2, action right. Fields move, never drop. A table that must stay a table scrolls inside its frame with the first column fixed; the page never scrolls sideways.
- Row actions: text actions or one compact trailing button; one filled bulk action for the list.
- Collapsing a strip drops the item least relevant to the main action, not the last in source order.
- Blocks that carry an action move up as a summary row ("5 items low · Review"), never below the main list.
- Panes one at a time: choosing a row pushes the detail; back returns to the list at its scroll position.
- Settings: label column stacks above its panel. Right rail → under the main column or into a tab. Builders show work read-only; palette as a bottom sheet.
- Secondary actions in a sheet, bulk actions hidden, advanced settings on their own screen, charts reduced to the key metric.
- Tablet (768-1023px, layout.md §14) is its own band: sidebar folds (or rail in landscape), tables keep 4-5 columns with secondary fields as sublines and the identity column never truncated while another has room, panels stack once either is <~340px, master-detail fits.
- Input help by capability (`hover`, `pointer` queries), never by width.

## iOS (HIG)
- Targets 44×44pt. Standard side margins 16pt (20pt on wider devices). List rows ≥44pt.
- Never hardcode bar heights; use safe areas. Reference: nav bar 44pt, large-title nav 96pt (title 34pt bold, collapses on scroll), tab bar 49pt + 34pt home indicator inset, status bar 47-59pt by device.
- Dynamic Type text styles only (sizes: typography.md); body 17pt, floor 11pt; support the largest accessibility sizes without truncation.
- SF Pro (system font) for UI; SF Symbols matched to text weight; semantic system colours (`label`, `secondaryLabel`, `systemBackground`, `separator`) and one tint colour.
- Navigation: tab bar for 2-5 top-level sections (icon + label, never hidden on push unless full-screen task); navigation stack with back title; sheets for focused tasks (detents medium/large, grabber, swipe down to dismiss; confirm only with unsaved changes).
- Never block the left-edge swipe back. No custom back buttons. No hamburger as primary nav.
- Settings: inset grouped lists. Alerts: ≤2 side-by-side buttons (3+ stack), Cancel on the leading side, the likely action trailing; a destructive button takes the destructive style and is never the preferred (bold) one, so Cancel stays the default.
- Swipe actions on list rows (trailing destructive, leading positive) with visible alternatives. Pull-to-refresh only on refreshable lists. Long press opens a context menu.
- System materials for bars and sheets; never hand-rolled glass. iOS 26+ Liquid Glass: tab bars, toolbars and controls float on system glass above content (the tab bar can minimise on scroll); standard components get it free; never put glass on the content layer or stack glass on glass.
- iPad: in regular width the tab bar can become a sidebar (adaptable tab view); support pointer hover effects, hardware-keyboard shortcuts (listed when Cmd is held), multiple windows and Split View sizes.
- Haptics: impact (light/medium/heavy/soft/rigid) for physical moments, notification (success/warning/error) for outcomes, selection for picker ticks; SwiftUI `.sensoryFeedback`. Confirmations and important actions only, fired on the same frame as the visual.
- Reduce Motion → crossfade; Reduce Transparency → opaque; Increase Contrast → stronger separators.

## Android (Material 3)
- Targets 48×48dp with ≥8dp spacing. Text in sp, layout in dp. Roboto/Roboto Flex or the brand face via type roles.
- Window classes: compact <600dp, medium 600-839, expanded 840-1199, large 1200-1599, extra-large ≥1600. Margins 16dp compact, 24dp medium and up.
- Navigation by class: compact → navigation bar (3-5 destinations; 80dp baseline, 64dp in M3 Expressive); medium → navigation rail (80dp baseline, 96dp collapsed in Expressive); expanded+ → expanded rail (220-360dp, Expressive's replacement for the drawer) or permanent drawer (≤360dp). Modal drawer only for secondary destinations.
- Canonical layouts at medium and up: list-detail, supporting pane, feed. Two panes from expanded.
- Top app bar: small/center 64dp, medium 112dp, large 152dp, collapsing on scroll.
- FAB: one per screen, the primary action only; 56dp (small 40, large 96); extended FAB with label when space allows.
- Type through the M3 roles only (Display, Headline, Title, Body, Label; sizes: typography.md).
- Shape scale: 0, 4, 8, 12, 16, 28, full. Tonal elevation (surface-container levels), not heavy shadows.
- Colour roles (primary, on-primary, primary-container, surface-container-low…high) with Dynamic Color and a static fallback scheme.
- Predictive Back always works; never intercept back without a reason. Edge-to-edge with window insets (default from Android 15).
- Snackbars for transient feedback: one line, ≤1 action, 4-10s, above the nav bar and FAB.
- Motion: container transform, shared axis, fade through; standard easing `cubic-bezier(0.2, 0, 0, 1)`; durations 50-200 short, 250-400 medium. Compose M3 Expressive uses spring tokens instead (spatial springs for movement, non-bouncy effects springs for colour and opacity).
- Haptics via `performHapticFeedback` (CONFIRM, REJECT, LONG_PRESS, CLOCK_TICK, SEGMENT_TICK); none on scroll.
- Never port iOS controls to Android or the reverse; never ship web affordances (hover states, custom back) in a native app.

## Desktop and Electron apps
- Feel native: OS font stack `-apple-system, BlinkMacSystemFont, "Segoe UI Variable Text", "Segoe UI", system-ui`; follow OS dark mode (`nativeTheme`); arrow cursor on controls, pointer only on links; `user-select: none` on chrome, never on content.
- Title bar: macOS `titleBarStyle: 'hiddenInset'`, keep ~72-80px clear at the left for traffic lights, bar 28pt (52pt with unified toolbar). Windows `titleBarOverlay` 32-40px tall, keep ~138px clear at the right for caption buttons (46px each). `-webkit-app-region: drag` on the bar, `no-drag` on every control inside it.
- Native menu bar with standard menus and accelerators: `CmdOrCtrl` (Cmd on macOS, Ctrl elsewhere). macOS: first menu named after the app (About, Settings…, Hide, Quit); "Settings…" `Cmd+,` (named "Preferences" before macOS 13). Windows: menu inside the window, Settings under File or Tools, `Ctrl+,` common. Undo/redo `CmdOrCtrl+Z` / `Shift+CmdOrCtrl+Z` (plus `Ctrl+Y` on Windows) on a real undo stack. Close window `CmdOrCtrl+W`; quit `Cmd+Q` on macOS only.
- Dialog button order follows the OS: macOS primary rightmost with Cancel to its left; Windows primary first then Cancel, both right-aligned. Use native message boxes (`dialog.showMessageBox`) to get it free.
- Native context menus (`Menu.popup`), native notifications, native file dialogs. Right-click mirrors visible actions.
- Window: `show: false` until `ready-to-show`; `backgroundColor` = theme ground (no white flash). Persist bounds, maximised state and panel sizes. Set a minimum size (~800×600) and design that size. Multiple windows when documents are independent; single-instance lock otherwise.
- Translucent sidebar material (macOS `vibrancy: 'sidebar'`, Windows `backgroundMaterial: 'mica'`) only behind the sidebar, with an opaque fallback under reduced transparency.
- Keyboard everywhere: every action reachable by shortcut or menu, Tab order through panes, F6 or `Ctrl+Tab` between regions.
- Offline-tolerant: autosave every 30-60s, recover drafts on relaunch ("Restore / Discard"), queue writes while offline. Auto-update quietly; prompt to restart, never force mid-task.
- Overlay scrollbars styled from the palette, never hidden. Drop zones show on drag-over only.
- Tray / menu-bar icons: monochrome template images on macOS (`Template` suffix, 16-22pt), a multi-size .ico on Windows; click (macOS) or right-click (Windows) opens a native menu.

## Chat and AI surfaces
- Conversation column ~680-760px, centred on the area beside the sidebar; user turns right-aligned on a one-step tint, assistant turns full-width on the ground with no bubble. No avatars on every turn.
- Composer pinned to the bottom inside safe-area insets: auto-growing textarea (1 to ~8 lines, then scroll), Enter sends and Shift+Enter breaks on desktop (Enter breaks on touch), attach and send as labelled icon buttons, send disabled only while empty.
- Streaming: tokens render as they arrive with a Stop control in the send slot; auto-scroll only while the user is at the bottom, otherwise a "Jump to latest" pill; announce completion, not every token (`aria-live="polite"` on a summary, not the stream).
- Each answer: copy, regenerate, feedback as quiet icon buttons on hover and focus (always visible on touch); code blocks per typography.md §13; citations as numbered inline links to a source list, never invented.
- Label AI-generated content; errors keep the user's message with Retry; long tool runs show the real step ("Searching 3 sources") instead of a generic spinner. No sparkle icon or shimmer to mean "AI" (tells.md).

## Critique
- The 7 app questions, personas, Nielsen score and ship bar: process.md §10-11. Verify by rendering at 1440 / 768 / 390 and the real target viewport.
