#!/usr/bin/env python3
"""
Build a print-ready PDF for Amazon KDP paperback (6 x 9 in trim).

Reads the same Markdown sources as build_epub.py, converts to a single
HTML file with print CSS, then renders to PDF via Edge headless.

Usage:
    uv run python build_pdf.py
"""

import os
import re
import html as html_mod
import subprocess
import tempfile

import markdown
from latex2mathml.converter import convert as latex_to_mathml

# ── Book metadata ──────────────────────────────────────────────────
BOOK_TITLE = "Base 16 Numerology"
BOOK_SUBTITLE = "Decoding Your Life in Hex, from Unix Time to Soul Code"
AUTHOR = "Horace Chan"
COPYRIGHT_YEAR = "2025"

OUTPUT_PDF = "base16_numerology_paperback.pdf"
OUTPUT_HTML = "base16_numerology_paperback.html"

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# ── KDP trim: 6 x 9 in ───────────────────────────────────────────
# Margins: inside (gutter) 0.75in, outside 0.625in, top/bottom 0.75in.
# Chromium --print-to-pdf does not support @page :left/:right, so we
# use symmetric margins with the larger (gutter-safe) value on both
# sides.  0.75in satisfies KDP gutter for books up to 500 pages.

PRINT_CSS = r"""
@page {
    size: 6in 9in;
    margin: 0.75in;
}

/* ── Base typography ─────────────────────────────────── */
body {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #111;
    orphans: 3;
    widows: 3;
}

/* ── Headings ────────────────────────────────────────── */
h1 {
    font-size: 22pt;
    margin-top: 0;
    margin-bottom: 0.4em;
    line-height: 1.2;
    break-after: avoid;
}
h2 {
    font-size: 17pt;
    margin-top: 1.4em;
    margin-bottom: 0.5em;
    line-height: 1.25;
    break-after: avoid;
}
h3 {
    font-size: 13pt;
    margin-top: 1.2em;
    margin-bottom: 0.4em;
    break-after: avoid;
}
h4 {
    font-size: 11pt;
    margin-top: 1em;
    margin-bottom: 0.3em;
    break-after: avoid;
}

/* ── Paragraphs & lists ──────────────────────────────── */
p {
    margin: 0 0 0.6em 0;
    text-align: justify;
    hyphens: auto;
    -webkit-hyphens: auto;
}
ul, ol {
    margin: 0.4em 0 0.8em 1.4em;
    padding: 0;
}
li {
    margin-bottom: 0.25em;
}
blockquote {
    margin: 1em 1.5em;
    font-style: italic;
    color: #333;
    border-left: 2pt solid #999;
    padding-left: 0.8em;
}
hr {
    border: none;
    border-top: 0.5pt solid #aaa;
    margin: 1.5em auto;
    width: 40%;
}

/* ── Code & preformatted ─────────────────────────────── */
code {
    font-family: "Courier New", Courier, monospace;
    font-size: 0.85em;
}
pre {
    font-family: "Courier New", Courier, monospace;
    font-size: 7.5pt;
    line-height: 1.3;
    white-space: pre-wrap;
    word-wrap: break-word;
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 3pt;
    padding: 8pt 10pt;
    margin: 0.8em 0;
    break-inside: avoid;
}
pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: inherit;
}

/* ── Tables ──────────────────────────────────────────── */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    font-size: 8.5pt;
    line-height: 1.35;
    break-inside: avoid;
}
th, td {
    border: 0.5pt solid #666;
    padding: 3pt 5pt;
    text-align: left;
    word-wrap: break-word;
    overflow-wrap: break-word;
}
th {
    background-color: #eee;
    font-weight: bold;
}

/* ── Chapter sections ────────────────────────────────── */
.chapter {
    break-before: page;
}

/* ── Title page ──────────────────────────────────────── */
.title-page {
    break-before: avoid;
    text-align: center;
    padding-top: 2in;
}
.title-page h1 {
    font-size: 28pt;
    margin-bottom: 0.2em;
}
.title-page .subtitle {
    font-size: 15pt;
    font-weight: normal;
    font-style: italic;
    color: #444;
    margin-bottom: 1.5em;
}
.title-page .author {
    font-size: 14pt;
    margin-top: 1em;
}

/* ── Copyright page ──────────────────────────────────── */
.copyright-page {
    break-before: page;
    font-size: 8.5pt;
    line-height: 1.5;
    padding-top: 60%;
}
.copyright-page p {
    text-align: left;
}

/* ── Dedication ──────────────────────────────────────── */
.dedication {
    break-before: page;
    padding-top: 2in;
    text-align: center;
}
.dedication p {
    text-align: center;
    font-style: italic;
}
.dedication h2 {
    text-align: center;
}

/* ── TOC ─────────────────────────────────────────────── */
.toc {
    break-before: page;
}

/* ── Math ────────────────────────────────────────────── */
.display-math {
    text-align: center;
    margin: 0.8em 0;
}
math {
    font-size: 1em;
}
"""


