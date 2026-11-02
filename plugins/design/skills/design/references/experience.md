# Experience Mode: Games, Toys, Creative Tools, Progression

Use when: the surface is played, performed or practised (games, toys, music and creative tools, learning apps with XP/levels/streaks, celebrations, 3D or canvas scenes, screens read mid-action from a distance).

## 1. Stance
- Experience is bold: dials VARIANCE 8-10, MOTION 6-9, DENSITY 2-3. The work (the scene, the instrument, the board) leads from the first frame; the interface recedes.
- Ask first: what leads, what the player does with their hands and eyes, viewing distance, input (touch, keys, mic, MIDI), session length, sound on or off. Batch per `process.md`.
- Settings, lists, stats pages and account screens inside a game are Operate: build them per `apps.md`, quiet and dense. Only the play surface and reward moments go loud.
- One delight thesis per surface. Spend it at moments that earn it: effort, waiting, first use, recovery, mastery.
- One extraordinary set piece per surface (the rare tier), never several. Removal test: would anyone notice it gone? Neighbour test: could a neighbouring product use the moment unchanged? If yes, it is a category effect; rework it from the subject.
- Never fake progress, award XP for nothing, or delay completion for a flourish. Reward real skill: accuracy, consistency, things learned.
- No jokes about money, privacy, loss or blocked work.
- When the world names a technique (WebGL, physics, audio-reactive), build the real thing, not a static imitation, behind `@supports` / feature checks with a working fallback. For an ambitious set piece, propose 2-3 directions and get a pick before code.

## 2. Reward hierarchy (frequency sets the size)

| Tier | Trigger | Budget | Contents |
|---|---|---|---|
| Micro | every correct action, hit, note | ≤150-300ms, local | scale pulse 1.08-1.15, colour flash, tick sound, haptic tick |
| Small | task / round complete | ≤0.8-1.2s, in place | pop-in, ≤40 particles, number count-up |
| Medium | lesson / level complete | 1.5-2s, may take the screen | layered timeline below, badge, summary with real numbers |
| Rare | milestone, first-ever, personal best | 2-3s, full screen, tap to skip | big set piece, unique sound, shareable card |

- Celebration scales with consequence; a routine save just feels certain.
- Controls and per-action micro feedback obey the ≤300ms UI cap (`motion.md`). Small and medium rewards may run longer only because they never block input; rare celebrations are exempt.
- Overlapping rewards merge: add to the live counter or cut the old one to its end state. Never queue a backlog of celebrations, and never rely on `animationend` for correct state.
- Confetti only for real milestones, once per trigger, skipped on bulk repeats. Reward bursts are one-shot, never looping.
- Vary the presentation of frequent rewards (2-4 variants, random particle seeds, pitch steps); identical fanfares become noise. Vary presentation, never fairness.
- Never block input during a reward. The next action is available on frame 1; the reward plays around it.
- Celebration copy names the real achievement with numbers ("12 clean chord changes in a row", "Best run: 94% on time"), never "Awesome!!" (`copy.md`).

**Layered celebration timeline** (medium tier):
```
0ms     flash or scale pop on the cause (the thing the player did)
~50ms   particles from the cause's position
~150ms  number count-up (XP, score)
~400ms  secondary settle: badge, level bar, streak flame
end     resolve to a calm state with the next action focused
```

## 3. Game feel and juice
- Build around the stop, not the travel: the instant an impact arrests is the felt part.
- Schedule effects against known event times (beat grid, clip timings, collision results), never live detection. Only scheduling allows anticipation and same-frame sync.
- Impact kinds differ in motion first, colour second. A light hit is not a paler heavy hit. A blow received is not a strike reversed: rings inward, debris off the body, no flash at the hand. Effects take the world's palette plus one contrasting accent.
- In app UI, shake means error or remote conflict only: 2-4px, non-looping, ≤300ms (motion.md §9). Never shake on success. In games, screen shake belongs to impacts only.

