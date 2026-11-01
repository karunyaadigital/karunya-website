import os, urllib.parse
from art import *
from specs import *
from audit import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
WA_NUM = "916386492334"
CALL = "+917317659337"
CALL_TXT = "+91 73176 59337"
WA_TXT = "+91 63864 92334"
ADDR = "Taktakpur Road, Near Mahavir Mandir, Varanasi, Uttar Pradesh"
IG_FOUNDER = "https://www.instagram.com/bhanuhelpsdoctors/"
IG_KARUNYA = "https://www.instagram.com/karunyadigital/"
DEFAULT_MSG = "Namaste Karunya Digital, main doctor hoon. Apne clinic ki marketing ke baare mein baat karni hai."


def wa(msg=DEFAULT_MSG):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(msg)


PAGES = [("index.html", "Home"), ("services.html", "Services"), ("work.html", "Work"), ("blog.html", "Blog"), ("about.html", "About"), ("contact.html", "Contact"), ("audit.html", "Free check")]

ORIGINALS = [
    ("reelbaaz", "kc-reelbaaz", "EP 01", "Reelbaaz Doctor", "Why every doctor needs to be on social media."),
    ("nmc", "kc-nmc", "EP 02", "NMC Guidelines 2026", "The social media mistakes doctors must never make."),
    ("diwali", "kc-diwali", "EP 03", "Diwali Special", "3 marketing strategies for doctors this festive season."),
    ("why", "kc-why", "EP 04", "Why Karunya Digital?", "You heal. We get you heard."),
    ("camera", "kc-camera", "EP 05", "Scared of the camera?", "How doctors go from 'what do I say?' to confident on video."),
]


def canon(page):
    if page == "home": return ""
    if page.startswith("blog-") or page == "blog": return page + ".html"
    if page == "404": return "404.html"
    if page in SPECS: return SPECS[page]["file"]
    return page + ".html"


def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#012A5E">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="canonical" href="https://karunyadigital.online/{canon(page)}">
<meta property="og:url" content="https://karunyadigital.online/{canon(page)}">
<meta property="og:image" content="https://karunyadigital.online/assets/icon-blue-512.png">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="fonts/Waylimo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Karunya Digital","url":"https://karunyadigital.online/","description":"Healthcare marketing agency for doctors and hospitals in India: Instagram reels, Google Business Profile, SEO and doctor branding","logo":"https://karunyadigital.online/assets/icon-blue-512.png","image":"https://karunyadigital.online/assets/icon-blue-512.png","priceRange":"Rs 20,000 - Rs 40,000 per month","knowsAbout":["Social media management for doctors","Healthcare marketing","SEO for doctors","Google Business Profile","NMC advertising guidelines"],"founder":{{"@type":"Person","name":"Bhanu Pratap Rai","sameAs":"{IG_FOUNDER}"}},"sameAs":["{IG_KARUNYA}"],"telephone":"{CALL}","address":{{"@type":"PostalAddress","streetAddress":"Taktakpur Road, Near Mahavir Mandir","addressLocality":"Varanasi","addressRegion":"Uttar Pradesh","addressCountry":"IN"}},"areaServed":["Varanasi","Meerut","Lucknow","Prayagraj","Agra","Greater Noida"]}}</script>
</head>
<body class="page-{page}">
<a class="skip" href="#main">Skip to content</a>
<canvas class="trail" aria-hidden="true"></canvas>
'''


def header(active):
    def L(href, name):
        cur = ' aria-current="page"' if name == active else ''
        return f'<a class="link" href="{href}"{cur}>{name}</a>'
    spec_cur = active in [SPECS[k]["short"] for k in SPECS]
    items = ""
    for k in SPECS:
        cur = ' aria-current="page"' if SPECS[k]["short"] == active else ''
        items += f'<a href="{SPECS[k]["file"]}"{cur}>{spec_art(k, "dd-art")}<span><b>{SPECS[k]["name"]}</b><em>{plays_fmt(spec_total(k))} plays</em></span></a>'
    dcur = ' aria-current="page"' if spec_cur else ''
    dd = (f'<div class="dd"><button class="link dd-btn" type="button" aria-expanded="false" aria-controls="dd-menu"{dcur}>Specialties'
          f'<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="2" fill="none"/></svg></button>'
          f'<div class="dd-menu" id="dd-menu">{items}</div></div>')
    links = L("index.html", "Home") + dd + L("services.html", "Services") + L("work.html", "Work") + L("blog.html", "Blog") + L("about.html", "About") + L("contact.html", "Contact")
    return f'''<header class="site-header">
 <div class="wrap head-in">
  <a class="brand" href="index.html" aria-label="Karunya Digital home"><img src="assets/logo-white.png" alt="Karunya Digital" width="120" height="38"></a>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn btn-lime btn-sm" href="audit.html">Free check</a></nav>
  <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
 </div>
</header>
'''


def ig_btn(url, handle, cls="ig-btn"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{IG_ICON}<span>@{handle}</span></a>'


def footer():
    return f'''<section class="cta-band" aria-labelledby="cta-h">
 <div class="lotus-wrap">{lotus()}</div>
 <div class="wrap">
  <h2 id="cta-h">Patient aaj raat bhi search karega. Kal subah woh aapko mile.</h2>
  <p>Ek WhatsApp message bhejiye. Hum aapki speciality aur shehar dekh ke batayenge ki shuruaat kahan se karein.</p>
  <div class="cta-row" style="display:flex;flex-wrap:wrap;gap:14px">
   <a class="btn btn-lime" href="audit.html">Free profile check karein</a>
   <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{wa_icon()}WhatsApp pe baat</a>
  </div>
 </div>
