## Appendix A – Bytes, Nibbles, and Hex Archetypes

This appendix is for readers who want a deeper understanding of the relationship between binary data and the archetypes. It bridges the gap between the engineering reality of bytes and the symbolic practice of Base 16 Numerology.

### Bits, Nibbles, and Bytes: A Primer

At the lowest level, a computer stores information as **bits**—binary digits, each of which can be 0 or 1. Bits are grouped into larger units:

- **1 bit** → 2 possible states (0 or 1)
- **2 bits** → 4 possible states (00, 01, 10, 11)
- **3 bits** → 8 possible states
- **4 bits** → 16 possible states → this is a **nibble**
- **8 bits** → 256 possible states → this is a **byte**

A **nibble** (also spelled "nybble") is half a byte—four bits, representing a value from 0 to 15. In hexadecimal notation, a nibble is written as a single character: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, or f.

A **byte** is two nibbles—eight bits, representing a value from 0 to 255. In hexadecimal notation, a byte is written as two characters: `0x00` through `0xff`.

This is why hex is so natural for computing: every byte can be written as exactly two hex digits, and every hex digit corresponds to exactly four bits. The mapping is clean and reversible.

### From Byte to Archetype: The Modulo-16 Mapping

Any byte \(B\) produced by LIBRE‑256 lies between 0 and 255. To map that byte to an archetype, Base 16 Numerology takes:

\[
h = B \bmod 16,
\]

which yields a digit between 0 and f.

This is equivalent to taking the **lower nibble** of the byte—the rightmost hex digit when the byte is written in hex. For example:

- If \(B = 0\text{x}00 = 0\), then \(h = 0\) → **Field**.
- If \(B = 0\text{x}07 = 7\), then \(h = 7\) → **Seeker**.
- If \(B = 0\text{x}0f = 15\), then \(h = f\) → **Integrator**.
- If \(B = 0\text{x}9e = 158\), then \(h = e\) → **Heart of All**.
- If \(B = 0\text{x}ff = 255\), then \(h = f\) → **Integrator**.
- If \(B = 0\text{x}30 = 48\), then \(h = 0\) → **Field**.
- If \(B = 0\text{x}a5 = 165\), then \(h = 5\) → **Traveler**.

### The Distribution: 16 Catches per Digit

There are 256 possible byte values and 16 possible hex digits. This means exactly 16 byte values map to each digit:

- **0 (Field):** 0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240
- **1 (Spark):** 1, 17, 33, 49, 65, 81, 97, 113, 129, 145, 161, 177, 193, 209, 225, 241
- **2 (Mirror):** 2, 18, 34, 50, 66, 82, 98, 114, 130, 146, 162, 178, 194, 210, 226, 242
- ... and so on for each digit ...
- **f (Integrator):** 15, 31, 47, 63, 79, 95, 111, 127, 143, 159, 175, 191, 207, 223, 239, 255

Each archetype has an equal "catch basin" of 16 byte values. If LIBRE-256 distributes its outputs evenly across 0–255 (which testing confirms it does, approximately), then each archetype is equally likely for any given input.

This is a desirable property. It means no archetype is inherently rarer or more common than any other. Every digit has an equal chance of appearing, ensuring that the system doesn't bias toward any particular reading.

### The Upper Nibble: The Hidden Octave

When we take `mod 16`, we are extracting the lower nibble and discarding the upper nibble. But the upper nibble contains information too. The byte `0x3e` and the byte `0x9e` both reduce to `e` (Heart of All), but they differ in their upper nibble: `3` versus `9`.

Some practitioners like to note the full byte as an "extended reading." The upper nibble can be interpreted as an **octave** or **coloring** of the base archetype:

- `0x0e` → Heart of All, octave 0 (Field-colored): Compassion rooted in pure potential.
- `0x3e` → Heart of All, octave 3 (Voice-colored): Compassion expressed through communication.
- `0x7e` → Heart of All, octave 7 (Seeker-colored): Compassion deepened by inquiry.
- `0x9e` → Heart of All, octave 9 (Bridge-colored): Compassion in service of completion and release.
- `0xde` → Heart of All, octave d (Alchemist-colored): Compassion born of transformation and crisis.

