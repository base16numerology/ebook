## Appendix B – ASCII, Unicode, and the Secret Life of Characters

Every character in your name already has a numeric identity. This appendix provides a deeper look at the character encoding systems that underpin Base 16 Numerology, for readers who want to understand the substrate their hex digits are built on.

### ASCII: The First Alphabet of the Machine Age

ASCII (American Standard Code for Information Interchange) was published in 1963. It assigns codes 0 through 127 to 128 characters:

- **0–31:** Control characters (non-printable). These include Tab (9), Line Feed (10), and Carriage Return (13). They are the invisible commands that structure text—the digital equivalents of a scribe's formatting marks.

- **32:** Space. The most important invisible character. In Base 16 Numerology, spaces in your name contribute bytes to the hash, which is why "Mary Jane" and "MaryJane" produce different results.

- **33–47:** Punctuation and symbols. `!`, `"`, `#`, `$`, `%`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `-`, `.`, `/`.

- **48–57:** Digits 0–9.

- **65–90:** Uppercase Latin letters A–Z.

- **97–122:** Lowercase Latin letters a–z.

**Key insight for numerology:** In ASCII (and Unicode), uppercase and lowercase letters have different codes. `A` is 65, `a` is 97—they differ by exactly 32. This means "ALEX" and "alex" are different byte sequences and will produce different LIBRE-256 hashes.

Traditional numerology ignores case: A and a are both "1." Base 16 Numerology respects case because the bytes are different. This is not a bug; it's a feature. The way your name is written—the specific capitalization on your birth certificate—is part of the spell.

### Unicode: The Universal Character Set

ASCII served English well, but the world has thousands of writing systems. Unicode was created to assign a unique code point to every character in every human writing system, past and present.

As of Unicode 16.0 (2024), there are over 154,000 assigned characters. Some highlights:

**Latin Extended:**
- `é` (e with acute accent) → U+00E9
- `ñ` (n with tilde) → U+00F1
- `ü` (u with diaeresis) → U+00FC

These accented characters are *different code points* from their unaccented counterparts. "Jose" and "José" are different strings. "Muller" and "Müller" are different strings. Base 16 Numerology treats them differently because they are, at the byte level, genuinely different.

**Cyrillic:**
- `А` (Cyrillic A) → U+0410
- `Б` (Cyrillic Be) → U+0411
- `Д` (Cyrillic De) → U+0414

Note: Cyrillic А (U+0410) looks identical to Latin A (U+0041) on screen, but they are different code points with different byte representations. This means "Anna" in Latin script and "Анна" in Cyrillic are different byte sequences, even though they represent the same name in the same language. Each produces its own hash.

**Arabic:**
- `م` (Meem) → U+0645
- `ح` (Haa) → U+062D
- `د` (Dal) → U+062F

Arabic is written right-to-left and uses contextual letter forms (the same letter looks different at the beginning, middle, or end of a word). Unicode encodes the abstract letter, not the specific visual form. LIBRE-256 operates on the code points, not the visual rendering.

**CJK (Chinese, Japanese, Korean):**
- `日` (sun/day) → U+65E5
- `月` (moon/month) → U+6708
- `明` (bright, combining sun and moon) → U+660E

CJK characters are among the most byte-intensive in UTF-8, typically requiring 3 bytes each. A Chinese name like "陈明" is 6 bytes in UTF-8, while "Chen Ming" is 10 bytes. Same person, same pronunciation, different byte patterns, potentially different archetypes.

**Emoji:**
- `😊` (Smiling Face with Smiling Eyes) → U+1F60A
- `🔥` (Fire) → U+1F525
- `💻` (Laptop) → U+1F4BB

Emoji are valid Unicode characters with assigned code points. In UTF-8, most emoji require 4 bytes. If your name (or online handle) includes emoji, those emoji contribute bytes to the hash.

### UTF-8: The Encoding Standard

Unicode defines the *what* (which code points exist), while UTF-8 defines the *how* (how code points are stored as bytes in memory).

UTF-8 is a variable-length encoding:

- **1 byte** for ASCII characters (U+0000 to U+007F): the byte is identical to the ASCII code.
- **2 bytes** for code points U+0080 to U+07FF: covers most European scripts, Arabic, Hebrew, and many others.
- **3 bytes** for code points U+0800 to U+FFFF: covers CJK ideographs, most of the rest of the Basic Multilingual Plane.
- **4 bytes** for code points U+10000 to U+10FFFF: covers emoji, rare scripts, historical scripts, and mathematical symbols.

LIBRE-256 operates on the UTF-8 byte sequence, not on the raw code points. This means:

- An ASCII character contributes 1 byte to the hash.
- A CJK character contributes 3 bytes.
- An emoji contributes 4 bytes.

The number and weight of bytes differ by script, which means names in different scripts have different "byte weights" even for similar phonetic content. This is intentional: Base 16 Numerology does not claim that a name in English and the same name in Chinese should produce the same result. Each encoding carries its own energy.

### Practical Implications

**Which version of your name should you use?**

Your **full legal birth name** as it appears on your birth certificate, in whatever script it was originally written. If your birth certificate is in Arabic, use the Arabic form. If it's in Latin script with accents, include the accents. If your legal name has changed (through marriage, legal petition, etc.), you can compute both the birth name and current name; they represent different energies.

**What about nicknames and handles?**

Your birth name Expression is the foundational reading, but you can hash any version of your name for additional insight:

- Your childhood nickname may reveal an archetype you've outgrown (or not).
- Your professional name may reveal the energy you broadcast in your career.
- Your online handle may reveal your digital persona—the archetype you chose, consciously or not, for your life on the internet.

**What about names in multiple scripts?**

If your name is commonly written in more than one script (for example, a Chinese name that also has a romanized form), you can hash both versions. The birth certificate version is primary; alternative scripts offer supplementary readings.

**What about typos?**

A typo changes the byte sequence, which changes the hash. "Horace" and "Hoarce" are different strings with (likely) different hex digits. This is why precision matters: your exact string is your exact spell. Use the correct, intended form of your name.

### The Secret Life of Characters

Here is a thought to end this appendix:

Every character you have ever typed, every message you have ever sent, every document you have ever written—all of it was stored as sequences of bytes, each byte writeable as two hex digits.

Your love letters? Hex.  
Your angry emails? Hex.  
Your dreams, typed into a journal at 3 AM? Hex.

The characters are not just symbols on a screen. They are numbers—numbers that live in the same hexadecimal space as the archetypes in this book. When you hash your name, you are not doing something artificial. You are asking the system that already encodes your name to reveal one more layer of its structure.

The characters were always numbers. Base 16 Numerology just asks what those numbers mean.
