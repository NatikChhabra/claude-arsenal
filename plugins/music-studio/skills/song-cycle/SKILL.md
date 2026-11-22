---
name: song-cycle
description: >-
  Start here for any new song: the owner's two-week song cycle from a riff or an idea to a released track, where he
  writes, plays and sings every part and Claude only sets up, teaches, measures and assembles his own takes. Gives the
  14-day plan, who does each step, which skill and tool runs it, the gate that ends each stage, and how to keep the
  song board in step. Use for "new song", "let's make a song", "start a track", "what's next on my song", "I want one
  song every two weeks", or when a song has stalled.
---

# song-cycle

status: draft (the stages and gates come from a real single made end to end on one acoustic guitar in Nov 2026; the
14-day clock is new, so the day counts are the plan, not yet a measured average; promote to beta after the first song
run on this clock)

The owner wants a finished song about every two weeks, and he wants each one to feel like his own art: "I want my
own creativity, my own vision, not the AI's vision." So this skill is a schedule and a division of work. He is the
artist. Claude is the engineer, the teacher and the second pair of ears that measures what it can't hear.

## 1. Whose hands (read before every stage)
| His (always) | Claude's (on his material only) |
|---|---|
| The idea, what it's about, the references (from his own playlist) | Opening SONG.md and the board card, the date for day 14 |
| Chords, form, melody, every word | Lint for cliches and syllable drift, first-chorus time, questions that help him choose |
| Every sound: guitar, voice, body taps, claps, anything else he records | Play sheets, slow play-alongs, click tracks, the take check right after each take |
| Which take, which tone, which section order | Cutting his takes onto the grid, assembling repeats, drums from his own taps, mix numbers |
| Every "does this sound right" | Measurements (loudness, clicks, harshness, timing), never "it sounds" |
| The cover idea and the pick | Laying out his photo or drawing, file specs, embedding |
| Uploading the release | The release kit with every field filled in |

Hard lines, unless he asks for one himself in that song: no AI singing or voice conversion (vocal-route route F is his
default), no generated instruments or stems, no lyric lines written for him (Claude may list rhymes or ask "what
did she actually say?" when he asks for help, and marks anything it typed as a suggestion until he rewrites it), no
sample libraries in place of a part he could play or tap. Guitar only: beats, pads and textures come from his guitar
too (body taps, slaps, chucks, harmonics, swells), never from another instrument he didn't play.

**The tone is his.** After the first single he said everything worked except the guitar tone processing Claude had
done (an exciter and big EQ moves on a soundhole-pickup take). So: he picks the tone at the source, on his amp or in
his amp-sim plugin. Claude may set up 2-4 tone options in the plugin's own controls when he allows it, never edits an
app's files, and he chooses by ear. After the take Claude does clean-up only (level, noise, clicks, gentle corrective
EQ); any change that alters the character of his sound goes to him as a level-matched before and after, and the
"before" wins unless he picks the change. Offer at most 3-4 options for any creative choice and let
him pick; say which one you would take only if he asks.

Teach while doing: each time Claude does a studio step (a click, a level, a fade, a crossfade, an EQ cut), say in one
line how he would do it himself in his DAW, so the next song needs Claude less.

## 2. The 14 days
| Days | Stage | He does | Claude does | Skill and tools | Gate to move on |
|---|---|---|---|---|---|
| 1 | Idea | a riff or voice memo, one line of what it's about, 2 reference songs he plays a lot | SONG.md from `templates/SONG.md`, card on the board, day-14 date | song-from-idea §1, `listening_taste.py` | the one line and the riff exist |
| 2-3 | Write | chords and form on the guitar, hums the melody, writes the words | lint, first-chorus time, syllable counts, range check on his hum | song-from-idea, `lyric_lint.py`, `voice_range.py` | lyric_lint 0 FAIL, he can play and hum it start to end |
| 4-6 | Practise | plays to the sheet until it's steady | one play sheet and a slow and a full-speed play-along from his chords | guitar-capture §0, `guitar_level.py` | one clean run at full speed |
| 7-8 | Record | picks his tone, then records each part to the click (and his voice, if the song has words) | studio check before the first take, `take_check.py` after every take, redo list on the spot | studio-setup, guitar-capture §1, `take_check.py`, `beatmap.py` | every take PASS or WARN, nothing FIX |
| 9-10 | Build | listens to each section, says keep or change with a timestamp | assembles from his takes only: loops, hit-by-hit re-play, a drum kit from his own taps | produce-arrange, `loop_assemble.py` | the energy map holds, he approves each section by ear |
| 11-12 | Mix and master | judges on headphones and the phone speaker; plays it to 2 people who don't know how it was made | balance, EQ, the master chain, every measured gate | mix-master, `loudness.py`, `lookahead_limit.py`, music-review | 0 gate FAIL, his OK, the listeners' words written down |
| 13 | Cover | picks the photo or drawing, chooses from 4 directions | lays it out, hides his face if it's his photo, embeds it | design (video.md covers), `still_check.py` | he picks one |
| 14 | Release | uploads it himself | FLAC and MP3 with the cover, CREDITS.md, the release kit | mix-master §4.5, marketing-studio release-rollout | it's submitted |

Two weeks is his rough plan, not a deadline: some songs take a month, and a board or a reply never says "behind" or
"late". Keep the pace with overlap, not with rushing: start the next song's Idea (day 1) while this one is in Mix. If a stage
slips, cut scope, never the bar: fewer layers, a shorter song, one cover direction he already likes. Never skip the
take check, the gates or his listen.

## 3. Every stage
- Open the stage by reading SONG.md (`## Cycle` says where the song is) and what he said last, with its timestamps.
- Close the stage only on its gate. Write the date, the gate result and his words into `## Cycle`, then move the board
  card (if he keeps a song board with a data store, update that song's `stage`, `day` and `next` fields there too, and
  never move a card he moved himself back).
- Anything he records goes to `songs/<slug>/raw/` untouched (studio-setup §5 has the layout). Builds read from there.
- When he rejects something, ask what he heard and where (a timestamp), then measure that spot before changing it
  (mix-master §3 has the cases that came up before).

## 4. When a song stalls
- Day 4 and no full lyric: play him back his own hum over the chords and ask for one line at a time, his words; or make
  the song an instrumental, which is a real choice, not a failure (his first single was one).
- Takes keep failing the check: run studio-setup §6 (the 1-minute rig check) before asking for another take.
- He's not feeling it: ask which of his references it should be closer to, and change one thing.

## 5. Notes
- Claude cannot hear. Anything audible is his call or a listener's, backed by numbers (music-review).
- The first single (Nov 2026) took one long weekend of rebuilds because every lesson was new. Those lessons now live
  in guitar-capture, produce-arrange and mix-master; read them instead of rediscovering them.
