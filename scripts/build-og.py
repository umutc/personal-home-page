#!/usr/bin/env python3
"""
Generate the OpenGraph preview images (1200x630) for umutcelik.com.tr.

Pillow is the only dependency. Run once when content changes:

    python3 scripts/build-og.py

Output: og.png at repo root (homepage card) and one og.png per blog post
listed in POSTS, next to that post's index.html.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og.png"
AVATAR = ROOT / "umut-celik.jpg"

W, H = 1200, 630
BG = (10, 10, 10)
TEXT = (237, 237, 237)
MUTED = (148, 163, 184)
ACCENT = (122, 167, 255)
CHIP_BG = (23, 33, 47)

NAME = "Umut Celik"
ROLE = "Senior Software Engineer"
TAGLINE = "AI agents · web scraping at scale · AWS"
CHIPS = ["Node.js", "TypeScript", "AWS", "MongoDB", "MCP"]
DOMAIN = "umutcelik.com.tr"

FONT_PATHS = [
    "/System/Library/Fonts/HelveticaNeue.ttc",
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]


def load_font(size, bold=False):
    for path in FONT_PATHS:
        try:
            font = ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
            return font
        except (OSError, ValueError):
            continue
    return ImageFont.load_default()


def text_width(draw, text, font):
    left, _, right, _ = draw.textbbox((0, 0), text, font=font)
    return right - left


# Variant colors from the blog charts (dark palette), in the same order.
SURFACES = [
    ("Claude in Chrome", (57, 135, 229)),
    ("Playwright · Chrome", (217, 89, 38)),
    ("Orca browser", (25, 158, 112)),
    ("Safari MCP", (201, 133, 0)),
    ("Playwright · WebKit", (213, 81, 129)),
]

POSTS = [
    {
        "out": ROOT / "blog" / "five-ways-to-drive-a-browser" / "og.png",
        "title": "Five ways to drive a browser",
        "subtitle": "The same Claude Code agent through five browser automation surfaces.",
        "footer": "670 runs · every transcript published",
    },
]


def wrap(draw, text, font, max_width):
    lines, line = [], ""
    for word in text.split():
        candidate = f"{line} {word}".strip()
        if line and text_width(draw, candidate, font) > max_width:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def build_post_card(post):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (6, H)], fill=ACCENT)

    x, max_w = 80, W - 160
    font_title = load_font(70, bold=True)
    font_sub = load_font(32)
    font_label = load_font(24)
    font_small = load_font(22)

    y = 78
    for line in wrap(draw, post["title"], font_title, max_w):
        draw.text((x, y), line, font=font_title, fill=TEXT)
        y += 84
    y += 22
    for line in wrap(draw, post["subtitle"], font_sub, max_w):
        draw.text((x, y), line, font=font_sub, fill=MUTED)
        y += 44

    row_y = 410
    sx = x
    for name, color in SURFACES:
        draw.rounded_rectangle([(sx, row_y + 4), (sx + 20, row_y + 24)], radius=3, fill=color)
        draw.text((sx + 30, row_y), name, font=font_label, fill=TEXT)
        sx += 30 + text_width(draw, name, font_label) + 34
        if sx > W - 260:
            sx, row_y = x, row_y + 44

    draw.text((x, H - 70), f"{NAME} · {post['footer']}", font=font_small, fill=MUTED)
    domain = f"{DOMAIN}/blog"
    draw.text((W - text_width(draw, domain, font_small) - 80, H - 70), domain, font=font_small, fill=MUTED)

    img.save(post["out"], "PNG", optimize=True)
    print(f"Wrote {post['out']} ({post['out'].stat().st_size / 1024:.1f} KB)")


def main():
    build_home_card()
    for post in POSTS:
        build_post_card(post)


def build_home_card():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    accent_w = 6
    draw.rectangle([(0, 0), (accent_w, H)], fill=ACCENT)

    avatar_size = 140
    avatar_x, avatar_y = 80, 80
    if AVATAR.exists():
        avatar = Image.open(AVATAR).convert("RGB").resize(
            (avatar_size, avatar_size), Image.LANCZOS
        )
        mask = Image.new("L", (avatar_size, avatar_size), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.ellipse((0, 0, avatar_size, avatar_size), fill=255)
        img.paste(avatar, (avatar_x, avatar_y), mask)

    text_x = avatar_x + avatar_size + 36

    font_name = load_font(84, bold=True)
    font_role = load_font(38)
    font_tag = load_font(30)
    font_chip = load_font(22, bold=True)
    font_domain = load_font(22)

    name_y = avatar_y + 6
    draw.text((text_x, name_y), NAME, font=font_name, fill=TEXT)

    role_y = name_y + 100
    draw.text((text_x, role_y), ROLE, font=font_role, fill=TEXT)

    tagline_y = role_y + 54
    draw.text((text_x, tagline_y), TAGLINE, font=font_tag, fill=MUTED)

    chip_y = 430
    chip_x = avatar_x
    chip_pad_x, chip_pad_y = 18, 10
    chip_gap = 14
    for label in CHIPS:
        tw = text_width(draw, label, font_chip)
        chip_w = tw + chip_pad_x * 2
        chip_h = font_chip.size + chip_pad_y * 2
        draw.rounded_rectangle(
            [(chip_x, chip_y), (chip_x + chip_w, chip_y + chip_h)],
            radius=chip_h // 2,
            fill=CHIP_BG,
        )
        draw.text(
            (chip_x + chip_pad_x, chip_y + chip_pad_y - 2),
            label,
            font=font_chip,
            fill=MUTED,
        )
        chip_x += chip_w + chip_gap

    dw = text_width(draw, DOMAIN, font_domain)
    draw.text((W - dw - 80, H - 70), DOMAIN, font=font_domain, fill=MUTED)

    img.save(OUT, "PNG", optimize=True)
    size_kb = OUT.stat().st_size / 1024
    print(f"Wrote {OUT} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