</section>
<footer class="site-footer">
 <div class="f-marquee" aria-hidden="true"><div class="fm-track"><span>Aap ilaaj kijiye.</span><span class="o">Aawaaz hum banenge.</span><span>Aap ilaaj kijiye.</span><span class="o">Aawaaz hum banenge.</span><span>Aap ilaaj kijiye.</span><span class="o">Aawaaz hum banenge.</span></div></div>
 <div class="wrap">
  <div class="f-top">
   <div class="f-brand">
    <img src="assets/logo-white.png" alt="Karunya Digital" width="160" height="51">
    <p>Doctors aur hospitals ke liye social media aur marketing agency. Reels, Google Business Profile, SEO aur branding, ek hi team se.</p>
    <div class="f-live"><span class="dot"></span><span>Varanasi, <b data-clock>--:--</b> IST</span><span class="f-status" data-status></span></div>
   </div>
   <div class="f-cols">
    <div><h4>Explore</h4><ul>{"".join(f'<li><a href="{h}">{n}</a></li>' for h, n in PAGES)}</ul></div>
    <div><h4>Specialties</h4><ul>{"".join(f'<li><a href="{SPECS[k]["file"]}">{SPECS[k]["name"]}</a></li>' for k in SPECS)}</ul></div>
    <div><h4>Talk to us</h4><ul>
     <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></li>
     <li><a href="tel:{CALL}">Call {CALL_TXT}</a></li>
     <li class="addr">{ADDR}</li></ul></div>
    <div><h4>Follow</h4><ul>
     <li>{ig_btn(IG_KARUNYA, "karunyadigital", "f-ig")}</li>
     <li>{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors", "f-ig")}</li></ul>
     <button class="to-top" type="button" data-top aria-label="Back to top"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to top</button>
    </div>
   </div>
  </div>
 </div>
 <div class="f-journey"><div class="wrap"><p>Reel se reception tak. Yahi hai Karunya ka kaam.</p></div>{journey("journey jf", compact=True)}</div>
 <div class="f-bot"><div class="wrap"><span>© <span data-year>2026</span> Karunya Digital. Kashi mein, dil se banaya.</span><span>Har post doctor ki approval ke baad hi live hoti hai.</span></div></div>
</footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{wa_icon(26)}<span>WhatsApp pe baat karein</span></a>
<script src="js/main.js" defer></script>
</body>
</html>
'''


def reel(src, name, sub, auto=True, cls=""):
    return f'''<figure class="reel {cls}">
 <div class="reel-frame"><video src="media/{src}.mp4" poster="media/{src}.jpg" muted loop playsinline preload="none" {"data-auto" if auto else ""} aria-label="{name}"></video>
 <button class="sound" type="button" data-sound aria-pressed="false">{SOUND}<span>Sound on</span></button></div>
 <figcaption><b>{name}</b><span>{sub}</span></figcaption>
</figure>'''


def page_hero(h1, p):
    return f'''<section class="page-hero"><div class="wrap"><h1 class="hero-fade d1">{h1}</h1><p class="hero-fade d2">{p}</p></div>{skyline_strip()}</section>'''


def ticker():
    items = []
    for k in SPECS:
        for name, city, photo, vids, reels in SPECS[k]["doctors"]:
            if reels and reels[0][0] >= 50000:
                items.append(f'<span><b>{name}</b> {plays_fmt(reels[0][0])} plays</span>')
    row = '<span class="lab">Karunya Exclusives</span>' + "".join(items)
    return f'<div class="ticker" aria-label="Play counts of Karunya Exclusives reels"><div class="tk-track">{row}{row}</div></div>'


def originals():
    first = ORIGINALS[0]
    thumbs = "".join(
        f'<button class="og-thumb{" on" if i == 0 else ""}" type="button" data-video="media/k-{v}.mp4" data-poster="media/{c}.jpg" data-title="{t}" data-desc="{d}" data-ep="{ep}" aria-pressed="{"true" if i == 0 else "false"}">'
        f'<img src="media/{c}.jpg" alt="{t}" loading="lazy" width="540" height="960"><span><em>{ep}</em>{t}</span></button>'
        for i, (v, c, ep, t, d) in enumerate(ORIGINALS))
    return f'''<section class="sec originals" id="originals" aria-labelledby="og-h">
 <div class="og-bg" aria-hidden="true"><div class="film f1"></div><div class="film f2"></div></div>
 <div class="wrap og-grid">
  <div class="og-copy">
   <p class="og-tag rv">Karunya Originals</p>
   <h2 id="og-h" class="rv">Doctors ke liye hamari apni series.</h2>
   <p class="lead rv">Script, animation aur editing, sab in-house. Yahi quality aapke clinic ko milegi. Episode chuniye, yahin dekhiye.</p>
   <div class="og-now rv"><em data-og-ep>{first[2]}</em><b data-og-title>{first[3]}</b><span data-og-desc>{first[4]}</span></div>
   {ig_btn(IG_KARUNYA, "karunyadigital", "ig-btn rv")}
  </div>
  <div class="og-stage">
   <div class="og-phone"><div class="og-screen"><video data-og-video src="media/k-{first[0]}.mp4" poster="media/{first[1]}.jpg" playsinline preload="none" aria-label="Karunya Originals episode"></video>
    <button class="og-play" type="button" data-og-play aria-label="Play episode"><svg viewBox="0 0 24 24" width="34" height="34" aria-hidden="true"><path d="M8 5l12 7-12 7z" fill="currentColor"/></svg></button></div></div>
   <div class="og-thumbs" role="group" aria-label="Episodes">{thumbs}</div>
  </div>
 </div>
</section>'''


# verified from clients' Instagram accounts (scan of latest posts + checked top reels), 1 Nov 2026
STATS = {"plays_cr": 3.26, "reels_lakh": 44, "reels_10lakh": 8, "top": "54.73 lakh", "doctors": "50+"}


def totals_section():
    tiles = ""
    for k in SPECS:
        sp = SPECS[k]
        n = len(sp["doctors"])
        tiles += (f'<a class="spec-tile st-{k}" href="{sp["file"]}">{spec_art(k)}'
                  f'<span class="st-name">{sp["name"]}</span>'
                  f'<span class="st-num">{plays_fmt(spec_total(k))}</span><span class="st-sub">plays, best reels se</span>'
                  f'<span class="go">Dekhiye</span></a>')
    return f'''<section class="sec blue totals" id="specialties" aria-labelledby="tot-h">
 <div class="wrap">
  <p class="og-tag rv">Numbers jo khud bolte hain</p>
  <div class="tot-head">
   <p class="tot-big"><span data-count="{STATS["plays_cr"]}" data-suffix=" crore+">{STATS["plays_cr"]} crore+</span></p>
   <div>
    <h2 id="tot-h" class="rv">plays, hamare doctors ki reels pe.</h2>
    <p class="lead rv">Yeh numbers hamare clients ke Instagram accounts se seedhe liye gaye hain. Koi ads ka khel nahi, asli patients aur parivaar jo dekh rahe hain.</p>
   </div>
  </div>
  <div class="stat-row">
   <div class="stbox rv"><b data-count="{STATS["reels_lakh"]}">{STATS["reels_lakh"]}</b><span>reels ne 1 lakh+ plays cross kiye</span></div>
   <div class="stbox rv"><b data-count="{STATS["reels_10lakh"]}">{STATS["reels_10lakh"]}</b><span>reels 10 lakh+ tak pahunchi</span></div>
   <div class="stbox rv"><b>{STATS["top"]}</b><span>sabse badi single reel (Dental, Agra)</span></div>
   <div class="stbox rv"><b>{STATS["doctors"]}</b><span>doctors poore India mein</span></div>
  </div>
  <div class="spec-grid">{tiles}</div>
  <p class="spec-more">Pulmonologist, physician, paediatrician ya koi aur speciality? Hum aapke saath bhi kaam karte hain. <a href="{wa("Namaste Karunya Digital, kya aap meri speciality ke saath kaam karte hain?")}" target="_blank" rel="noopener">WhatsApp pe poochiye</a></p>
  <p class="data-note light-note">Source: clients ke public Instagram accounts, 1 November 2026. Numbers samay ke saath badalte rehte hain.</p>
 </div>
</section>'''


def bridge_section():
    return f'''<section class="sec dark bridge-sec" aria-labelledby="br-h">
 <div class="wrap">
  <h2 id="br-h" class="rv">Ek reel. Hazaron log. Ek patient aapke clinic tak.</h2>
  <p class="lead rv">Aise milta hai aaj ka patient apne doctor se: reel dekhi, share hui, shehar mein log jude, Google pe search kiya, aur seedha aapke clinic.</p>
  <div class="journey-wrap rv">{journey()}</div>
 </div>
</section>'''



PLANS = [
    ("Starter", "20,000", "Online pehchaan ki shuruaat karne wale doctors ke liye.",
     ["Instagram reels: script aur editing", "Google Business Profile management", "Mahine ka content calendar", "Har mahine report"]),
    ("Growth", "25,000", "Apne shehar mein tezi se badhne wale doctors ke liye.",
     ["Starter ka sab kuch", "Har mahine zyada reels", "NMC compliance check har post pe", "Reviews ke replies", "Doctor branding"]),
    ("Authority", "40,000", "Apni speciality ka jaana-maana naam banne ke liye.",
     ["Growth ka sab kuch", "High-end motion graphic reels", "YouTube Shorts", "Competitor analysis", "Priority support"]),
]


def pricing(compact=False):
    cards = ""
    for i, (n, p, d, f) in enumerate(PLANS):
        pop = ' pop' if i == 1 else ''
        badge = '<span class="pl-badge">Sabse popular</span>' if i == 1 else ''
        msg = f"Hello Karunya Digital, I'm interested in the {n} plan (Rs {p}/month)."
        cards += (f'<article class="plan{pop} rv">{badge}<h3>{n}</h3><p class="pl-d">{d}</p>'
                  f'<p class="pl-p"><span>Rs</span><b>{p}</b><em>/month</em></p>'
                  f'<ul>{"".join(f"<li>{x}</li>" for x in f)}</ul>'
                  f'<a class="btn {"btn-lime" if pop else "btn-line-w"}" href="{wa(msg)}" target="_blank" rel="noopener">{n} chuniye</a></article>')
    cards += (f'<article class="plan hosp rv"><h3>Full hospital marketing</h3><p class="pl-d">Multi-speciality hospital, kai doctors, poori marketing.</p>'
              f'<p class="pl-p"><b class="small">Custom plan</b></p><ul><li>Har doctor aur department</li><li>Hospital aur doctor ka brand saath</li><li>Dedicated team</li></ul>'
              f'<a class="btn btn-wa" href="tel:{CALL}">Call {CALL_TXT}</a></article>')
    return f'''<section class="sec dark pricing" id="pricing" aria-labelledby="pr-h"><div class="wrap">
 <h2 id="pr-h" class="rv">Seedhe monthly plans</h2>
 <p class="lead rv">Saaf daam, koi chhupa kharcha nahi. Exact kaam aapki speciality aur shehar ke hisaab se call pe tay hota hai.</p>
 <div class="plans">{cards}</div>
</div></section>'''


def team():
    people = [("founder", "Bhanu Pratap Rai", "Founder", "Strategy for every doctor we work with, and the voice behind @bhanuhelpsdoctors.", f'{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}'),
              ("AR", "Ankita Rai", "Manager & scripts", "Writes the scripts and runs client coordination, so every reel says the right thing in the right words.", ""),
              ("ED", "Editing team", "High-end video editors", "Editors who combine AI tools with real skill, and understand the emotion an audience should feel in every cut.", "")]
    cards = ""
    for a, n, r, d, x in people:
        av = '<img src="media/founder.webp" alt="" width="420" height="420">' if a == "founder" else f'<span>{a}</span>'
        cards += f'<article class="tm rv"><div class="tm-av">{av}</div><h3>{n}</h3><p class="tm-r">{r}</p><p>{d}</p>{x}</article>'
    return f'''<section class="sec light" aria-labelledby="tm-h"><div class="wrap">
 <h2 id="tm-h" class="rv">Aapke content ke peeche ki team</h2>
 <p class="lead rv">Chhoti, focused team. Aapko hamesha pata rahega ki aapka content kaun likh raha hai aur kaun edit kar raha hai.</p>
 <div class="team">{cards}</div>
</div></section>'''


def audit_page():
    b = audit_form()
    specs_opts = "".join(f"<option>{x}</option>" for x in ["Gynaecology", "IVF / Fertility", "Orthopaedics", "Dental", "Pulmonology", "Paediatrics", "General physician", "Hospital", "Other"])
    body = f"""<main id="main">
<section class="a-hero" aria-labelledby="ah-h">
 <div class="a-orbs" aria-hidden="true"><i></i><i></i><i></i></div>
 <div class="wrap a-hero-grid">
  <div class="a-intro">
   <p class="og-tag hero-fade d1">Free for doctors &middot; 2 minutes</p>
   <h1 id="ah-h" class="hero-fade d1">How easy is it for patients to find you?</h1>
   <p class="hero-fade d2">Get a free score for your Google profile and Instagram, with the three fixes that matter most. No call, no cost.</p>
   <div class="a-demo hero-fade d3" aria-hidden="true">
    <svg viewBox="0 0 200 200"><circle cx="100" cy="100" r="84" fill="none" stroke="rgba(176,224,230,.2)" stroke-width="14"/><circle class="demo-arc" cx="100" cy="100" r="84" fill="none" stroke="#D1FF42" stroke-width="14" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" transform="rotate(-90 100 100)"/></svg>
    <span class="demo-n">?</span>
    <span class="chip c1">Google</span><span class="chip c2">Instagram</span><span class="chip c3">Reviews</span>
   </div>
  </div>
  <form id="start" class="a-startcard hero-fade d2" novalidate>
   <h2>Start your free check</h2>
   <div><label for="s-name">Your name</label><input id="s-name" name="name" type="text" autocomplete="name" placeholder="Dr. ..."></div>
   <div><label for="s-phone">WhatsApp number</label><input id="s-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" placeholder="10-digit number"></div>
   <div class="two"><div><label for="s-spec">Speciality</label><select id="s-spec" name="speciality">{specs_opts}</select></div>
   <div><label for="s-city">City</label><input id="s-city" name="city" type="text" autocomplete="address-level2" placeholder="Varanasi"></div></div>
   <p class="s-err" role="alert"></p>
   <button class="btn btn-lime s-go" type="submit">Start my free check</button>
   <p class="hint">Your report is shared only with you on WhatsApp. No spam.</p>
  </form>
 </div>
</section>

<section class="sec light a-questions" id="questions" hidden><div class="wrap audit-grid">
 <form id="audit" class="audit" novalidate>
  <div class="a-step"><h2><span>1</span>Your Google profile</h2>{b["g"]}</div>
  <div class="a-step"><h2><span>2</span>Your Instagram</h2>{b["i"]}</div>
  <p class="a-err" role="alert"></p>
  <button class="btn btn-lime a-go" type="submit">Show my score</button>
 </form>
 <aside class="a-side" aria-live="polite">
  <div class="a-card">
   <div class="gauge"><svg viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="84" fill="none" stroke="rgba(176,224,230,.25)" stroke-width="16"/><circle class="g-arc" cx="100" cy="100" r="84" fill="none" stroke="#D1FF42" stroke-width="16" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" transform="rotate(-90 100 100)"/></svg>
    <div class="g-num"><b data-score>0</b><span>/100</span></div></div>
   <p class="a-level" data-level>Answer the questions to see your score</p>
   <div class="a-bars"><div><span>Google</span><i><em data-bar="g"></em></i><b data-sub="g">0/50</b></div><div><span>Instagram</span><i><em data-bar="i"></em></i><b data-sub="i">0/50</b></div></div>
   <p class="a-prog"><b data-answered>0</b> of 10 answered</p>
  </div>
 </aside>
</div></section>

<section class="sec dark a-result" id="result" hidden><div class="wrap">
 <p class="og-tag">Your result</p>
 <h2><span data-greet></span>, here are your top 3 fixes</h2>
 <ol class="fixes" data-fixes></ol>
 <div class="a-lead">
  <div><h3>Your report is with the Karunya team.</h3><p>We'll review your actual Google profile and Instagram and share a detailed plan with you on WhatsApp. Want to talk right now?</p></div>
  <div class="a-lead-cta"><a class="btn btn-wa" data-wa-now href="{wa()}" target="_blank" rel="noopener">{wa_icon()}Chat on WhatsApp now</a><a class="btn btn-line-w" href="services.html#pricing">See plans</a></div>
 </div>
</div></section>

<form name="free-check" data-netlify="true" netlify-honeypot="bot-field" hidden>
 <input name="bot-field"><input name="stage"><input name="name"><input name="phone"><input name="speciality"><input name="city">
 <input name="score"><input name="google_score"><input name="instagram_score"><textarea name="answers"></textarea>
</form>
</main>
"""
    return head("Free Google + Instagram check for doctors | Karunya Digital", "A free 2-minute check of your clinic's Google Business Profile and Instagram. Get a score out of 100 and your top 3 fixes.", "audit") + header("Free check") + body + footer()


def page404():
    body = f"""<main id="main" class="nf">
<section class="nf-hero">
 <div class="wrap nf-grid">
  <div>
   <p class="og-tag">Error 404</p>
   <h1>This page took a wrong turn.</h1>
   <p class="lead">Even the best rickshaw driver in Kashi gets lost in the galis sometimes. The page you're looking for doesn't exist.</p>
   <p class="nf-moral">But your clinic should never be this hard to find.</p>
   <div class="cta-row" style="display:flex;flex-wrap:wrap;gap:14px;margin-top:26px"><a class="btn btn-lime" href="index.html">Take me home</a><a class="btn btn-line-w" href="audit.html">Check how findable my clinic is</a></div>
  </div>
  <div class="nf-art">{lost_scene()}</div>
 </div>
</section>
</main>
"""
    return head("Page not found | Karunya Digital", "This page doesn't exist. Head back to Karunya Digital.", "404").replace("<meta charset=\"utf-8\">", "<meta charset=\"utf-8\">\n<base href=\"/\">\n<meta name=\"robots\" content=\"noindex\">") + header("") + body + footer()



# ------------------------------------------------------------------ BLOG
import glob, re, datetime, html as _html
import markdown as _md

CAT_ICON = {"Google Business Profile": "gmb", "Instagram": "reels", "Reels": "reels", "Meta Ads": "ads", "Branding": "brand", "Strategy": "calendar", "NMC": "calendar"}


from build_posts import load_posts


def nice_date(d):
    try:
        return datetime.date.fromisoformat(d).strftime("%-d %B %Y")
    except Exception:
        return d


def post_card(p):
    cov = f'media/blog/{p["slug"]}.jpg'
    art = f'<img src="{cov}" alt="" width="1200" height="630" loading="lazy">' if os.path.exists(os.path.join(OUT, cov)) else icon(CAT_ICON.get(p["category"], "calendar"), 200)
    return (f'<a class="pcard rv" href="{p["slug"]}.html"><div class="pc-art{" has-img" if "<img" in art else ""}">{art}</div>'
            f'<span class="pc-cat">{p["category"]}</span><h3>{_html.escape(p["title"])}</h3><p>{_html.escape(p.get("description", ""))}</p>'
            f'<span class="pc-meta">{nice_date(p.get("date", ""))} &middot; {p["minutes"]} min read</span></a>')


def blog_index(posts):
    cards = "".join(post_card(p) for p in posts) or '<p class="lead">The first articles are on their way.</p>'
    body = f"""<main id="main">
{page_hero("The Karunya blog", "Practical guides for doctors on Google, Instagram, reels and patient trust. Plain language, no jargon, always within NMC guidelines.")}
<section class="sec light"><div class="wrap"><div class="posts">{cards}</div></div></section>
</main>
"""
    return head("Blog: healthcare marketing guides for doctors | Karunya Digital", "Practical guides for doctors in India on Google Business Profile, Instagram reels, NMC rules and patient trust.", "blog") + header("Blog") + body + footer()


def blog_post(p, posts):
    others = [o for o in posts if o["slug"] != p["slug"]][:2]
    rel = "".join(post_card(o) for o in others)
    ld = ('{"@context":"https://schema.org","@type":"BlogPosting","headline":%s,"description":%s,"datePublished":"%s","author":{"@type":"Person","name":"Bhanu Pratap Rai","url":"%s"},"publisher":{"@type":"Organization","name":"Karunya Digital","logo":{"@type":"ImageObject","url":"https://karunyadigital.online/assets/icon-blue-512.png"}},"mainEntityOfPage":"https://karunyadigital.online/%s.html"}'
          % (_json_str(p["title"]), _json_str(p.get("description", "")), p.get("date", ""), IG_FOUNDER, p["slug"]))
    body = f"""<main id="main">
<section class="page-hero post-hero"><div class="wrap">
 <p class="crumb hero-fade d1"><a href="blog.html">Blog</a> / {p["category"]}</p>
 <h1 class="hero-fade d1">{_html.escape(p["title"])}</h1>
 <div class="byline hero-fade d2"><img src="media/founder.webp" alt="" width="48" height="48"><span><b>Bhanu Pratap Rai</b>{nice_date(p.get("date", ""))} &middot; {p["minutes"]} min read</span></div>
</div>{skyline_strip()}</section>
<section class="sec light"><div class="wrap post-grid">
 <article class="prose"><img class="post-cover" src="media/blog/{p["slug"]}.jpg" alt="{_html.escape(p["title"])}" width="1200" height="630">{p["html"]}</article>
 <aside class="post-side"><div class="ps-card">
  <p class="og-tag">Free for doctors</p><h3>How findable is your clinic?</h3><p>Get your Google + Instagram score and top 3 fixes in 2 minutes.</p>
  <a class="btn btn-lime" href="audit.html">Get my free check</a>
  <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{wa_icon(18)}Chat on WhatsApp</a>
 </div></aside>
</div></section>
{f'<section class="sec white"><div class="wrap"><h2 style="font-size:clamp(1.6rem,3vw,2.2rem)">Keep reading</h2><div class="posts two">{rel}</div></div></section>' if rel else ''}
</main>
"""
    h = head(f"{p['title']} | Karunya Digital", p.get("description", ""), p["slug"])
    h = h.replace('content="https://karunyadigital.online/assets/icon-blue-512.png"', f'content="https://karunyadigital.online/media/blog/{p["slug"]}.jpg"')
    h = h.replace("</head>", f'<script type="application/ld+json">{ld}</script>\n</head>')
    return h + header("Blog") + body + footer()


def _json_str(x):
    import json
    return json.dumps(x)


# ------------------------------------------------------------------ HOME
def home():
    talk = [
        ("ortho", "Mujhe camera ke saamne bolna nahi aata.",
         "Koi baat nahi. Script hum likhte hain, aapki bhasha mein. Editing aur captions hamari zimmedaari. Camera pe nahi aana? Voiceover aur motion graphics se bhi reel banti hai."),
        ("gynaec", "NMC ke rules ka darr lagta hai.",
         "Isliye hamara content patient ko samjhaane pe tika hai. Na “best doctor” jaise daave, na guarantee, na patient ki pehchaan. Har post aapki haan ke baad hi jaati hai."),
        ("pulmo", "OPD, surgery, emergency… time hi nahi hai.",
         "Aapko time dena hi nahi hai. Ek WhatsApp group, mahine ka ek calendar. Aap approve kariye, posting, replies aur report hum sambhalte hain."),
        ("ivf", "Agencies bade vaade karti hain, phir gaayab.",
         "Hum ranking ya patients ki guarantee nahi dete, kisi ke haath mein nahi hoti. Hum dete hain roz ki mehnat, har mahine ki saaf report, aur sach."),
    ]
    rows = ""
    for kind, q, a in talk:
        rows += f'''<div class="talk-row">
  <div class="say d"><span class="pre avatar-w">{avatar(kind)}</span><p class="bubble pre">“{q}”</p></div>
  <div class="say k"><img class="avatar pre" src="assets/k-blue.png" alt="" width="88" height="88"><p class="bubble pre">{a}</p></div>
 </div>'''

    svcs = [
        ("reels", "Reels & Shorts", "Script, editing, captions aur posting. Pehle 3 second mein patient ka dhyaan."),
        ("gmb", "Google Business Profile", "“Near me” search mein aapka profile poora, saaf aur bharosemand dikhe."),
        ("ads", "NMC-safe promotion", "Hospitals ke liye factual awareness campaigns, sirf jahan NMC rules allow karein."),
        ("calendar", "Content calendar & reports", "Mahine ka plan ek PDF mein. Proposals, forms aur competitor report bhi."),
        ("brand", "Doctor branding", "“Dr. Name × Karunya” logo, colours aur profile, taaki har jagah ek pehchaan."),
    ]
    svc_rows = "".join(f'''<a class="svc-row" href="services.html#{k}"><div><h3>{t}</h3><span class="go">Detail dekhein</span></div><p>{d}</p>{icon(k)}</a>''' for k, t, d in svcs)

    steps = [
        ("WhatsApp pe baat", "Aap apni speciality, shehar aur abhi kya chal raha hai, woh batate hain."),
        ("Free profile check", "2 minute ka free check kariye, ya hum aapka Google aur Instagram dekh ke saaf batate hain ki kya kam hai."),
        ("Mahine ka plan", "Content calendar PDF mein aapke paas aata hai. Aap approve karte hain ya badlaav batate hain."),
        ("Kaam hum karte hain", "Script, editing, posting aur replies roz. Mahine ke aakhir mein simple report."),
    ]
    steps_html = "".join(f'<li class="step-i"><span class="n">Kadam {i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))

    faces = [("p-manisha", "Dr. Manisha Chaudhary", "Gynaecology, Meerut"), ("p-garima", "Dr. Garima Singh", "Gynaecology, Varanasi"),
             ("p-alka", "Dr. Alka Sony Chaudhary", "Gynaecology, Siwan"), ("p-tanima", "Dr. Tanima Shukla", "Gynaecology, Lucknow"),
             ("p-tanu", "Dr. Tanu Sharma", "IVF & Fertility"), ("p-rishabh", "Dr. Rishabh Jaiswal", "Orthopaedics, Max Lucknow"),
             ("p-raman", "Dr. Raman Jindal", "Orthopaedics, Meerut"), ("p-madhuresh", "Dr. Madhuresh Kumar", "Ortho & Spine, Siwan"),
             ("p-sunaina", "Dr. Sunaina Gupta", "Dental, Agra"), ("p-neetu", "Dr. Neetu Pal", "Dental, Greater Noida"),
             ("p-vaibhav", "Dr. Vaibhav Krishna", "Pulmonology, Prayagraj")]
    faces_html = "".join(f'<figure class="face"><span class="ex-badge">Karunya Exclusive</span><img src="media/{f}.jpg" alt="{n}" width="600" height="750" loading="lazy"><figcaption><b>{n}</b>{f"<small class=deg>{DEG[n]}</small>" if n in DEG else ""}<span>{s}</span></figcaption></figure>' for f, n, s in faces)

    phone = f'''<div class="phone-x" data-phone data-state="1" aria-hidden="true">
 <div class="px-screen">
  <div class="px-status"><span>11:40</span><span>●●● 4G</span></div>
  <div class="px-s px-s1">
    <div class="px-search"><svg width="16" height="16" viewBox="0 0 24 24"><circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="2.5" fill="none"/><path d="M15 15l6 6" stroke="currentColor" stroke-width="2.5"/></svg><span data-type="gynaecologist near me"></span><i class="caret"></i></div>
    <div class="px-moon"></div>
    <p class="px-note">Pet mein dard. Raat ke 11:40. Kis doctor ke paas jaayein?</p>
  </div>
  <div class="px-s px-s2">
    <div class="px-search sm"><span>gynaecologist near me</span></div>
    <div class="px-map"><i></i><i></i><i></i></div>
    <div class="px-res"><b>Clinic A</b><em>★★★★★ 312 reviews</em><span class="ph"></span></div>
    <div class="px-res"><b>Clinic B</b><em>★★★★☆ 188 reviews</em><span class="ph"></span></div>
    <div class="px-res"><b>Clinic C</b><em>★★★★☆ 96 reviews</em><span class="ph"></span></div>
    <div class="px-res ghost"><b>Your clinic?</b><em>No photos, no reviews</em></div>
  </div>
  <div class="px-s px-s3">
    <div class="px-prof"><span class="pin"></span><div><b>Your clinic</b><em>★★★★★ · Open · 2 km</em></div></div>
    <div class="px-video"><video src="media/alka.mp4" poster="media/alka.jpg" muted loop playsinline preload="none"></video></div>
    <div class="px-btns"><span>Call</span><span>Directions</span><span>Reels</span></div>
  </div>
  <div class="px-s px-s4">
    <div class="px-chat">
     <p class="in">Namaste, kal subah appointment mil sakta hai?</p>
     <p class="out">Ji, kal subah 10 baje aa jaiye. Report saath laaiyega.</p>
     <p class="in">Dhanyavaad doctor sahab 🙏</p>
    </div>
  </div>
 </div>
</div>'''

    body = f'''<main id="main">
<section class="hero" aria-labelledby="hero-h">
 {hero_scene()}
 <div class="wrap hero-inner">
  <h1 id="hero-h" class="hero-fade d1">Achhe doctor ko dhundhna aasaan hona chahiye.</h1>
  <p class="sub hero-fade d2">Doctors aur hospitals ke liye social media aur marketing agency. Google, Instagram aur YouTube pe aapki pehchaan, aapke patient ki bhasha mein.</p>
  <div class="cta-row hero-fade d3">
   <a class="btn btn-lime" href="audit.html">Free profile check karein</a>
   <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{wa_icon()}WhatsApp pe baat</a>
  </div>
  <ul class="hero-proof hero-fade d3"><li><b>3.26 crore+</b>plays on reels</li><li><b>44</b>reels 1 lakh+ pe</li><li><b>50+</b>doctors, poore India mein</li></ul>
 </div>
</section>
{ticker()}

<section class="sec light story" id="journey" aria-labelledby="story-h">
 <div class="wrap">
  <h2 id="story-h" class="rv">Ek raat. Ek patient. Ek search.</h2>
  <p class="lead rv">Har din aapke shehar mein koi na koi isi tarah doctor dhundhta hai. Yeh kahani aapke clinic ki bhi ho sakti hai.</p>
  <div class="story-grid">
   <div class="chapters">
    <article class="chapter" data-step="1"><span class="time">Raat 11:40</span><h3>Sunita ko pet mein tez dard hai.</h3><p>Pati phone uthate hain aur likhte hain: <b>gynaecologist near me</b>. Kisi doctor ka naam nahi pata. Bas bharosa chahiye.</p></article>
    <article class="chapter" data-step="2"><span class="time">Raat 11:41</span><h3>Teen naam aate hain. Aapka nahi.</h3><p>Aap shehar ke sabse anubhavi doctor ho sakte hain. Par jiska profile khaali hai, na photo, na video, na reviews ka jawaab, woh pareshaan parivaar ke liye maujood hi nahi.</p></article>
    <article class="chapter" data-step="3"><span class="time">Agar aisa hota</span><h3>Aapka profile khud bolta.</h3><p>Saaf photos. Aapki aawaaz mein ek chhota video jo unka darr kam kare. Sahi timing, sahi number. Woh rukte, video dekhte, aur aapko call karte.</p></article>
    <article class="chapter" data-step="4"><span class="time">Agli subah</span><h3>Ek call. Ek parivaar ka bharosa.</h3><p>Yahi hamara kaam hai: aapki mehnat ko us patient tak pahunchana jise aapki zaroorat hai. Na jhoothe daave, na shor. Sirf bharosa, jo roz badhta hai.</p></article>
   </div>
   <div class="phone-col">{phone}</div>
  </div>
 </div>
</section>

{totals_section()}

{bridge_section()}

{originals()}

<section class="sec profiles-sec" aria-labelledby="reels-h">
 <div class="wrap">
  <p class="og-tag lt rv">Karunya Exclusives</p>
  <h2 id="reels-h" class="rv">Hamare doctors, Instagram pe</h2>
  <p class="lead rv">Asli doctor, asli page, asli numbers. Kisi bhi doctor pe tap karke unka profile khud dekhiye.</p>
  <div class="pf-grid">{profile_cards()}</div>
  <p class="data-note">Play counts are from Instagram (October 2026) and may change over time.</p>
 </div>
</section>

<section class="sec blue testi" aria-labelledby="testi-h">
 <div class="wrap testi-grid">
  {reel("manisha-twins", "Dr. Manisha Chaudhary, Meerut", "Normal delivery with twins, explained simply", cls="big")}
  <div>
   <h2 id="testi-h" class="rv">NMC ke naye rules? Hum pehle se ready hain.</h2>
   <blockquote class="rv">“Educate karo, advertise nahi.”</blockquote>
   <p class="rv">6 October 2026 se NMC ke naye guidelines lagu hain. Patient testimonial, “best doctor” jaise claims aur fake reviews ab mana hain. Hamari har reel patient ko samjhaane ke liye banti hai, aur doctor ki haan ke baad hi post hoti hai.</p>
   <p class="rv"><a class="btn btn-lime" href="blog-nmc-new-guidelines-doctors-social-media.html">NMC guidelines simple bhasha mein padhein</a></p>
  </div>
 </div>
</section>

<section class="sec light" aria-labelledby="talk-h">
 <div class="wrap">
  <h2 id="talk-h" class="rv">Aapke mann mein jo sawaal hain, hum jaante hain.</h2>
  <p class="lead rv">Doctors humse yeh chaar baatein sabse zyada kehte hain. Aur yeh hamara jawaab hai.</p>
  <div class="talk">{rows}</div>
 </div>
</section>


<section class="sec light duo-sec" aria-labelledby="duo-h">
 <div class="wrap">
  <p class="og-tag lt rv">Doctor &times; Karunya</p>
  <h2 id="duo-h" class="rv">Personal branding ek team game hai.</h2>
  <p class="lead rv">Social media sirf agency ke bharose nahi chalta. Patient ko doctor ka chehra, aawaaz aur bharosa chahiye. Isliye hum aapke saath ek team ki tarah kaam karte hain, aap apni jagah, hum apni jagah.</p>
  <div class="duo">
   <div class="duo-col you rv"><h3>Aapka kaam</h3><ul>
    <li>Mahine mein thoda samay shoot ke liye</li>
    <li>Patients ke asli sawaal hum tak pahunchana</li>
    <li>Camera pe apni baat, apne andaaz mein</li>
    <li>Har post ko approve karna</li></ul></div>
   <div class="duo-mid" aria-hidden="true"><b>Dr.</b><em>&times;</em><b>K</b><i></i></div>
   <div class="duo-col us rv"><h3>Hamara kaam</h3><ul>
    <li>Topic research aur script</li>
    <li>Shoot guide, editing aur captions</li>
    <li>Posting, replies aur Google profile</li>
    <li>Har mahine report aur agla plan</li></ul></div>
  </div>
  <p class="duo-note rv">Jab doctor aur team saath chalte hain, tab content mein asli bharosa dikhta hai. Wahi patient ko aapke clinic tak laata hai.</p>
 </div>
</section>

<section class="sec dark" aria-labelledby="svc-h">
 <div class="wrap">
  <h2 id="svc-h" class="rv">Ek clinic ko jo chahiye, ek hi team se.</h2>
  <div class="svc-list">{svc_rows}</div>
 </div>
</section>

<section class="sec light" aria-labelledby="proc-h">
 <div class="wrap">
  <h2 id="proc-h" class="rv">Shuruaat kaise hoti hai</h2>
  <p class="lead rv">Chaar seedhe kadam. Aapka kaam sirf pehla message aur har mahine ki approval.</p>
  <div class="process">
   <div class="road"></div><div class="road-fill"></div>
   <svg class="rick-ico" viewBox="-10 -100 160 110" aria-hidden="true">{rickshaw().replace('translate(0 666)', 'translate(0 0)')}</svg>
   <ol class="steps">{steps_html}</ol>
  </div>
 </div>
</section>

{pricing()}

<section class="sec white seo-sec" aria-labelledby="seo-h"><div class="wrap seo-grid">
 <h2 id="seo-h" class="rv">Doctors ke liye social media aur marketing agency</h2>
 <div class="rv">
  <p>Karunya Digital ek <b>healthcare marketing agency</b> hai jo sirf doctors aur hospitals ke saath kaam karti hai. Hum <b>social media management for doctors</b>, Instagram reels, Google Business Profile aur SEO sambhalte hain, NMC ke naye rules ke saath, taaki aapke shehar ke patient aapko aasaani se dhoondh sakein.</p>
  <p>Gynaecologist, IVF specialist, orthopaedic surgeon, dentist ya pulmonologist, Varanasi se Meerut, Lucknow, Agra aur Prayagraj tak, 50+ doctors aaj hamare saath hain. Sab kuch NMC guidelines ka dhyaan rakhte hue.</p>
 </div>
</div></section>

<section class="sec blue" aria-labelledby="faces-h">
 <div class="wrap">
  <p class="og-tag rv">Karunya Exclusives</p>
  <h2 id="faces-h" class="rv">50+ doctors, poore India mein, Karunya ke saath</h2>
  <div class="faces">{faces_html}</div>
  <div class="names" aria-label="More Karunya Exclusives">
   <span class="h">Prakash Hospital</span><span class="h">Kastharni Hospital</span><span class="h">Sangeeta Hospital</span>
   <span class="nm"><b>Dr. Saurabh Rai</b><small>MBBS, MS (Ortho), MRCS (A), DNB, FJIR · Orthopaedic & Trauma</small></span><span class="nm"><b>Dr. P. K. Verma</b><small>MBBS, MS, MCh (Neurosurgery) · Brain & Spine</small></span><span class="nm"><b>Dr. Shubhada Singh</b><small>MBBS, MS (Obs & Gynae) · Gynaecology</small></span><span class="nm"><b>Dr. Umesh P. Kanade</b><small>MBBS, MS (Ortho), DNB (Ortho) · Orthopaedics & Spine</small></span><span class="nm"><b>Dr. Harshit Singh</b><small>MBBS, DGO, DNB (Obs & Gynae) · Gynaecology, Darbhanga</small></span><span class="nm"><b>Dr. Tanmay Datey</b><small>MBBS, D.Ortho, DNB (Ortho), MNAMS, FISS · Orthopaedic Spine Surgeon, Amravati</small></span><span class="nm"><b>Dr. Neha Jha</b><small>MBBS, MD · Gynaecology, Darbhanga</small></span><span class="nm"><b>Dr. Nitish Gupta</b><small>MBBS, MD (Pulmonary Medicine) · Pulmonology, Agra</small></span>
  </div>
  <ul class="cities"><li>Varanasi</li><li>Meerut</li><li>Lucknow</li><li>Prayagraj</li><li>Agra</li><li>Greater Noida</li><li>Siwan</li><li>Darbhanga</li><li>Amravati</li></ul>
 </div>
</section>
</main>
'''
    return head("Karunya Digital | Social Media & Marketing Agency for Doctors in India", "Karunya Digital is a social media and marketing agency for doctors and hospitals in India: Instagram reels, Google Business Profile, SEO and doctor branding. 50+ doctor clients.", "home") + header("Home") + body + footer()


# ------------------------------------------------------------------ SPECIALTY
def spec_page(k):
    sp = SPECS[k]
    msg = f"Namaste Karunya Digital, main {sp['who']} hoon. Mere clinic ke liye reels aur marketing ke baare mein baat karni hai."
    docs = ""
    for name, city, photo, vids, reels in sp["doctors"]:
        tot = sum(p for p, _ in reels)
        img = f'<img src="media/{photo}.jpg" alt="{name}" width="600" height="750" loading="lazy">' if photo else f'<span class="mono">{name.replace("Dr. ", "")[:1]}</span>'
        pu = ig_profile(name)
        rl = f'<li><a class="doc-go" href="{pu}" target="_blank" rel="noopener">{IG_ICON}<span>Click to see profile</span></a></li>' if pu else ""
        stat = (f'<p class="dstat"><b>{plays_fmt(tot)}</b> plays, best {len(reels)} reel{"s" if len(reels) > 1 else ""}</p>' if reels
                else f'<p class="dstat"><b>{len(vids)} reels</b> hamari team ne edit kiye</p>')
        docs += f'''<article class="doc rv"><div class="doc-ph"><span class="ex-badge">Karunya Exclusive</span>{img}</div><div class="doc-body"><h3>{name}</h3>{f'<p class="deg">{DEG[name]}</p>' if name in DEG else ""}<p class="city">{city}</p>{stat}<ul class="doc-reels">{rl}</ul></div></article>'''
    topics = "".join(f'<li>{t}</li>' for t in sp["topics"])
    how = "".join(f'<div class="value"><h3>{t}</h3><p>{d}</p></div>' for t, d in sp["how"])
    others = "".join(f'<a class="other" href="{SPECS[o]["file"]}">{spec_art(o, "dd-art")}<span>{SPECS[o]["name"]}</span></a>' for o in SPECS if o != k)
    body = f'''<main id="main">
<section class="page-hero spec-hero">
 <div class="wrap spec-hero-grid">
  <div>
   <p class="crumb hero-fade d1"><a href="index.html#specialties">Specialties</a> / {sp["name"]}</p>
   <h1 class="hero-fade d1">{sp["h1"]}</h1>
   <p class="hero-fade d2">{sp["lead"]}</p>
   <div class="spec-stats hero-fade d3"><div><b data-count="{spec_total(k) / 100000:.2f}" data-suffix=" lakh">{plays_fmt(spec_total(k))}</b><span>plays, hamare {sp["short"]} doctors ki best reels pe</span></div></div>
   <div class="cta-row hero-fade d3" style="display:flex;flex-wrap:wrap;gap:14px;margin-top:26px"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon()}WhatsApp pe baat karein</a></div>
  </div>
  <div class="spec-hero-art">{spec_art(k)}</div>
 </div>
 {skyline_strip()}
