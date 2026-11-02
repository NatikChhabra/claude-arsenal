#!/usr/bin/env python3
"""svgkit - exam-shaped diagram engine for a study vault. Run from the vault root.

Renders diagrams from compact JSON specs into the `diagrams` folder of study.json (or --out).
Every diagram paints its own light surface, so it reads identically in Obsidian's
light and dark themes (an SVG embedded via ![[x.svg]] cannot inherit theme CSS).

Archetypes:
  timeline  vertical dated spine        {events:[{date,label,note?,color?}]}
  stages    process chain with arrows   {steps:[{label,sub?}]}
  compare   2-3 column comparison       {columns:[{title,color?,items:[...]}]}
  layers    hierarchy, widest at top    {levels:[{label,sub?}]}
  matrix    labelled grid               {cols:[...],rows:[...],cells:[[{label,sub?}]]}
  bars      value chart                 {data:[{label,value,color?}],unit?,target?}
  cycle     closed loop                 {nodes:[{label,sub?}]}
  dots      dot plot on a value axis    {rows:[{label,values:[...]}],series:[{name,color}],domain:[lo,hi],ticks?}
  form      page-layout format card     {lines:[{text,align?,style:head|title|body|slot|small|gap,note?,must?}],box?}
            (a letter / notice / invitation shape on paper, margin notes; `must` = a marks-bearing part)

Every spec also takes "title" and optional "subtitle" / "width". Draw only facts already in the note.

Usage:  python svgkit.py specfile.json [--out DIR] [--config study.json]
where specfile.json = {"out-slug": {"kind": "...", "title": "...", ...}, ...}
"""
import json
import os
import sys

OUT_DIR = None   # set in __main__ from --out or the vault config

SURFACE = "#fcfcfb"
BORDER = "#e3e3df"
INK = "#0b0b0b"
INK2 = "#52514e"
INK3 = "#87867d"
GRID = "#ececE8"

SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
          "#e87ba4", "#008300", "#4a3aa7", "#e34948"]

FONT = "'Segoe UI',Inter,system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def wrap(text, width_px, size, bold=False):
    """Greedy wrap using an average glyph-width estimate."""
    per = size * (0.58 if bold else 0.545)
    limit = max(4, int(width_px / per))
    words, lines, cur = str(text).split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= limit or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, size=14, fill=INK, weight="400", anchor="start", ls="0"):
    return ('<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" fill="%s" '
            'font-weight="%s" text-anchor="%s" letter-spacing="%s">%s</text>'
            % (x, y, FONT, size, fill, weight, anchor, ls, esc(s)))


def block(x, y, lines, size, fill, weight="400", anchor="start", lh=1.35):
    out = []
    for i, ln in enumerate(lines):
        out.append(text(x, y + i * size * lh, ln, size, fill, weight, anchor))
    return out


def rect(x, y, w, h, fill="#ffffff", stroke=BORDER, r=10, sw=1, extra=""):
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%d" '
            'fill="%s" stroke="%s" stroke-width="%s" %s/>'
            % (x, y, w, h, r, fill, stroke, sw, extra))


def tint(hexcolor, alpha):
    return '%s" fill-opacity="%s' % (hexcolor, alpha)


def frame(width, height, title, subtitle=None):
    """Returns (opening svg string, content_top_y)."""
    head = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 %d %d" role="img" aria-label="%s">'
            % (width, height, width, height, esc(title)),
            '<rect width="%d" height="%d" rx="14" fill="%s" stroke="%s"/>'
            % (width, height, SURFACE, BORDER)]
    y = 40
    head.append(text(28, y, title, 19, INK, "700"))
    y += 10
    if subtitle:
        for i, ln in enumerate(wrap(subtitle, width - 56, 13)):
            head.append(text(28, y + 14 + i * 17, ln, 13, INK2))
        y += 14 + 17 * len(wrap(subtitle, width - 56, 13))
    return head, y + 22


def arrow_defs():
    """Markers are unreliable across renderers - arrowheads are drawn as polygons."""
    return []


def AR(color):
    return ""


