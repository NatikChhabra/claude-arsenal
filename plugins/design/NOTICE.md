# Notices

The design standard in `skills/design/` (SKILL.md and `references/`) is written for this plugin. Its rules were studied from, and then rewritten and reconciled against, the public design skills and guides below. No text from them is carried over verbatim; credit goes to their authors for the ideas.

## Upstream reading list (ideas, not code)

- taste-skill (leonxlnx/taste-skill, MIT)
- impeccable (pbakaus/impeccable)
- UI UX Pro Max
- Emil Kowalski's animation and interface writing
- design-taste
- dembrandt
- Claude Design / open-design
- awesome-design-md (VoltAgent/awesome-design-md)
- claudedesignskills
- img2threejs
- scrollcraft

Why some of their tooling is not shipped (network calls, unpinned installs, session hooks) is recorded in `skills/design/references/tools.md` under "Not adopted".

## Third-party code (MIT)

Two checkers under `skills/design/tools/` are third-party MIT code, modified for this plugin (renamed output, banners and escape comment, a video mode, `.js`/`.mjs` scanning). Each keeps its licence file beside it, and the notices are repeated here as MIT requires.

### `skills/design/tools/preflight.mjs`

Licence file: `skills/design/tools/LICENSE-preflight`.

```
MIT License

Copyright (c) 2026 Nguyễn Phú Cường

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### `skills/design/tools/taste/` (lint.mjs, inspect.mjs, lib/)

Licence file: `skills/design/tools/taste/LICENSE`. Origin: taste-skill (leonxlnx/taste-skill).

```
MIT License

Copyright (c) 2026 Leonxlnx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
