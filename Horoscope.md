---
name: dual-zodiac-horoscope
description: Combines Chinese Lunar/Zodiac calculations with Western tropical sun sign horoscopes to deliver multi-tradition astrological insights.
---

# Dual Zodiac & Horoscope Skill

## Overview
This skill calculates a user's dual astrological profile based on their Gregorian birth date (and specific birth year lunar transition rules for the Chinese Zodiac). It merges Western tropical sun sign traits with Chinese animal sign attributes.

## Calculation Rules

### 1. Western Zodiac (Tropical)
Determine the sign based strictly on the month and day of the Gregorian birth date:
- **Capricorn**: Dec 22 – Jan 21
- **Aquarius**: Jan 22 – Feb 18
- **Pisces**: Feb 19 – Mar 20
- **Aries**: Mar 21 – Apr 19
- **Taurus**: Apr 20 – May 20
- **Gemini**: May 21 – Jun 21
- **Cancer**: Jun 22 – Jul 22
- **Leo**: Jul 23 – Aug 22
- **Virgo**: Aug 23 – Sep 22
- **Libra**: Sep 23 – Oct 22
- **Scorpio**: Oct 23 – Nov 22
- **Sagittarius**: Nov 23 – Dec 21

### 2. Chinese Zodiac (Lunar New Year Constraint)
*Crucial Rule*: If a user is born in January or early February, do not assume January 1 resets the animal sign. Check the exact Lunar New Year boundary date for that specific year (e.g., 2026 starts Feb 17, 2027 starts Feb 6). 

The 12-year animal sequence order:
1. Rat
2. Ox
3. Tiger
4. Rabbit
5. Dragon
6. Snake
7. Horse (Active for Feb 17, 2026 – Feb 5, 2027)
8. Goat / Sheep (Active for Feb 6, 2027 – Jan 25, 2028)
9. Monkey
10. Rooster
11. Dog
12. Pig

## Interaction Flow
1. **Prompt for Birth Info**: Ask the user for their birth date (Month, Day, Year).
2. **Compute Signs**: 
   - Identify Western Sun Sign and Element (Fire, Earth, Air, Water).
   - Identify Chinese Zodiac Animal and elemental year (Wood, Fire, Earth, Metal, Water).
3. **Synthesize Output**: Provide a dual synthesis showing how the inner/seasonal Western archetype interacts with the broader archetype of their Chinese birth animal.
