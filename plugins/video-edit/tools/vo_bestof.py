#!/usr/bin/env python3
"""Best-of VO: build one clean voice-over from the best take of each line.

The speaker records the script two or three times. For each line you pick the take that says it best (from the
transcript and a listen), give its rough start/end (from the transcript's word times), and this tool:
  - finds the real speech onset and tail on the level envelope (needs quiet before the onset, so a breath or the
    previous word is not cut in),
  - shortens long pauses inside a line (crossfaded, never inside a word),
  - matches speech loudness line to line,
  - places the lines with the gaps you choose and writes one mono WAV plus lines.json
    (each line's placed start/end, and each word's placed time when a word-timestamp file is given).
lines.json drives captions and cue sheets for the edit.

  python vo_bestof.py spec.json            # writes spec["out"] and spec["out_json"]
  python vo_bestof.py --selftest

spec.json:
{
  "sr": 48000,
  "takes": {"t1": "take1.wav", "t2": "take2.wav"},
  "words": {"t1": "take1_words.json"},          # optional: [{"word","start","end"}] or whisper segments
  "lines": [
    {"take": "t2", "start": 1.16, "end": 3.64, "text": "Your business is good, but your ad isn't."},
    {"take": "t1", "start": 22.66, "end": 24.98, "text": "First three businesses get 30% off.",
     "clamp_end": 25.06},                      # cut before an ad-lib that follows
    {"take": "t1", "start": 56.26, "end": 57.56, "text": "I'll always come to you.", "pre": 0.04}
  ],
  "start": 0.30,                                # first word in by 0.5 s
  "gaps": [0.30, 0.42, 0.40],                   # pause before line 2, 3, ... (last value repeats)
  "threshold_db": -46,                          # speech vs room; raise for a noisy room
  "out": "vo.wav", "out_json": "lines.json"
}
Lessons it encodes (launch-ad VO, Nov 2026): a whisper word time can be 0.3-0.8 s off, so the onset search window
is wide and demands 120 ms of quiet before speech; clamp a line's end when the take runs on into an ad-lib; re-run a
transcript on the CUT file to confirm every word survived (a clipped first consonant shows up as a changed word).
"""
import json, sys, os

H_S = 0.01  # envelope hop, seconds


def _np():
    import numpy as np
    return np


def env_db(x, sr):
    np = _np(); h = int(sr * H_S); n = len(x) // h
    if n == 0:
        return np.full(1, -120.0)
    return 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)


def bounds(x, sr, a, b, th):
    """Real onset near a and real tail near b (seconds)."""
    e = env_db(x, sr); n = len(e)
    i0, i1 = max(13, int((a - 0.30) / H_S)), min(n - 2, int((a + 0.80) / H_S))
    on = None
    for i in range(i0, i1):
        if e[i] > th and e[i + 1] > th and (e[i - 12:i] < th).all():
            on = i; break
    if on is None:  # fall back to the first loud frame in the window
        on = next((i for i in range(i0, i1) if e[i] > th), int(a / H_S))
    j0, j1 = max(0, int((b - 0.25) / H_S)), min(n, int((b + 0.35) / H_S))
    loud = [j for j in range(j0, j1) if e[j] > th]
    off = max(loud) if loud else int(b / H_S)
    return on * H_S - 0.06, off * H_S + 0.10


def squeeze(seg, sr, th, maxgap=0.34, keep=0.24):
    """Shorten internal pauses longer than maxgap to keep seconds. Returns (audio, removed[(t, dur)])."""
    np = _np(); e = env_db(seg, sr); quiet = e < th - 2
    cuts, i = [], 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]:
                j += 1
            if (j - i) * H_S > maxgap and i > 5 and j < len(quiet) - 5:
                mid, half = (i + j) / 2 * H_S, ((j - i) * H_S - keep) / 2
                cuts.append((mid - half, mid + half))
            i = j
        else:
            i += 1
    xf = int(0.012 * sr); pieces, last, removed = [], 0, []
    for a, b in cuts:
        A, B = int(a * sr), int(b * sr)
        pieces.append(seg[last:A + xf].copy()); last = B; removed.append((a, b - a))
    pieces.append(seg[last:].copy())
    y = pieces[0]; r = np.linspace(0, 1, xf)
    for p in pieces[1:]:
        if len(y) < xf or len(p) < xf:
            y = np.concatenate([y, p]); continue
        y = np.concatenate([y[:-xf], y[-xf:] * (1 - r) + p[:xf] * r, p[xf:]])
    return y, removed


def tmap(t, removed):
    s = 0
    for a, d in removed:
        if t > a + d:
            s += d
        elif t > a:
            s += t - a
    return t - s


def load_words(path, key=None):
    W = json.load(open(path))
    if isinstance(W, dict):  # {"file.wav": [segments]} or {"segments": [...]}
        W = W.get('segments') or W.get(key) or next(iter(W.values()))
    out = []
    for s in W:
        if 'words' in s:
            out += [dict(word=w['word'], start=w['start'], end=w['end']) for w in s['words']]
        elif 'word' in s:
            out.append(dict(word=s['word'], start=s['start'], end=s['end']))
    return out


