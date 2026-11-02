# design

One house design standard for everything people look at: web pages, apps, dashboards, games, 3D, decks, emails, OG
images, claude.ai artifacts, thumbnails, Shorts and Reel covers, in-video text and edit feel. One rule set with every
conflict settled once, plus three local checkers that must pass before work is called done.

## Skill
| Skill | Use for |
|---|---|
| [`design`](skills/design/SKILL.md) | before writing, restyling or reviewing anything visual, and before any design feedback |

The skill picks a mode (Persuade, Operate, Read, Experience, Video), runs a 10-step process (brief, inventory, three
directions, tokens, still build, gate, look, motion, report) and holds a ship bar of every scored row at 8.5+ with a
fresh blind review.

## References (`skills/design/references/`)
| File | Covers |
|---|---|
| [process.md](skills/design/references/process.md) | brief to report, critique passes, scoring rubrics, ship bar, redesigns |
| [tells.md](skills/design/references/tells.md) | the anti-slop catalogue: banned hexes, words and patterns |
| [typography.md](skills/design/references/typography.md) | faces, pairings, scales, loading, long-form reading |
| [colour.md](skills/design/references/colour.md) | roles, OKLCH, palettes, dark mode, contrast, status colours |
| [layout.md](skills/design/references/layout.md) | grid, spacing, sections, radius, elevation, z-index, responsive |
| [motion.md](skills/design/references/motion.md) | easing, durations, springs, gestures, scroll, reduced motion |
| [components.md](skills/design/references/components.md) | navigation, forms, states, overlays, loading, empty, accessibility |
| [pages.md](skills/design/references/pages.md) | marketing and landing pages, hero, imagery, SEO, Web Vitals |
| [apps.md](skills/design/references/apps.md) | app shells, KPIs, charts, tables, settings, chat UIs, mobile |
| [experience.md](skills/design/references/experience.md) | games, rewards, juice, celebrations, streaks, 3D, canvas |
| [video.md](skills/design/references/video.md) | thumbnails, covers, captions, overlays, composites, feed tests |
| [edit.md](skills/design/references/edit.md) | motion for video, camera, sound feel, music levels, film look, QC |
| [copy.md](skills/design/references/copy.md) | headlines, buttons, errors, empty states, formatting |
| [systems.md](skills/design/references/systems.md) | brand identity, brand characters, tokens, DESIGN.md templates |
| [decks.md](skills/design/references/decks.md) | slides, prototypes, email, OG images, print |
| [tools.md](skills/design/references/tools.md) | checker commands, flags and what each one checks |

The other plugins in this marketplace point here for every visual, motion and sound rule instead of repeating them.

## Checkers (`skills/design/tools/`)
```bash
node tools/taste/lint.mjs <files|dirs> [--app|--video] [--json]       # static anti-slop scan
node tools/preflight.mjs <files|dirs> [--video]                       # dashes, focus, z-index, scroll listeners
node tools/taste/inspect.mjs <url|index.html> [--app|--video] [--widths 1440,768,390|1920x1080]   # real browser
```
- Node 22+. The inspector drives a local headless Chrome, Edge, Brave or Chromium over CDP; set `CHROME_PATH` when none
  is on the usual paths. It writes `.design-check/inspect/` in the current folder: gitignore it or delete it after.
- None of the checkers call the network.
- `preflight.mjs` and `taste/` are third-party MIT code, modified here; their licences sit beside them and in
  [NOTICE.md](NOTICE.md).

## Install
```
/plugin install design --marketplace NatikChhabra/claude-arsenal
```
Or `/plugin marketplace add NatikChhabra/claude-arsenal`, then `/plugin install design@claude-arsenal`. More options: the [marketplace README](../../README.md).
