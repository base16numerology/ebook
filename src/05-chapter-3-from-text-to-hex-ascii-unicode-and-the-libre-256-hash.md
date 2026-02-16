## Chapter 3 – From Text to Hex  
### ASCII, Unicode and the LIBRE‑256 Hash

To decode your name, we have to talk about characters. Not the characters in a novel—though we will get to those—but the characters in a computer. Because in Base 16 Numerology, your name is not a word. It is a spell, and the incantation is measured in bytes.

### Characters as Numbers

Every character you type on a keyboard—every letter, digit, space, and punctuation mark—has a numeric code assigned to it by international standards. This is not mysticism; it is engineering. But the distinction blurs when you realize that the first thing any computer does with your name is turn it into a sequence of numbers.

In human terms your name might be:

> Alex Jordan

In machine terms it is a sequence of codes:

- `A` = 65  
- `l` = 108  
- `e` = 101  
- `x` = 120  
- space = 32  
- `J` = 74  
- `o` = 111  
- `r` = 114  
- `d` = 100  
- `a` = 97  
- `n` = 110  

That's ASCII—the American Standard Code for Information Interchange, created in 1963. ASCII assigned codes 0 through 127 to the basic Latin alphabet, digits, punctuation, and a handful of control characters. It was designed for English, by English speakers, in an English-speaking country.

But the world is larger than English.

### Unicode: Every Script Under the Sun

Unicode extends ASCII's idea to virtually every writing system humans have ever used. As of 2024, Unicode defines over 154,000 characters across 168 scripts, including:

- Latin, Greek, Cyrillic, Armenian, Georgian
- Arabic, Hebrew, Syriac, Thaana
- Devanagari, Bengali, Gurmukhi, Tamil, Telugu, Kannada, Malayalam
- Thai, Lao, Tibetan, Myanmar
- Chinese (CJK Unified Ideographs), Japanese (Hiragana, Katakana), Korean (Hangul)
- Ethiopian, Cherokee, Canadian Aboriginal Syllabics
- Mathematical symbols, musical notation, and thousands of emoji

Every character has a code point—a unique number. `A` is U+0041. `Ж` (Cyrillic Zhe) is U+0416. `日` (Chinese/Japanese "sun/day") is U+65E5. `😊` (Smiling Face) is U+1F60A.

When these code points are stored in a computer, they are encoded as sequences of bytes. The most common encoding is UTF-8, which represents each code point as 1 to 4 bytes:

- ASCII characters (U+0000 to U+007F): 1 byte each
- Most European and Middle Eastern scripts: 2 bytes each
- CJK ideographs: 3 bytes each
- Emoji and rare scripts: 4 bytes each

This means "Alex Jordan" is 11 bytes in UTF-8. But "アレックス" (the same name in Japanese katakana) is 15 bytes. And "Алекс" (in Russian) is 10 bytes. The same person, the same sound, different byte patterns.

### Why This Matters for Numerology

Base 16 Numerology does **not** flatten this to "A = 1, B = 2":

- `ALEX` and `alex` are different byte patterns. In traditional numerology, case doesn't matter. Here, it does. The uppercase A (65) and the lowercase a (97) are different bytes, and they produce different hash results.

- Spaces, hyphens, apostrophes, emoji—everything with a code point—counts. "Mary Jane" and "MaryJane" are different byte sequences. "O'Brien" and "OBrien" are different. Every character matters.

- The same name in different scripts produces different results. "Horace" in Latin letters and "ホレス" in katakana are different byte streams. Base 16 Numerology does not claim they should be the same. It treats each encoding as its own spell.

Your exact string is your exact spell. No simplification, no normalization, no "well, close enough." The bytes are what they are.

This has a practical implication: when you compute your Hex Expression, you should use your **full legal birth name as it appears on your birth certificate**, in whatever script it was originally written. If your birth certificate says "José María García," that's your input—accents, spaces, and all. If it says "김민수," that's your input.

### LIBRE‑256: The Hash with an Open‑Source Soul

Now we need to turn a variable-length string of bytes into a single byte. This is the job of a hash function.

Hash functions are a cornerstone of computer science. They take inputs of any size and produce outputs of a fixed size. The best-known hash functions—SHA-256, MD5, BLAKE3—are designed for cryptographic security: they must be collision-resistant, preimage-resistant, and unpredictable.

LIBRE-256 has no such ambitions. It is a tiny, 8-bit hash function designed for symbolic use. Its output is a single byte: a number between 0 and 255. Its goals are:

