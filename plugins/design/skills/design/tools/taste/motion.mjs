#!/usr/bin/env node
// Motion film: plays a page on a virtual clock and photographs it at a fixed frame rate, so motion can be judged
// frame by frame (motion.md §14). A shim injected before the page's own scripts drives setTimeout, setInterval,
// requestAnimationFrame, performance.now, Date.now and every CSS / Web Animation from that one clock, so each frame
// is exactly on its beat, with no recording jitter. (Chrome's virtual-time policy can't be used: new headless
// stops painting while it is paused.) Limits: Workers, audio clocks and document.timeline.currentTime stay real. Writes the frames and contact sheets (6 x 5 tiles, read left to right).
// Zero dependencies: Node 22+ and an installed Chrome / Edge / Chromium (or CHROME_PATH).
//
//   node motion.mjs <url | path/to/index.html[?query][#hash]> [--size 1920x1080] [--fps 10] [--seconds 6]
//        [--at "ArrowDown@3.4,Enter@4.2,js:startMove()@2"] [--tv] [--out DIR] [--keep-frames]
//
//   --at   events on the page clock: a key name (ArrowDown, Enter, Escape, " " ...) or js:<expression> (no commas), then @seconds
//   --tv   also writes sheets as an old TV shows them: 480 lines, soft, 5% overscan cut from every edge
import { createServer } from 'node:http';
import { existsSync, mkdirSync, readFileSync, statSync, rmSync } from 'node:fs';
import { resolve, dirname, extname, relative, sep, join } from 'node:path';
import { Browser } from './lib/cdp.mjs';

const argv = process.argv.slice(2);
const opt = (k, d) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : d; };
const flag = (k) => argv.includes(k);
const VALUED = ['--size', '--fps', '--seconds', '--at', '--out'];
const target = argv.find((a, i) => !a.startsWith('--') && !VALUED.includes(argv[i - 1]));
if (!target) { console.error('usage: node motion.mjs <url | file.html> [--size WxH] [--fps N] [--seconds S] [--at "Key@s,js:expr@s"] [--tv] [--out DIR]'); process.exit(2); }
const [W, H] = opt('--size', '1920x1080').split('x').map(Number);
const fps = Number(opt('--fps', '10')), seconds = Number(opt('--seconds', '6'));
const out = resolve(opt('--out', '.design-check/motion'));
const events = (opt('--at', '') || '').split(',').filter(Boolean).map((s) => {
  const at = s.lastIndexOf('@'); return { what: s.slice(0, at), t: Number(s.slice(at + 1)) };
}).sort((a, b) => a.t - b.t);
if (events.some((e) => !Number.isFinite(e.t))) { console.error('--at: every event needs @seconds'); process.exit(2); }

