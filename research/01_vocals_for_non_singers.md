# Vocals for a guitarist who can't sing (2 Nov 2026)

## The problem
The owner plays guitar, writes, and loves singing, but his sung pitch and tone aren't release quality. The goal is a
vocal that sounds great AND keeps the song his: his melody, words, phrasing and guitar.

## The five routes (used by the `vocal-route` skill)
1. **Guide + pitch fix + voice conversion.** He sings/hums the melody anyway (wrong notes are fine), pitch correction
   snaps it to the melody, then a voice-conversion model (RVC via Applio; Seed-VC SVC) swaps the timbre. Keeps his
   phrasing and emotion, which is what makes vocals feel human. Needs a target voice he owns or licensed. Seed-VC is
   archived (Nov 2025, GPL-3.0), so prefer a maintained tool.
2. **Vocal synthesis.** Synthesizer V 2 or ACE Studio (paid) or OpenUtau + DiffSinger (free): notes + lyrics in a
   piano roll. Most control, zero singing. Takes tuning effort to sound alive; language support varies (check Hindi).
3. **Generate from his guitar.** Suno (upload audio), ACE-Step 1.5 (local, MIT, cover/repaint/reference audio, LoRA on
   ~8 songs, runs on AMD via ROCm 7.2), ElevenLabs Music. Fastest; least control over exact melody; licence terms differ.
4. **Rap/spoken word** in his own voice: no pitch needed.
5. **A real singer** from the RP community or hired: best human result, needs consent and credit.

## Starting recommendation (to test, not yet tested)
- Demos: route 3 with ACE-Step 1.5 locally (free, private, MIT) and Suno for comparison, his guitar as reference audio.
- Releases: route 1 or 2 so the melody is exactly his, with the chosen tool fixed per "artist voice" for consistency.
- First test when music work begins: one chorus through routes 1, 2 and 3; blind-compare; record results here.

## Rights checklist
- Voice models: only his own voice or licensed/consented voices; never a real artist.
- Generators: confirm the current plan allows public and commercial release before distributing.
- Platforms: follow AI-disclosure rules on Spotify/YouTube/TikTok.

## Sources (fetched 2 Nov 2026)
- ACE-Step 1.5: https://github.com/ACE-Step/ACE-Step-1.5 ; AMD blog (4 Feb 2026):
  https://www.amd.com/en/blogs/2026/commercial-grade-ai-music-generation-on-amd-ryzen-ai-and-radeon-ace-step-1-5.html
- Seed-VC: https://github.com/Plachtaa/seed-vc
- Overviews to re-read when testing: https://freebeat.ai/articles/best-ai-singing-voice-generators-in-2026-vocal-synths-for-original-songs-and-characters ,
  https://www.soundverse.ai/blog/article/best-ai-vocal-generators
