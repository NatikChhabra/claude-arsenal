---
name: drop-topic
description: Remove a topic or game the creator dropped, completely and in one pass - raws, renders, Shorts, thumbnails, transcripts, backups, job logs, worktree copies, demo clips cut from its footage, and every plan that still schedules it - leaving one veto line and a 3-line stub. Use for "drop <topic>", "delete everything related to <topic>", "I don't like this game", or when he vetoes a topic that has files.
---

# drop-topic <slug>

status: beta

His "delete" for that topic = the OK, raws included. One ask is enough: a first pass that cleaned the repo and left
~126 GB of renders on disk made the creator ask twice.

## Steps
1. **Find all of it:** every file and folder whose name holds the slug under the project's media folders, plus every
   edit list or job file whose SOURCE is the topic's raw (grep the JSON). Untracked renders often carry no topic name:
   check stale worktrees' logs and demo-clip sources. Skip worktrees other sessions are using.
2. **Delete:** everything inside the project (raws, transcripts, rough cuts, Shorts, thumbnails, published notes,
   backups, job logs, stale worktrees holding only its renders, clips cut from it) goes to the recycle bin, file by file
   (no "too big for the bin" dialog, so nothing is lost for good). Never touch another topic's files or a worktree a
   running session uses. Outside the project folder (his pictures, the game's saves): list only, his call.
3. **Repo:** remove its tracked files; every plan stops scheduling it; history keeps one line "<Topic> dropped <date>,
   creator disliked it". Add it to the veto list the topic-pick reads (skill `topic-pick`) and a 3-line stub in the
   dropped folder. Anything still useful (tool test data, vocabulary) moves to a neutral home first.
4. **Index:** re-run the project's raw-file index if it has one.
5. **Check + ship:** the project's self-test passes; commit + push if it uses git; ONE message: what went, GB freed,
   what sits in the recycle bin for him to empty.