1. **Determinism:** The same input always produces the same output.
2. **Sensitivity:** Small changes in input produce different outputs (usually).
3. **Distribution:** Outputs are spread reasonably evenly across 0–255.
4. **Simplicity:** The algorithm can be understood, verified, and reimplemented by anyone with basic programming knowledge.
5. **Openness:** The algorithm is fully documented and freely available.

The name "LIBRE" nods to free and open-source culture: algorithms you can inspect, question, and fork.

> **L**ocalized  
> **I**terative  
> **B**yte  
> **R**esonance  
> **E**ncoder – 256 states.

Under the hood (for the curious):

1. Treat the input as a vector of bytes  
   \[
   \mathbf{x} = [x_0, x_1, \dots, x_{n-1}], \quad x_i \in \{0, \dots, 255\}.
   \]

2. Initialize a 4-component state vector \(\mathbf{v} = [v_0, v_1, v_2, v_3]\) to a fixed seed.

3. For each byte \(x_i\), update the state using XOR operations and bit-rotations:
   - \(v_0 \leftarrow v_0 \oplus x_i\)
   - \(v_1 \leftarrow v_1 \oplus \text{ROL}(x_i, 3)\)
   - \(v_2 \leftarrow v_2 \oplus \text{ROL}(x_i, 5)\)
   - \(v_3 \leftarrow v_3 \oplus \text{ROL}(x_i, 7)\)
   
   where ROL denotes left bit-rotation within a byte.

4. After processing all bytes, multiply by a fixed 4×4 matrix \(M\) modulo 256:
   \[
   \mathbf{y} = M \cdot \mathbf{v} \pmod{256}.
   \]

5. Collapse \(\mathbf{y}\) back into a single byte:
   \[
   B = y_0 \oplus y_1 \oplus y_2 \oplus y_3.
   \]

For non‑geeks:

> LIBRE‑256 is just the function the app uses to turn your name into a number between 0 and 255. You can think of it as a blender: you put in your bytes, it spins them around, and what comes out is a single number that represents the "essence" of the input.

For medium-geeks:

> It is an iterated XOR-rotate accumulator followed by a linear mixing step. Not cryptographically secure, but sufficient for symbolic purposes. The mixing matrix ensures that every input byte influences the final output, and the rotation steps provide diffusion across bit positions.

For full geeks:

> The reference implementation is available on the project's GitHub repository. It is about 30 lines of Python. You can read it, test it, and satisfy yourself that it does what we claim.

### From Byte to Hex Archetype

Once LIBRE‑256 gives you a byte \(B\), we compress it to a hex digit:

\[
h = B \bmod 16.
\]

This is the modulo operation—the remainder when you divide by 16. It is the same operation that converts a byte into its lower nibble: the last hex digit when the byte is written in hexadecimal.

- If \(B = 158\), then \(158 \bmod 16 = 14\) → hex `e` → **Heart of All**.
- If \(B = 73\), then \(73 \bmod 16 = 9\) → hex `9` → **Bridge**.
- If \(B = 0\), then \(0 \bmod 16 = 0\) → hex `0` → **Field**.
- If \(B = 255\), then \(255 \bmod 16 = 15\) → hex `f` → **Integrator**.

This `h` is your archetype digit for the string you hashed.

Note that exactly 16 different byte values map to each hex digit: bytes 0, 16, 32, ..., 240 all map to `0`; bytes 1, 17, 33, ..., 241 all map to `1`; and so on. This means each archetype has an equal "catch basin" of 16 byte values, ensuring no archetype is inherently more or less likely than any other (assuming LIBRE-256 distributes its outputs evenly).

### Computing Your Hex Expression: A Worked Example

Let's walk through a complete example. Suppose your birth name is "Alex Jordan."

**Step 1: Convert to bytes (UTF-8)**

| Character | Code Point | UTF-8 Bytes |
|-----------|-----------|-------------|
| A | 65 | 65 |
| l | 108 | 108 |
| e | 101 | 101 |
| x | 120 | 120 |
| (space) | 32 | 32 |
| J | 74 | 74 |
| o | 111 | 111 |
| r | 114 | 114 |
| d | 100 | 100 |
| a | 97 | 97 |
| n | 110 | 110 |

The byte vector is: [65, 108, 101, 120, 32, 74, 111, 114, 100, 97, 110].

**Step 2: Feed into LIBRE-256**

