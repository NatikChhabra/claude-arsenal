# marketing-studio

Campaign plans, release rollouts and per-platform copy in the brand's or character's own voice, built on sourced
platform rules (research/05_release_marketing.md) and two tested tools.

| Skill | What it does |
|---|---|
| `release-rollout` | Releasability gate (rights, distributor AI policy, artist identity), dated calendar with Spotify's floors, assets, pitch, read-outs |
| `social-copy` | One version per platform, a concrete fact in every piece, 3 options and a pick, copy_lint and a blind reader |
| `campaign-plan` | Goal with a baseline, audiences by why they care, one message and 3 angles, channels in and out of the server, decisions per read-out |

Tools (`tools/`, stdlib only, each has `--selftest`):
- `rollout.py <release-date>`: the dated calendar; FAIL when the 7-day pitch and delivery floor is already missed.
- `copy_lint.py <file> --platform <p>`: dashes, the design plugin's banned words and shapes, platform limits, no-fact
  and hashtag/emoji/caps warnings, follower bragging in pitches.

Brand kits come from the `design` skill (references/systems.md). Nothing posts without the owner's OK for that post.
All skills are `status: draft` until used on a real launch.

## Install

```
/plugin install marketing-studio --marketplace NatikChhabra/claude-arsenal
```
