# Songwriting craft: checkable rules

Sources: research/04_production_and_video.md §6 (claims table there). Tags: CONFIRMED = read on the cited page;
INFERRED = our rule built on confirmed facts. Re-check numbers at each research refresh.

## 1. Time to the hook
- Intros in top-10 songs fell from over 20 s (mid 1980s) to about 5 s by 2015; the title arrives ~18% sooner; tempo up
  ~8% (Leveille Gauvin, Musicae Scientiae, OSU). CONFIRMED.
- Hot 100 top 10, 2017: pop reaches the first chorus at 0:39 on average, hip-hop at 0:30; pop intros 9 s, hip-hop 17 s;
  86% of hip-hop top-10 songs had a chorus before the first verse by Q4 2017 (Hit Songs Deconstructed). CONFIRMED.
- 2024 counter-trend: average top-10 length up 20+ s to 3:40 (HSD via secondary). CONFIRMED (secondary).
- **Rules (INFERRED):** a voice or the signature guitar line by ~0:10; the first chorus or hook by 0:30-0:45 (lyric_lint
  warns past ~50 s from the form and BPM); for rap or a hook-led track, put the hook first. A longer build is a choice
  written in the decisions log with its reason (a cinematic character theme may earn it), never a default.
- The first 30 s also feed every Short, Reel and TikTok cut (marketing-studio): a song whose best 15-30 s sit after
  1:30 is harder to promote. Know where the clip moment is before writing verse 2.

## 2. Prosody: words that sit on the music
- "Stressed syllables occur in strong positions of the measure" and unstressed ones on weak beats (Pattison, Writing
  Better Lyrics; Berklee). CONFIRMED (via the Wikipedia "Lyric setting" citation).
- Keep the language's natural stress; verbs usually take it; compound words stress the first part; pronouns and
  -ty / -ly endings are the usual mis-stresses (Coutts, Berklee). CONFIRMED.
- Hindi and Hinglish: keep spoken word order and spoken stress ("bhai", "yaar", "scene kya hai" land where a person would
  hit them). Never bend a word's stress to make a rhyme. INFERRED.
- **Check:** speak each line over a click at tempo. Every stressed syllable on beat 1 or 3 (2 and 4 in a half-time
  feel). An unstressed syllable on a downbeat is a rewrite unless it is a deliberate syncopation you can name.

## 3. Line shape
- Matching lines across verses keep the same syllable count and stress pattern (the melody repeats; the words must fit
  it). lyric_lint.py warns past 4 syllables apart between verses and 3 within repeated sections. Our tolerance is
  INFERRED; tighten it if a singer or a generator trips on lines that passed.
- Lines over ~16 syllables are hard to sing at most tempos (warned). Rap verses are the exception: write them to the
  bar with a syllables-per-bar count instead.
- End-word variety: the same end word 3+ times in one verse reads lazy (warned). Choruses may repeat on purpose.

## 4. The chorus
- The title is said in the chorus, ideally its first or last line, and the chorus repeats at least twice (lyric_lint
  FAIL with one chorus).
- An anchor line comes back inside the chorus (warned when the first line never returns).
- Melody: the chorus sits higher or denser than the verse (a lift a listener feels in the first second of the
  section). The pre-chorus builds tension (rising line, shorter phrases, held chord) that the chorus releases.

## 5. Specific, not stock (the no-slop rule for lyrics)
- Every verse carries at least two inventory items from SONG.md (names, places, objects, numbers, rituals only this
  character has). A line that would fit any song is cut.
- Banned words: the design plugin's one list (`design` skill, references/tells.md), enforced by lyric_lint (FAIL).
- AI-lyric cliches (neon, echoes, whispers, shadows, ignite, embers, soar, symphony, shattered...): WARN; keep one only
  when it is literally in the scene (a real neon sign on a real street the character works).
- No em or en dashes anywhere (FAIL): they also confuse vocal synths and generators.

## 6. Guitar-first writing (the owner's instrument)
- Open-position keys (E, A, D, G, C) ring best; a capo moves them to the singer's range without new shapes.
- Write the riff or the progression first, record it to a click (guitar-capture), then find the top line over it.
- Range check before lyrics are final: the chosen vocal route's voice sets the range (vocal-route §range).

## 7. Collaboration with a generator or a synth
- A generator (vocal-route C) sings what the lyrics imply rhythmically; clean syllable counts and section headers in
  square brackets are what it reads. Run lyric_lint before every generation.
- A synth or a voice conversion (routes A and B) follows the guide's melody exactly: fix prosody before recording the
  guide, not after.
