# Mistake taxonomy (9 codes)

Copy this into the vault as `<root>/reference/taxonomy.md`. It is the **only** place the codes are defined; any second copy drifts.

Validated in the source vault against 79 code-instances over 60 logged rows from 7 papers in 5 subjects: no mistake shape was found that these 9 codes could not express.

| Code | Type | Meaning |
|---|---|---|
| **K** | Knowledge gap | Did not know the content, including a genuine recall slip ("knew it, blanked") |
| **R** | Assertion-Reason link not tested | An A-R item answered without the three steps: (i) is A true? (ii) is R true? (iii) does R *explain* A? Step (iii) is the one skipped |
| **D** | Directive misread | Answered "explain" as "describe", missed "with example", answered half of a two-part question, ignored *compare / distinguish* |
| **F** | Format fail | No points, no headings, wrong word count, wrong genre format (letter, notice), paragraph where points were needed |
| **T** | Terminology miss | Idea in ordinary words, missing the keyword the marker scans for, including a wrong statute year or article number |
| **E** | Example missing | Right concept, no illustration, case, data or named textual detail |
| **S** | Structure fail | No intro-body-conclusion, rambling, circular, no link back to the question |
| **P** | Pacing | Ran out of time, left blank, rushed the last section |
| **C** | Careless | Misread the question, wrong option, wrong number of points |

## How codes are assigned

- **The plain-English "what went wrong" is the required field. The code is optional.** Leave it blank unless the reason actually matches a definition above.
- A code applied because it "feels adjacent" is worse than a blank: it corrupts the tally and every cross-subject rule it feeds. The source vault's worst audit finding was exactly this (a directive skip tagged C instead of D, unnoticed for weeks; a code whose definition matched none of the rows using it).
- R originally meant "recall slip". Every row using it turned out to be an A-R failure, so it was redefined to match the evidence and recall slips now log as K. Redefine a code when the data says so; never stretch rows to fit.
- P stayed at 0 across short unit tests; keep it anyway, it matters on full-length papers.
- A multi-code row ("K + F") counts once for each code in every tally.

## The split that matters (post-mortems)

| Bucket | Codes |
|---|---|
| Did not know it | K |
| Knew it, wrote it badly | R, D, F, T, E, S |
| Time / careless | P, C |

If the middle bucket is biggest, the fix is answer format, not more revision. (The source template put R with K; once R meant A-R link-testing it is an execution failure, so it sits in the middle here.)

Review the taxonomy against a machine recount (`tallycheck.py`) every few months, or sooner if a paper produces a mistake none of the codes fit.
