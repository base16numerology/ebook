#!/usr/bin/env python3
"""
Build a full-wrap paperback cover PDF for Amazon KDP.

Layout: back cover + spine + front cover, with 0.125" bleed on all
outside edges.  The front cover uses the existing cover.png.  The spine
and back cover are generated with matching background colour, text, and
book description.

Usage:
    uv run python build_cover_pdf.py
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

# ── Book metadata ──────────────────────────────────────────────────
BOOK_TITLE = "Base 16 Numerology"
BOOK_SUBTITLE = "Decoding Your Life in Hex, from Unix Time to Soul Code"
AUTHOR = "Horace Chan"
SPINE_TITLE = "Base 16 Numerology"
SPINE_AUTHOR = "Horace Chan"

BACK_COVER_TEXT = (
    "What if the universe speaks in hex?\n"
    "\n"
    "Traditional numerology was built for pen and paper. "
    "Base 16 Numerology reimagines the practice for the digital age, "
    "using the same hexadecimal system that powers every screen, file, "
    "and network packet on Earth.\n"
    "\n"
    "Your name becomes UTF-8 bytes. Your birth moment becomes a Unix "
    "timestamp. Both are hashed through LIBRE-256 \u2014 an open, "
    "reproducible algorithm \u2014 and reduced to a single hex digit "
    "between 0 and f. That digit is your archetype.\n"
    "\n"
    "Sixteen archetypes across four realms \u2014 Physical, Emotional, "
    "Mental, and Spiritual \u2014 form your Hex Soul Map: a five-position "
    "portrait of your Life Path, Expression, Soul Urge, Personality, "
    "and Maturity.\n"
    "\n"
    "Written for readers who are mystical enough to enjoy archetypes "
    "and skeptical enough to want the math underneath."
)

# ── Physical specs ─────────────────────────────────────────────────
DPI = 300
TRIM_W_IN = 6.0          # front/back cover width
TRIM_H_IN = 9.0          # cover height
BLEED_IN = 0.125
PAGE_COUNT = 134
PAPER_THICKNESS = 0.002252    # white paper, inches per page

COVER_IMAGE = "src/cover.png"
OUTPUT_PDF = "base16_numerology_cover.pdf"

# ── Colours (sampled from cover.png background) ───────────────────
BG_COLOR = (13, 24, 43)       # dark navy from cover
TEXT_COLOR = (214, 186, 119)   # gold from cover title
TEXT_COLOR_LIGHT = (180, 170, 150)  # lighter for description body

# ── Fonts ──────────────────────────────────────────────────────────
FONT_DIR = r"C:\Windows\Fonts"


def in_to_px(inches):
    """Convert inches to pixels at DPI."""
    return round(inches * DPI)


def load_font(name, size_pt):
    """Load a TrueType font at the given point size (at 300 DPI)."""
    size_px = round(size_pt * DPI / 72)
    path = os.path.join(FONT_DIR, name)
    return ImageFont.truetype(path, size_px)


def get_text_bbox(draw, text, font):
    """Return (width, height) of rendered text."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_wrapped_text(draw, text, font, x, y, max_width, line_spacing=1.4,
                      fill=TEXT_COLOR_LIGHT):
    """Draw word-wrapped text. Returns y position after last line."""
    paragraphs = text.split("\n")
    cur_y = y
    for para in paragraphs:
        if not para.strip():
            cur_y += round(font.size * 0.6)
            continue
        words = para.split()
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            tw, _ = get_text_bbox(draw, test, font)
            if tw > max_width and line:
                draw.text((x, cur_y), line, font=font, fill=fill)
                cur_y += round(font.size * line_spacing)
                line = word
            else:
                line = test
        if line:
            draw.text((x, cur_y), line, font=font, fill=fill)
            cur_y += round(font.size * line_spacing)
    return cur_y