def build(spec, base='.'):
    np = _np(); import soundfile as sf
    sr = spec.get('sr', 48000); th = spec.get('threshold_db', -46)
    src = {}
    for k, f in spec['takes'].items():
        x, r = sf.read(os.path.join(base, f))
        if r != sr:
            raise SystemExit(f'{f}: {r} Hz, spec says {sr}. Resample first.')
        src[k] = x.mean(1) if x.ndim > 1 else x
    words = {k: load_words(os.path.join(base, f), os.path.basename(spec['takes'][k]))
             for k, f in spec.get('words', {}).items()}
    gaps = spec.get('gaps', [0.4]); segs = []
    for L in spec['lines']:
        x = src[L['take']]; s, e = bounds(x, sr, L['start'], L['end'], th)
        s -= L.get('pre', 0.0)
        if 'clamp_end' in L:
            e = min(e, L['clamp_end'])
        seg = x[int(s * sr):int(e * sr)].copy()
        seg, removed = squeeze(seg, sr, th)
        fi, fo = int(0.008 * sr), int(0.035 * sr)
        seg[:fi] *= np.linspace(0, 1, fi); seg[-fo:] *= np.linspace(1, 0, fo)
        ed = env_db(seg, sr); act = ed > th + 10
        if act.any():
            seg *= 10 ** (-20 / 20) / np.sqrt(np.mean(10 ** (ed[act] / 10)))
        ws = [w for w in words.get(L['take'], []) if w['start'] >= s - 0.05 and w['end'] <= e + 0.3]
        segs.append(dict(L=L, s=s, seg=seg, removed=removed, words=ws))
    t = spec.get('start', 0.30)
    for i, d in enumerate(segs):
        if i:
            t += gaps[min(i - 1, len(gaps) - 1)]
        d['at'] = t; t += len(d['seg']) / sr
    out = np.zeros(int((t + 0.3) * sr)); lines = []
    for d in segs:
        i = int(d['at'] * sr); out[i:i + len(d['seg'])] += d['seg']
        lines.append(dict(text=d['L'].get('text', ''), take=d['L']['take'], src=round(d['s'], 2),
                          start=round(d['at'], 3), end=round(d['at'] + len(d['seg']) / sr, 3),
                          words=[dict(w=w['word'].strip(),
                                      s=round(d['at'] + tmap(w['start'] - d['s'], d['removed']), 3),
                                      e=round(d['at'] + tmap(w['end'] - d['s'], d['removed']), 3))
                                 for w in d['words']]))
    pk = np.abs(out).max() or 1.0
    out = np.tanh(out / pk * 1.2) / np.tanh(1.2) * 0.89
    sf.write(os.path.join(base, spec.get('out', 'vo.wav')), out, sr)
    json.dump(lines, open(os.path.join(base, spec.get('out_json', 'lines.json')), 'w'), indent=1)
    return lines, len(out) / sr


def selftest():
    import tempfile
    np = _np(); import soundfile as sf
    sr = 48000; d = tempfile.mkdtemp()
    rng = np.random.default_rng(1)

    def take(words_at, dur):
        x = rng.normal(0, 10 ** (-60 / 20), int(dur * sr))
        for a, b in words_at:
            n = int((b - a) * sr); tt = np.arange(n) / sr
            x[int(a * sr):int(a * sr) + n] += 0.2 * np.sin(2 * np.pi * 180 * tt) * np.hanning(n) ** 0.2
        return x
    # take 1: line A at 1.0-1.6 and 2.4-2.9 (an inner 0.8 s pause); line B at 5.0-5.7
    sf.write(f'{d}/t1.wav', take([(1.0, 1.6), (2.4, 2.9), (5.0, 5.7)], 7), sr)
    sf.write(f'{d}/t2.wav', take([(0.5, 1.2)], 3), sr)
    json.dump([{'word': 'hello', 'start': 1.0, 'end': 1.6}, {'word': 'there', 'start': 2.4, 'end': 2.9}],
              open(f'{d}/w1.json', 'w'))
    spec = {'takes': {'t1': 't1.wav', 't2': 't2.wav'}, 'words': {'t1': 'w1.json'},
            'lines': [{'take': 't1', 'start': 0.7, 'end': 2.9, 'text': 'hello there'},  # rough start 0.3 s early
                      {'take': 't2', 'start': 0.5, 'end': 1.2, 'text': 'second'},
                      {'take': 't1', 'start': 5.0, 'end': 5.7, 'text': 'third', 'clamp_end': 5.5}],
            'start': 0.3, 'gaps': [0.4]}
    lines, dur = build(spec, d)
    a, b, c = lines
    assert abs(a['start'] - 0.3) < 1e-6, a
    assert 0.9 < a['src'] + 0.06 < 1.06, ('onset found near 1.0', a['src'])
    assert a['end'] - a['start'] < 2.0, ('inner pause squeezed', a)
    assert abs(b['start'] - (a['end'] + 0.4)) < 0.01, (a, b)
    assert c['end'] - c['start'] < 0.75, ('clamp_end honoured', c)
    w = a['words'][1]['s']
    assert a['start'] < w < a['end'], ('word time mapped inside the line', a)
    x, r = sf.read(f'{d}/vo.wav')
    assert r == sr and abs(len(x) / sr - dur) < 0.01 and np.abs(x).max() <= 0.9
    print('vo_bestof selftest OK')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        selftest()
    elif len(sys.argv) == 2:
        p = sys.argv[1]; lines, dur = build(json.load(open(p)), os.path.dirname(os.path.abspath(p)))
        for L in lines:
            print('%6.2f %6.2f %-3s %s' % (L['start'], L['end'], L['take'], L['text']))
        print('duration', round(dur, 2))
    else:
        print(__doc__); sys.exit(2)
