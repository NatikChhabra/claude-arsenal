#!/usr/bin/env python3
"""adb_drive.py -- drive one Android app over adb without tapping something else by mistake.

Every tap first checks that the target app owns the screen and that no notification has dropped
down over it. A heads-up notification grows the status bar window; a blind tap there once started
a WhatsApp call and once opened an SMS thread. Stdlib only.

  python adb_drive.py --serial <phone-ip>:<port> --pkg com.example.app ui
  python adb_drive.py ... tap 540 1200            (add --long for a long press)
  python adb_drive.py ... shot home               (screenshot -> ./shots/home.png)
  python adb_drive.py ... quiet on|off            (heads-up notifications off, then back to what they were)
  python adb_drive.py ... awake on|off            (10 min screen timeout, then back to what it was)
  python adb_drive.py --selftest

ADB_SERIAL and ADB_PKG may replace --serial and --pkg. Saved originals live in ./.adb_drive_state.json.
"""
import argparse, json, os, re, subprocess, sys, time, xml.etree.ElementTree as ET

STATE = '.adb_drive_state.json'
BAR_MAX = 130          # status bar height in px when nothing is dropped down (tall phones ~100-130)
SETTINGS = {'quiet': ('global', 'heads_up_notifications_enabled', '0'), 'awake': ('system', 'screen_off_timeout', '600000')}


def adb(serial, *args, check=True):
    r = subprocess.run(['adb', '-s', serial, *args], capture_output=True, text=True, encoding='utf-8', errors='replace')
    if check and r.returncode:
        sys.exit(f'adb {" ".join(args)} failed: {r.stderr.strip()}')
    return r.stdout


def focus_ok(window_dump, pkg):
    """The app's activity is the focused app and the focused window is the app or its own popup."""
    app = re.search(r'mFocusedApp=.*', window_dump)
    cur = re.search(r'mCurrentFocus=.*', window_dump)
    if not app or not cur or pkg not in app.group():
        return False
    # an app's menus take focus as a separate window; NotificationShade, StatusBar and other apps do not count
    return pkg in cur.group() or bool(re.search(r'PopupWindow|Pop-up window', cur.group()))


def status_bar_bottom(windows_dump):
    """Bottom edge of the StatusBar window frame, or None. Grows when a notification drops down."""
    m = re.search(r'StatusBar\}:.*?frame=\[\d+,\d+\]\[\d+,(\d+)\]', windows_dump, re.S)
    return int(m.group(1)) if m else None


