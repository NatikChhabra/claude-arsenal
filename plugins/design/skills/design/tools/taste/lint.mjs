#!/usr/bin/env node
// design / lint: static scan of source files for the tells this skill bans.
// Catches them before a render, plus the ones a render cannot see (copy habits, motion values).
//
//   node lint.mjs [files or directories ...] [--app] [--video] [--json]
//
// Exit code 1 when any FAIL is found. Zero dependencies. Node 22+.
import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, extname, relative, resolve } from 'node:path';

const args = process.argv.slice(2);
if (args.includes('-h') || args.includes('--help')) { console.log('usage: node lint.mjs [files or directories ...] [--app] [--video] [--json]'); process.exit(0); }
const asJson = args.includes('--json');
// App screens (references/apps.md) keep quiet table and panel lines, faint shadows, data labels
// and their own typefaces.
// Video mode is for motion graphics rendered to video (overlays, title cards, stings over footage):
// text-shadow, -webkit-text-stroke, paint-order stroke and drop-shadow filters carry text over a moving
// picture, one neutral scrim or vignette gradient per file is allowed, ease-in on exits is allowed, and
// scale(0) stays a WARN (fine for particles). Everything else is unchanged.
// A direction.json in .design-check/ (or the old .taste-skill/) with "kind": "app" or "video" switches the mode on.
let appMode = args.includes('--app');
let videoMode = args.includes('--video');
for (const p of ['.design-check/direction.json', '.taste-skill/direction.json']) {
  try { const k = JSON.parse(readFileSync(p, 'utf8')).kind; if (k === 'app') appMode = true; if (k === 'video') videoMode = true; break; } catch {}
}
const APP_LEVEL = { hairline: null, 'outlined-box': null, 'default-font': null, numbering: 'WARN', mono: 'WARN', shadow: 'WARN', eyebrow: 'WARN', 'cta-copy': null, 'h-screen': null };
const roots = args.filter((a) => !a.startsWith('--'));
if (!roots.length) roots.push('.');
const EXT = new Set(['.html', '.htm', '.css', '.scss', '.less', '.js', '.jsx', '.ts', '.tsx', '.vue', '.svelte', '.astro', '.mdx']);
const SKIP = new Set(['node_modules', '.git', '.next', '.nuxt', '.svelte-kit', 'dist', 'build', 'out', '.vercel', '.design-check', '.taste-skill', 'coverage', '.turbo', 'vendor']);

const files = []; const tooBig = [];
const walk = (p) => {
  let st; try { st = statSync(p); } catch { return; }
  if (st.isDirectory()) { for (const f of readdirSync(p)) if (!SKIP.has(f) && !f.startsWith('.')) walk(join(p, f)); }
  else if (EXT.has(extname(p)) && !/\.min\.|\.d\.ts$|(^|[\\/])(package-lock\.json|yarn\.lock|pnpm-lock\.yaml|bun\.lockb?|[^\\/]+\.lock)$/.test(p)) { if (st.size < 4000000) files.push(p); else tooBig.push(p); }
};
for (const r of roots) {
  try { statSync(resolve(r)); } catch { console.error(`Not found: ${r}`); process.exit(2); }
  walk(resolve(r));
}
if (!files.length) { console.error(`No source files (${[...EXT].join(' ')}) under: ${roots.join(', ')}`); process.exit(2); }
if (tooBig.length) console.error(`Skipped (over 4 MB, check by hand): ${tooBig.join(', ')}`);

