# Ads, posters and in-game signs

Use when: a business ad, hiring poster, menu board, event flyer, opening announcement, Discord or social post graphic,
in-game billboard, sign or screen, for a real business or a roleplay (RP) one, still or animated (GIF, MP4 loop).
Mode: Persuade boldness at Video read sizes. Sizes and print: `decks.md`. Read at distance: `experience.md` §7.
Gate: `tools/still_check.py --as ad` (or `--as ingame`), then the stranger read below. Both pass or it is not shown.

## Why this file exists
A hiring poster for a BBQ business was sent back as "hella low effort AI" (Nov 2026). still_check on it, measured
afterwards: 58 words on one image (wall at 40), 4 lines of fine print under 6 px on a phone, no single subject (the
largest region 18% of the height), two lines of text overlapping, an AI generator's C2PA provenance in the file, and a
loop of ~46 drifting ember specks a frame with smoke and a glowing headline. Every one of those is a default nobody
chose. This file is the rule set that stops it.

## 1. Brief before pixels (5 minutes, never skipped)
- **The business inventory.** 8-12 things only this business has: its real name and logo, the street or corner it is on,
  the real items it sells (names exactly as on its menu), its prices, its hours, its colours (sign, uniforms, cups),
  its owner's or mascot's voice, how people really apply or order (phone number in game, walk in, a Discord channel).
  Ask once for what is missing, each with a default. Never invent jobs, perks, pay, prices or contacts: a placeholder
  is marked as one in the report, never designed in as if real.
- **One job per piece.** A hiring poster says: we are hiring, the 1-2 roles that matter most, how to apply. Job
  descriptions, perks lists and menus go in the post's text, not in the image.
- **Where it lives** decides the profile: Discord or social = `ad`; an in-game billboard, sign or TV = `ingame`; a 9:16
  story = `story`. Ask the RP server's ad rules (in-character only, no real brands, size and file limits) before building.
- **What would make it fail**, written down: "reads as a template", "looks AI-made", "can't read it in a chat preview".

## 2. Pick a vernacular, never "a nice poster"
Real businesses look like their world, not like a design tool. Choose ONE vernacular from the subject, name it in the
brief, and commit every choice to it (type, paper, colour, texture, how text is made):
| Business | Vernaculars to choose from (pick one) |
|---|---|
| BBQ, diner, food truck | hand-painted sign-writer board; butcher paper with a stamped menu; a felt letterboard; wood-type print (two inks, misregistered); a stencilled crate or smoker-door look |
| Bar, club, music night | screen-printed gig poster (2-3 flat inks, halftone photo); photocopied flyer (high-contrast photo, typewriter or Letraset type); a real neon sign photographed at night |
| Garage, mechanic, tow | enamel sign; service-counter carbon form; vinyl lettering on a van door |
| Shop, boutique | price tag or receipt; shopping-bag print; window decal |
| Club, gang, crew | spray stencil on a wall; patch or embroidered badge; a cheap printed sticker |
| Office, law, real estate | real-estate yard sign; business card; letterhead |
- The vernacular gives the texture honestly: misregistration, a stamp's uneven ink, letterboard gaps, the paper's tooth.
  It is drawn from the medium, not sprayed on as a "grunge overlay".
- Three directions = three different vernaculars, shown small side by side before one is polished (house rule: mock 3,
  the owner picks or combines).

## 3. Hierarchy and words
- One dominant line, 2-6 words, at headline size (still_check `text_px` PASS at the `scroll_past` view). For a hiring
  poster that is the offer in the business's voice ("WE NEED A PITMASTER", "HIRING: GRILL + COUNTER"), not "NOW HIRING!"
  under a logo with a 3-line subtitle.
- One subject >= 35% of the height: the real product (the item photographed or screenshotted in game), the logo built
  big, or the place itself. Not four equal boxes.
- Supporting text grouped in one block: role(s), where, how to apply. Total words <= 18 is the target; 40 is a wall
  (FAIL). Nothing under 6 px at the phone view: if it doesn't fit at a readable size, it goes in the post text.
- Two typefaces at most: one display face with real character that belongs to the vernacular (wood type, sign-painter
  script, a condensed grotesque, a stencil), and one plain face. Never a "fire", "BBQ" or "western" novelty font
  picked from the category; never the overused display faces in `tells.md`.
- No exclamation marks in display type. No stock lines ("Join our team!", "Join the crew!", "Exciting opportunity").
  Copy sounds like the owner talking: short, specific, a real item or place named.

## 4. Real over generated
- Use the business's real logo (vectorise it if it only exists as a low-res image), real in-game screenshots of the
  place, the food prop or the vehicle, real colours sampled from the sign or the uniforms.
- AI images only for a background texture or a plate nobody looks at, and only after a blind viewer can't tell. A file
  that carries AI provenance (C2PA, a generator name) is logged in the report; never strip it.
- Text is always real type (HTML/SVG rendered to PNG, `decks.md`), never letters drawn by an image model.

## 5. Animation: one idea that belongs to the place
- Default: the poster is complete and readable on frame 1 (chat previews, embeds, reduced motion and in-game textures
  show the first frame), then ONE motion that the business owns, then a long hold. Hold >= 2/3 of the loop.
- Motion ideas that read as made by a person: a letterboard letter slotted in; a stamp landing "HIRING" with a small
  ink spread; a price card flipping; one letter of the real neon sign flickering on its own rhythm; a ticket printing;
  the smoker lid lifting once with real smoke from that lid. Each happens once a loop, timed, with a pause after it.
