#!/usr/bin/env python3
"""loop_assemble.py: build a full song from short parts a player recorded once each, by placing them on a bar grid.

    python loop_assemble.py plan.json out.wav
    python loop_assemble.py --selftest

For a player who wants to record each part one time (verse, chorus, ...) and have repeats reused, the way a looper
or a producer's copy-paste works. Every sound in the output is his own recording; nothing is generated.

plan.json:
  {"bpm": 90, "beats_per_bar": 4,
   "clips": {"chorus": {"file": "parts.wav", "bars": 4, "onsets": [0, 1, 1.5, ...], "at_s": 42.67}, ...},
   "song": [{"at": 20, "clip": "chorus", "from": 0, "bars": 4, "gain_db": 0, "layer": "gtr"}, ...],
   "tail_s": 3.0}
  onsets   beats (from the part's first downbeat) where notes start, from the tab. Used to find the part in the take.
  at_s     where the part's first downbeat sits in the click track he played along to. Parts that share one file and
           all have at_s are found together (one offset for the whole take), then each is refined on its own.
           Without at_s the whole file is searched.
  song     each entry puts bars [from, from+bars) of a part at song bar `at`. Entries on the same layer cut the
           previous one's ring at the next downbeat; different layers (a melody over a chorus) are summed.
           A bar with no entry is silence. ring_s on an entry overrides tail_s (0.15 before a silent drop).

How it places audio: each recorded bar is found to the millisecond (his own timing inside the bar stays), cut 25 ms
before its downbeat and crossfaded onto the grid, so loops line up with the click and with each other. A run that
ends on the part's last bar keeps the recorded ring (tail_s), faded out; otherwise the ring stops at the next bar.

Prints a report and fails (exit 1) when a part can't be found reliably, drifts more than 0.5% from the click, is
clipped, or is too quiet. Fix those by re-recording that part, not by editing.
Needs numpy and soundfile (scipy for resampling if files differ in sample rate).
"""
import json, os, sys

PRE = 0.025      # cut this long before each downbeat, so the attack is never split
XF = 0.012       # crossfade at a bar seam
HOP = 128


def load(path):
    import numpy as np, soundfile as sf
    y, sr = sf.read(path, always_2d=True)
    ch = int(np.argmax((y ** 2).mean(0)))                     # phone and USB mics often fill one channel only
    return y[:, ch].astype(np.float64), sr


