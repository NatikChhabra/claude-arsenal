---
name: research-outreach
description: Contact researchers, conference chairs and news desks about a paper so the emails get read and nobody is annoyed; official addresses only, one specific question, plain AI disclosure, no citation asks, draft-only with link checks, honest follow-up rules, and what replies to expect. Use for "email researchers about my paper", "ask the conference if I'm eligible", "get my research in the news", "who should I contact", "follow up".
---

# /research-outreach

status: beta

Why: busy researchers and newsrooms ignore or resent generic, AI-sounding mail. What worked: short notes that name
one of the recipient's own papers and ask one real question. What did not: cold emails to news desks for a preprint
story, which mostly went unanswered.

## Inputs
- The paper's public link (concept DOI), a two-sentence summary, the AI-use disclosure sentence.
- The account to send from (check which account the mail connector is signed in to before drafting).

## Steps
1. **Addresses only from the person's or outlet's own page** (homepage, faculty page, a recent paper's author line,
   the outlet's contact page). Never guess or build one from a pattern; record the source URL next to each.
2. **Researchers** (one email each):
   - Name one of their papers and how yours uses it; ask one question only they can answer.
   - About 120 words, plain, no flattery, no stock phrases; the AI disclosure in one honest line.
   - Never ask for a citation (citation rings are misconduct). An endorsement ask goes only after they reply warmly.
   - Send 2 or 3 a day. No follow-up to a researcher who did not reply; a reply that says no gets a short thank-you.
3. **Venues:** ask the chairs in writing early whether the author is eligible (school students, sole authors) and
   whether the AI use is acceptable. Expect: eligibility yes, AI use questioned. Answers so far (2026): disclosure is
   required but not sufficient; the author must validate the results, interpret them and write their own
   contribution (see `author-ownership`). Ask before paying or submitting anywhere.
4. **Press:**
   - Cold email to news desks rarely gets a reply for a preprint story. Use official tip addresses, the outlet's
     language preference (English is fine for most), the local angle first, and a WhatsApp number when the outlet's
     contact page lists one: local reporters read WhatsApp.
   - Never inflate: "preprint, not peer reviewed", "submitted", never "published" or "accepted" until true.
   - One follow-up at most, after 10 or more days, with one new fact. Then stop until there is real news; an
     acceptance is the hook worth re-pitching to everyone.
   - Never quote a private email (a researcher's praise) to the press without that person's permission.
   - Business, grievance or letters-only inboxes are not tip lines; skip them. Calls and office visits only if the
     owner wants them.
5. **Draft only.** Create drafts, label them (Researchers, Venues, Press, Accounts), fix and verify links (connector
   gotcha below), then tell the owner which drafts are ready. The owner sends.
6. **After sending:** check Sent for the clean link and the inbox for bounces the same day; mark dead addresses in the
   contacts file so nobody reuses them.

## Review before delivery
- Every address has a source URL; no recipient gets two near-identical emails.
- Each draft re-read from the mail side shows clean links (no `google.com/url?q=` wrappers) and the right sender.
- No claim beyond what is true today; no private quote without permission.

## Notes / sources
- Mail connector link rewriting and the fix: `workflow` plugin, `docs/gotchas.md` ("Connectors").
- Release steps and profiles: `paper-release`.
