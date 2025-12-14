## Appendix B – ASCII, Unicode, and the Secret Life of Characters

Every character in your name already has a numeric identity.

- ASCII assigns codes to basic Latin letters, digits, and punctuation.  
- Unicode extends this idea to virtually every script in use today, plus emoji and many symbols.

Base 16 Numerology uses these code points as input to LIBRE‑256.

Examples:

- `A` → 65  
- `a` → 97  
- `Ж` → `U+0416`  
- `日` → `U+65E5`  
- `😊` → `U+1F60A`

At runtime, these code points become bytes. LIBRE‑256 operates on those bytes, not on a hand‑crafted “A = 1, B = 2” table.

Because we work at the Unicode level:

- Names written in Cyrillic, Greek, Arabic, Devanagari, Kanji, Hangul, etc. can all be hashed.  
- Online handles with punctuation and emoji are also valid input.

Traditional numerology tables usually stumble as soon as you leave A–Z or need accents. Base 16 Numerology quietly follows Unicode wherever it goes. If software can encode your name, this system can listen to it in hex.
