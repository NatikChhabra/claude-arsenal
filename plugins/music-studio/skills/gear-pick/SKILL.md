---
name: gear-pick
description: >-
  Pick ONE instrument or music-gear setup for the owner to buy: a few questions in one message, his real listening
  history instead of a typed list, the whole-setup budget (guitar plus whatever makes it heard), live store prices read
  on product pages, then one recommendation with links, stock and a total. Use for "which guitar should I buy",
  "recommend an electric", "best guitar under 30k", "what amp or interface do I need", or any music gear purchase.
---

# gear-pick

status: beta (used on one real purchase, Nov 2026: an electric guitar setup in India under a hard cap; the listening
tool was tested on his real player cache)

The owner wants one answer he can buy today, not a buyer's guide. Twice in the first real session he sent a tiered
answer back ("give me one guitar"), and his budget dropped sharply once he saw full-setup totals. So: totals from the
first reply, one pick at the end.

## 1. Ask once (one message of short questions; a second round only if he asks for it)
- Where and how he buys (country, online or a shop he can visit, and whether everything must come from one store: one
  cart can rule out the cheapest item elsewhere).
- The hard cap for EVERYTHING (instrument, amp or interface, cable). Ask "hard limit or stretch?".
- What he already owns and loves (keep it, build around it, never sell him a duplicate).
- Room, headphones or both, and will he play for people. That decides a practice amp, a USB interface into his DAW,
  or both. When he wants both, an amp with USB audio built in (Fender Mustang LT25, Boss Katana Gen 3) is one box
  instead of two.
- Feel: body size, weight, neck. Ask about looks only if he has said looks matter.
- Do NOT ask what music he listens to when a library is reachable: read it (step 2). DO ask what he plays or wants to
  play on the instrument: what he plays is not what he listens to. In the first real session the library was all
  clean indie, and only after the pick did he mention classic hard-rock riffs, which moved the pick to HSS.
- Ask about accessories he needs (a strap if he stands, a cable) in this same message, so they are inside the cap.
End with a sample short answer ("<city>, 25k hard, headphones, smaller") so he can reply in one line. If he answers
"I gave you everything", stop asking and decide.

## 2. Read his taste from evidence
- Desktop player cache: `python ${CLAUDE_SKILL_DIR}/../../tools/listening_taste.py <player-data-dir>` (Feishin:
  `"%APPDATA%/feishin"` on Windows, quoted; stage the `IndexedDB` files when the folder is on his PC). It prints the songs and
  the artists by song count. A playlist export or a "recently played" screen works too.
- Map the songs to a tone family, then to the instrument:

| What he plays | Tone | Instrument |
|---|---|---|
| Clean, jangly indie, bedroom pop, funk, 80s pop | single coils, chorus, reverb | Strat (three single coils) or Tele |
| Classic rock riffs plus clean pop | one humbucker for drive | HSS Strat-style |
| Hard rock, metal | humbuckers, high gain | dual humbucker |
| Fingerstyle, slaps, chucks, harmonics | acoustic body | acoustic or thin-body electro-acoustic |
| Flamenco, nylon fingerstyle | nylon strings | classical |

- Name his songs in the reply as the reason ("three single coils is the sound of 505 and Daylight"). Say what his
  techniques become on the new instrument (chucks on an electric become funky muted strums).

## 3. Budget the whole setup
- An electric is silent without a way to be heard: a practice amp, OR a USB audio interface into his DAW with a free
  amp sim (plays through PC speakers in the room and headphones at night). The interface route also records.
- Windows interface rule: it must ship its own ASIO driver. Behringer UM2 and UMC22 point to ASIO4ALL, so skip them for
  live playing. Focusrite, Audient, M-Audio M-Track Solo, PreSonus and Arturia ship ASIO drivers.
- Free tone (checked on the makers' pages, Nov 2026): Guitar Rig 7 Player (amp, chorus and reverb in one, needs a free
  Native Instruments account); the TONE3000 plugin with NAM captures (see guitar-capture section 4); Valhalla
  Supermassive for big reverb; TAL-Chorus-LX for chorus.
- Amp features can beat price: ask whether he wants to save his own sounds (presets) and control the amp from an app.
  In the first real session a cheaper amp with the same USB recording was turned down for the one with preset saving.
- The computer cable is part of the setup: check the amp's or interface's USB port (micro-B vs USB-C) and whether a
  cable is in the box, and say which cable he needs. A buyer whose phones are all USB-C may prefer a USB-C amp.
- Price the cable (about 3 m) and a strap if he stands, from a store page, in the first total. In the first real session
  adding them at the end pushed the leading guitar over the hard cap and flipped the pick; a guitar that leaves room for
  them is better than one that wins on paper and breaks the cap.

## 4. Check prices live, on product pages
- Never quote a price from memory. Open each product page and read the chosen variant's price, MRP and "Sold Out" label;
  note the date.
- India, learned the hard way: Bajaao search cards often show a cached or sold-out variant's price, so trust the
  product page; amazon.in refuses automated fetching; Johns Music shows "Add to cart" and "Notify me" on the same page,
  so tell him to WhatsApp before paying; small dealers ask buyers to confirm stock by phone.
- An MRP far below every other store is a stale listing, not a deal. "Used Gear Available" links on Bajaao go to a
  separate used marketplace (connect.bajaao.com), not an open-box listing.
- The web-fetch tool has an hourly page budget shared by every agent in the session (about 100 pages). A broad
  parallel sweep of stores can burn it before the finalists are verified: search once, then open product pages only for
  the two or three finalists, and check the computer cable early.

## 5. Deliver one pick
- One line up top: the setup and the total against his cap.
- Each item: link, price, stock (or "confirm stock with X"), one reason tied to his songs or hands.
- One line on the obvious alternatives and why not (sold out, over the cap, wrong pickups for his music).
- Anything he asked for outside the brief (strings, a setup for his old guitar) goes in one short separate paragraph.
- No "best overall / best value" tiers.
- Add one "how it connects" line for a beginner: guitar, guitar cable (1/4" jack), amp input; amp USB to the PC. Say
  that an amp's "line in / streaming" jack is an input for playing songs through the amp and does not send the guitar
  to the PC (a beginner in the first real session assumed it did).

## Review before delivery
- Total within the hard cap, with the cable counted?
- Every price read from a page today, every stock state stated or flagged?
- Exactly one pick, matched to his listening evidence and to the gear he keeps?
- Plain words: a beginner reads "USB box that plugs your guitar into the PC", not "interface with Hi-Z input".
