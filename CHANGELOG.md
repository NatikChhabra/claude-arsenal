# Changelog

## Unreleased
- design: new `video.md` §7 on single and album covers, learned on a guitar-only instrumental where two code-drawn
  covers (a photoreal render and a three-ink screen-print look) both scored 5/10 with fresh blind readers. It covers
  the store rules (3000x3000, words match metadata, no handles or logos), why a real photo of the artist's own thing
  beats a scanned hand-made mark and both beat code, a five-minute phone shot list (a ringing string draws its own
  wave through rolling shutter), the waveform cliché, title type that reads at 180 px, and the blind prompt. New
  `tools/song_shape.py` (numpy + ffmpeg, selftest in CI) writes a track's loudness shape and inner silences as JSON,
  with the silences held flat and eased so a drawn line never zig-zags at a drop bar.
- music-studio: guitar-capture "record once" learns from the first real takes, which ignored the click (free tempo,
  one file per part). The parts are re-played hit by hit from his own take, each note and strum placed on the grid,
  with Rubber Band only for slices that end too soon. Also: strum boundaries, note substitution from other bars,
  left/right doubles and a chuck percussion stem from his own hits, and how to fix a dark soundhole pickup (hiss
  above 5 kHz, presence EQ, exciter, spline the clipped chucks). mix-master targets: the ffmpeg AAC spike also
  appears on 48 kHz / 24-bit sources, at limiter flat tops.
- music-studio: guitar-capture "record once, loop the rest" for a player who wants to play each part one time. New
  `tools/loop_assemble.py` (numpy + soundfile, selftest in CI) finds every part in one take recorded to a click track
  (shared offset for the whole take, then each part and each bar to the millisecond), places the bars on the song
  grid with a 25 ms pre-downbeat crossfade, keeps the recorded ring at a part's end, layers a melody part over a
  chorus, and fails on a weak match, more than 0.5% drift from the click, clipping or a quiet take. First use: 7
  four-bar parts (28 bars played) built a 77-bar song; tested before recording on a plucked-string render of the
  record track with human timing (every bar within 18 ms of the grid, no gaps at loop joins, the drop bar silent).
  A 25-case stress run plus 30 random takes then found and fixed an eighth-note slip on players 0.4% off tempo and
  a roll bar locking onto a later string, and added checks for click in the mic, missing or wrong parts, missed
  notes and a bar over 70 ms off. mix-master targets: ffmpeg AAC encode-check spikes on 44.1 kHz float input.
- music-studio: `gear-pick` lessons from finishing the same purchase: ask whether he wants preset saving and app
  control (it beat a cheaper amp with the same USB recording), name the computer cable (micro-B vs USB-C, in the box
  or not), add a "how it connects" line because a beginner thought the amp's line-in jack sends the guitar to the PC
  (and call the 1/4" cable "the guitar cable", since "1/4 inch" alone read as an adapter to buy), spend the shared
  hourly web-fetch budget on finalists only, and Bajaao's "Used Gear" links are a separate used marketplace.
- advocate: new `cell-rep` skill (beta). Built while a public defender was live in a station: speed rules first (one short
  reply in under a minute, at most one question, trust what the user sees in game over a wiki that missed a real station),
  the in-cell card (intro, what to get, element and stacking checks, bail and plea options, the court's own clocks,
  AI-filing guard), and how to keep a live-answer helper permanently in cell-rep mode (saved cases labelled background,
  since an "active case" label leaked one case's facts into unrelated reps; one-shortcut launch; restart only the helper).
- advocate: `trial-prep` learns from the second round on the same case. The playbook is organised by job (how we win,
  their points and our answers, one page per witness with that witness's objections beside our questions, the closing
  as a full speech, exact words for each verdict), and a blind review runs before delivery (it caught a misstated
  co-defendant sentence, leading questions on our own witness and closing lines that contradicted our own cross).
- marketing-studio: `social-copy` gets a LinkedIn row (first two lines carry the result with a number, short
  paragraphs instead of emoji bullets, zero emoji, 3 hashtags at most). Learned when the owner rejected a launch post
  that read as AI because of emoji bullets and a "What I learned" list; the rewrite passed `copy_lint` and a blind read.
- design: new "Spreadsheets, ledgers and record books" section in `apps.md` (blank-safe running balance, money at the
  right edge, frozen header block with totals, brand at ~3%, dropdowns and amber mistake flags, SUMIF links between
  tabs, Google Sheets "Replace spreadsheet" import that keeps the share link). Learned rebuilding a business
  transaction sheet whose first balance cell read the header (`#VALUE!`) and whose filler formulas showed 0 down every
  empty row.
- music-studio: guitar-capture §0, measure the player before writing his part. A guessed beginner part was called
  "sub par"; asking 9 level questions and measuring a minute of songs he already plays fixed it. New
  `tools/guitar_level.py` reads tuning (cents), clipping, notes per second, steadiness, picked vs strummed, range and
  hesitations per stretch of playing (selftest in CI; on a real 73 s take it found a 30 s clean run at 5.2 notes/s and
  a guitar 6-12 cents flat). §0 also lists moves that sound big on open shapes (harmonics, hammer-on tune, thumb on
  every beat, chucks, a silent drop, slap + chuck groove), a relative-major ending for a lift, and the one-sheet format.
- music-studio: a vocal route for an owner who wants his own real voice on the record. New Route F in
  vocal-route (melody written into his measured range, talk-sung verses, close dry recording, comp for feel, light
  pitch correction, doubles; a listener who hears tuning fails it like one who hears AI). New `tools/voice_range.py`
  measures a voice from any take (pYIN), estimates the comfortable range from speech or measures it from a sung take,
  fits a melody to it with a capo or the shapes a fourth lower, and flags clipped takes (selftest in CI). First use: a
  song's chorus peak moved 3 semitones down from a spoken take before any guide was recorded. song-from-idea §4 step 0:
  when the owner brings his own lyrics, keep his sentences and fill gaps only with his answers (a polished rewrite with
  invented details read as AI to him). mix-master §1: check raw takes for a dead channel and low input level
  before processing. Route F steps 8-9: never tune a melody-less chant (it read as a robot), and build the hook as a
  short tune on his own title line, taught with a looped hook track first. Route D: offer "talk it" as a real choice to a non-singer. produce-arrange:
  the stitched-backing stopgap for loose takes, and why a played-through take is the next ask.
- music-studio: a demo that passed every gate was rated -1 ("missing everything"), so gates now cover the arrangement.
  music-review: an "Arrangement built" gate (every energy-map layer present; chorus 2+ dB over verse, last chorus
  loudest, bridge 3+ dB under) and a click scan, plus the rule that gates never mean "good". New `tools/vocal_comp.py`
  (no AI): `double` lines up another take of the same line with the lead (DTW + Praat PSOLA; onset correlation 0.2 ->
  0.5-0.85 on a real untrained voice) and `nudge` moves only sustained notes toward the chord, capped at 1 semitone
  (selftest in CI). vocal-route Route F steps 10-11: doubles and nudges from the takes already on disk, and a declined
  AI voice stays declined. produce-arrange: a no-DAW band from CC0 sample libraries (VSCO 2 CE, Swirly Drums) with
  pitch-label checks, grid placement of free-time vocal lines, and the low-mid and click fixes found in the mix.
  guitar-capture: a play-along with his own voice in it, and beginner parts to ask for (play-through, one-finger riff,
  body taps as the drums).
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
