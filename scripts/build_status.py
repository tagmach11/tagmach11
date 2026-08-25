#!/usr/bin/env python3
"""Build an RPG-style status screen SVG for the GitHub profile README."""

from pathlib import Path

W, H = 888, 640
GOLD = "#E8D48B"
GOLD_DIM = "#8A7030"
INK = "#F3EAD3"
DIM = "#8B9BB4"
CYAN = "#7EC8E3"
HP = "#3DDC84"
MP = "#5B9DFF"
EXP = "#E0B84A"
BAR_BG = "#070B14"
FILL = "#121C31"
BG = "#070B14"
SLOT = "#0C1424"


def panel(x, y, w, h, title=None):
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{FILL}" stroke="{GOLD}" stroke-width="3"/>',
        f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{h - 12}" rx="1" fill="none" stroke="{GOLD_DIM}" stroke-width="1.5"/>',
    ]
    if title:
        tw = 22 + len(title) * 11
        parts.append(
            f'<rect x="{x + 20}" y="{y - 11}" width="{tw}" height="22" fill="{FILL}" stroke="{GOLD}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{x + 20 + tw / 2}" y="{y + 5}" text-anchor="middle" class="title">{title}</text>'
        )
    return "\n  ".join(parts)


def seg_bar(x, y, value, segments=20, seg_w=8, gap=2, h=12, color=GOLD):
    filled = round(segments * value / 100)
    total_w = segments * (seg_w + gap) - gap
    parts = [
        f'<rect x="{x - 3}" y="{y - 3}" width="{total_w + 6}" height="{h + 6}" fill="{BAR_BG}" stroke="#1C2740" stroke-width="1"/>'
    ]
    for i in range(segments):
        sx = x + i * (seg_w + gap)
        c = color if i < filled else "#1C2740"
        parts.append(f'<rect x="{sx}" y="{y}" width="{seg_w}" height="{h}" fill="{c}"/>')
    return "\n  ".join(parts)


abilities = [
    ("STR", 90, "Java"),
    ("MAG", 88, "Spring Boot"),
    ("INT", 85, "AWS"),
    ("DEX", 80, "React / TS"),
    ("DEF", 84, "Docker / Linux"),
    ("VIT", 82, "MySQL"),
]

skills = [
    ("JAVA", 90),
    ("SPRING", 88),
    ("AWS", 85),
    ("LINUX", 84),
    ("DOCKER", 82),
    ("MYSQL", 82),
    ("REACT", 80),
    ("TS", 80),
    ("GIT", 84),
    ("MAVEN", 78),
    ("GRADLE", 76),
    ("NGINX", 72),
    ("HTML/CSS", 75),
    ("VITE", 70),
    ("TERRAFORM", 62),
    ("FLUTTER", 55),
]

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Player status screen">
  <style>
    .ui {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }}
    .title {{ fill: {GOLD}; font-size: 12px; font-weight: 700; letter-spacing: 2px; }}
    .label {{ fill: {DIM}; font-size: 12px; letter-spacing: 2px; }}
    .value {{ fill: {INK}; font-size: 13px; letter-spacing: 0.4px; }}
    .name {{ fill: {INK}; font-size: 26px; font-weight: 700; letter-spacing: 2px; }}
    .job {{ fill: {CYAN}; font-size: 13px; letter-spacing: 2px; }}
    .num {{ fill: {GOLD}; font-size: 20px; font-weight: 700; }}
    .small {{ fill: {GOLD}; font-size: 12px; font-weight: 700; }}
    .hint {{ fill: {DIM}; font-size: 11px; letter-spacing: 1px; }}
    .cmd {{ fill: {INK}; font-size: 15px; letter-spacing: 2px; }}
    .cmd-on {{ fill: {GOLD}; font-size: 15px; font-weight: 700; letter-spacing: 2px; }}
    .slot {{ fill: {INK}; font-size: 11px; letter-spacing: 0.5px; }}
    .slot-n {{ fill: {GOLD}; font-size: 11px; font-weight: 700; }}
  </style>

  <rect width="{W}" height="{H}" fill="{BG}"/>
  <rect x="8" y="8" width="{W - 16}" height="{H - 16}" fill="none" stroke="#1C2740" stroke-width="2"/>

  {panel(24, 28, 840, 150, "STATUS")}
  <text x="52" y="72" class="ui label">NAME</text>
  <text x="122" y="74" class="ui name">borico</text>
  <text x="52" y="104" class="ui job">CLOUD OPS ENGINEER</text>
  <text x="52" y="130" class="ui hint">incident trainer  /  partner automation</text>

  <text x="430" y="64" class="ui label">LV</text>
  <text x="478" y="66" class="ui num">24</text>
  <text x="560" y="64" class="ui label">ID</text>
  <text x="600" y="64" class="ui value">tagmach11</text>

  <text x="430" y="98" class="ui label">HP</text>
  {seg_bar(470, 86, 100, segments=24, color=HP)}
  <text x="730" y="98" class="ui small">128/128</text>

  <text x="430" y="126" class="ui label">MP</text>
  {seg_bar(470, 114, 90, segments=24, color=MP)}
  <text x="730" y="126" class="ui small">90/100</text>

  <text x="430" y="154" class="ui label">EXP</text>
  {seg_bar(470, 142, 64, segments=24, color=EXP)}
  <text x="730" y="154" class="ui small">NEXT 640</text>

  {panel(24, 196, 360, 316, "ABILITY")}
'''

ay = 236
for stat, val, skill in abilities:
    svg += f'''  <text x="52" y="{ay + 14}" class="ui label">{stat}</text>
  <text x="108" y="{ay + 16}" class="ui num">{val}</text>
  <text x="168" y="{ay + 14}" class="ui value">{skill}</text>
  {seg_bar(52, ay + 24, val, segments=28, seg_w=8, gap=2, h=8, color=GOLD)}
'''
    ay += 46

svg += f'''
  {panel(404, 196, 460, 316, "SKILL")}
'''

# 4x4 inventory slots
slot_w, slot_h = 102, 64
ox, oy = 424, 224
for i, (name, val) in enumerate(skills):
    col, row = i % 4, i // 4
    x = ox + col * (slot_w + 8)
    y = oy + row * (slot_h + 8)
    svg += f'''  <rect x="{x}" y="{y}" width="{slot_w}" height="{slot_h}" fill="{SLOT}" stroke="#2A3A58" stroke-width="1.5"/>
  <text x="{x + 10}" y="{y + 28}" class="ui slot">{name}</text>
  <text x="{x + 10}" y="{y + 48}" class="ui slot-n">{val}</text>
  {seg_bar(x + 42, y + 38, val, segments=6, seg_w=6, gap=1, h=8, color=GOLD)}
'''

svg += f'''
  {panel(24, 530, 840, 86, "COMMAND")}
  <polygon points="52,576 64,570 64,582" fill="{GOLD}"/>
  <text x="76" y="580" class="ui cmd-on">TROUBLEOPS</text>
  <text x="76" y="598" class="ui hint">Java / Spring incident lab</text>
  <text x="310" y="580" class="ui cmd">PARTNEROPS</text>
  <text x="310" y="598" class="ui hint">ACE / CRM automation</text>
  <text x="540" y="580" class="ui cmd">RECIPEBOOK</text>
  <text x="540" y="598" class="ui hint">Dart / TypeScript</text>
  <text x="760" y="580" class="ui hint">Z : SEL</text>
</svg>
'''

out = Path(__file__).resolve().parents[1] / "status.svg"
out.write_text(svg)
print(f"wrote {out}")