def read_markdown_files(chapters_dir):
    """Return list of (basename, markdown_text) sorted by filename."""
    files = [
        f for f in os.listdir(chapters_dir)
        if re.match(r"^\d{2}-.*\.md$", f, flags=re.IGNORECASE)
    ]
    files.sort()
    chapters = []
    for fname in files:
        path = os.path.join(chapters_dir, fname)
        with open(path, "r", encoding="utf-8") as fh:
            text = fh.read()
        base = os.path.splitext(fname)[0]
        chapters.append((base, text))
    return chapters


def md_to_html_body(md_text):
    """Convert markdown to HTML body fragment, with math to MathML."""
    body = markdown.markdown(
        md_text,
        output_format="html",
        extensions=["mdx_math", "fenced_code", "tables"],
        extension_configs={
            "mdx_math": {
                "enable_dollar_delimiter": True,
                "add_preview": False,
            }
        },
    )

    def convert_display_math(match):
        latex = match.group(1).strip()
        try:
            mathml = latex_to_mathml(latex, display="block")
            return f'<div class="display-math">{mathml}</div>'
        except Exception:
            return (
                f'<p style="text-align:center;">'
                f'<code>{html_mod.escape(latex)}</code></p>'
            )

    def convert_inline_math(match):
        latex = match.group(1).strip()
        try:
            return latex_to_mathml(latex, display="inline")
        except Exception:
            return f'<code>{html_mod.escape(latex)}</code>'

    body = re.sub(
        r'<script type="math/tex; mode=display">(.*?)</script>',
        convert_display_math, body, flags=re.DOTALL,
    )
    body = re.sub(
        r'<script type="math/tex">(.*?)</script>',
        convert_inline_math, body, flags=re.DOTALL,
    )

    return body


def build_html(chapters_dir):
    """Build a single HTML document from all markdown sources."""
    chapters = read_markdown_files(chapters_dir)
    if not chapters:
        raise SystemExit(
            "No manuscript .md files found in: " + chapters_dir
        )

    front_matter_files = []
    toc_files = []
    body_files = []

    for base, md_text in chapters:
        prefix = base[:2]
        if prefix == "00":
            front_matter_files.append((base, md_text))
        elif prefix == "01":
            toc_files.append((base, md_text))
        else:
            body_files.append((base, md_text))

    parts = []

    # Title page
    parts.append(f"""
<div class="title-page">
  <h1>{html_mod.escape(BOOK_TITLE)}</h1>
  <p class="subtitle">{html_mod.escape(BOOK_SUBTITLE)}</p>
  <p class="author">by {html_mod.escape(AUTHOR)}</p>
</div>""")

    # Copyright page
    parts.append(f"""
<div class="copyright-page">
  <p><strong>{html_mod.escape(BOOK_TITLE)}: {html_mod.escape(BOOK_SUBTITLE)}</strong></p>
  <p>&copy; {COPYRIGHT_YEAR} {html_mod.escape(AUTHOR)}</p>
  <p>All rights reserved. No part of this book may be reproduced,
  stored in a retrieval system, or transmitted in any form or by any
  means&mdash;electronic, mechanical, photocopying, recording, scanning,
  or otherwise&mdash;without prior written permission of the publisher,
  except in the case of brief quotations embodied in critical articles
  and reviews.</p>
  <p>This book presents a symbolic and spiritual system. It is provided
  for informational and entertainment purposes only and is not a
  substitute for professional advice of any kind.</p>
</div>""")

    # Dedication & Note to Reader from 00-front-matter
    if front_matter_files:
        _, fm_text = front_matter_files[0]
        dedication_match = re.search(
            r'^(##\s+Dedication.*)$',
            fm_text,
            flags=re.MULTILINE | re.DOTALL,
        )
        if dedication_match:
            dedication_html = md_to_html_body(dedication_match.group(1))
            parts.append(
                f'<div class="dedication">\n{dedication_html}\n</div>'
            )

    # Table of Contents
    for _, md_text in toc_files:
        toc_html = md_to_html_body(md_text)
        parts.append(f'<div class="toc">\n{toc_html}\n</div>')

    # Body chapters
    for _, md_text in body_files:
        chapter_html = md_to_html_body(md_text)
        parts.append(f'<div class="chapter">\n{chapter_html}\n</div>')

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html_mod.escape(BOOK_TITLE)}</title>
  <style>
{PRINT_CSS}
  </style>