def labels(ui_xml):
    """(label, x, y, state) for every node with text or a content description."""
    # uiautomator never writes a DTD; refusing one keeps entity tricks out of the stdlib parser
    if '<!DOCTYPE' in ui_xml or '<!ENTITY' in ui_xml:
        raise ValueError('unexpected DTD in uiautomator dump')
    out = []
    for n in ET.fromstring(ui_xml).iter('node'):
        text = n.get('text') or n.get('content-desc') or ''
        b = re.findall(r'\d+', n.get('bounds', ''))
        if not text or len(b) != 4:
            continue
        x0, y0, x1, y1 = map(int, b)
        state = '[ON]' if n.get('checked') == 'true' else '[off]' if n.get('checkable') == 'true' else ''
        out.append((text.replace('\n', ' '), (x0 + x1) // 2, (y0 + y1) // 2, state))
    return out


def guard(serial, pkg, tries=6, wait=3.0):
    for _ in range(tries):
        win = adb(serial, 'shell', 'dumpsys', 'window')
        bar = status_bar_bottom(adb(serial, 'shell', 'dumpsys', 'window', 'windows'))
        if focus_ok(win, pkg) and bar is not None and bar <= BAR_MAX:
            return True
        print(f'waiting: {pkg} in front={focus_ok(win, pkg)}, status bar bottom={bar}', file=sys.stderr)
        time.sleep(wait)
    return False


def save_and_set(serial, which, on):
    ns, key, value = SETTINGS[which]
    state = json.load(open(STATE)) if os.path.exists(STATE) else {}
    tag = f'{serial}|{ns}|{key}'
    if on:
        state.setdefault(tag, adb(serial, 'shell', 'settings', 'get', ns, key).strip())
        adb(serial, 'shell', 'settings', 'put', ns, key, value)
    elif tag in state:
        adb(serial, 'shell', 'settings', 'put', ns, key, state.pop(tag))
    json.dump(state, open(STATE, 'w'), indent=1)
    print(f'{key} = {adb(serial, "shell", "settings", "get", ns, key).strip()}')


def main(argv):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')   # labels carry symbols a Windows console mangles
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--serial', default=os.environ.get('ADB_SERIAL'))
    p.add_argument('--pkg', default=os.environ.get('ADB_PKG'))
    p.add_argument('--selftest', action='store_true')
    p.add_argument('cmd', nargs='*')
    p.add_argument('--long', action='store_true')
    a = p.parse_args(argv)
    if a.selftest:
        return selftest()
    if not a.serial or not a.cmd:
        p.error('need --serial (or ADB_SERIAL) and a command')
    cmd, rest = a.cmd[0], a.cmd[1:]
    if cmd == 'ui':
        # /data/local/tmp, not /sdcard: the dump holds whatever is on screen, so it is deleted at once
        dump = '/data/local/tmp/adb_drive_ui.xml'
        adb(a.serial, 'shell', 'uiautomator', 'dump', dump)
        xml = adb(a.serial, 'shell', 'cat', dump)
        adb(a.serial, 'shell', 'rm', '-f', dump, check=False)
        for t, x, y, s in labels(xml):
            print(f'{t[:48]:<48} @ {x},{y} {s}')
    elif cmd == 'tap':
        if not a.pkg:
            p.error('tap needs --pkg (or ADB_PKG)')
        x, y = rest[:2]
        if not guard(a.serial, a.pkg):
            sys.exit(f'NOT TAPPED: {a.pkg} not in front or a notification is down')
        adb(a.serial, 'shell', 'input', *(['swipe', x, y, x, y, '900'] if a.long else ['tap', x, y]))
        print(f'tapped {x},{y}{" (long)" if a.long else ""}')
    elif cmd == 'shot':
        os.makedirs('shots', exist_ok=True)
        path = os.path.join('shots', f'{rest[0] if rest else "shot"}.png')
        png = subprocess.run(['adb', '-s', a.serial, 'exec-out', 'screencap', '-p'], capture_output=True).stdout
        open(path, 'wb').write(png)
        print(path)
    elif cmd in SETTINGS:
        save_and_set(a.serial, cmd, (rest or ['on'])[0] == 'on')
    else:
        p.error(f'unknown command {cmd}')
    return 0


def selftest():
    win = ('  mCurrentFocus=Window{12cae77 u0 app.x/app.x.MainActivity}\n'
           '  mFocusedApp=ActivityRecord{64075969 u0 app.x/.MainActivity t3277}\n')
    assert focus_ok(win, 'app.x')
    assert focus_ok(win.replace('app.x/app.x.MainActivity', 'Pop-up window'), 'app.x')
    assert not focus_ok(win.replace('app.x/app.x.MainActivity', 'NotificationShade'), 'app.x')
    assert not focus_ok(win.replace('u0 app.x/.MainActivity', 'u0 com.whatsapp/.Main'), 'app.x')
    bar = ('Window #3 Window{a u0 StatusBar}:\n    mAttrs=...\n    Frames: parent=[0,0][1080,2340] '
           'display=[0,0][1080,2340] frame=[0,0][1080,101] last=[0,0][1080,101]\n')
    assert status_bar_bottom(bar) == 101   # the three-digit value must survive (a substr bug once read 101 as 01)
    assert status_bar_bottom(bar.replace('[1080,101] last', '[1080,412] last')) == 412
    assert status_bar_bottom('no status bar here') is None
    xml = ('<hierarchy><node text="Play" bounds="[0,0][100,50]" checkable="false"/>'
           '<node text="" content-desc="Shuffle" bounds="[100,0][200,50]" checkable="true" checked="true"/>'
           '<node text="" bounds="[0,0][1,1]"/></hierarchy>')
    assert labels(xml) == [('Play', 50, 25, ''), ('Shuffle', 150, 25, '[ON]')]
    try:
        labels('<!DOCTYPE x [<!ENTITY a "b">]><hierarchy/>')
        raise AssertionError('DTD accepted')
    except ValueError:
        pass
    print('adb_drive selftest ok')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