</section>

<section class="sec light" aria-labelledby="sd-h"><div class="wrap">
 <p class="og-tag lt rv">Karunya Exclusives</p>
 <h2 id="sd-h" class="rv">Hamare {sp["short"]} doctors aur unke numbers</h2>
 <p class="lead rv">Kisi bhi doctor ka profile khud dekhiye. Numbers unke Instagram se hain (1 Nov 2026).</p>
 <div class="docs">{docs}</div>
</div></section>

<section class="sec reels-sec" aria-labelledby="sr-h">
 <div class="wrap"><h2 id="sr-h" class="rv">Reels jinpe patient rukte hain</h2></div>
 <div class="reel-strip">{"".join(spec_cards(k))}</div>
</section>

<section class="sec dark" aria-labelledby="st-h"><div class="wrap">
 <h2 id="st-h" class="rv">Aapke patient yeh search kar rahe hain</h2>
 <p class="lead rv">Har sawaal ek reel hai. Har reel ek naye patient tak pahunchne ka raasta.</p>
 <ul class="topics">{topics}</ul>
</div></section>

<section class="sec light" aria-labelledby="sh-h"><div class="wrap about-grid">
 <div><h2 id="sh-h" class="rv">{sp["short"]} ke liye hum alag kya karte hain</h2>
 <p class="lead rv">Har speciality ka patient alag hota hai: alag darr, alag sawaal, alag bhasha. Hamara content usi hisaab se banta hai.</p>
 <a class="btn btn-navy" style="margin-top:22px" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Mere clinic ka plan bhejiye</a></div>
 <div class="values">{how}</div>
