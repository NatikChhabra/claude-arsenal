# Changelog

## Unreleased
- advocate (new plugin): `trial-prep` skill (beta, first used 2026-11-08 as defense second chair on a 20-count
  felony case). Builds a prep pack from the case file and the court's own law: deadlines from the judge's order first,
  charges and elements (including whether accomplice liability reaches attempts), timeline, weak points per count,
  evidence and discovery list, theory, cross banks, objections, chair duties. Records two traps from that case: court
  forums need the user's signed-in browser (read long DOM text in ~900-character slices), and the judge must come from
  the docket, not from a prior case with the same parties. Ethics guard: preparation only, never AI-written filings.
- music-studio: new `gear-pick` skill (beta) for buying an instrument or gear setup: questions once, his real
  listening history instead of a typed song list, the whole-setup budget (an electric needs an amp or an ASIO interface
  plus a cable), prices read on product pages (store search cards show stale prices), and one pick, never tiers. New
  `tools/listening_taste.py` reads the songs he plays from a Feishin player cache (play-queue JSON plus the Snappy and
  V8 query cache; LevelDB .log records rejoined across blocks and .ldb tables decoded, so the queue survives a
  compaction; Latin-1 and UTF-16 strings read as stored; stdlib only, selftest in CI). On a real cache it listed 54
  songs with play counts. Registry: Guitar Rig 7 Player (TRIAL). From a real purchase where two tiered answers were
  sent back with "give me one guitar", and where a strap and cable added at the end flipped the pick.
- research: `author-ownership` gains a one-sitting version (Introduction, Limitations, Conclusion and contribution
  statement, three questions each), "fix the reason, keep the point" with numbers read from result files, and a rule
  never to write an author's overclaimed contribution: check it against the git history, the paper's disclosure and
  what venues were told. From a real session where the author's first answer overclaimed and three venues already
  knew the AI's role.
- design + video-edit: the spoken launch ad. New `ads.md` section 9 (one scene per spoken claim, the problem as an object,
  a signed quote to prove a boast, the number built in step with the voice, and nine craft rules each taken from a blind
  reviewer's note: visible motion, no hard zooms, ghost-then-fill numbers, one caption baseline and plate, offer
  margins, badge placement). New `tools/scene_frames.mjs` renders a page with `render(t)` plus a cue file to exact
  frames and an mp4. New `video-edit/tools/vo_bestof.py` builds one VO from the best take of each line with word times
  for captions (selftest in CI; reproduced the real launch-ad cut to the millisecond). `pages.md`: a price calculator
  that shows the discounted deposit, shared plan terms said once, gallery reveals after decode, and tap-to-copy contact
  with no app hand-off. Over three blind rounds the ad went from about 7.2 to 7.6-8.4 and the site from 7.8 to 8.0.
- design: ads that pass every meter can still "feel AI". New `ads.md` section 8 (build the poster as a physical sheet,
  cut the client's assets from their old piece, break symmetry, one light and a lifted corner, handwriting that never
  repeats a glyph, pressed stamps, the stranger "which parts look AI" read) and a sample-watermark rule: owner name
  tiled over the whole piece, drifting per frame in loops, metadata, clean master kept apart. New `tools/paper_kit.py`
  (sheet, tape, stamp ink mask, tiled watermark; deterministic; selftest in CI). On the BBQ hiring poster the blind 2x2
  picked the business's old GIF as the amateur one, and still_check scored the new piece 8.9.
- design: after a BBQ hiring poster was sent back as "low effort AI", the design skill now covers ads properly.
  New `references/ads.md` (business inventory first, one vernacular from the business's world, one line and one
  subject, real over generated, one motion the place owns then a long hold, in-game placement, a 5-step review) and an
  "Ads, posters and animated loops" block in `tells.md`. The skill's description and mode table now name posters,
  hiring and business ads, in-game/RP signs and GIF loops, so it loads for them. New `tools/still_check.py`: the pixel
  gate for any finished still or loop at its real viewing size (thumbnail, ad, ingame, cover, story profiles): headline
  size, fine print, word wall, glyph contrast, one subject, clutter, AI gloss and palette, AI provenance, sameness,
  faked platform UI; animations add WCAG flashes, particle fields, whole-frame motion, the loop seam and the upload
  budget. Generalised from the owner's proven thumbnail gate (calibrated on 290 real cards). On the rejected poster it
  scored 4.9: a 58-word wall FAIL, plus particle field, fine print, no subject, text on text and AI provenance WARNs.
  creator `thumbnail` gates now run it instead of "if the project has a checker".