// one throwaway http server on 127.0.0.1: the target (when it is a local file, so module scripts and fetch behave,
// like the inspector) and the contact sheets, which load through a real navigation so they are painted before capture
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.json': 'application/json', '.wav': 'audio/wav', '.mp3': 'audio/mpeg', '.woff2': 'font/woff2' };
let url = target, root = null;
const [pathq, hash = ''] = target.split('#'), [path, query = ''] = pathq.split('?');
const sheetHtml = new Map();
const send = (res, type, body) => { res.writeHead(200, { 'content-type': type }); res.end(body); };
const server = createServer((req, res) => {
  const u = decodeURIComponent(req.url.split('?')[0]);
  if (u.startsWith('/__motion/sheet/')) return sheetHtml.has(u) ? send(res, 'text/html', sheetHtml.get(u)) : (res.writeHead(404), res.end());
  if (u.startsWith('/__motion/f/')) { const f = join(out, 'frames', u.slice(12).replace(/[^\w.]/g, '')); return existsSync(f) ? send(res, 'image/jpeg', readFileSync(f)) : (res.writeHead(404), res.end()); }
  const p = root && resolve(root, '.' + u);
  if (!p || !p.startsWith(root) || !existsSync(p) || statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  send(res, TYPES[extname(p).toLowerCase()] || 'application/octet-stream', readFileSync(p));
});
await new Promise((r) => server.listen(0, '127.0.0.1', r));
const base = `http://127.0.0.1:${server.address().port}`;
if (!/^https?:/.test(target)) {
  const file = resolve(path); if (!existsSync(file)) { console.error('no such file: ' + file); server.close(); process.exit(2); }
  root = dirname(file);
  url = `${base}/${relative(root, file).split(sep).map(encodeURIComponent).join('/')}${query ? '?' + query : ''}${hash ? '#' + hash : ''}`;
}

rmSync(out, { recursive: true, force: true }); mkdirSync(join(out, 'frames'), { recursive: true });
// software compositing: the headless GPU path drops whole compositor frames under load (busy frames came out as bare
// background in about half the runs); the software compositor paints every frame it is asked for
const browser = await Browser.launch({ width: W, height: H, extraArgs: ['--disable-gpu', '--disable-gpu-compositing'] });
const page = await browser.newPage({ width: W, height: H });
// the clock shim: page time only moves when __vt.advance(ms) is called, in 60 Hz ticks
const SHIM = `(() => {
  let T = 0, id = 1, rafs = []; const q = [], base = Date.now(), seen = new WeakMap(), nativeRaf = window.requestAnimationFrame.bind(window);
  const later = (fn, a) => typeof fn === 'function' ? () => fn(...a) : () => (0, eval)(fn);
  window.setTimeout = (fn, ms = 0, ...a) => { const i = id++; q.push({ i, at: T + Math.max(0, +ms || 0), fn: later(fn, a) }); return i; };
  window.setInterval = (fn, ms = 0, ...a) => { const i = id++, every = Math.max(1, +ms || 0); q.push({ i, at: T + every, every, fn: later(fn, a) }); return i; };
  window.clearTimeout = window.clearInterval = (i) => { const k = q.findIndex((e) => e.i === i); if (k >= 0) q.splice(k, 1); };
  window.requestAnimationFrame = (fn) => { const i = id++; rafs.push({ i, fn }); return i; };
  window.cancelAnimationFrame = (i) => { rafs = rafs.filter((r) => r.i !== i); };
  performance.now = () => T; Date.now = () => base + T;
  const sync = () => { for (const a of document.getAnimations()) {
    if (!seen.has(a)) seen.set(a, T - (a.currentTime || 0));
    if (a.playState === 'finished') continue;
    const t = (T - seen.get(a)) * (a.playbackRate || 1), end = a.effect ? a.effect.getComputedTiming().endTime : Infinity;
    if (t >= end) a.finish(); else { a.pause(); a.currentTime = t; }
  } };
  window.__vt = { now: () => T, paint: () => new Promise((r) => nativeRaf(() => nativeRaf(r))), advance(ms) {
    const until = T + ms;
    while (T < until) {
      const next = Math.min(until, T + 1000 / 60);
      for (;;) { q.sort((a, b) => a.at - b.at); const e = q[0]; if (!e || e.at > next) break;
        T = Math.max(T, e.at); if (e.every) e.at += e.every; else q.shift(); try { e.fn(); } catch (err) { console.error(err); } }
      T = next; const rs = rafs; rafs = []; for (const r of rs) { try { r.fn(T); } catch (err) { console.error(err); } }
      sync();
    } } };
})();`;
await page.send('Page.addScriptToEvaluateOnNewDocument', { source: SHIM });
const KEYS = { Enter: 13, Escape: 27, ' ': 32, ArrowLeft: 37, ArrowUp: 38, ArrowRight: 39, ArrowDown: 40, Backspace: 8, Tab: 9 };
async function fire(what) {
  if (what.startsWith('js:')) return page.eval(what.slice(3)).catch((e) => console.error('  js event failed: ' + e.message));
  const code = KEYS[what] ?? what.toUpperCase().charCodeAt(0);
  for (const type of ['rawKeyDown', 'keyUp']) {
    await page.send('Input.dispatchKeyEvent', { type, key: what, code: what.length === 1 ? 'Key' + what.toUpperCase() : what, windowsVirtualKeyCode: code });
  }
}

// the page loads in real time (fonts, images) while its clock stays at 0; frame 0 is that first state
await page.goto(url, { settleMs: 400 });
const step = 1000 / fps, total = Math.round(seconds * fps);
const PER = 30, COLS = 6, TW = 480, TH = Math.round(TW * H / W);
let ei = 0;
for (let f = 0; f < total; f++) {
  const now = f * step;
  while (ei < events.length && events[ei].t * 1000 <= now) await fire(events[ei++].what);
  // two real paint frames first: on heavy pages raster lags behind the DOM, and an early capture shows unpainted tiles as black blocks
  await page.eval('__vt.paint()');
  // full frames; the sheet page scales them down (a scaled clip capture comes out blank on pages with a viewport meta)
  await page.screenshot({ path: join(out, 'frames', `f${String(f).padStart(4, '0')}.jpg`), quality: 82 });
  await page.eval(`__vt.advance(${step})`);
}
const errors = page.consoleErrors.slice();
await page.close();   // the filmed page keeps a frozen clock; close it before the sheets are drawn
await (await browser.newPage({ width: 64, height: 64 })).goto('about:blank', { settleMs: 50 });   // after a close, the next new window paints black once: spend that on a blank

// contact sheets: the frames laid out on a page and photographed by the same browser (no image library needed)
const sheets = [];
async function sheet(name, tv) {
  const frames = [...Array(total).keys()];
  for (let s = 0; s * PER < frames.length; s++) {
    const slice = frames.slice(s * PER, (s + 1) * PER), rows = Math.ceil(slice.length / COLS);
    // Each frame is drawn into its own small canvas, one at a time: thirty full-size images on one page overrun
    // Chrome's decode budget and some tiles never paint (seen as black blocks). tv: the frame is drawn 11% larger
    // and centred, so 5% of every edge falls outside the tile (overscan), then softened.
    const srcs = slice.map((f) => `/__motion/f/f${String(f).padStart(4, '0')}.jpg`), labels = slice.map((f) => `${(f / fps).toFixed(1)}s`);
    const html = `<!doctype html><meta charset="utf-8"><style>body{margin:0;background:#111;display:grid;grid-template-columns:repeat(${COLS},${TW}px);gap:4px;padding:4px}
      .c{position:relative;width:${TW}px;height:${TH}px}canvas{display:block}
      b{position:absolute;left:0;top:0;background:#0d0d0d;color:#f2f2f2;font:12px/1 monospace;padding:3px 5px}</style>
      ${labels.map((l) => `<div class="c"><canvas width="${TW}" height="${TH}"></canvas><b>${l}</b></div>`).join('')}
      <script>window.__ready = (async () => { const cs = document.querySelectorAll('canvas'), srcs = ${JSON.stringify(srcs)};
        for (let i = 0; i < srcs.length; i++) { const im = new Image(); im.src = srcs[i]; await im.decode();
          const g = cs[i].getContext('2d'); ${tv ? `g.filter = 'blur(.55px)'; g.drawImage(im, -${Math.round(TW * .055)}, -${Math.round(TH * .055)}, ${Math.round(TW * 1.11)}, ${Math.round(TH * 1.11)});` : `g.drawImage(im, 0, 0, ${TW}, ${TH});`} }
        return true; })();</script>`;
    const key = `/__motion/sheet/${name}-${s}`; sheetHtml.set(key, html);
    const sp = await browser.newPage({ width: COLS * (TW + 4) + 4, height: rows * (TH + 4) + 4 });
    await sp.goto(base + key, { settleMs: 50 });
    await sp.eval('window.__ready');
    await sp.eval(`new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r)))`);
    const png = join(out, `${name}-${String(s + 1).padStart(2, '0')}.jpg`);
    await sp.screenshot({ path: png, quality: 82 }); await sp.close(); sheets.push(png);
  }
}
await sheet('sheet', false);
if (flag('--tv')) await sheet('tv', true);
await browser.close(); server.close();
if (!flag('--keep-frames')) rmSync(join(out, 'frames'), { recursive: true, force: true });

console.log(`DESIGN · MOTION   ${total} frames at ${fps} fps, ${seconds}s, ${W}x${H}`);
for (const e of events) console.log(`  event ${e.what} @ ${e.t}s`);
for (const e of errors) console.log(`  PAGE ERROR  ${e}`);
console.log('\nLOOK AT THE FRAMES: open every sheet with your image viewer / Read tool before saying anything about the motion:');
for (const s of sheets) console.log('  ' + relative(process.cwd(), s));
process.exit(errors.length ? 1 : 0);