- Banned as defaults (the AI ad kit): particle fields (embers, sparks, dust, bokeh, snow) over the whole poster; smoke
  or fog layers drifting over text; a pulsing glow or light sweep on the headline; lens flares; shimmer; steam on every
  hot thing; a slow zoom on everything; floating, bobbing or rotating elements. still_check `particles` and `motion`
  measure the first two.
- Timing: a 3-6 s loop, seamless (`loop` PASS); never more than 3 flashes a second (`flash`, WCAG 2.3.1).
- Files: Discord free uploads cap at 10 MB (`size` row); MP4 (H.264, yuv420p, `-movflags +faststart`) is sharper and
  smaller than GIF; send both, GIF for autoplay in chat. A GIF uses a palette built from the poster's own inks
  (`palettegen=stats_mode=diff`), not dithered gradients.

## 6. In-game placement
- `--as ingame`: 3-6 words, read across a street (`text_px` at the 128 px view), flat shapes, high contrast, no fine
  print. Test it in the game at the real viewing distance when possible and look at the screenshot, not the file.
- Texture sizes: the game's limit (often a power of two, e.g. 1024x512 or 2048x1024). Build at that size, not a
  downscale of a portrait poster; an ad designed for a phone is redesigned for a billboard, not squashed.

## 7. Review (before anyone sees it)
1. `still_check.py <file> --as ad --words "<the exact words>" [--vs <the business's last 3 pieces>]`: 0 FAIL; every
   WARN fixed or defended in one sentence.
2. Stranger read: a fresh agent (or person) gets ONLY the image at phone size and answers: what business is this, what
   do they want you to do, how do you do it, and which part looks fake, generic or AI-made. A wrong answer or a named
   AI spot = rebuild that part and ask a new reader.
3. Harsh-scroller critique: "You scroll a busy Discord channel. In 2 seconds, why would you stop on this, and what
   would make you scroll past?" Fix what it names.
4. Set beside the business's last three pieces and two real-world examples of the chosen vernacular: if ours reads as
   a template next to the real ones, change the layout, not the shade.
5. Score with `process.md` and ship only at the bar. The report names every placeholder (roles, pay, contacts) that
   still needs the owner's real info.

## 8. Made, not generated: the sheet-on-a-wall recipe and the AI-feel fixes
Learned on a hiring poster that passed every meter and a blind 2x2 against the business's old piece, and still
"felt AI" to the owner. A poster that looks generated is usually too even, too centred and lit by nothing.
- **Build it as a physical object.** `tools/paper_kit.py` makes the layers: `sheet` (torn top edge, tooth, fibres, one
  fold, lobed grease stains with a tide line, never round grey blobs), `tape` (torn ends), `stamp` (an ink mask whose
  voids follow paper tooth and a rocked hand pressure). Sheet on a rotated div with a two-layer drop shadow; brand art
  and type printed into it with `mix-blend-mode: multiply`; the same sheet again on top at `soft-light` ~0.75 so stains,
  fold and tooth run across the ink. CSS masks and SVG noise maps go in as `data:` URIs (Chrome blocks `file://`).
- **Use their assets, cut from what they already have.** Their old GIF or screenshot holds the logo, wordmark and
  background: flood-fill the logo out, mask the wordmark by its colour, keep their wall or wood. Do not redraw or
  restyle a logo the owner asked to keep; print it into the paper and leave it.
- **Break the symmetry.** Nothing sits dead centre: logo and wordmark a few px off and tilted under 1.5 degrees, the
  stamp off-axis at 4-7 degrees, tapes at clearly different angles and lengths. `inspect` will WARN `off-centre`:
  defend it as the point.
- **Give it one light.** A warm light from one side (a baked radial PNG, not a CSS gradient, which `inspect` fails),
  a darker lifted corner with its own soft shadow, and a soft-light curl across the sheet. Uniform vignettes read as a
  filter.
- **Handwriting is never a font at rest.** Per-letter jitter (baseline, rotation, scale, skew, stroke weight 0.3-1.9
  px), per-line tilt, and a small displacement map (`feImage` noise + `feDisplacementMap`, scale 3-5; `feTurbulence`
  is a preflight ban) so repeated letters never match. Re-read the smallest line after: past scale ~4 an "n" turns
  into an "r".
- **Stamps were pressed.** Rounded corners, a wobbled border, a faint double strike (a 3-4 px offset text-shadow at
  ~0.2), the stamp lands once with a 1-2 px sheet dip on contact, then holds.
- **Test it like a stranger.** A fresh reader gets the image only: "which parts look AI or pasted in, worst first" and
  a 2x2 "which is the amateur one" against the business's previous piece. Fix what is named, except the client's own
  brand art, which stays as given and is noted in the report.

### Samples sent before a deal: watermark them
A spec piece sent to a business is watermarked so it can't be used unpaid, and the clean master is kept apart.
- `paper_kit.py mark OUT.png --text "<owner name>"` tiles the name diagonally over the whole frame (light fill, dark
  stroke, so it shows on dark and light ground). In an HTML loop, build the same rows in the page and drift them one
  tile per loop so no two frames share a clean pixel; add one larger "SAMPLE · NAME" pass through the main message.
  Over the logo and headline, never only a corner, which a crop removes.
- Write artist and copyright into the file (`ffmpeg -metadata artist=... -metadata copyright=...`).
- Deliver `_SAMPLE` files and a separate `clean_master/`. Say plainly that no watermark is impossible to remove; this
  one costs a redraw of most of the piece. A drifting mark grows a GIF (about 6x here): send the MP4 when the GIF passes
  the upload cap.
