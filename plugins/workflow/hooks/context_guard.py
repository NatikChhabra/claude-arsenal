"""context_guard.py: Claude Code PostToolUse hook (matcher "*"). Working-rules USAGE 1 made automatic. Stdlib only.

It reads the session's own transcript (a helper's own one when `agent_id` is set) and, once the context has grown GROW
tokens past the session's WORK START (a helper: AGENT_GROW past its first call), tells it once per further STEP band to
finish the chunk and hand off. It never blocks a tool and never asks for a skipped gate: quality never pays for usage.
Silent in every other case, and a crash is swallowed (a broken guard must never break a tool call). Test: test_hooks.py.

Why these numbers (six tuning rounds on real transcripts, Oct 2026):
- A written rule ("past ~150k, hand off") did not hold. In one overnight session, re-reading a context that had grown to
  250k on average (max 384k) was 33.6% of its usage; helpers that grew from ~50k to ~224k were most of the 52.5% agents cost.
- Counting cold-start reads (project rules, hand-off, brief: ~20-40k) as growth made sessions hand off after one small
  step, and every hand-off paid a new cold start. A turn costs ~0.1 x its context, a cold start a fixed R:
  cost per unit of work = R/L + 0.1(b + gL/2), lowest at +85-135k of growth when R ~265k (g = 1.5-2.5k per call).
  So the work start = the context at the first tool that is not a read (start-up reads capped at STARTUP).
- In a hosted project thread the fixed setup is ~117k, so R ~500k and the optimum moves to +120-190k: nudge +140k, every
  25k after, due at +200k even when nobody is around to start the next session.
- A call that re-writes more than half its context to the cache (the cache expired during a wait: a helper's lives 5 min,
  a main session's 1 h) gets one note. Measured: helpers waiting 6-12 min on long jobs re-wrote ~190k each time, 21.5% of
  one thread's usage.
- A 13-helper fan-out was the costliest session of a day (54% of the day went to helpers' own work), so a main session
  starting a helper while more than RUN_CAP already work (transcripts written in the last 3 min) is told to queue it, and
  a helper past IMG_CAP images (each re-read on every later call) is told to write its findings and return.
- A helper's fixed start is ~87k and one big read is 5-20k, so +60k fired right after the first reads (5 of 5 helpers);
  they returned half done and each re-spawn paid the start again. Helpers get +120k, and "finish the item in hand".
"""
import glob, json, os, re, sys, tempfile, time

GROW, HARD, AGENT_GROW, STEP, STARTUP, COLD_MIN = 140_000, 200_000, 120_000, 25_000, 40_000, 50_000
RUN_CAP, IMG_CAP, IMG_STEP = 4, 20, 10
IMAGE = (".png", ".jpg", ".jpeg", ".webp", ".gif")
READ_TOOLS = {"Read", "Grep", "Glob", "ToolSearch", "Skill", "LS", "TodoWrite", "TaskList", "TaskGet", "WebSearch", "WebFetch"}
READ_CMDS = re.compile(r"(?:cd\s+\S+\s*(?:&&|;)\s*)*(?:cat|head|tail|sed\s+-n|grep|rg|ls|find|wc|pwd|echo|Get-Content|Get-ChildItem|Select-String|"
                       r"git\s+(?:pull|log|status|show|diff|fetch|branch|rev-parse))\b")
MAIN = ("Context is {now}k, {grown}k past this session's work start (working-rules USAGE 1). Finish the chunk you are on "
        "(the whole step, not a sub-step), then hand off at its boundary: the hand-off REPLACES the previous STATUS block "
        "(older ones go to the archive). Until then push heavy reads (images, long logs, big diffs, file sweeps) into "
        "helpers that return a short answer. If nobody can start the next session for hours (the user is away), keep "
        "working in this one until +{hard}k. Never skip a check or a test to get there.")
HARD_MSG = ("Context is {now}k, {grown}k past this session's work start (working-rules USAGE 1): the hand-off is due at "
            "the next step boundary, attended or not. Write it (it REPLACES the previous STATUS block), then start fresh "
            "from it. Never skip a check or a test to get there.")
COLD_AGENT = ("Your last call re-wrote your whole {now}k context to the cache (~{eq}k of usage): a helper's cache lives 5 min "
              "and a wait outlived it (a long run, Monitor, a sleep). Never wait on a long job again in this helper: return "
              "what you have now and name the job the orchestrator should run in the background (its cache lives 1 h).")
COLD_MAIN = ("Your last call re-wrote your whole {now}k context to the cache (~{eq}k of usage): a wait outlived the 1 h cache. "
             "Before the next wait that can pass 1 h (a long job, the user away), write the hand-off first and let a "
             "fresh session pick up the result (working-rules USAGE 3).")
FANOUT = ("{n} helpers are working at once (cap {cap}, working-rules USAGE 4): let this one run, start no more until one "
          "returns, and fold what the first ones found into the next briefs. One helper per section or span, never one per item.")
