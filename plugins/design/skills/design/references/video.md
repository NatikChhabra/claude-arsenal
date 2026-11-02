# Video packaging: thumbnails, titles, covers, on-video text, composites, blind reads

Use when: making or reviewing a YouTube thumbnail, a title + thumbnail pair, a Shorts or Reels cover, any 9:16 frame, text burned into video, a photo composite or cut-out, or when measuring whether packaging works. Edit feel, motion, camera, sound, captions-as-words, film look, QC and video slop tells live in `edit.md`.

Scope and overrides. These rules are for fixed video canvases (1280x720, 1080x1920, 1920x1080 frames), not web pages. Where they differ from the web references, the video rule wins on video:
- Text over footage and thumbnails takes a hard ink outline and a hard offset shadow (§4). The web bans on `text-shadow`, stroked display text and drop shadows (SKILL.md Surfaces, tells.md Glow) do not apply to video text.
- One soft vignette and one 1-2% grain pass are part of a composite's finish (§5). The web grain and vignette ban (tells.md, pages.md) does not apply.
- Red is fine in thumbnails, a game's own death screen and brand reaction art. "No red" is a UI rule.
- The colour split "ground 70-90%, accent under 5%" is UI only; thumbnails need colourfulness (§1.9).
- decks.md's cover and thumbnail rows are summaries; the full rules here win: covers use the §3 bands, thumbnails are judged at 168x94 and 246x138, never at 320 px.
- A pinned brand palette (for example neon on near-black) is identity, not the "dark neon" tell. Never add glow to it.

## 1. Thumbnails

### 1.1 Start from one click incentive
Before any pixel, give each card ONE incentive and write the sentence a stranger would say about it (6+ words, a verb + an open outcome, true in the video with its timestamp). Three cards = three different incentives.

| Incentive | The stranger's sentence shape |
|---|---|
| Humiliation with a score | "he lost 40 times to a goat" |
| An absurd "how?" | "how is a fridge driving the bus" |
| A known thing in a new state | "the final boss is now his pet" |
| A rule or challenge | "he can only use the frying pan" |
| Danger with an open outcome | "the dragon is about to eat him" |
| Reward or money | "he sold a rock for 90,000" |

- Find it in the creator's own words. Read the video's whole caption file start to end and list every line with a number, a confession, a rule or an absurd act. The monster or spectacle is only the stage.
- After a rejection, change the INCENTIVE, not the frame or the caption. List every rejected card (moment + reaction + words) before building. The same creature shown 5 times with new captions read as one card.
- One template (a monster moment + a reacting character + a caption) across 9 takes was skipped every time: no incentive, no click.

### 1.2 One audience per card
- Name the video's 3 audiences by WHY they would watch: fans of someone or something famous in it, genre viewers who do not know this game, comedy seekers who do not care which game. Give each card one. Never three cards for the same audience.
- YouTube's per-segment thumbnail serving (announced 23 Sep 2026 as coming soon) serves each segment the best of 3; Netflix per-viewer artwork lifted its core metrics.

### 1.3 Which hooks win, measured within channel
Each channel's winners minus its own flops (winners >= 2.5x own median Hindi, >= 2x Western; flops <= 0.6x), 208 Hindi let's-play cards from 59 channels and ~110 Western comedy cards from 14, blind coders, 90% bootstrap CI. Bold = CI clear of zero.

| Feature | Hindi | Western |
|---|---|---|
| A stranger gets it in 1 s without knowing the game | **+15** | **+14** (the one finding that replicates) |
| A number on the card | **+15** | +4 |
| A famous thing (face, character, logo known on sight) | **+12** | **+7** |
| A strong felt focal point | **+11** | +7 |
| A split / two states (before-after, Day 1 vs Day 100) | **+10** | +0 |
| Danger | +9 | -2 |
| A self-imposed challenge | **+8** | **+9** |
| A known thing in a new state | **+6** | -2 |
| Versus (two sides) | **+6** | -4 |
| Absurd (should not be possible or here) | +3 | **+17** |
| Scale (giant vs tiny) | +0 | **+5** |
| No focal point at all | **-6** | -3 |
| A mystery / hidden thing | **-6** | -2 |
| A raw screenshot + text | **-7** | -1 |
| No words at all | -7 | **-11** |
| Pure spectacle (pretty or epic shot, no situation) | **-10** | **-4** |
| Cinematic poster or painting polish | +0 | **-18** |
| Dark card | +1 | **-19** |
| "Two worlds colliding" mash-up | +0 | +5 (not supported) |

Read it as direction, not law: the video's topic rides along with its card.

