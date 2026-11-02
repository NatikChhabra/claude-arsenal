---
name: release
description: Release a finished, creator-approved video package end to end - stage the finals in one upload folder, schedule the long first and every Short after it in YouTube Studio and the Reels in Meta Business Suite through the browser, set related videos once the long is public, read every value back after a reload, then the bookkeeping, cleanup and post-mortem. Use for "upload", "schedule it", "release", "put it in the upload folder", "post the reels".
---

# release <ep>

status: beta

Run it end to end once the creator said "upload". He never repeats a step or an approval.

## Talking to him
- No progress updates. ONE message at the end: each item, its link, its date + time (in his time zone), as bullets.
- His "upload" + the dates in the plan he already approved = the OK for every step below. Write them into the plan; do
  not ask again. If a permission system still refuses a publish step, ask ONCE, in one line, with the exact sentence he
  can paste (naming every action + date).
- A real blocker = one line with the exact fix. Never send him setup steps you can do yourself.
- Never log in, enter a password or accept terms for him: those are his clicks.

## 0. Before
- The day before the slot: the upload account is signed in (if the project has an uploader, run its account check).
- His OK stamped on the long + every Short and Reel (skill `final-review` 5).
- A score under 8.5 ships only on his own override with his words on that sheet; it waives score rows only, never a
  missing score, the thumbnail/cover tests, the click floor or the safe zone.
- Skill `growth-gate` once more on the final package and its links.

## 1. Stage (the moment it is final)
The finals live in ONE upload folder per video (for example `UPLOAD/video<N>_<ep>/`, in the main project checkout, not a
worktree copy): the long, each Short, `thumbnails/` (A/B/C), `reel_covers/`, the caption file, and one upload sheet in
Studio's click order (every title, description, caption, tags, playlist, cover, end screen, card, date). Each file passed
QC on that exact file. Never cleared, never a second copy elsewhere. If the project has a staging tool, it stages at
review-ready and re-stages after his OK; a stop hook that blocks while an approved final sits outside the folder keeps
it honest.

## 1b. Text (the upload sheet)
Written by skill `publish-meta` (one sheet for the long, one per Short and per Reel) and copied into the upload sheet:
the store link in full, 3 title + thumbnail PAIRS, the Reel caption = store link + 5 tags only, any line the publisher's
video policy requires, every CC BY credit line verbatim, the caption file (romanised if that is how the audience reads).

## 2. YouTube (in Studio through the browser; never an API publish call)
- API uploads from an unaudited app are locked private, so Studio is the way. Claude uploads whatever the creator
  hands over; some creators drop the long themselves: ask once what he does, then remember it.
- Getting a file into Studio when the browser automation caps uploads (Chrome's file upload refused > 10 MB per call,
  and a page fetch from a localhost server hung on the local-network prompt): `split -b 9000000 -d -a 3 <file>
  <scratch>/chunks/<k>.`; in the Studio tab add an `<input type=file id=claude_probe>` with a change listener that keeps
  each part by name; one upload call per part (parallel calls are fine); then `new File(parts sorted by name,
  "<name>.mp4")`, check its size against the source, and set it on Studio's `input[type=file]` via a DataTransfer + a
  change event. No page reload until every upload is done: the parts live in the page. A long gets an upload copy
  first (x264 `-crf 18 -maxrate 24M -bufsize 48M`, audio copied: 880 MB for 5 min of 1440p60, SSIM 0.97 against a 55
  Mbps master), about 100 calls instead of 240.
- Studio habits that stuck: hook `HTMLInputElement.prototype.click` before any "Upload file" (else a native picker
  opens on the creator's screen); for schedule time open the time field and click the list item (typed time doesn't
  stick); for the date type it as "Oct 30, 2026" + Enter in the picker's input. Test & Compare (3 pairs) is set at
  upload and shows "Ineligible: not public" until the long is public. Captions: Languages > Upload manual; the caption
  file must sit inside the session's working directory.
- Per item: title, thumbnail (+ Test & Compare A/B/C), description, tags, playlist (the topic playlist), language
  (video + audio), captions (Languages > upload), end screen (the next video on that topic/premise if one exists, else
  the best performer by APV, + Subscribe, never over the mascot), card. The sheet names the end-screen target by its
  11-character video id, never prose.
