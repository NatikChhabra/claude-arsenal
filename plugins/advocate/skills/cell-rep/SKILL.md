---
name: cell-rep
description: "Live, fast help for a defense advocate representing a detained client at a police station or holding cell (a \"cell rep\") in a court that publishes its own rules: where to go, what to ask the client and officers, rights checks, charge and stacking review, bail and plea calls, and the live-answer helper set up so every rep needs zero setup. Use for \"cell rep\", \"I'm going to the cells\", \"client got arrested\", \"PD called me\", \"rep at the station\", or any live custody request."
---
# Cell rep

status: beta

The bar: the advocate is standing in the station with the client and officers while you work. Every minute spent on
setup or questions is dead time. First used 2026-11-08 (a public defender called in for a cell rep while live).

## Speed rules (these beat thoroughness)
1. **First reply in under a minute**, one short message: where to go, the first thing to say, the strongest angle.
   No greeting, no recap.
2. Ask **at most one question**, and only if the answer blocks the next step. Otherwise start on the likeliest reading
   and say which one you picked.
3. **Trust what the user sees in game over any wiki.** A station heard as "RPD" was a real station the wiki didn't list.
   A "correction" based on the wiki sent the user to the wrong place. If a location is unclear, tell them to text the
   caller ("which station?"). It is faster than research.
4. Keep the live-answer helper **always in cell-rep mode** (see below), so a new rep never needs a rebuild.
5. Put deep work (case-specific bail and plea plan, charge maths) in a second message, after the charges arrive.

## In the cell: the card to send
- **Intro:** name, role, that they're representing the client. Tell the client to say nothing more to police without
  counsel.
- **Get:** charges exactly as read, arrest time, stop reason and when detention started, how the client was
  identified, when rights were read and whether questioning continued after they asked for a lawyer, the search basis,
  any footage or witnesses, injuries or force, priors, bail or probation status, and the client's own version in private.
- **Check:** does every element fit; any duplicate or stacked counts; modifiers and their conditions; which charges
  allow no bail under this code (list them from the code, never from memory of another court).
- **Plea-first.** Most cell-rep clients plead guilty or no contest at the station, and trials are rare (a bench trial
  at most). The first live client said "forget it" and pleaded no contest mid-argument. So the advocate's main job is
  the best deal before the plea, in this order: strike charges that don't fit their elements or stack illegally, then
  remove modifiers whose conditions aren't met (name the condition the officer skipped), then ask for discretionary
  modifiers to be dropped, then ask for lower months and fines with reasons. Read back the final totals, and only then
  does the client plead. Suggest a trial only for a strong defence, and say what it costs.
- **Quote, don't paraphrase.** When an officer or prosecutor reads a statute aloud, they often stop before the
  condition that helps the defence (a location rule read without the victim-status condition that follows it). Keep
  the full statute text in the helper, and answer with the exact words they skipped. Paraphrased answers get "you're
  saying the wrong thing" from the other side.
- **Options:** guilty goes straight to sentencing (argue low end: first offence, remorse, cooperation). Not guilty
  means bail is decided (the benchmark is often the maximum fine). Deals stay open until trial. **Never let the client waive
  the right to appeal the sentence.** The client decides the plea, and the advocate lays out the options.
- **Clocks:** copy the court's own deadlines after a not-guilty plea (docket posting, declaring representation).
  Missing one can dismiss the case or default the defense.
- **Ethics guard:** many bar codes ban AI-written filings and docket posts. Give points; the user writes the filing.

## Live-answer helper (always ready)
If the user runs a live meeting assistant that listens and answers on screen, set it up once so it never needs setup:
- The mode prompt opens with **DEFAULT MODE: CELL REP**: unless a case number or client is named, every transcript is a
  new cell rep, and saved cases are **background only** ("never bring their facts into a cell rep"). A saved case
  labelled "ACTIVE CASE" leaked its facts into unrelated reps.
- The mode prompt says **who is being asked**. On the first live rep, an officer asked the advocate for ID and a
  security search before entering the cells, and the helper told him to refuse "without probable cause". That is
  facility security, not a search of the client: the advocate complies politely. Search rights are argued only for the
  client, and a search incident to a lawful arrest needs no warrant. The angles there are probable cause for the arrest
  and how far the search went.
- After each rep, read the helper's question/answer log and grade a few answers against the law. Fast, relevant
  answers can still be wrong about who is speaking to whom.
- The first line of each answer is the one sentence to say now. Then 1 to 3 lines of authority (section, months, fine).
- Answer from the user's own plan (account mode) with thinking off. Measured: time to first word dropped from 9.5 s to about 3 s.
- Launch through one shortcut that starts the helper before the assistant. If the assistant is opened on its own,
  answers come without the law, or not at all. When the user says "it's on", check that both processes are running and
  the assistant's model points at the helper.
- After a context edit, rebuild and restart **only the helper** (the restart loop brings it back in seconds) while
  the assistant is idle. Run one tiny test question, never a whole suite, and confirm no saved-case facts appear.

## Review before sending
- Speed rules followed (first message short, one question at most).
- No law from another court or real-world law unless the court adopts it. Guesses marked "[my read]".
- No em dashes; plain spoken English.