</div></section>

<section class="sec white" aria-label="Other specialties"><div class="wrap">
 <h2 style="font-size:clamp(1.6rem,3vw,2.2rem)">Dusri specialties bhi dekhiye</h2>
 <div class="others">{others}</div>
</div></section>
</main>
'''
    return head(f"Marketing for {sp['name']} doctors | Karunya Digital", f"Instagram reels, Google Business Profile and SEO for {sp['name']} doctors. Our doctors' best reels: {plays_fmt(spec_total(k))} plays.", k) + header(sp["short"]) + body + footer()


# ------------------------------------------------------------------ SERVICES
def services():
    items = [
        ("reels", "Reels & Shorts", "For doctors who want to educate patients but have no time for cameras and editing.",
         ["Weekly topics based on real patient questions", "Hinglish ya English script: 3 second ka hook, 3 baatein, saaf call to action", "Editing, captions, music and thumbnails", "Posting on Instagram Reels and YouTube Shorts", "Camera pe nahi aana? Voiceover aur motion graphics"],
         "Har script NMC guidelines dhyaan mein rakh ke likhi jaati hai, aur aapki haan ke baad hi shoot hoti hai.", "I'd like to know more about Reels."),
        ("gmb", "Google Business Profile", "For clinics that rank low in “near me” searches or have an incomplete profile.",
         ["Complete profile: services, timings, photos, service area", "Weekly Google posts", "Review replies written in your tone", "Answers to common patient questions on your profile", "Monthly report: calls and direction requests"],
         "The honest truth: nobody can guarantee a Google ranking. We do everything that helps it, and show you the results every month.", "I'd like to know more about Google Business Profile."),
        ("ads", "NMC-safe promotion", "For hospitals that want to share factual information about departments, facilities and health camps.",
         ["A check of every post against the October 2026 NMC guidelines", "Factual hospital awareness campaigns, only where the rules allow", "Health-day and awareness content", "No testimonials, offers or “best doctor” claims", "A clear monthly report"],
         "Since 6 October 2026, ads that promote an individual doctor's practice are risky under NMC rules. We'll tell you honestly what is safe before you spend a rupee.", "I'd like to know what promotion is safe under the NMC rules."),
        ("calendar", "Content calendar & reports", "For doctors who want to know exactly what goes out this month, and when.",
         ["Monthly content calendar in a clean PDF", "Topics planned around festivals and health days", "Competitor analysis report", "Proposals, patient forms and printable material"],
         "Your calendar arrives before the month begins. Change anything you like.", "I'd like to know more about the content calendar."),
        ("brand", "Doctor branding", "For doctors with a different photo, name and colour on every platform.",
         ["“Dr. Name × Karunya” co-brand logo", "Your colours and fonts", "Instagram profile, bio and highlight covers", "A consistent look across reels and posts"],
         "A consistent identity helps patients remember you, and builds trust faster.", "I'd like to know more about doctor branding."),
    ]
    rows = ""
    for k, t, f, ticks, honest, msg in items:
        rows += f'''<article class="svc-detail" id="{k}">
 <div class="art-board">{icon(k, 360)}</div>
 <div>
  <h2>{t}</h2>
  <p class="for">{f}</p>
  <ul class="ticks">{"".join(f"<li>{x}</li>" for x in ticks)}</ul>
  <p class="honest">{honest}</p>
  <a class="btn btn-navy btn-sm" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Ask about this</a>
 </div>
