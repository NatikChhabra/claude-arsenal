---
name: trial-prep
description: "Build a complete, court-ready prep pack for one case from the case file (complaint, statements, docket) and the court's own published law and procedure: who's who, deadlines from the judge's order, charges and elements, a timeline, weak points per charge, evidence and discovery list, defense theory with fallbacks, leading cross banks per witness, objections, and second-chair duties. Use for \"I've been assigned a case\", \"prep me for trial\", \"second chair\", \"first chair\", \"case prep\", \"cross questions\", \"defense strategy\", a pasted case docket or complaint, or a court case thread link."
---
# Trial prep

status: beta

The bar: an advocate can walk into court with only this pack and never be surprised by a deadline, an element, or a
witness. Built first for a defense second chair on a 20-count felony case (2026-11-08).

## Inputs
- The case file: complaint, statement of facts, officer statements, evidence list, every docket post (judge's orders,
  counsel appearances, witness lists). Read **all** of it, every page.
- The court's own law: criminal code, procedures of the court, rights section, bar or ethics code, binding precedent.
  Prefer the owner's saved copy of the law corpus; cite file and section for every rule.
- The user's role (first or second chair, which side) and who leads.

## Getting the case file
1. Court forums often need a login. A cloud fetch gets the login page or a 403: do not try to get around it.
   Read the page through the user's own signed-in browser (Claude in Chrome), or a session on their device, or ask
   them to paste it. Pull post bodies with a DOM query (article per post, author, time, body, links) and read long
   results in slices of about 900 characters, because tool output gets cut off past roughly 1,000.
2. Evidence images on third-party hosts may be blocked for the browser tool. List them and ask the user to look.

## Steps
1. **Who's who.** Judge, both sides' chairs, client ID, arresting and primary officers. Check the judge from the
   docket, never from a guess or an earlier case with the same parties (a first pass profiled the wrong judge).
2. **Deadlines.** Copy every clock from the judge's opening order (it beats the general procedures), work out the real
   dates, and put the first hard one at the top of the pack (often "all subpoenas before the scheduler").
3. **Charges and elements.** Full statute text per charge, every element, max sentence, aggravators, stacking. Take
   the text from the court's live published code, not only a saved copy: check its "last amended" line first (a
   stacking point in one pack was written from a copy five weeks out of date, and the new text allowed both charges;
   see the cell-rep skill's law freshness check). Check
   whether party, accomplice or conspiracy liability exists in this code and whether it reaches attempts; a pile of
   counts against a non-shooter often stands or falls on it. Say so plainly if a law doesn't exist.
4. **Timeline.** Number every event from the statements. Note who saw what, and every contradiction between officers
   (colours, times, who fired).
5. **Weak points per charge.** For each element: which fact proves it, who says so, and what's missing. Count named
   victims against the number of counts, and ask for particulars when they don't match. Check forensic results
   (GSR, casings) against each count.
6. **Evidence and discovery.** Use the court's own definitions, not real-world ones (one court defined hearsay
   only as what the witness didn't personally perceive, so a radio call the officer heard himself was a foundation
   fight, not hearsay). One row per exhibit: what it shows, the issue for us (foundation, hearsay, search,
   recording consent, prior bad acts, earlier pleas), and a short list of discovery requests to file now.
7. **Theory.** One main theory in a sentence, two fallbacks (narrow the case, plea), and any affirmative defense with
   its posting deadline. Plea calls belong to lead counsel and the client: say so.
8. **Cross banks.** Per witness, short leading questions with one fact each, built from their own statement.
   Add the objections to have ready, and the affidavit-versus-live-witness problem if the other side plans affidavits.
9. **Speeches.** Check the trial form before writing an opening: many courts' bench trials have no opening
   statements, so the opening becomes talking points for the pre-trial conference and the start of the closing.
   Write spoken lines (short, names, exhibit numbers), check every number in them against the case file, and put
   delivery notes under them.
10. **Conflicts and benchmarks.** Look up co-defendants' cases: who represented them (a lead who defended a
   co-defendant on the same incident is a conflict to raise first), and what sentence they got (the plea benchmark).
11. **Role duties.** What this chair does today, at the pre-trial conference and in court (exhibit log, a tracker with one
   row per count, objections, notes to lead).

## Review before delivery
- Every fact traces to the case file; every rule cites a section; guesses are marked "[my read]".
- The judge, parties and dates match the docket.
- The first hard deadline is the first thing the user reads.
- **Ethics guard:** many bar codes ban AI-written filings or docket posts. The pack is preparation only. Never draft the
  actual filing text; give structure and points, and tell the user to write it themselves.
- Plain language, no em dashes, English unless asked.
- **Blind review before delivery.** Give the PDF and the source files to a reviewer with no build context and ask what
  a nervous reader would miss, what is wrong against the sources, and what could backfire if said in court. On the
  first real run it caught: a co-defendant sentence stated as "time served" when it was 2,050 months served as time
  served (it sank the comparison); leading questions scripted for our own witness; closing lines that contradicted our
  own cross; questions whose answers we did not know. Fix, re-render, review again until nothing must-fix remains.
- Every cross question is closed (yes or no) and its answer is known from the file; a question that depends on an
  exhibit says so in brackets. Questions for our own witness are open.

## Notes / sources
- **The deliverable is a short in-court playbook, not the research.** The owner rejected a 32-page pack as too much;
  the 9-page version that worked has three parts: (1) the case on two pages (story, charges, the defense in one breath,
  a "they say / you say" table), (2) the court script in trial order (cross per witness with pushback lines, the
  acquittal ask, our case, closing beats, an "if this happens, do this" table), (3) objections as their own list
  ("you hear / you say", "when they object to you"). Research, motions and law text stay as source files and feed
  the script. No side notes inside the script. Action items (deadlines, conflicts) go in the chat reply, not the PDF.
- **Second round (same case): organise by job, not only by clock.** The 9-page step-by-step script then came back as
  "badly organised": closing beats and step lists were hard to read live. The layout that replaced it: (1) the case,
  (2) how we win (the ways it ends well, then a table of every strong point: point / where it comes from / how to use
  it), (3) their best points (they say / why it sounds strong / you say), (4) start of trial and the opening in order,
  (5) questioning: one page with every objection, then one page per witness with our questions on the left and
  "object while the State questions them" (objections that witness is likely to trigger) on the right, (6) the closing
  as a full speech to read word for word, (7) verdict and sentencing with the exact words for each outcome, (8) an
  "if this happens" table. Everything read aloud sits in one marked box style, so the reader can find it at a glance.
- Save the pack in a case folder: `00_Case_Brief`, `01_Procedure`, `02_Objections`, `03_Motions`, `04_Duties`,
  `05_Charges_and_Elements`, `source/` (case thread verbatim, law excerpts, prior cases, inventory).
- Prior cases of the same client and the same judge's past rulings are useful, but check the ID number before relying on
  a name match.
