"""song_shape.py - a track's own loudness shape, ready to draw on its cover, visualiser or lyric video.

A cover drawn from the song's measured shape belongs to that song only (video.md section 7): intro, builds, the drop
bar, the last chorus and the ring-out sit where they really are. This reads any audio file ffmpeg can decode and
writes the shape as JSON.

    python song_shape.py SONG.wav OUT.json [--fps 20] [--smooth 2.0] [--floor -38] [--range 30] [--gamma 1.4]
                                            [--gap-db -40] [--gap-min 0.5] [--hold 5.0]
    python song_shape.py --selftest

OUT.json:
  duration          seconds
  fps               frames per second of the arrays below
  db                RMS level per frame in dBFS (raw, unsmoothed)
  shape             0..1 per frame: level mapped from floor..floor+range, gamma-curved, smoothed over --smooth s,
                    peak-normalised. Draw this.
  shape_held        the same with every inner silence held flat and eased in and out over --hold s, so a drawn wave
                    calms to a straight line and restarts instead of jumping (a 1 s collapse inside one wave cycle
                    drew as a broken zig-zag on the first cover that used it)
  gaps              inner silences: [{"start": s, "end": s}] where the level stays under --gap-db for --gap-min s.
                    Lead-in and tail silence are not gaps.

Mapping a shape onto a line: x = left + (t / duration) * width, amplitude = shape_held[t] * max_amplitude, times
sin(pi * u) ** 0.3 so both ends of a string stay pinned.
Needs numpy and ffmpeg on PATH.
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile

import numpy as np

SR = 8000  # loudness shape only: 8 kHz mono is plenty and keeps a 4-minute song under 2 M samples


def decode(path):
    cmd = ["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
    try:
        raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    except FileNotFoundError:
        sys.exit("song_shape: ffmpeg not found on PATH")
    except subprocess.CalledProcessError as e:
        sys.exit(f"song_shape: ffmpeg could not decode {path}: {e.stderr.decode(errors='ignore')[-200:]}")
    x = np.frombuffer(raw, np.float32)
    if x.size < SR:
        sys.exit(f"song_shape: {path} is under 1 s of audio")
    return x


def smooth(v, sec, fps):
    s = sec * fps
    if s <= 0:
        return v
    k = np.arange(-int(4 * s), int(4 * s) + 1)
    w = np.exp(-0.5 * (k / s) ** 2)
    w /= w.sum()
    pad = len(k) // 2
    return np.convolve(np.pad(v, pad, mode="edge"), w, mode="valid")


def ease(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def shape(x, fps=20, smooth_s=2.0, floor=-38.0, rng=30.0, gamma=1.4, gap_db=-40.0, gap_min=0.5, hold=5.0):
    hop = SR // fps
    n = len(x) // hop
    rms = np.sqrt((x[: n * hop].reshape(n, hop).astype(np.float64) ** 2).mean(1))
    db = 20 * np.log10(rms + 1e-9)
    t = np.arange(n) / fps
    s = smooth(np.clip((db - floor) / rng, 0, 1) ** gamma, smooth_s, fps)
    s = s / s.max() if s.max() > 0 else s
    # inner gaps: quiet runs that are not the lead-in or the tail
    loud = np.where(db >= gap_db)[0]
    gaps = []
    if loud.size:
        first, last = loud[0], loud[-1]
        quiet = db < gap_db
        i = first
        while i <= last:
            if quiet[i]:
                j = i
                while j <= last and quiet[j]:
                    j += 1
                if (j - i) / fps >= gap_min:
                    gaps.append({"start": round(i / fps, 3), "end": round(j / fps, 3)})
                i = j
            else:
                i += 1
    held = s.copy()
    for g in gaps:
        a, b = g["start"], g["end"]
        win = np.where(t < a, ease((a - t) / hold), np.where(t > b, ease((t - b) / hold), 0.0))
        held *= win
    return {"duration": round(len(x) / SR, 3), "fps": fps, "db": np.round(db, 2).tolist(),
            "shape": np.round(s, 4).tolist(), "shape_held": np.round(held, 4).tolist(), "gaps": gaps}


def selftest():
    sr = SR
    t = np.arange(int(sr * 30)) / sr
    env = np.where(t < 10, 0.1, 0.5)            # soft intro, loud body
    env[(t > 18) & (t < 20)] = 0.0              # a 2 s silent drop bar
    env[t > 28] = 0.0                           # tail silence (not a gap)
    x = (env * np.sin(2 * np.pi * 220 * t)).astype(np.float32)
    with tempfile.TemporaryDirectory() as d:
        wav = os.path.join(d, "t.wav")
        subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(sr), "-ac", "1", "-i", "-", wav],
                       input=x.tobytes(), check=True)
        out = shape(decode(wav))
    assert abs(out["duration"] - 30) < 0.05, out["duration"]
    assert len(out["gaps"]) == 1, out["gaps"]
    g = out["gaps"][0]
    assert abs(g["start"] - 18) < 0.15 and abs(g["end"] - 20) < 0.15, g
    s, h, fps = np.array(out["shape"]), np.array(out["shape_held"]), out["fps"]
    assert s[5 * fps] < s[15 * fps], "intro should draw smaller than the body"
    assert h[19 * fps] == 0.0, "the drop bar must be held flat"
    assert np.max(np.abs(np.diff(h))) < 0.05, "held shape must ease, not jump"
    print("song_shape selftest: PASS")


def main():
    if "--selftest" in sys.argv:
        return selftest()
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("audio")
    p.add_argument("out")
    p.add_argument("--fps", type=int, default=20)
    p.add_argument("--smooth", type=float, default=2.0, help="seconds of Gaussian smoothing")
    p.add_argument("--floor", type=float, default=-38.0, help="dBFS drawn as zero")
    p.add_argument("--range", type=float, default=30.0, help="dB from floor to full height")
    p.add_argument("--gamma", type=float, default=1.4)
    p.add_argument("--gap-db", type=float, default=-40.0)
    p.add_argument("--gap-min", type=float, default=0.5)
    p.add_argument("--hold", type=float, default=5.0, help="seconds to ease into and out of a gap")
    a = p.parse_args()
    out = shape(decode(a.audio), a.fps, a.smooth, a.floor, a.range, a.gamma, a.gap_db, a.gap_min, a.hold)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(out, f)
    print(f"song_shape: {out['duration']} s, {len(out['shape'])} frames at {a.fps} fps, gaps "
          + (", ".join(f"{g['start']}-{g['end']} s" for g in out["gaps"]) or "none"))


if __name__ == "__main__":
    main()
