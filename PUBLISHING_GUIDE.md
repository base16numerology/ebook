# Publishing Guide: Base 16 Numerology

Pre-filled metadata and step-by-step instructions for publishing to
**Amazon Kindle Direct Publishing (KDP)** and **Kobo Writing Life**.

---

## Pre-Flight Checklist

- [x] EPUB builds without errors (`uv run python build_epub.py`)
- [x] EPUB passes structural validation (no XML errors, valid OPF/NCX)
- [x] Cover image present (1024×1536 px)
- [ ] **IMPORTANT: Upscale cover to 2560×1600 px** (see Cover Image section below)
- [ ] Proofread final EPUB in an EPUB reader (e.g. Calibre, Apple Books)
- [ ] Test on Kindle Previewer (free download from Amazon)
- [ ] Obtain ISBNs if desired (see ISBN section below)

---

## Cover Image Requirements

Your current cover is **1024×1536 px**. Both platforms want larger:

| Platform | Minimum        | Recommended     | Aspect Ratio |
|----------|---------------|-----------------|--------------|
| Amazon KDP | 625×1000 px | **2560×1600 px** | 1.6:1 (H:W) |
| Kobo     | 1400 px short side | **1600×2400 px** | 1.5:1 (H:W) |

**Action needed:** Upscale or re-export your cover to at least **1600×2400 px**
(ideally **2560×1600 px** for KDP). If you used an AI image generator or
design tool, re-export at higher resolution. Then rebuild the EPUB:

```powershell
# Copy the new cover into src/
Copy-Item new_cover.png .\src\cover.png
uv run python build_epub.py
```

---

## ISBN (Optional but Recommended)

- **Amazon KDP** does NOT require an ISBN — they assign a free ASIN.
  However, you CAN enter your own ISBN if you have one.
- **Kobo** does NOT require an ISBN for ebooks, but recommends one for
  discoverability.
