"""Send one prompt to a local OpenAI-compatible LLM server (start one with scripts/llm.ps1). Stdlib only.

  python scripts/ask.py "Summarise this" < notes.txt
  python scripts/ask.py --think "Hard question"
Prompt = args + stdin (if piped). Prints the answer only.
Env: LLM_URL (default http://127.0.0.1:8091/v1/chat/completions), LLM_MODEL (sent only when set; llama.cpp ignores it).
Use it for bulk drafting that Claude would otherwise spend tokens on; Claude checks the output, never ships it unread.
"""
import json
import os
import sys
import urllib.request

URL = os.environ.get("LLM_URL", "http://127.0.0.1:8091/v1/chat/completions")


def ask(prompt, system=None, think=False, max_tokens=4096):
    msgs = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": prompt}]
    body = {"messages": msgs, "max_tokens": max_tokens, "chat_template_kwargs": {"enable_thinking": think}}
    if os.environ.get("LLM_MODEL"):
        body["model"] = os.environ["LLM_MODEL"]
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        return json.load(r)["choices"][0]["message"]["content"].strip()


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    args = sys.argv[1:]
    think = "--think" in args
    args = [a for a in args if a != "--think"]
    prompt = " ".join(args)
    if not sys.stdin.isatty():
        prompt = (prompt + "\n\n" + sys.stdin.read()).strip()
    if not prompt:
        sys.exit(__doc__)
    print(ask(prompt, think=think))
