---
name: design
description: House design standard, the process, anti-slop rules, exact values and local checkers every visual job follows. Use for writing, restyling or reviewing anything visual (websites, landing pages, apps, dashboards, settings, components, CSS, games, celebrations, 3D, slide decks, prototypes, emails, OG images, claude.ai artifacts), for video work (thumbnails, Shorts/Reel covers, in-video text, overlays, captions, motion graphics, composites, edit feel), and before giving any design feedback. Load it before the first line. Covers type, colour, layout, motion, UX, copy, brand characters, video text and motion, scoring and the ship bar; lint, preflight and a real-browser inspector must pass before work is called done.
---

# Design

status: beta

My house standard for anything people look at: pages, apps, games, decks, thumbnails and video. One rule set, every conflict settled once, checked by local tools before anything is called done.

## Precedence

1. The user's words in this conversation.
2. The project's own brand, DESIGN.md or design tokens. A pinned palette, font or era is honoured even when it matches a tell (neon on near-black included); never add the glow the tell warns about.
3. This skill.
4. Other design guidance loaded in the session (frontend-design plugin, artifact-design). Platform contracts still apply, e.g. an artifact's allowed CDNs and theming rules.

## My standing taste

- No AI slop, ever. That is not "no AI": AI-made images, 3D, video or music ship only when a blind stranger can't tell. Never an AI or TTS voice where a human voice is expected.
- Blunt critique, no flattery.
- Big, dopamine-heavy motion on rewards and celebrations; none at rest.
- One star element per screen. Everything around it stays quiet and readable, but restraint that reads bland ("food without seasoning") is a failure too: give each screen one bold thing with real character.
- No red in UI (apps, dashboards, tools) unless asked. Exempt: thumbnails, photos, album art, brand reaction art, a game's own death or fail screen.
- My own tools default dark: pure black or near-black grounds (`#000`, `#0d1117`, a warm `#0e0d0c`), surfaces stepped lighter, never a lone blue panel. Purple is allowed in my tools when I ask; the purple-blue AI gradient stays banned. Products for other people pick light or dark from the scene (`process.md` §6).
- Show, don't describe. When the direction is open, mock 3 directions on the real screen with real data and send them as screenshots before the full build. I pick, and may combine ("C with B's celebrations"). Mockup first: nothing beyond the mockup changes until I approve, and every change is checked on screen before it is reported.
- Ask in one batch, each question with a suggested default. Never ask what the brief, the files or the recording already answer.

## Pick the mode first

| Mode | Surfaces | Boldness | Motion | Read |
|---|---|---|---|---|
| Persuade | marketing, landing, portfolio, product site | high, one idea from the subject | entrances, 2-3 scroll scenes, one signature move | `pages.md` |
| Operate | apps, dashboards, tools, settings, admin | quiet, dense, ~3% colour, one star element | feedback only, no entrances | `apps.md` |
| Read | docs, articles, long-form | calm, typographic | almost none | `typography.md`, `layout.md` |
| Experience | games, music/learning apps, toys, celebrations, 3D | loud where earned | juice on rewards, ceremonies | `experience.md` |
| Video | thumbnails, Shorts/Reel covers, in-video text, captions, overlays, motion graphics, composites, edit feel | loud, read at phone size, one focal point per moment | eased and weighted, on the hit frame, exits mirror entrances | `video.md`, `edit.md` |

A product site that shows its app is Persuade; the interface fragments inside it follow Operate. An HTML overlay template rendered into video is Video, not Persuade.

## The run

