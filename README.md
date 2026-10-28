# Qhauz Dealer Funnel

Three-step funnel for [Qhauz](https://go.qhauz.com/dealer-leads): Facebook & Instagram ads, instant lead follow-up and reporting for independent and used car dealerships.

| Step | File | Live URL on go.qhauz.com |
|---|---|---|
| 1. Landing page + survey | [`index.html`](index.html) | `/dealer-leads` |
| 2. Pick a time | [`calendar.html`](calendar.html) | `/calendar-page-119534` |
| 3. Thank you + videos | [`thank-you.html`](thank-you.html) | `/dealer-thank-you-page-157395` |

Each page is a single self-contained HTML file (fonts from Google Fonts, images embedded).

## What each page does
- **index.html**: animated landing page with the 6-question survey (questions copied exactly from the live page), SEO meta tags and structured data. On finish it links to the booking calendar with name, email and phone pre-filled. To send survey answers to GoHighLevel, set the `WEBHOOK` constant in the script to a GHL inbound-webhook URL (empty = answers are not sent anywhere).
- **calendar.html**: embeds the live GoHighLevel booking widget and passes the survey's details into it. `noindex`.
- **thank-you.html**: Jeremy's two Loom videos in a playlist, plus the next-steps checklist. `noindex`.

## Putting a page live in GoHighLevel
Sites → Funnels → Qhauz Dealer Lead Funnel → open the step → Edit → add a Custom HTML/Javascript element and paste the page code. Keep the same step URL, publish, then test on desktop and phone.

## Repository layout
```
index.html, calendar.html, thank-you.html   final pages (step 1, 2, 3)
images/                                     Jeremy's photo + video cover frames
versions/1-replica                          first rebuild of the original page
versions/2-upgraded                         upgraded page (SEO, FAQ, calculator)
versions/3-animated-redesign                final animated redesign + source
versions/4-calendar                         booking page + source
versions/5-thank-you                        thank-you page + source (body.v1.html = earlier version without video)
```
To rebuild a page from source: edit `body.html` in its folder and run `python3 build.py`.

## Before going live
Confirm with Jeremy: the "What's included" list, the example ad concepts and the FAQ answers on the landing page. The example text-message conversation is illustrative and labelled as such.