**Trauma screen shake** (smooth, stackable; replaces white-noise `setInterval` shake):
```js
// on hit: trauma = Math.min(1, trauma + 0.3..0.6)  (scale with impact)
const s = trauma * trauma;                    // shake = trauma squared
x = MAX_PX * s * noise(t * 25, 0);            // smooth noise (Perlin/simplex), not Math.random
y = MAX_PX * s * noise(0, t * 25);
rot = MAX_DEG * s * noise(t * 25, 99);        // MAX_DEG 2-3
trauma = Math.max(0, trauma - 1.2 * dt);
// UI: MAX_PX 6-12. Apply to a wrapper transform only, never the HUD.
```

**Hit-stop**: freeze 40-100ms scaled with impact; flash white or pulse scale during the freeze (via a CSS class or outside GSAP, since the global timeline is frozen).
```js
gsap.globalTimeline.timeScale(0);
setTimeout(() => gsap.globalTimeline.timeScale(1), 60); // not delayedCall: it freezes too
// own loop: multiply dt by 0 for the hold, keep input and audio running
```

**Squash and stretch** (keep volume, scaleX ≈ 1/scaleY; anticipation, overshoot, settle). Non-brand game objects only (a ball, a jelly, a coin). A brand character or mascot is NEVER squashed, stretched or deformed, in any medium: uniform scale, tilt and move only, structural scale stays 1.00 x 1.00. Its weight comes from timing, overshoot and rotation; hurt or dead reads through face, pose, tilt, props or light, never a flattened body.
```js
animate(el, { scaleY:[1,.85,1.12,1], scaleX:[1,1.15,.92,1] },
  { duration:.35, times:[0,.15,.45,1] });  // transform-origin: 50% 100% for a landing
```

- Pop-in: `gsap.from(el,{scale:0.6, autoAlpha:0, duration:.45, ease:"back.out(2.5)"})` for non-brand game objects. Bounce and overshoot are allowed there; never on standard controls.
- Overshoot by weight, for brand characters and anything that goes into video: a solid character or object ≤5% (`back.out` ≤1.2, or none); text, cards and glints ≤10% (`back.out` ≤1.7); only a snap of ≤5 frames may reach ~16%. No elastic or bounce eases on them: past these caps it reads as the preset zoom-and-bounce look. Exit mirrors the entrance, quicker.
- Character face changes go through drawn in-betweens (about 3 drawings, ~8 frames), never an opacity crossfade or morph between two stills. Idle is never frozen.
- Pulse 1.0 → 1.15-1.25 → 1 (heart 1.25, badge bloom 1.2 → 1). Exaggeration 10-15% for UI-scale rewards.
- Springs for pop: toast 180/12 (react-spring), press 0.95 / hover 1.05 at Motion spring 400/17. Momentum release may bounce 0.2.
- Checkmark draw 300ms. Row/tile highlight fades over 1-2s.
- Additive blending for emissive effects with `depthWrite:false, depthTest:true`.
- Pool everything; allocate nothing after construction; start effects invisible. Measure the frame cost you get, not the one you expect.
- Calibrate trails and continuous layers per action speed; one global threshold smears fast moves and leaves slow ones bare.

**Particles**
- Burst: radial velocity 5-10, gravity 0.3/frame, life -0.02/frame, alpha and scale track life, all × `ticker.deltaTime` (1.0 at 60fps). Remove the ticker and destroy when all are dead.
- Counts: confetti ≤150 on mobile; ≤40 for small rewards; <1000 total on mobile 3D.
- Never particles or moving backgrounds behind text being read.
- Tools: `canvas-confetti` with `disableForReducedMotion:true`; Pixi v8 `ParticleContainer` for heavy bursts; GSAP Physics2DPlugin for DOM particles.

**Combo and streak escalation**
- Each tier adds visible change: particles ×1.3, trauma +0.1, pitch +1 semitone (`playbackRate = 2 ** (n/12)`), colour step at thresholds 3 / 5 / 10.
- Combo window 1.5-2s. Cap escalation (pitch at +7 to +12 semitones). Show the multiplier where the eyes already are.
- Break a combo quietly: the counter fades, a soft down-step sound at most. No punishment noise, no red flash.

