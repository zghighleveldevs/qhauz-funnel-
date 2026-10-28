import json, html, pathlib
D = pathlib.Path(__file__).parent
body = (D / "body.html").read_text()
b64 = (D.parent / "jeremy.b64").read_text().strip()

URL = "https://go.qhauz.com/dealer-leads"
SEO_TITLE = "Facebook & Instagram Ads for Used Car Dealers | Qhauz"
SEO_DESC = ("Qhauz runs Facebook & Instagram ads for your dealership only, answers every lead in seconds "
            "and books appointments. Built by a 16-year dealership veteran. Get your store's ad plan.")

FAQ = [
 ("Who is Qhauz for?",
  "Owners and managers of independent and used car dealerships who want more of their own leads, "
  "not shared lists, and want every lead answered quickly."),
 ("Are the leads shared with other dealers?",
  "No. The ads run for your store only and are built around your inventory, people and offers, "
  "so the shoppers who respond are responding to your dealership."),
 ("How fast do leads get a response?",
  "Within seconds, day or night. Each new lead gets an instant text and email, and your team gets an alert "
  "with the lead's details."),
 ("What happens on the ad plan call?",
  "It's a 20-minute Google Meet screen share with Jeremy. You'll look at where your leads come from today, "
  "your inventory and offers, and how the ads and follow-up would run for your store."),
 ("What should I have ready for the call?",
  "Just your dealership website and a rough idea of how many more vehicles you could sell each month. "
  "If you're a manager, bring the owner if you can."),
 ("How much does it cost?",
  "It depends on your market, your goals and your ad budget. Jeremy goes through the numbers for your store on the call, "
  "so you can decide whether it's a fit."),
 ("Will my sales team see the leads?",
  "Yes. Your team gets an alert with each new lead's details the moment it comes in, and every conversation is kept in one place."),
 ("Will I know which ads produce sales?",
  "Yes. Reporting shows which ads turn into conversations, appointments, test drives and sales, so you can see what your budget is producing."),
 ("Where is Qhauz based?",
  "Qhauz is based in Lawrence, Kansas and works with independent and used car dealerships."),
]
faq_html = "\n".join(
  f'      <details><summary>{html.escape(q)}</summary><p class="a">{html.escape(a)}</p></details>' for q, a in FAQ)

CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#63b3ed" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
X = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#d27a6f" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>'

ld = {
 "@context": "https://schema.org",
 "@graph": [
  {"@type": "ProfessionalService", "@id": URL + "#org", "name": "Qhauz", "url": URL,
   "description": SEO_DESC, "telephone": "+1-913-407-7430", "email": "jeremy@qhauz.com",
   "address": {"@type": "PostalAddress", "streetAddress": "1200 E 25th St", "addressLocality": "Lawrence",
               "addressRegion": "KS", "postalCode": "66046", "addressCountry": "US"},
   "areaServed": {"@type": "Country", "name": "United States"},
   "founder": {"@type": "Person", "name": "Jeremy Pine", "jobTitle": "Founder"},
   "knowsAbout": ["Car dealership marketing", "Facebook ads for car dealers", "Instagram ads",
                  "Automotive lead generation", "CRM follow-up", "Appointment setting"]},
  {"@type": "Service", "name": "Dealer lead generation and follow-up", "provider": {"@id": URL + "#org"},
   "serviceType": "Facebook & Instagram advertising for car dealerships",
   "audience": {"@type": "BusinessAudience", "audienceType": "Independent and used car dealerships"}},
  {"@type": "WebPage", "@id": URL, "url": URL, "name": SEO_TITLE, "description": SEO_DESC,
   "inLanguage": "en-US", "about": {"@id": URL + "#org"}},
  {"@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
 ]}

fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500;1,9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">')

seo = f'''<meta name="description" content="{html.escape(SEO_DESC)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{URL}">
<meta name="theme-color" content="#0a1a33">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Qhauz">
<meta property="og:title" content="Stop Buying the Same Leads Every Other Dealer Gets | Qhauz">
<meta property="og:description" content="Ads run for your store only, so the buyers are yours. Every lead gets answered in seconds, day or night.">
<meta property="og:url" content="{URL}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Stop Buying the Same Leads Every Other Dealer Gets | Qhauz">
<meta name="twitter:description" content="Facebook & Instagram ads for your dealership only, with every lead answered in seconds.">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'''

def fill(webhook=""):
    return (body.replace("__FAQ__", faq_html).replace("__CHECK__", CHECK).replace("__X__", X)
                .replace("__JEREMY__", "data:image/jpeg;base64," + b64).replace("__WEBHOOK__", webhook))

# 1) Claude artifact (skeleton is added at publish time)
art = ('<title>Qhauz Dealer Leads</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
       + seo + "\n" + fonts + "\n" + fill())
(D / "qhauz-dealer-leads-v2.html").write_text(art)

# 2) Hosted, Google-indexable full document
hosted = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(SEO_TITLE)}</title>
{seo}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%230a1a33'/%3E%3Ctext x='16' y='23' font-family='Georgia,serif' font-weight='700' font-size='20' text-anchor='middle' fill='%23f4efe4'%3EQ%3C/text%3E%3Ccircle cx='25' cy='22' r='2.4' fill='%2363b3ed'/%3E%3C/svg%3E">
{fonts}
<style>[hidden]{{display:none!important}}</style>
</head>
<body>
{fill()}
</body>
</html>
'''
(D / "index.html").write_text(hosted)
print(len(art), len(hosted))
