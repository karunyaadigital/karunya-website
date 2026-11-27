import os, json, urllib.parse
from art import *
from specs import *
from audit import *
from team_art import TEAM, char
from home_page import street_scene, founder_art, heal_heard, ICON

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
WA_NUM = "916386492334"
CALL = "+917317659337"
CALL_TXT = "+91 73176 59337"
WA_TXT = "+91 63864 92334"
ADDR = "Taktakpur Road, Near Mahavir Mandir, Varanasi, Uttar Pradesh 221001"
IG_FOUNDER = "https://www.instagram.com/bhanuhelpsdoctors/"
IG_KARUNYA = "https://www.instagram.com/karunyadigital/"
DEFAULT_MSG = "Hello Karunya Digital, I'm a doctor and I'd like to talk about marketing for my clinic."


def wa(msg=DEFAULT_MSG):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(msg)


PAGES = [("index.html", "Home"), ("services.html", "Services"), ("work.html", "Work"), ("blog.html", "Blog"), ("game.html", "Game"), ("about.html", "About"), ("contact.html", "Contact"), ("audit.html", "Free check")]

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
    if page in ("privacy", "terms"): return page + ".html"
    if page in SPECS: return SPECS[page]["file"]
    return page + ".html"


def head(title, desc, page):
    if len(title) > 65 and " | " in title:
        short = title.rsplit(" | ", 1)[0]
        title = short if len(short) >= 30 else title
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
<meta property="og:site_name" content="Karunya Digital">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="fonts/Waylimo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","@id":"https://karunyadigital.online/#org","name":"Karunya Digital","url":"https://karunyadigital.online/","description":"Healthcare digital marketing agency in Varanasi for doctors, clinics and hospitals across India: Instagram reels, Google Business Profile, SEO and doctor branding","logo":"https://karunyadigital.online/assets/icon-blue-512.png","image":"https://karunyadigital.online/assets/icon-blue-512.png","knowsAbout":["Social media management for doctors","Healthcare marketing","SEO for doctors","Google Business Profile","NMC advertising guidelines"],"founder":{{"@type":"Person","name":"Bhanu Pratap Rai","sameAs":"{IG_FOUNDER}"}},"sameAs":["{IG_KARUNYA}"],"telephone":"{CALL}","openingHours":"Mo-Sa 10:00-19:00","address":{{"@type":"PostalAddress","streetAddress":"Taktakpur Road, Near Mahavir Mandir","addressLocality":"Varanasi","postalCode":"221001","addressRegion":"Uttar Pradesh","addressCountry":"IN"}},"areaServed":["Varanasi","Lucknow","Prayagraj","Kanpur","Gorakhpur","Meerut","Agra","Greater Noida","Patna","Uttar Pradesh","Bihar",{{"@type":"Country","name":"India"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"Karunya Digital","alternateName":["Karunya Digital Varanasi","Karunya Digital healthcare marketing agency"],"url":"https://karunyadigital.online/"}}</script>
</head>
<body class="page-{page}">
<a class="skip" href="#main">Skip to content</a>
'''


def page_ld(html, name, url, faq=None, service=None):
    """Add BreadcrumbList (+ FAQPage / Service) structured data to a page."""
    base = "https://karunyadigital.online/"
    out = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": base},
        {"@type": "ListItem", "position": 2, "name": name, "item": base + url}]}]
    if faq:
        out.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
    if service:
        out.append({"@context": "https://schema.org", "@type": "Service", "name": service, "serviceType": service, "url": base + url,
                    "provider": {"@type": "ProfessionalService", "name": "Karunya Digital", "url": base},
                    "areaServed": [{"@type": "City", "name": "Varanasi"}, {"@type": "Country", "name": "India"}],
                    "audience": {"@type": "Audience", "audienceType": "Doctors, clinics and hospitals"}})
    tags = "".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>\n' for o in out)
    return html.replace("</head>", tags + "</head>", 1)


def header(active):
    def L(href, name):
        cur = ' aria-current="page"' if name == active else ''
        return f'<a class="link" href="{href}"{cur}>{name}</a>'
    spec_cur = active in [SPECS[k]["short"] for k in SPECS]
    items = ""
    for k in SPECS:
        cur = ' aria-current="page"' if SPECS[k]["short"] == active else ''
        items += f'<a href="{SPECS[k]["file"]}"{cur}>{spec_art(k, "dd-art")}<span><b>{SPECS[k]["name"]}</b><em>{SPECS[k]["short"]}</em></span></a>'
    dcur = ' aria-current="page"' if spec_cur else ''
    dd = (f'<div class="dd"><button class="link dd-btn" type="button" aria-expanded="false" aria-controls="dd-menu"{dcur}>Specialties'
          f'<svg width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="2" fill="none"/></svg></button>'
          f'<div class="dd-menu" id="dd-menu">{items}</div></div>')
    links = L("index.html", "Home") + dd + L("services.html", "Services") + L("work.html", "Work") + L("blog.html", "Blog") + L("game.html", "Game") + L("about.html", "About") + L("contact.html", "Contact")
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


MORE_SPECS = ["Pulmonology & Chest", "Paediatrics", "Dermatology", "ENT", "General Physicians", "Neurology", "Multi-speciality Hospitals"]
CTA_WORDS = "".join(f'<span class="cw2">{w}</span>' for w in ["clinic", "hospital", "gynaecology practice", "IVF centre", "dental clinic", "ortho clinic", "nursing home", "chest clinic", "skin clinic", "child clinic"])
CTA_PINS = "".join(f'<span class="cp" style="left:{x}%;top:{y}%;--d:{i * .7:.1f}s"><i></i><em>{t}</em></span>' for i, (t, x, y) in enumerate(
    [("Clinic", 6, 22), ("Hospital", 88, 16), ("IVF centre", 78, 70), ("Dental clinic", 92, 44), ("Ortho clinic", 4, 70), ("Nursing home", 64, 88), ("Child clinic", 20, 90), ("Gynae clinic", 70, 6)]))


def popup():
    return f'''<div class="fc-pop" id="fc-pop" role="dialog" aria-modal="false" aria-labelledby="fcp-h" hidden>
 <button class="fcp-x" type="button" data-pop-close aria-label="Close">×</button>
 <div class="fcp-badge">Free · 2 minutes</div>
 <h2 id="fcp-h">How easy is it for patients to find you?</h2>
 <ul class="fcp-steps"><li><b>1</b>Answer 10 quick questions</li><li><b>2</b>Get your score out of 100</li><li><b>3</b>See your top 3 fixes</li></ul>
 <a class="btn btn-navy" href="audit.html">Check my clinic for free</a>
 <p class="fcp-note">No call, no cost. Your report comes on WhatsApp.</p>
</div>'''


GUIDE_CITIES = ["Varanasi", "Lucknow", "Prayagraj", "Patna", "Gorakhpur", "Kanpur"]


def footer_guides():
    posts = globals().get("POSTS") or []
    links = ['<a href="healthcare-marketing-agency-varanasi.html">Healthcare marketing agency in Varanasi</a>',
             '<a href="google-business-profile-management-for-doctors.html">Google Business Profile for doctors</a>',
             '<a href="instagram-reels-for-doctors.html">Instagram Reels for doctors</a>',
             '<a href="seo-services-for-doctors.html">SEO services for doctors</a>']
    links += [f'<a href="healthcare-marketing-agency-{c.lower()}.html">Healthcare marketing agency in {c}</a>' for c in ["Lucknow", "Prayagraj", "Meerut", "Patna", "Gorakhpur"]]
    for c in GUIDE_CITIES:
        m = [p for p in posts if c.lower() in p.get("keyword", "").lower()]
        m.sort(key=lambda p: (len(p.get("keyword", "")), p.get("date", "")))
        if m:
            links.append(f'<a href="{m[0]["slug"]}.html">Agency guide: {c}</a>')
    for slug, name in [("blog-digital-marketing-agency-for-doctors", "Digital marketing agency for doctors"), ("blog-hospital-marketing-agency", "Hospital marketing agency"), ("blog-digital-marketing-agency-cost-for-doctors", "Agency cost for doctors")]:
        if any(p["slug"] == slug for p in posts):
            links.append(f'<a href="{slug}.html">{name}</a>')
    if not links:
        return ""
    return f'<div class="wrap f-guides"><h4>Healthcare marketing guides</h4><p>{" · ".join(links)}</p></div>'


def footer():
    return f'''<section class="cta-band" aria-labelledby="cta-h">
 <div class="lotus-wrap">{lotus()}</div>
 <div class="cta-pins" aria-hidden="true">{CTA_PINS}</div>
 <div class="wrap">
  <h2 id="cta-h"><span class="sr">Let's make your clinic easy to find.</span><span aria-hidden="true">Let's make your</span><span class="cta-slot" aria-hidden="true">{CTA_WORDS}</span><span aria-hidden="true">easy to find.</span></h2>
  <p>Someone in your city will search tonight. One WhatsApp message, and we'll show you where to start.</p>
  <div class="cta-row" style="display:flex;flex-wrap:wrap;gap:14px">
   <a class="btn btn-lime" href="audit.html">Get a free check</a>
   <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{wa_icon()}Talk on WhatsApp</a>
  </div>
 </div>
</section>
<footer class="site-footer">
 <div class="f-marquee" aria-hidden="true"><div class="fm-track"><span>You heal.</span><span class="o">We get you heard.</span><span>You heal.</span><span class="o">We get you heard.</span><span>You heal.</span><span class="o">We get you heard.</span></div></div>
 <div class="wrap">
  <div class="f-top">
   <div class="f-brand">
    <img src="assets/logo-white.png" alt="Karunya Digital" width="160" height="51">
    <p>Social media and marketing for doctors and hospitals. Reels, Google Business Profile, SEO and branding, from one team.</p>
    <div class="f-live"><span class="dot"></span><span>Varanasi, <b data-clock>--:--</b> IST</span><span class="f-status" data-status></span></div>
   </div>
   <div class="f-cols">
    <div><h4>Explore</h4><ul>{"".join(f'<li><a href="{h}">{n}</a></li>' for h, n in PAGES)}</ul></div>
    <div><h4>Specialties</h4><ul>{"".join(f'<li><a href="{SPECS[k]["file"]}">{SPECS[k]["name"]}</a></li>' for k in SPECS)}{"".join(f'<li><a href="services.html">{n}</a></li>' for n in MORE_SPECS)}</ul></div>
    <div><h4>Talk to us</h4><ul>
     <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></li>
     <li><a href="tel:{CALL}">Call {CALL_TXT}</a></li>
     <li class="addr">{ADDR}</li><li class="addr">Mon–Sat, 10am–7pm</li></ul></div>
    <div><h4>Follow</h4><ul>
     <li>{ig_btn(IG_KARUNYA, "karunyadigital", "f-ig")}</li>
     <li>{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors", "f-ig")}</li></ul>
     <button class="to-top" type="button" data-top aria-label="Back to top"><svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>Back to top</button>
    </div>
   </div>
  </div>
 </div>
 {footer_guides()}
 <div class="f-bot"><div class="wrap"><span>© <span data-year>2026</span> Karunya Digital. Made with care in Kashi.</span><span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · Every post goes live only after the doctor's approval.</span></div></div>
</footer>
<a class="wa-float" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{wa_icon(26)}<span>Chat on WhatsApp</span></a>
{popup()}
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
            items.append(f'<span><b>{name}</b> {SPECS[k]["short"]} · {city}</span>')
    row = '<span class="lab">Karunya Exclusives</span>' + "".join(items)
    return f'<div class="ticker" aria-label="Karunya Exclusives doctors"><div class="tk-track">{row}{row}</div></div>'


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
   <h2 id="og-h" class="rv">Our own series, made for doctors.</h2>
   <p class="lead rv">Script, animation and editing, all in-house. This is the quality your clinic gets. Pick an episode and watch it here.</p>
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


# Instagram: clients' public reels, 1 Nov 2026 (3.26 Cr). Google Business Profile, 23 profiles we manage, Nov 2024 - Oct 2026:
# 9,39,426 views, 22,830 calls, 29,561 direction requests. 3.26 Cr + 0.094 Cr = 3.35 Cr views.
STATS = {"views_cr": 3.35, "calls": "52,000+", "gviews": "9.4 lakh+", "reels_lakh": 44, "doctors": "50+"}


def totals_section():
    tiles = ""
    for k in SPECS:
        sp = SPECS[k]
        n = len(sp["doctors"])
        tiles += (f'<a class="spec-tile st-{k}" href="{sp["file"]}">{spec_art(k)}'
                  f'<span class="st-name">{sp["name"]}</span>'
                  f'<span class="st-sub">Reels, Google profile and plan</span>'
                  f'<span class="go">Explore</span></a>')
    return f'''<section class="sec blue totals" id="specialties" aria-labelledby="tot-h">
 <div class="wrap">
  <p class="og-tag rv">Numbers that speak for themselves</p>
  <div class="tot-head">
   <p class="tot-big"><span data-count="{STATS["views_cr"]}" data-suffix=" crore+">{STATS["views_cr"]} crore+</span></p>
   <div>
    <h2 id="tot-h" class="rv">views of our doctors on Instagram and Google.</h2>
    <p class="lead rv">Real families in real cities, watching our doctors explain, and then calling their clinics.</p>
   </div>
  </div>
  <div class="stat-row">
   <div class="stbox rv"><b>{STATS["calls"]}</b><span>patients called or asked for directions on Google</span></div>
   <div class="stbox rv"><b>{STATS["gviews"]}</b><span>views of our doctors' Google profiles</span></div>
   <div class="stbox rv"><b data-count="{STATS["reels_lakh"]}">{STATS["reels_lakh"]}</b><span>reels crossed 1 lakh views</span></div>
   <div class="stbox rv"><b>{STATS["doctors"]}</b><span>doctors and hospitals across India</span></div>
  </div>
  <div class="spec-grid">{tiles}</div>
  <p class="spec-more">Pulmonologist, physician, paediatrician or another speciality? We work with you too. <a href="{wa("Hello Karunya Digital, do you work with my speciality?")}" target="_blank" rel="noopener">Ask on WhatsApp</a></p>
 </div>
</section>'''


def bridge_section():
    return f'''<section class="sec dark bridge-sec" aria-labelledby="br-h">
 <div class="wrap">
  <h2 id="br-h" class="rv">One reel. Thousands of people. One patient at your clinic.</h2>
  <p class="lead rv">This is how patients find doctors today: they watch a reel, share it, people in the city join in, they search on Google, and they walk into your clinic.</p>
  <div class="journey-wrap rv">{journey()}</div>
 </div>
</section>'''



def team():
    cards = ""
    for kind, n, r, d in TEAM:
        av = founder_art("fa tm-fa") if kind == "photo" else char(kind)
        link = ig_btn(IG_FOUNDER, "bhanuhelpsdoctors") if kind == "photo" else ""
        cards += f'<article class="tm2 rv"><div class="tm2-av{" ph" if kind == "photo" else ""}">{av}</div><h3>{n}</h3><p class="tm-r">{r}</p><p>{d}</p>{link}</article>'
    return f'''<section class="sec light" aria-labelledby="tm-h"><div class="wrap">
 <h2 id="tm-h" class="rv">One team. Every skill a doctor needs.</h2>
 <p class="lead rv">Strategy, scripts, editing, motion graphics, design, Google and client care, all under one roof in Varanasi.</p>
 <div class="team2">{cards}</div>
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
  <div class="a-lead-cta"><a class="btn btn-wa" data-wa-now href="{wa()}" target="_blank" rel="noopener">{wa_icon()}Chat on WhatsApp now</a><a class="btn btn-line-w" href="services.html">See our services</a></div>
 </div>
</div></section>

<form name="free-check" data-netlify="true" netlify-honeypot="bot-field" hidden>
 <input name="bot-field"><input name="stage"><input name="name"><input name="phone"><input name="speciality"><input name="city">
 <input name="score"><input name="google_score"><input name="instagram_score"><textarea name="answers"></textarea>
</form>
</main>
"""
    return head("Free Google + Instagram check for doctors | Karunya Digital", "A free 2-minute check of your clinic's Google Business Profile and Instagram. Get a score out of 100 and your top 3 fixes.", "audit") + header("Free check") + body + footer()


def game_page():
    body = f"""<main id="main">
<section class="kg-sec" aria-labelledby="kg-h">
 <div class="wrap kg-grid">
  <div class="kg-intro">
   <p class="og-tag">Karunya Games &middot; Free &middot; 4 levels</p>
   <h1 id="kg-h">Doctor Saheb <mark>Famous</mark> Kaise Bane?</h1>
   <p>A game for doctors. Take your clinic from your mohalla to all of India by catching the marketing that brings patients, and dodging the mistakes that hurt a clinic, like fake reviews and "100% cure" claims.</p>
   <ul class="kg-how">
    <li><b>1</b><span>Pick your doctor, then move left and right with your finger, mouse or arrow keys.</span></li>
    <li><b>2</b><span>Catch the white cards, avoid the red ones. Combos multiply your points up to 4x.</span></li>
    <li><b>3</b><span>Clear 4 levels: Mohalla, Shehar, Pradesh and Poora India. A quick true-or-false question follows each one.</span></li>
    <li><b>4</b><span>Grab power-ups: the lime K card, Strong Hook, Content Plan and Patient Trust.</span></li>
   </ul>
   <p class="kg-note">Every red card you catch comes with a real-life lesson at the end, based on Google's rules and the NMC guidelines for doctors.</p>
  </div>

  <div class="kg" id="kg">
   <canvas aria-label="Doctor Saheb Famous Kaise Bane game"></canvas>
   <div class="kg-hud" id="kg-hud">
    <div class="kg-row">
     <div class="kg-pill">⭐ <b id="kg-score">0</b></div>
     <div class="kg-pill" id="kg-level">L1 · Mohalla</div>
     <div class="kg-pill" id="kg-lives">❤️❤️❤️</div>
    </div>
    <div class="kg-time"><i id="kg-timefill"></i></div>
   </div>
   <div class="kg-ctrl"><button type="button" id="kg-pause" aria-label="Pause">⏸</button><button type="button" id="kg-fs" aria-label="Full screen">⛶</button><button type="button" id="kg-mute" aria-label="Sound on or off">🔊</button></div>

   <div class="kg-ov" id="kg-startScreen">
    <div class="kg-brand"><div class="kg-k"><span>K</span><i></i></div><div class="kg-wm">Karunýa<small>DIGITAL</small></div></div>
    <h2>Doctor Saheb<br><mark>Famous</mark> Kaise Bane?</h2>
    <p class="kg-sub">Mohalle se poore India tak, 4 level. Sahi marketing pakdo, galtiyon se bacho.</p>
    <div class="kg-pick" role="group" aria-label="Apna doctor chuno">
     <button type="button" data-avatar="m" aria-pressed="true"><i>👨‍⚕️</i>Dr. Saheb</button>
     <button type="button" data-avatar="f" aria-pressed="false"><i>👩‍⚕️</i>Dr. Sahiba</button>
    </div>
    <div class="kg-legend">
     <div class="kg-lg good"><h4>✅ Pakdo</h4>🎬 Reels · ⭐ Reviews<br>📍 GMB · 🔍 SEO<br>📢 Ads · 🌐 Website</div>
     <div class="kg-lg bad"><h4>❌ Bacho</h4>🤥 Fake Reviews<br>🚫 "100% Cure"<br>🙈 DM Ignore</div>
     <div class="kg-lg gold"><b>Power-ups:</b> ⚡ K card = 2x points + shield · 🧲 Strong Hook · 🗓️ Content Plan · ❤️ Patient Trust<br><b>Combo</b> banao: 5 = x2, 10 = x3, 20 = x4</div>
    </div>
    <button type="button" class="kg-btn lime" id="kg-playBtn">▶ Game Shuru Karo</button>
    <p class="kg-hint"><span id="kg-menuBest"></span><br>📱 Ungli se drag karo &nbsp;·&nbsp; 💻 Mouse ya ← → keys</p>
   </div>

   <div class="kg-ov kg-quiz" id="kg-quiz" hidden>
    <p class="kg-qtag" id="kg-qTag"></p>
    <h3>Sahi ya Galat?</h3>
    <p class="kg-qtext" id="kg-qText"></p>
    <div class="kg-row2" id="kg-qBtns">
     <button type="button" class="kg-btn lime" id="kg-qYes">✅ Sahi</button>
     <button type="button" class="kg-btn red" id="kg-qNo">❌ Galat</button>
    </div>
    <p class="kg-qres" id="kg-qRes" hidden></p>
    <button type="button" class="kg-btn lime" id="kg-qNext" hidden>Aage badho →</button>
   </div>

   <div class="kg-ov" id="kg-pauseScreen" hidden>
    <h2>Game ruka hua hai</h2>
    <p class="kg-sub">Patients intezaar kar rahe hain.</p>
    <div class="kg-row2">
     <button type="button" class="kg-btn lime" id="kg-resumeBtn">▶ Wapas Khelo</button>
     <button type="button" class="kg-btn ghost" id="kg-quitBtn">Game chhodo</button>
    </div>
   </div>

   <div class="kg-ov" id="kg-endScreen" hidden>
    <div class="kg-rank" id="kg-endTag">Aapka Rank</div>
    <div class="kg-rankname" id="kg-rankName">—</div>
    <div class="kg-stats">
     <div class="kg-stat"><b id="kg-fScore">0</b><small>Score</small></div>
     <div class="kg-stat"><b id="kg-fPatients">0</b><small>Patients</small></div>
     <div class="kg-stat"><b id="kg-fBest">0</b><small>Best</small></div>
    </div>
    <div class="kg-mini" id="kg-mini"></div>
    <div class="kg-badges" id="kg-badges"></div>
    <div class="kg-lessons" id="kg-lessons"></div>
    <p class="kg-ctaq">Game mein toh ho gaya. <b>Asli clinic</b> ko bhi famous banana hai? 👇</p>
    <a class="kg-btn wa" id="kg-waBtn" href="{wa()}" target="_blank" rel="noopener">💬 WhatsApp pe Baat Karein</a>
    <div class="kg-contact">WhatsApp: {WA_TXT} · Call: {CALL_TXT}</div>
    <div class="kg-row2">
     <button type="button" class="kg-btn lime" id="kg-againBtn">↻ Dobara Khelo</button>
     <button type="button" class="kg-btn ghost" id="kg-copyBtn">📋 Score Copy Karo</button>
    </div>
   </div>
   <div class="kg-toast" id="kg-toast"></div>
  </div>
 </div>
</section>
</main>
"""
    h = head("Free marketing game for doctors | Karunya Digital", "Doctor Saheb Famous Kaise Bane? A free 4-level game for doctors: catch Reels, Google reviews and SEO, dodge fake reviews and NMC mistakes, and earn badges.", "game")
    h = h.replace('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="css/style.css">\n<link rel="stylesheet" href="css/game.css">')
    return h + header("Game") + body + footer().replace('<script src="js/main.js" defer></script>', '<script src="js/main.js" defer></script>\n<script src="js/game.js" defer></script>')


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
    art = f'<img src="{cov}" alt="{_html.escape(p["title"], quote=True)}" width="1200" height="630" loading="lazy">' if os.path.exists(os.path.join(OUT, cov)) else icon(CAT_ICON.get(p["category"], "calendar"), 200)
    return (f'<a class="pcard rv" href="{p["slug"]}.html"><div class="pc-art{" has-img" if "<img" in art else ""}">{art}</div>'
            f'<span class="pc-cat">{p["category"]}</span><h3>{_html.escape(p["title"])}</h3><p>{_html.escape(p.get("description", ""))}</p>'
            f'<span class="pc-meta">{nice_date(p.get("date", ""))} &middot; {p["minutes"]} min read</span></a>')


def blog_index(posts):
    cards = "".join(post_card(p) for p in posts) or '<p class="lead">The first articles are on their way.</p>'
    body = f"""<main id="main">
{page_hero("The Karunya blog", "Practical guides for doctors and hospitals on choosing a healthcare marketing agency, plus Google, Instagram and the NMC rules. Plain language, no jargon.")}
<section class="sec light"><div class="wrap"><div class="posts">{cards}</div></div></section>
</main>
"""
    return head("Blog: Guides to Hiring a Healthcare Marketing Agency | Karunya Digital", "Guides for doctors and hospitals in India on choosing a digital marketing agency: costs, city guides, speciality guides and NMC rules.", "blog") + header("Blog") + body + footer()


STOP = set("a an the for in of and to vs or how what is your my with india 2026 digital marketing agency".split())


def related_posts(p, posts, n=3):
    kw = set(re.findall(r"[a-z]+", (p.get("keyword", "") + " " + p["title"]).lower())) - STOP
    scored = []
    for i, o in enumerate(posts):
        if o["slug"] == p["slug"]:
            continue
        ow = set(re.findall(r"[a-z]+", (o.get("keyword", "") + " " + o["title"]).lower())) - STOP
        scored.append((-len(kw & ow), i, o))
    scored.sort(key=lambda t: (t[0], t[1]))
    return [o for _, _, o in scored[:n]]


def faq_ld(html):
    m = re.search(r"<h2[^>]*>\s*Frequently asked questions\s*</h2>(.*?)(?=<h2|$)", html, re.S | re.I)
    if not m:
        return ""
    qa = re.findall(r"<p><strong>(.*?)</strong>\s*(?:<br\s*/?>)?\s*(.*?)</p>", m.group(1), re.S)
    items = []
    for q, a in qa:
        q = _html.unescape(re.sub("<[^>]+>", "", q)).strip()
        a = _html.unescape(re.sub("<[^>]+>", "", a)).strip()
        if q and a:
            items.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
    if not items:
        return ""
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}, ensure_ascii=False)


def blog_post(p, posts):
    others = related_posts(p, posts, 2)
    rel = "".join(post_card(o) for o in others)
    ld = ('{"@context":"https://schema.org","@type":"BlogPosting","headline":%s,"description":%s,"datePublished":"%s","author":{"@type":"Person","name":"Bhanu Pratap Rai","url":"%s"},"publisher":{"@type":"Organization","name":"Karunya Digital","logo":{"@type":"ImageObject","url":"https://karunyadigital.online/assets/icon-blue-512.png"}},"mainEntityOfPage":"https://karunyadigital.online/%s.html","image":"https://karunyadigital.online/media/blog/%s.jpg","dateModified":"%s","inLanguage":"en-IN","keywords":%s,"articleSection":%s}'
          % (_json_str(p["title"]), _json_str(p.get("description", "")), p.get("date", ""), IG_FOUNDER, p["slug"], p["slug"], p.get("date", ""), _json_str(p.get("keyword", "")), _json_str(p.get("category", ""))))
    bc = ('{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://karunyadigital.online/"},{"@type":"ListItem","position":2,"name":"Blog","item":"https://karunyadigital.online/blog.html"},{"@type":"ListItem","position":3,"name":%s,"item":"https://karunyadigital.online/%s.html"}]}'
          % (_json_str(p["title"]), p["slug"]))
    fq = faq_ld(p["html"])
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
    h = h.replace('<meta property="og:type" content="website">', f'<meta property="og:type" content="article">\n<meta property="article:published_time" content="{p.get("date", "")}">')
    extra = f'<script type="application/ld+json">{ld}</script>\n<script type="application/ld+json">{bc}</script>\n'
    if fq:
        extra += f'<script type="application/ld+json">{fq}</script>\n'
    h = h.replace("</head>", extra + "</head>")
    return h + header("Blog") + body + footer()


def _json_str(x):
    import json
    return json.dumps(x)


# ------------------------------------------------------------------ HOME
def blog_preview():
    posts = POSTS[:3]
    if not posts:
        return ""
    f0 = posts[0]
    main = (f'<a class="bp-main rv" href="{f0["slug"]}.html"><img src="media/blog/{f0["slug"]}.jpg" alt="{_html.escape(f0["title"], quote=True)}" width="1200" height="630" loading="lazy">'
            f'<span class="pc-cat">{f0["category"]} · {f0["minutes"]} min read</span><h3>{_html.escape(f0["title"])}</h3><p>{_html.escape(f0.get("description", ""))}</p></a>')
    side = "".join(f'<a class="bp-s rv" href="{p["slug"]}.html"><img src="media/blog/{p["slug"]}.jpg" alt="{_html.escape(p["title"], quote=True)}" width="1200" height="630" loading="lazy"><span><span class="pc-cat">{p["category"]}</span><b>{_html.escape(p["title"])}</b></span></a>' for p in posts[1:])
    return f'''<section class="sec light" aria-labelledby="bl-h"><div class="wrap">
 <p class="og-tag lt rv">From the blog</p>
 <h2 id="bl-h" class="rv">Guides for doctors who want to be found.</h2>
 <div class="bp">{main}<div class="bp-side">{side}</div></div>
 <p style="margin-top:26px"><a class="text-link" href="blog.html">All articles</a></p>
</div></section>'''


def home():
    talk = [
        ("ortho", "“I don't know how to talk in front of a camera.”",
         "That's fine. We write the script in your language and guide you through the shoot. Editing and captions are on us. Not comfortable on camera? Voiceover and motion graphics reels work too."),
        ("gynaec", "“I'm worried about the NMC rules.”",
         "That's why our content is built on patient education. No “best doctor” claims and no patient identities. Every post goes live only after your yes."),
        ("pulmo", "“OPD, surgery, emergencies… I have no time.”",
         "You hardly need any. One WhatsApp group and one calendar a month. You approve, we handle posting, replies and the report."),
        ("ivf", "“Agencies make big promises and then disappear.”",
         "We stay. A dedicated team, work you can see every week, and a clear report every month showing your views, calls and direction requests."),
    ]
    rows = ""
    for kind, q, a in talk:
        rows += f'''<div class="talk-row">
  <div class="say d"><span class="pre avatar-w">{avatar(kind)}</span><p class="bubble pre">{q}</p></div>
  <div class="say k"><img class="avatar pre" src="assets/k-blue.png" alt="" width="88" height="88"><p class="bubble pre">{a}</p></div>
 </div>'''

    svcs = [
        ("reels", "Reels & Shorts", "Script, shoot guidance, editing, captions and posting. Patients hooked in the first 3 seconds."),
        ("gmb", "Google Business Profile", "A complete, clear and trusted profile when someone searches “near me”."),
        ("ads", "NMC-safe promotion", "Factual awareness campaigns for hospitals, only where the NMC rules allow."),
        ("calendar", "Content calendar & reports", "Your month planned in one PDF, plus proposals, forms and competitor reports."),
        ("brand", "Doctor branding", "Your colours, profile and look, consistent on every platform."),
    ]
    svc_rows = "".join(f'''<a class="svc-row" href="services.html#{k}"><div><h3>{t}</h3><span class="go">See details</span></div><p>{d}</p>{icon(k)}</a>''' for k, t, d in svcs)

    steps = [
        ("Message us on WhatsApp", "Tell us your speciality, your city and what's happening right now."),
        ("Free profile check", "Take the 2-minute free check, or we review your Google and Instagram and tell you clearly what's missing."),
        ("Your monthly plan", "Your content calendar arrives as a PDF. You approve it or tell us what to change."),
        ("We do the work", "Scripts, editing, posting and replies every day. A simple report at the end of the month."),
    ]
    steps_html = "".join(f'<li class="step-i"><span class="n">Step {i + 1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(steps))

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
    <p class="px-note">Stomach pain. 11:40 at night. Which doctor should we go to?</p>
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
     <p class="in">Hello, can I get an appointment tomorrow morning?</p>
     <p class="out">Yes, please come at 10 am. Bring your reports.</p>
     <p class="in">Thank you, doctor 🙏</p>
    </div>
  </div>
 </div>
</div>'''

    body = f'''<main id="main">
<section class="hero" aria-labelledby="hero-h">
 {street_scene()}
 <div class="h3-chips" aria-hidden="true">
  <span class="pill2 q1">{ICON["follow"]}New follower from Varanasi</span>
  <span class="pill2 q2">{ICON["heart"]}2,431 likes on today's reel</span>
  <span class="pill2 q3">{ICON["pin"]}Directions requested</span>
 </div>
 <div class="h3-time" aria-hidden="true"><span class="tt"><b>6:00 pm</b>Saw your reel</span><span class="ta"></span><span class="tt"><b>6:15 pm</b>At your clinic</span></div>
 <div class="wrap hero-inner">
  <h1 id="hero-h" class="hero-fade d1">A good doctor should be <span class="hl">easy to find.</span></h1>
  <p class="sub hero-fade d2">A <a href="healthcare-marketing-agency-varanasi.html" style="color:inherit;text-decoration:underline;text-underline-offset:3px">healthcare digital marketing agency in Varanasi</a> for doctors and hospitals across India. Your name on Google, Instagram and YouTube, in your patients' language.</p>
  <div class="cta-row hero-fade d3">
   <a class="btn btn-lime" href="audit.html">Get a free check</a>
   <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener">{wa_icon()}WhatsApp us</a>
  </div>
  <ul class="hero-proof hero-fade d3"><li><b>3.35 crore+</b>views on Instagram & Google</li><li><b>52,000+</b>patients called or asked for directions</li><li><b>50+</b>doctors across India</li></ul>
 </div>
</section>
{ticker()}

<section class="sec dark premiere" aria-labelledby="ad-h">
 <div class="pm-glow" aria-hidden="true"></div>
 <div class="wrap pm-grid">
  <div class="pm-copy">
   <p class="og-tag rv">Now showing</p>
   <h2 id="ad-h" class="rv">Karunya Digital in 45 seconds.</h2>
   <p class="lead rv">Made exactly the way we make reels for our doctors: a clear hook, a simple story and a reason to act. Tap “Sound on”.</p>
   <a class="btn btn-lime rv" style="margin-top:26px" href="{wa("Hello Karunya Digital, I'd like a reel like your 45-second video for my clinic.")}" target="_blank" rel="noopener">{wa_icon(18)}Make one like this for me</a>
  </div>
  <div class="pm-stage rv">
   <span class="pm-ring r1" aria-hidden="true"></span><span class="pm-ring r2" aria-hidden="true"></span>
   {reel("karunya-ad", "Karunya Digital in 45 seconds", "Made the way we make reels for doctors", cls="pm-reel")}
  </div>
  <ol class="pm-beats" aria-label="How every Karunya reel is built">
   <li class="rv"><b>01</b><div><h3>The hook</h3><p>The first three seconds. One line that makes a patient stop scrolling.</p></div></li>
   <li class="rv"><b>02</b><div><h3>The story</h3><p>One real question, answered simply, in the language your patients speak.</p></div></li>
   <li class="rv"><b>03</b><div><h3>The reason to act</h3><p>A clear next step, so the right patient knows how to reach you.</p></div></li>
  </ol>
 </div>
</section>

<section class="sec light story" id="journey" aria-labelledby="story-h">
 <div class="wrap">
  <h2 id="story-h" class="rv">One night. One patient. One search.</h2>
  <p class="lead rv">Every day, someone in your city looks for a doctor exactly like this. This story could be about your clinic.</p>
  <div class="story-grid">
   <div class="chapters">
    <article class="chapter" data-step="1"><span class="time">11:40 pm</span><h3>Sunita has sharp stomach pain.</h3><p>Her husband picks up his phone and types: <b>gynaecologist near me</b>. They don't know any doctor's name. They just need someone they can trust.</p></article>
    <article class="chapter" data-step="2"><span class="time">11:41 pm</span><h3>Three names appear. Yours isn't one of them.</h3><p>You may be the most experienced doctor in the city. But a profile with no photos, no videos and no review replies simply doesn't exist for a worried family.</p></article>
    <article class="chapter" data-step="3"><span class="time">What if</span><h3>Your profile spoke for you.</h3><p>Clear photos. A short video in your voice that eases their fear. The right timings and number. They stop, watch, and call you.</p></article>
    <article class="chapter" data-step="4"><span class="time">Next morning</span><h3>One call. One family's trust.</h3><p>That is our job: bringing your work to the patient who needs you. No false claims, no noise. Just trust that grows every day.</p></article>
   </div>
   <div class="phone-col">{phone}</div>
  </div>
 </div>
</section>

{totals_section()}

{bridge_section()}

<section class="sec dark hh-sec" aria-labelledby="hh-h"><div class="wrap">
 <p class="og-tag rv" style="justify-content:center">What we do</p>
 <h2 id="hh-h" class="rv">Your care, heard across your city.</h2>
 <div class="bm2">{heal_heard()}</div>
 <p class="bm2-p rv">Your care is the heartbeat. We turn it into reels and a Google profile that reach the families in your city who need you.</p>
</div></section>

{originals()}

<section class="sec profiles-sec" aria-labelledby="reels-h">
 <div class="wrap">
  <p class="og-tag lt rv">Karunya Exclusives</p>
  <h2 id="reels-h" class="rv">The doctors who trust us</h2>
  <p class="lead rv">Real doctors, real pages. Tap any doctor to see their Instagram.</p>
  <div class="pf-grid">{profile_cards()}</div>
 </div>
</section>

<section class="sec blue more-docs" aria-labelledby="faces-h">
 <div class="wrap">
  <p class="og-tag rv">50+ doctors work with us</p>
  <h2 id="faces-h" class="rv">And many more doctors and hospitals, in 9 cities.</h2>
    <div class="names" aria-label="More Karunya Exclusives">
   <span class="h">Prakash Hospital</span><span class="h">Kastharni Hospital</span><span class="h">Sangeeta Hospital</span>
   <span class="nm"><b>Dr. Neetu Pal</b><small>BDS, MDS · Dental, Greater Noida</small></span><span class="nm"><b>Dr. Vaibhav Krishna</b><small>MBBS, MD (Respiratory Medicine) · Pulmonology, Prayagraj</small></span><span class="nm"><b>Dr. Saurabh Rai</b><small>MBBS, MS (Ortho), MRCS (A), DNB, FJIR · Orthopaedic & Trauma</small></span><span class="nm"><b>Dr. P. K. Verma</b><small>MBBS, MS, MCh (Neurosurgery) · Brain & Spine</small></span><span class="nm"><b>Dr. Shubhada Singh</b><small>MBBS, MS (Obs & Gynae) · Gynaecology</small></span><span class="nm"><b>Dr. Umesh P. Kanade</b><small>MBBS, MS (Ortho), DNB (Ortho) · Orthopaedics & Spine</small></span><span class="nm"><b>Dr. Harshit Singh</b><small>MBBS, DGO, DNB (Obs & Gynae) · Gynaecology, Darbhanga</small></span><span class="nm"><b>Dr. Tanmay Datey</b><small>MBBS, D.Ortho, DNB (Ortho), MNAMS, FISS · Orthopaedic Spine Surgeon, Amravati</small></span><span class="nm"><b>Dr. Neha Jha</b><small>MBBS, MD · Gynaecology, Darbhanga</small></span><span class="nm"><b>Dr. Nitish Gupta</b><small>MBBS, MD (Pulmonary Medicine) · Pulmonology, Agra</small></span>
  </div>
  <ul class="cities"><li>Varanasi</li><li>Meerut</li><li>Lucknow</li><li>Prayagraj</li><li>Agra</li><li>Greater Noida</li><li>Siwan</li><li>Darbhanga</li><li>Amravati</li></ul>
 </div>
</section>

<section class="sec blue testi" aria-labelledby="testi-h">
 <div class="wrap testi-grid">
  {reel("manisha-twins", "Dr. Manisha Chaudhary, Meerut", "Normal delivery with twins, explained simply", cls="big")}
  <div>
   <h2 id="testi-h" class="rv">New NMC rules? We already follow them.</h2>
   <blockquote class="rv">“Educate, don't advertise.”</blockquote>
   <p class="rv">The NMC's new guidelines apply from 6 October 2026. Patient testimonials, “best doctor” claims and fake reviews are now banned. Every reel we make educates patients, and goes live only after the doctor says yes.</p>
   <p class="rv"><a class="btn btn-lime" href="blog-nmc-new-guidelines-doctors-social-media.html">Read the NMC guidelines, simply explained</a></p>
  </div>
 </div>
</section>

<section class="sec light" aria-labelledby="talk-h">
 <div class="wrap">
  <h2 id="talk-h" class="rv">We know what you're thinking.</h2>
  <p class="lead rv">Doctors tell us these four things most often. Here's our answer.</p>
  <div class="talk">{rows}</div>
 </div>
</section>


<section class="sec light duo-sec" aria-labelledby="duo-h">
 <div class="wrap">
  <p class="og-tag lt rv">Doctor &times; Karunya</p>
  <h2 id="duo-h" class="rv">Personal branding is a team game.</h2>
  <p class="lead rv">Social media doesn't run on an agency alone. Patients want the doctor's face, voice and trust. So we work with you as one team: you do your part, we do ours.</p>
  <div class="duo">
   <div class="duo-col you rv"><h3>Your part</h3><ul>
    <li>A little time each month for shoots</li>
    <li>Sharing the real questions patients ask</li>
    <li>Speaking on camera, in your own style</li>
    <li>Approving every post</li></ul></div>
   <div class="duo-mid" aria-hidden="true"><b>Dr.</b><em>&times;</em><b>K</b><i></i></div>
   <div class="duo-col us rv"><h3>Our part</h3><ul>
    <li>Topic research and scripts</li>
    <li>Shoot guidance, editing and captions</li>
    <li>Posting, replies and your Google profile</li>
    <li>A monthly report and the next plan</li></ul></div>
  </div>
  <p class="duo-note rv">When the doctor and the team move together, real trust shows in the content. That is what brings patients to your clinic.</p>
 </div>
</section>


{team()}

<section class="sec dark" aria-labelledby="svc-h">
 <div class="wrap">
  <h2 id="svc-h" class="rv">Everything a clinic needs, from one team.</h2>
  <div class="svc-list">{svc_rows}</div>
 </div>
</section>

<section class="sec light" aria-labelledby="proc-h">
 <div class="wrap">
  <h2 id="proc-h" class="rv">How we get started</h2>
  <p class="lead rv">Four simple steps. All you do is send the first message and approve each month.</p>
  <div class="process">
   <div class="road"></div><div class="road-fill"></div>
   <svg class="rick-ico" viewBox="-10 -100 160 110" aria-hidden="true">{rickshaw().replace('translate(0 666)', 'translate(0 0)')}</svg>
   <ol class="steps">{steps_html}</ol>
  </div>
 </div>
</section>

{blog_preview()}

{home_faq()}

<section class="sec white seo-sec" aria-labelledby="seo-h"><div class="wrap seo-grid">
 <h2 id="seo-h" class="rv">A social media and marketing agency for doctors</h2>
 <div class="rv">
  <p>Karunya Digital is a <b>healthcare marketing agency</b> that works only with doctors and hospitals. We handle <b>social media management for doctors</b>, Instagram reels, Google Business Profile and SEO, within the new NMC rules, so patients in your city find you easily.</p>
  <p>Gynaecologists, IVF specialists, orthopaedic surgeons, dentists and pulmonologists, from <a href="healthcare-marketing-agency-varanasi.html">Varanasi</a> to <a href="healthcare-marketing-agency-meerut.html">Meerut</a>, <a href="healthcare-marketing-agency-lucknow.html">Lucknow</a>, Agra, <a href="healthcare-marketing-agency-prayagraj.html">Prayagraj</a>, <a href="healthcare-marketing-agency-patna.html">Patna</a> and <a href="healthcare-marketing-agency-gorakhpur.html">Gorakhpur</a>: 50+ doctors work with us today.</p>
 </div>
</div></section>


</main>
'''
    _h = head("Healthcare Digital Marketing Agency for Doctors | Karunya Digital", "Healthcare digital marketing agency in Varanasi for doctors, clinics and hospitals across India: Instagram reels, Google Business Profile, SEO. 50+ doctors.", "home") + header("Home") + body + footer()
    return page_ld(_h, "Healthcare marketing agency for doctors", "", faq=HOME_FAQ)



# ------------------------------------------------------------------ VARANASI LANDING (local SEO)
HOME_FAQ = [
    ("What does a healthcare marketing agency do for a doctor?", "It makes you easy to find and easy to trust online. For our doctors that means patient-education Reels, a complete Google Business Profile, SEO for your clinic's name and services, and a consistent look everywhere, with a clear report every month."),
    ("Which doctors and hospitals does Karunya Digital work with?", "Only healthcare. We work with gynaecologists, IVF specialists, orthopaedic surgeons, dentists, pulmonologists, physicians, clinics, nursing homes and multi-speciality hospitals. 50+ doctors across India work with us from our Varanasi office."),
    ("Is my marketing safe under the NMC 2026 guidelines?", "Yes. Every post is planned as patient education and checked against the NMC's Guidelines on Ethical Advertising and Public Communication (October 2026). No testimonials, no before/after photos, no 'best doctor' claims and no discount offers. Nothing goes live without your approval."),
    ("I'm not comfortable on camera. Can you still help?", "Yes. We write the script and guide you on what to say, where to stand and which light to use, so most doctors record on their own phone in a few minutes. If you prefer not to appear, voiceover and motion-graphic videos work too."),
    ("How much of my time does it take every month?", "One call to start. After that, you approve the monthly content calendar and give a little time for recording. Scripts, editing, captions, posting, Google updates and reports are handled by our team."),
    ("Do I need to be in Varanasi to work with you?", "No. Our office is on Taktakpur Road, Varanasi, and we work with doctors in Meerut, Lucknow, Prayagraj, Agra, Greater Noida, Bihar and other cities over WhatsApp and calls."),
    ("How do I get started?", "Take the free 2-minute Google + Instagram check, or send us a WhatsApp message. We look at your profiles, have a short call, and share a written plan made for your speciality and city."),
]


def home_faq():
    rows = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in HOME_FAQ)
    return f'''<section class="sec light" id="faq" aria-labelledby="hfaq-h"><div class="wrap">
 <p class="og-tag lt rv">Before you message us</p>
 <h2 id="hfaq-h" class="rv">Questions doctors ask us first.</h2>
 <div class="faq rv">{rows}</div>
 <p class="lead rv" style="margin-top:26px">More questions? See our <a href="services.html">services</a>, read the <a href="blog.html">guides for doctors</a>, or <a href="{wa()}" target="_blank" rel="noopener">ask us on WhatsApp</a>.</p>
</div></section>'''


VNS_SLUG = "healthcare-marketing-agency-varanasi"
VNS_FAQ = [
    ("Where is Karunya Digital's office in Varanasi?", "Our office is on Taktakpur Road, near Mahavir Mandir, Varanasi, Uttar Pradesh 221001. We are open Monday to Saturday, 10am to 7pm."),
    ("Do you work only with doctors and hospitals?", "Yes. Karunya Digital is a healthcare-only marketing agency. We work with doctors, dentists, clinics and hospitals, not with other industries."),
    ("Do you send a camera crew for shoots?", "No. We write the scripts, guide you on how to record on your phone (light, sound, framing), and then handle editing, captions and posting."),
    ("Is your work safe under the NMC 2026 advertising guidelines?", "Every post is planned as patient education and checked against the NMC guidelines (and the National Dental Commission advisory for dentists) before it reaches you. Nothing goes live without your approval. We don't do testimonials, before/after photos, 'best doctor' claims or discount offers."),
    ("How much does it cost?", "We don't publish fixed prices. After a short call we share a plan and a fixed monthly fee that fits your speciality and goals. The fee is never linked to the number of patients or leads."),
    ("Can you work with doctors outside Varanasi?", "Yes. Our only office is in Varanasi, and we work with doctors in other cities remotely over WhatsApp and calls."),
]


def varanasi_page():
    msg = "Hello Karunya Digital, I'm a doctor in Varanasi and I'd like to talk about marketing for my clinic."
    services_v = [
        ("Google Business Profile", "Correct name, address, phone, timings, services and photos, so patients searching 'doctor near me' in Varanasi find you on Google Maps."),
        ("Instagram & Reels", "Patient-education Reels in Hindi, Hinglish or English. We write scripts, guide your phone shoot, edit, caption and post."),
        ("SEO & website", "Pages for each service and condition you treat, your qualifications and registration details, and local search basics done right."),
        ("YouTube & Shorts", "Longer explainers and Shorts that answer the questions your patients ask every day."),
        ("Monthly strategy & report", "Calls, direction requests, profile views and reach, explained in plain words, with next month's plan."),
    ]
    sv = "".join(f'<div class="value"><h3>{t}</h3><p>{d}</p></div>' for t, d in services_v)
    specs = "".join(f'<li><a href="{SPECS[k]["file"]}">{SPECS[k]["name"]}</a></li>' for k in SPECS) + '<li><a href="services.html">Multi-speciality hospitals</a></li><li><a href="services.html">General physicians</a></li>'
    guides = [q for q in POSTS if "varanasi" in q.get("keyword", "").lower()][:3]
    guide_cards = "".join(post_card(q) for q in guides)
    faq_html = "".join(f'<p><strong>{_html.escape(q)}</strong><br>{_html.escape(a)}</p>' for q, a in VNS_FAQ)
    body = f"""<main id="main">
{page_hero("Healthcare digital marketing agency in Varanasi", "Karunya Digital helps doctors, dentists, clinics and hospitals in Varanasi get found on Google, Instagram and YouTube. One healthcare-only team on Taktakpur Road. You approve every post.")}
<section class="sec light" aria-labelledby="v1-h"><div class="wrap about-grid">
 <div>
  <h2 id="v1-h">A digital marketing agency for doctors in Varanasi</h2>
  <p class="lead">When a family in Varanasi needs a doctor, they search on their phone first: on Google Maps, on Instagram, in Hindi and in English. Our job is to make sure they find correct, useful information about you.</p>
  <p class="lead">We work only in healthcare, with 50+ doctor clients. Every piece of content is patient education, written for the NMC 2026 guidelines, and goes live only after your yes.</p>
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:22px"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Talk on WhatsApp</a><a class="btn btn-navy" href="audit.html">Get a free check</a></div>
 </div>
 <div class="values">{sv}</div>
</div></section>
<section class="sec dark" aria-labelledby="v2-h"><div class="wrap">
 <h2 id="v2-h">Specialities we market in Varanasi</h2>
 <p class="lead">Each speciality has different patients and different questions, so the content is built for it.</p>
 <ul class="topics">{specs}</ul>
</div></section>
<section class="sec white" aria-labelledby="v3-h"><div class="wrap" style="max-width:860px"><article class="prose">
 <h2 id="v3-h">Why a healthcare-only agency in Varanasi</h2>
 <p>Most agencies in the city work with every kind of business, from hotels to coaching centres. Medical marketing has its own rules. Since 6 October 2026, the NMC's Guidelines on Ethical Advertising and Public Communication bar patient testimonials, before/after content, "best" or "guaranteed" claims, paid or solicited reviews and discount offers. Dentists also follow the National Dental Commission's advisory of 14 October 2026.</p>
 <p>We plan around these rules from the start, so your pages build trust without putting your registration at risk. Read our <a href="blog-digital-marketing-agency-in-varanasi.html">guide to choosing a digital marketing agency in Varanasi</a> and our <a href="blog-how-to-choose-digital-marketing-agency-for-clinic.html">clinic agency checklist</a> before you hire anyone, including us.</p>
 <h2>How we work with Varanasi doctors</h2>
 <ol><li><b>Free check:</b> we look at your Google profile and Instagram and share the top fixes.</li><li><b>Short call or visit:</b> we understand your speciality, patients and goals, and share a plan with a fixed monthly fee.</li><li><b>Monthly content:</b> topics, scripts, shoot guidance, editing and posting, all approved by you.</li><li><b>Monthly report:</b> what changed on Google and Instagram, in plain words.</li></ol>
 <h2>Visit or call us</h2>
 <p><b>Karunya Digital</b><br>{ADDR}<br>Mon–Sat, 10am–7pm<br>Call <a href="tel:{CALL}">{CALL_TXT}</a> · WhatsApp <a href="{wa(msg)}" target="_blank" rel="noopener">{WA_TXT}</a><br><a href="https://www.google.com/maps/search/?api=1&amp;query=Karunya+Digital+Taktakpur+Road+Varanasi" target="_blank" rel="noopener">Open in Google Maps</a></p>
 <h2>Frequently asked questions</h2>
 {faq_html}
</article></div></section>
{f'<section class="sec light"><div class="wrap"><h2 style="font-size:clamp(1.6rem,3vw,2.2rem)">Varanasi guides for doctors</h2><div class="posts">{guide_cards}</div></div></section>' if guide_cards else ''}
</main>
"""
    import json
    faq = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in VNS_FAQ]}, ensure_ascii=False)
    bc = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://karunyadigital.online/"}, {"@type": "ListItem", "position": 2, "name": "Healthcare marketing agency in Varanasi", "item": f"https://karunyadigital.online/{VNS_SLUG}.html"}]})
    svc = json.dumps({"@context": "https://schema.org", "@type": "Service", "name": "Healthcare digital marketing in Varanasi", "serviceType": "Digital marketing for doctors, clinics and hospitals", "provider": {"@id": "https://karunyadigital.online/#org"}, "areaServed": {"@type": "City", "name": "Varanasi"}, "url": f"https://karunyadigital.online/{VNS_SLUG}.html"})
    h = head("Healthcare Digital Marketing Agency in Varanasi for Doctors | Karunya Digital", "Healthcare digital marketing agency in Varanasi for doctors, dentists and hospitals: Google Maps, Instagram Reels, SEO. NMC-safe. Taktakpur Road office.", VNS_SLUG)
    h = h.replace("</head>", f'<script type="application/ld+json">{svc}</script>\n<script type="application/ld+json">{bc}</script>\n<script type="application/ld+json">{faq}</script>\n</head>')
    return h + header("") + body + footer()

