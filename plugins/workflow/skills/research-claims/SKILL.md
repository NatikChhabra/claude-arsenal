---
name: research-claims
description: Tag every research claim CONFIRMED, INFERRED or DEBUNKED with its source, read the whole source before claiming anything about it, say WHEN each claim is true, never inherit a number unchecked, and reframe a failed popular claim honestly as our hypothesis. Use for any research, fact-check, dossier, competitor or strategy breakdown, a script that states facts, or "verify this", "is this true", "check these numbers", "research".
---

# /research-claims

status: beta

Why: research dossiers that read with authority carried claims that did not survive checking: a "retention sag at
minutes 7-12", a third-party estimate quoted as an official figure, an editing rule the subject had publicly disavowed,
a prize amount off by half. When the work's value is being better-researched than the generic version, one unverified
claim is the main risk.

## Tags (every claim gets one)
- **CONFIRMED**: checked against a primary source (the official page, the data itself, the subject's own words, the
  code, the recording at a timestamp). Cite it: link, file:line, or `@<seconds>`.
- **INFERRED**: our reasoning from confirmed facts, or a credible secondary source not yet checked. Say what it rests on.
- **DEBUNKED**: checked and false. Keep it in the project's debunked list (named in CLAUDE.md) so nobody re-imports it.

## Rules
1. **Never inherit a number.** A figure from an earlier dossier, a blog or a summary is INFERRED until you check it.
   Real data the project measured beats blog numbers.
2. **A failed popular claim is reframed honestly**, not dropped and not asserted: "our hypothesis: X" (the user chose
   this over "keep it, labelled as estimate").
3. **Read the whole source first.** Read a transcript, document or recording start to end before any claim about it;
   half a transcript produced a claim that was true only for the first half.
4. **Say WHEN it is true.** Every claim about a source carries its timestamp or date and the span it holds for
   ("X before the midpoint; Y after").
5. **Docs go stale.** Before "not possible" or "it doesn't do X", check the real thing (its UI, source, settings).
6. **Ask what the source can't answer;** never ask what it already answers.
7. **Live context first.** Before building on a topic, check the news, trends and collaborations around it; a missed
   live event made one piece of work stale on arrival.

## Output
A claims table at the end of the research file:

| # | Claim | Tag | Source | True when |
|---|---|---|---|---|

Plus one line per DEBUNKED claim added to the project's debunked list.