IMAGES = ("{n} images are in this helper's context, and each is re-read on every later call (cap {cap}, working-rules "
          "USAGE 4). Write the findings for what you have looked at now and return; a fresh helper takes the rest.")
AGENT = ("Context is {now}k, {grown}k more than this helper started with (working-rules USAGE 1). Finish the item of your "
         "brief you are on, start no new heavy reads, put the full result in a file and return a short answer naming "
         "anything left.")


def size(line):
    try:
        u = json.loads(line)["message"]["usage"]
    except (ValueError, KeyError, TypeError):
        return None
    return u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0) + u.get("cache_read_input_tokens", 0)


def written(line):
    try:
        return json.loads(line)["message"]["usage"].get("cache_creation_input_tokens", 0)
    except (ValueError, KeyError, TypeError, AttributeError):
        return 0


def first_last(path):
    """Context of the first and the latest model call, and what the latest wrote to the cache. Reads the head and the last
    4 MB only: transcripts reach tens of MB."""
    first = last = None; wrote = 0
    with open(path, "rb") as f:
        for raw in f:
            if b'"usage"' in raw and (first := size(raw)):
                break
        f.seek(max(0, os.path.getsize(path) - 4_000_000))
        for raw in f:
            if b'"usage"' in raw and (n := size(raw)):
                last, wrote = n, written(raw)
    return first, last, wrote


def is_read(d):
    t = d.get("tool_name") or ""
    if t in READ_TOOLS or re.match(r"mcp__.+__(read|list|get|search|query|find)", t):
        return True
    return t in ("Bash", "PowerShell") and bool(READ_CMDS.match(((d.get("tool_input") or {}).get("command") or "").strip()))


def say(msg):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))


def fanout(d, agent, path, mark):
    """The fan-out note (a main session starting a helper) or the image note (a helper reading a picture), else None."""
    tool = d.get("tool_name") or ""
    if not agent and tool in ("Agent", "Task"):
        sub = os.path.join(path[:-len(".jsonl")], "subagents")
        now = time.time()
        n = sum(1 for f in glob.glob(os.path.join(sub, "*.jsonl")) if now - os.path.getmtime(f) < 180)
        return FANOUT.format(n=n, cap=RUN_CAP) if n > RUN_CAP else None
    fp = str((d.get("tool_input") or {}).get("file_path") or "")
    if agent and tool == "Read" and fp.lower().endswith(IMAGE):
        raw = open(path, "rb").read()
        n = raw.count(b'"type":"image"') + raw.count(b'"type": "image"')
        if n < IMG_CAP:
            return None
        try:
            told = json.load(open(mark + "_img"))
        except (OSError, ValueError):
            told = -1
        if (n - IMG_CAP) // IMG_STEP <= told:
            return None
        json.dump((n - IMG_CAP) // IMG_STEP, open(mark + "_img", "w"))
        return IMAGES.format(n=n, cap=IMG_CAP)
    return None


def main():
    d = json.load(sys.stdin)
    path = d.get("transcript_path") or ""
    agent = d.get("agent_id")
    if agent:
        path = os.path.join(path[:-len(".jsonl")], "subagents", f"agent-{agent}.jsonl")
    if not path.endswith(".jsonl") or not os.path.exists(path):
        return
    mark = os.path.join(tempfile.gettempdir(), f"context_guard_{d.get('session_id')}_{agent or 'main'}")
    if msg := fanout(d, agent, path, mark):
        return say(msg)
    first, last, wrote = first_last(path)
    if not first or not last:
        return
    try:
        st = json.load(open(mark))
    except (OSError, ValueError):
        st = {"base": first if agent else None, "band": -1}
    if last != first and wrote > 0.5 * last and last >= (COLD_MIN if agent else 3 * COLD_MIN) and st.get("cold") != last:
        st["cold"] = last                       # once per such call; a main session only from 150k (a fresh start costs ~that)
        json.dump(st, open(mark, "w"))
        return say((COLD_AGENT if agent else COLD_MAIN).format(now=last // 1000, eq=2 * wrote // 1000))
    if st["base"] is None:                      # still in the start-up reads: the work start is the first non-read tool
        if is_read(d) and last < first + STARTUP:
            return
        st["base"] = min(last, first + STARTUP)
        json.dump(st, open(mark, "w"))
    grown, grow = last - st["base"], (AGENT_GROW if agent else GROW)
    if grown < grow:
        return
    band = (grown - grow) // STEP
    if band <= st["band"]:
        return
    st["band"] = band
    json.dump(st, open(mark, "w"))
    msg = AGENT if agent else (HARD_MSG if grown >= HARD else MAIN)
    say(msg.format(now=last // 1000, grown=grown // 1000, hard=HARD // 1000))


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    try:
        main()
    except Exception:
        pass        # a broken guard must never break a tool call
