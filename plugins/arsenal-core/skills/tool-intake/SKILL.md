---
name: tool-intake
description: Evaluate a tool, Claude plugin, skill pack, MCP server, AI model or GitHub repo for the arsenal and record a verdict. Use when the owner sends a link or a session finds a promising tool.
---
# Tool intake

status: draft

## Steps
1. Identify it exactly: URL, version or commit, licence, maintainer, last release date, platform support (Windows, AMD GPU).
2. List every capability it has. For each: do we already have it (which skill)? would it make our output better or
   save real time at equal quality?
3. Check the deal-breakers: licence forbids public or commercial use; needs NVIDIA-only CUDA with no ROCm/DirectML/CPU
   path; sends private files to a service without the owner's OK; archived and unmaintained; would install anywhere under
   `F:\AI Models\` other than `arsenal\`.
4. Verdict `ADOPT`, `TRIAL`, `WATCH` or `SKIP` (meanings in GROWTH.md). Prefer rebuilding a capability inside our skill
   over a bare copy of someone else's workflow.
5. Record it: one row in `registry/tools.md` (or `registry/local-models.md` for models) with a `recheck` date for
   WATCH/TRIAL; longer notes and sources go in `research/`.
6. If ADOPT or TRIAL, wire it into the matching skill as an option, with the exact install command.

## Row format
`| name | area | what it does for us | licence | runs on | verdict | recheck | source |`