// Each rule: [level, id, regex, message]. Tested per line. `code` lines (inside <pre>/<code>) skip the mono rule.
const R = [
  ['FAIL', 'mono', /\bfont-mono\b|font-family\s*:[^;{}]*(mono\b|monospace|Courier|Consolas|Menlo|Monaco)|(JetBrains|Geist|IBM\+?Plex|Space|DM|Roboto|Fragment|Azeret|Red\+?Hat|Martian|Commit|Departure|Fira)[+_ ]?Mono|Geist_Mono|GeistMono|Fira[+ ]Code|ui-monospace/i, 'Monospace type. Only literal code may be monospace.'],
  ['FAIL', 'gradient', /(linear|radial|conic)-gradient\(|\bbg-(gradient|linear|radial|conic)-|\b(from|via)-(?!\[?0)[a-z]+-\d{2,3}\b/, 'Gradient fill. Use a flat colour or a real image (a neutral scrim over a photo is the one exception).'],
  ['FAIL', 'gradient-text', /bg-clip-text|background-clip\s*:\s*text|text-transparent/, 'Gradient / clipped text. Use solid colour.'],
  ['FAIL', 'shadow', /box-shadow\s*:\s*(?!none|0 0 #0000|var\(--tw)|(?<![.$])\bshadow(-(sm|md|lg|xl|2xl|inner|\[[^\]]+\]))?(?=["'\s`])(?<!-shadow)|drop-shadow\(|\bdrop-shadow(-|\b)|text-shadow\s*:\s*(?!none)/, 'Shadow. Elements at rest carry none; only real overlays (menu, dialog, sticky bar) may.'],
  ['FAIL', 'numbering', />\s*[(\[]?0[1-9][)\]]?\.?\s*<|["'`]\s*0[1-9]\s*["'`]|decimal-leading-zero|>\s*(Step|Phase|No\.?|Chapter)\s*0?\d\s*</i, 'Decorative index numbering (01 / 02 / 03).'],
  ['WARN', 'numbering', /padStart\(\s*2\s*,\s*["']0["']\s*\)/, 'Zero-padding in script. Fine for a clock, a date or a price; if it builds 01 / 02 / 03 labels, remove it.'],
  ['FAIL', 'eyebrow', /class(Name)?\s*=\s*["'`{][^"'`}]*\b(eyebrow|kicker|overline|pretitle|pre-title|suptitle|sup-title|tagline-label|section-label|section-tag)\b|\.(eyebrow|kicker|overline|pretitle|section-label|section-tag)\b\s*[{,]/i, 'Eyebrow / kicker label above a heading.'],
  ['FAIL', 'micro-label', /(?=[^"'`]*\buppercase\b)(?=[^"'`]*\btracking-(wide|wider|widest|\[[^\]]+\])\b)(?=[^"'`]*\btext-(xs|\[1[0-3]px\]|\[0?\.[67]\d*rem\])\b)[^"'`]+/, 'Tiny uppercase letter-spaced label.'],
  ['FAIL', 'purple', /\b(bg|text|from|to|via|border|ring|fill|stroke|shadow|decoration|outline)-(purple|violet|indigo|fuchsia)-\d{2,3}\b|#(6366f1|8b5cf6|7c3aed|a855f7|4f46e5|a78bfa|818cf8|9333ea|6d28d9|c084fc)\b/i, 'Indigo / violet: the generated-page accent.'],
  ['FAIL', 'claude-palette', /#(d97757|da7756|c15f3c|cc785c|bd5d3a|f0eee6|faf9f5|f5f4ed|eeece2|e8e6dc)\b/i, 'Claude-brand cream / terracotta colour.'],
  ['FAIL', 'emoji', /[\u{1F300}-\u{1FAFF}\u{2700}-\u{27BF}\u{2600}-\u{26FF}]/u, 'Emoji used as UI.'],
  ['FAIL', 'lorem', /lorem ipsum|dolor sit amet/i, 'Placeholder copy shipped.'],
  ['FAIL', 'hairline', /<hr\b|\bdivide-[xy](-\d|\b)|\b(h|w)-px\b|border-(top|bottom|left|right)\s*:\s*(0?\.5|1)px|\bborder-[tblrxy](?![-\w])|\bborder-[tblrxy]-(?!0\b|none)\[?1?(px)?\]?(?=["'\s`])|height\s*:\s*1px/, 'Thin rule / divider line. Separate with space, tone or scale; lines belong to real tables and form fields.'],
  ['WARN', 'outlined-box', /border\s*:\s*1px\s+solid|\bborder\b(?=[^"'`]*\brounded)/, 'A 1px outlined box. Prefer a filled surface or no box.'],
  ['WARN', 'glass', /backdrop-blur|backdrop-filter\s*:/, 'Backdrop blur. One sticky bar at most; glass cards are a tell.'],
  ['WARN', 'copy', /\b(unlock|unleash|supercharge|seamless(ly)?|elevate|empower(s|ing)?|revolutioni[sz]e|game[- ]chang(er|ing)|cutting[- ]edge|next[- ]gen(eration)?|world[- ]class|best[- ]in[- ]class|all[- ]in[- ]one|effortless(ly)?|blazing(ly)?[- ]fast|lightning[- ]fast|reimagin(e|ed|ing)|delve|tapestry|leverage|synergy|streamline|robust|holistic|turbocharge|transform the way|take your .{1,30} to the next level|say goodbye to|in today'?s|the future of|built for the modern|not just .{1,40}[,\u2014-] (it'?s|but)|more than (just )?a)\b/i, 'Stock marketing phrase. Say the specific thing the product does.'],
  ['WARN', 'cta-copy', />\s*(Learn more|Get started|Click here|Read more|Discover more|Explore now|Submit)\s*</i, 'Generic button label. Name the action or the thing ("Book a table", "See the plans").'],
  ['WARN', 'default-font', /family=(Inter|Poppins|Montserrat|Roboto|Open\+Sans|Space\+Grotesk|Instrument\+Serif|Playfair\+Display|Plus\+Jakarta\+Sans|Outfit|Sora|Lato|Nunito|Raleway)\b|font-family\s*:\s*["']?(Inter|Poppins|Montserrat|Roboto|Space Grotesk|Instrument Serif|Playfair Display|Plus Jakarta Sans|Outfit|Sora)\b|from ["']next\/font\/google["'].*\b(Inter|Poppins|Montserrat|Space_Grotesk|Instrument_Serif|Playfair_Display|Plus_Jakarta_Sans|Outfit|Sora)\b|\b(Inter|Poppins|Space_Grotesk|Instrument_Serif|Playfair_Display)\s*\(\s*\{/, 'A default typeface. Use the faces named by the drawn direction.'],
  ['WARN', 'transition-all', /transition\s*:\s*all\b|\btransition-all\b/, 'transition: all. Name the properties (transform, opacity).'],
  ['WARN', 'ease-in', /(?<![-\w])ease-in(?!-out)\b/, 'ease-in on UI feels sluggish. Use a strong ease-out for enters and exits.'],
  ['WARN', 'scale-zero', /scale\(\s*0\s*\)|\bscale-0\b/, 'Entering from scale(0). Start at 0.95-0.98 with opacity 0.'],
  ['WARN', 'h-screen', /\bh-screen\b|height\s*:\s*100vh/, '100vh jumps on mobile. Use 100svh / 100dvh.'],
  ['WARN', 'bounce', /animate-(bounce|ping|pulse)\b/, 'Looping attention animation (bounce / ping / pulse dot).'],
];
if (appMode) {
  for (const r of R) if (r[1] in APP_LEVEL) r[0] = APP_LEVEL[r[1]];
  R.push(['FAIL', 'placeholder-data', /\b(John|Jane) Doe\b|\bAcme( Inc| Corp)?\b|\bexample\.com\b|\bFirstname Lastname\b|\b123 Main St\b/, 'Placeholder data. Use believable names, amounts that add up and real units for this product.']);
  R.push(['WARN', 'framework-colour', /#(3b82f6|2563eb|1d4ed8|60a5fa|10b981|22c55e|ef4444|f59e0b)\b/i, 'A framework default colour (Tailwind blue, green, red, amber). Take the accent and status colours from the dealt style.']);
}

if (videoMode) {
  for (const r of R) {
    if (r[1] === 'shadow') {
      r[2] = /box-shadow\s*:\s*(?!none|0 0 #0000|var\(--tw)|(?<![.$])\bshadow(-(sm|md|lg|xl|2xl|inner|\[[^\]]+\]))?(?=["'\s`])(?<!-shadow)/;
      r[3] = 'Box shadow. In video, text-shadow, a text stroke and drop-shadow filters carry text over footage; boxes at rest carry none.';
    }
    if (r[1] === 'ease-in') r[0] = null; // exits may accelerate away
    if (r[1] === 'scale-zero') r[3] = 'scale(0). Fine for a particle popping in or out; a word or a card enters from 0.95-0.98 with opacity 0.';
  }
}
// A scrim or vignette: every colour in the gradient is grey, black, white or transparent (channel spread <= 14,
// as inspect judges it). Anything else that names a colour (red, var(), hsl(), oklch(), from-purple-500) is not neutral.
// ponytail: one line only; a gradient whose stops sit on the next lines counts as not neutral.
const GEOM = new Set(['to', 'top', 'bottom', 'left', 'right', 'center', 'at', 'circle', 'ellipse', 'closest-side', 'closest-corner', 'farthest-side', 'farthest-corner', 'in', 'srgb', 'transparent', 'black', 'white', 'gray', 'grey']);
const TW_DIR = /^(t|b|l|r|tl|tr|bl|br)$/;
const TW_NEUTRAL = /^(black|white|transparent|neutral|zinc|stone)$/; // Tailwind gray and slate are blue-tinted
const greyish = (c) => c.length === 3 && Math.max(...c) - Math.min(...c) <= 14;
const neutral = (line) => {
  let colours = 0;
  for (const [, n] of line.matchAll(/\b(?:from|via|to)-([a-z]+)\b/g)) { if (TW_DIR.test(n)) continue; if (!TW_NEUTRAL.test(n)) return false; colours++; }
  for (const g of line.matchAll(/gradient\(/g)) {
    const start = g.index + g[0].length; let depth = 1, j = start;
    for (; j < line.length && depth; j++) { if (line[j] === '(') depth++; else if (line[j] === ')') depth--; }
    let bad = false;
    const body = line.slice(start, j)
      .replace(/rgba?\(([^)]*)\)/g, (_, a) => { bad ||= !greyish(a.split(/[,\s/]+/).filter(Boolean).slice(0, 3).map(Number)); colours++; return ' '; })
      .replace(/#([0-9a-f]{3,8})\b/gi, (_, h) => { const x = h.length <= 4 ? [...h.slice(0, 3)].map((c) => c + c).join('') : h.slice(0, 6); bad ||= !greyish([0, 2, 4].map((k) => parseInt(x.slice(k, k + 2), 16))); colours++; return ' '; });
    if (bad) return false;
    for (const [w] of body.matchAll(/(?<![\w.#-])[a-z][a-z-]*/gi)) { const k = w.toLowerCase(); if (!GEOM.has(k)) return false; if (/^(transparent|black|white|gr[ae]y)$/.test(k)) colours++; }
  }
  return colours > 0;
};

const findings = [];
let emDashes = 0;
for (const file of files) {
  const rel = relative(process.cwd(), file).split('\\').join('/');
  const lines = readFileSync(file, 'utf8').split(/\r?\n/);
  let inCode = false; let selector = ''; let pending = ''; let scrimUsed = false; let inBlock = false;
  lines.forEach((line, i) => {
    // prose inside a /* block comment */ that runs over several lines is not code: the shadow rule reads past it
    const wasInBlock = inBlock; const open = line.lastIndexOf('/*'), close = line.lastIndexOf('*/');
    if (inBlock ? close >= 0 && close > open : false) inBlock = false; else if (open >= 0 && open > close) inBlock = true;
    const noBlock = wasInBlock ? (close >= 0 ? line.slice(close + 2) : '') : line;
    // track the CSS selector we are inside, so rules scoped to [data-ui] (interface fragments) keep their own lines
    if (line.includes('{')) { selector = pending + line.slice(0, line.indexOf('{')); pending = ''; } else if (!line.includes('}')) pending = (pending + ' ' + line).slice(-300);
    const inUi = /data-ui/.test(selector) || /data-ui/.test(line);
    if (line.includes('}') && !line.includes('{')) { selector = ''; pending = ''; }
    if (/<(pre|code)\b/i.test(line)) inCode = true;
    const codeLine = inCode || /<(pre|code|kbd|samp)\b/i.test(line);
    if (/<\/(pre|code)>/i.test(line)) inCode = false;
    if (line.length > 2000) return; // minified or data
    if (/design-ignore|taste-skill-ignore/.test(line)) return;
    if (!/^\s*(\/\/|\/\*|\*|<!--)/.test(line)) emDashes += (line.replace(/\/\/.*$|\/\*.*?\*\/|<!--.*?-->/g, '').match(/\u2014/g) || []).length; // comments are not copy
    for (const [level, id, re, message] of R) {
      if (!level) continue;
      if (id === 'mono' && (codeLine || /(^|[\s,>+~(])(pre|code|kbd|samp)\b|code/i.test(selector))) continue; // real code may be monospace
      if ((id === 'hairline' || id === 'outlined-box') && /(^|[\s,>+~(])(table|thead|tbody|tfoot|tr|td|th|input|textarea|select|fieldset)\b/i.test(selector)) continue; // real tables and form fields keep their lines
      if (inUi && (id === 'hairline' || id === 'outlined-box' || id === 'shadow')) continue;
      if (id === 'hairline' && /sr-only|visually-hidden|clip(-path)?\s*:|outline/i.test(line + selector)) continue; // screen-reader helpers and focus outlines are not rules
      if ((id === 'copy' || id === 'cta-copy' || id === 'emoji') && /^\s*(\/\/|\/\*|\*|import |@import|<!--)/.test(line)) continue;
      const m = (id === 'shadow' ? noBlock.replace(/\/\*.*?\*\/|<!--.*?-->|(^|\s)\/\/.*$|^\s*(\/\*|\*).*$/g, '') : line).match(re); // a comment that says "shadow" is not a class, and neither is light.shadow in a 3D scene
      if (!m) continue;
      if (id === 'gradient' && videoMode && !scrimUsed && neutral(line)) { scrimUsed = true; continue; } // the one scrim or vignette
      findings.push({ level, id, file: rel, line: i + 1, match: m[0].trim().slice(0, 70), message });
    }
  });
}
if (emDashes > 4) findings.push({ level: 'WARN', id: 'em-dash', file: '(all files)', line: 0, match: `${emDashes} em dashes`, message: 'Em dashes. The house rule bans them in visible text: use a full stop, a comma or a colon (preflight fails on any one).' });

if (asJson) { console.log(JSON.stringify({ files: files.length, findings }, null, 1)); process.exit(findings.some((f) => f.level === 'FAIL') ? 1 : 0); }

const byId = new Map();
for (const f of findings) { const k = f.level + ' ' + f.id; if (!byId.has(k)) byId.set(k, []); byId.get(k).push(f); }
console.log(`DESIGN · LINT   ${files.length} file(s)`);
if (!findings.length) console.log('\nNo banned patterns in source. Now run inspect.mjs on the rendered page.');
for (const lvl of ['FAIL', 'WARN']) {
  const keys = [...byId.keys()].filter((k) => k.startsWith(lvl));
  if (!keys.length) continue;
  console.log(`\n${lvl}`);
  for (const k of keys) {
    const list = byId.get(k);
    console.log(`  [${list[0].id}] ${list[0].message}  (${list.length}×)`);
    for (const f of list.slice(0, 6)) console.log(`      ${f.file}:${f.line}  ${f.match}`);
    if (list.length > 6) console.log(`      … ${list.length - 6} more`);
  }
}
const fails = findings.filter((f) => f.level === 'FAIL').length;
console.log(`\nRESULT: ${fails} FAIL, ${findings.length - fails} WARN${fails ? ': fix the FAILs before rendering.' : ''}`);
console.log('Interface fragments marked data-ui keep their own borders and shadows. Any other line that must keep a flagged pattern for a real reason can carry the comment design-ignore (the old taste-skill-ignore still works).');
process.exit(fails ? 1 : 0);