- Short cover: custom Short thumbnails are partner-programme + desktop only. If Studio's Short > Details > Thumbnail
  shows "Upload file", upload the designed 1080x1920 cover; else click the suggested frame nearest its `cover_at`. None
  of them is it: the creator sets it on his phone (YouTube app > You > Your videos > the Short > three dots > Edit >
  thumbnail pencil > drag to `cover_at` > Save), the one step to ask, once, with the timestamp. Read it back after a
  reload (Studio > Content > Shorts).
- Visibility: read what is set first, never overwrite a schedule he set. Schedule after Studio's Checks (copyright + ad
  suitability) pass. Slots from the channel's own analytics: the long first; the first Short ~30 min after the long's
  public time; the rest inside the long's first 7 days.
- **LONG FIRST:** no Short or Reel is scheduled before the long goes public (Shorts that sold an unlisted long sent 0
  Shorts-feed views to it). Every Short + Reel date >= the long's public time + 30 min. A long he keeps unlisted to
  watch first gets its public date from him first.

## 3. Reels (Meta Business Suite through the browser)
- Instagram's API can't schedule Reels; Business Suite can (Create reel). If the project has a Reel uploader, its dry
  run is the caption + QC gate only.
- A < 10 MB copy when the browser caps uploads, in scratch, deleted after the post (no second final):
  `ffmpeg -y -i <short>.mp4 -c:v libx264 -b:v <kbps>k -pass 1 -an -f null NUL` (`/dev/null` off Windows), then the
  same with `-pass 2 -c:a copy <tmp>.mp4`, `<kbps>` = 9.5 MB * 8 / seconds - audio kbps; check
  `ffmpeg -i <tmp>.mp4 -i <short>.mp4 -lavfi ssim -f null -` >= 0.99.
- Caption from the sheet; cover = the designed cover via Upload image (else the `cover_at` frame); Schedule (24 h clock):
  the first Reel the evening of the long's day, the rest at the evening peak on days without a Short. Meta AI
  translation OFF (confirm once, log it).
- The whole Reel inside ONE page load (a reload drops the file hook and can open a native picker).
- Type the caption as keystrokes, hashtags LAST with a trailing space (scripted text insertion broke the composer; a
  caption ending on a link lost its tail to hashtag autocomplete). Read the caption back after the cover is set.

## 4. Related video (after the long is PUBLIC)
Studio's picker lists only public videos: right after the long goes live, set each Short's related video = the long,
reload, read it back, log the long id + the reload time. If the session will be gone by then, schedule a check-in.

## 5. Verify (a change counts only once it stuck)
Reload Studio + Business Suite from scratch and read every value back by the sheet's checklist:
- Long: title + Test & Compare pairs, thumbnail, description, tags, playlist, languages, captions, chapters shown, end
  screen, cards, visibility + date.
- Each Short: title, cover, description, playlist, related video, date. Each Reel: caption, cover, Meta AI translation
  off, date.
Log each item + "verified after reload <time>". A value not seen after a reload is not done: say what he should check.

## 6. After
- Write the bookkeeping: every video id, the release date and how, per sheet (`"released"`, or `"held": "<why>"` for a
  cut that never goes up), and the retro dates (day 1, 3, 7) in the project's hand-off file. If the project has an
  after-upload tool, run it (it re-reads every field; DID NOT STICK = fix it).
- Cleanup: drafts and intermediates go now; raws only once the Part 2 decision is settled (ask once before raws go);
  finals, screenshots and stills stay forever. Remove this video's copies from stale worktrees. Use the recycle bin,
  never a permanent delete.
- Update the project's hand-off, the video's brief and the creator's dashboard; commit and push if the project uses git.

## 7. Post-mortem (the day the release is verified, unasked)
List every miss the blind reviews, QC and his notes caught between the FIRST cut and the final (for example a menu
opening, an off-screen payoff, 22 voiceless spans > 5 s, garbled captions). For each: which check, tool or skill step
would have caught it before review; then build it, so the next first cut starts near the bar. Log the list + each fix
in the video's retro file under `## Post-mortem`. Include what the creator named himself (one release's: Shorts never
had designed covers, so every Short now ships a 9:16 cover + a `cover_at` frame, checked like the long's thumbnails).

## Traps
- Permission filters refuse API publish calls and relayed approvals: use the browser and the one approval line.
- Keep the project's settings files valid after any edit (a missing comma breaks every session).
- A worktree session stages into the main checkout's upload folder, never its own.