**Number tickers**
- Count over 0.4-0.8s, `power2.out`; `font-variant-numeric: tabular-nums` so width never wobbles. Big jumps: roll the last 2-3 digits.
- Write `textContent` from a ref or motion value; never `setState` per frame. Pixi: `BitmapText` (plain `Text` re-rasterises every change).
- Screen readers get the final value once (`aria-live="polite"`), not every tick.

## 4. Sound and haptics
- Causality: fire on the causal event; match character to the action's physicality.
- Harmony: visual, sound and haptic fire on the same frame. Pre-decode with WebAudio `decodeAudioData`; never `new Audio()` per hit. `new AudioContext({latencyHint:"interactive"})`, resumed on the first user gesture.
- Utility: in menus and chrome, sound and haptics only for success, error, commit, snap; on the play surface the per-hit tick is the core loop. Over-feedback trains people to ignore all of it.
- No UI sound without consent on the web: default off, one visible mute toggle, remembered. Where sound is the product (music tools, games), it starts on the user's first play action.
- Separate volumes: music, effects, voice. In game UI, duck music 3-6dB under key effects. Pool ≤8 voices. Voice-led video is different: music sits 10 LU under speech in gaps and 18 LU under it while someone talks (`edit.md`).
- UI sounds 50-200ms. Rewards rise (major intervals); errors are low, soft and short, never buzzers. Randomise pitch ±3-5% and gain ±10% to avoid the machine-gun effect. These tick and blip rules are for app and game UI only; in a video edit, synth pops and blips are banned and every sound is a real, nameable recording (`edit.md`).
- Instrument and reference sounds are real samples (a recorded open string pitch-shifted, or a CC0 sample set whose licence you read), never a synth imitation. Never a TTS voice where a person is expected.
- Music tools: never play reward sounds over the user's own playing or a mic input being analysed. Use visuals mid-phrase; sound between attempts, in key if tonal.
- Mic input for pitch or onset analysis: `getUserMedia({audio:{echoCancellation:false, noiseSuppression:false, autoGainControl:false}})`; the defaults are tuned for speech and mangle instruments. Show a live input meter so the player knows they are heard, and state plainly when detection is unsure instead of guessing.
- Rhythm and music timing: drive visuals from the audio clock (heard time ≈ `ctx.currentTime - ctx.baseLatency - ctx.outputLatency`, or map with `ctx.getOutputTimestamp()`), never rAF time. Schedule sounds with `source.start(when)` about 100ms ahead from a short look-ahead timer, never fire them from `setTimeout` on the beat. Offer a latency calibration (tap-along offset). Feedback under ~50ms reads as caused; over ~100ms reads as lag. Typical hit windows: perfect ±25-45ms, good ±70-90ms.
- Haptics web: `navigator.vibrate(10-20)` tick, `[20,40,20]` success, `[40,60,40]` error. Android only; iOS Safari ignores it, so haptics never carry meaning alone.
- Haptics native: iOS `UIImpactFeedbackGenerator` light/medium/heavy, `UINotificationFeedbackGenerator` success/warning/error (call `prepare()` before); Android `HapticFeedbackConstants.CONFIRM` / `REJECT`.

## 5. Progression UI (XP, levels, streaks, mastery)
- First level-up inside the first session (3-5 minutes). Curve: XP to next level ≈ `base × n^1.5`; early fast, later steady. Never a wall.
- Level bar: pill track, height 12-16px, fill in the accent, animated 320ms ease-out per increment. Label with real numbers ("1,648 / 2,480 XP"), tabular figures.
- Level-up: fill to 100%, hold 100-150ms, flash, reset to 0, fill the remainder. Never jump the bar backwards without that beat.
- Streaks count days. Show "today done" unmistakably. Forgive: 1 grace day or a freeze. Loss copy is neutral ("Streak reset. Your best is 23 days."), never shame. No guilt notifications, no fake scarcity, no countdown pressure.
- Let the player choose the daily goal. Show what improved with before/after numbers, not only points.
- Never lose progress: autosave at every checkpoint and on `visibilitychange`; a reload resumes where the player was.
- Adaptive difficulty: aim for ~80% success. Below ~60% step down; above ~90% step up.
- Mastery map: locked (muted, legible), available, current (the only pulsing node, 1.6s period, stops under reduced motion), done. One current node at a time.
- Badges only for real milestones; never a wall of unearned badges. Currency only if it buys something real.
- Onboarding: first win within 60s, taught in context, 1-3 concepts, skippable and replayable, shown once.
- Guided setup and calibration are self-paced: each step shows a diagram and one plain instruction, waits for real input (never advances on a timer), has Back and Skip, and a "nothing heard" hint.
- Practice is hands-free: when the instrument or pad is the controller, never send the player back to the mouse mid-session. Continuous rounds, play-to-start, an idle pause, auto-advance when a block is done.
- Ethics floor: no near-miss slot-machine tricks, no variable-ratio rewards for spending, no streak hostage-taking. Dopamine comes from competence.