# ------------------------------------------------------------------ SERVICE LANDING PAGES
NMC_LINE = "Every post is planned as patient education and checked against the NMC's Guidelines on Ethical Advertising and Public Communication (October 2026). Nothing goes live without your approval."
SVC_PAGES = {
    "google-business-profile-management-for-doctors": {
        "nav": "Google Business Profile for doctors", "svc": "gmb",
        "title": "Google Business Profile Management for Doctors | Karunya Digital",
        "desc": "Google Business Profile management for doctors, clinics and hospitals: complete profile, weekly posts, review replies and a monthly report. NMC-safe.",
        "h1": "Google Business Profile management for doctors",
        "sub": "When a patient searches \u201cdoctor near me\u201d, Google Maps answers first. We keep your profile complete, correct and active, so the right patients can call you or ask for directions.",
        "h2": "Be the doctor patients find on Google Maps",
        "intro": ["Most patients never reach a clinic's website. They see the Google profile: your name, speciality, timings, photos and reviews, and decide in a few seconds. A half-filled profile with the wrong timing or an old phone number quietly sends them elsewhere.",
                  "Karunya Digital manages Google Business Profiles for doctors, dentists, clinics and hospitals. We work only in healthcare, so we know what a patient looks for and what the medical rules allow."],
        "points": [("A complete, correct profile", "Name, address, phone, timings, services, departments, service area and photos, checked and kept up to date."),
                   ("Weekly Google posts", "Short patient-education updates and health-day posts that keep your profile active."),
                   ("Review replies in your tone", "Polite, professional replies to every review. We never buy, write or solicit reviews."),
                   ("Patient questions answered", "Clear answers to the common questions people ask on your profile."),
                   ("A monthly report", "Profile views, calls and direction requests, explained in plain words.")],
        "why": ("Why doctors need a healthcare-only team for Google", "A Google profile for a clinic is not the same as one for a shop. Medical categories, doctor-and-hospital listings at the same address, and the NMC and National Dental Commission rules on reviews and claims all need care. We set the profile up correctly once, then keep it active every week."),
        "steps": ["We check your current profile and share the top fixes.", "We complete and correct every section, with your approval.", "We post weekly and reply to reviews in your tone.", "You get a monthly report with calls and direction requests."],
        "faq": [("What is Google Business Profile management for doctors?", "It is the regular work of keeping a doctor's or clinic's Google listing complete, correct and active: details, photos, services, posts, review replies and a monthly report, so patients searching nearby can find and contact you."),
                ("Can you get me more Google reviews?", "We help you reply to reviews professionally and make it easy for patients to find your profile. We never buy, write or solicit reviews, because the NMC guidelines and Google's own policies do not allow it."),
                ("Do you manage profiles for hospitals with many doctors?", "Yes. We manage the hospital listing and each doctor's listing so they support each other and patients are not confused."),
                ("Do I need a website for Google Business Profile?", "No, a profile works without a website. A simple, correct website does help trust and search, and we can guide you on that too."),
                ("What do I see every month?", "A plain-language report with profile views, calls, direction requests and what we plan next.")],
        "related": ["blog-google-business-profile-for-doctors", "blog-google-reviews-for-doctors-nmc", "blog-seo-for-doctors"],
    },
    "instagram-reels-for-doctors": {
        "nav": "Instagram Reels for doctors", "svc": "reels",
        "title": "Instagram Reels & Social Media for Doctors | Karunya Digital",
        "desc": "Instagram Reels and social media management for doctors: scripts, shoot guidance, editing, captions and posting. Patient education, NMC-safe.",
        "h1": "Instagram Reels and social media for doctors",
        "sub": "You know the answers your patients need. We turn them into short, clear Reels in Hindi, Hinglish or English, and handle everything after you press record.",
        "h2": "Patient education that people actually watch",
        "intro": ["Patients scroll before they search. A 40-second Reel that answers one real question, in the language your patients speak, builds more trust than any poster. The hard part is finding the time: topics, scripts, editing, captions, posting.",
                  "Karunya Digital does that part. We work only with doctors and hospitals, with 50+ doctor clients across India, so every script is written for patients and for the medical rules."],
        "points": [("Topics from real patient questions", "Weekly topics picked from what your patients actually ask in the OPD."),
                   ("Scripts in your language", "Hindi, Hinglish or English: a 3-second hook, three clear points and a simple next step."),
                   ("Shoot guidance", "What to say, where to stand and which light to use, so you can record on your phone in minutes."),
                   ("Editing, captions and thumbnails", "Clean edits, readable captions and a consistent look for your page."),
                   ("Posting on Instagram and YouTube Shorts", "We publish, write the captions and keep your page regular.")],
        "why": ("Why doctors choose a healthcare-only social media team", "A general agency writes for likes. Medical content has to be accurate, calm and within the rules. We write patient education, not promotion: no testimonials, no before/after photos, no superlative claims. Not comfortable on camera? Voiceover and motion-graphic Reels work too."),
        "steps": ["You share the questions patients ask you most.", "We send a monthly content calendar and scripts for your approval.", "You record on your phone with our guidance.", "We edit, caption and post, and report every month."],
        "faq": [("Do you send a camera crew to my clinic?", "No. We write the scripts and guide your phone shoot (light, sound, framing), then handle editing, captions and posting."),
                ("Are Reels allowed for doctors under the NMC guidelines?", "Educational content is allowed. What the October 2026 NMC guidelines restrict is promotion: testimonials, before/after content, 'best' or 'guaranteed' claims and solicitation. We plan every Reel as patient education and you approve it before it goes live."),
                ("I don't have time to shoot. What then?", "Most doctors record a month's Reels in one short sitting. If you prefer not to appear, we make voiceover and motion-graphic videos."),
                ("Which languages do you write in?", "Hindi, Hinglish and English, based on what your patients speak."),
                ("Do you also manage Facebook and YouTube?", "Yes. The same content is adapted for Facebook and YouTube Shorts.")],
        "related": ["blog-instagram-marketing-agency-for-doctors", "blog-social-media-agency-for-doctors", "blog-bio-for-doctors-on-instagram"],
    },
    "seo-services-for-doctors": {
        "nav": "SEO services for doctors", "svc": "calendar",
        "title": "SEO Services for Doctors, Clinics & Hospitals | Karunya Digital",
        "desc": "SEO services for doctors, clinics and hospitals in India: local SEO, Google Business Profile, service pages and patient-education content. NMC-safe.",
        "h1": "SEO services for doctors, clinics and hospitals",
        "sub": "Patients type their problem and their city into Google. Good SEO makes sure a correct, helpful page about you is what they find.",
        "h2": "Local SEO built for how patients search",
        "intro": ["A patient rarely searches for a doctor's name first. They search \u201cgynaecologist in Varanasi\u201d, \u201cknee pain doctor near me\u201d or a question about their symptom. SEO for doctors is the work of being the clear, trustworthy answer to those searches.",
                  "Karunya Digital does SEO only for healthcare. We combine your Google Business Profile, your website and your patient-education content, so they all point patients to the same correct information."],
        "points": [("Local SEO and Google Maps", "A complete Google Business Profile and consistent name, address and phone everywhere."),
                   ("Pages for what you treat", "Clear pages for each service and condition, with your qualifications and registration details."),
                   ("Patient-education articles", "Answers to the questions patients ask, written in simple language and reviewed by you."),
                   ("Technical basics done right", "Fast pages, mobile-friendly layout, correct titles and structured data."),
                   ("A monthly report", "Which searches found you, plus calls and direction requests, in plain words.")],
        "why": ("Why medical SEO needs a specialist", "Google holds health pages to a higher standard of accuracy and trust, and the NMC guidelines limit what a doctor's page can claim. We write factual, patient-first content with your credentials shown clearly, and we stay away from 'best doctor' and 'guaranteed' language that can put your registration at risk."),
        "steps": ["Free check of your Google profile and current search presence.", "A plan for your speciality and city, with the pages and topics to build.", "We build and publish, with your approval on every page.", "Monthly report and next month's plan."],
        "faq": [("How long does SEO take for a doctor?", "Google profile fixes can show within weeks. Website pages and articles build steadily over a few months as Google reads and trusts them."),
                ("Do I need a website for SEO?", "For Google Maps, a complete profile is the start. For wider searches, a simple website with clear pages for your services helps a lot, and we can guide you on that."),
                ("Is SEO allowed for doctors under NMC rules?", "Yes. Giving accurate information about your qualifications, services and timings, and educating patients, is allowed. Superlative claims, testimonials and solicitation are not, and we avoid them."),
                ("Do you do SEO for hospitals?", "Yes. We plan pages for each department and doctor so the hospital and its doctors are found together."),
                ("Which cities do you work in?", "Our office is in Varanasi and we work with doctors across India, including Lucknow, Prayagraj, Meerut, Patna and Gorakhpur, over WhatsApp and calls.")],
        "related": ["blog-seo-agency-for-doctors", "blog-seo-for-doctors", "blog-hospital-seo-agency"],
    },
}