### 1.4 The stranger test
- On the picture alone: "someone who never played this game, what is happening?" If the answer needs a game word (pawn, vocation, a creature's lore name), rebuild with things everyone has a word for (a giant, a dragon, game over, fire, falling) or pick another moment.
- The gist of a picture lands in about 13 ms (Potter 2014). A reader who does not know a name skips every card that leans on it.

### 1.5 A situation, inside it, just before the payoff
- Show a situation, not a subject: one frozen moment with a before and an after, so a stranger says in one sentence what is HAPPENING (a verb, not a noun) and what might happen next.
- Every figure, avatar included, stands INSIDE the scene: feet or contact on its ground, facing or touching the thing, something of the scene in front of it. A floating head or a sticker beside a backdrop fails. On 465 outliers from 27 niches: inside-the-scene figures 47x vs 39x; an avatar inside a game moment 47x vs 40x.
- Leave the question open: the moment just BEFORE the payoff (the danger arriving, not the death; the catch mid-air, not the fish on the scale). Show an outcome only when it raises a "how?".
- The payoff must be in the video, and early. Test & Compare picks by watch-time share, not CTR, so a promise paid late loses even when it wins clicks. Pick moments from the first ~3 minutes.

### 1.6 One felt focal point
- At 168 px one element is felt in a glance: a face or emotion carrier (a roaring creature face, burning jaws, the brand character) fills >= ~50% of the frame height and carries the card's most contrast and its hottest colour.
- Gate: 3 fresh readers asked "what did you see first, and how does it feel?" all name it AND the feeling.
- Readable is not clickable: a card read correctly by 3/3 readers was clicked by 0/3.

### 1.7 A face is a floor, not a lever
- Within channel, a face or a big face shows no lift (Hindi +0 / -1, Western +1 / +4); extreme expression +2 / +9 with no reliable effect. Strong emotion sits on 68% of Hindi winners and 67% of flops.
- vidIQ: faces on 69% of 500 breakouts, exaggerated expressions on 5-6%. 1of10 (300k outliers): face vs no face about equal.
- Use a face only when it IS the action (pointing at, grabbed by, screaming AT the thing), never reacting beside the scene.
- The emotion matches the stakes. Danger shows fear or threat, never a smile, laugh, smug or celebrate. A smiling character on a calm sky beside a small fire read as "kids' channel".

### 1.8 Words: 0-3, and they must talk
- 0-3 words we add (4-5 warn, 6+ refused, 12+ is a wall). No words is a valid default: at the top outlier tier 0 words ran 50x vs 38x; vidIQ breakouts 52% use 0-3, 28% none. For a Hindi audience 4+ words still did fine (+11), and some words beat none (§1.3).
- Words talk: an opinion, emotion, doubt, verdict, question, number or a line someone says, adding what the picture cannot. Never a label ("Part 4", "END", "Monthly Update", "Recap #2"), never a summary, never the title again.
- Words mean something to a stranger and cannot be misread. Inside phrases fail. A line meant as "it will one-shot ME" read as a boast to 3/3 strangers; test each line on blind readers for its intended meaning.
- Size: each cap >= 8% of the frame height. The headline line >= 11 px tall at 168x94 (about an 85 px box at 1280x720, font size ~110 caps or ~95 lowercase); under 6 px FAIL. Winners' median 14.5-16.6 px at 168 (290 thumbnails). Anything under 4 px at 168 is fine print, game UI included: cut it.
- Glyph contrast >= 4.5:1 against its own background inside the line box at 246x138 (2.0 = fail; winners' median 4.7-5.9).
- No swearing, no Devanagari on a Hindi-audience card (Roman script), nothing in the bottom-right badge corner.

### 1.9 Measured floors (a floor stops unreadable cards; it never passes one)
| Check | Pass | Fail |
|---|---|---|
| Feed separation: outer band delta-E76 vs #0F0F0F (dark) AND #FFFFFF (light) | >= 35 | 15 |
| Colourfulness (Hasler-Suesstrunk M) at 168x94 | >= 70 (winners 71-75, field median 70, p25 60) | 35 (rejected cards 39-42) |
| Gloss: HSV S > 0.9 | <= 25% of pixels | > 25% = AI-gloss warn |
| Duration badge zone x >= 1100, y >= 620 on 1280x720 | empty | anything there |
| Hook in the top half (TV apps show the top first), top-half salient share | >= 0.50 | 0.27 |
| Focal regions (salient regions >= 2% of frame) | 1-3 | 5 |
| Edge density at 246x138 | <= 0.26 | 0.42 |
| Elements (subject, avatar, one text or marker; sparkles, rings, bubbles, cards each count) | <= 3 | 4+ (4-element cards rated 2-2.5/10) |
| Subject height (one subject doing something; never a document or text card) | >= 35% (0.40 good) | 0.22 |
- A heavy vignette or dark edge merges the card into dark mode: lighten an edge or keep a bright element touching it. In a mock with its 4-6 neighbours, ours is never the darkest or greyest.
- The story reads with the bottom half covered.
- Pixel metrics do not predict CTR: on 12,946 thumbnails from 600 channels every pixel feature differs <= 0.06 sd between a channel's winners and losers, and a floor gate fails 41% of losers vs 19% of winners. A card the owner rated 0/10 scored 9.3. The idea decides (§1.1-1.7).

### 1.10 Build tiers
1. Default: a staged in-game shot taken at record time (HUD off, photo mode or free cam, >= 1440p uncompressed, the moment before the payoff, subject big). Code only crops, grades and adds <= 1 marker or <= 3 words. Top faceless winners have little or no compositing; compressed, motion-blurred video frames make bad cut-outs.
2. One cut-out lit back into a frame of the same scene (§1.11).
3. Collage, bubbles, cards: only as a deliberate third test variant.

### 1.11 Recipe: a cut-out lit into its scene
1. Move the cut-out's Lab mean and std 30-50% toward the backdrop region it covers (tone zones and cast in §5).
2. Rim: a 3-8 px band on the light side, screened with the backdrop's brightest colour at 40-60%.
3. Cast shadow: the alpha skewed away from the light, blurred 20-40 px, at 25-40%. Contact shadow: a thin ellipse blurred 4-8 px where it touches. Both agree with ONE light.
4. Depth: backdrop blur 6-20 px, optional 10-20% haze, something of the scene in front of the subject.
5. Finish last, over the whole frame: one curves pass + 1-2% grain + one soft vignette (kept inside the >= 35 delta-E feed separation).
- A generic offset drop shadow alone = FAIL. Dark subjects recolour toward their bright in-game colour so they pop.

### 1.11b Getting a clean cut-out from video
1. Pull frames from a full-resolution source section, not thumbnails (thumbnails carry burned-in badges and are low-res). Rank candidates by sharpness (variance of the Laplacian) and drop motion-blurred frames before looking.
2. Pick frames where the subject is alone on a plain or contrasting ground and fills the frame; the cut-out must not need an upscale (> 1.15x never ships).
3. Matte with BiRefNet (`rembg`, session `birefnet-general-lite`): on cartoon and CGI frames it held clean edges where `isnet-general-use` failed (green character on a green ground, glow outlines).
4. Keep only the subject: the alpha blob under a seed point on the subject; a neighbour touching it goes by colour (keep the subject's own palette in the zone where they meet). Check at 200% on a mid-grey and a dark ground: no halo, fringe, foreign sliver or hard cut except the frame edge.
5. A subject cut by the frame edge is placed against that same screen edge and never lifts off it (SKILL.md, Characters).

### 1.12 Frozen brand art and props
- A brand character comes only from its approved source (a code-built vector or the approved sticker PNGs). Never redraw it, AI-regenerate it, squash, stretch or deform it: uniform scale, tilt and move only.
- In a thumbnail it fills >= 45% of the frame height (>= 55% as the focal point), touches the scene (a scene layer over part of it + a contact shadow) and sits IN the relation with the threat, never as a corner reaction. A sticker face vanishes at phone size (at 60 px tall terrified, scared, shock and gasp look the same), so emotion comes from pose, size and contact.
- How faceless channels use avatars: pure faceless channels mostly leave the avatar out of their top cards; the mascot channel that wins puts it INTO the game, lit and textured like the scene (2.6-3.7x). Nobody wins with a sticker border. Inside each channel the losers are as polished as the winners: finish is table stakes.
- Sticker borders: only round, built from a blurred alpha, only on 1-2 graphic objects (a prop, a price tag). A character in its own scene gets light, not a border.
- A familiar UI card with an absurd value is a proven device: a price tag, a score, "-90%", a store listing (a fake store listing ran 61x). Use the game's real number. A prop can carry the emotion when a face cannot.
- Backdrops: a designed backdrop is fine; never a default flat digital colour, a code gradient that reads as a slide, or an abstract burst. Pick the colour for harmony with the subject, separation from it, and standing out in that game's feed.

### 1.13 Never on a card
Fake platform UI (timestamps, "views", "subscribe", red progress bars), invented numbers, re-typeset or sheared game UI (use its real pixels), meme templates, emoji, editor labels ("BEFORE/AFTER", "LESSON 1"), abstract burst backgrounds, raw frames with text, the red-arrow + red-circle + shocked-face formula with nothing else, sparkles, rings, glows, poster polish, swearing, anything in the badge corner. Every number shown is true and sourced.

### 1.14 A/B: 3 pairs, drastically different
- Every long video gets 3 title + thumbnail PAIRS, each with a different hook mechanism, composition AND palette. Never 3 shades of one design.
- The winner is picked by watch-time share and needs ~2,000+ impressions per variant (tests at 225 and 262 impressions ended inconclusive). Keep the winner and re-run it against 2 new variants. Log pairs and winner.

### 1.15 File
16:9, compose at 1280x720 (downscale only; an upscale adds nothing), <= 2 MB, a JPEG twin at stepped-down quality when the PNG is over. Cut-outs only from full-res native frames; an upscale > 1.15x is LOW-RES and never ships (an upscaled crop read as "low quality"; the losing cards measured sharpness 12.8 vs the winner's 22.1 at 168x94).

### 1.16 A worked winner, generalised
The owner's best-rated card, measured at 168x94: one real face with one emotion a stranger names in one word at 95% of the height (luma spread 186, sharpness 22.1, saturation 0.59), doing something TO the other subject (two characters + one relation, the creator is the loser), the stake in the game's own look (its red death screen), <= 4 words in the creator's voice, one backdrop colour, 3 elements, native-res crisp. The losers: a 1.33x upscale of a blurred frame (sharpness 12.8) and a blank grey face (saturation 0.36). A subject standing BESIDE the threat is not a relation.

## 2. Titles as packaging (pairing and visual rules only)
- Thumbnail and title are one unit. The picture is the moment; the title adds the premise or a twist. The card's words never repeat the title's premise (the game name may sit on both). Eye tracking (ETRA 2018): viewers look at the thumbnail first and about twice as long as the title.
- Long title ~55-70 chars, premise first, inside the ~40 chars a mobile feed shows. Short title: the hook inside the first 40 visible chars (60 desktop, 100 max), no `#shorts`, no hashtag stack (3+ tags 0.94x), at most two all-caps words.
- A Short's title is only for the situation the picture cannot show, never to explain the joke.
- Specific beats vague: the game, a true number, a situation. No em or en dashes, no emoji, no hashtags in long titles, no swearing.
- The click floor's "what I expect" lines (§6.5) are the mismatch check: if readers expect something the video does not pay, the pair is wrong.

## 3. Shorts and Reels covers + vertical frames

### 3.1 Two products
- A Short and a Reel of the same moment share captions and gates but get their own render when a lever differs: length (Short 15-35 s; a Reel may keep setup to ~60 s), frame one (Short: the clearest premise with sound off; Reel: the most sendable line, voice from 0.0 s), the ending, cover and words. The payoff never changes.
- Platform AI processing stays off (`edit.md` §8.7).
- Instagram does not recommend Reels that are low-res, watermarked (another app's mark included), bordered, muted, mostly text or already posted. Upload your own clean render, 720p or more at 30 fps or more.

### 3.2 UI bands at 1080x1920 (x from left, y from top)
| App | Always covered (FAIL for our text or character) | Sometimes covered (WARN) |
|---|---|---|
| YouTube Shorts | top 0-120; bottom 1620-1920 (title, channel, Subscribe); right rail x 960-1080 from y 1000 to 1620 | y 120-180 (tall phones); y 1530-1620 (2-line title, related-video pill) |
| Instagram Reels | top 0-210 (header, camera); bottom 1610-1920 (handle, caption, audio); right rail x 960-1080 from y 1100 to 1610 | y 210-270 (Meta's 14% line); y 1520-1610 (caption second line) |
- Meta's own ad rule: 14% top, 35% bottom, 6% sides free of text. Band values are secondary measurements that agree with each other; re-measure on a phone screenshot after either app redesigns.
- Nothing added sits above y 270. Top-anchored text uses a 290 px top margin (at 200 a hook bar measured inside Instagram's 210-270 band).
- Captions: bottom-centre, lines inside x 140-940 (clear of both rails; at a 60 px right margin a long chunk reached x > 960), baseline ~440 px above the bottom. A per-piece caption baseline stays within 0.20-0.80 of the height so it can dodge game chat without entering a FAIL band.
- A corner character goes in a TOP corner (default top-left, about x 40-340, y 560-900; top-right when the game HUD is top-left). Never bottom-left or bottom-right: both sit under the apps' title and buttons. Move it when it covers the subject.
- Manual check on every render: grab frame 0, 1.0 s and the last frame; subject inside the bands, character visible, every auto pan watched.

### 3.3 Frame one is the hook
- On-screen WORDS within the first 0.5 s (a character or motion does not count) and the speaker's voice by 0.5 s, saying a line about what is in frame. Missing either = FAIL. Pull a caption that starts before 0.5 s to 0.0 s.
- Frame one shows the subject + the situation, readable in ~1 s with sound OFF (on YouTube it is the feed thumbnail). Goal and obstacle go in the first spoken sentence (7 of 7 measured winners, median 14.1x). Never open on filler or mid-thought.
- Measured miss: Shorts that opened slow kept 15-35% past the first seconds; healthy is 60-70%+.
- No added hook-text bar. Words on a vertical screen are the speaker's captions and the game's own text. Editor-written hook lines read AI-made and did not separate winners (Hindi Shorts with no added text in the first 2 s: median 28.5x, 4.2x with one outlier channel removed; with an English premise line or title card: 3.8x; the one added Hinglish line sat on a 1.01x control). No text, emoji or filters in the apps' cover editors either.
- A joke that lives in small game text, a chat bubble or an NPC or TTS voice does not survive at phone size, however it is cropped or captioned. Pick moments where the speaker's spoken line is the joke and the picture shows the stakes in frame one.

### 3.4 Framing a 16:9 source into 9:16
- Default full-height: a crop window 0.316 of the source width (810x1440 of 2560x1440, scaled 1.33x), placed by a saliency camera that per piece either holds on the subject or does one slow pan. No jitter, no whip pans; no clear subject = centre. (The old 4:3 band filled only 42% of the screen.)
- Go wide only when the joke needs width (cause and effect far apart, UI or subtitles to read, mirrors): square 1080x1080 (56% fill) or 4:5 1080x1350 (70%), never the 4:3 band. Bars must do a job (the avatar, the caption, the game's own text), never empty blur: Instagram reach-limits Reels "with borders".

### 3.5 Covers
- Every Short and Reel gets a designed 1080x1920 cover built like a thumbnail: the moment BEFORE the payoff, one subject >= 35% of the frame height, 0-3 words (the speaker's or the game's), a brand character lit and never squashed.
- Safe zones: hard edge y 240-1680 (Instagram 3:4 grid crop; also clears YouTube's 2:3 card crop of ~150 px). Words, faces, character: x 60-1020, y 300-1500 (above the YouTube shelf title band). Best spot: x 60-1020, y 420-1500 (survives a 1:1 centre crop), subject centre near y 900-960.
- Words >= 70 px tall on the 1080x1920 file (~13 px on the 202 px shelf card), 2-4 words a line. 9 px text and 5-line premises read as noise and were the weakest lifts. Small game UI counts as no words.
- Bright and busy: mean luma >= 50/255 (> 110 = bright), not flat. On 1,539 shelf cards from 19 channels: dark covers were 11% of 3x winners vs 23% of under-median Shorts; bright 33% vs 18%; flat 20% vs 34%. Never a dark corridor, menu, transition or letterboxed strip with a tiny subject.
- One subject fills the card (a lit character, the jaws, hands with a price tag, a half-screen game crop).
- The template does not separate winners; the moment does. Controls with the same title bar and layout as their channel's winners sat at ~1x. Spend effort on the moment.
- Pick the frame on purpose: name the exact second for the app's frame picker, and make sure the cover moment exists inside the Short (frame one or a held frame).
- Where covers show: not in the swipe feed (the video plays, so frame one matters most); the Shorts tab and search show 2:3 cover-fit (~150 px lost top and bottom); the Instagram profile grid shows the centre 3:4; some surfaces letterbox to ~3:2. Keep the subject central on both axes. When the Reel cover is frame one, the playing overlays cover ~270 px top, ~670 px bottom, ~230 px right (one secondary source, unverified).
- Files: YouTube custom Short thumbnail 9:16 JPG or PNG (spec 2160x3840, min height 640, up to 50 MB; house cap 2 MB with a JPG twin), desktop only and partner-gated. Instagram cover: JPEG up to 8 MB, 9:16. There is no A/B test for Short covers.
- Reel caption text: at most 5 hashtags (Instagram has ignored extras since Dec 2025).

## 4. Text on video

### 4.1 Which words
- Only the speaker's exact words or real game/UI words. No editor labels, roasts, parentheticals, "ATTEMPT #7", kinetic WHAT/HOW/WHY, or time cards without a real number. The edit sharpens the joke; it never writes its own on top.
- A word card that repeats the line just said is an echo, not emphasis (tell T4, `edit.md` §8). Text must add something.
- For a Hindi-speaking audience, captions in Roman script as spoken (preferred 57.8% vs 25.1% Devanagari), English words stay English, casual spelling. 93% of that audience watches on phones.

### 4.2 The outline + shadow recipe
- White fill, near-black ink outline (#0A0A0A-#141414), optionally a hard offset shadow in the brand accent, no blur. Flat captions with no outline over moving gameplay read robotic.
- Proportions: stroke = max(3 px, 5.5% of font size); hard shadow offset down-right = max(4 px, 7% of font size); line spacing -1/8 of size. CSS: `paint-order: stroke fill` so the stroke never eats the glyph.
- A slam word at 1080: stroke 18 px, hard shadow 10x12 px, no blur.
- One heavy grotesk in black weight, lowercase by default; the look stays fixed per brand, the layout changes freely. A game's own words (a death screen) keep the game's look.

### 4.3 Sizes
| Canvas | Caption | Outline | Notes |
|---|---|---|---|
| 16:9 at 1080p | ~82 px | 6 px | bottom third, <= 2 lines, above any corner character |
| 9:16 at 1080x1920 | ~152 px | 8 px | 2-3 word chunks inside x 140-940 |
| 9:16 key-phrase pop | ~132 px CAPS | 8 px + hard accent shadow | one phrase, real peak lines only |
| Thumbnail 1280x720 | caps >= 8% of height, line >= 11 px at 168x94 | 5.5% of size | §1.8 |
| Cover 1080x1920 | >= 70 px tall | | §3.5 |
- Size follows delivery: a shout (well over the talk level) = CAPS at ~1.4x; a mumble = small lowercase. The words never change.
- Phone viewing at ~30 cm has no measured caption-size floor yet. experience.md's read-at-distance tiers are for ~1 m and TV. Treat caption height as a share of frame height, keep one statement on screen at a time, and measure against Shorts that were watched vs swiped before fixing a number.

### 4.4 Timing and reading
- Caption pop-in 70 ms from 86% to 100% scale. A 9:16 chunk never leaves a sentence's last word alone, stays up >= 0.4 s, and flips on the speaker's audible words.
- Reading speed (16:9 captions): p95 <= 17 cps scores 10, <= 22 scores 8.5, <= 25 scores 7, above fails. Vertical 2-word chunks are scored on flip rate instead.
- Anything meant to be read holds >= 30 frames at 60 fps (0.5 s), and long enough to read twice for a sentence.
- At most 1 new piece of text per 1.5 s; at most 3 transient layers; each element on screen >= 0.5 s.
- No zoom, shake or RGB split while text that matters is on screen. Read before energy.

### 4.5 Placement
- Never over a character, a censor box, the game's subtitles or prompts. Per piece: lift the rows over a bottom-centre prompt, move them sideways to a blank side (x 0.15-0.85), or move the baseline (0.15-0.95 of height on 16:9, 0.20-0.80 on 9:16).
- Cards and stickers live in the top two thirds; the caption band stays reserved.
- Recreated chats or messages use the real app's look, never a crooked pasted screenshot; in a statement, one highlighted keyword at most.

## 5. Composites and image finish

### 5.1 Lighting match
- The eye misses a wrong light direction but catches mismatched tone zones, colour temperature, saturation, local contrast and edge sharpness (Ostrovsky 2005; Xue et al. 2012; Lalonde + Efros 2007).
- Match the subject's p2 / p50 / p98 luma to a ~40 px ring around it (match the zones, not the mean); identical black levels. Take the scene's colour cast (firelight = warm skin). Cap chroma at the ring's p95. Lab b* within 8 of the ring.
- Match sharpness and grain; add a 1-3 px light wrap (the scene's colour bleeding into the edge); 2-3 depth layers (foreground occluder, subject, haze/background); contact shadow wherever it touches.
- A deliberately cartoon character is judged on how well it is integrated (lit by the scene, matched, occluded, touching, same grain), never on whether it can be told apart.

### 5.2 Edges
- Keep the matte's soft alpha; clean it AFTER the resize with a short ramp (alpha 70-150), never a 0/255 threshold before it.
- Fix a bad mask with a cleaner frame or a soft brush, never hand rectangles. No stair-steps. Expand the canvas before any shear or rotate (a sheared card with sliced corners was the worst-rated cut).
- No halo or dark box: the ring just outside the cut-out darkens <= 3 luma. No glow outline, no generic drop-shadow box.
- Check every edge at 200% on the full-size file. Edge faults are invisible at 168 px but the owner views full size and on TV.

### 5.3 One finish over everything
One grade + one grain pass (1-2%) + at most one soft vignette over the whole frame, last. A clean layer next to a noisy one, or a patch with < 0.5x the frame's fine noise, reads plastic and AI-made.

### 5.4 Cleaning game frames
- Small round HUD marks (a reticle): inpaint from surrounding pixels before any crop, push, grade or 9:16 crop. Never a delogo filter (streaks) or a blur box (visible square). A text label or HUD bar leaves a smear: crop it or pick another span.
- Never darken, blur or cut out the game picture to present a subject.

### 5.5 Redaction look (identifying details in frame)
- A per-frame tracked box (the 0.5 s running median of the track, never the span max), centred with no lag, feathered rounded edge (feather 0.22 of the target's short side). Mosaic blocks never under 24 px, or a strong blur.
- A box clamped at a frame edge grows inward to 2x the median key size (a clamped box left a plate readable for 3 frames). Fade out over its last second.
- Prove it: OCR every frame of the span; nothing legible.

### 5.6 AI imagery and added media
- AI images ship only as a prop, backdrop extension or lighting pass a blind stranger cannot tell is AI. The subject stays the real frame. Never strip provenance labels; log which element is AI.
- A real person's likeness: their real photo first, face unedited. An AI likeness only with the owner's yes on that exact card plus the platform's altered-content disclosure.
- Licence tiers. GREEN: own art, Apache / CC0 / public-domain images, the platform's audio library, CC0 foley. YELLOW: a famous meme template only as a <= 1.5 s transformed still used as commentary, never in a thumbnail. RED: film, TV or Bollywood dialogue, anime clips, news clips, songs (recreate the meme in your own voice). Every CC BY file gets a credits line the description carries.

### 5.7 Measurable AI-look tells for images (research basis: being read as AI costs ~10 points of demand even on real photos)
| # | Tell | Threshold |
|---|---|---|
| M1 | AI provenance metadata (C2PA, IPTC trainedAlgorithmicMedia, EXIF Software) | WARN: triggers platform "AI info" labels |
| M2 | Oversaturation | colourfulness > the game's top-6 median +30%, or > 25% of pixels at S > 0.9 |
| M3 | HDR halos | a 2-8 px luminance overshoot along > 30% of the subject contour |
| M4 | Plastic smoothness | patch fine-noise std < 0.5x the real frame's |
| M5 | Diffusion fingerprint | FFT radial energy in the 0.1-0.4 band (FreqCross, Synthbuster) on the AI element's crop: score > 0.5 = WARN; shrink, re-composite into a real frame, or cut it |
| M6 | Garbled text in an AI element | OCR confidence < 0.6 or non-words = FAIL |
| M7 | AI palette | teal 170-200 + orange 20-40 hues > 60% of saturated pixels, or magenta 270-320 > 25%, when the real frame has under half that |
| M8 | Posed symmetry | saliency centroid within 5% of centre AND mirror correlation > 0.8 |
| M9 | Lit from another world | Lab b* delta > 8 vs a 40 px ring, or no contact shadow |
| M10 | Upscaled softness | Laplacian variance ratio < 0.4 |
| M11 | Sameness | pHash distance < 10 to any of our last 8, or the same text box + character box within 5% |
| M12 | Cloned role-model layout | NCC > 0.85 on a region = FAIL |
| M13 | Brand character not from its approved source | NCC of its box vs the nearest approved sticker at that scale + tilt < 0.9, or aspect ratio off by > 2% = FAIL |
| M14 | Fake platform UI or invented numbers | FAIL |

Judged image tells, by a reviewer at 200% and at 168 px: waxy surfaces; impossible geometry or fingers; background mush or repeats; a style clash with the game's renderer; gloss (god rays, sparkles, smoke, glow = an ad, not a moment); generic, could be anyone's; a scene not in the video; the red-arrow + circle + shocked-face formula alone; shading the scene does not have. Gate: a fresh agent sees ours mixed with 3 real game thumbnails, "point at each AI part, or say none". Pass = it cannot point at ours better than at the decoys.

- Channel art (YouTube banner 2560x1440): before showing any version, render the desktop, phone (safe area 1546x423, centred) and TV crops side by side on one sheet. Wordmark centred on x 1280 inside the safe area, the whole character inside the phone crop, no tagline unless asked.

## 6. Blind readers and measurement

### 6.1 Fresh and context-free
- The session that built the work never grades it alone. The builder knows the joke; builders score ~1.5 points above fresh readers, and our own check once ranked a 0/10 card first.
- Every reader is a FRESH agent given ONLY the file: never the title (unless the test needs it), the video, the build script, edit notes, earlier reviews or our reasoning.
- Thumbnail read prompt on the 360 px card: "In one sentence, what is happening, and what do you think the video is about? What did you see first, and how does it feel? Do any words mean something to you?"

### 6.2 Judge at the real sizes
- Render 1280x720 and 1080x1920 PNGs and judge them in a feed mock: the 360 px card, the 168x94 up-next card with its duration badge, 246x138 search, the 202 px Shorts shelf. Never at browser widths; web inspectors do not cover fixed canvases.
- Neighbour mock: the card among the 4-6 it will sit beside. Covers: a one-look read of the 202 px card plus a mock among the game's top Shorts, 3 fresh readers, under 8.5 = redo.
- Pasted-element test for composites: a second reader at 200% is told "one element was pasted in: which, and how can you tell?". Pass = it cannot name one, or names a wrong one.

### 6.3 The harsh scroller (final judge, with the owner's pick)
One fresh agent per card, shown the 168 px neighbour mock and the card with its title: "You scroll YouTube on your phone and skip almost everything. Card N is new. In 3 lines: what do I get if I tap it; the one reason I scroll past; the one change that would make me tap. No praise."

### 6.4 The unskippable bar (locked on 465 outliers, 27 niches)
Score 0-10. Ship = every row except U4 >= 7 AND the mean of the 11 >= 8.5. A blind reader scores U1-U4 and U10-U11; U5-U9 are scored at 200% on the full file by a second reader.

| Row | 10 = | 0 = |
|---|---|---|
| U1 Situation | a stranger says what is HAPPENING (a verb) and what might happen next | a subject posing, a lineup, a logo |
| U2 The gap | one specific question the title does not answer | no question, or one nobody cares about |
| U3 Relevance | a thing the viewer already knows, in a new or wrong state | nothing recognisable, or in its normal state |
| U4 Stakes (bonus) | a danger, price, clock or loss readable at 168 px | everything calm |
| U5 Inside, not beside | contact, facing or touching, something of the scene in front | a floating head or sticker beside a backdrop |
| U6 Tone zones | highlights and shadows at the scene's levels, same blacks | a bright flat cut-out on a dark scene |
| U7 Temperature + saturation | the scene's cast, saturation within its range | daylight subject in a night scene |
| U8 Edges + light wrap | no halo, outline or box; scene colour bleeds 1-3 px in | sticker border, glow, aliased cut |
| U9 Depth + grain | 2-3 layers, contact shadow, one grade + one grain | flat layers, clean next to noisy |
| U10 One focal point at 168 px | the eye lands on ONE spot; <= 3 elements; reads with the bottom third covered | 3+ things of equal weight |
| U11 Words talk (0-3) | none, or a doubt, verdict, number or line a person would say | a label, a summary, the title again |
| U12 Title pairs, video pays | the title adds premise or twist; the moment is in the video | the title repeats the picture, or the video never shows it |

### 6.5 The click floor
- 6 phone cards WITH titles: ours, the last rejected card as an anchor, 4 role-model hits from a comedy feed (not the game's search feed: trailers and walkthroughs lose to anything, so that test is useless).
- 3 fresh readers, each with a persona from the target audience (e.g. a 19-year-old Hindi gaming viewer) and time for exactly 2 videos, answer "CLICK: a, b" plus one line per card on what they expect.
- Ship needs >= 2 of 3 clicks. Necessary, not sufficient: it clicked two cards the owner rejected. Beating the anchor is logged, never a pass.

### 6.6 Calibrate before a reader gates
- Run every new gate or prompt on a fixture set first: known rejects must FAIL, known approvals must PASS. No gate stands alone; a reader that fails calibration is a log until it predicts real A/B winners.
- On 6 owner-rated cards: the "what is happening / what did you see first" reads sorted all 6 correctly. A feed-rank reader passed all 6 (rejects too) and flipped order on a re-run. A 2x2 "which is amateur" reader picked ours 18/18. The feed-seat ranker alone passed a 0/10 card (bright colour fools rankers); together with the two reads it sorted all 6.
- When |self-score - outcome| > 1.0, the rubric is missing a dimension: add it the same day, with a number and a source. Decide rule changes on 3-5 videos, not one.

### 6.7 Video reviews
- 3 FRESH reviewers in parallel, none sees another's review, the same exact row list; a script averages per row (mean, min, spread). Fix a weakness when 2 of 3 name it (spans within 3 s) or a measured gate fails; one reviewer's point is weighed, not obeyed. One reviewer's own scale steered an edit from 7.4 to 6.8 before this rule.
- Ship = the blind ship score >= 8.5 AND every row's average >= 8.5. A self score may sit at most 0.5 above the blind score. A low blind score is fixed, never argued. Keep iterating while the score rises; stop and report on plateau or oscillation.
- Reviewers who cannot hear: every sound row is marked "(not by ear)" and capped at 8; the overall sound row at 7, minus 1 per sound template tell. (Unheard reviewers gave 8-9 to a mix the owner disliked.)
- Watch the WHOLE render, picture and sound, at full runtime, plus a frame strip at every boundary (0.5 s steps across a span, 0.1 s at edges). A reviewer that judged stills passed a film the owner scored 3.5/10.
- Motion-aware evidence for films and motion pieces: every cut 3 frames before + 3 after at 30 fps, a 6-frame burst for every shot >= 3 s. Score against two anchors (9 = reference craft, 3.5-4 = a rejected cut). A re-cut must beat the cut it replaces head to head TWICE with the order swapped, a fresh reviewer each time. After a review-tool change, re-run both anchors (bad <= 4.5, good >= 8.5) or revert.
- Anchor calibration: compare each row with an owner-rated anchor ("better, same or worse, by how much"); not clearly better = at most 5.5 on that row. Keep a ledger of the owner's verdicts next to the gated scores.
- Human side-by-side: frame sheets at the SAME fps and tiling from 3 of our minutes (first, middle, last full) and 3 human-edited reference minutes. Per pair, a forced choice: which looks made by a person, which you would keep watching, with one line naming the device behind each.
- Zero-context test for every Short and Reel: a stranger with no context answers What happened / Why is it funny / Want to finish it / Watch the full video. A blank, "not sure" or "no" = RE-CUT whatever the score. Rows: hook 0-1 s, zero-context payoff, pace, readable lines, picture cleanliness, sound, loop or ending, reason to watch the long, platform fit, cover. A moment with 2 fresh rounds under 7.5 is dropped; no third polish round (one moment ran 10 rounds and stayed 5.9-6.8). Shorts had been scored ~3 points high before this.

### 6.8 How a score is built
- Four layers in order: L1 gates pass/fail on external specs (any fail = not shippable); L2 measured 0-10 from numbers only; L3 house style as pass/fail lists that only BLOCK; L4 outcome (real post-release numbers) overrides L2 for calibration. Home-made self-ratings drifted high (every row 8.5-9.0) on videos that then measured CTR 2.0% and 27% retained at 0:30.
- L2 bands for video: 10 = beats the published pro spec with margin, 8.5 = meets it (the ship floor), 7 = within one tolerance step, <= 5 = fails. Example, loudness: |I + 14| <= 0.5 -> 10, <= 1 -> 8.5, <= 2 -> 7, else 4. This is a different scale from process.md's page bands, where 8.5 is rare: say which one applies.
- Judgement rows (story, emotion, jokes) use Murch's Rule of Six weights (emotion 51, story 23, rhythm 10, eye-trace 7, 2D/3D 9), are labelled judgement, and are never self-scored above 8 without an outcome number.
- The gated overall = min(row mean, the AI-feel cap from `edit.md` §8, "feels made by a person", "fun to a stranger", "sound quality"). A device count never raises it. Recompute the score from the reviewer's tables; where it disagrees with the typed number, the computed one ships.

### 6.9 Within-channel winner vs flop (the method behind §1.3)
1. Per channel take the same 60-120 recent uploads. Winners >= 2.5x the channel's own median (>= 2x for big Western channels), flops <= 0.6x. Comparing a channel with itself removes channel size.
2. Shuffle and number the cards at 320x180. Coders see images only: no titles, views or group; keys moved out of their folder.
3. Two independent coders per feature; report agreement (84-99% here).
4. Per feature: winners' share minus flops' share, averaged over channels, with a 90% bootstrap CI. Bold only what clears zero.
5. State the limits: topic rides with the card, the crawl's search bias, AI coders. Winner-vs-winner across channels gives hints, not causes.
