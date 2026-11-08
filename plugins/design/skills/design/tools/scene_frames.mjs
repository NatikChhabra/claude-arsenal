#!/usr/bin/env node
// Scene renderer for built ads: an HTML page that draws any moment with window.render(t) becomes exact video frames.
// Use when the ad is made of real pieces (paper, prints, phone screens, stamps) and must sync to a voice-over to the
// frame: ads.md section 9. Deterministic (no wall-clock animation), so a re-render after one fix is identical elsewhere.
//
//   node scene_frames.mjs page.html cues.json OUTDIR [--fps 30] [--size 1080x1920] [--at 2.5,9.3,20.6] [--audio mix.wav --mp4 out.mp4]
//
// The page contract:
//   - window.render(t) draws the frame for t seconds. Use only t (and your cue times) for motion: no CSS transitions,
//     no requestAnimationFrame, no Date.now().
//   - set document.title = 'ready' (or 'fit') once fonts and images are decoded and layout is measured.
//   - the cue file is JSON {dur, cues:[{id,start,end,...beat times}], caps:[{start,end,text,key?}]}. Its cues and caps
//     arrive as window.CUES and window.CAPS before the first render, so timing lives in one file next to the VO's
//     lines.json and a re-time never touches the page.
// --at renders only those times (fast checks of the risky beats); otherwise every frame 0..dur.
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const a = process.argv.slice(2);
if (a.length < 3 || a[0] === '-h' || a[0] === '--help') {
  console.log(fs.readFileSync(new URL(import.meta.url)).toString().split('\n').filter(l => l.startsWith('//')).map(l => l.slice(3)).join('\n'));
  process.exit(a.length < 3 ? 2 : 0);
}
const [page, cueFile, out] = a;
// playwright from the project, the working folder or a global install (npm i -D playwright)
let chromium;
for (const base of [process.cwd() + '/', import.meta.url]) { try { ({ chromium } = createRequire(base)('playwright')); break; } catch {} }
if (!chromium) { console.error('playwright not found: npm i -D playwright (or run from a folder that has it)'); process.exit(2); }
const opt = k => { const i = a.indexOf(k); return i > 0 ? a[i + 1] : null; };
const fps = +(opt('--fps') || 30);
const [W, H] = (opt('--size') || '1080x1920').split('x').map(Number);
const cfg = JSON.parse(fs.readFileSync(cueFile, 'utf8'));
const times = opt('--at') ? opt('--at').split(',').map(Number) : [...Array(Math.ceil(cfg.dur * fps)).keys()].map(i => i / fps);

const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: W, height: H } });
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.resolve(page));
await p.waitForFunction(() => document.title === 'ready' || document.title === 'fit', null, { timeout: 60000 });
await p.evaluate(c => { window.CUES = c.cues || []; window.CAPS = c.caps || []; }, cfg);
fs.mkdirSync(out, { recursive: true });
let i = 0;
for (const t of times) {
  await p.evaluate(t => window.render(t), t);
  await p.screenshot({ path: `${out}/f${String(i++).padStart(5, '0')}.png` });
}
await b.close();
if (errs.length) { console.error('page errors:\n' + errs.join('\n')); process.exit(1); }
console.log(`${i} frames -> ${out}`);

const mp4 = opt('--mp4');
if (mp4 && !opt('--at')) {
  const args = ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', `${out}/f%05d.png`];
  if (opt('--audio')) args.push('-i', opt('--audio'), '-c:a', 'aac', '-b:a', '192k', '-shortest');
  args.push('-c:v', 'libx264', '-crf', '20', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', mp4);
  const r = spawnSync('ffmpeg', args, { stdio: 'inherit' });
  if (r.status) process.exit(r.status);
  console.log(`encoded ${mp4}`);
}