The algorithm processes each byte through its XOR-rotate-accumulate loop, then applies the mixing matrix. (The app handles this; we're showing the logic, not asking you to compute it.)

Suppose the output is: \(B = 0x9e = 158\).

**Step 3: Reduce modulo 16**

\(158 \bmod 16 = 14\) → hex `e`.

**Step 4: Look up the archetype**

`e` → **Heart of All** — Unity, compassion, oneness.

The app would display:

- `B_expr = 0x9e`  
- `h_expr = e`  
- Archetype: **e – Heart of All**

You focus on the archetype; the bytes are there for curiosity and verification.

### Vowels, Consonants, and the Inner/Outer Self

We feed different slices of your name into LIBRE‑256 to get different readings:

- **Hex Expression** – full birth name. This is the complete signal—everything your name encodes.

- **Hex Soul Urge** – just the vowels (A, E, I, O, U, sometimes Y). The vowels are extracted from your name, keeping their order and their byte values, and hashed separately. "Alex Jordan" → vowels are "A", "e", "o", "a" → byte sequence [65, 101, 111, 97].

- **Hex Personality** – everything else: consonants, spaces, punctuation, digits. "Alex Jordan" → non-vowels are "l", "x", " ", "J", "r", "d", "n" → byte sequence [108, 120, 32, 74, 114, 100, 110].

Each slice produces its own byte, then its own hex digit, then its own archetype.

The logic behind this split:

- **Expression** is the full string you broadcast to the world. It is everything about your name, all at once.
- **Soul Urge** is the vowel song underneath. Vowels are the open sounds—the sounds that flow freely through an open vocal tract. They represent what flows freely through you: your desires, your inner music, your unguarded self.
- **Personality** is the consonant shell people first meet. Consonants are shaped sounds—sounds produced by obstructing airflow. They represent the structures you place between your inner world and the outer world: your persona, your presentation, your professional face.

This is not arbitrary symbolism. There is a genuine phonological distinction between vowels and consonants that maps metaphorically onto the distinction between inner experience and outer presentation. The vowels carry the melody; the consonants carry the rhythm. The vowels are the emotion; the consonants are the articulation.

### The Y Question

In English, Y is sometimes a vowel ("gym," "byte," "melody") and sometimes a consonant ("yes," "year," "you"). Traditional numerology has elaborate rules about when Y counts as a vowel.

Base 16 Numerology takes a simpler approach: the app uses a consistent rule based on phonological context. But since both the "vowel Y" and "consonant Y" versions of your name can be computed instantly, you can try both and see which reading resonates more strongly.

In practice, the difference usually changes your Soul Urge and Personality by one archetype at most—and sometimes the readings are surprisingly similar regardless. This is because LIBRE-256 distributes changes non-linearly; adding or removing a single byte can shift the result to a nearby digit or jump it across the entire range.

### Unicode, Every Alphabet, and Why Hex Wins

Traditional numerology usually assumes:

- A Latin alphabet (A–Z),  
- English spellings,  
- And fussy transliteration when it meets other languages.

If your name is Chinese, Arabic, Hindi, Russian, Japanese, etc., those tables get awkward fast. How do you assign a number to 陈? To محمد? To राम? Traditional systems require transliteration to Latin characters first, which introduces ambiguity and cultural bias.

Base 16 Numerology avoids this because we deal directly with **Unicode bytes**:

- Cyrillic, Greek, Devanagari, Kanji, Hangul, Arabic, Hebrew and more all become byte streams.  
- LIBRE‑256 doesn't care which human alphabet produced the bytes.

From the machine's perspective, everything is bytes.  
From this system's perspective, that means **every culture gets to speak in hex without translation**.

A name in Mandarin doesn't need to be "romanized" before it can be interpreted. A name in Arabic doesn't need to be stripped of its right-to-left directionality and forced into a Latin straitjacket. The bytes are the bytes, and LIBRE-256 accepts them as they are.

This is perhaps the most quietly radical feature of Base 16 Numerology: it treats every writing system as equal, because it operates at a level below writing systems—at the level of bytes, where all scripts are just patterns of numbers.

If software can encode your name, LIBRE‑256 can hash it, and Base 16 Numerology can talk about it.

### A Note on Precision and Humility

We want to be clear about what LIBRE-256 does and does not do.

It does deterministically map any byte sequence to a single byte. It does distribute outputs reasonably evenly. It does treat every input as distinct.

It does not "detect" your soul. It does not "read" your energy. It does not access any information beyond the bytes you give it.

The meaning comes from the interpretation, not from the algorithm. LIBRE-256 is a mirror—it reflects back whatever you bring to it. The profundity of your reading depends not on the quality of the hash function but on the quality of your self-reflection.

This is true of all divination systems, from the I Ching to tarot to traditional numerology. The system provides structure; you provide meaning. Base 16 Numerology just happens to provide that structure using the same tools that run your phone, your laptop, and the internet.
