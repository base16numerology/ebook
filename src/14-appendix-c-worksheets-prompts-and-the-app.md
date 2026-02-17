## Appendix C – Worksheets, Prompts, and the App

Because Base 16 Numerology relies on Unix timestamps and hash functions, all heavy arithmetic is delegated to the companion website and mobile app. This appendix provides worksheets, journaling prompts, and a guide to using the app effectively.

### The Companion App: Your Hex Calculator

The app handles everything computational so you can focus on interpretation. Here's what it does:

**Core Calculations:**

1. **Hex Life Path:** Enter your birth date, time, and place. The app converts to UTC, computes the Unix timestamp, runs LIBRE-256, and returns your hex digit and archetype.

2. **Hex Expression:** Enter your full birth name. The app encodes it in UTF-8, runs LIBRE-256, and returns the result.

3. **Hex Soul Urge:** The app automatically extracts vowels from your name, hashes them separately, and returns the result.

4. **Hex Personality:** The app automatically extracts consonants and other characters, hashes them, and returns the result.

5. **Hex Maturity:** Computed automatically from Life Path and Expression: `(Life Path + Expression) mod 16`.

6. **Personal Hex Years:** Enter a range of years, and the app computes the Personal Hex Year for each, based on your birthday's Unix timestamp in each year.

7. **String Hash:** Hash any string—a name, an address, a question, a project title—and see its hex digit.

**Display:**

The app shows:
- The raw byte value (e.g., `0x9e`) for verification.
- The hex digit (e.g., `e`) for quick reference.
- The archetype name and description (e.g., "Heart of All – Unity, compassion, oneness").
- The realm (e.g., "Spiritual").
- The Hex Soul Map diagram with all five core positions.

### Worksheet: My Hex Soul Map

Use this worksheet to record your core numbers. You can fill it out by hand using the app's results.

```
╔══════════════════════════════════════════════════╗
║              MY HEX SOUL MAP                     ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  Name: _______________________________________   ║
║  Birth date & time: __________________________   ║
║  Birth place: ________________________________   ║
║                                                  ║
║          ┌─────────────────────┐                 ║
║          │  EXPRESSION         │                 ║
║          │  Digit: ___         │                 ║
║          │  Archetype: _____   │                 ║
║          │  Realm: ________    │                 ║
║          └────────┬────────────┘                 ║
║                   │                              ║
║  ┌────────────┐   │   ┌────────────────┐         ║
║  │ SOUL URGE  │───┼───│  PERSONALITY   │         ║
║  │ Digit: ___ │   │   │  Digit: ___    │         ║
║  │ Arch: ____ │   │   │  Arch: _____   │         ║
║  │ Realm: ___ │   │   │  Realm: _____  │         ║
║  └────────────┘   │   └────────────────┘         ║
║                   │                              ║
║          ┌────────┴────────────┐                 ║
║          │  LIFE PATH          │                 ║
║          │  Digit: ___         │                 ║
║          │  Archetype: _____   │                 ║
║          │  Realm: ________    │                 ║
║          └────────┬────────────┘                 ║
║                   │                              ║
║          ┌────────┴────────────┐                 ║
║          │  MATURITY           │                 ║
║          │  Digit: ___         │                 ║
║          │  Archetype: _____   │                 ║
║          │  Realm: ________    │                 ║
║          └─────────────────────┘                 ║
║                                                  ║
║  Realm Summary:                                  ║
║  Physical (0-3): ___ digits                      ║
║  Emotional (4-7): ___ digits                     ║
║  Mental (8-b): ___ digits                        ║
║  Spiritual (c-f): ___ digits                     ║
║                                                  ║
║  Repeated digits: ____________________________   ║
║  Missing realms: _____________________________   ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

### Worksheet: My Narrative

After filling out your Hex Soul Map, complete these sentences:

1. **As a Life Path `___` (_______________), I'm learning to…**

   _________________________________________________________

2. **As an Expression `___` (_______________), I'm here to…**

   _________________________________________________________

3. **As a Soul Urge `___` (_______________), I secretly long to…**

   _________________________________________________________

4. **As a Personality `___` (_______________), I appear as…**

   _________________________________________________________

5. **As a Maturity `___` (_______________), I'm growing into…**

   _________________________________________________________

6. **My story title (like a novel title):**

   _________________________________________________________

7. **The tension in my map:**

   _________________________________________________________

8. **The harmony in my map:**

   _________________________________________________________

### Worksheet: Personal Hex Year Log

Use this to track the archetypal flavor of each year. Fill it in on or near each birthday.

```
╔═══════╦═══════╦════════════════╦══════════════════════════╗
║  PERSONAL HEX YEAR LOG                                    ║
╠═══════╦═══════╦════════════════╦══════════════════════════╣
║ Year  ║ Digit ║   Archetype    ║  Themes / Events / Notes ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╠═══════╬═══════╬════════════════╬══════════════════════════╣
║       ║       ║                ║                          ║
╚═══════╩═══════╩════════════════╩══════════════════════════╝
```

### Worksheet: Relationship Overlay

For comparing your Hex Soul Map with another person's:

```
╔══════════════════════════════════════════════════════════╗
║  RELATIONSHIP OVERLAY                                    ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  Person A: ________________  Person B: ________________  ║
║                                                          ║
║  Position       │ Person A    │ Person B    │ Composite  ║
║  ───────────────┼─────────────┼─────────────┼──────────  ║
║  Life Path      │ ___ (_____) │ ___ (_____) │ ___ (____) ║
║  Expression     │ ___ (_____) │ ___ (_____) │ ___ (____) ║
║  Soul Urge      │ ___ (_____) │ ___ (_____) │ ___ (____) ║
║  Personality    │ ___ (_____) │ ___ (_____) │ ___ (____) ║
║  Maturity       │ ___ (_____) │ ___ (_____) │ ___ (____) ║
║                                                          ║
║  Shared digits: _________________________________________║
║  Shared realms: _________________________________________║
║  Friction points: _______________________________________║
║  Harmony points: ________________________________________║
║                                                          ║
║  Relationship narrative:                                 ║
║  ________________________________________________________║
║  ________________________________________________________║
║  ________________________________________________________║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