def service_page(slug):
    d = SVC_PAGES[slug]
    msg = f"Hello Karunya Digital, I'd like to know more about {d['nav']}."
    pts = "".join(f'<div class="value"><h3>{t}</h3><p>{x}</p></div>' for t, x in d["points"])
    steps = "".join(f"<li>{x}</li>" for x in d["steps"])
    faq_html = "".join(f"<details><summary>{_html.escape(q)}</summary><p>{_html.escape(a)}</p></details>" for q, a in d["faq"])
    rel = [q for q in POSTS if q["slug"] in d["related"]]
    rel_cards = "".join(post_card(q) for q in rel)
    others = "".join(f'<li><a href="{k}.html">{v["nav"]}</a></li>' for k, v in SVC_PAGES.items() if k != slug) + "".join(f'<li><a href="{SPECS[k]["file"]}">{SPECS[k]["name"]} marketing</a></li>' for k in SPECS) + f'<li><a href="{VNS_SLUG}.html">Healthcare marketing agency in Varanasi</a></li>'
    body = f"""<main id="main">
{page_hero(d["h1"], d["sub"])}
<section class="sec light" aria-labelledby="s1-h"><div class="wrap about-grid">
 <div>
  <h2 id="s1-h">{d["h2"]}</h2>
  {"".join(f'<p class="lead">{x}</p>' for x in d["intro"])}
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:22px"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Talk on WhatsApp</a><a class="btn btn-navy" href="audit.html">Get a free check</a></div>
 </div>
 <div class="values">{pts}</div>
</div></section>
<section class="sec white" aria-labelledby="s2-h"><div class="wrap" style="max-width:860px"><article class="prose">
 <h2 id="s2-h">{d["why"][0]}</h2>
 <p>{d["why"][1]}</p>
 <p>{NMC_LINE}</p>
 <h2>How it works</h2>
 <ol>{steps}</ol>
 <p>We don't publish fixed prices. After a short call we share a written plan and a fixed monthly fee that fits your speciality and city.</p>
</article>
 <h2 style="margin-top:48px">Frequently asked questions</h2>
 <div class="faq">{faq_html}</div>
</div></section>
<section class="sec dark" aria-labelledby="s3-h"><div class="wrap">
 <h2 id="s3-h">More from Karunya Digital</h2>
 <ul class="topics">{others}</ul>
</div></section>
{f'<section class="sec light"><div class="wrap"><h2 style="font-size:clamp(1.6rem,3vw,2.2rem)">Guides for doctors</h2><div class="posts">{rel_cards}</div></div></section>' if rel_cards else ''}
</main>
"""
    h = head(d["title"], d["desc"], slug)
    return page_ld(h, d["nav"], slug + ".html", faq=d["faq"], service=d["nav"]) + header("Services") + body + footer()