## 6. Experience surfaces: colour, type, press
- Colour from the world; committed or drenched strategies suit play (`colour.md`). Muted low-energy palettes fail games, habits and practice tools. Playful and learning products default light; dark only when the scene itself is dark (stage, night, space). Exception: the owner's own tools default dark (SKILL.md, My standing taste).
- Still banned (unless it is a pinned brand palette, then still no glow): neon accent on near-black with glow, AI purple-blue, decorative gradients and glass on HUD chrome or level ribbons, emoji as icons (a fire emoji is not a streak icon). Rendered scene lighting is not a decorative gradient.
- Wrong / miss states never rely on colour alone: add shape, position, sound. Check the owner's rules first (this owner dislikes red in UI: use amber or a neutral plus an icon; feedback without red: hit green `#3EE08F`, close yellow `#FFD23F`, miss = dim plus a 4px shake). A game's own death or fail screen keeps its red.
- Display face with character for scores, titles and callouts; heavy weights (700-800) are fine on game chrome. Avoid the overused list (`typography.md`). Scores and timers: tabular figures of the display face, not monospace.
- Tactile key-cap press (deliberate, Experience only): solid same-hue deep shade under the button, no blur.
  ```css
  .key { box-shadow: 0 4px 0 var(--accent-deep); transition: transform 90ms, box-shadow 90ms; }
  .key:active { transform: translateY(4px); box-shadow: 0 0 0 var(--accent-deep); } /* bounds unchanged */
  ```
  Never with hard black offset shadows plus flat saturated ink plus condensed display all together (an AI rendition cluster).
- Touch targets ≥48px in play (bigger than the 44/24 floors); thumb zone for primary actions; every gesture has a visible control.

**Game UI shell**
- Start screen allowed in games (unlike app prototypes) only as one "Play" action over the live world, with Continue first when a save exists; settings and credits secondary. Never a logo splash longer than ~1.5s, never unskippable.
- HUD: ≤4 always-on elements in the corners inside safe areas (layout.md §18); health/time/score where the eyes already are; everything else on demand. HUD never shakes with the camera.
- Pause menu: opens on Esc, P, Start or tab blur; Resume first and focused; then Restart, Settings, Quit with a confirm only if progress would be lost. Gameplay frozen underneath, dimmed with the scrim.
- Menus fully keyboard and gamepad navigable with a visible focus ring; one confirm and one back button everywhere; input prompts match the device in use (keys vs controller glyphs).
- Results screen: real numbers first (score, accuracy, best), one primary "Play again", then "Next"; rewards per §2.
- Tutorials teach by doing in the first level (first win within 60s, §5), not with text walls; controls reference reachable from pause.

## 7. Readability at distance and mid-action
- The CSS px is defined for ~71cm. At distance d, scale by `d / 71cm` for equal size (1m ≈ 1.4×), then more for glance reading.
- Screen read from ~1m while playing (laptop, music stand, TV):

| Role | CSS px at 1m |
|---|---|
| The thing to act on now (next note, target, timer) | 64-96, weight 600-800 |
| Glance values (score, streak, BPM) | ≥40 |
| Secondary labels | ≥20 |
| Anything important | never <18 |

