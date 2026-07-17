# Subscribe — page copy

*(Auckland · Weekly Edition — eyebrow band)*

## Never Miss an Issue

New issue every Friday. One email, straight to your inbox, no spam — just a link to that week's front page the moment it's live.

**[ Email address ______ ] [ Subscribe ]**

*(No price, no account, no fine print — matches the paper's own "free, no catch" positioning throughout the rest of the site.)*

## What You'll Get

- A link to the new issue every Friday morning, print-and-digital both
- Nothing else — no other lists, no third-party sharing
- Easy out — email us any time and we'll take you off the list, no questions asked

## Prefer Paper?

Bubble Tea News is also free in print at participating stores. **[ Find a pickup location → ]**

---

**Notes for build:**
- Keep this to a single email field — no name, no extra questions. The paper's whole pitch is "free and easy to take," and the signup should match that.
- **Live via FormSubmit.co**, posting to david_logan_nz@outlook.com — same lightweight approach as the contact form, chosen deliberately over a real newsletter service (Buttondown/Mailchimp) for now. Trade-off: each signup lands as an individual email notification, not a managed list. David needs to manually collect addresses from those notifications and send the Friday email himself — no send tooling, no automated one-click unsubscribe. Copy was adjusted ("email us to unsubscribe" instead of "one click") to stay honest about that.
- Revisit with a real newsletter service once volume makes manual list-tracking painful — swap the form's `action` URL for the new service's embed endpoint once David has an account.
- Cross-link both ways with Pickup Locations, same pattern as Advertise ↔ Pickup Locations: readers who want digital go here, readers who want print go there.