# ------------------------------------------------------------------ CITY LANDING PAGES
CITY_PAGES = {
    "lucknow": {"city": "Lucknow", "state": "Uttar Pradesh", "guide": "blog-digital-marketing-agency-for-doctors-in-lucknow",
        "proof": "In Lucknow we already work with Dr. Rishabh Jaiswal (orthopaedics, Max Hospital) and Dr. Tanima Shukla (gynaecology).",
        "local": "Lucknow has large hospitals and hundreds of independent clinics, so a patient searching on their phone sees many names at once. The doctors they call are the ones whose Google profile is complete and whose face and voice they have already seen in a short video."},
    "prayagraj": {"city": "Prayagraj", "state": "Uttar Pradesh", "guide": "blog-digital-marketing-agency-in-prayagraj",
        "proof": "In Prayagraj we already work with Dr. Vaibhav Krishna (pulmonology).",
        "local": "Patients come to Prayagraj from the districts around it, and most of them search in Hindi before they travel. Clear Hindi and Hinglish content, with the right address, timings and phone number on Google, is what brings them to the right clinic."},
    "meerut": {"city": "Meerut", "state": "Uttar Pradesh", "guide": "",
        "proof": "In Meerut we already work with Dr. Manisha Chaudhary (gynaecology), Dr. Raman Jindal (orthopaedics) and Sangeeta Hospital.",
        "local": "Meerut patients compare local doctors with hospitals in Delhi NCR. A doctor who explains things simply in a Reel, and whose Google profile shows correct timings and real replies to reviews, gives families a reason to stay in the city for treatment."},
    "patna": {"city": "Patna", "state": "Bihar", "guide": "blog-digital-marketing-agency-for-doctors-in-patna",
        "proof": "In Bihar we already work with doctors in Siwan, including Dr. Alka Sony Chaudhary (gynaecology) and Dr. Madhuresh Kumar (orthopaedics).",
        "local": "Patna is where families from across Bihar come for specialist care. They usually search from their home district first, so the doctors they find are the ones with a complete Google profile and patient-education videos in the language they speak."},
    "gorakhpur": {"city": "Gorakhpur", "state": "Uttar Pradesh", "guide": "blog-digital-marketing-agency-in-gorakhpur",
        "proof": "We are based in Varanasi and work with 50+ doctors across Uttar Pradesh and Bihar.",
        "local": "Gorakhpur serves patients from eastern Uttar Pradesh and the districts near the border. Many of them search in Hindi on a phone, so simple Hindi videos and a correct Google Maps listing matter more than a fancy website."},
}