- Glance-critical text and marks ≥7:1; nothing interactive <4.5:1. Strokes and indicator lines ≥3px; markers ≥24px.
- One "now" layer at full strength; "next" dimmed but ≥3:1; everything else quiet or gone. Never make the player read a sentence mid-action: encode by position, shape, size, colour together. Text belongs between attempts.
- Big moves in the periphery only when they are signal. Ambient motion near the focus point is noise.
- TV / 10-foot: min 24px at 1080p, 5% safe area on every edge.
- Test: screenshot, view at 50% size from arm's length, or stand at the real distance. If the "now" item is not found in under 0.5s, enlarge it or remove competitors.

## 8. Reduced motion and accessibility
- Under `prefers-reduced-motion`: keep the feedback, drop the motion. No shake, camera pans or zooms, particles, parallax or squash. Use a colour or opacity change, a static badge, a crossfade, and sound unless muted. The reduced state is the finished state.
- Library switches: motion.md §10, plus `canvas-confetti` `disableForReducedMotion:true`.
- In-game settings beyond the OS flag: screen-shake intensity 0-100% (default 100, 0 under reduced motion), flash toggle, separate volumes, colour-blind safe mode, remappable keys, pause anytime, timing assists or untimed mode.
- No flashing >3/s, no full-viewport moving backgrounds, no slow ~0.2Hz oscillation, no abrupt full-screen brightness jumps. Anything moving >5s gets a pause. Motion is never the only signal of a state change; every audio cue has a visual equivalent.
- Auto-pause gameplay (not just rendering) on `blur` / `visibilitychange`; resume only on player input, with a short countdown for timed play.
- Keyboard play: `keydown` handled, `preventDefault` on Space/arrows inside the game so the page does not scroll; focus visibly on the game root. Controller games: poll the Gamepad API inside the game loop.

## 9. Picking the runtime

| Job | Use |
|---|---|
| Reward UI on DOM | GSAP timelines + canvas particles (`motion.md` for library rules) |
| Authored reward states (idle → win → combo tier) | Rive state machine; code only fires triggers |
| One-shot vector celebration | dotLottie (<100KB ideal, <200KB OK) |
| Many sprites / particles 2D | PixiJS v8; raw Canvas2D under ~300 particles |
| 3D scene | Three.js (vanilla, importmap); R3F + drei only if the app is already React |
| Cheap depth | CSS 3D transforms; vanilla-tilt max 15-25°, perspective 1000, on one hero object, never every card |

- Rive and dotLottie setup, budgets, cleanup and export rules: `motion.md`.

## 10. 2D canvas and PixiJS
- Canvas2D: `canvas.width = cssW * dpr` with dpr ≤2, `ctx.setTransform(dpr,0,0,dpr,0,0)`. Layer canvases: static background drawn once, dynamic foreground per frame. Pre-render static art to an offscreen canvas. No `shadowBlur` per frame. Pixel art: integer positions, `imageSmoothingEnabled=false`, `image-rendering: pixelated`.
- Heavy simulation: `OffscreenCanvas` in a Worker.
- Pixi v8 setup:
  ```js
  const app = new Application();
  await app.init({ resizeTo: el, antialias:false, autoDensity:true, resolution: Math.min(devicePixelRatio,2) });
  el.appendChild(app.canvas);
  ```
- `await Assets.load()` before sprites; pack spritesheets to cut draw calls. Particles: `new ParticleContainer({dynamicProperties:{position:true}})` + `addParticle(new Particle({texture,x,y}))`; changing a static property needs `container.update()`.
- Filters 1-2 max, set `filterArea`, `filters=null` when done. Static vectors `cacheAsTexture()`. `cullable=true`. Destroy with `{children:true, texture:true, textureSource:true}`.
- Stale v7 APIs to refuse: `cacheAsBitmap`, `baseTexture`, `ParticleContainer(count,{...})` + `Sprite`.

## 11. 3D on the web
**Earned only when**: the object is the subject and depth aids understanding (a product to inspect, an instrument or fretboard where hand position in depth matters), the interaction needs rotation or depth, the data has a real third dimension, or it is a game. If a 2D illustration says the same thing, ship 2D. "If you can't explain why it exists, remove it."
**Slop**: floating blob or gradient sphere hero, Vanta or particle field behind text, spinning logo, tilt on every card, 150KB+ of decoration draining battery, a model right at 0° and cardboard at 90°, abstract 3D behind a product launch, 3D WebGL galleries.

