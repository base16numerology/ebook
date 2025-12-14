# Base 16 Numerology (ebook)

Manuscript source for **_Base 16 Numerology: Decoding Your Life in Hex, from Unix Time to Soul Code_** by **Horace Chan**.

This book treats modern computing primitives (hex, Unicode bytes, Unix timestamps, hashing) as a symbolic language: your name and birth moment are encoded, hashed via **LIBRE‑256**, reduced `mod 16`, and interpreted as one of sixteen hex archetypes (`0`–`f`). It’s written for readers who are mystical enough to enjoy archetypes and skeptical enough to want the math underneath.

## Repository contents

- Manuscript (Markdown, in reading order):
	- [00-front-matter.md](00-front-matter.md)
	- [01-table-of-contents.md](01-table-of-contents.md)
	- [02-introduction-when-the-soul-learned-to-count-in-hex.md](02-introduction-when-the-soul-learned-to-count-in-hex.md)
	- [03-chapter-1-the-power-of-sixteen.md](03-chapter-1-the-power-of-sixteen.md)
	- [04-chapter-2-what-is-base-16-numerology.md](04-chapter-2-what-is-base-16-numerology.md)
	- [05-chapter-3-from-text-to-hex-ascii-unicode-and-the-libre-256-hash.md](05-chapter-3-from-text-to-hex-ascii-unicode-and-the-libre-256-hash.md)
	- [06-chapter-4-birth-in-machine-time-unix-epoch-and-your-hex-life-path.md](06-chapter-4-birth-in-machine-time-unix-epoch-and-your-hex-life-path.md)
	- [07-chapter-5-the-sixteen-archetypes-0-f-explained.md](07-chapter-5-the-sixteen-archetypes-0-f-explained.md)
	- [08-chapter-6-the-hex-soul-map-combining-your-numbers.md](08-chapter-6-the-hex-soul-map-combining-your-numbers.md)
	- [09-chapter-7-cycles-timestamps-and-personal-hex-years.md](09-chapter-7-cycles-timestamps-and-personal-hex-years.md)
	- [10-chapter-8-relationships-work-and-places-in-hex.md](10-chapter-8-relationships-work-and-places-in-hex.md)
	- [11-chapter-9-practice-case-studies-and-skeptic-mode.md](11-chapter-9-practice-case-studies-and-skeptic-mode.md)
	- [12-appendix-a-bytes-nibbles-and-hex-archetypes.md](12-appendix-a-bytes-nibbles-and-hex-archetypes.md)
	- [13-appendix-b-ascii-unicode-and-the-secret-life-of-characters.md](13-appendix-b-ascii-unicode-and-the-secret-life-of-characters.md)
	- [14-appendix-c-worksheets-prompts-and-the-app.md](14-appendix-c-worksheets-prompts-and-the-app.md)
- Cover image: [cover.png](cover.png)
- EPUB builder: [build_epub.py](build_epub.py)
- Built artifacts:
	- [base16_numerology.epub](base16_numerology.epub)


## Build the EPUB

### Prerequisites

- Python 3
- `uv` (Python package manager)

This repo includes `pyproject.toml` with the required dependencies.

### Install deps (uv)

```powershell
Set-Location b:\base16numerology\ebook
uv sync
```

### Run

`build_epub.py` reads the manuscript Markdown files in the same directory as the script, matching `??-*.md` (for example `00-front-matter.md`, `01-table-of-contents.md`, …). It ignores other Markdown files like `README.md`.

```powershell
Set-Location b:\base16numerology\ebook
uv run python .\build_epub.py
```

Output: `base16_numerology.epub`

## License / rights

- Repository license file: `LICENSE` (GPLv3).
- The book text itself includes its own copyright notice in `00-front-matter.md`.
