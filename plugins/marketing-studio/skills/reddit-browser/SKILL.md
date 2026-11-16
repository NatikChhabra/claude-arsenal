---
name: reddit-browser
description: >-
  Manage the owner's Reddit through his signed-in browser: read the inbox and replies, find threads worth answering,
  draft posts and comments, and post only after his yes for that exact text. No API app is needed. Use for "check my
  Reddit", "reply on Reddit", "post this to r/...", "what did people say", or any Reddit job, because Reddit no longer
  gives new API apps and its public API closes in March 2027.
---

# reddit-browser

status: draft (written 16 Nov 2026 from a tool search; promote to beta after the first real session)

## Why a browser
Reddit shut self-service app creation in Nov 2025, stopped new API access requests on 31 Oct 2026 and closes the public
API in March 2027. Reddit MCP servers (for example jordanburke/reddit-mcp-server, MIT) need such an app for writes, so
without an old app the browser is the only route that keeps working. Registry row: `registry/tools.md`.

## Inputs
The task (read, reply, post), the subreddit or thread link, and the project's facts for the text (see social-copy).

## Steps
1. Use the built-in browser pane (or Claude in Chrome) on the owner's signed-in Reddit. Never type his password or
   open a login on his behalf; if signed out, ask him to sign in there.
2. Read first: inbox, replies, the thread and the subreddit's rules and recent posts (get_page_text, not screenshots).
3. Draft with social-copy, in the owner's voice, checked by copy_lint. Match the subreddit's rules, self-promotion
   limits and flair. Disclose that the owner made the project when it is his.
4. Show the exact text and the exact place (subreddit or thread link). Wait for his yes on that text.
5. Post it, then read the page back to confirm it is live and say the link.
6. Log what was posted and when in the project's STATE.md. One yes covers one post or one reply.

## Never
- Voting, karma farming, cross-posting the same text to many subreddits, new accounts, or anything that looks like a bot.
- Sending DMs unless he asked for that exact message.
- Deleting or editing posts without his yes.
- Posting anything he has not read.

## Review before delivery
Text matches what he approved word for word; the link works; subreddit rules were read in this session.

## Notes / sources
Dates and the MCP's tool list: github.com/jordanburke/reddit-mcp-server README (read 16 Nov 2026). Reddit's own
announcement of 30 Sep 2026 is linked there.