**Scene setup**
```js
const renderer = new THREE.WebGLRenderer({ antialias: !isMobile });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));     // 1 on low-end
renderer.toneMapping = THREE.ACESFilmicToneMapping;        // or AgX
renderer.setAnimationLoop(tick);                           // not manual rAF
scene.environment = new THREE.PMREMGenerator(renderer)
  .fromScene(new RoomEnvironment()).texture;               // IBL: most of the "real" look, cheap
```
- Pin the three version in the importmap (never an unversioned URL). WebGPU: `WebGPURenderer` from `three/webgpu` falls back to WebGL2 by itself; use it only when you need compute or TSL, otherwise WebGL.
- Resize: `camera.aspect=w/h; camera.updateProjectionMatrix(); renderer.setSize(w,h)`. Motion via `clock.getDelta()`. Never allocate (Vector3, geometry) in the loop.
- Camera FOV 45-75; near as large and far as small as possible (cures z-fighting; `polygonOffset` as fallback).
- Render on demand when static (R3F `frameloop="demand"` + `invalidate()`); pause on `visibilitychange` and off-screen.
- Controls: damping on, clamp polar angle and zoom, never capture page wheel scroll; on touch, enter rotate mode explicitly so one-finger drags still scroll the page (`touch-action`).
- Loading: a still render at the final framing as poster, crossfade to live; never a spinner over a blank canvas. No-WebGL fallback is that poster.
- Dispose geometry, materials, textures (`material.dispose()` does not free them), render targets, then `renderer.dispose()`.
- R3F: `dpr={[1,2]}`; never setState in `useFrame` (mutate refs × delta); no `new Vector3()` in JSX; `useGLTF` inside `<Suspense>`; toggle `visible` instead of remounting; `dispose={null}` on shared assets. drei: `AdaptiveDpr`, `PerformanceMonitor`, `Detailed`, `Instances`, `Environment`.

**Lighting**
- Three-point: key DirectionalLight 3, fill 1, rim 0.5 behind, low hemisphere/ambient. Real-time lights 3-5, shadow casters 2-3.
- Shadows: tight shadow-camera frustum, `mapSize` 1024 mobile / 2048 desktop, soft PCF (`PCFShadowMap` + `shadow.radius`; recent releases deprecate `PCFSoftShadowMap`), `shadowMap.autoUpdate=false` when static. Studio ground: `ShadowMaterial` opacity ~0.16 beats a blob.
- Write a lighting spec: key direction, colour temperature, intensity, softness; fill or the reason for none; rim or env cue for silhouette; exposure and tone-mapping intent; background; contact shadow.
- Materials must read in neutral light before you tune lights toward a reference.

**Materials**
- Basic (unlit UI), Lambert (cheap, mobile), Standard (PBR default), Physical (clearcoat, transmission; costliest).
- Sample colours from references as RGB medians; never guess. Independent PBR channels: never reuse albedo as roughness, AO or normal.
- `colorSpace = SRGBColorSpace` on colour maps only; normal/roughness/AO stay linear.
- Gloss: roughness 0.05-0.2. Bevels are real geometry, radius 0.02-0.08 (2-4 segments soft, 1 hard).
- Coloured candy/anodised: metalness ~0.35, clearcoat ~0.6, roughness ~0.18, envMapIntensity ~0.7. High metalness lets the environment steal the hue. A purple that survives shading needs R ≳ B.
- Maps ≥1024px for close-ups, 2048 when fidelity matters.

**Budgets** (conservative)

| | Draw calls | Visible tris | Texture memory | DPR | FPS |
|---|---|---|---|---|---|
| Desktop | <100 | <1M (hero model <50k) | 100-150MB | 1-2 | 60 |
| Mobile | <50 | <100k | 30-50MB | 1 | 30-60 |