def resample(x, sr, to):
    if sr == to:
        return x
    from math import gcd
    from scipy.signal import resample_poly
    g = gcd(sr, to)
    return resample_poly(x, to // g, sr // g)


def envelope(x, sr):
    """Onset strength (positive spectral flux, log magnitude), one value per HOP samples."""
    import numpy as np
    n = 1024
    x = np.pad(x, (n // 2, max(0, n - len(x))))               # frame i is centred on sample i * HOP
    frames = np.lib.stride_tricks.sliding_window_view(x, n)[::HOP] * np.hanning(n)
    mag = np.log1p(30 * np.abs(np.fft.rfft(frames, axis=1)))
    flux = np.maximum(0, np.diff(mag, axis=0)).sum(1)
    flux = np.concatenate([[0], flux])
    flux -= np.convolve(flux, np.ones(31) / 31, 'same')       # remove slow level changes
    flux = np.maximum(flux, 0)
    return flux / (flux.max() + 1e-12)


def split(onsets):
    """Onsets may be beats or [beat, weight] pairs (weight = how many strings sound there, say)."""
    b = [o[0] if isinstance(o, (list, tuple)) else o for o in onsets]
    w = [o[1] if isinstance(o, (list, tuple)) else 1.0 for o in onsets]
    return b, w


def pattern(onsets_s, rate, ratio=1.0, width=0.012, weights=None):
    import numpy as np
    span = max(onsets_s) * ratio + 0.2
    t = np.arange(int(span * rate)) / rate
    p = np.zeros_like(t)
    for o, w in zip(onsets_s, weights or [1.0] * len(onsets_s)):
        p += w * np.exp(-0.5 * ((t - o * ratio) / width) ** 2)
    return p


def best_offset(env, pat, lo, hi):
    """Best frame offset for pat inside env[lo:hi]; returns (offset_frames, score, zscore)."""
    import numpy as np
    lo, hi = max(0, lo), min(len(env) - len(pat), hi)
    if hi <= lo:
        return None, 0.0, 0.0
    seg = env[lo:hi + len(pat)]
    c = np.correlate(seg, pat, 'valid')
    k = int(np.argmax(c))
    if 0 < k < len(c) - 1:                                     # parabolic peak for sub-frame accuracy
        a, b, d = c[k - 1], c[k], c[k + 1]
        frac = 0.5 * (a - d) / (a - 2 * b + d) if (a - 2 * b + d) != 0 else 0.0
    else:
        frac = 0.0
    med = np.median(c)
    mad = np.median(np.abs(c - med)) + 1e-12
    return lo + k + frac, float(c[k]), float((c[k] - med) / mad)


def locate(env, rate, onsets_s, lo_s, hi_s, weights=None):
    """Find downbeat time and tempo ratio of a part. Returns (downbeat_s, ratio, zscore)."""
    import numpy as np
    best = (None, 1.0, -1e9, 0.0)
    for r in np.arange(0.985, 1.0151, 0.001):
        off, sc, z = best_offset(env, pattern(onsets_s, rate, r, weights=weights), int(lo_s * rate), int(hi_s * rate))
        if off is not None and sc > best[2]:
            best = (off, r, sc, z)
    off, r, _, z = best
    return (off / rate if off is not None else None), float(r), z


def bar_starts(env, rate, d, r, bar_s, bars, onsets_beats, beat_s, bpb=4, win=0.05):
    """Refine every bar's downbeat inside +-win around the tempo line."""
    out = []
    for k in range(bars + 1):
        guess = d + k * bar_s * r
        ob = [o * beat_s for o in onsets_beats if k * bpb <= o < (k + 1) * bpb - 1e-9]
        if k < bars and ob:
            rel = [o - k * bar_s for o in ob]
            if min(rel) < 0.01:                                # only refine when the bar starts with a note
                off, _, _ = best_offset(env, pattern(rel, rate, r), int((guess - win) * rate), int((guess + win) * rate))
                if off is not None:
                    out.append(off / rate)
                    continue
        out.append(guess)
    return out


def assemble(plan, base_dir='.', stems=False):
    """Returns (audio, sr, report, problems); with stems=True audio is {layer: array}, same length and scale."""
    import numpy as np
    bpm, bpb = plan['bpm'], plan.get('beats_per_bar', 4)
    beat_s = 60.0 / bpm
    bar_s = beat_s * bpb
    tail_s = plan.get('tail_s', 3.0)
    files, report, problems = {}, [], []
    sr = None
    for name, c in plan['clips'].items():
        p = c['file'] if os.path.isabs(c['file']) else os.path.join(base_dir, c['file'])
        if p not in files:
            x, s = load(p)
            sr = sr or s
            clipped = int((np.abs(x) > 0.99).sum())
            x = resample(x, s, sr)
            files[p] = {'x': x, 'clipped': clipped, 'env': envelope(x, sr)}
        c['_path'] = p
    rate = sr / HOP
    # one offset per shared file, from every part with at_s
    group = {}
    for name, c in plan['clips'].items():
        if 'at_s' in c:
            group.setdefault(c['_path'], []).append(c)
    shift = {}
    for p, cs in group.items():
        if len(cs) < 2:
            continue
        on = sorted(c['at_s'] + o * beat_s for c in cs for o in split(c.get('onsets', range(c['bars'] * bpb)))[0])
        t0 = on[0]
        off, _, _ = best_offset(files[p]['env'], pattern([o - t0 for o in on], rate), 0, len(files[p]['env']))
        shift[p] = off / rate - t0 if off is not None else 0.0
    found = {}
    for name, c in plan['clips'].items():
        f = files[c['_path']]
        beats, wts = split(c.get('onsets', range(c['bars'] * bpb)))
        ons = [o * beat_s for o in beats]
        if 'at_s' in c and c['_path'] in shift:                # less than an eighth note either way: no 8th slips
            centre = c['at_s'] + shift[c['_path']]
            lo, hi = centre - min(0.12, beat_s / 4), centre + min(0.12, beat_s / 4)
        else:
            lo, hi = 0, len(f['x']) / sr
        d, r, z = locate(f['env'], rate, ons, lo, hi, wts)
        if d is None:
            problems.append(f'{name}: not found')
            continue
        starts = bar_starts(f['env'], rate, d, r, bar_s, c['bars'], beats, beat_s, bpb)
        dev = [1000 * (starts[k] - (d + k * bar_s * r)) for k in range(c['bars'] + 1)]
        seg = f['x'][int(d * sr):int((d + c['bars'] * bar_s) * sr)]
        peak = 20 * np.log10(np.abs(seg).max() + 1e-12) if len(seg) else -120
        found[name] = (f['x'], starts)
        line = (f'{name:12s} downbeat {d:7.3f} s  tempo {100 * (1 / r - 1):+5.2f}%  match {z:5.1f}  '
                f'bar wobble {max(abs(v) for v in dev):3.0f} ms  peak {peak:6.1f} dBFS')
        report.append(line)
        if z < 6:
            problems.append(f'{name}: weak match ({z:.1f}); check it is the right part, or re-record over the click')
        if abs(r - 1) > 0.005:
            problems.append(f'{name}: {100 * (1 / r - 1):+.2f}% off the click; re-record with the click in one ear')
        if peak < -30:
            problems.append(f'{name}: quiet ({peak:.0f} dBFS); move the mic closer or play harder')
    for p, f in files.items():
        if f['clipped']:
            problems.append(f'{os.path.basename(p)}: {f["clipped"]} clipped samples; lower the input gain')
    if any(e['clip'] not in found for e in plan['song']):
        return None, sr, report, problems
    end_bar = max(e['at'] + e['bars'] for e in plan['song'])
    n = int((end_bar * bar_s + tail_s + 1) * sr)
    by_layer = {}
    for e in sorted(plan['song'], key=lambda e: e['at']):
        by_layer.setdefault(e.get('layer', 'main'), []).append(e)
    layers = {}
    for layer, es in by_layer.items():
        out = layers[layer] = np.zeros(n)
        for i, e in enumerate(es):
            x, starts = found[e['clip']]
            cbars = plan['clips'][e['clip']]['bars']
            g = 10 ** (e.get('gain_db', 0) / 20)
            nxt = es[i + 1]['at'] if i + 1 < len(es) else None
            for k in range(e['bars']):
                cb = e['from'] + k
                src0 = starts[cb] - PRE
                last = (k == e['bars'] - 1)
                if not last:
                    src1 = starts[cb + 1] - PRE + XF
                elif cb + 1 == cbars:                          # part's last bar: keep the recorded ring
                    src1 = starts[cb + 1] + e.get('ring_s', tail_s)
                else:                                          # ring stops before the part's next attack
                    src1 = starts[cb + 1] - 0.003
                dst0 = (e['at'] + k) * bar_s - PRE
                seg = x[max(0, int(src0 * sr)):int(src1 * sr)].copy()
                if dst0 < 0:
                    seg, dst0 = seg[int(-dst0 * sr):], 0.0
                a = int(XF * sr)
                if len(seg) > 2 * a:
                    seg[:a] *= np.linspace(0, 1, a)
                    if not last:
                        seg[-a:] *= np.linspace(1, 0, a)
                if last:
                    cut, by_next = len(seg), False
                    if nxt is not None:
                        c2 = int(((nxt * bar_s + 0.03) - dst0) * sr)
                        if c2 < cut:
                            cut, by_next = c2, True
                    if cb + 1 != cbars:
                        by_next = True                         # stopped before the part's next attack: short fade
                    seg = seg[:max(cut, 0)]
                    fo = min(len(seg), int((0.055 if by_next else min(0.8, e.get('ring_s', tail_s) / 2 + 0.03)) * sr))
                    if fo > 0:
                        seg[-fo:] *= np.linspace(1, 0, fo) ** (1 if by_next else 2)
                i0 = int(round(dst0 * sr))
                m = min(len(seg), n - i0)
                out[i0:i0 + m] += g * seg[:m]
    out = sum(layers.values())
    sc = min(1.0, 0.89 / (np.abs(out).max() + 1e-12))
    nz = np.nonzero(np.abs(out) > 1e-5)[0]
    end = nz[-1] + int(0.2 * sr) if len(nz) else n
    if stems:
        return {k: v[:end] * sc for k, v in layers.items()}, sr, report, problems
    return out[:end] * sc, sr, report, problems


def selftest():
    import numpy as np, soundfile as sf, tempfile
    rng = np.random.default_rng(3)
    sr, bpm = 44100, 90
    beat = 60 / bpm
    bar = 4 * beat

    def pluck(f, dur=1.4):
        t = np.arange(int(dur * sr)) / sr
        return sum(np.sin(2 * np.pi * f * h * t) / h for h in (1, 2, 3)) * np.exp(-t * 3) * 0.2

    onsets = [b + o for b in (0, 4, 8, 12) for o in (0, 1, 1.5, 2, 3, 3.5)]
    take_ratio, at, lead = 1.003, 6.0, 1.734            # player 0.3% slow, recording started 1.734 s early
    x = rng.normal(0, 0.002, int(30 * sr))
    for o in onsets:
        i = int((lead + at + o * beat * take_ratio + rng.normal(0, 0.004)) * sr)
        y = pluck(196 * (1 + (o % 4 == 0)))
        x[i:i + len(y)] += y
    tmp = tempfile.mkdtemp()
    sf.write(os.path.join(tmp, 'take.wav'), x, sr)
    sf.write(os.path.join(tmp, 'solo.wav'), x[int((lead + at - 1) * sr):], sr)
    plan = {'bpm': bpm, 'tail_s': 2.0,
            'clips': {'a': {'file': 'take.wav', 'bars': 4, 'onsets': onsets, 'at_s': at},
                      'a2': {'file': 'take.wav', 'bars': 2, 'onsets': onsets[:12], 'at_s': at},
                      'b': {'file': 'solo.wav', 'bars': 4, 'onsets': onsets}},
            'song': [{'at': 0, 'clip': 'a', 'from': 0, 'bars': 4}, {'at': 4, 'clip': 'a', 'from': 0, 'bars': 4},
                     {'at': 9, 'clip': 'b', 'from': 1, 'bars': 2},
                     {'at': 4, 'clip': 'a2', 'from': 0, 'bars': 2, 'layer': 'top', 'gain_db': -6}]}
    out, osr, rep, prob = assemble(plan, tmp)
    ok = True
    print('\n'.join(rep))
    for name, want in (('a', lead + at), ('b', 1.0)):
        line = [l for l in rep if l.startswith(name + ' ')][0]
        got = float(line.split('downbeat')[1].split('s')[0])
        if abs(got - want) > 0.012:
            print(f'FAIL {name}: downbeat {got:.3f}, expected {want:.3f}'); ok = False
    if prob:
        print('FAIL problems on a clean take:', prob); ok = False
    env = envelope(out, osr)
    rate = osr / HOP
    for b in (0, 4, 9, 10):                                   # every placed bar must hit the grid
        k = int(b * bar * rate)
        pk = k - 6 + int(np.argmax(env[max(0, k - 6):k + 6]))
        if abs(pk - k) / rate > 0.015:
            print(f'FAIL bar {b}: attack {1000 * (pk - k) / rate:.0f} ms off the grid'); ok = False
    gap = out[int((8 * bar + 0.3) * osr):int((9 * bar - 0.1) * osr)]   # bar 8 has no entry: ring fades, then silence
    if np.abs(gap[-int(0.3 * osr):]).max() > 1e-3:
        print('FAIL the empty bar is not silent'); ok = False
    for b in (1, 2, 3, 5):                                    # seams inside runs: no dropout before the downbeat
        w = out[int((b * bar - 0.02) * osr):int((b * bar - 0.005) * osr)]
        if np.sqrt((w ** 2).mean()) < 1e-3:
            print(f'FAIL dropout before bar {b}'); ok = False
    if not (10 * bar < len(out) / osr < 11 * bar + 3):
        print('FAIL length', len(out) / osr); ok = False
    bad = dict(plan); bad['clips'] = {'a': dict(plan['clips']['a'])}; bad['song'] = plan['song'][:1]
    sf.write(os.path.join(tmp, 'take.wav'), x * 0.005, sr)
    _, _, _, prob2 = assemble(bad, tmp)
    if not any('quiet' in p for p in prob2):
        print('FAIL a quiet take was not flagged'); ok = False
    print('selftest', 'PASS' if ok else 'FAIL')
    return ok


def main(argv):
    if argv[1:2] == ['--selftest']:
        return 0 if selftest() else 1
    if len(argv) != 3:
        print(__doc__)
        return 2
    import soundfile as sf
    plan = json.load(open(argv[1]))
    out, sr, rep, prob = assemble(plan, os.path.dirname(os.path.abspath(argv[1])))
    print('\n'.join(rep))
    for p in prob:
        print('PROBLEM', p)
    if out is not None:
        sf.write(argv[2], out, sr, subtype='PCM_24')
        print(f'wrote {argv[2]}  {len(out) / sr:.1f} s')
    return 1 if prob or out is None else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
