---
name: personal-edit
description: Make a private edit for someone's friends or family (a birthday video, a roast, an anniversary, a farewell, a wedding or reunion montage) at the same bar as a published video. Read everything given once, write a beat plan, ask only one-word questions with options, show one short preview of the hardest section, render, run blind + design + sound reviews, deliver big-screen, HD and phone copies, and write the person's PLAYBOOK.md so next year's edit starts ahead. Use for "birthday video", "edit for my friend", "make a video for <name>", "roast video", "anniversary edit", "farewell video", "personal edit", or a repeat edit for the same person.
---

# Personal edit

status: beta

Same tools and the same bar as a channel video: the same render pipeline and its checks, the same sound rules, the same
review loop. Craft lessons flow both ways: a lesson learned here goes into the shared style log, and the channel's lessons
apply here. Visual, motion, text and sound rules: **skill design, references/edit.md** (and its review checklist for the
design review).

**Privacy first:** the person's info, photos, chats, voice notes, jokes and personality never leave the private project
folder. Never put them in a shared repo, a public artifact, a prompt to an outside service, or a craft log (log the lesson,
never the person).

## Where things live
- Project folder: `<private root>/<Name>_<Occasion>_<year>/`, outside any shared repo. Sources, beat plan, EDL, renders
  and the playbook stay there.
- Per person: `<project>/<NAME>_<OCCASION>_PLAYBOOK.md` from [references/playbook-template.md](references/playbook-template.md).
  A repeat edit (a yearly birthday) starts by reading the last one.
- Render tools run from their own install on the project's EDL with absolute paths; the same pre-render check and delivery
  oracle run as on the channel.

## What is different from a channel video
- **Private:** music has no licence limit (the subject's own favourite songs first), but nothing is bought and no login
  is used.
- **Swearing:** uncensored only when the requester says so for THIS edit; default = the channel's bleep rule.
- **The requester's identity** stays off screen if they are faceless on their channel. No brand character unless asked.
- **A narrator voice is allowed:** offer 2-3 short samples, the requester picks; it must pass a blind read (nobody can tell
  it is synthetic) or it is out.
- **One interim:** a 10-20 s preview of the hardest section, so the look is approved before the full render. Nothing else
  interim reaches them.
- **Outputs:** a big-screen master (1440p60, or 4K when it plays on a TV), a 1080p copy, and a phone copy under 20 MB
  (messaging apps recompress anything bigger).

## Defaults that worked (a birthday edit approved as "perfect"; replace with the requester's taste once known)
- **Smooth chaos:** high energy but not loud; the energy comes from cuts, pacing and design. One beat per punchline (too
  fast = missed).
- **Readability first:** chats and text big enough on a phone; no zoom, shake or RGB split while words matter.
- **Real-chat recreations** in the real app's look, bubbles typing in on the beat, never a crooked pasted screenshot.
- **Look:** a punchy grade, light grain, a soft glow; a blurred photo of the subject as the backdrop (never a busy one).
- **Text:** a heavy impact face on true meme captions; bold white with ONE accent-colour keyword for statements.
- **Reactions:** white-border cut-out stickers popping at the side, never covering the chat; never a sticker or emoji on
  every cut (each one placed because the requester asked or the beat earns it).
- **The running gag** = the subject's real obsession or catchphrase, from the requester's notes, never invented.
- **Sound:** real nameable sounds only (app tones from a named source, real foley), each on the right beat; a celebration
  sound only on a real win or wish; never silence.
- **A fake-emotional turn** ends in 1-2 sincere lines, not a speech. An ending the requester approved is never touched
  again.
- **Usually disliked:** generic meme templates, busy backgrounds, tiny face crops, overused meme sounds, game-show sounds on
  gags, stock whooshes.

## Capability menu: pick by what you are given
| Input | First choice | Also |
|---|---|---|
| Photos only | 2.5D parallax (a depth map, then a slow camera move through the photo) for hero shots; the subject cut out and popping over their own blurred photo for reactions | eased Ken Burns as filler; collage grids on the beat; a photo "comes alive" with a cut-out + parallax + a real sound; text-led storytelling over blurred backdrops |
| Chats | A recreation in the app's own look, bubbles typing in on the beat, the punchline bubble held | a zoom on the original only when it matters (a timestamp, a deleted message) |
| Voice notes | The real voice under a waveform card or the speaker's photo; the punchline gets a hold | big captions in the language they speak |
| Video clips | Cut tight like a channel video (snaps, whips on a real move, a freeze + sticker, a ramp on a hit) | stabilise shaky phone clips; track a sticker to a face |
| Memes / stickers | White-border cut-outs at the side, popped on the punchline | impact captions on true meme frames only |
| Songs | The subject's own songs as beds, cut on the bar | a narrator over a low bed |
| A song as the whole piece | A kinetic lyric video: lyrics timed to the sung words (a vocal stem gives word times), cuts on the bars, a palette per section | text behind a cut-out of the subject |
| A scene that never happened | Generated imagery or toon 3D only if it passes a blind read (nobody can tell it is AI); otherwise build it from real photos with depth moves | never a real person's face invented |
Optional tools: a beat tracker for bar lines, a stem splitter for vocals, a monocular depth model for parallax, a
segmentation model (SAM 2, BiRefNet) for cut-outs, frame interpolation (RIFE) for smooth slow moves.

**Concept first:** one idea the whole edit is about, said as a visual mechanism ("the number that won't go away"); 1-3
motifs that change state each time they return; intensity rising section by section with >= 3 real holds; an ending that
is an idea, not a fade.

## Workflow
1. **Read EVERYTHING given** (photos, chats, memes, voice notes, notes, the old playbook) once, end to end. List the jokes,
   the running gag candidates and the gaps.
2. **Beat plan:** sections, the running gag, where each punchline lands, music per section. One file in the project folder.
3. **Ask only what blocks the plan,** as one-word questions with 2-4 options each and your pick marked. Never ask what the
   material already answers.
4. **Preview:** 10-20 s of the hardest section: the look, the text size, one gag with its sound. The requester OKs the look
   before the full render.
5. **Full render, then three FRESH reviews** (helpers that write findings to files): a blind review (story and laughs, as
   a stranger), a design review (skill design), a sound review (fake, glue, buried words, silence, wrong-beat sounds).
   Fix every applicable rubric row to 8.5+; re-review what changed.
6. **Deliver** the three outputs in the project folder; give the requester the paths.
7. **Write or refresh the PLAYBOOK.md;** put craft lessons (never the person) into the shared style log; delete the
   project's intermediates (proxies, test renders, temp audio) and keep sources, EDL, playbook and finals.
