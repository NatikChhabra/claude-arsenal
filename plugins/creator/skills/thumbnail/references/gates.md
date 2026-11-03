# Thumbnail gates (measured first, then fresh readers)

The rules and numbers each gate checks: skill design, `references/video.md` (§ named per gate). This file is the run
order, the pass marks and the prompts. No gate stands alone: one feed-rank gate alone passed a card the creator rated
0/10 (bright colour fools rankers); T1 + T4 + T10 together sorted all 6 of his rated cards right (video.md §6.6).

## 4a. The measured gate (every variant)
Run the design plugin's checker per variant with its own title and words:
`python <design skill>/tools/still_check.py A.png B.png C.png --as thumbnail --title "<its title>" --words "<its words>"
[--frame <the real frame>] [--vs <the last 8 approved>] [--mock feed.png]` (the feed mock wants the topic's 6 top
thumbnails in `--vs`). Without Python, downscale to 168x94 (suggested) and 246x138 (search) and measure the floors by hand: video.md §1.8 (headline height, words, glyph contrast)
and §1.9 (feed separation, colourfulness, gloss, badge corner, top half, focal regions, elements, subject height).
FAIL = rebuild before any reader sees it; WARN = fix when cheap, say which. A FLOOR, not a CTR predictor: a card the
creator scored 0/10 measured 9.3, because its miss was the idea.
- A feed mock: ours among the topic's 6 top thumbnails, dark and light mode, at 168 px. Ours is never the darkest or
  greyest card.
- AI elements: only per video.md §5.6-5.7; log which element is AI. Never strip an AI provenance label.

## 4b. Fresh readers (each a new agent, image only)
- **U1-U12** (video.md §6.4): ship = every row but U4 >= 7 and the mean of the 11 >= 8.5. U5-U9 come from a second
  reader at 200% (the pasted-element test, §6.2).
- **T1 + T4 blind read:** the 360 px card, one look, the prompt in §6.1. Pass = it names the situation, matches the
  title's promise, names the focal point + a feeling that matches the stakes, and the words land (an opinion, emotion,
  question or number, not an inside phrase).
- **T3 words** (§1.8) · **T5 edges:** no straight erase, no re-typeset or sheared topic UI; look at 200% (§5.2).
- **T10 feed seat + 2x2 = a LOG, not a pass mark.** Calibration: feed readers put all 6 of the creator's rated cards
  (rejects too) in the top 3 of 7, and the 2x2 reader picked all 6 as the amateur. Run once on the 3 final cards: ours +
  the topic's 6 top thumbnails, titles hidden; 3 readers: "This is a YouTube feed. Rank every numbered thumbnail from the
  one you'd click first to the one you'd click last. Reply with the numbers in order only." 1 reader on a 2x2 of ours +
  3 top cards: "One of these four was made by an amateur. Which one? Reply with the number only."
- **T12 click floor (WITH its title, §6.5):** 6 phone cards with titles: ours, the creator's latest rejected card (the
  anchor), 4 role-model hits from a comedy or role-model feed. 3 fresh readers, prompt: "Read this image and nothing
  else: IMAGE. It is your YouTube home feed on your phone. You are <the target viewer, e.g. a 19-year-old who watches
  gaming videos for fun>. You have time to watch exactly 2 of these 6 videos. Which 2 numbers do you click? Then, for
  each of the 6, one short line: what you expect to get from it, and why you would or would not click. Be honest;
  skipping is normal. Answer in exactly this format: CLICK: a, b / 1: ... / 6: ..." Pass = >= 2 of 3 click ours, with
  its incentive sentence written. Beating the anchor is a log only. Never the topic's own search feed (trailers and
  walkthroughs: ours won every time, so it measures nothing). A wrong "what I expect" line = title and picture promise
  different videos.
- **Harsh-scroller critique = the final judge with his pick** (§6.3): 1 fresh agent per card, the neighbour mock at
  168 px + the card with its title. Fix what it names that the incentive and the cut allow; log the 3 lines per card.
- **T11 honest:** the payoff is in the video; the picture is the moment before it, or an outcome that asks "how?".

## Heuristics (fix when cheap, say which failed)
T2 one subject >= 35% of the height (the focal face >= ~50%) · T6 a cut-out is lit (§1.11) · T8 <= 3 elements · T9 it
reads with the bottom half covered.

## Compare with his favourites
Put the creator's best-rated cards next to the set in the same mock: ours must not look cheaper. A new gate or reader
prompt is calibrated on his rated cards first (the rejects FAIL, the favourites PASS).