</head>
<body>
{"".join(parts)}
</body>
</html>
"""
    return full_html


def html_to_pdf_via_edge(html_path, pdf_path):
    """Use Edge headless to print HTML to PDF."""
    if not os.path.isfile(EDGE_PATH):
        raise SystemExit(
            f"Microsoft Edge not found at: {EDGE_PATH}\n"
            "Set EDGE_PATH in this script to the correct location."
        )

    file_url = "file:///" + html_path.replace("\\", "/")

    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        file_url,
    ]

    print("Launching Edge headless...")
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        stderr = result.stderr.strip()
        if stderr:
            print(f"Edge stderr: {stderr}")

    if not os.path.isfile(pdf_path):
        raise SystemExit("Edge did not produce a PDF. Check stderr above.")


def build_pdf(chapters_dir, output_html, output_pdf):
    print("Building HTML from Markdown sources...")
    full_html = build_html(chapters_dir)

    html_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), output_html
    )
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML written to {html_path}")

    pdf_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), output_pdf
    )
    html_to_pdf_via_edge(html_path, pdf_path)

    if os.path.isfile(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"PDF written to {pdf_path} ({size_mb:.1f} MB)")

        try:
            from pypdf import PdfReader
            reader = PdfReader(pdf_path)
            page_count = len(reader.pages)
            w = float(reader.pages[0].mediabox.width)
            h = float(reader.pages[0].mediabox.height)
            print(f"Pages: {page_count}  |  Size: {w/72:.2f}in x {h/72:.2f}in")
            print()
            _check_gutter(page_count)
        except ImportError:
            pass


def _check_gutter(page_count):
    """Print KDP gutter margin guidance based on page count."""
    print("KDP gutter (inside) margin requirements:")
    thresholds = [
        (150, 0.375), (300, 0.5), (500, 0.625), (700, 0.75), (828, 0.875),
    ]
    for max_pages, min_gutter in thresholds:
        marker = ">>" if page_count <= max_pages else "  "
        print(f"  {marker} {max_pages:>3} pages or fewer -> {min_gutter}\"")
        if page_count <= max_pages:
            break
    current_margin = 0.75
    print(f"  Current inside margin: {current_margin}\"")
    for max_pages, min_gutter in thresholds:
        if page_count <= max_pages:
            if current_margin >= min_gutter:
                print("  OK: Gutter margin is sufficient.")
            else:
                print(
                    f"  WARNING: Increase margins to at least "
                    f"{min_gutter}\" for {page_count} pages."
                )
            break


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.join(base_dir, "src")
    html_out = os.path.join(base_dir, OUTPUT_HTML)
    pdf_out = os.path.join(base_dir, OUTPUT_PDF)
    build_pdf(chapters_dir, html_out, pdf_out)
