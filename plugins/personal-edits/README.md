# personal-edits

One skill for private edits made for someone's friends or family: birthday videos, roasts, anniversaries, farewells,
reunion montages. Same bar as a published video, with privacy rules on top: the person's material never leaves the
private project folder.

## Skills
| Skill | Use for | Output |
|---|---|---|
| `personal-edit` | a private edit from photos, chats, voice notes, clips and songs: read everything, beat plan, one-word questions, a 10-20 s preview, full render, blind + design + sound reviews, delivery | master, 1080p and phone (< 20 MB) copies, `<NAME>_<OCCASION>_PLAYBOOK.md` |

Reference: `skills/personal-edit/references/playbook-template.md`, the per-person playbook that makes next year's edit
for the same person start ahead.

## Works with
- The design plugin (**skill design, references/edit.md**) for look, text, motion and sound rules and the design review.
- The video-edit plugin for the render gates and `scripts/job.py` (run long renders detached).

## Privacy
- Keep each project outside any shared repo.
- Never put the person's info, photos, chats or jokes into a shared log, a public page or an outside service.
- Craft lessons go into the shared style log; the person never does.

## Install
```
/plugin install personal-edits --marketplace NatikChhabra/claude-arsenal
```
Or `/plugin marketplace add NatikChhabra/claude-arsenal`, then `/plugin install personal-edits@claude-arsenal`. More options: the [marketplace README](../../README.md).
