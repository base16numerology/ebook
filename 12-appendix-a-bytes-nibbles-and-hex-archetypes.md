## Appendix A – Bytes, Nibbles, and Hex Archetypes

Any byte \(B\) produced by LIBRE‑256 lies between 0 and 255. To map that byte to an archetype, Base 16 Numerology simply takes:

\[
h = B \bmod 16,
\]

which yields a digit between 0 and f.

- If \(B = 0\), then \(h = 0\) → Field.  
- If \(B = 7\), then \(h = 7\) → Seeker.  
- If \(B = 15\) (0x0f), then \(h = f\) → Integrator.  
- If \(B = 158\) (0x9e), then \(h = 14\) → `e` → Heart of All.  
- If \(B = 255\) (0xff), then \(h = f\) again.

A **byte** is 8 bits (0–255). A **nibble** is 4 bits (0–15). Hex digits represent nibbles; bytes are often written as two hex digits (`0x00`–`0xff`).

In this system:

- LIBRE‑256 compresses your input into a byte.  
- The archetype layer cares only about the nibble, obtained via `mod 16`.

The app will show both the byte and the hex digit, but interpretation focuses on the digit and its archetype. The byte is there for anyone who enjoys seeing the raw data.