</article>'''
    faq = [
        ("Kya aap NMC guidelines follow karte hain?", "Haan. Hamara content NMC ki professional conduct guidelines dhyaan mein rakh ke banta hai: patient education pehle, koi superlative daava nahi, aur bina permission patient ki pehchaan nahi. Har post aapki approval ke baad hi live hoti hai, aakhri faisla hamesha aapka."),
        ("Mujhe kitna time dena padega?", "Shuruaat mein ek call. Uske baad mahine ka calendar approve karna aur shoot ke liye thoda samay. Baaki sab hamari team sambhalti hai."),
        ("Shoot kaise hota hai?", "Hum script dete hain aur shoot ke liye saaf guide karte hain, kya bolna hai, kaise khade hona hai, kaunsi light. Uske baad editing, captions, posting aur strategy hamari team karti hai. Camera pe nahi aana chahte? Voiceover aur motion graphics se bhi reel banti hai."),
        ("Kitna kharcha aata hai?", "Plans Rs 20,000 per month se shuru hote hain. Growth Rs 25,000 aur Authority Rs 40,000. Full hospital marketing ke liye +91 73176 59337 pe call kariye, custom plan banega."),
        ("Kya aap ranking ya patients ki guarantee dete hain?", "Nahi. Jo agency guarantee deti hai, woh sach nahi bol rahi. Hum mehnat, consistency aur har mahine ki saaf report ki guarantee dete hain."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f'''<main id="main">
{page_hero("Ek clinic ko jo chahiye, sab ek jagah.", "Paanch services, ek team. Aap ilaaj pe dhyaan dijiye, patient tak pahunchne ka kaam hamara.")}
<section class="sec light"><div class="wrap">{rows}</div></section>
{pricing()}
<section class="sec white" aria-labelledby="faq-h"><div class="wrap">
 <h2 id="faq-h">Doctors yeh sawaal sabse zyada poochte hain</h2>
 <div class="faq">{faq_html}</div>
