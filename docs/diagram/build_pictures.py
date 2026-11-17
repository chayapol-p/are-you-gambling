#!/usr/bin/env python3
"""
Build the README pictures for Are You Gambling? in the "two scoreboards" style, light and dark.

The style: a stock price board and a roulette history board, side by side, each showing the past.
The repeating mark is a row of past spins beside the project name, top left on every picture.

  Input:  nothing; every picture is drawn from the data in this file
  Output: <output folder>/<picture>.html and <picture>-dark.html, one <svg> per page
          (export each page to PNG with the readme-kit export_png.py script)

Run: python3 docs/diagram/build_pictures.py docs/diagram
Fonts: Inter and JetBrains Mono, bundled in docs/diagram/fonts/ with their SIL Open Font License texts.
"""

import sys
from pathlib import Path

# Constants
## The project and the canvas
PROJECT_NAME = "ARE YOU GAMBLING?"
CANVAS_WIDTH = 960                     # every picture shares this width; it exports to 1920 pixels

## Colours by role, light and dark. Drawing functions use these names, never colour codes.
LIGHT_PALETTE = {
    "ground": "#f6f5f1", "board": "#ffffff",
    "ink": "#1b1f24", "soft": "#5f6670", "faint": "#c9ccd1",
    "accent": "#c62828", "on_accent": "#ffffff",
}
DARK_PALETTE = {
    "ground": "#0d1117", "board": "#161b22",
    "ink": "#e6edf3", "soft": "#9aa4ae", "faint": "#3a424c",
    "accent": "#ff5a52", "on_accent": "#0d1117",
}

## Fonts: a plain face for quotes and names, a mono face for board labels
QUOTE_FONT = "'Inter', Helvetica, Arial, sans-serif"
LABEL_FONT = "'JetBrains Mono', Menlo, monospace"
FONT_FACES = [  # family, weight, file
    ("Inter", 400, "fonts/inter-latin-400-normal.woff2"),
    ("Inter", 700, "fonts/inter-latin-700-normal.woff2"),
    ("JetBrains Mono", 400, "fonts/jetbrains-mono-latin-400-normal.woff2"),
    ("JetBrains Mono", 700, "fonts/jetbrains-mono-latin-700-normal.woff2"),
]

## Words for the mirror picture, taken word for word from a real test run of the skill
YOUR_LINE = "“It's down 30%. It'll bounce back now.”"
UNCLE_LINE = "“Black is due! Five reds in a row.”"
CLOSING_LINE = "Both bet that the past has to turn around."


# ---- Text helpers ----

# Write a quote or a name in the plain face.
def quote_text(colors, x, y, words, size=18, color_role="ink", anchor="middle", bold=False):
    weight = 700 if bold else 400
    return (f'<text x="{x}" y="{y}" fill="{colors[color_role]}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{QUOTE_FONT}" text-anchor="{anchor}">{words}</text>')


# Write a small board label in the mono face.
def label_text(colors, x, y, words, size=12, color_role="soft", anchor="start", bold=False):
    weight = 700 if bold else 400
    return (f'<text x="{x}" y="{y}" fill="{colors[color_role]}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{LABEL_FONT}" text-anchor="{anchor}" letter-spacing="0.12em">{words}</text>')


# ---- Shape helpers ----

# Draw one scoreboard: an opaque board with a rounded border and a label across the top.
def scoreboard(colors, x, y, width, height, label):
    return (f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="12" fill="{colors["board"]}" '
            f'stroke="{colors["ink"]}" stroke-width="2"/>'
            + label_text(colors, x + 22, y + 34, label))


# Draw one past spin: a filled chip with a letter, so the meaning never rests on colour alone.
def spin_chip(colors, center_x, center_y, radius, letter):
    return (f'<circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="{colors["accent"]}"/>'
            f'<text x="{center_x}" y="{center_y + radius * 0.3}" fill="{colors["on_accent"]}" font-size="{radius * 0.8}" '
            f'font-weight="700" font-family="{QUOTE_FONT}" text-anchor="middle">{letter}</text>')


# Draw the spin the gambler expects next: a dashed empty chip with its letter and a question mark.
def expected_chip(colors, center_x, center_y, radius, letter):
    return (f'<circle cx="{center_x}" cy="{center_y}" r="{radius}" fill="none" stroke="{colors["soft"]}" '
            f'stroke-width="2" stroke-dasharray="5 4"/>'
            f'<text x="{center_x}" y="{center_y + radius * 0.3}" fill="{colors["soft"]}" font-size="{radius * 0.7}" '
            f'font-weight="700" font-family="{QUOTE_FONT}" text-anchor="middle">{letter}?</text>')


# ---- The repeating mark ----

# Draw the project name with a row of five past spins beside it, top left on every picture.
def repeating_mark(colors):
    parts = [label_text(colors, 40, 40, PROJECT_NAME, size=13, color_role="ink", bold=True)]
    first_dot_x = 40 + len(PROJECT_NAME) * 13 * 0.72 + 14     # mono width, plus a gap after the name
    for i in range(5):
        parts.append(f'<circle cx="{first_dot_x + i * 14}" cy="35" r="5" fill="{colors["accent"]}"/>')
    return "".join(parts)


# ---- Picture: the mirror ----

MIRROR_HEIGHT = 440
BOARD_TOP, BOARD_WIDTH, BOARD_HEIGHT = 70, 390, 230
LEFT_BOARD_X, RIGHT_BOARD_X = 40, 530