### Journaling Prompts

Use these prompts for deeper exploration. You can use one per week, or pick whichever calls to you.

**Identity Prompts:**
1. My Life Path digit is `___`. Where have I seen this pattern repeating throughout my life?
2. If my Life Path archetype wrote me a letter, what would it say?
3. My Expression digit is `___`. Do I feel aligned with what my name broadcasts? Why or why not?
4. What would it look like to fully embody the high expression of my Life Path?
5. What would it look like if I fell completely into my Life Path's shadow?

**Inner/Outer Prompts:**
6. My Soul Urge says I secretly want `___`. Is this true? When did I last feel this desire?
7. My Personality says I appear as `___`. Does this match how I think people see me?
8. Is there a gap between my Soul Urge and my Personality? How does this gap show up in my daily life?
9. Who in my life sees past my Personality mask to my Soul Urge?
10. If my Personality is my armor, what is it protecting?

**Growth Prompts:**
11. My Maturity digit is `___`. Does this feel like where I'm heading? Does it excite or frighten me?
12. What would my life look like in 10 years if I fully embodied my Maturity archetype?
13. What from my Life Path do I need to release to grow into my Maturity?
14. Which realm is missing from my chart? How might I develop those qualities?
15. Which repeated digit in my chart carries the most energy right now?

**Cycle Prompts:**
16. My current Personal Hex Year is `___`. How is this archetype showing up this month?
17. Looking back, did last year's archetype describe the year accurately?
18. What does my current year's archetype invite me to do that I've been avoiding?
19. What is the shadow of my current year's archetype, and am I falling into it?
20. If my year's archetype could give me one piece of advice, what would it be?

**Relationship Prompts:**
21. My partner/friend/colleague's Life Path is `___`. How does it interact with mine?
22. Where do we harmonize? Where do we create friction?
23. What does our Composite Map say about the purpose of this relationship?
24. What archetype is missing from our combined chart, and how can we develop it together?
25. If our relationship were a hex digit, which one would it be, and why?

**Free Exploration:**
26. Hash a question that's been on your mind. What archetype does it produce? What does that suggest?
27. Hash your home address. Does the archetype match how your home feels?
28. Hash the name of a project you're working on. Does the archetype align with the project's goals?
29. Look at the 4×4 matrix of archetypes. Which corner are you most drawn to? Which do you avoid?
30. If you could choose your Life Path digit, which would you choose? Why? (And is the answer different from the one you have?)

### A Final Note

The worksheets are blank pages. The prompts are invitations. The app is a calculator.

The real tool is your attention.

Base 16 Numerology works—to whatever degree it works—because it gives you a structured reason to look at yourself carefully. The hex digits are not answers. They are questions, dressed in hexadecimal, patient enough to wait for you to engage with them.

The numbers are just an interface. The real program is your life.

Now go run it.
