---
name: vocal-route
description: Choose and run the best way to get great vocals on a song when the owner (a guitarist who can't sing) won't be the final sung voice. Use whenever a song needs vocals.
---
# Vocal route

status: draft

The owner loves singing but can't sing well. This skill picks how the vocal gets made so the song still sounds like
his song. Full comparison and sources: `research/01_vocals_for_non_singers.md`.

## Routes (pick per song; mix routes when useful)
| Route | He provides | Tool options | Best when |
|---|---|---|---|
| A. Guide + voice conversion | a rough sung, hummed or spoken guide of the melody (pitch can be off; pitch is fixed after) | pitch-correct the guide, then RVC/Applio or Seed-VC with a voice model he owns or licensed | he wants his own phrasing and timing, a consistent "artist" voice across songs |
| B. Vocal synthesis (draw it) | melody notes + lyrics | Synthesizer V 2, ACE Studio, or free OpenUtau + DiffSinger | full control of every note, clean pro result, no singing at all |
| C. Generate from his guitar | his guitar recording or chords + lyrics | Suno (audio upload/cover), ACE-Step 1.5 local (MIT, AMD ok: cover, repaint, reference audio), ElevenLabs Music | fast demos and full songs; check each service's licence before release |
| D. Rap or spoken delivery | his own voice, rhythm only | his mic + light processing | the style allows it; no pitch needed |
| E. A real singer | the song sheet + guide | an RP community singer or a hired session vocalist | the best human result; needs credit and consent |

## Steps
1. Read the song sheet from `song-from-idea`.
2. Recommend one route with the reason (style, language, deadline, how much control he wants). Hindi or Hinglish:
   test the chosen tool on one chorus first; pronunciation varies a lot between tools.
3. Run the route on the chorus only, review, then the full song.
4. Pitch and timing clean-up, then hand the stem to `mix-master`.

## Rules
- Only voices he owns or has written permission to use. Never clone a real artist.
- Record which tool and model made each vocal in `songs/<slug>/CREDITS.md` (needed for licences and future fixes).
- Blind check: play the chorus to someone without saying how it was made. If they say "AI", fix it before release.
