# Copy and UX writing

Use when writing or reviewing any visible string: headlines, body, buttons, links, nav, labels, errors, empty states, toasts, confirmations, alt text, numbers. Write copy before markup; layout cannot rescue a headline that needs four lines.

## 1. Copy comes first

- Write the page or screen as a plain-text copy deck before any markup. Run the real copy at every breakpoint.
- Answer five questions in a scratch note, one line each:
  1. Who reads, and what do they already know?
  2. What is this, said the way its maker would tell a friend?
  3. What single thing should they believe after one screen?
  4. What makes them believe it (the thing itself, a number, a name, a demonstration)?
  5. What do they do next?
- List the page as claims, one per section, each with its proof. A section with no claim is filler: delete it. The order of the argument is the order of the page.
  ```
  1. A three-legged oak stool, made to order.            -> the stool, large
  2. Each seat is cut from one board.                     -> three close-ups
  3. It takes six weeks, and you can follow it.           -> the stages, photographed
  4. It costs 240 and the maker delivers it.              -> price, button
  ```
- Feed the copy from the inventory of 8-12 things only this client has (name and its meaning, street, its numbers, its constraint, materials, hours, rituals). Specific nouns come from there.
- Persuade question chain and what the first screen must say per subject: pages.md §1.
- Per state in an app, decide: the one fact the user needs now, the next action, any context that changes the decision, the tone. Say each idea once; a heading that explains the state makes the intro redundant.
- Refinement keeps copy. Ask before changing factual copy, claims, legal text, nav labels, form field names or SEO slugs.

## 2. Voice and tone