1. **Read the brief and the project.** Subject, audience, the one action, stack, existing brand, real assets. Write a one-line read: "Reading this as: <kind> for <audience>, <mode>, leaning <direction>."
2. **Inventory 8-12 things only this client has:** names, numbers, places, materials, rituals, artefacts, their real data, their own lines. Distinctive design comes from these, not from style.
3. **Ask, if needed:** up to 5-7 questions in one batch, each with a default. Skip anything the brief, the code or memory already answers.
4. **Three directions.** Each differs on a named axis. Idea sentence: "On this page, [thing from the subject] becomes [device]." If the nearest competitor could use it unchanged, it's a category idea; redo it. Direction open and the user present: mock all 3 low-fi on the real screen, send screenshots, let them pick or combine. Otherwise pick the one carrying something only this client has, and say why.
5. **Tokens first:** colour roles, type scale, spacing, radius, motion. A raw value in a component is a second system.
6. **Build still** (motion off): hero or primary view at desktop and phone, then each section or block with real content, then every state (empty, loading, error, hover, focus, active, disabled, selected). Video: the still frame at the moment it must read, at phone size, before any motion.
7. **Gate:** run the checkers (below). Fix every FAIL. Each WARN is wrong unless you can defend it in one sentence.
8. **Look:** open every screenshot or frame and critique it with the passes in `process.md` (Video: the feed test and blind readers in `video.md`). Fix the top 3 problems and re-inspect. Keep iterating while the score rises; stop on plateau or oscillation and report the score as found.
9. **Move:** add the motion layer last (`motion.md`; Video: `edit.md`), then re-gate.
10. **Report honestly:** direction and why, what was checked and at what widths or sizes, scores, sample content to replace. Never claim a check you didn't run.

Redesigns: inspect "before" first, and list what must survive (routes, form field names, data, analytics IDs, SEO slugs, nav labels, legal copy). Keep the stack. A review stops at the critique plus the 3 biggest changes.

## Non-negotiables

- **One focal point per screen** (per moment in video). A stranger gets what it is, who it's for and what to do within 5 seconds; a thumbnail or cover within 1.
- **Type:** 2-3 sizes doing visible work. Display ≥4x body on Persuade. Headline ≤2 lines at every width. Body ≥16px with leading 1.4-1.7 matched to measure (45-75ch). At most 2 families. Use `tabular-nums` wherever numbers align.
- **Colour:** roles as tokens (`--bg --surface --ink --muted --accent --accent-ink`). UI ground 70-90%, accent <5% of any screen and only on the action plus at most one recurring thing. Thumbnails run on colourfulness instead (`video.md`). Body contrast ≥4.5:1, large text ≥3:1, focus and non-text UI ≥3:1.
- **Layout:** one grid, one pair of equal outer margins (≥16px on phone). 2-3 left edges per page. Gaps between sections clearly larger than gaps within. Neighbouring sections never share a layout. No nested cards.
- **Surfaces (web and app):** no decorative gradients, glows, text-shadow, glass cards, resting shadows on Persuade, emoji icons, or fake dashboards made of grey bars. Text over video and thumbnails is the exception: outline, stroke and a hard offset shadow are how it reads (`video.md`).
- **Motion:** animate only `transform` and `opacity` (plus `clip-path`). UI: ease-out for enter and exit, never `ease-in`, ≤300ms. Video: entrances fast-in with a long settle, exits mirror the entrance and run quicker (`power2.in`). Never start from `scale(0)` (use 0.95-0.98). Never animate keyboard actions or anything used 100+ times a day. `prefers-reduced-motion` gives fewer, gentler animations that end in the finished state. Gate hover behind `(hover: hover) and (pointer: fine)`.
- **Characters:** a brand character or mascot is never squashed, stretched or deformed: uniform scale, tilt and move only. Overshoot by weight: character ≤5%, text and cards ≤10%, a snap of ≤5 frames ~16%. No elastic or bounce eases on them.
- **States:** all 8 interaction states, plus empty, loading (skeleton at the real layout, no shimmer, no shift), error (inside the failing block, with what failed and a Retry) and stale.
- **Copy:** specific nouns and real numbers. Buttons are a verb plus an object. Sentence case. No em or en dashes in any visible text. No buzzwords. Never invent proof. No placeholder data (lorem, John Doe, Acme, 99.99%). On-screen words in video are the speaker's exact words or real UI words, never a label explaining the joke.
- **Accessibility:** semantic HTML, a visible `:focus-visible`, full keyboard path, real `alt`, labels above fields, touch targets ≥44px, nothing conveyed by colour alone, works at 200% zoom.
- **Phone is its own composition:** re-author line breaks and crops, use `dvh`/`svh` not `100vh`, no sideways scroll.

## Fast slop scan (any hit means not done)