</div></section>
</main>
'''
    return head("Social Media Marketing Services for Doctors | Karunya Digital", "Social media management, Instagram reels, Google Business Profile, SEO and personal branding for doctors and hospitals. Plans from Rs 20,000/month.", "services") + header("Services") + body + footer()


# ------------------------------------------------------------------ WORK
def work():
    cal = "".join(f"<b>{d}</b>" for d in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    plan = {3: ("r", "Reel", "3 signs of PCOS"), 5: ("p", "Post", "Meet the doctor"), 8: ("s", "Story", "Q&A"), 10: ("r", "Reel", "Pregnancy diet"),
            12: ("p", "Post", "Clinic timings"), 15: ("s", "Story", "Poll"), 17: ("r", "Reel", "Normal vs C-section"), 19: ("p", "Post", "Health day"),
            22: ("s", "Story", "Patient question"), 24: ("r", "Reel", "Period myths"), 26: ("p", "Post", "Festival wishes")}
    for i in range(1, 29):
        if i in plan:
            c, t, s = plan[i]
            cal += f'<div class="{c}">{i}<small>{t}: {s}</small></div>'
        else:
            cal += f'<div>{i}</div>'
    body = f'''<main id="main">
{page_hero("Work you can see. Results you can count.", "Karunya Originals, reels for Karunya Exclusives doctors, and the formats behind every month of work.")}
{originals()}
<section class="sec profiles-sec" aria-labelledby="w0"><div class="wrap">
 <p class="og-tag lt">Karunya Exclusives</p>
 <h2 id="w0">Hamare doctors, Instagram pe</h2>
 <p class="lead">Kisi bhi doctor pe tap karke unka Instagram profile dekhiye.</p>
 <div class="pf-grid">{profile_cards()}</div>
