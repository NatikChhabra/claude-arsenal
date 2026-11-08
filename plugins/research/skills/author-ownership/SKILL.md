---
name: author-ownership
description: When an AI agent ran much of a study, build the human author's real understanding and a written contribution that venues accept; short Socratic sessions on the baseline, the key design choice and the main weakness, analogies and multiple choice when stuck, the author's own hypotheses kept, and an interpretation paragraph in their words with only facts and grammar fixed. Use for "help me understand my paper", "prepare me for reviewers", "the venue is worried about AI use", "what did I contribute".
---

# /author-ownership

status: beta

Why: conference chairs (2026) told an AI-assisted author that full disclosure is required but not sufficient:
choosing the question, directing the agent and taking responsibility do not meet their AI rules. The author must
validate the methods and results, interpret the findings and make a substantive contribution. "I read it and
understood everything" is not evidence; what the author can explain and write is.

## Inputs
- The paper, its key numbers, its limitations section.
- The author's time: sessions of about 15 minutes; stop when they are overwhelmed and save progress.

## Steps
1. **Say it straight:** the venue's concern, what reviewers will likely do, and the choice: put in the hours, or keep
   it a preprint. Never pretend disclosure alone is enough.
2. **Three questions** a reviewer would ask, one at a time, answers in the author's own words (any language mix):
   1. What the main measure is and what the baseline means.
   2. Why the key design choice was made (for a style study: why compare with models trained before the change).
   3. The main weakness and the check that addresses it.
3. **When an answer is off,** name what is right first, then the one fact that is wrong. If they are stuck, switch
   to an everyday analogy (catalogues for model generations, a locked answer sheet for a model that cannot have
   copied later writing), then a fill-in-the-blank, then multiple choice, then ask them to say it back.
4. **Keep their own ideas.** A hypothesis the author proposes that the paper did not make is the most valuable output;
   check it against the literature and say if it matches a known idea.
5. **Write their paragraph.** Turn their explanations into an interpretation or discussion paragraph: fix facts and
   grammar only, keep their ideas and order, mark what was changed, and ask them to confirm each sentence is
   something they believe and can explain.
   - **One-sitting version** (when the author wants it all done at once): four parts, three questions each,
     all three answered in one message: Introduction (what earlier work did with the baseline, why the reference
     choice matters, who should care), Limitations (the AI system's own role in the study, use versus adoption of a
     style, scope of the data), Conclusion (the result in two sentences, one question for future work), and the
     contribution statement. Save each paragraph to a file as soon as it is drafted.
   - **Fix the reason, keep the point.** When the author reaches a true conclusion by a wrong reason ("that model
     barely matters, it is a small one"), give the true reason with the number read from the result files ("it is
     one of 19 models; without it the gap is still X"), and say what does depend on it.
6. **Make it visible in the paper:** the author's paragraph goes into the Discussion; where possible the author
   re-runs a key result and checks the numbers; the AI-use statement says what the author validated and wrote.
   - **Never write an overclaimed contribution.** Under pressure an author may say "I did everything, the AI only
     wrote code". Check every claim against the record (git history, the paper's own disclosure, what venues were
     already told) and write only what is true. Say plainly why: a statement that contradicts a public record is
     what sinks a paper, and the honest "disclosed, then learned and wrote these sections" is the stronger story.
     Also correct statements the work has made stale (for example "not checked by a human" after the author did).
7. **Save** a file listing what the author can now explain, their hypotheses and the paragraph, for the next session.

## Review before delivery
- The author answered each question correctly in their own words at least once.
- The paragraph contains no idea the author did not express or accept.
- The paper's contribution statement matches what the author actually did.

## Notes / sources
- Venue questions and replies: `research-outreach`.
