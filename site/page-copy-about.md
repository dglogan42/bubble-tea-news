# About — page copy

*(Auckland · Weekly Edition — eyebrow band)*

## About Bubble Tea News

Bubble Tea News is a free weekly broadsheet for Auckland's bubble tea scene — print and digital, complimentary, no subscription required. New issue every Friday.

## What's In It

Breaking neighbourhood bulletins, market research on what Auckland actually wants in its cup, a rotating cast of columnists covering everything from politics to puzzles, and a weekly ad slot for the stores that stock it. See **[ The Desk → ]** for who's writing this week.

## Where To Find It

Free at participating bubble tea stores across Auckland, and free online at bubbletea.nz. **[ Pickup locations → ]**

## A Note on Voice

All content is satire and character-voice, per each contributor's house disclaimer. Columnists write in the voice of a persona — that's the format, not a claim about who's actually behind the byline. Nothing in Bubble Tea News should be read as real news, real financial advice, real reviews of real people, or an official statement from anyone or anything referenced in it.

## Get In Touch

Want Bubble Tea News in your store, want to advertise, or just want to say hello — a short form: Name, Email, "What's this about?" (stock my store / advertise / general), Message.

Live via FormSubmit.co, posting to david_logan_nz@outlook.com — no backend needed, submissions land straight in the inbox.

---

**Notes for build:**
- The "Note on Voice" section is doing real work — it's the plain-English version of the satire/non-affiliation disclaimer that runs in the print footer every issue. Don't cut it for brevity; it's load-bearing.
- Contact form currently routes to David's personal inbox (david_logan_nz@outlook.com) — swap the `action` URL in `about.html` to a dedicated address (e.g. hello@bubbletea.nz) once the domain and a real mailbox exist.
- FormSubmit.co needs a one-time confirmation click on the *first* real submission (sent to the destination inbox) before it actually starts forwarding — test this before relying on it.
- `_captcha` is set to `false` for a one-step submit; if spam becomes a problem, flip it back to the default (adds a confirmation page after submit).
- Keep this page short. It's a credibility/orientation stop, not a landing page — most of the real pitch work happens on Home, Advertise, and Pickup Locations.