</div></section>
<section class="sec light" aria-labelledby="w1"><div class="wrap">
 <p class="og-tag lt">Hamare edit kiye reels</p>
 <h2 id="w1">Speciality ke hisaab se reels</h2>
 <p class="lead">Speciality chuniye. Yeh video hamari team ne edit kiye hain, yahin chalte hain.</p>
 <div class="tabs" role="tablist" aria-label="Speciality">
  <button role="tab" aria-selected="true" data-tab="all">All</button>{"".join(f'<button role="tab" aria-selected="false" data-tab="{k}">{SPECS[k]["short"]} <small>{plays_fmt(spec_total(k))}</small></button>' for k in SPECS)}
 </div>
</div>
 <div class="reel-strip on-light" data-tabbed>{"".join(c for k in SPECS for c in spec_cards(k))}</div>
</section>
<section class="sec light" aria-labelledby="w3"><div class="wrap">
 <h2 id="w3">What you receive every month</h2>
 <p class="lead">These are sample formats. Topics, colours and language are different for every doctor.</p>
 <div class="mock-grid">
  <div class="mock m1"><span class="tag">Reel script</span><h3>The first 3 seconds</h3><p class="cap">A hook that stops the scroll, then 3 points, then a question.</p>
   <div class="phone"><div class="phone-in"><p class="hook">Periods late hain? Pehle yeh 3 cheezein samjhiye.</p><p class="cap-bar">Hook · 0:00 to 0:03</p><div class="bars"><i></i><i></i><i></i></div><span class="play"></span></div></div></div>
  <div class="mock m2"><span class="tag">Content calendar</span><h3>Your month, planned in one PDF</h3><p class="cap">Reels, posts and stories with dates. You approve, we publish.</p>
   <div class="cal">{cal}</div>
   <div class="legend"><span><i style="background:var(--blue)"></i>Reel</span><span><i style="background:var(--lime);border:1.5px solid var(--navy)"></i>Post</span><span><i style="background:var(--sky)"></i>Story</span></div></div>
  <div class="mock m3"><span class="tag">Google Business Profile</span><h3>Profile checklist</h3><p class="cap">The details that make patients trust a clinic.</p>
   <div class="gcard"><div class="gmap"><i></i></div><div class="gbody"><b>Your clinic</b><ul class="chk"><li>Clear photos: clinic, team, OPD</li><li>Complete services and timings</li><li>One Google post every week</li><li>A reply to every review</li><li>Answers to common questions</li></ul></div></div></div>
  <div class="mock m4"><span class="tag">Meta ad</span><h3>Reach people in your city</h3><p class="cap">A patient-awareness ad with a WhatsApp button. No false claims.</p>
   <div class="adcard"><div class="ad-top"><i></i><span><b>Your clinic</b><br>Sponsored</span></div><div class="ad-img">When should you get your thyroid tested?</div><div class="ad-foot"><span style="background:none;color:var(--navy);padding:0">Free awareness video</span><span>WhatsApp</span></div></div></div>
 </div>
