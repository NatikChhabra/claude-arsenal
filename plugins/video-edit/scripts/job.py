"""job.py: run a long command (transcribe, render, a caption check, a test suite) DETACHED from the agent session, with a
status file any later session can read. Why: a transcription started inside a session dies with that session and can
sit dead for hours unnoticed. Stdlib only, Python 3.8+, Windows + macOS + Linux.

    python job.py start <name> -- <command...>   -> <jobs>/<name>.log + <name>.json
    python job.py status [<name>]                -> running / done / FAILED (exit N) / DIED
    python job.py selftest                       -> starts two tiny jobs and checks their states

<jobs> = $JOB_DIR, else ./logs/jobs under the current directory (run status from the same directory, or set JOB_DIR).
The child runs in a new detached process group: closing the session or the terminal does not kill it. <name>.json holds
the command, pid, start, end and exit code; "DIED" = the json says running but the pid is gone (re-run it).
The command's TMP/TEMP/TMPDIR point at <jobs>/../tmp (or $JOB_TMP), so big renders fill the project's drive, not the
system drive.
"""
import json, os, shutil, subprocess, sys, tempfile, time

DIR = os.environ.get("JOB_DIR") or os.path.join(os.getcwd(), "logs", "jobs")
TMP = os.environ.get("JOB_TMP") or os.path.join(os.path.dirname(os.path.abspath(DIR)), "tmp")
PY = sys.executable
FMT = "%Y-%m-%d %H:%M:%S"


def alive(pid):
    if os.name == "nt":                                 # os.kill(pid, 0) on Windows terminates the process: ask tasklist
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH", "/FO", "CSV"], capture_output=True, text=True).stdout
        return f'"{pid}"' in out                        # the exact CSV field: pid 12 must not match 1234
    try: os.kill(pid, 0); return True
    except OSError: return False


def load(st):
    for _ in range(50):                                 # the other side may be mid-write: retry a torn read
        try:
            with open(st) as fh: return json.load(fh)
        except (ValueError, OSError): time.sleep(0.1)
    with open(st) as fh: return json.load(fh)


def save(st, d):
    with open(st, "w") as fh: json.dump(d, fh)


def start(name, cmd):
    os.makedirs(DIR, exist_ok=True)
    st, log = os.path.join(DIR, name + ".json"), os.path.join(DIR, name + ".log")
    # the wrapper (this file, "run") waits for the command and writes its own pid + exit code; it is what runs detached
    flags = (subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP) if os.name == "nt" else 0
    save(st, {"cmd": cmd, "pid": None, "start": time.strftime(FMT), "state": "running"})
    env = dict(os.environ, JOB_DIR=os.path.abspath(DIR), JOB_TMP=os.path.abspath(TMP))
    try:
        p = subprocess.Popen([PY, os.path.abspath(__file__), "run", name, "--"] + cmd, cwd=os.getcwd(), creationflags=flags,
                             stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             start_new_session=os.name != "nt", close_fds=True, env=env)
    except OSError as e:
        save(st, {"cmd": cmd, "start": time.strftime(FMT), "state": "failed", "exit": str(e)}); raise
    print(f"started {name} (pid {p.pid}), detached\n  log:    {log}\n  status: python {os.path.abspath(__file__)} status {name}")


def run(name, cmd):
    st, log = os.path.join(DIR, name + ".json"), os.path.join(DIR, name + ".log")
    d = load(st) if os.path.exists(st) else {"cmd": cmd, "start": time.strftime(FMT)}
    d.update(pid=os.getpid()); save(st, d)
    os.makedirs(TMP, exist_ok=True)
    with open(log, "w", encoding="utf-8") as fh:
        try:
            rc = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT,
                                env=dict(os.environ, PYTHONUTF8="1", TMP=TMP, TEMP=TMP, TMPDIR=TMP)).returncode
        except OSError as e:                            # command not found: a FAILED state, not a DIED one
            fh.write(f"job.py: {e}\n"); rc = 127
    d.update(state="done" if rc == 0 else "failed", exit=rc, end=time.strftime(FMT))
    save(st, d)


def state(d):
    s = d["state"]
    if s == "running" and not d.get("pid"):             # the wrapper writes its pid within a second of the start
        age = time.time() - time.mktime(time.strptime(d["start"], FMT))
        if age > 30: s = "DIED (never started: re-run it)"
    elif s == "running" and not alive(d["pid"]): s = "DIED (re-run it)"
    elif s == "failed": s = f"FAILED (exit {d.get('exit')})"
    return s


def status(name=None):
    if not os.path.isdir(DIR): return print("no jobs")
    for f in sorted(x for x in os.listdir(DIR) if x.endswith(".json") and (not name or x == name + ".json")):
        d = load(os.path.join(DIR, f))
        print(f"{f[:-5]}: {state(d)}  start {d['start']}" + (f"  end {d['end']}" if d.get("end") else "")
              + f"  | {' '.join(map(str, d['cmd']))[:120]}")


def selftest():
    global DIR, TMP
    DIR = tempfile.mkdtemp(prefix="jobtest_"); TMP = os.path.join(DIR, "tmp")
    start("ok", [PY, "-c", "print('hi')"]); start("bad", [PY, "-c", "import sys; sys.exit(3)"])
    for _ in range(100):
        got = {n: state(load(os.path.join(DIR, n + ".json"))) for n in ("ok", "bad")}
        if "running" not in got.values(): break
        time.sleep(0.2)
    assert got == {"ok": "done", "bad": "FAILED (exit 3)"}, got
    with open(os.path.join(DIR, "ok.log"), encoding="utf-8") as fh: assert fh.read().strip() == "hi"
    shutil.rmtree(DIR, ignore_errors=True)
    print("job.py selftest PASS")


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    a = sys.argv[1:]
    if a[:1] == ["status"]: status(a[1] if len(a) > 1 else None)
    elif a[:1] == ["selftest"]: selftest()
    elif a[:1] in (["start"], ["run"]) and len(a) > 3 and a[2] == "--": (start if a[0] == "start" else run)(a[1], a[3:])
    else: print(__doc__); sys.exit(1)