- One voice per product; tone shifts with the moment. One register per page: never mix terse technical, editorial prose and marketing punch unless the brand voice is exactly that.
- Plain language. Keep trade words the audience genuinely knows; never flatten them into generic ones.
- Boring beats cute. AI-cute copy (forced metaphor, wordplay that does not track, mock-humble craft talk) is worse than a plain functional sentence.
- Address the user as "you". The product says "we" only for a human-backed action ("We'll email you when it's ready"); never "I" unless the product is a named assistant. Pick "your" or "my" for owned things and hold it.
- Use contractions (can't, you're, it's) except in legal or precision-critical text.
- Never "please" as filler; never "sorry" unless the product is at fault and it cost the user something.
- No jokes about money, privacy, deletion, access loss or blocked work. Warmth is fine there, wit is not.
- Delight copy only at moments that earn it (effort, waiting, first use, recovery, mastery). Test: a neighbouring product could not use the line unchanged.
- Specific beats generic: "Start tracking" over "Get started"; a real kbd hint or product-specific badge copy over a slogan.
- No confirmshaming or guilt copy on declines: the decline says what it does ("Not now", "Reject all").

| Moment | Tone | Shape |
|---|---|---|
| Routine success | neutral, past tense | 1-4 words: "Saved", "Link copied" |
| Real milestone | warm, specific | one line with the number: "30 days in a row" |
| Recoverable error | calm, direct | what failed + how to fix |
| Payment, privacy, data loss, access | serious, reassuring | full sentences, consequence first |
| First-use empty | inviting | heading + one sentence + action |
| Waiting | honest | names the operation, real progress |
| Pro tool error | terse, exact | "Row 412: VAT number missing" |

## 3. Headlines

- Every headline fits in **2 lines or fewer at every width** (1440, 768, 390). Do the arithmetic before committing to a sentence:
  ```
  chars per line ≈ line width px ÷ (font size px × k)
  k ≈ 0.40 condensed · 0.50 grotesk/serif at display size, tight tracking · 0.58 wide, extended, all caps
  ```

| Where | Line width | Size | Chars/line | 2-line budget |
|---|---|---|---|---|
| Phone 390, 20px gutters | 350px | 44px | ~16 | ~32 |
| Phone 390, 20px gutters | 350px | 34px | ~21 | ~42 |
| Tablet 768 | 690px | 64px | ~22 | ~44 |
| Desktop, 12-col measure | 1100px | 104px | ~21 | ~42 |
| Desktop, half width | 620px | 72px | ~17 | ~34 |

- Budget: **~32 characters, 4-6 words** works everywhere at a confident size (gallery median: 5 words, 32 chars). Up to ~42 only if the phone size drops to the mid-30s. Hard ceiling 8 words; past that it is a sentence: move the rest into the supporting line.
- Fix a long headline in this order: cut words, widen the measure, reduce size last. Never ship a timid 28px nine-word headline; five words at 64px wins.
- Control the break: `max-width` in `ch`, `text-wrap: balance`, author the break between phrases (`Stools for<br> small kitchens`) and check it at 390; hide the `<br>` under a breakpoint if it misfires. No orphan word on line 2: cut a word, or bind the last two with `&nbsp;`.
- Section headings: 2-5 words (median 3), plain: "Pricing", "The menu", "Rooms". Every section opens with one.
- Operate screen titles: a noun, 1-3 words ("Invoices", "Analytics"). Greeting only on a personal home, never with emoji.
- Sentence case. No full stop, unless the brand sets every headline with one.
- Shapes that work (pick the plainest true one):
  - **The name**, very large, with a one-line description beside it. Best for short names and visual subjects.
  - **What it is**, with one specific word: "Furniture for small rooms."
  - **The claim** a competitor could not sign: "Your bank won't do this."
  - **The instruction**, verb first: "Understand your money."
  - **The place or moment**: "Lisbon, since 1984."
- Shapes that are the average of every landing page: tells.md (Banned shapes). Also never style one word of a headline differently (italic, serif, colour, underline, pill); emphasis uses the same family's bold or italic.
- A bare-name headline needs a ≥18px line under it that says what the thing is.

## 4. Supporting line, statements, body

- **Supporting line:** one sentence, ≤22 words, ≤4 lines on phone, directly under the headline (32-48px below) and visible with it. Says concretely what it is and for whom. Never restates the headline; never docked at the screen foot or delayed by animation.
- **Statement** (manifesto line, large quote): it is a paragraph, so mark it up `<p>` or `<blockquote>`. ≤25 words, ≤36px desktop / 32 tablet / 24 phone, ≤3 lines (4 on phone). Bigger, or used as the first screen's main line, and it is a headline with a 2-line limit.
- **Body:** short paragraphs of plain statements. Specific noun and real number: "ships in a week" not "fast delivery", "38 seats" not "intimate". Delete any sentence a competitor could print unchanged.
- Landing page paragraphs ≤~25 words. Default section shape: heading + ≤25-word paragraph + one visual or one action.
- Deliver every requested section completely in that tight copy: the whole menu with prices, every room with its rate, every speaker and talk. Long sets go in a fitting component (grouped chunks, tabs, top 3-5 + "View full list"), never cut to a stub.
- Use the number of items the content has. Three parallel items everywhere (features, stats, steps) is a tell.
- Bold in body: a 2-5-word claim cluster, about one per section, never starting on an article ("the", "a").
- No explainer captions narrating the design ("A clean layout for…"), no micro-meta lines under headings.
- Captions: one short line that adds information (who, where, when; under a verdict or chart, a quantity), never a synonym of the heading.

## 5. Proof, sample content, placeholders

- **Never invent proof:** customers, logos, named quotes, ratings, stars, user counts ("10,000+ teams"), press, benchmarks ("10× faster", "99.9% uptime"), prices, capabilities. Real logos only when they really are customers.
- No fake scarcity or urgency: countdowns, "Only 2 left", live-stock or "people viewing" counters only when the number is real and live.
- No proof supplied: use what is true by construction. Show the thing large, state how it works specifically, use brief facts (price, place, year, materials, what's included).
- A requested testimonial or logo section with no real material: plainly fictional sample content, no real companies or people, flagged in the report for replacement.
- **Sample details are expected** where the brief gives the shape but not the detail ("six rooms from €140"): write each one plausibly (name, bed, view, rate) so the design is judged at real density. List every sample detail in the report.
- A binding fact with no basis at all (exact price, phone, address, legal entity): a visible marked slot like `[Your price]`, listed in the report.
- Demo data in apps: author it at full fidelity, irregular and realistic (`47.2%`, `1,284`), internally consistent (totals equal displayed parts), labelled synthetic. Never fake-perfect (`99.99%`, `50%`, `1234567`) or fake-precise specs the brand doesn't claim (`5.8 mm`, `4.1×`).
- Never ship: lorem ipsum, John/Jane Doe, Sarah Chan, Acme, Nexus, SmartFlow, Cloudly, example.com, 123 Main St, "User 1", "Item 1", "Feature One/Two", "Welcome to our website", `{{placeholder}}`, `[REPLACE]`, visible TODOs, "Coming soon" on shipped features. Names are locale-appropriate and believable.
- No checkout exists: the primary goes to the real destination, else a prefilled `mailto:` or a flagged `#checkout`. Never a fake payment form.

## 6. Buttons and CTAs

- Name the action or the thing: verb + object. 1 word ideal, 2 fine, 3 max ("Book a table", "Download for Mac", "Save changes", "See the plans"). Titles carry longer explanation.
- Describe the outcome, not the gesture: "Save changes", never "Click to save". Name by effect: "Archive" not "Hide", "Transfer ownership" not "Change user".
- Never "Submit", "OK", "Yes", "No", "Get started", "Learn more", "Click here", "Read more" when a specific verb exists. "Continue" is fine between wizard steps; "Cancel" stays "Cancel".
- One primary per screen or view (one per step in a flow). It keeps one name everywhere. A second action is a text link with different words. No duplicate intents ("Get in touch" next to "Let's talk"). On long pages repeat the primary at most once at the bottom, never twice in one viewport.
- Persuade: the first screen carries the real action (a search, an add-to-cart, a booking), not a link to it. CTAs promise the result: "Start free", "Check fitment".
- Labels never wrap to 2 lines (check at 390). Sentence case, no full stop.
- At most one arrow glyph, on the primary only, and only if the direction uses arrows.
- Loading label keeps the button width: spinner, or present participle with an ellipsis ("Saving…"). After a one-way action, the result replaces the button in the same slot ("Sent").
- Disabled buttons say why nearby ("Add a payment method to publish"), never silently.
- Menu items and buttons that open a dialog needing more input end in an ellipsis: "Rename…", "Export…". Direct actions don't.

## 7. Links and navigation labels

- Link text makes sense out of context: name the destination ("Pricing details", "Read the 2025 report"). Never "here", "click here", "more".
- Download links state format and size: "Annual report (PDF, 2.4 MB)". Links that open a new tab say so (visually or in the accessible name).
- Return links name the destination: "← Dashboard", never "Back" (back is history, up is hierarchy). Breadcrumb's current page is plain text.
- Nav labels: single nouns, specific beats generic ("Library" not "Home", "Workspace settings" not "Settings"), the user's words not the engineer's ("Jobs" not `task_assignment`).
- Same name on every surface for one destination: nav, breadcrumb, page title, dialog, email, API error. One label used once; any repeated target or label in nav is a finding.
- Persuade nav: wordmark + 3-5 links (median 3) + one action; phone uses a text "Menu". Operate: ~7 items per group, groups named by user goal.
- Language switcher shows the current language by endonym ("Suomi", "Deutsch"), not a flag or globe alone.
- Keyboard hints use platform glyphs in `<kbd>`: "⌘K" on Mac, "Ctrl+K" elsewhere.

## 8. App words

- Trade words, not schema words: "Waiting on the customer", "Due on the 28th", not "Items", "Records", "Status".
- No internal shorthand, IDs, error codes or process names in customer UI ("recon job", "P2").
- Ceiling of ~10 coined terms per product. Keep a glossary; same noun and verb for the same concept everywhere; never vary words for literary effect.
- Show state transitions as labels plus verb buttons: "Draft" → "Mark as paid" → "Paid".
- A screen's subline talks about the data or the finding ("Revenue is up on repeat orders"), never about the interface ("Here you can see your revenue").
- Every relative figure names its baseline and window in words: "45 min earlier than last Sunday", "+12% vs last month". From zero write "+4 (new)", not "+∞%".
- Colour and copy say good/bad, not up/down: latency up is negative.
- One word per comparison axis: change-over-time and difference-across-peers never share a word on one card. +/− only for before/after, never across peers.
- One name per moment; a fact shown twice is one variable and agrees everywhere. Totals and deltas are computed from the displayed rounded parts.
- Counts name the whole: "1-50 of 1,284", "Showing 24 of 310 invoices", "View all (47)", "Filter (3)"; bulk selection says "3 selected", then "Select all 247 results".
- KPI: label above value, units as a small suffix. Legends are labels ("■ Completed □ Total"), not sentences.
- Settings: label by domain concept with units ("Maximum wait per request (s)"); show defaults ("Reset to default (15 s)"); explain dependencies ("When retry is off, max attempts has no effect"); preview what the setting produces; label toggles by the setting, not its state.
- Freshness: "Updated 4 min ago" with a refresh action wherever data can be stale. Autosave: "Saved 2 min ago" / "Saving…".
- Pro tools: absolute time with timezone; consumer surfaces: relative time with the absolute date on hover.

## 9. Forms and microcopy

- Field anatomy (label, placeholder, helper, required marking): components.md §7. Wording rules here.
- Helper text answers the implicit question and never restates the label. Explain why you ask only when it is not obvious.
- Show requirements before submission, beside the field: password rules, file types and size ("PNG or JPG, up to 5 MB"). Better: remove the limit (accept any common format).
- Character limits: show a counter only near the limit ("12 characters left").
- Search fields: placeholder names the scope ("Search lessons"), backed by an accessible name; it is the one place a placeholder may stand in for a visible label.
- If a control needs a how-to sentence, redesign the control.
- Validation copy says what to fix without blaming: cause + fix + example ("Enter a VAT number like FI12345678"), never "Invalid input", never "You entered…".
- Multiple errors after submit: a summary at the top naming the count ("2 fields need attention") linking to each field.
- Wizard step titles in the user's language ("Your delivery address"), with "Step 2 of 4".
- Unsaved changes: "Discard unsaved changes?" with "Keep editing" / "Discard".

## 10. Error messages

- Formula: **what failed + why (if known and useful) + how to recover**. The object by name, the fix as an action.
- Never "Something went wrong", "Error 500", "Oops!", "Uh oh", raw codes or stack traces as the message. A code may follow as small reference text for support.
- Never promise a cause or resolution the system cannot know. Say when data was last good.
- Place the error where the failure is: field inline, block inside the failing block, page-level only when the whole page failed. Preserve the user's input.
- Failed destructive or save action: say nothing was lost, and where it is kept.
- No exclamation marks, no humour, no red-only meaning (pair with icon + text).

| Case | Write |
|---|---|
| Offline save | Couldn't save “Q3 plan”. You're offline; your changes are kept on this device. [Retry] |
| Autosave failed | Autosave failed. Your changes are stored on this device. [Retry save]; on return: [Restore] [Discard] |
| Sign-in failed | Email or password is incorrect. (Never say which one.) [Reset password] |
| Block load failed | Couldn't load invoices. Last updated 09:42. [Retry] |
| Server fault (500) | Couldn't load invoices. The problem is on our side. [Retry] |
| Timeout | This is taking longer than usual. [Try again] |
| 401 / session expired | Your session ended. Sign in to pick up where you left off. |
| 403 | You don't have access to Billing. Ask a workspace admin to add you. [Request access] |
| 404 | This page moved or never existed. [Go to dashboard] [Search] |
| 429 | Too many attempts. Try again in 2 minutes. |
| Payment declined | Your card was declined. Try another card or contact your bank. |
| Conflict | Dana edited this while you were away. [Review changes] |
| Retry failed 3 times | Still can't connect. [Contact support] |

## 11. Empty states

- Distinguish five kinds and write each differently: first use, user cleared, no results, filtered to nothing, no permission. An error is never shown as empty.
- First use: what will appear here + why it matters + how to start (one action or template), placed where the data will be. Keep the frame and header; one sentence spanning the block.
- No results echoes the query and offers a way out: "No results for 'fretbord'. Check the spelling or search all lessons."
- Filtered: "No invoices match these filters. [Clear filters]".
- User cleared: short and done: "All caught up."
- No permission: "You don't have access to Payroll. [Request access]".
- Pro tools: empty states point at the fix ("Widen the date range"); consumer: onboarding tone.
- Never an illustration with "No data yet" in an empty chart; write what will show and when ("Your first session will show here").

## 12. Loading and progress

- Name the real operation: "Importing 1,284 contacts…", not "Loading…" when the wait is meaningful.
- Determinate when known: "312 of 1,284". Never fake progress or delay completion for a flourish.
- Past ~10s show real progress plus "Cancel"; past ~30s users assume it is stuck, so say what is still happening. Background jobs release the user: "Exporting. We'll notify you when the file is ready." The result lands somewhere findable.
- Waits of 3s+ may show the actual process steps or one genuinely useful tip; never copy that pretends to be progress.
- AI output streams as it generates (never a 10s+ spinner) and is labelled as AI-generated.

## 13. Success, toasts, notifications

- Routine success is brief and past tense: "Saved", "Invoice sent to Dana", "12 files moved". Never "Successfully…".
- No toast when the change is already visible in place. An in-place confirmation ("Saved", "Copied") clears itself after 2-3s.
- Mention the next consequence only when it changes what the user does ("Invoice sent. Dana has 14 days to pay.").
- Toast anatomy and timing: components.md §10. Undo copy: "Project archived. [Undo]". Prefer undo to confirmation for anything reversible.
- Live region text reads as a complete phrase: "3 items in cart", not "3".
- Notifications: actor + action + object, in past tense: "Dana commented on Q3 plan", "Invoice 1042 was paid".
- Bulk summary (thresholds: components.md §13): "1,240 contacts imported, 3 skipped. [View skipped]".
- Celebration copy scales with consequence: specific and numeric ("30-day streak"), at most one exclamation mark, never for routine saves.

## 14. Confirmations and destructive actions

- When to confirm vs undo, focus and dismissal: components.md §9. Wording:
- Title names action and object: "Delete project “Website redesign”?".
- Body states the consequence and scope in words: "This will email all 240 subscribers." / "3 invoices and their payment history will be deleted. This can't be undone."
- Confirm button repeats the action and object: "Delete project", "Delete 3 invoices". Never Yes/No/OK/Submit. Cancel holds default focus.
- Highest risk: type the name to confirm ("Type website-redesign to confirm").
- Multi-tenant: repeat the workspace or tenant name in the destructive confirm.
- Destructive settings sit last, with the consequence in words.

## 15. Onboarding, tooltips, help

- Teach 1-3 core concepts, in context, on real controls with sample data. Tours 3-7 steps, one sentence each, with "Skip" and "Back", replayable, shown once. "New" badges and discovery cues end on first open or after ~3 showings.
- Help order: self-explanatory UI > tooltip > docs. Help titles are tasks: "How do I export a report?".
- Tooltips: 1-2 lines, no links or buttons inside, add information the label lacks.
- Icon-only controls get an accessible name that matches the tooltip.

## 16. Accessibility and localisation of strings

- Alt text carries the image's information; functional images say the action ("Go to homepage"); decorative `alt=""`; complex images: short alt + caption or table.
- Accessible names contain the visible label text (WCAG 2.5.3). Screen-reader text for visual-only marks: a muted dash reads "No value".
- Never rely on colour, position or shape alone in instructions ("the green button on the right" fails).
- Write complete translatable strings. Never concatenate fragments; use named placeholders so translators can reorder.
- Plurals through ICU / the i18n library: "1 file", "0 files". Never `count === 1 ? … : …`, never "file(s)".
- Leave 30-40% room for expansion (German runs ~30% longer; labels under 10 characters can double). Don't abbreviate early to fit.
- Truncate with an ellipsis and the full text on hover/focus; middle-truncate file names and IDs (`Q3-rep…final.pdf`); never truncate prices, counts, or the identifying column first.
- No idioms, puns or culture-bound jokes in product UI. Mark inline foreign text with `lang`.
- Check at 200% zoom and with the longest real value (100+ character names, numbers in the billions).

## 17. Case and punctuation

- **Sentence case** for headings, buttons, labels, nav, tabs, menus, table headers and titles. Capitalise proper nouns and product names only. Native macOS menus follow platform title case.
- **No em or en dashes** in any visible text: UI copy, titles, descriptions, captions, posts, scripts, alt text, messages. Use a comma, colon or full stop. Verbatim third-party lines (a licence credit, a publisher notice) are exempt.
- Numeric ranges: an unspaced hyphen (`9-17`, `€140-€220`) or "to" in sentences.
- Middle dot `·` at most once per line. No strings of words joined by dots or slashes.
- Curly quotes and apostrophes (“ ” ’), a real ellipsis (…).
- Full stops on full sentences (body, helper, errors, toasts with two sentences). None on headlines, buttons, labels, nav or single-fragment toasts.
- Exclamation marks: at most one, celebrations only, never in errors.
- Oxford comma: pick once per product and hold it (default: use it). "and" over "&" outside brand names and tight nav.
- All caps only for ≤3 words, via `text-transform`, with +0.02-0.06em tracking. Never caps for emphasis.

## 18. Numbers, units, dates

| Thing | Rule |
|---|---|
| Counts in UI | Always numerals ("3 files"), 0 decimals |
| Separators | From locale via `Intl.NumberFormat` (en: `1,284`) |
| Compact | `12.4k`, `3.1M` only in tight slots, full value on hover; never in comparison tables |
| Money | Currency symbol per locale, no space in en (`$48`); 2 decimals in tables and checkout, whole prices on marketing (`€240`); code when ambiguous (`US$`, `CA$`) |
| Percent | `12%` in en; 0-1 decimals in UI, 1-2 in dense tables, fixed within a column; points vs percent stated (`+2.1 pts`); an internal score is never shown as % |
| Deltas | Sign on every change (`+4`, `−3`, true minus U+2212 in tables), window in words |
| Units | `&nbsp;` between number and unit (`10 kg`, `45 min`); correct symbols (`ms`, `s`, `km`, `kB`, `MB`); in tables the unit goes in the header ("Duration (min)") |
| Ranges | Unspaced en dash, or "from €140" when only the floor matters |
| Dates | Month names, not ambiguous numerals (`12 Mar 2026`, not `03/12/2026`); `Intl.DateTimeFormat`; 12/24h per locale; timezone on anything scheduled |
| Relative time | "5 min ago" for recent items, absolute date after ~7 days, absolute on hover always |
| Durations, timers | `1 h 20 min` in prose; `01:20:05` in timers with tabular figures |
| Zero / missing | Print `0`; missing is a muted en dash with SR text "No value"; never "N/A"; "Not measured" when the reason matters |
| Alignment | Numbers right-aligned with `tabular-nums`, fixed decimals per column |
| Precision | No false precision; round to what the decision needs |

## 19. Banned words and phrases

- One list for the whole skill: tells.md (Copy and furniture: banned words, banned shapes, performative labels, furniture text, generic CTAs, hedging, emoji). Grep against it in the copy audit.

## 20. Mode notes

- **Persuade:** argument first, 2-line headlines, one supporting sentence, real first-screen action, full content in tight copy. Page structure lives in pages.md.
- **Operate:** trade words, noun titles, terse exact errors, baselines named, no greeting slogans, no marketing voice inside the product. Screens live in apps.md.
- **Read:** headings are linkable and say what the section answers; one convention per element.
- **Experience:** in-play instructions ≤6 words, verb first; reward copy specific and escalating by tier; failure neutral ("Streak ended at 14. Go again"), never punishing; long text skippable. See experience.md.
- **Decks:** titles in one grammatical style, parallel, introduce the slide; no verdict or punchline titles. See decks.md.
- **Page metadata:** pages.md §14; write the title and OG headline in the reader's phrase.

## 21. Copy audit (before calling it done)

- Reread every visible string: headlines, labels, buttons, captions, alt text, footer, errors, toasts, empty states.
- Rewrite anything grammatically broken, with an unclear referent ("we plan to stay that way" with no antecedent), cute-but-wrong, or LLM-thoughtful. When unsure, replace it with a plain functional sentence.
- Competitor test on every sentence; specificity test: every word, number and name belongs to this brief.
- Grep: U+2014, spaced en dashes, banned words (tells.md), lorem, `{{`, `[REPLACE]`, TODO, Acme, example.com.
- At 390px: no headline over 2 lines, no button label over 1 line, no orphans, no overflow.
- Test long names, 0 / 1 / many plurals, billions, 30-40% expansion, 200% zoom.
- Every requested section delivered completely; every sample detail and marked slot listed in the report; no invented proof.
- Final copy is as short as it can be without losing meaning or recovery.