def build_cover():
    # ── Dimensions ────────────────────────────────────────────
    spine_in = PAGE_COUNT * PAPER_THICKNESS
    total_w_in = BLEED_IN + TRIM_W_IN + spine_in + TRIM_W_IN + BLEED_IN
    total_h_in = BLEED_IN + TRIM_H_IN + BLEED_IN

    canvas_w = in_to_px(total_w_in)
    canvas_h = in_to_px(total_h_in)

    bleed_px = in_to_px(BLEED_IN)
    back_w = in_to_px(TRIM_W_IN)
    spine_w = in_to_px(spine_in)
    front_w = in_to_px(TRIM_W_IN)

    print(f"Spine width:   {spine_in:.4f}\" ({spine_w} px)")
    print(f"Full cover:    {total_w_in:.4f}\" x {total_h_in:.4f}\"")
    print(f"Canvas:        {canvas_w} x {canvas_h} px at {DPI} DPI")

    # Key x positions (left edge of each zone)
    back_trim_x = bleed_px
    spine_x = bleed_px + back_w
    front_trim_x = spine_x + spine_w
    front_bleed_end = front_trim_x + front_w + bleed_px

    # Key y positions
    top_trim_y = bleed_px
    bottom_trim_y = bleed_px + in_to_px(TRIM_H_IN)

    # Safe margins (0.375" from trim for text on front/back)
    safe_margin = in_to_px(0.375)
    # Spine safe margin (0.0625" from spine edge)
    spine_safe = in_to_px(0.0625)

    # ── Create canvas ─────────────────────────────────────────
    img = Image.new("RGB", (canvas_w, canvas_h), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # ── Place front cover image ───────────────────────────────
    # The front cover area (with bleed) goes from front_trim_x - 0
    # (the spine edge has no bleed) to the right bleed edge, and
    # from top bleed to bottom bleed.
    front_cover_img = Image.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), COVER_IMAGE)
    )
    # Scale to fill the front cover area including right+top+bottom bleed
    front_area_w = front_w + bleed_px   # right bleed only (spine side has no bleed)
    front_area_h = canvas_h             # full height with bleed top+bottom
    front_cover_resized = front_cover_img.resize(
        (front_area_w, front_area_h), Image.LANCZOS
    )
    img.paste(front_cover_resized, (front_trim_x, 0))

    # ── Back cover ────────────────────────────────────────────
    # Background already filled.  Add text in the safe area.
    back_safe_left = back_trim_x + safe_margin
    back_safe_right = spine_x - safe_margin
    back_text_width = back_safe_right - back_safe_left
    back_safe_top = top_trim_y + safe_margin

    # Barcode zone: KDP places barcode in lower-right of back cover.
    # Reserve roughly 2" wide x 1.2" tall in the lower-right area.
    barcode_w = in_to_px(2.0)
    barcode_h = in_to_px(1.2)
    barcode_margin = in_to_px(0.25)

    # Back cover title (book title)
    font_back_title = load_font("georgiab.ttf", 22)
    draw.text(
        (back_safe_left, back_safe_top),
        BOOK_TITLE,
        font=font_back_title,
        fill=TEXT_COLOR,
    )
    title_w, title_h = get_text_bbox(draw, BOOK_TITLE, font_back_title)

    # Back cover subtitle
    font_back_subtitle = load_font("georgiai.ttf", 13)
    subtitle_y = back_safe_top + title_h + in_to_px(0.15)
    draw.text(
        (back_safe_left, subtitle_y),
        BOOK_SUBTITLE,
        font=font_back_subtitle,
        fill=TEXT_COLOR,
    )
    _, sub_h = get_text_bbox(draw, BOOK_SUBTITLE, font_back_subtitle)

    # Horizontal rule
    rule_y = subtitle_y + sub_h + in_to_px(0.25)
    rule_left = back_safe_left
    rule_right = back_safe_left + in_to_px(1.5)
    draw.line(
        [(rule_left, rule_y), (rule_right, rule_y)],
        fill=TEXT_COLOR,
        width=2,
    )

    # Back cover description text
    font_back_body = load_font("georgia.ttf", 10)
    body_y = rule_y + in_to_px(0.25)
    max_body_y = bottom_trim_y - safe_margin - barcode_h - barcode_margin
    draw_wrapped_text(
        draw, BACK_COVER_TEXT, font_back_body,
        back_safe_left, body_y,
        back_text_width,
        line_spacing=1.45,
        fill=TEXT_COLOR_LIGHT,
    )

    # ── Spine ─────────────────────────────────────────────────
    # Spine text runs bottom-to-top (standard for English books).
    # We draw on a temporary image and rotate.
    spine_safe_left = spine_x + spine_safe
    spine_safe_right = spine_x + spine_w - spine_safe
    usable_spine_w = spine_safe_right - spine_safe_left

    # Spine height (text runs along this length)
    spine_text_h = in_to_px(TRIM_H_IN) - 2 * safe_margin

    # Create a horizontal strip: width=spine_text_h, height=usable_spine_w
    # Then rotate 90° CW and paste
    spine_strip = Image.new("RGB", (spine_text_h, usable_spine_w), BG_COLOR)
    spine_draw = ImageDraw.Draw(spine_strip)

    # Find a font size that fits the spine width
    spine_font_size = 8
    for sz in range(12, 5, -1):
        test_font = load_font("georgiab.ttf", sz)
        _, th = get_text_bbox(spine_draw, SPINE_TITLE, test_font)
        if th <= usable_spine_w - 4:
            spine_font_size = sz
            break

    spine_font = load_font("georgiab.ttf", spine_font_size)
    spine_author_font = load_font("georgia.ttf", spine_font_size)

    # Title on the left (which becomes bottom after rotation)
    tw, th = get_text_bbox(spine_draw, SPINE_TITLE, spine_font)
    text_y = (usable_spine_w - th) // 2
    spine_draw.text((in_to_px(0.3), text_y), SPINE_TITLE,
                    font=spine_font, fill=TEXT_COLOR)

    # Author on the right (which becomes top after rotation)
    aw, ah = get_text_bbox(spine_draw, SPINE_AUTHOR, spine_author_font)
    author_x = spine_text_h - aw - in_to_px(0.3)
    spine_draw.text((author_x, text_y), SPINE_AUTHOR,
                    font=spine_author_font, fill=TEXT_COLOR)

    # Rotate 90° clockwise: bottom-to-top reading direction
    spine_rotated = spine_strip.rotate(-90, expand=True)

    # Paste onto canvas
    paste_x = spine_safe_left
    paste_y = top_trim_y + safe_margin
    img.paste(spine_rotated, (paste_x, paste_y))

    # ── Save as PDF ───────────────────────────────────────────
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, OUTPUT_PDF)

    img.save(output_path, "PDF", resolution=DPI)

    # Also save a low-res PNG preview for quick inspection
    preview_path = output_path.replace(".pdf", "_preview.png")
    preview = img.copy()
    preview.thumbnail((1600, 1200), Image.LANCZOS)
    preview.save(preview_path)
    print(f"Preview PNG:  {preview_path}")

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"Cover PDF written to {output_path} ({file_size:.1f} MB)")
    print()
    print("Layout summary:")
    print(f"  Trim size:    {TRIM_W_IN}\" x {TRIM_H_IN}\"")
    print(f"  Bleed:        {BLEED_IN}\"")
    print(f"  Spine:        {spine_in:.4f}\" ({PAGE_COUNT} pages, white paper)")
    print(f"  Full cover:   {total_w_in:.4f}\" x {total_h_in}\"")
    print(f"  Resolution:   {DPI} DPI")
    print(f"  Pages > 79:   spine text included")
    print()
    print("  [BACK COVER] [SPINE] [FRONT COVER]")
    print("  ←── 6\" ────→ ←0.3\"→ ←── 6\" ────→")
    print()
    print("Note: KDP will auto-place a barcode on the back cover.")
    print("Upload this file as your cover PDF when publishing.")


if __name__ == "__main__":
    build_cover()