- video-edit: new `tools/watch.py` (the watch pack: a whole render as one time-aligned text timeline with DEAD,
  OVERLOAD, STEP, UNCUED, FLASH, FROZEN, SILENCE and, with a beat map, OFFBEAT flags, plus contact sheets for the worst
  windows) wired into roughcut gates, creator final-review and music-studio music-video; new `scripts/lut.py` (our own
  film LUTs), referenced from design edit.md and music-video. Both rebuilt from the owner's working edit pipeline as
  standalone tools.
- CI also runs the still_check, watch and beatmap selftests (closes the beatmap gap noted below).
- workflow: new `android-adb-drive` skill (beta, used for real on 2026-11-03) with `scripts/adb_drive.py`: taps only when the
  app owns the screen and no notification banner is down (two real mis-taps started a call and opened an SMS), saves and
  restores the settings it changes, lists the screen as tappable labels. Stdlib; `--selftest` runs without a phone.
- `scripts/validate.py` now runs the `--selftest` of every stdlib script in `plugins/*/scripts/` (adb_drive,
  redact, skill_lint), so CI covers new scripts without a workflow-file edit. `music-studio/tools/beatmap.py` has a
  selftest that no CI step runs yet (it needs numpy, librosa and soundfile): add it to the ffmpeg step when convenient.
- workflow: new `pre-report-secrets-scan` skill (draft, the owner's own) with `scripts/redact.py`, a stdlib first pass that
  reuses `secret_guard`'s key patterns, adds report-only shapes, never prints a value and rescans its own output. CI runs
  its selftest.
- music-studio and marketing-studio rebuilt to the arsenal's bar: all 10 skills rewritten as full workflows with gates,
  references and review rubrics, from 3 new research files (182 sourced, tagged claims: vocal tools 2026, production
  and video, release marketing). New tested tools: `lyric_lint.py`, `loudness.py` (with the phone-speaker vocal check),
  `beatmap.py` (beats, bars, sections, cuts on grid), `rollout.py` (release calendar), `copy_lint.py`; `templates/SONG.md`.
  Registry music section rewritten (38 rows, new Distribution section). CI now also runs skill_lint, the hook tests and
  the stdlib tool selftests, as CLAUDE.md already said it did.
- New `research` plugin (beta, from one real paper release): `paper-release` (Zenodo software and preprint DOIs,
  ORCID incl. DataCite auto-update, Google Scholar, LinkedIn, arXiv endorsement, under-18 consent and CS review-paper
  rule), `research-outreach` (researchers, venues, press, with follow-up rules) and `author-ownership` (building the
  author's own understanding and contribution when an AI agent did much of the work). workflow gotchas: a
  "Connectors" section on the Gmail connector rewriting draft links and how to fix and verify them.
- design: `tools/taste/motion.mjs`, a zero-dependency motion film. It plays a page on a virtual clock (timers, rAF, CSS and
  Web Animations driven together), photographs it at a fixed frame rate with keys or scripted moves on cue, and writes
  time-stamped contact sheets plus an old-TV view (`--tv`). Documented in tools.md and motion.md §14.
- design: rules proved on a TV launcher built with the skill: the cut-edge rule for cut-out characters (SKILL.md), web
  launchers on TV sticks, canvas particles on weak devices, impacts that reach small speakers, the user as the cause of
  the biggest moment (experience.md), per-keyframe easing for scheduled effects (motion.md), briefing sub-agents and
  valid review packs (process.md §8b), clean cut-outs from video (video.md §1.11b).
- creator: reference-study's yt-dlp download carries the EJS flags YouTube now needs. registry: rembg + BiRefNet, yt-dlp EJS.
- Merged the design, creator, video-edit, personal-edits, study and workflow plugins. design replaces design-studio
  (its brief, brand kit, sizes and HTML-to-PNG method folded into design references); workflow absorbs arsenal-core
  (`arsenal-update` skill, tool verdicts in `tool-change`). Versions dropped, `status:` on every skill; the validator also
  checks dashes, long descriptions and banned names in more file types; CI also runs skill_lint and the hook tests.
- Groundwork: marketplace manifest, four plugins (arsenal-core, music-studio, design-studio, marketing-studio) with draft
  skills, tool registry, research notes (vocals for non-singers, music tool landscape, design and marketing skills,
  patterns to reuse), skill template, structure validator and CI.
