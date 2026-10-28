import pathlib, html
D=pathlib.Path(__file__).parent
body=(D/"body.html").read_text(); b64=(D.parent/"jeremy.b64").read_text().strip()
CHECK='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#63b3ed" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'
fonts=('<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;1,9..144,500;1,9..144,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap">')
why=(D/"img/why.jpg.b64").read_text().strip(); leads=(D/"img/leads.jpg.b64").read_text().strip()
def fill(embed): return (body.replace("__CHECK__",CHECK).replace("__JEREMY__","data:image/jpeg;base64,"+b64)
    .replace("__WHY__","data:image/jpeg;base64,"+why).replace("__LEADS__","data:image/jpeg;base64,"+leads)
    .replace("__EMBED__","true" if embed else "false"))
head_meta='''<meta name="description" content="Your time is reserved. Watch this short video from Jeremy before your Qhauz Dealer Growth Call.">
<meta name="robots" content="noindex, follow">
<meta name="theme-color" content="#0a1a33">'''
(D/"qhauz-thank-you.html").write_text('<title>Qhauz Thank You</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'+head_meta+"\n"+fonts+"\n"+fill(False))
(D/"thank-you.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Watch This Before Your Call | Qhauz</title>
{head_meta}
{fonts}
<style>[hidden]{{display:none!important}}</style>
</head>
<body>
{fill(True)}
</body>
</html>
''')
print("ok")