</div></section>
</main>
'''
    return head("Work | Karunya Digital", "Karunya Originals, reels for our doctors by speciality, and the monthly formats behind our work.", "work") + header("Work") + body + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    values = [
        ("Healthcare only", "We don't market restaurants or showrooms. Only doctors and hospitals, so we understand your world and your patients."),
        ("Truth first", "No guarantees on rankings or patient numbers. We guarantee effort, consistency and a clear report."),
        ("The patient's language", "Simple Hinglish or English. Medical information an ordinary family can understand."),
        ("Your approval, always", "No post, reel or ad goes live without your approval. Your name, your decision."),
    ]
    vh = "".join(f'<div class="value"><h3>{t}</h3><p>{d}</p></div>' for t, d in values)
    body = f'''<main id="main">
<section class="ghat-wrap" aria-labelledby="ab-h">
 <div class="ghat-cap"><div class="wrap" style="padding-top:clamp(100px,12vw,140px)"><h1 id="ab-h" class="hero-fade d1" style="font-size:clamp(2.4rem,5vw,4.4rem);max-width:12em">Kashi ke ghaaton se, desh ke doctors ke liye.</h1></div></div>
 {ghat()}
</section>

<section class="sec light"><div class="wrap about-grid">
 <div>
  <h2 class="rv">Karunya matlab karuna.</h2>
  <p class="meaning rv">Doctor roz karuna se kaam karte hain. Hamara kaam hai ki woh karuna sahi patient tak pahunche.</p>
  <p class="rv">Karunya Digital Varanasi se chalne wali healthcare marketing agency hai. Hum poore India mein 50+ doctors aur hospitals ke saath kaam karte hain, zyadatar badhte shehron mein, jahan achhe doctor bahut hain par online unki aawaaz kam hai.</p>
  <p class="rv">Hamari team script, editing, design aur Google profile sambhalti hai, taaki doctor apna poora dhyaan patients pe de sakein.</p>
 </div>
 <div>
  <h2 class="rv" style="margin-bottom:22px">Hum kaise kaam karte hain</h2>
  <div class="values">{vh}</div>
 </div>
</div></section>

<section class="sec dark founder" aria-labelledby="fd-h"><div class="wrap founder-grid">
 <div class="f-card rv">
  <div class="f-avatar"><img src="media/founder.webp" alt="Bhanu Pratap Rai, founder of Karunya Digital" width="420" height="420"></div>
  <b>Bhanu Pratap Rai</b><span>Founder, Karunya Digital</span>
  {ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}
 </div>
 <div>
  <p class="og-tag rv">Founder se miliye</p>
  <h2 id="fd-h" class="rv">Doctors ki aawaaz banana hi hamara kaam hai.</h2>
  <p class="lead rv">Bhanu Pratap Rai ne Karunya Digital ek hi maqsad se shuru kiya: doctors aur hospitals ko un patients tak pahunchana jinhe unki zaroorat hai, imaandari se aur profession ke niyamon ke andar.</p>
  <p class="rv" style="color:var(--sky)">Apne Instagram pe Bhanu doctors ke liye social media ki kaam ki baatein share karte hain. Karunya ke page pe hamara latest kaam dikhta hai.</p>
  <div class="f-links rv">{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}{ig_btn(IG_KARUNYA, "karunyadigital")}</div>
 </div>
</div></section>

{team()}

<section class="sec white"><div class="wrap about-grid">
 <div>
  <h2 class="rv">45 second mein Karunya</h2>
  <p class="lead rv">Hamara apna ad, bilkul waise hi bana jaise hum doctors ke liye banate hain.</p>
  <h3 style="margin-top:36px;font-size:1.8rem">Hum kahan kaam karte hain</h3>
  <ul class="cities"><li>Varanasi</li><li>Meerut</li><li>Lucknow</li><li>Prayagraj</li><li>Agra</li><li>Greater Noida</li><li>Siwan</li><li>Darbhanga</li><li>Amravati</li></ul>
 </div>
 <div>{reel("karunya-ad", "Karunya Digital", "Who we are, in 45 seconds", auto=False, cls="about-reel")}</div>
</div></section>
</main>
'''
    return head("About | Karunya Digital", "Karunya Digital is a healthcare marketing agency in Varanasi, founded by Bhanu Pratap Rai. We work only with doctors and hospitals.", "about") + header("About") + body + footer()


# ------------------------------------------------------------------ CONTACT
def contact():
    needs = ["Reels", "Google profile", "SEO / website", "Content calendar", "Branding", "Not sure yet"]
    chips = "".join(f'<label><input type="checkbox" name="need" value="{n}"><span>{n}</span></label>' for n in needs)
    body = f'''<main id="main">
{page_hero("Let's talk.", "One message is enough. We'll call you, understand your practice, and suggest what's right for your clinic.")}
<section class="sec light"><div class="wrap contact-grid">
 <div>
  <a class="big-wa" href="{wa()}" target="_blank" rel="noopener"><span>The fastest way</span><strong>Send us a WhatsApp message</strong><span class="num">{wa_icon(24)}{WA_TXT}</span></a>
  <div class="info">
   <div><h3>Call</h3><p><a href="tel:{CALL}">{CALL_TXT}</a></p></div>
   <div><h3>Office</h3><p>Karunya Digital, Healthcare Marketing Agency<br>{ADDR}</p><p style="margin-top:6px"><a class="text-link" href="https://www.google.com/maps/search/?api=1&query={urllib.parse.quote('Karunya Digital Taktakpur Road Varanasi')}" target="_blank" rel="noopener">Open in Google Maps</a></p></div>
   <div><h3>Instagram</h3><p class="f-links">{ig_btn(IG_KARUNYA, "karunyadigital")}{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}</p></div>
   <div><h3>What happens next</h3><p>After your message, we call you, review your profiles and send a clear plan. No pressure.</p></div>
  </div>
 </div>
 <form class="form" id="wa-form" novalidate>
  <h2>Tell us about your practice</h2>
  <p class="hint">This form prepares your WhatsApp message. You can edit it before sending.</p>
  <div class="two">
   <div><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" placeholder="Dr. ..."></div>
   <div><label for="f-spec">Speciality</label><input id="f-spec" name="spec" type="text" placeholder="Gynaecologist, Ortho, IVF..."></div>
  </div>
  <div><label for="f-city">City</label><input id="f-city" name="city" type="text" autocomplete="address-level2" placeholder="Varanasi, Meerut, Lucknow..."></div>
  <fieldset><legend>What do you need?</legend><div class="chips">{chips}</div></fieldset>
  <div><label for="f-msg">Anything else? (optional)</label><textarea id="f-msg" name="msg" placeholder="For example: opening a new clinic, or Instagram isn't growing."></textarea></div>
  <p class="err" role="alert" style="color:var(--lime);margin:0;font-weight:700"></p>
  <button class="btn btn-wa" type="submit">{wa_icon()}Prepare WhatsApp message</button>
 </form>
</div></section>
</main>
'''
    return head("Contact | Karunya Digital", "Talk to Karunya Digital on WhatsApp or by phone. Taktakpur Road, Varanasi.", "contact") + header("Contact") + body + footer()


POSTS = load_posts()
for k in SPECS:
    open(os.path.join(OUT, SPECS[k]["file"]), "w").write(spec_page(k))
open(os.path.join(OUT, "blog.html"), "w").write(blog_index(POSTS))
for _p in POSTS:
    open(os.path.join(OUT, _p["slug"] + ".html"), "w").write(blog_post(_p, POSTS))
for fn, html in [("index.html", home()), ("audit.html", audit_page()), ("404.html", page404()), ("services.html", services()), ("work.html", work()), ("about.html", about()), ("contact.html", contact())]:
    open(os.path.join(OUT, fn), "w").write(html)
pages = [""] + [SPECS[k]["file"] for k in SPECS] + ["blog.html"] + [p["slug"] + ".html" for p in POSTS] + ["audit.html", "services.html", "work.html", "about.html", "contact.html"]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://karunyadigital.online/{p}</loc><lastmod>2026-11-01</lastmod></url>" for p in pages) + "</urlset>")
print("built")
