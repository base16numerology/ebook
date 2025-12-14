## Chapter 3 – From Text to Hex  
### ASCII, Unicode and the LIBRE‑256 Hash

To decode your name, we have to talk about characters.

### Characters as Numbers

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

That’s ASCII. Unicode extends this idea to almost every script humans use.

Base 16 Numerology does **not** flatten this to “A = 1, B = 2”:

- `ALEX` and `alex` are different byte patterns.  
- Spaces, hyphens, apostrophes, emoji—everything with a code point—counts.

Your exact string is your exact spell.

### LIBRE‑256: The Hash with an Open‑Source Soul

To turn your name into a single byte we use **LIBRE‑256**:

> **L**ocalized  
> **I**terative  
> **B**yte  
> **R**esonance  
> **E**ncoder – 256 states.

The name “LIBRE” nods to free and open‑source culture: algorithms you can inspect, question, and fork.

Under the hood (for the curious):

1. Treat the input as a vector of bytes  
   \[
   \mathbf{x} = [x_0, x_1, \dots, x_{n-1}], \quad x_i \in \{0, \dots, 255\}.
   \]
2. Build a 4‑component state vector \(\mathbf{v}\) from rolling XORs and bit‑rotations of the bytes.  
3. Multiply by a fixed 4×4 matrix \(M\) modulo 256:
   \[
   \mathbf{y} = M \cdot \mathbf{v} \pmod{256}.
   \]
4. Collapse \(\mathbf{y}\) back into a single byte  
   \[
   B = y_0 \oplus y_1 \oplus y_2 \oplus y_3.
   \]

For non‑geeks:

> LIBRE‑256 is just the function the app uses to turn your name into a number between 0 and 255.

### From Byte to Hex Archetype

Once LIBRE‑256 gives you a byte \(B\), we compress it to a hex digit:

\[
h = B \bmod 16.
\]

- If \(B = 158\), then \(158 \bmod 16 = 14\) → hex `e`.  
- If \(B = 73\), then \(73 \bmod 16 = 9\) → hex `9`.

This `h` is your archetype digit for the string you hashed.

For your **Hex Expression**:

\[
h_{\text{expr}} = (\text{LIBRE‑256}(	ext{full birth name}) \bmod 16).
\]

The app will show something like:

- `B_expr = 0x9e`  
- `h_expr = e`  
- Archetype: **e – Heart of All**

You focus on the archetype; the bytes are there for curiosity.

### Vowels, Consonants, and the Inner/Outer Self

We feed different slices of your name into LIBRE‑256:

- **Hex Expression** – full birth name.  
- **Hex Soul Urge** – just the vowels (A, E, I, O, U, sometimes Y).  
- **Hex Personality** – everything else: consonants, spaces, punctuation.

Each slice produces its own byte, then its own hex digit, then its own archetype.

- Expression: the full string you broadcast.  
- Soul Urge: the vowel song underneath.  
- Personality: the consonant shell people first meet.

### Unicode, Every Alphabet, and Why Hex Wins

Traditional numerology usually assumes:

- A Latin alphabet (A–Z),  
- English spellings,  
- And fussy transliteration when it meets other languages.

If your name is Chinese, Arabic, Hindi, Russian, Japanese, etc., those tables get awkward fast.

Base 16 Numerology avoids this because we deal directly with **Unicode bytes**:

- Cyrillic, Greek, Devanagari, Kanji, Hangul, Arabic, Hebrew and more all become byte streams.  
- LIBRE‑256 doesn’t care which human alphabet produced the bytes.

From the machine’s perspective, everything is bytes.  
From this system’s perspective, that means **every culture gets to speak in hex without translation**.

If software can encode your name, LIBRE‑256 can hash it, and Base 16 Numerology can talk about it.