# Draw the left board: a price line falling 30%, then a dashed line for the bounce the buyer expects.
def price_board(colors):
    parts = [scoreboard(colors, LEFT_BOARD_X, BOARD_TOP, BOARD_WIDTH, BOARD_HEIGHT, "YOUR STOCK")]
    # The change is set in the plain face, because mono letter spacing splits the minus sign from the number
    parts.append(quote_text(colors, LEFT_BOARD_X + BOARD_WIDTH - 22, BOARD_TOP + 38, "−30%", size=24,
                            color_role="accent", anchor="end", bold=True))

    # The real fall, drawn solid
    fall_points = [(70, 140), (125, 152), (180, 178), (235, 172), (290, 210), (330, 238)]
    fall_path = "M " + " L ".join(f"{x},{y}" for x, y in fall_points)
    parts.append(f'<path d="{fall_path}" fill="none" stroke="{colors["accent"]}" stroke-width="4" '
                 f'stroke-linejoin="round" stroke-linecap="round"/>')

    # The bounce the buyer expects, drawn dashed, ending in a question mark
    parts.append(f'<path d="M 330,238 L 380,170" fill="none" stroke="{colors["soft"]}" stroke-width="2.5" '
                 f'stroke-dasharray="6 5" stroke-linecap="round"/>')
    parts.append(quote_text(colors, 396, 166, "?", size=22, color_role="soft", bold=True))
    return "".join(parts)


# Draw the right board: five reds in a row, then a dashed chip for the black the uncle expects.
def roulette_board(colors):
    parts = [scoreboard(colors, RIGHT_BOARD_X, BOARD_TOP, BOARD_WIDTH, BOARD_HEIGHT, "UNCLE'S TABLE · LAST 5")]
    chip_y, chip_radius, chip_gap = 195, 24, 58
    first_chip_x = RIGHT_BOARD_X + 52
    for i in range(5):
        parts.append(spin_chip(colors, first_chip_x + i * chip_gap, chip_y, chip_radius, "R"))
    parts.append(expected_chip(colors, first_chip_x + 5 * chip_gap, chip_y, chip_radius, "B"))
    return "".join(parts)


# Draw the mirror picture: both boards, an equals sign between them, the two lines and the closing line.
def mirror_svg(colors, slug):
    parts = [f'<rect width="{CANVAS_WIDTH}" height="{MIRROR_HEIGHT}" fill="{colors["ground"]}"/>',
             repeating_mark(colors),
             price_board(colors),
             roulette_board(colors)]

    # The equals sign sits in the gap between the boards, level with their middles
    gap_center_x = (LEFT_BOARD_X + BOARD_WIDTH + RIGHT_BOARD_X) // 2
    parts.append(quote_text(colors, gap_center_x, BOARD_TOP + BOARD_HEIGHT // 2 + 14, "=", size=44, bold=True))

    # Each line under its own board
    parts.append(quote_text(colors, LEFT_BOARD_X + BOARD_WIDTH // 2, 344, YOUR_LINE, size=19))
    parts.append(quote_text(colors, RIGHT_BOARD_X + BOARD_WIDTH // 2, 344, UNCLE_LINE, size=19,
                            color_role="accent", bold=True))

    # The closing line, below a faint rule
    parts.append(f'<line x1="40" y1="378" x2="{CANVAS_WIDTH - 40}" y2="378" stroke="{colors["faint"]}" stroke-width="1"/>')
    parts.append(label_text(colors, CANVAS_WIDTH // 2, 410, CLOSING_LINE.upper(), size=12, anchor="middle"))

    description = ("Two scoreboards side by side. Left: your stock, down 30 percent, with a dashed line for the "
                   "bounce you expect. Right: the uncle's roulette table, five reds in a row, with a dashed chip "
                   "for the black he expects. Under them: It's down 30%, it'll bounce back now. "
                   "Black is due, five reds in a row.")
    return wrap_svg(slug, MIRROR_HEIGHT, "Your reason beside the uncle's", description, "".join(parts))


# ---- Page wrapper ----

# Wrap drawn parts in an accessible <svg> with a title and a description.
def wrap_svg(slug, height, title, description, body):
    return (f'<svg viewBox="0 0 {CANVAS_WIDTH} {height}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-labelledby="{slug}-title {slug}-desc">'
            f'<title id="{slug}-title">{title}</title><desc id="{slug}-desc">{description}</desc>{body}</svg>')


# Put one picture on its own page, loading the bundled fonts by relative path.
def picture_page(colors, heading, svg):
    font_rules = "".join(
        f"@font-face {{ font-family: '{family}'; font-weight: {weight}; src: url('{path}') format('woff2'); }}\n    "
        for family, weight, path in FONT_FACES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{heading} · Are You Gambling?</title>
  <style>
    {font_rules}body {{ margin: 0; padding: 2rem; background: {colors["ground"]}; }}
    svg {{ width: 100%; display: block; }}
  </style>
</head>
<body>
{svg}
</body>
</html>
"""


# ---- Write every picture, light and dark ----

PICTURES = [  # file name, page heading, drawing function
    ("mirror", "Your reason beside the uncle's", mirror_svg),
]


# Write a light and a dark page for every picture into the output folder.
def write_all_pictures(output_folder: Path) -> None:
    output_folder.mkdir(parents=True, exist_ok=True)
    for suffix, colors in (("", LIGHT_PALETTE), ("-dark", DARK_PALETTE)):
        for file_name, heading, draw_picture in PICTURES:
            slug = f"{file_name}{suffix}"
            page_file = output_folder / f"{slug}.html"
            page_file.write_text(picture_page(colors, heading, draw_picture(colors, slug)), encoding="utf-8")
            print(f"build_pictures: wrote {page_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("build_pictures: usage: build_pictures.py <output folder>")
    write_all_pictures(Path(sys.argv[1]))
