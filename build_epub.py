#!/usr/bin/env python3
import os
import zipfile
import uuid
import datetime
import html
import re

try:
    import markdown
except ImportError:
    raise SystemExit(
        "This script requires the 'markdown' package.\n"
        "Install it with:\n\n    pip install markdown\n"
    )

BOOK_TITLE = "Base 16 Numerology: Decoding Your Life in Hex, from Unix Time to Soul Code"
AUTHOR = "Horace Chan"

OUTPUT_EPUB = "base16_numerology.epub"
COVER_FILENAME = "cover.png"        # optional; put cover.png next to this script


def read_markdown_files(chapters_dir):
    """
    Return a list of (basename_without_ext, markdown_text) sorted by filename.

    By default this expects the manuscript files to be in the same directory as
    this script, named like "00-front-matter.md", "01-table-of-contents.md", etc.
    """
    files = [
        f
        for f in os.listdir(chapters_dir)
        if re.match(r"^\d{2}-.*\.md$", f, flags=re.IGNORECASE)
    ]
    files.sort()
    chapters = []
    for fname in files:
        path = os.path.join(chapters_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        base = os.path.splitext(fname)[0]
        chapters.append((base, text))
    return chapters


def extract_title_from_md(md_text, fallback):
    """
    Grab the first Markdown heading line (#, ##, or ###) and use its text as title.
    If none found, fall back to provided fallback string.
    """
    for line in md_text.splitlines():
        # Match headings like "# Title", "## Title", "### Title"
        m = re.match(r'^\s{0,3}(#{1,6})\s+(.*)$', line)
        if m:
            title = m.group(2).strip()
            if title:
                return title
    return fallback


def md_to_xhtml(title, md_text):
    """
    Convert markdown text to a minimal XHTML document string with given <title>.
    Handles LaTeX math via python-markdown-math extension, then converts to MathML.
    """
    from latex2mathml.converter import convert as latex_to_mathml
    
    body_html = markdown.markdown(
        md_text,
        output_format="xhtml1",
        extensions=["mdx_math"],
        extension_configs={
            "mdx_math": {
                "enable_dollar_delimiter": True,
                "add_preview": False,
            }
        },
    )
    
    # mdx_math outputs <script type="math/tex"> tags for MathJax.
    # Convert these to MathML for EPUB reader compatibility.
    import re
    
    def convert_display_math(match):
        latex = match.group(1)
        try:
            mathml = latex_to_mathml(latex, display="block")
            return f'<div style="text-align:center;">{mathml}</div>'
        except:
            return f'<p style="text-align:center;"><code>{html.escape(latex)}</code></p>'
    
    def convert_inline_math(match):
        latex = match.group(1)
        try:
            mathml = latex_to_mathml(latex, display="inline")
            return mathml
        except:
            return f'<code>{html.escape(latex)}</code>'
    
    # Replace display math
    body_html = re.sub(
        r'<script type="math/tex; mode=display">(.*?)</script>',
        convert_display_math,
        body_html,
        flags=re.DOTALL
    )
    # Replace inline math
    body_html = re.sub(
        r'<script type="math/tex">(.*?)</script>',
        convert_inline_math,
        body_html,
        flags=re.DOTALL
    )
    
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>{html.escape(title)}</title>
  <meta charset="utf-8" />
</head>
<body>
{body_html}
</body>
</html>
"""


def cover_to_xhtml(book_title):
    """Generate a minimal cover page that displays cover.png."""
    return f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
<!DOCTYPE html>
<html xmlns=\"http://www.w3.org/1999/xhtml\">
<head>
  <title>{html.escape(book_title)} – Cover</title>
  <meta charset=\"utf-8\" />
</head>
<body>
  <div style=\"text-align:center; margin:0; padding:0;\">
    <img src=\"cover.png\" alt=\"Cover\" style=\"max-width:100%; height:auto;\" />
  </div>
</body>
</html>
"""


def build_epub(chapters_dir, output_epub, book_title, author, cover_filename=None):
    chapters = read_markdown_files(chapters_dir)
    if not chapters:
        raise SystemExit(
            "No manuscript .md files found. Expected files named like '00-*.md' in: "
            + chapters_dir
        )

    book_id = str(uuid.uuid4())
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest_items = []
    spine_items = []
    xhtml_files = []
    nav_labels = []

    # Optional cover
    has_cover = cover_filename and os.path.exists(cover_filename)
    if has_cover:
        # Many EPUB2 readers expect an actual XHTML cover page plus an OPF guide entry.
        manifest_items.append(
            '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>'
        )
        manifest_items.append(
            '<item id="cover-image" href="cover.png" media-type="image/png"/>'
        )
        spine_items.append('<itemref idref="cover" linear="no"/>')
        xhtml_files.append(("cover.xhtml", cover_to_xhtml(book_title)))

    # Build XHTML files and manifest/spine entries
    for idx, (base, md_text) in enumerate(chapters, start=1):
        # Extract human-readable title from Markdown heading
        pretty_title = extract_title_from_md(md_text, fallback=base)
        xhtml_name = f"{base}.xhtml"
        xhtml_content = md_to_xhtml(pretty_title, md_text)
        xhtml_files.append((xhtml_name, xhtml_content))
        nav_labels.append(pretty_title)

        item_id = f"item{idx}"
        manifest_items.append(
            f'<item id="{item_id}" href="{xhtml_name}" media-type="application/xhtml+xml"/>'
        )
        spine_items.append(f'<itemref idref="{item_id}"/>')

    manifest_xml = "\n    ".join(manifest_items)
    spine_xml = "\n    ".join(spine_items)

    # content.opf
    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{html.escape(book_title)}</dc:title>
    <dc:creator>{html.escape(author)}</dc:creator>
    <dc:identifier id="BookId">urn:uuid:{book_id}</dc:identifier>
    <dc:language>en</dc:language>
    <dc:date>{now}</dc:date>
    {"<meta name=\"cover\" content=\"cover-image\"/>" if has_cover else ""}
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    {manifest_xml}
  </manifest>
  <spine toc="ncx">
    {spine_xml}
  </spine>
  {"<guide><reference type=\"cover\" title=\"Cover\" href=\"cover.xhtml\"/></guide>" if has_cover else ""}
</package>
"""

    # toc.ncx
    nav_points = []
    for idx, (base, _) in enumerate(chapters, start=1):
        xhtml_name = f"{base}.xhtml"
        label = nav_labels[idx - 1]  # title we pulled from the md
        nav_points.append(f"""
    <navPoint id="navPoint-{idx}" playOrder="{idx}">
      <navLabel><text>{html.escape(label)}</text></navLabel>
      <content src="{xhtml_name}"/>
    </navPoint>""")
    navpoints_xml = "\n".join(nav_points)

    toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"
  "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{book_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{html.escape(book_title)}</text></docTitle>
  <navMap>
    {navpoints_xml}
  </navMap>
</ncx>
"""

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0"
  xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf"
      media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""

    # Build the EPUB (ZIP)
    with zipfile.ZipFile(output_epub, "w") as zf:
        # mimetype must be first and uncompressed
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        # META-INF
        zf.writestr("META-INF/container.xml", container_xml)
        # OEBPS core files
        zf.writestr("OEBPS/content.opf", content_opf)
        zf.writestr("OEBPS/toc.ncx", toc_ncx)
        # Chapters
        for xhtml_name, xhtml_content in xhtml_files:
            zf.writestr(f"OEBPS/{xhtml_name}", xhtml_content.encode("utf-8"))
        # Optional cover
        if has_cover:
            with open(cover_filename, "rb") as f:
                zf.writestr("OEBPS/cover.png", f.read())

    print(f"EPUB written to {output_epub}")


if __name__ == "__main__":
  base_dir = os.path.dirname(os.path.abspath(__file__))
  cover_path = os.path.join(base_dir, COVER_FILENAME)
  out_path = os.path.join(base_dir, OUTPUT_EPUB)
  build_epub(base_dir, out_path, BOOK_TITLE, AUTHOR, cover_path)

