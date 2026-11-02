# Claude Arsenal

Natik's personal toolkit of Claude Code skills, plugins, MCP servers and local AI tools.
It is built to grow: every project and side project that uses it should leave it a little better.

**Current focus:** music making, music videos, design and marketing.
**Status:** groundwork. The structure, rules and research are in place; most skills are `draft` and get filled in as real work starts.

## Install (any project, any machine)

The repo is a Claude Code plugin marketplace.

```
/plugin marketplace add NatikChhabra/claude-arsenal
/plugin install music-studio@claude-arsenal
/plugin install design-studio@claude-arsenal
/plugin install marketing-studio@claude-arsenal
/plugin install arsenal-core@claude-arsenal
```

Restart Claude Code afterwards. `/plugin` lists what is installed.

## What is in here

| Path | What it is |
|---|---|
| `CLAUDE.md` | Rules every session follows when working in or with the arsenal (read first) |
| `GROWTH.md` | How the arsenal improves itself: the intake loop, verdicts, versioning |
| `plugins/arsenal-core` | Skills for maintaining the arsenal itself (`arsenal-update`, `tool-intake`) |
| `plugins/music-studio` | Songwriting, vocals for a guitarist who can't sing, production, mixing, music videos |
| `plugins/design-studio` | Posters, brand kits, social graphics for RP characters and businesses |
| `plugins/marketing-studio` | Campaign plans, launch rollouts, social copy |
| `registry/` | Every outside tool, plugin, MCP server and model we looked at, with a verdict |
| `research/` | The research behind each verdict, with sources |
| `templates/` | Starting points for a new skill or plugin |
| `scripts/validate.py` | Structure check, run locally and in CI on every push |

## Golden rules (full list in CLAUDE.md)

1. Never break what already works. Additive changes, on a branch, through a pull request.
2. Every tool we adopt gets a registry row with a verdict and a reason.
3. No AI slop: anything that ships must not read, look or sound machine-made.
4. The owner's other repos are read-only references. Nothing here writes to them.
