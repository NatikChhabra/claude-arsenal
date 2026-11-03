---
name: android-adb-drive
description: "Drive an app on the owner's Android phone over adb (wireless debugging) without tapping the wrong thing: every tap checks the app owns the screen and no notification has dropped over it, settings changed for the session are saved and put back, and screens are read as labels with tap coordinates. Use for 'set up this app on my phone', 'change the settings in <app>', 'check my phone', 'test it on the phone', 'tap through', adb, uiautomator, wireless debugging, or any phone automation."
---
# Drive an Android app over adb

status: beta

Tool: `python ${CLAUDE_PLUGIN_ROOT}/scripts/adb_drive.py` (stdlib; `--selftest` runs without a phone).

## Why the guard exists
Two real mis-taps on 2026-11-03, both from a plain `adb shell input tap`:
- a WhatsApp message arrived as a heads-up banner exactly where the tap landed, and the tap started a call;
- an SMS banner did the same a few hours later and opened the thread.
A banner grows the status bar window, so the tool refuses to tap while the status bar is taller than normal or another
app (or the notification shade) has focus. It retries for about 18 s, then says NOT TAPPED instead of guessing.

## Inputs
- Serial: `adb devices` (wireless debugging gets a NEW port each time the phone re-enables it; re-read it after any
  "device offline"). Pairing needs the 6-digit code and pair port from Developer options > Wireless debugging.
- The app's package: `adb shell pm list packages | grep -i <name>`.

## Steps
1. `export ADB_SERIAL=<ip:port> ADB_PKG=<package>`. Check the phone is unlocked:
   `adb shell dumpsys window | grep -m1 isKeyguardShowing` must be false. A locked phone cannot be driven; ask the owner
   to unlock and keep the app open.
2. Check nobody is using the phone right now: take a `shot`, wait 5 s, take another. If the screen changed and you did
   not touch it, the owner is using it: STOP, tell them, and either wait or give them the steps to do themselves. Two
   people tapping the same phone is how the wrong thing gets pressed.
3. `adb_drive.py quiet on` (heads-up banners off) and, for long sessions, `awake on` (10 min screen timeout). Both save
   the original value; put them back with `quiet off` / `awake off` before ending the turn, even when the work failed.
4. Read the screen with `adb_drive.py ui` (label @ x,y and [ON]/[off] for switches). Prefer these coordinates over
   guessing from a screenshot. Screenshots (`shot <name>`) are full resolution; if you view a half-size copy, double
   its coordinates.
5. Tap with `adb_drive.py tap X Y` (`--long` for a long press). Its own menus count as the app (they take focus as a
   pop-up window). After every tap that changes something, read the screen again and confirm the new state
   (`ui` shows [ON]/[off]). Never chain taps blind.
6. To leave the app or a sheet, `adb shell input keyevent KEYCODE_BACK` once and re-read; counting BACK presses blind
   walks out of the app into whatever is underneath.

## Things that look like they work but do not
- **Airplane mode kills adb over Wi-Fi.** To prove an app plays offline, measure instead: watch the server's traffic
  (`docker stats --no-stream` NetIO on the music server) while a downloaded song plays; no change = played from the
  phone. Then ask the owner to try real airplane mode once.
- `monkey -p <pkg> -c android.intent.category.LAUNCHER 1` reopens an app after you fell out of it.
- `settings get` after every `settings put`; Samsung keeps some values per profile.
- Pull-to-refresh is a different gesture per screen; an app's Home pull may not do what its Library pull does. Read the
  app's docs or code before telling the owner which pull syncs.

## Review before delivery
- `quiet` and `awake` are back to their saved values (`settings get` shows them).
- Every change you claim is visible in a final `ui` read or screenshot.
- Anything you could not do (locked phone, owner using it, device offline) is said plainly, with the steps for the
  owner to do it themselves.

## Notes / sources
- Built and proved on a Samsung SM-A566E (Android 16) on 2026-11-03 while moving the owner from Symfonium to the Octo
  app: settings, playlists, pinning, downloads, an offline test by traffic measurement.
- The status bar check once read `101` as `01` (a substring bug); the selftest keeps the three-digit case.