- Centred hero with a headline, subtitle and two buttons over a screenshot.
- The stock section order: logos → 3 icon cards → testimonial → pricing → CTA.
- An eyebrow label or "New" pill above headings; a line of subtext under every label.
- 01/02/03 numbering on things that aren't a sequence.
- One accent word in italic or colour.
- The cream + serif + terracotta look; near-black + neon/acid accent with glow (unless it is the pinned brand palette, then still no glow); purple-blue AI gradient.
- One 12-16px radius on everything; ghost cards (1px border + big soft shadow).
- Mono "technical" labels; middle-dot meta strings; "Get started" / "Learn more".
- The same fade-up on every block; bounce on UI; infinite pulsing dots; scroll hijacking.
- Dashboard kit: "Welcome back 👋", 4 KPI tiles with icons in tinted circles + green pills + sparklines, rainbow charts, zebra tables.
- Video: a caption that explains the joke or names the edit; preset zoom-and-bounce; a stock whoosh or UI blip; a cut-out pasted with only a generic offset drop shadow; a thumbnail wall of words.

Full catalogue: `tells.md` (Video tells: `video.md`, `edit.md`).

## Ship bar

Every scored row ≥8.5 (8.5 = meets the published spec or the pro reference; `process.md` §10), 0 FAIL, plus a fresh blind review by a reviewer with no build context. Iterate while the score rises; stop on plateau or oscillation and report the score as found, never rounded up.

## References (read the ones the task touches)

| File | Covers |
|---|---|
| `references/process.md` | brief → directions → build → gate → critique passes, scoring rubrics and caps, ship bar, redesign protocol, report |
| `references/tells.md` | complete anti-slop catalogue and banned hexes, words and patterns |
| `references/typography.md` | faces, pairings, scales, display and body rules, loading, i18n, Read-mode docs and articles |
| `references/colour.md` | roles, OKLCH, palettes, dark mode and theming, contrast, status, domain palettes |
| `references/layout.md` | grid, spacing, sections, radius, elevation, z-index, sticky, responsive, units |
| `references/motion.md` | easing, durations, springs, gestures, scroll-driven, reduced motion, libraries, review standard |
| `references/components.md` | IA, nav, forms, buttons and states, overlays, notifications, loading, empty, accessibility, icons, illustration |
| `references/pages.md` | Persuade pages: argument, hero, sections, imagery, video, scroll stories, SEO, Web Vitals |
| `references/apps.md` | Operate screens: shell, KPIs, charts, tables, settings, chat and AI, native mobile, desktop |
| `references/experience.md` | games and game UI, rewards, juice, celebrations, XP and streaks, 3D, canvas, read-at-distance |
| `references/video.md` | Video mode: thumbnails, Shorts/Reel covers, captions and overlays, composites, feed tests, blind readers |
| `references/edit.md` | Video mode: motion for video, camera, sound feel, music levels, film look, video QC |
| `references/copy.md` | headlines, CTAs, errors, empty states, app words, formatting |
| `references/systems.md` | brand identity, brand characters and app icons, tokens, DESIGN.md templates, brand-system lessons, brand library fetch, style by domain |
| `references/decks.md` | slides, prototypes, presenting variations, email, OG images, print |
| `references/tools.md` | checker commands, flags, what they check, when to use which |

## Gate commands (run from the project root)

```bash
node ${CLAUDE_SKILL_DIR}/tools/taste/lint.mjs <files|dirs> [--app|--video]   # static anti-slop scan
node ${CLAUDE_SKILL_DIR}/tools/preflight.mjs <files|dirs> [--video]          # em dash, focus, z-index, scroll listeners
node ${CLAUDE_SKILL_DIR}/tools/taste/inspect.mjs <url|index.html> [--app|--video] [--widths 1440,768,390|1920x1080]   # real Chrome: measures + screenshots
```

Use `--app` for Operate screens and `--video` for HTML that renders into video or thumbnails (or set `"kind"` in `.design-check/direction.json`). The inspector writes to `.design-check/inspect/` in the project: open every screenshot it lists, then delete the folder (or gitignore it) when done. The checkers encode a strict house taste. A deliberate exception gets a `design-ignore` comment (the old `taste-skill-ignore` still works) and a one-sentence reason in the report. Rendered video and stills are judged by the frame checks in `video.md` and `edit.md`. Details in `references/tools.md`.