def city_slug(k):
    return f"healthcare-marketing-agency-{k}"


def city_page(k):
    d = CITY_PAGES[k]; c = d["city"]; slug = city_slug(k)
    msg = f"Hello Karunya Digital, I'm a doctor in {c} and I'd like to talk about marketing for my clinic."
    services_c = [
        ("Google Business Profile", f"Correct name, address, phone, timings, services and photos, so patients searching 'doctor near me' in {c} find you on Google Maps."),
        ("Instagram & Reels", "Patient-education Reels in Hindi, Hinglish or English. We write scripts, guide your phone shoot, edit, caption and post."),
        ("SEO & website", "Pages for each service and condition you treat, your qualifications and registration details, and local search basics done right."),
        ("YouTube & Shorts", "Longer explainers and Shorts that answer the questions your patients ask every day."),
        ("Monthly strategy & report", "Calls, direction requests, profile views and reach, explained in plain words, with next month's plan."),
    ]
    sv = "".join(f'<div class="value"><h3>{t}</h3><p>{x}</p></div>' for t, x in services_c)
    specs = "".join(f'<li><a href="{SPECS[x]["file"]}">{SPECS[x]["name"]}</a></li>' for x in SPECS) + "".join(f'<li><a href="{x}.html">{v["nav"]}</a></li>' for x, v in SVC_PAGES.items())
    faq = [
        (f"Does Karunya Digital have an office in {c}?", f"No. Our only office is on Taktakpur Road, Varanasi. We work with doctors in {c} remotely, over WhatsApp and calls, the same way we work with doctors in other cities."),
        (f"How do shoots work for a doctor in {c}?", "We don't send a camera crew. We write the script and guide you on light, sound and framing, so you record on your phone in a few minutes. We then edit, caption and post."),
        ("Is the work safe under the NMC 2026 advertising guidelines?", "Every post is planned as patient education and checked against the NMC guidelines (and the National Dental Commission advisory for dentists). No testimonials, before/after photos, 'best doctor' claims or discount offers. Nothing goes live without your approval."),
        ("How much does it cost?", "We don't publish fixed prices. After a short call we share a written plan and a fixed monthly fee that fits your speciality and city. The fee is never linked to the number of patients or leads."),
        (f"Which doctors in {c} do you work with?", "Gynaecologists, IVF specialists, orthopaedic surgeons, dentists, pulmonologists, physicians, clinics, nursing homes and multi-speciality hospitals. We work only in healthcare."),
    ]
    faq_html = "".join(f"<details><summary>{_html.escape(q)}</summary><p>{_html.escape(a)}</p></details>" for q, a in faq)
    guide = next((q for q in POSTS if q["slug"] == d["guide"]), None)
    guide_line = f' Before you hire anyone, including us, read our <a href="{guide["slug"]}.html">guide to choosing a digital marketing agency in {c}</a>.' if guide else ""
    others = "".join(f'<li><a href="{city_slug(x)}.html">{v["city"]}</a></li>' for x, v in CITY_PAGES.items() if x != k) + f'<li><a href="{VNS_SLUG}.html">Varanasi</a></li>'
    body = f"""<main id="main">
{page_hero(f"Healthcare digital marketing agency for doctors in {c}", f"Karunya Digital helps doctors, dentists, clinics and hospitals in {c} get found on Google, Instagram and YouTube. A healthcare-only team. You approve every post.")}
<section class="sec light" aria-labelledby="c1-h"><div class="wrap about-grid">
 <div>
  <h2 id="c1-h">A digital marketing agency for doctors in {c}</h2>
  <p class="lead">{d["local"]}</p>
  <p class="lead">{d["proof"]} Every piece of content is patient education, written for the NMC 2026 guidelines, and goes live only after your yes.</p>
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-top:22px"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Talk on WhatsApp</a><a class="btn btn-navy" href="audit.html">Get a free check</a></div>
 </div>
 <div class="values">{sv}</div>
</div></section>
<section class="sec dark" aria-labelledby="c2-h"><div class="wrap">
 <h2 id="c2-h">What we do for {c} doctors</h2>
 <p class="lead">Each speciality has different patients and different questions, so the content is built for it.</p>
 <ul class="topics">{specs}</ul>
</div></section>
<section class="sec white" aria-labelledby="c3-h"><div class="wrap" style="max-width:860px"><article class="prose">
 <h2 id="c3-h">Why {c} doctors choose a healthcare-only agency</h2>
 <p>Most agencies work with every kind of business, from hotels to coaching centres. Medical marketing has its own rules. Since 6 October 2026, the NMC's Guidelines on Ethical Advertising and Public Communication bar patient testimonials, before/after content, "best" or "guaranteed" claims, paid or solicited reviews and discount offers. We plan around these rules from the start, so your pages build trust without putting your registration at risk.{guide_line}</p>
 <h2>How we work with doctors in {c}</h2>
 <ol><li><b>Free check:</b> we look at your Google profile and Instagram and share the top fixes.</li><li><b>Short call:</b> we understand your speciality, patients and goals, and share a written plan with a fixed monthly fee.</li><li><b>Monthly content:</b> topics, scripts, shoot guidance, editing and posting, all approved by you.</li><li><b>Monthly report:</b> what changed on Google and Instagram, in plain words.</li></ol>
 <h2>Talk to us</h2>
 <p><b>Karunya Digital</b><br>{ADDR}<br>Mon–Sat, 10am–7pm<br>Call <a href="tel:{CALL}">{CALL_TXT}</a> · WhatsApp <a href="{wa(msg)}" target="_blank" rel="noopener">{WA_TXT}</a></p>
</article>
 <h2 style="margin-top:48px">Frequently asked questions</h2>
 <div class="faq">{faq_html}</div>
</div></section>
<section class="sec dark" aria-labelledby="c4-h"><div class="wrap">
 <h2 id="c4-h" style="font-size:clamp(1.6rem,3vw,2.2rem)">Other cities we work in</h2>
 <ul class="topics">{others}</ul>
</div></section>
</main>
"""
    h = head(f"Healthcare Marketing Agency for Doctors in {c} | Karunya Digital", f"Healthcare digital marketing agency for doctors, clinics and hospitals in {c}: Google Business Profile, Instagram Reels and SEO. NMC-safe, healthcare-only team.", slug)
    h = page_ld(h, f"Healthcare marketing agency in {c}", slug + ".html", faq=faq, service=f"Healthcare digital marketing in {c}")
    return h + header("") + body + footer()


