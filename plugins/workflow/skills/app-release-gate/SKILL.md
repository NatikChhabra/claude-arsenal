---
name: app-release-gate
description: "Gate a desktop or mobile app release so a build that passes every test cannot still crash, freeze or loop on a user's machine. Rehearses the real flow end to end, starts the installed app the way a user does, checks hardware code against a pretend device, keeps a local diary for bug reports and stages the rollout. Use for 'release', 'ship it', 'cut a version', 'publish the build', 'is it ready to release', 'it crashes on my PC', 'it freezes', 'not responding', 'works here but not there', and before giving anyone a Publish link for an app or installer."
---
# App release gate

status: beta

Written after a first public release passed every unit test and every screenshot check, then closed at the end of
its own setup and froze its window on the first real computers. The tests had drawn the screens. None had run the flow.

## Inputs
- The app's repo, its CI, and the last release's bug reports.
- What the app touches outside itself: sound cards, cameras, files, the network, the updater.

## Steps
1. **List the real flows**, not the screens: first start, setup from first click to last, every "finish" button, close
   and reopen, update from the previous version. Each one gets a rehearsal the build runs by itself.
2. **Rehearse the end of each flow.** A screenshot test that fills a screen with example data proves the paint code, not
   the flow. Drive the real objects: start the step, finish it, tear it down, paint once more. Prove the rehearsal has
   teeth: put the old bug back, watch it fail, take the bug out again.
3. **Start the installed app in CI the way a user does.** Install, launch with no flags, wait about 25 seconds, check
   the process is alive and its window answers, ask it to close, require exit code 0. Then read its own log and fail
   on a freeze or crash line.
4. **Put hardware behind a pretend device.** Anything that waits on a driver (audio, camera, serial, Bluetooth) gets a
   fake with switches: goes silent, refuses to open, vanishes and returns, floods change messages, answers slowly.
   Assert budgets, not just outcomes: zero opens in an hour of healthy running, at most N opens when it never starts.
5. **Bound every retry.** No retry loop on the UI thread without all three: a growing wait between goes, a cap on
   goes, and a notice with a button when the cap is hit. Never do work inside a change callback; set a flag and act on
   the next tick. One deliberate change opens the device once.
6. **Keep a local diary.** One text file beside the settings: what was opened, how long it took, what failed. A watch
   thread writes "the window stopped answering while: X" after about a second without a heartbeat. A crash handler
   writes one line with no allocation; the next start reads it in. "Save a report" includes the last lines. Strip
   usernames from paths. Nothing is sent by itself.
7. **Reports for people who are not technical:** one button that saves or copies everything, plain words for what is
   in it, and a route that needs no account.
8. **Run a memory checker** (ASan and UBSan, or the platform's own) through every screen and each rehearsal.
9. **Stage it.** Testers get the build a day before everyone. The owner runs it on their own machine before anything
   public or any marketing push points at it.
10. **One click to publish.** Version bump and changelog only in the release commit, wait for green CI on that exact
    commit, then hand over the link. Push nothing to the release branch between green and publish.

## Review before delivery
- Every flow from step 1 has a rehearsal that ran in CI on the release commit, and one was shown to fail on a real bug.
- The start-and-close check ran on the installed build, not the build tree.
- Retry budgets are asserted in a test, with numbers.
- The release note leads with what was fixed, in the user's words, and says what could not be verified (for example
  "not run on a real sound card from here").

## Notes / sources
- Code that only compiles on one OS and cannot be built locally: read it once more for platform macros before pushing
  (`interface`, `module`, `small`, `min`, `max`) and let CI be the compile check; never claim it works before CI is green.
- `wsprintf` writes up to 1024 bytes whatever the buffer size: size the buffer for that.