- Files: model <5MB, ideally <1MB, loaded <2s. glTF/GLB + Draco or meshopt, KTX2/Basis textures, ORM packed. Textures 1024 preferred, 2048 max.
- InstancedMesh for >50 identical objects; `mergeGeometries` for static; LOD; `matrixAutoUpdate=false` on static objects.
- Mobile: no antialias, minimal shadows, no post-processing, Lambert, <1000 particles.
- Profile: `renderer.info.render.calls` / `.triangles`, `renderer.info.memory`, Spector.js.

**Image to Three.js (procedural model from one reference)**
- Keep a state file of pass, targets and scores; it is authoritative over chat memory. Validate the image suits 3D, rate complexity (simple / moderate / complex / ultra), write a quality contract before code.
- Spec hierarchy, materials, pivots, sockets: ≤5 critical + ≤3 important feature targets per pass; a detail inventory of ≥9 details, each mapped to a local feature. Reject a spec that could describe many objects.
- 8 locked passes, only the current one editable: blockout → structural → form → material → surface → lighting → interaction → optimisation. The blockout holds every silhouette-defining part.
- Gates: deterministic checks run before any vision scoring, and vision is never consulted on a hard-gate failure. Continue only with vision score ≥0.7, every critical feature ≥ its own threshold, render + side-by-side sheet, PBR evidence ≥0.7.
- Turntable at 0/90/180/270; non-planar forms hold from ≥2 angles; self-intersection and attachment checks. Look-dev in 3 views: neutral, grazing, reference-match.
- Corrections: 3 per pass, 6 total; stop on repeats, oscillation or plateau and ask.
- Fidelity: 0.4 silhouette, 0.6 macro forms, 0.75 reads right, 0.85 strong real-time, 0.95 near-reference. Never claim 0.9+ from one image. Triangle tiers: low ≤6k, standard ≤60k, hero above.
- Lessons: silhouette IoU misses the interior, so measure inside the outline. ≤10 distinct vertex-Z planes = a slab, not a solid. Parts overlap 0.02-0.05 at seams. Root scale stays [1,1,1]; hide with opacity, not scale. Left/right is a mirror `(x,y,z)→(-x,y,z)` with winding flipped. Tapered sweeps with parallel transport, not tubes. Wait for `map.image.complete` before screenshots (else false chrome). Bind effects to sockets or bones, never magic coordinates. "A box that reads as a box is worse than an honest absence."

## 12. Performance for games
- Frame budget: 16.7ms at 60Hz (plan ~10ms of your own work), 8.3ms at 120Hz. Target 60; simplify below 50.
- Loop: one rAF (or `setAnimationLoop`); fixed-timestep simulation with an accumulator, render interpolated; clamp `dt` to ≤0.1s after tab switches; `performance.now()` for time.
- Zero allocation per frame (pools, preallocated vectors) to avoid GC hitches. Animate only `transform` and `opacity` on DOM HUDs; batch reads before writes.
- Input: act on `pointerdown` / `keydown`, never `click`; `touch-action:none` on the play surface; pointer capture for drags; clear drag state on `pointercancel` and `blur`.
- Quality tiers by measured FPS (rolling rAF delta average or drei `PerformanceMonitor`), not UA sniffing. Step down in order: DPR → particle count → shadows → post-processing → effect layers.
- Idle: render on demand or throttle; pause everything hidden or off-screen. Lazy-start heavy contexts near the viewport; code-split engines with dynamic `import()`; sized poster to avoid CLS.
- Test on a real mid-range phone and a Chromebook-class laptop, with an FPS meter and DevTools Performance (long tasks). `will-change` only during an animation.

## 13. Verify before calling it done
- Screenshots at 1440 / 768 / 390 plus the real play viewport and distance (`process.md`).
- Review motion in slow motion (2-5×) and frame by frame; record a filmstrip of the loudest reward, the quietest and a miss.
- Play it with reduced motion on, sound off, keyboard only, and in colour-blind simulation.
- Check frame cost under the heaviest combo on mobile. Confirm every reward appears for a real achievement and every number shown adds up.
- Anti-slop for this mode: `tells.md` (confetti on every action, mascot spam, glass level ribbons, emoji streak flames, pulsing everything, shame modals).