def arrow(x1, y1, x2, y2, color=INK3, sw=2.4, head=7.5):
    """Straight arrow with an explicit polygon head (renderer-independent)."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    p1 = (x2, y2)
    p2 = (bx - head * 0.62 * math.sin(a), by + head * 0.62 * math.cos(a))
    p3 = (bx + head * 0.62 * math.sin(a), by - head * 0.62 * math.cos(a))
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round"/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            % (x1, y1, bx, by, color, sw,
               p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], color))


# ----------------------------------------------------------------- timeline
def r_timeline(spec):
    W = spec.get("width", 880)
    events = spec["events"]
    pad_l, spine = 28, 150
    card_x, card_w = spine + 34, W - (spine + 34) - 28
    rows, h = [], 0
    for ev in events:
        lab = wrap(ev["label"], card_w - 32, 14.5, True)
        note = wrap(ev["note"], card_w - 32, 12.5) if ev.get("note") else []
        ch = 16 + len(lab) * 20 + (6 + len(note) * 17 if note else 0) + 14
        rows.append((ev, lab, note, ch))
        h += ch + 14
    body = []
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + h + 18
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body += arrow_defs()
    body.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" '
                'stroke-width="2"/>' % (spine, y0, spine, y0 + h - 14, GRID))
    y = y0
    for i, (ev, lab, note, ch) in enumerate(rows):
        c = ev.get("color") or SERIES[i % 3]
        cy = y + 20
        body.append(text(spine - 18, cy + 5, ev["date"], 13.5, INK2, "700", "end"))
        body.append('<circle cx="%d" cy="%.1f" r="7" fill="%s" stroke="%s" '
                    'stroke-width="3"/>' % (spine, cy, c, SURFACE))
        body.append(rect(card_x, y, card_w, ch, "#ffffff", BORDER, 10))
        body.append('<rect x="%.1f" y="%.1f" width="4" height="%.1f" rx="2" fill="%s"/>'
                    % (card_x, y, ch, c))
        ty = y + 26
        body += block(card_x + 18, ty, lab, 14.5, INK, "600")
        if note:
            body += block(card_x + 18, ty + len(lab) * 20 + 6, note, 12.5, INK2)
        y += ch + 14
    return head + body + ["</svg>"], W, H


# ------------------------------------------------------------------- stages
def r_stages(spec):
    W = spec.get("width", 880)
    steps = spec["steps"]
    per_row = spec.get("per_row", 3 if len(steps) % 3 == 0 or len(steps) > 4 else len(steps))
    per_row = min(per_row, 4)
    gap, pad = 46, 28
    bw = (W - pad * 2 - gap * (per_row - 1)) / per_row
    rows = [steps[i:i + per_row] for i in range(0, len(steps), per_row)]
    heights = []
    for row in rows:
        hh = 0
        for s in row:
            lab = wrap(s["label"], bw - 28, 15, True)
            sub = wrap(s["sub"], bw - 28, 12.5) if s.get("sub") else []
            hh = max(hh, 22 + len(lab) * 20 + (6 + len(sub) * 17 if sub else 0) + 18)
        heights.append(hh)
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + sum(heights) + 34 * (len(rows) - 1) + 16
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = arrow_defs()
    n = 0
    y = y0
    for ri, row in enumerate(rows):
        bh = heights[ri]
        for ci, s in enumerate(row):
            c = s.get("color") or SERIES[n % len(SERIES)]
            x = pad + ci * (bw + gap)
            body.append(rect(x, y, bw, bh, "#ffffff", c, 12, 1.6))
            body.append('<circle cx="%.1f" cy="%.1f" r="13" fill="%s" stroke="%s" '
                        'stroke-width="2.5"/>' % (x + 22, y, c, SURFACE))
            body.append(text(x + 22, y + 5, str(n + 1), 13, "#ffffff", "700", "middle"))
            lab = wrap(s["label"], bw - 28, 15, True)
            sub = wrap(s["sub"], bw - 28, 12.5) if s.get("sub") else []
            ty = y + 34
            body += block(x + 16, ty, lab, 15, INK, "650")
            if sub:
                body += block(x + 16, ty + len(lab) * 20 + 6, sub, 12.5, INK2)
            if ci < len(row) - 1 and spec.get("arrows", True):
                ax = x + bw + 10
                body.append(arrow(ax, y + bh / 2, ax + gap - 20, y + bh / 2))
            n += 1
        y += bh + 34
    return head + body + ["</svg>"], W, H


# ------------------------------------------------------------------ compare
def r_compare(spec):
    W = spec.get("width", 880)
    cols = spec["columns"]
    pad, gap = 28, 22
    cw = (W - pad * 2 - gap * (len(cols) - 1)) / len(cols)
    maxh = 0
    prepared = []
    for i, col in enumerate(cols):
        t = wrap(col["title"], cw - 34, 15.5, True)
        items = [wrap(it, cw - 46, 13) for it in col["items"]]
        h = 34 + len(t) * 21 + 16 + sum(len(x) * 18 + 12 for x in items) + 10
        prepared.append((col, t, items, h))
        maxh = max(maxh, h)
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + maxh + 16
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    for i, (col, t, items, h) in enumerate(prepared):
        c = col.get("color") or SERIES[i % len(SERIES)]
        x = pad + i * (cw + gap)
        body.append(rect(x, y0, cw, maxh, "#ffffff", BORDER, 12))
        body.append('<rect x="%.1f" y="%.1f" width="4.5" height="%.1f" rx="2.2" fill="%s"/>'
                    % (x, y0, maxh, c))
        ty = y0 + 30
        body += block(x + 18, ty, t, 15.5, INK, "700")
        yy = ty + len(t) * 21 + 6
        body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                    % (x + 18, yy - 12, x + cw - 16, yy - 12, GRID))
        yy += 8
        for lines in items:
            body.append('<circle cx="%.1f" cy="%.1f" r="3.2" fill="%s"/>' % (x + 21, yy - 4, c))
            body += block(x + 32, yy, lines, 13, INK2)
            yy += len(lines) * 18 + 12
    return head + body + ["</svg>"], W, H


# ------------------------------------------------------------------- layers
def r_layers(spec):
    W = spec.get("width", 760)
    levels = spec["levels"]
    pad = 28
    rowsh = []
    shrink0 = spec.get("shrink", 0.10)
    for i, lv in enumerate(levels):
        bw0 = (W - pad * 2) * (1 - shrink0 * i)
        lab = wrap(lv["label"], bw0 - 40, 15.5, True)
        sub = wrap(lv["sub"], bw0 - 40, 12.5) if lv.get("sub") else []
        rowsh.append(20 + len(lab) * 21 + (4 + len(sub) * 17 if sub else 0) + 12)
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + sum(rowsh) + 20 * (len(levels) - 1) + 16
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = arrow_defs()
    n = len(levels)
    y = y0
    for i, lv in enumerate(levels):
        shrink = spec.get("shrink", 0.10)
        bw = (W - pad * 2) * (1 - shrink * i)
        x = (W - bw) / 2
        c = lv.get("color") or SERIES[i % len(SERIES)]
        h = rowsh[i]
        body.append(rect(x, y, bw, h, "#ffffff", c, 11, 1.6))
        body.append('<rect x="%.1f" y="%.1f" width="6" height="%.1f" rx="3" fill="%s"/>'
                    % (x, y, h, c))
        lab = wrap(lv["label"], bw - 40, 15.5, True)
        sub = wrap(lv["sub"], bw - 40, 12.5) if lv.get("sub") else []
        body += block(x + 20, y + 28, lab, 15.5, INK, "650")
        if sub:
            body += block(x + 20, y + 28 + len(lab) * 21 + 4, sub, 12.5, INK2)
        if i < n - 1:
            body.append(arrow(W / 2, y + h + 3, W / 2, y + h + 17, INK3, 2.2, 6))
        y += h + 20
    return head + body + ["</svg>"], W, H


# ------------------------------------------------------------------- matrix
def r_matrix(spec):
    W = spec.get("width", 880)
    cols, rows, cells = spec["cols"], spec["rows"], spec["cells"]
    pad = 28
    rowlab_w = spec.get("rowlab", 150)
    avail = W - pad * 2 - rowlab_w
    weights = spec.get("colw") or [1.0] * len(cols)
    tot = float(sum(weights))
    widths = [avail * w / tot for w in weights]
    xs = []
    acc = pad + rowlab_w
    for w in widths:
        xs.append(acc)
        acc += w

    hsize = 13.0
    def too_wide(sz):
        for c, cl in enumerate(cols):
            for word in (cl.split() or [""]):
                if len(word) * sz * 0.6 > widths[c] - 36:
                    return True
        return False
    while hsize > 10 and too_wide(hsize):
        hsize -= 0.5
    head_lines = max(len(wrap(cl, widths[c] - 36, hsize, True)) for c, cl in enumerate(cols))
    head_h = 18 * head_lines + 16

    rh = []
    for r in range(len(rows)):
        hh = 50
        for c in range(len(cols)):
            cell = cells[r][c]
            lab = wrap(cell.get("label", ""), widths[c] - 34, 13.5, True)
            sub = wrap(cell.get("sub", ""), widths[c] - 34, 12) if cell.get("sub") else []
            hh = max(hh, 20 + len(lab) * 18 + (4 + len(sub) * 16 if sub else 0) + 16)
        rl_lines = len(wrap(rows[r], rowlab_w - 16, 13.5, True)) if rows[r] else 0
        hh = max(hh, 20 + rl_lines * 18 + 12)
        rh.append(hh)

    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + head_h + sum(rh) + 8 * len(rows) + 12
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    for c, cl in enumerate(cols):
        x = xs[c]
        body.append('<rect x="%.1f" y="%.1f" width="10" height="10" rx="3" fill="%s"/>'
                    % (x + 8, y0 + 4, SERIES[c % len(SERIES)]))
        body += block(x + 24, y0 + 14, wrap(cl, widths[c] - 36, hsize, True), hsize, INK, "700")
    y = y0 + head_h
    for r, rl in enumerate(rows):
        body += block(pad + 4, y + 26, wrap(rl, rowlab_w - 16, 13.5, True), 13.5, INK, "700")
        for c in range(len(cols)):
            cell = cells[r][c]
            x, cw = xs[c], widths[c]
            col = SERIES[c % len(SERIES)]
            body.append(rect(x + 4, y, cw - 8, rh[r], "#ffffff", BORDER, 10))
            body.append('<rect x="%.1f" y="%.1f" width="%.1f" height="4" rx="2" fill="%s" '
                        'fill-opacity="0.55"/>' % (x + 4, y, cw - 8, col))
            lab = wrap(cell.get("label", ""), cw - 34, 13.5, True)
            sub = wrap(cell.get("sub", ""), cw - 34, 12) if cell.get("sub") else []
            body += block(x + 17, y + 26, lab, 13.5, INK, "650")
            if sub:
                body += block(x + 17, y + 26 + len(lab) * 18 + 4, sub, 12, INK2)
        y += rh[r] + 8
    return head + body + ["</svg>"], W, H


# --------------------------------------------------------------------- bars
def r_bars(spec):
    W = spec.get("width", 820)
    data = spec["data"]
    pad = 28
    labw = spec.get("labw", 210)
    barmax = W - pad * 2 - labw - 70
    vmax = max([d["value"] for d in data] + [spec.get("target", 0)]) or 1
    rowh = 38
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + rowh * len(data) + 22
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    unit = spec.get("unit", "")
    if spec.get("target"):
        tx = pad + labw + barmax * (spec["target"] / vmax)
        body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                    'stroke-width="1.5" stroke-dasharray="5 4"/>'
                    % (tx, y0 - 6, tx, y0 + rowh * len(data) - 10, INK3))
        body.append(text(tx, y0 - 12, spec.get("target_label", "target"), 11.5, INK3, "600", "middle"))
    for i, d in enumerate(data):
        y = y0 + i * rowh
        c = d.get("color") or spec.get("series_color", SERIES[0])
        body += block(pad, y + 18, wrap(d["label"], labw - 12, 13), 13, INK2)
        bw = max(3, barmax * (d["value"] / vmax))
        body.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" rx="4" fill="%s"/>'
                    % (pad + labw, y + 6, bw, c))
        body.append(text(pad + labw + bw + 10, y + 19,
                         ("%g" % d["value"]) + unit, 12.5, INK, "700"))
    return head + body + ["</svg>"], W, H


# -------------------------------------------------------------------- cycle
def r_cycle(spec):
    import math
    W = spec.get("width", 880)
    nodes = spec["nodes"]
    n = len(nodes)
    bw = spec.get("boxw", 170)
    pad = 28
    rx = (W - pad * 2 - bw) / 2
    ry = spec.get("ry", max(125, rx * 0.56))

    boxes = []
    maxbh = 0
    for nd in nodes:
        lab = wrap(nd["label"], bw - 26, 13.5, True)
        sub = wrap(nd["sub"], bw - 26, 11.5) if nd.get("sub") else []
        bh = 20 + len(lab) * 18 + (4 + len(sub) * 15 if sub else 0) + 14
        boxes.append((lab, sub, bh))
        maxbh = max(maxbh, bh)

    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + ry * 2 + maxbh + 26
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    cx, cy = W / 2.0, y0 + ry + maxbh / 2.0

    def pos(t):
        a = -math.pi / 2 + t * 2 * math.pi / n
        return cx + rx * math.cos(a), cy + ry * math.sin(a)

    for i in range(n):
        sx, sy = pos(i + 0.31)
        mx, my = pos(i + 0.5)
        ex, ey = pos(i + 0.63)
        body.append('<path d="M %.1f %.1f Q %.1f %.1f %.1f %.1f" fill="none" stroke="%s" '
                    'stroke-width="2.2" stroke-linecap="round"/>'
                    % (sx, sy, mx + (mx - cx) * 0.06, my + (my - cy) * 0.06, ex, ey, INK3))
        hx, hy = pos(i + 0.685)
        body.append(arrow(ex, ey, hx, hy, INK3, 0.01, 9))

    for i, nd in enumerate(nodes):
        lab, sub, bh = boxes[i]
        x, y = pos(i)
        c = nd.get("color") or SERIES[i % len(SERIES)]
        bx, by = x - bw / 2, y - bh / 2
        body.append(rect(bx, by, bw, bh, "#ffffff", c, 11, 1.8))
        body += block(bx + bw / 2, by + 24, lab, 13.5, INK, "650", "middle")
        if sub:
            body += block(bx + bw / 2, by + 24 + len(lab) * 18 + 4, sub, 11.5, INK2, "400", "middle")

    if spec.get("centre"):
        cl = wrap(spec["centre"], 200, 14, True)
        body += block(cx, cy - (len(cl) - 1) * 9, cl, 14, INK3, "700", "middle")
    return head + body + ["</svg>"], W, H


# --------------------------------------------------------------------- dots
def r_dots(spec):
    """Dot plot on a non-zero value axis. rows:[{label, values:[...]}], series:[{name,color}]."""
    W = spec.get("width", 820)
    rows, series = spec["rows"], spec["series"]
    lo, hi = spec["domain"]
    ticks = spec.get("ticks", [lo, hi])
    pad, labw = 28, spec.get("labw", 150)
    x0, x1 = pad + labw, W - pad - 40
    rowh = 40
    legend_h = 30 if len(series) > 1 else 0

    def X(v):
        return x0 + (x1 - x0) * (float(v) - lo) / (hi - lo)

    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    H = y0 + legend_h + 26 + rowh * len(rows) + 16
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    if legend_h:
        lx = x0
        for sr in series:
            body.append('<circle cx="%.1f" cy="%.1f" r="6" fill="%s"/>' % (lx + 6, y0 + 6, sr["color"]))
            body.append(text(lx + 18, y0 + 11, sr["name"], 13, INK, "600"))
            lx += 34 + len(sr["name"]) * 7.2
    ya = y0 + legend_h + 14
    for t in ticks:
        body.append(text(X(t), ya, ("%g" % t), 11.5, INK3, "600", "middle"))
        body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1"/>'
                    % (X(t), ya + 8, X(t), ya + 10 + rowh * len(rows), GRID))
    for i, r in enumerate(rows):
        cy = ya + 12 + rowh * i + rowh / 2
        body.append(text(pad, cy + 5, r["label"], 13.5, INK2, "600"))
        vals = [v for v in r["values"] if v is not None]
        if len(vals) > 1:
            body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
                        % (X(min(vals)), cy, X(max(vals)), cy, BORDER))
        order = sorted([(v, k) for k, v in enumerate(r["values"]) if v is not None])
        for rank, (v, k) in enumerate(order):
            c = series[k]["color"]
            body.append('<circle cx="%.1f" cy="%.1f" r="7" fill="%s" stroke="%s" stroke-width="2"/>'
                        % (X(v), cy, c, SURFACE))
            dx, anchor = (-12, "end") if (rank == 0 and len(order) > 1) else (12, "start")
            body.append(text(X(v) + dx, cy + 4.5, "%g" % v, 12.5, INK, "700", anchor))
    return head + body + ["</svg>"], W, H


# --------------------------------------------------------------------- form
def r_form(spec):
    """A page-layout format card: the shape on paper, annotated in the margin.
    lines:[{text, align:left|center|right, style:head|title|body|slot|gap, note?, must?}]
    """
    W = spec.get("width", 880)
    pad = 28
    paper_w = spec.get("paper", 470)
    px = pad + 10
    note_x = px + paper_w + 34
    note_w = W - note_x - pad
    styles = {
        "head":  (15, "700", INK),
        "title": (14.5, "700", INK),
        "body":  (13, "400", INK2),
        "slot":  (13, "600", "#2a78d6"),
        "small": (12, "400", INK3),
    }
    rows = []
    for ln in spec["lines"]:
        st = ln.get("style", "body")
        if st == "gap":
            rows.append((ln, [], 10, []))
            continue
        size = styles[st][0]
        tl = wrap(ln.get("text", ""), paper_w - 44, size, styles[st][1] == "700")
        nl = wrap(ln["note"], note_w - 12, 12) if ln.get("note") else []
        h = max(len(tl) * size * 1.35, len(nl) * 16) + 9
        rows.append((ln, tl, h, nl))
    head, y0 = frame(W, 10, spec["title"], spec.get("subtitle"))
    inner = sum(r[2] for r in rows) + 36
    H = y0 + inner + 20
    head, y0 = frame(W, H, spec["title"], spec.get("subtitle"))
    body = []
    body.append(rect(px, y0, paper_w, inner, "#ffffff", BORDER, 6))
    if spec.get("box"):
        body.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="none" '
                    'stroke="%s" stroke-width="2.2"/>' % (px + 12, y0 + 12, paper_w - 24, inner - 24, INK))
    y = y0 + 22
    for ln, tl, h, nl in rows:
        st = ln.get("style", "body")
        if st == "gap":
            y += h
            continue
        size, weight, fill = styles[st]
        al = ln.get("align", "left")
        if al == "center":
            tx, anchor = px + paper_w / 2, "middle"
        elif al == "right":
            tx, anchor = px + paper_w - 24, "end"
        else:
            tx, anchor = px + 24, "start"
        body += block(tx, y + size, tl, size, fill, weight, anchor)
        if nl:
            must = ln.get("must")
            c = "#e34948" if must else INK3
            ly = y + size * 0.65
            body.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
                        'stroke-width="1.2" stroke-dasharray="3 3"/>'
                        % (px + paper_w + 4, ly, note_x - 6, ly, c))
            body.append('<circle cx="%.1f" cy="%.1f" r="3.5" fill="%s"/>' % (note_x - 6, ly, c))
            body += block(note_x + 4, y + 13, nl, 12, c if must else INK2, "600" if must else "400")
        y += h
    return head + body + ["</svg>"], W, H


RENDER = {"timeline": r_timeline, "stages": r_stages, "compare": r_compare,
          "layers": r_layers, "matrix": r_matrix, "bars": r_bars, "cycle": r_cycle,
          "dots": r_dots, "form": r_form}


def build(specs):
    os.makedirs(OUT_DIR, exist_ok=True)
    for slug, spec in specs.items():
        parts, W, H = RENDER[spec["kind"]](spec)
        path = os.path.join(OUT_DIR, slug + ".svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(parts))
        print("OK  %-46s %dx%d" % (slug + ".svg", W, H))


if __name__ == "__main__":
    import argparse
    import studycfg
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Render SVG diagrams from a JSON spec."))
    ap.add_argument("spec", help='{"out-slug": {"kind": "...", "title": "...", ...}, ...}')
    ap.add_argument("--out", help="output folder (default: `diagrams` from the vault config)")
    a = ap.parse_args()
    OUT_DIR = a.out or studycfg.load(a.config)["diagrams"]
    with open(a.spec, "r", encoding="utf-8") as f:
        build(json.load(f))