- If you want an ISBN, purchase from your national agency:
  - **USA:** Bowker (https://www.myidentifiers.com/) — $125 for 1, $295 for 10
  - **Canada:** free from Library and Archives Canada
  - **UK:** Nielsen (https://www.nielsenisbnstore.com/)
- Use a **separate ISBN for each format** (EPUB for Kobo, Kindle edition).

---

## Book Metadata (Use for Both Platforms)

Copy-paste these values when filling out the publishing forms.

### Title & Author

| Field | Value |
|-------|-------|
| **Title** | Base 16 Numerology |
| **Subtitle** | Decoding Your Life in Hex, from Unix Time to Soul Code |
| **Author** | Horace Chan |
| **Language** | English |

### Book Description (HTML — works on both KDP and Kobo)

```html
<p><b>What if the universe speaks in hex?</b></p>

<p>Traditional numerology was built for pen and paper — a Latin alphabet,
calendar dates, and single-digit reductions. <i>Base 16 Numerology</i>
reimagines the ancient practice for the digital age, using the same
hexadecimal system that powers every screen, file, and network packet on
Earth.</p>

<p>Your name becomes UTF-8 bytes. Your birth moment becomes a Unix
timestamp. Both are hashed through LIBRE-256 — an open, reproducible
algorithm — and reduced to a single hex digit between <b>0</b> and
<b>f</b>. That digit is your archetype.</p>

<p>Sixteen archetypes across four realms — Physical, Emotional, Mental,
and Spiritual — form your <b>Hex Soul Map</b>: a five-position portrait
of your Life Path, Expression, Soul Urge, Personality, and Maturity.</p>

<p>Inside you'll discover:</p>
<ul>
<li>How hexadecimal, Unicode, and Unix time create a universal symbolic language</li>
<li>The LIBRE-256 hash: open-source, verifiable, and spiritually resonant</li>
<li>All sixteen archetypes (0–f) explained in depth — light, shadow, and positional meaning</li>
<li>How to build and read your personal Hex Soul Map</li>
<li>Personal Hex Years: a cycle-based timing tool for decisions and growth</li>
<li>Relationship overlays, career guidance, and place-based readings in hex</li>
<li>Practice case studies and a built-in skeptic mode</li>
<li>Worksheets, journaling prompts, and companion app guide</li>
</ul>

<p>Written for readers who are mystical enough to enjoy archetypes and
skeptical enough to want the math underneath. No special knowledge of
programming is required — every concept is explained from first
principles.</p>

<p><b>The numbers are just an interface. The real program is your
life.</b></p>
```

### Plain-Text Description (Fallback)

```
What if the universe speaks in hex?

Traditional numerology was built for pen and paper. Base 16 Numerology
reimagines the practice for the digital age, using the same hexadecimal
system that powers every screen, file, and network packet on Earth.

Your name becomes UTF-8 bytes. Your birth moment becomes a Unix
timestamp. Both are hashed through LIBRE-256 — an open, reproducible
algorithm — and reduced to a single hex digit between 0 and f. That
digit is your archetype.

Sixteen archetypes across four realms form your Hex Soul Map: a
five-position portrait of your Life Path, Expression, Soul Urge,
Personality, and Maturity.

Written for readers who are mystical enough to enjoy archetypes and
skeptical enough to want the math underneath.
```

### Categories / BISAC Codes

Amazon KDP and Kobo both use BISAC categories. Select up to **2** on KDP,
up to **3** on Kobo:

1. **BODY, MIND & SPIRIT / Numerology** (primary)
   - BISAC: OCC015000
2. **COMPUTERS / General** or **COMPUTERS / History** (secondary — captures the tech angle)
   - BISAC: COM000000 or COM034000
3. **BODY, MIND & SPIRIT / New Thought** (tertiary, Kobo only)
   - BISAC: OCC014000

### Keywords (up to 7 for KDP)

```
numerology, hexadecimal, base 16, soul map, archetypes, unix timestamp, spiritual technology
```

### Pricing (Suggested)

| Platform | Price (USD) | Royalty Rate | Notes |
|----------|------------|--------------|-------|
| Amazon KDP | $9.99 | 70% | Must be $2.99–$9.99 for 70% tier |
| Kobo | $9.99 | 70% | 70% for $2.99–$12.99 |

You can adjust pricing by territory on both platforms.

### Other Metadata

| Field | Value |
|-------|-------|
| **Publisher** | (your name or imprint, e.g. "Horace Chan") |
| **Publication date** | (set to your desired launch date) |
| **DRM** | Recommended: **No DRM** (readers prefer it; does not affect piracy) |
| **Age range** | Adult (18+) or General Audience |
| **Content warnings** | None required |

---

## Platform 1: Amazon Kindle Direct Publishing (KDP)

### Account Setup

1. Go to https://kdp.amazon.com/
2. Sign in with your Amazon account (or create one)
3. Complete tax information (W-9 for US, W-8BEN for international)
4. Add bank account for royalty payments

### Publishing Steps

1. **Go to "Bookshelf" → "Create New Title" → "Kindle eBook"**

2. **Kindle eBook Details** (page 1):
   - Language: English
   - Book Title: `Base 16 Numerology`
   - Subtitle: `Decoding Your Life in Hex, from Unix Time to Soul Code`
   - Series: (leave blank unless you plan a series)
   - Edition: 1
   - Author: `Horace Chan`
   - Description: paste the **HTML** description above
   - Publishing Rights: "I own the copyright"
   - Keywords: paste the 7 keywords above
   - Categories: select the BISAC codes above
   - Age Range: Not a children's book

3. **Kindle eBook Content** (page 2):
   - Manuscript: upload `base16_numerology.epub`
   - Cover: upload `src/cover.png` (or your upscaled version)
     - KDP has a Cover Creator if you need one, but your own is better
   - **Launch Kindle Previewer** to check formatting before proceeding
   - ISBN: optional (enter if you have one)

4. **Kindle eBook Pricing** (page 3):
   - KDP Select: **your choice** (enrolling gives Kindle Unlimited access
     but requires 90-day exclusivity — you CANNOT sell on Kobo during that
     period)
   - Territories: All territories (recommended)
   - Royalty: 70% (for $2.99–$9.99)
   - Set your price

5. Click **"Publish Your Kindle eBook"**
   - Review typically takes **24–72 hours**

### KDP Select vs. Wide Distribution

**If you want to sell on BOTH Amazon and Kobo**, do NOT enroll in KDP Select.
KDP Select requires exclusivity — your ebook can only be sold on Amazon.

**If you want Kindle Unlimited readers**, enroll in KDP Select but skip Kobo.

---

## Platform 2: Kobo Writing Life

### Account Setup

1. Go to https://www.kobo.com/writinglife
2. Create a Kobo Writing Life account
3. Complete tax information
4. Add bank account / PayPal for royalty payments

### Publishing Steps

1. **Go to "eBooks" → "Create New eBook"**

2. **eBook Details**:
   - Title: `Base 16 Numerology`
   - Subtitle: `Decoding Your Life in Hex, from Unix Time to Soul Code`
   - Author: `Horace Chan`
   - Language: English
   - Publisher: (your name or imprint)
   - Description: paste the **HTML** description above (Kobo supports HTML)
   - Categories: select using BISAC codes above
   - ISBN: optional

3. **Upload Content**:
   - Manuscript: upload `base16_numerology.epub`
   - Cover: upload `src/cover.png` (or upscaled version)

4. **Rights & Pricing**:
   - Territories: Worldwide (recommended)
   - Price: $9.99 USD (set per-territory if desired)
   - DRM: recommended OFF

5. Click **"Publish"**
   - Review typically takes **24–72 hours**

---

## Post-Publishing Checklist

- [ ] Verify the book appears in each store's search
- [ ] Purchase a copy on each platform and verify formatting
- [ ] Check that the Table of Contents navigation works
- [ ] Set up your Amazon Author Central page (https://author.amazon.com/)
- [ ] Set up your Kobo author page
- [ ] Consider a launch promotion (KDP Countdown Deal or Kobo Promotions)

---

## Files to Upload

| Platform | Manuscript File | Cover File |
|----------|----------------|------------|
| Amazon KDP | `base16_numerology.epub` | `src/cover.png` |
| Kobo | `base16_numerology.epub` | `src/cover.png` |

Both files are in: `B:\base16numerology\ebook\`

---

## Rebuilding the EPUB

If you make any changes to the manuscript, rebuild:

```powershell
Set-Location B:\base16numerology\ebook
uv run python build_epub.py
```

Output: `base16_numerology.epub`
