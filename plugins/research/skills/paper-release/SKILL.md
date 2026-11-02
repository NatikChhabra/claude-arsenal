---
name: paper-release
description: "Take a finished research paper to a citable public preprint and update every researcher profile: pre-release audit, GitHub release to a Zenodo software DOI, a separate readable Zenodo preprint record, ORCID works, Google Scholar, LinkedIn Publications and Featured, and arXiv (endorsement, under-18 consent, source package). Use for 'release my paper', 'get a DOI', 'put it on arXiv', 'add it to ORCID / Google Scholar / LinkedIn', 'make it citable'."
---

# /paper-release

status: beta

Why: a paper that is only a PDF in a repo is hard to read, cite or credit. Each platform has a trap that cost real
time (a wrong co-author pulled in by autocomplete, a 0-byte upload, a Scholar profile that never appears in search,
an arXiv endorsement that was refused), so the order and the checks below matter.

## Inputs
- The final paper (PDF and source), the code and data repo, the author's ORCID iD and accounts.
- The owner's OK for each public step (a release, a record, a profile change is public content).

## Steps
1. **Pre-release audit.** Every number comes from code that ran (macros generated from result files, not typed).
   Every citation resolves: re-resolve all links and titles by script (DOI metadata, arXiv API, PDF first page) and
   have the human author hand-check them too; ACL-family venues require the author's own check. Build both the
   anonymous review PDF and the named preprint from one source with a flag.
2. **Clean the repo history before it goes public**: no local usernames in paths, nothing whose licence forbids
   redistribution or adaptation. A history rewrite needs the owner's OK; if the host still serves old commits,
   delete and recreate the repo. Record the rewrite in the README.
3. **Software DOI:** `CITATION.cff` (validate it) and `.zenodo.json` (upload type software, honest licence, AI-use
   note), enable the repo in Zenodo's GitHub integration, publish a GitHub release. Zenodo gives a concept DOI (all
   versions, share this one) and a version DOI.
4. **Readable preprint record:** a separate Zenodo record, type Preprint, PDF only, CC BY 4.0, linked both ways to
   the software record (related identifiers: is supplement to / is supplemented by). A PDF buried in a code archive
   is not readable.
   - In the creators dialog, type the ORCID iD, never the name: name autocomplete can attach a stranger's ORCID.
     Zoom on each chip before saving. Never click outside an open dialog.
   - Check the uploaded file's size and checksum after upload; one upload completed at 0 bytes during an outage.
5. **ORCID:** Works, Add, Add work with a DOI, using the concept DOI; set the type (Preprint, Software); feature the
   paper. Profile email visibility is the owner's choice: point it out. Optional, with the owner's OK (it grants a
   permission): DataCite Profiles' ORCID auto-update adds future DataCite DOIs by itself, but only when the ORCID iD
   is in the record's creators field, only for DOIs registered or updated after it is switched on, and it skips
   Zenodo version DOIs.
6. **Google Scholar** (the owner creates the profile; the agent cannot create accounts): affiliation as the owner
   wants it, homepage = ORCID URL, "don't automatically update". Add the paper manually under Other: Source =
   Zenodo, Report number = the DOI (Scholar has no DOI field). Limit: without an institutional email the profile is
   public by link but not shown in name search; add one later.
7. **LinkedIn:** a Publications entry (title, Zenodo, date, DOI link) and the announcement post pinned in Featured.
   The owner presses Post.
8. **arXiv**, only after an endorser is likely:
   - Since 2026 endorsers are told authors should be experts; a first-time author without peer-reviewed work is
     often refused. Get a peer-reviewed acceptance (a student research workshop) first, then ask.
   - In arXiv CS, review articles and position papers need proof of completed peer review (journal or conference;
     workshop review is usually not enough) since 31 Oct 2025. Research papers are not affected; check the type.
   - Check an endorser can endorse before asking: open one of their papers at
     `arxiv.org/auth/show-endorsers/<id>`.
   - Under 18: the submission page requires the arXiv parent/guardian consent form (one box ticked, real
     signatures, full address), emailed to arXiv help from the account's address; approval took about one day.
   - Source package: one flat folder, main tex with the preprint flag set inside it, include the `.bbl`, inputs
     rewritten to relative paths; compile it and diff its text against the released PDF page by page.
   - A started submission expires after about two weeks; accounts may submit two papers per month.
9. **Update every link** (README badges, CITATION, profile README) and the project's notes with all DOIs.

## Review before delivery
- Every DOI resolves; both Zenodo records show the right author with the right ORCID and link to each other.
- The preprint PDF opens in the browser; the review PDF has no name, link or affiliation.
- Profiles show the paper; nothing was published, posted or submitted without the owner's OK.

## Notes / sources
- arXiv CS review and position papers (31 Oct 2025): https://blog.arxiv.org/?p=1740
- DataCite ORCID auto-update: https://support.datacite.org/docs/how-can-i-automatically-link-my-works-with-a-datacite-doi-to-my-orcid-id
- Gmail and other connector gotchas: `workflow` plugin, `docs/gotchas.md`.
- Venue eligibility and AI-use questions: `research-outreach`. Author contribution: `author-ownership`.