# ------------------------------------------------------------------ SPECIALTY
SPEC_WORDS = {"gynae": ["gynae", "women", "maternity"], "ivf": ["ivf", "fertility"], "ortho": ["ortho", "spine", "physio"], "dental": ["dental", "dentist"]}


def spec_guides(k):
    words = SPEC_WORDS.get(k, [])
    ps = [p for p in POSTS if any(w in (p.get("keyword", "") + " " + p["slug"]).lower() for w in words)][:3]
    if not ps:
        return ""
    sp = SPECS[k]
    return (f'<section class="sec light" aria-labelledby="sg-h"><div class="wrap"><h2 id="sg-h" style="font-size:clamp(1.6rem,3vw,2.2rem)">Guides for {"dentists" if k == "dental" else sp["name"] + " doctors"}</h2>'
            f'<p class="lead">Hiring a {sp["name"].lower()} marketing agency? Start with these guides.</p><div class="posts">{"".join(post_card(p) for p in ps)}</div></div></section>')


def spec_page(k):
    sp = SPECS[k]
    msg = f"Hello Karunya Digital, I'm a {sp['who']} and I'd like to talk about reels and marketing for my clinic."
    docs = ""
    for name, city, photo, vids, reels in sp["doctors"]:
        tot = sum(p for p, _ in reels)
        img = f'<img src="media/{photo}.jpg" alt="{name}" width="600" height="750" loading="lazy">' if photo else f'<span class="mono">{name.replace("Dr. ", "")[:1]}</span>'
        pu = ig_profile(name)
        rl = f'<li><a class="doc-go" href="{pu}" target="_blank" rel="noopener">{IG_ICON}<span>See Instagram profile</span></a></li>' if pu else ""
        if name in FB:
            rl += f'<li><a class="doc-go" href="{FB[name]}" target="_blank" rel="noopener">{FB_ICON}<span>See Facebook page</span></a></li>'
        stat = ""
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
   <div class="cta-row hero-fade d3" style="display:flex;flex-wrap:wrap;gap:14px;margin-top:26px"><a class="btn btn-wa" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon()}Talk on WhatsApp</a><a class="btn btn-lime" href="audit.html">Get a free check</a></div>
  </div>
  <div class="spec-hero-art">{spec_art(k)}</div>
 </div>
 {skyline_strip()}