This is entirely optional. The core system uses only the lower nibble. But for those who want additional nuance, the upper nibble is there—sitting in the data, waiting to be read.

The app shows both the full byte and the hex digit, allowing curious practitioners to explore the upper nibble if they wish.

### Binary Representation and Bit Patterns

For readers who think in binary, here is how the hex digits map to bit patterns:

| Hex | Binary | Archetype |
|-----|--------|-----------|
| 0 | 0000 | Field |
| 1 | 0001 | Spark |
| 2 | 0010 | Mirror |
| 3 | 0011 | Voice |
| 4 | 0100 | Foundation |
| 5 | 0101 | Traveler |
| 6 | 0110 | Hearth |
| 7 | 0111 | Seeker |
| 8 | 1000 | Sovereign |
| 9 | 1001 | Bridge |
| a | 1010 | Horizon |
| b | 1011 | Antenna |
| c | 1100 | Weaver |
| d | 1101 | Alchemist |
| e | 1110 | Heart of All |
| f | 1111 | Integrator |

Notice the structural patterns:

- **Bit 3 (the highest bit):** 0 for Physical and Emotional realms, 1 for Mental and Spiritual. This bit distinguishes the "lower" realms (body and heart) from the "upper" realms (mind and spirit).

- **Bit 2:** Together with bit 3, determines the realm. 00 = Physical, 01 = Emotional, 10 = Mental, 11 = Spiritual.

- **Bits 1 and 0:** Determine the position within the realm. 00 = Opening, 01 = Dynamic, 10 = Relational, 11 = Integrative.

This means the 4×4 matrix from Chapter 1 is literally encoded in the binary structure of the hex digits. The rows are the upper two bits; the columns are the lower two bits. The archetype system is not imposed on the binary representation—it emerges from it.

### LIBRE-256 Internals: What the Hash Actually Does

For the technically curious, here is a more detailed walkthrough of LIBRE-256's operation.

**Initialization:** The state vector \(\mathbf{v} = [v_0, v_1, v_2, v_3]\) is initialized to a fixed seed: `[0x6a, 0x09, 0xe6, 0x67]`. These values are the first four bytes of the SHA-256 initial hash value, used as a nod to the cryptographic tradition (though LIBRE-256 is not a cryptographic hash).

**Accumulation loop:** For each input byte \(x_i\):

```
v[0] ^= x_i
v[1] ^= ROL8(x_i, 3)
v[2] ^= ROL8(x_i, 5)
v[3] ^= ROL8(x_i, 7)
```

where `ROL8(x, n)` rotates the byte `x` left by `n` positions (with wraparound). This ensures that each input byte influences all four state components, and the rotations spread the influence across bit positions.

**Mixing step:** After all bytes are processed, the state is multiplied by a fixed 4×4 matrix modulo 256:

\[
M = \begin{pmatrix} 2 & 3 & 1 & 1 \\ 1 & 2 & 3 & 1 \\ 1 & 1 & 2 & 3 \\ 3 & 1 & 1 & 2 \end{pmatrix}
\]

This is a circulant matrix inspired by the MixColumns step in AES. It provides diffusion: every state byte influences every output byte.

**Collapse:** The four output bytes are XORed together to produce the final single-byte result:

\[
B = y_0 \oplus y_1 \oplus y_2 \oplus y_3.
\]

The result is a byte that depends on every input byte, with changes in any part of the input likely to produce changes in the output. This is not collision-resistant in a cryptographic sense, but it distributes well enough for symbolic purposes.

### Verification

If you want to verify that LIBRE-256 produces the results claimed in this book, the reference implementation is available on the project's GitHub repository. It is approximately 30 lines of Python, using only standard library operations (no external dependencies).

You can also implement LIBRE-256 in any language—JavaScript, C, Rust, Go, Java—and confirm that your implementation produces identical results for identical inputs. This reproducibility is by design: the algorithm is fully specified, with no hidden state, no random elements, and no platform-dependent behavior.

The app shows the raw byte and the hex digit for every computation, allowing you to verify against the reference implementation at any time.

This is the open-source soul of LIBRE-256: you don't have to trust it. You can read it, test it, and satisfy yourself.
