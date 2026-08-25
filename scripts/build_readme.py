#!/usr/bin/env python3
"""Build a GitHub README as a text RPG status screen (no SVG)."""

from pathlib import Path

INNER = 74


def bar(value: int, width: int = 20) -> str:
    filled = max(0, min(width, round(width * value / 100)))
    return "█" * filled + "░" * (width - filled)


def row(text: str = "") -> str:
    return "║ " + text.ljust(INNER) + " ║"


def rule(left="╠", mid="═", right="╣") -> str:
    return left + mid * (INNER + 2) + right


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

# two-column body: left 36, divider, right 35  -> 36+1+35 = 72, plus side spaces in row()
# row() already has "║ " + 74 + " ║". Split 74 into 36 | 1 | 37
L, R = 36, 37


def split_row(left: str, right: str) -> str:
    return "║ " + left.ljust(L) + "│" + right.ljust(R) + " ║"


lines = [
    "╔" + "═" * (INNER + 2) + "╗",
    row("STATUS".ljust(INNER)),
    rule(),
    row(f"{'NAME':<6} borico" + f"{'LV':>40}  24"),
    row(f"{'JOB':<6} CLOUD OPS ENGINEER" + f"{'ID':>28}  tagmach11"),
    row(),
    row(f"HP     {bar(100)}  128/128"),
    row(f"MP     {bar(90)}   90/100"),
    row(f"EXP    {bar(64)}  NEXT 640"),
    "╠" + "═" * (L + 1) + "╤" + "═" * (R + 1) + "╣",
    split_row(" ABILITY", " SKILL"),
    split_row("─" * L, "─" * R),
]

left_block: list[str] = []
for stat, val, name in abilities:
    left_block.append(f" {stat}  {val:>3}  {name:<14} {bar(val, 10)}")

left_block += [
    "",
    " EQUIP",
    " WPN  Maven / Gradle",
    " ARM  Nginx",
    " ACC  Terraform",
]

right_block = [f" {name:<10} {bar(val, 12)} {val:>3}" for name, val in skills]

height = max(len(left_block), len(right_block))
left_block += [""] * (height - len(left_block))
right_block += [""] * (height - len(right_block))

for left, right in zip(left_block, right_block):
    lines.append(split_row(left[:L], right[:R]))

lines += [
    "╠" + "═" * (L + 1) + "╧" + "═" * (R + 1) + "╣",
    row("COMMAND"),
    row(),
    row("  ▶  TROUBLEOPS          PARTNEROPS          RECIPEBOOK"),
    row("     Java / Spring        ACE / CRM            Dart / TS"),
    "╚" + "═" * (INNER + 2) + "╝",
]

screen = "\n".join(lines)

# verify widths
for i, line in enumerate(screen.splitlines(), 1):
    if len(line) != INNER + 4:
        raise SystemExit(f"line {i} width {len(line)} != {INNER + 4}: {line!r}")

readme = f"""<div align="center">

```
{screen}
```

<p>
  <a href="https://github.com/tagmach11/TroubleOps">TroubleOps</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/tagmach11/AWS_Billing_Automation">PartnerOps</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/tagmach11/Recipebook">RecipeBook</a>
</p>

</div>
"""

Path(__file__).resolve().parents[1].joinpath("README.md").write_text(readme)
print("README.md written")
for line in screen.splitlines():
    print(line)