</section>

<section class="sec light" aria-labelledby="sd-h"><div class="wrap">
 <p class="og-tag lt rv">Karunya Exclusives</p>
 <h2 id="sd-h" class="rv">Our {sp["short"]} doctors</h2>
 <p class="lead rv">See any doctor's profile for yourself.</p>
 <div class="docs">{docs}</div>
</div></section>

<section class="sec reels-sec" aria-labelledby="sr-h">
 <div class="wrap"><h2 id="sr-h" class="rv">Reels patients stop for</h2></div>
 <div class="reel-strip">{"".join(spec_cards(k))}</div>
</section>

<section class="sec dark" aria-labelledby="st-h"><div class="wrap">
 <h2 id="st-h" class="rv">What your patients are searching for</h2>
 <p class="lead rv">Every question is a reel. Every reel is a way for a new patient to find you.</p>
 <ul class="topics">{topics}</ul>
</div></section>

<section class="sec light" aria-labelledby="sh-h"><div class="wrap about-grid">
 <div><h2 id="sh-h" class="rv">What we do differently for {sp["short"]}</h2>
 <p class="lead rv">Every speciality has different patients: different fears, different questions, different language. Our content is built around that.</p>
 <a class="btn btn-navy" style="margin-top:22px" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Send me a plan for my clinic</a></div>
 <div class="values">{how}</div>
</div></section>

{spec_guides(k)}
<section class="sec white" aria-label="Other specialties"><div class="wrap">
 <h2 style="font-size:clamp(1.6rem,3vw,2.2rem)">Explore other specialties</h2>
 <div class="others">{others}</div>
</div></section>
</main>
'''
    _h = head(f"{sp['name']} Marketing Agency for {'Dentists' if k == 'dental' else 'Doctors'} | Karunya Digital, Varanasi", f"{sp['name']} marketing agency in Varanasi for doctors across India: NMC-safe Instagram reels, Google Business Profile and SEO.", k) + header(sp["short"]) + body + footer()
    return page_ld(_h, f"{sp['name']} marketing for doctors", sp["file"], service=f"{sp['name']} marketing for doctors and clinics")


# ------------------------------------------------------------------ SERVICES
def services():
    items = [
        ("reels", "Reels & Shorts", "For doctors who want to educate patients but have no time for cameras and editing.",
         ["Weekly topics based on real patient questions", "Hindi, Hinglish or English scripts: a 3-second hook, 3 points and a clear call to action", "Shoot guidance: what to say, where to stand, which light", "Editing, captions, music and thumbnails", "Posting on Instagram Reels and YouTube Shorts"],
         "Every script is written with the NMC guidelines in mind, and is shot only after your yes. Not comfortable on camera? Voiceover and motion graphics work too.", "I'd like to know more about Reels."),
        ("gmb", "Google Business Profile", "For clinics that rank low in “near me” searches or have an incomplete profile.",
         ["Complete profile: services, timings, photos, service area", "Weekly Google posts", "Review replies written in your tone", "Answers to common patient questions on your profile", "Monthly report: calls and direction requests"],
         "We do everything that helps you show up first, and show you the results every month: views, calls and direction requests.", "I'd like to know more about Google Business Profile."),
        ("ads", "NMC-safe promotion", "For hospitals that want to share factual information about departments, facilities and health camps.",
         ["A check of every post against the October 2026 NMC guidelines", "Factual hospital awareness campaigns, only where the rules allow", "Health-day and awareness content", "No testimonials, offers or “best doctor” claims", "A clear monthly report"],
         "Since 6 October 2026, ads that promote an individual doctor's practice are risky under NMC rules. We'll tell you honestly what is safe before you spend a rupee.", "I'd like to know what promotion is safe under the NMC rules."),
        ("calendar", "Content calendar & reports", "For doctors who want to know exactly what goes out this month, and when.",
         ["Monthly content calendar in a clean PDF", "Topics planned around festivals and health days", "Competitor analysis report", "Proposals, patient forms and printable material"],
         "Your calendar arrives before the month begins. Change anything you like.", "I'd like to know more about the content calendar."),
        ("brand", "Doctor branding", "For doctors with a different photo, name and colour on every platform.",
         ["Your colours and fonts", "Instagram profile, bio and highlight covers", "Thumbnail and cover style", "A consistent look across reels and posts"],
         "A consistent identity helps patients remember you, and builds trust faster.", "I'd like to know more about doctor branding."),
    ]
    more = {"reels": ' <a class="btn btn-line btn-sm" style="margin-top:12px" href="instagram-reels-for-doctors.html">Reels for doctors, in detail</a>', "gmb": ' <a class="btn btn-line btn-sm" style="margin-top:12px" href="google-business-profile-management-for-doctors.html">Google profile management, in detail</a>'}
    rows = ""
    for k, t, f, ticks, honest, msg in items:
        rows += f'''<article class="svc-detail" id="{k}">
 <div class="art-board">{icon(k, 360)}</div>
 <div>
  <h2>{t}</h2>
  <p class="for">{f}</p>
  <ul class="ticks">{"".join(f"<li>{x}</li>" for x in ticks)}</ul>
  <p class="honest">{honest}</p>
  <a class="btn btn-navy btn-sm" href="{wa(msg)}" target="_blank" rel="noopener">{wa_icon(18)}Ask about this</a>{more.get(k, "")}
 </div>
</article>'''
    faq = [
        ("Do you follow the NMC guidelines?", "Yes. Our content follows the NMC's Guidelines on Ethical Advertising and Public Communication (October 2026): patient education first, no superlative claims, no testimonials and no patient images. Every post goes live only after your approval."),
        ("How much of my time will this take?", "One call to start. After that, approving the monthly calendar and a little time for shoots. Our team handles the rest."),
        ("How does the shoot work?", "We give you the script and clear guidance on what to say, how to stand and which light to use. Editing, captions, posting and strategy are on us. Most doctors shoot on their phone."),
        ("How much does it cost?", "It depends on your speciality, city and goals. After a short call we send a written plan with the exact work and a fixed monthly fee. For full hospital marketing, call +91 73176 59337."),
        ("What will I see every month?", "A clear report with your reach, followers from your city, Google views, calls and direction requests, plus the plan for next month."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f'''<main id="main">
{page_hero("Everything a clinic needs, in one place.", "Five services, one team. You focus on patients; we handle how they find you.")}
<section class="sec light"><div class="wrap">{rows}</div></section>
<section class="sec white" aria-labelledby="faq-h"><div class="wrap">
 <h2 id="faq-h">Questions doctors ask most</h2>
 <div class="faq">{faq_html}</div>
</div></section>
</main>
'''
    _h = head("Digital Marketing Services for Doctors & Hospitals | Karunya Digital, Varanasi", "Healthcare digital marketing services from Varanasi: social media management, Instagram reels, Google Business Profile, SEO and branding for doctors and hospitals.", "services") + header("Services") + body + footer()
    return page_ld(_h, "Services", "services.html", faq=faq, service="Healthcare digital marketing for doctors and hospitals")


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
 <h2 id="w0">The doctors who trust us</h2>
 <p class="lead">Tap any doctor to see their Instagram profile.</p>
 <div class="pf-grid">{profile_cards()}</div>
</div></section>
<section class="sec light" aria-labelledby="w1"><div class="wrap">
 <p class="og-tag lt">Edited by our team</p>
 <h2 id="w1">Reels by speciality</h2>
 <p class="lead">Pick a speciality. These videos were edited by our team and play right here.</p>
 <div class="tabs" role="tablist" aria-label="Speciality">
  <button role="tab" aria-selected="true" data-tab="all">All</button>{"".join(f'<button role="tab" aria-selected="false" data-tab="{k}">{SPECS[k]["short"]}</button>' for k in SPECS)}
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
  <div class="mock m4"><span class="tag">Awareness post</span><h3>Health days, done right</h3><p class="cap">Educational posts for health days, within the NMC rules.</p>
   <div class="adcard"><div class="ad-top"><i></i><span><b>Your clinic</b><br>World Thyroid Day</span></div><div class="ad-img">When should you get your thyroid tested?</div><div class="ad-foot"><span style="background:none;color:var(--navy);padding:0">Patient education</span><span>Save</span></div></div></div>
 </div>
</div></section>
</main>
'''
    return head("Our Work: Reels & Marketing for Doctors | Karunya Digital", "Karunya Originals, reels for our doctors by speciality, and the monthly formats behind our work.", "work") + header("Work") + body + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    values = [
        ("Healthcare only", "We don't market restaurants or showrooms. Only doctors and hospitals, so we understand your world and your patients."),
        ("Clear reporting", "Every month you see exactly what we did and what changed: views, calls and direction requests."),
        ("The patient's language", "Simple Hindi, Hinglish or English. Medical information an ordinary family can understand."),
        ("Your approval, always", "No post, reel or ad goes live without your approval. Your name, your decision."),
    ]
    vh = "".join(f'<div class="value"><h3>{t}</h3><p>{d}</p></div>' for t, d in values)
    body = f'''<main id="main">
<section class="ghat-wrap" aria-labelledby="ab-h">
 <div class="ghat-cap"><div class="wrap" style="padding-top:clamp(100px,12vw,140px)"><h1 id="ab-h" class="hero-fade d1" style="font-size:clamp(2.4rem,5vw,4.4rem);max-width:12em">From the ghats of Kashi, for doctors across India.</h1></div></div>
 {ghat()}
</section>

<section class="sec light"><div class="wrap about-grid">
 <div>
  <h2 class="rv">Karunya means compassion.</h2>
  <p class="meaning rv">Doctors work with compassion every day. Our job is to make sure it reaches the right patient.</p>
  <p class="rv">Karunya Digital is a healthcare marketing agency based in Varanasi. We work with 50+ doctors and hospitals across India, mostly in growing cities where there are many good doctors but few strong voices online.</p>
  <p class="rv">Our team handles scripts, editing, design and Google profiles, so doctors can give their full attention to patients.</p>
 </div>
 <div>
  <h2 class="rv" style="margin-bottom:22px">How we work</h2>
  <div class="values">{vh}</div>
 </div>
</div></section>

<section class="sec dark founder" aria-labelledby="fd-h"><div class="wrap founder-grid">
 <div class="f-card rv">
  <div class="f-avatar">{founder_art("fa fa-about")}</div>
  <b>Bhanu Pratap Rai</b><span>Founder, Karunya Digital</span>
  {ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}
 </div>
 <div>
  <p class="og-tag rv">Meet the founder</p>
  <h2 id="fd-h" class="rv">Being the voice of doctors is our work.</h2>
  <p class="lead rv">Bhanu Pratap Rai started Karunya Digital with one aim: to help doctors and hospitals reach the patients who need them, honestly and within the rules of the profession.</p>
  <p class="rv" style="color:var(--sky)">On his Instagram, Bhanu shares practical social media lessons for doctors. Karunya's page shows our latest work.</p>
  <div class="f-links rv">{ig_btn(IG_FOUNDER, "bhanuhelpsdoctors")}{ig_btn(IG_KARUNYA, "karunyadigital")}</div>
 </div>
</div></section>

{team()}

<section class="sec white"><div class="wrap about-grid">
 <div>
  <h2 class="rv">Karunya in 45 seconds</h2>
  <p class="lead rv">Our own ad, made exactly the way we make reels for doctors.</p>
  <h3 style="margin-top:36px;font-size:1.8rem">Where we work</h3>
  <ul class="cities"><li>Varanasi</li><li>Meerut</li><li>Lucknow</li><li>Prayagraj</li><li>Agra</li><li>Greater Noida</li><li>Siwan</li><li>Darbhanga</li><li>Amravati</li></ul>
 </div>
 <div>{reel("karunya-ad", "Karunya Digital", "Who we are, in 45 seconds", auto=False, cls="about-reel")}</div>
</div></section>
</main>
'''
    return head("About Karunya Digital | Healthcare Marketing Agency in Varanasi", "Karunya Digital is a healthcare marketing agency in Varanasi, founded by Bhanu Pratap Rai. We work only with doctors and hospitals.", "about") + header("About") + body + footer()


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
   <div><h3>Office</h3><p>Karunya Digital, Healthcare Marketing Agency<br>{ADDR}<br>Mon–Sat, 10am–7pm</p><p style="margin-top:6px"><a class="text-link" href="https://www.google.com/maps/search/?api=1&query={urllib.parse.quote('Karunya Digital Taktakpur Road Varanasi')}" target="_blank" rel="noopener">Open in Google Maps</a></p></div>
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
    return head("Contact Karunya Digital | Healthcare Marketing Agency, Varanasi", "Talk to Karunya Digital, a healthcare marketing agency on Taktakpur Road, Varanasi. Call +91 73176 59337 or WhatsApp +91 63864 92334.", "contact") + header("Contact") + body + footer()


FB = {"Dr. Madhuresh Kumar": "https://www.facebook.com/starorthoandmaternity/"}
FB_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v7h4v-7h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>'


def legal(kind):
    if kind == "privacy":
        title, h1, intro = "Privacy Policy", "Privacy policy", "How Karunya Digital collects and uses information on this website."
        body = f"""<h2>Who we are</h2><p>Karunya Digital is a healthcare marketing agency at {ADDR}. Phone {CALL_TXT}, WhatsApp {WA_TXT}.</p>
<h2>What we collect</h2><p>When you use our free Google and Instagram check, we collect the details you type: your name, WhatsApp number, speciality, city and your answers. When you use the contact form, your message opens in WhatsApp and is sent only if you choose to send it.</p>
<h2>How we use it</h2><p>We use these details only to share your report, reply to you and talk about our services. We do not sell or rent your information to anyone.</p>
<h2>Where it is stored</h2><p>Form entries are stored securely with our website host, Netlify. Messages you send on WhatsApp are handled by WhatsApp.</p>
<h2>Cookies</h2><p>This website does not use advertising or tracking cookies.</p>
<h2>Your choices</h2><p>To see, correct or delete your details, message us on WhatsApp at {WA_TXT} or call {CALL_TXT}. We will act on your request within 7 working days.</p>
<h2>Updates</h2><p>If this policy changes, the updated version will be posted on this page. Last updated: 2 November 2026.</p>"""
    else:
        title, h1, intro = "Terms of Service", "Terms of service", "The terms for using this website and working with Karunya Digital."
        body = f"""<h2>About these terms</h2><p>By using karunyadigital.online you agree to these terms. Karunya Digital is based at {ADDR}.</p>
<h2>Our services</h2><p>We provide social media content, Google Business Profile management, SEO, websites and branding for doctors and hospitals. The exact work, price and timeline for each client are confirmed in writing before we start.</p>
<h2>Approvals</h2><p>No content is published without the client's approval. Clients are responsible for the medical accuracy of what they approve, and we plan every post around the NMC's Guidelines on Ethical Advertising and Public Communication.</p>
<h2>Payments</h2><p>Plans are billed monthly in advance unless agreed otherwise in writing. Prices on this website are in Indian rupees.</p>
<h2>Content on this website</h2><p>Articles on this website are general information for doctors and are not legal or medical advice. Logos, illustrations, videos and text on this website belong to Karunya Digital or are used with permission.</p>
<h2>Contact</h2><p>Questions about these terms: WhatsApp {WA_TXT} or call {CALL_TXT}. Last updated: 2 November 2026.</p>"""
    main = f'''<main id="main">{page_hero(h1, intro)}<section class="sec light"><div class="wrap" style="max-width:820px"><article class="prose">{body}</article></div></section></main>'''
    return head(f"{title} | Karunya Digital", intro, kind) + header("") + main + footer()


POSTS = load_posts()
for k in SPECS:
    open(os.path.join(OUT, SPECS[k]["file"]), "w").write(spec_page(k))
open(os.path.join(OUT, "blog.html"), "w").write(blog_index(POSTS))
for _p in POSTS:
    open(os.path.join(OUT, _p["slug"] + ".html"), "w").write(blog_post(_p, POSTS))
BANNED = ["apna hospital", "golden hospital", "aaha rani", "asha rani", "muzammil", "mujammil", "muzzamil"]
for fn, html in [(city_slug(k) + ".html", city_page(k)) for k in CITY_PAGES] + [(k + ".html", service_page(k)) for k in SVC_PAGES] + [(VNS_SLUG + ".html", varanasi_page()), ("index.html", home()), ("audit.html", audit_page()), ("game.html", game_page()), ("404.html", page404()), ("services.html", services()), ("work.html", work()), ("about.html", about()), ("contact.html", contact()), ("privacy.html", legal("privacy")), ("terms.html", legal("terms"))]:
    open(os.path.join(OUT, fn), "w").write(html)
pages = ["", VNS_SLUG + ".html"] + [city_slug(k) + ".html" for k in CITY_PAGES] + [k + ".html" for k in SVC_PAGES] + [SPECS[k]["file"] for k in SPECS] + ["blog.html"] + [p["slug"] + ".html" for p in POSTS] + ["audit.html", "game.html", "services.html", "work.html", "about.html", "contact.html", "privacy.html", "terms.html"]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://karunyadigital.online/{p}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>" for p in pages) + "</urlset>")
for _f in glob.glob(os.path.join(OUT, "*.html")):
    _t = open(_f).read().lower()
    for _b in BANNED:
        if _b in _t:
            raise SystemExit(f"BANNED name '{_b}' found in {_f}. Remove it before publishing.")
print("built")
