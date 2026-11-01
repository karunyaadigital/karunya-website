"""Karunya Digital website generator (v3: premium dark design, English).
Run: python3 build/build.py   -> writes site/*.html and sitemap.xml"""
import os, json, datetime, urllib.parse, html as _html
from specs import SPECS, DEG, plays_fmt, spec_total, ig_profile, IG_ICON
from audit import audit_form
from build_posts import load_posts
from home_page import home_body
from team_art import TEAM, char

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
WA_NUM = "916386492334"
CALL = "+917317659337"
CALL_TXT = "+91 73176 59337"
WA_TXT = "+91 63864 92334"
ADDR = "Taktakpur Road, Near Mahavir Mandir, Varanasi, Uttar Pradesh 221001"
IG_FOUNDER = "https://www.instagram.com/bhanuhelpsdoctors/"
IG_KARUNYA = "https://www.instagram.com/karunyadigital/"
DEFAULT_MSG = "Hello Karunya Digital, I'm a doctor and I'd like to talk about marketing for my clinic."
TODAY = datetime.date.today().isoformat()
E = _html.escape

# verified from clients' public Instagram accounts, 1 Nov 2026
STATS = [("3.26", "Cr+", "plays on our doctors' reels"), ("44", "", "reels crossed 1 lakh plays"),
         ("8", "", "reels crossed 10 lakh plays"), ("50", "+", "doctors across India")]

ORIGINALS = [
    ("reelbaaz", "kc-reelbaaz", "EP 01", "Reelbaaz Doctor", "Why every doctor needs to be on social media."),
    ("nmc", "kc-nmc", "EP 02", "NMC Guidelines 2026", "The social media mistakes doctors must never make."),
    ("diwali", "kc-diwali", "EP 03", "Diwali Special", "Three festive-season strategies for doctors."),
    ("why", "kc-why", "EP 04", "Why Karunya Digital?", "You heal. We get you heard."),
    ("camera", "kc-camera", "EP 05", "Scared of the camera?", "From 'what do I say?' to confident on video."),
]

PLANS = [
    ("Starter", "20,000", "For doctors starting to build their presence online.",
     ["Instagram reels: script and editing", "Google Business Profile management", "Monthly content calendar", "Monthly report"]),
    ("Growth", "25,000", "For doctors ready to grow fast in their city.",
     ["Everything in Starter", "More reels every month", "NMC compliance check on every post", "Replies to reviews", "Doctor branding"]),
    ("Authority", "40,000", "For doctors who want to be the known name in their speciality.",
     ["Everything in Growth", "High-end motion graphic reels", "YouTube Shorts", "Competitor analysis", "Priority support"]),
]

CITIES = ["Varanasi", "Meerut", "Lucknow", "Prayagraj", "Agra", "Greater Noida", "Siwan", "Darbhanga", "Amravati"]

ARROW = '<svg class="ar" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ARROW_UR = '<svg class="ar" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
WA_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>'
SOUND = '<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/><path d="M16 8.5a5 5 0 0 1 0 7" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>'
PLAY = '<svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l12 7-12 7z" fill="currentColor"/></svg>'


def wa(msg=DEFAULT_MSG):
    return f"https://wa.me/{WA_NUM}?text=" + urllib.parse.quote(msg)


def canon(page):
    if page == "home": return ""
    if page in SPECS: return SPECS[page]["file"]
    return page + ".html"


LD_ORG = json.dumps({
    "@context": "https://schema.org", "@type": "ProfessionalService", "name": "Karunya Digital", "url": "https://karunyadigital.online/",
    "description": "Healthcare marketing agency for doctors and hospitals in India: Instagram reels, Google Business Profile, SEO and doctor branding",
    "logo": "https://karunyadigital.online/assets/icon-blue-512.png", "image": "https://karunyadigital.online/assets/icon-blue-512.png",
    "priceRange": "Rs 20,000 - Rs 40,000 per month", "telephone": CALL,
    "openingHours": "Mo-Sa 10:00-19:00",
    "knowsAbout": ["Social media management for doctors", "Healthcare marketing", "SEO for doctors", "Google Business Profile", "NMC advertising guidelines"],
    "founder": {"@type": "Person", "name": "Bhanu Pratap Rai", "sameAs": IG_FOUNDER}, "sameAs": [IG_KARUNYA],
    "address": {"@type": "PostalAddress", "streetAddress": "Taktakpur Road, Near Mahavir Mandir", "addressLocality": "Varanasi", "postalCode": "221001", "addressRegion": "Uttar Pradesh", "addressCountry": "IN"},
    "areaServed": CITIES[:6]})


def head(title, desc, page, og_img="assets/icon-blue-512.png", extra=""):
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#F3F6FA">
<link rel="canonical" href="https://karunyadigital.online/{canon(page)}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="https://karunyadigital.online/{canon(page)}">
<meta property="og:image" content="https://karunyadigital.online/{og_img}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="fonts/Waylimo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/site.css">
<script>document.documentElement.classList.add("js")</script>
<script type="application/ld+json">{LD_ORG}</script>{extra}
</head>
<body class="p-{page}">
<a class="skip" href="#main">Skip to content</a>
'''


def header(active=""):
    def L(href, name):
        cur = ' aria-current="page"' if name == active else ''
        return f'<a class="nl" href="{href}"{cur}>{name}</a>'
    spec_links = "".join(f'<a href="{SPECS[k]["file"]}"><b>{SPECS[k]["name"]}</b><span>{plays_fmt(spec_total(k))} plays</span></a>' for k in SPECS)
    spec_on = ' aria-current="page"' if active in [SPECS[k]["short"] for k in SPECS] else ''
    return f'''<header class="hd">
 <div class="w hd-in">
  <a class="brand" href="index.html" aria-label="Karunya Digital home"><img src="assets/logo-navy.png" alt="Karunya Digital" width="118" height="37"></a>
  <nav class="nav" id="nav" aria-label="Main">
   {L("work.html", "Work")}{L("services.html", "Services")}
   <div class="dd"><button class="nl dd-btn" type="button" aria-expanded="false" aria-controls="dd-m"{spec_on}>Specialties</button><div class="dd-m" id="dd-m">{spec_links}</div></div>
   {L("blog.html", "Blog")}{L("about.html", "About")}{L("contact.html", "Contact")}
   <a class="btn btn-lime btn-sm nav-cta m-only" href="audit.html">Get a free check</a>
  </nav>
  <div class="hd-act">
   <a class="hd-wa" href="{wa()}" target="_blank" rel="noopener" aria-label="WhatsApp Karunya Digital">{WA_ICON}</a>
   <a class="btn btn-lime btn-sm" href="audit.html">Free check</a>
  </div>
  <button class="menu" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><i></i><i></i></button>
 </div>
</header>
'''


CTA_WORDS = "".join(f'<span class="cw2">{w}</span>' for w in ["clinic", "hospital", "gynaecology practice", "IVF centre", "dental clinic", "ortho clinic", "nursing home", "chest clinic", "skin clinic", "child clinic"])


def footer(cta=True):
    band = f'''<section class="cta" aria-labelledby="cta-h" data-trail="spark">
 <div class="w">
  <h2 id="cta-h" class="cta-h"><span class="sr">Let's make your clinic easy to find.</span><span aria-hidden="true">Let's make your</span><span class="cta-slot" aria-hidden="true">{CTA_WORDS}</span><span aria-hidden="true">easy to find.</span></h2>
  <div class="row"><a class="btn btn-lime" href="audit.html">Get a free check</a><a class="btn btn-ghost" href="{wa()}" target="_blank" rel="noopener">{WA_ICON}Talk on WhatsApp</a></div>
 </div>
</section>''' if cta else ""
    cols = "".join(f'<li><a href="{h}">{n}</a></li>' for h, n in [("work.html", "Work"), ("services.html", "Services & pricing"), ("blog.html", "Blog"), ("about.html", "About"), ("contact.html", "Contact"), ("audit.html", "Free check")])
    specs = "".join(f'<li><a href="{SPECS[k]["file"]}">{SPECS[k]["name"]}</a></li>' for k in SPECS)
    return f'''{band}
<footer class="ft">
 <div class="w">
  <div class="ft-top">
   <div class="ft-brand">
    <p class="ft-word">karunya<span>.</span></p>
    <p class="ft-tag">You heal. We get you heard.</p>
    <p class="ft-live"><i></i>Varanasi <b data-clock>--:--</b> IST · Mon–Sat, 10am–7pm</p>
   </div>
   <div class="ft-cols">
    <div><h3>Explore</h3><ul>{cols}</ul></div>
    <div><h3>Specialties</h3><ul>{specs}</ul></div>
    <div><h3>New business</h3><ul>
     <li><a href="{wa()}" target="_blank" rel="noopener">WhatsApp {WA_TXT}</a></li>
     <li><a href="tel:{CALL}">Call {CALL_TXT}</a></li>
     <li><a href="{IG_KARUNYA}" target="_blank" rel="noopener">Instagram @karunyadigital</a></li>
     <li><a href="{IG_FOUNDER}" target="_blank" rel="noopener">Founder @bhanuhelpsdoctors</a></li>
     <li class="muted">{ADDR}</li></ul></div>
   </div>
  </div>
  <div class="ft-bot"><span>© <span data-year>2026</span> Karunya Digital</span><span>Every post goes live only after the doctor's approval.</span><button class="totop" type="button" data-top>Back to top ↑</button></div>
 </div>
</footer>
<a class="wa-fab" href="{wa()}" target="_blank" rel="noopener" aria-label="Chat with Karunya Digital on WhatsApp">{WA_ICON}</a>
<script src="js/site.js" defer></script>
</body>
</html>
'''


def page_hero(eyebrow, h1, p, cls=""):
    return f'''<section class="ph {cls}"><div class="w">
 <p class="eyebrow up">{eyebrow}</p>
 <h1 class="ph-h up d1">{h1}</h1>
 <p class="ph-p up d2">{p}</p>
</div></section>'''


def reel_card(video, name, sub, plays=None):
    pl = f'<span class="rc-pl">{PLAY.replace("22", "12")}{plays_fmt(plays)} plays</span>' if plays else ""
    return f'''<figure class="rc">
 <div class="rc-f"><video src="media/{video}.mp4" poster="media/{video}.jpg" muted loop playsinline preload="none" data-auto aria-label="Reel: {E(name)}"></video>
  <button class="snd" type="button" data-sound aria-pressed="false">{SOUND}<span>Sound on</span></button>{pl}</div>
 <figcaption><b>{E(name)}</b><span>{E(sub)}</span></figcaption>
</figure>'''


def doctors():
    out = []
    for k in SPECS:
        for name, city, photo, vids, reels in SPECS[k]["doctors"]:
            best = max((p for p, _ in reels), default=0)
            out.append((best, k, name, city, photo))
    out.append((0, "pulmo", "Dr. Vaibhav Krishna", "Prayagraj", "p-vaibhav"))
    out.sort(key=lambda x: -x[0])
    return out


FB = {"Dr. Madhuresh Kumar": "https://www.facebook.com/starorthoandmaternity/"}
FB_ICON = '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v7h4v-7h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>'


def doc_card(best, k, name, city, photo):
    url = ig_profile(name)
    fb = FB.get(name)
    spec = SPECS[k]["short"] if k in SPECS else "Pulmonology"
    tag = "a" if url and not fb else "div"
    attrs = f' href="{url}" target="_blank" rel="noopener" aria-label="{E(name)} on Instagram"' if tag == "a" else ""
    pl = f'<p class="dc-pl"><b>{plays_fmt(best)}</b> plays on best reel</p>' if best else '<p class="dc-pl muted">Pulmonology content</p>'
    deg = f'<small>{DEG[name]}</small>' if name in DEG else ""
    if fb:
        go = (f'<span class="dc-links"><a class="dc-go" href="{url}" target="_blank" rel="noopener">{IG_ICON}Instagram</a>'
              f'<a class="dc-go" href="{fb}" target="_blank" rel="noopener">{FB_ICON}Facebook</a></span>')
    else:
        go = f'<span class="dc-go">{IG_ICON}Instagram{ARROW_UR}</span>' if url else ""
    return (f'<{tag} class="dc"{attrs}><div class="dc-ph"><img src="media/{photo}.jpg" alt="{E(name)}" width="600" height="750" loading="lazy"></div>'
            f'<div class="dc-b"><span class="dc-sp">{spec} · {E(city)}</span><b>{E(name)}</b>{deg}{pl}{go}</div></{tag}>')


def originals_row():
    cards = "".join(
        f'<button class="og" type="button" data-play="media/k-{v}.mp4" data-poster="media/{c}.jpg" data-title="{E(t)}">'
        f'<img src="media/{c}.jpg" alt="{E(t)}" width="540" height="960" loading="lazy"><span class="og-ep">{ep}</span>'
        f'<span class="og-pl">{PLAY}</span><span class="og-t"><b>{E(t)}</b>{E(d)}</span></button>'
        for v, c, ep, t, d in ORIGINALS)
    return f'<div class="og-row" data-drag>{cards}</div>'


def video_modal():
    return '''<div class="vm" id="vm" hidden role="dialog" aria-modal="true" aria-label="Video player">
 <button class="vm-x" type="button" data-close aria-label="Close video">×</button>
 <div class="vm-in"><video controls playsinline preload="none"></video></div>
</div>'''


def pricing_section():
    cards = ""
    for i, (n, p, d, f) in enumerate(PLANS):
        pop = i == 1
        msg = f"Hello Karunya Digital, I'm interested in the {n} plan (Rs {p}/month)."
        cards += (f'<article class="pl{" pop" if pop else ""}" data-r>{"<span class=pl-b>Most popular</span>" if pop else ""}<h3>{n}</h3><p class="pl-d">{d}</p>'
                  f'<p class="pl-p"><span>₹</span><b>{p}</b><em>/month</em></p><ul>{"".join(f"<li>{x}</li>" for x in f)}</ul>'
                  f'<a class="btn {"btn-lime" if pop else "btn-ghost"}" href="{wa(msg)}" target="_blank" rel="noopener">Choose {n}</a></article>')
    cards += (f'<article class="pl hosp" data-r><h3>Full hospital</h3><p class="pl-d">Multi-speciality hospitals with many doctors and departments.</p>'
              f'<p class="pl-p"><b class="sm">Custom plan</b></p><ul><li>Every doctor and department</li><li>Hospital and doctor brands together</li><li>Dedicated team</li></ul>'
              f'<a class="btn btn-ghost" href="tel:{CALL}">Call {CALL_TXT}</a></article>')
    return f'''<section class="sec" id="pricing" aria-labelledby="pr-h"><div class="w">
 <div class="sh"><p class="eyebrow" data-r>Pricing</p><h2 id="pr-h" class="h2" data-r>Simple monthly plans.</h2>
 <p class="lead" data-r>Clear prices, no hidden costs. We fine-tune the exact work to your speciality and city on a call.</p></div>
 <div class="plans">{cards}</div>
</div></section>'''


def team_grid():
    cards = ""
    for kind, n, r, d in TEAM:
        av = '<img src="media/founder.webp" alt="Bhanu Pratap Rai" width="420" height="420" loading="lazy">' if kind == "photo" else char(kind)
        link = f'<a class="tl" href="{IG_FOUNDER}" target="_blank" rel="noopener">Instagram{ARROW_UR}</a>' if kind == "photo" else ""
        cards += f'<article class="tm" data-r><div class="tm-av{" ph" if kind == "photo" else ""}">{av}</div><h3>{n}</h3><p class="tm-r">{r}</p><p>{d}</p>{link}</article>'
    return f'<div class="team">{cards}</div>'


# ------------------------------------------------------------------ HOME
def home():
    body = home_body(globals())
    return head("Karunya Digital | Social Media & Marketing Agency for Doctors in India",
                "Karunya Digital is a social media and marketing agency for doctors and hospitals in India: Instagram reels, Google Business Profile, SEO and doctor branding. 50+ doctor clients.",
                "home") + header() + body + footer()


# ------------------------------------------------------------------ SERVICES
def services():
    items = [
        ("reels", "Reels & Shorts", "For doctors who want to educate patients but have no time for scripts and editing.",
         ["Weekly topics from real patient questions", "Hindi, Hinglish or English scripts with a strong first 3 seconds", "Shoot guidance: what to say, where to stand, which light", "Editing, captions, music and thumbnails", "Posting on Instagram Reels and YouTube Shorts"],
         "Not comfortable on camera? Voiceover and motion graphics reels work too."),
        ("gmb", "Google Business Profile", "For clinics that rank low in “near me” searches or have an incomplete profile.",
         ["Complete profile: services, timings, photos, service area", "A Google post every week", "Review replies written in your tone", "Answers to common patient questions", "Monthly report: calls and direction requests"],
         "We do everything that helps you show up first, and show you the results every month."),
        ("seo", "SEO & website", "For doctors who want patients to find accurate answers from them first.",
         ["A fast, mobile-first website or landing page", "Service and condition pages written for patients", "Articles that answer local search questions", "Basic technical SEO and Google Search Console"],
         "Search traffic builds slowly, then keeps working for you every day."),
        ("brand", "Doctor branding", "For doctors with a different photo, name and colour on every platform.",
         ["“Dr. Name × Karunya” co-brand logo", "Your colours and fonts", "Instagram profile, bio and highlight covers", "A consistent look across reels and posts"],
         "A consistent identity helps patients remember you and builds trust faster."),
        ("calendar", "Content calendar & reports", "For doctors who want to know exactly what goes out, and when.",
         ["Monthly content calendar in a clean PDF", "Topics planned around health days and festivals", "Competitor analysis", "Proposals, patient forms and printable material"],
         "Your calendar arrives before the month begins. Change anything you like."),
    ]
    rows = ""
    for i, (k, t, f, ticks, note) in enumerate(items):
        rows += f'''<article class="sd" id="{k}" data-r>
 <span class="n">0{i + 1}</span>
 <div><h2>{t}</h2><p class="sd-f">{f}</p></div>
 <div><ul class="ticks">{"".join(f"<li>{x}</li>" for x in ticks)}</ul><p class="sd-n">{note}</p>
 <a class="tl" href="{wa(f"Hello Karunya Digital, I'd like to know more about {t}.")}" target="_blank" rel="noopener">Ask about this{ARROW}</a></div>
</article>'''
    faq = [
        ("Do you follow the NMC guidelines?", "Yes. Our content follows the NMC's Guidelines on Ethical Advertising and Public Communication (October 2026): patient education first, no superlatives or guarantees, no testimonials, and no patient images. Every post goes live only after your approval."),
        ("How much of my time will this take?", "One call to start. After that, approving the monthly calendar and a little time for shoots. Our team handles the rest."),
        ("How does the shoot work?", "We give you the script and clear guidance on what to say, how to stand and which light to use. Editing, captions, posting and strategy are on us. We don't send camera crews; most doctors shoot on a phone."),
        ("How much does it cost?", "Plans start at ₹20,000 per month, with Growth at ₹25,000 and Authority at ₹40,000. For full hospital marketing, call +91 73176 59337 for a custom plan."),
        ("What will I see every month?", "A clear report with your reach, followers from your city, Google views, calls and direction requests, plus the plan for next month."),
    ]
    faq_html = "".join(f"<details data-r><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    body = f'''<main id="main">
{page_hero("Services", "Everything a clinic needs to be <em>found</em>.", "Five services, one team. You focus on patients; we handle how they find you.")}
<section class="sec tight"><div class="w">{rows}</div></section>
{pricing_section()}
<section class="sec" aria-labelledby="faq-h"><div class="w faq-g">
 <div class="sh"><p class="eyebrow" data-r>FAQ</p><h2 id="faq-h" class="h2" data-r>Questions doctors ask.</h2></div>
 <div class="faq">{faq_html}</div>
</div></section>
</main>
'''
    return head("Social Media Marketing Services for Doctors | Karunya Digital", "Instagram reels, Google Business Profile, SEO and doctor branding for doctors and hospitals. Plans from ₹20,000/month.", "services") + header("Services") + body + footer()


# ------------------------------------------------------------------ WORK
def work():
    reels = [("alka", "Dr. Alka Sony Chaudhary", "Gynaecology, Siwan", 4102136), ("garima", "Dr. Garima Singh", "Gynaecology, Varanasi", 540277),
             ("tanu", "Dr. Tanu Sharma", "IVF & Fertility", 1605452), ("raman", "Dr. Raman Jindal", "Orthopaedics, Meerut", 167524),
             ("neetu", "Dr. Neetu Pal", "Dental, Greater Noida", None)]
    rc = "".join(reel_card(v, n, s) for v, n, s, _ in reels)
    dcards = "".join(doc_card(*d) for d in doctors())
    body = f'''<main id="main">
{page_hero("Work", "Work you can see. Results you can <em>count</em>.", "Karunya Originals, reels we edit for our doctors, and the doctors behind them.")}
<section class="sec og-sec" aria-labelledby="w1"><div class="w"><div class="sh"><p class="eyebrow" data-r>Karunya Originals</p><h2 id="w1" class="h2" data-r>Our own series.</h2></div></div>{originals_row()}</section>
<section class="sec" aria-labelledby="w2"><div class="w"><div class="sh"><p class="eyebrow" data-r>Client reels</p><h2 id="w2" class="h2" data-r>Edited by our team.</h2>
 <p class="lead" data-r>A few of the reels we script and edit. Tap “Sound on” to listen.</p></div></div>
 <div class="rc-row" data-drag>{rc}</div></section>
<section class="sec" aria-labelledby="w3"><div class="w"><div class="sh"><p class="eyebrow" data-r>Karunya Exclusives</p><h2 id="w3" class="h2" data-r>Our doctors.</h2>
 <p class="lead" data-r>Tap a card to see their Instagram. Play counts from 1 November 2026.</p></div>
 <div class="dc-grid">{dcards}</div></div></section>
</main>
{video_modal()}
'''
    return head("Work | Karunya Digital", "Karunya Originals, reels we edit for our doctors, and the doctors behind them.", "work") + header("Work") + body + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    values = [("Healthcare only", "Only doctors and hospitals. We understand your world and your patients."),
              ("Clear reporting", "Every month you see exactly what we did and what changed: views, calls and direction requests."),
              ("The patient's language", "Simple Hindi, Hinglish or English that an ordinary family understands."),
              ("Your approval, always", "Nothing goes live without your yes. Your name, your decision.")]
    vh = "".join(f'<div class="val" data-r><span class="n">0{i + 1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(values))
    th = team_grid()
    cities = "".join(f"<li>{c}</li>" for c in CITIES)
    body = f'''<main id="main">
{page_hero("About", "From the ghats of Kashi, for doctors across <em>India</em>.", "Karunya means compassion. Doctors practise it every day. Our job is to make sure it reaches the patients who need it.")}
<section class="sec tight"><div class="w ab-g">
 <div data-r><h2 class="h2">A healthcare-only studio.</h2></div>
 <div class="prose-sm" data-r>
  <p>Karunya Digital is a healthcare marketing agency based in Varanasi. We work with 50+ doctors and hospitals across India, mostly in growing cities where there are many good doctors but few strong voices online.</p>
  <p>Our team writes the scripts, guides the shoot, edits, designs and manages Google profiles, so doctors can give their full attention to patients.</p>
 </div>
</div></section>
<section class="sec"><div class="w"><div class="sh"><p class="eyebrow" data-r>Principles</p><h2 class="h2" data-r>How we work.</h2></div><div class="vals">{vh}</div></div></section>
<section class="sec"><div class="w"><div class="sh"><p class="eyebrow" data-r>Team</p><h2 class="h2" data-r>One team. Every skill a doctor needs.</h2><p class="lead" data-r>Strategy, scripts, editing, motion graphics, design, Google and client care, all under one roof in Varanasi.</p></div>{th}</div></section>
<section class="sec"><div class="w ab-g">
 <div><p class="eyebrow" data-r>Where we work</p><h2 class="h2" data-r>Nine cities and counting.</h2><ul class="cities" data-r>{cities}</ul></div>
 <div data-r>{reel_card("karunya-ad", "Karunya Digital in 45 seconds", "Made the way we make reels for doctors")}</div>
</div></section>
</main>
'''
    return head("About | Karunya Digital", "Karunya Digital is a healthcare marketing agency in Varanasi, founded by Bhanu Pratap Rai. We work only with doctors and hospitals.", "about") + header("About") + body + footer()


# ------------------------------------------------------------------ CONTACT
def contact():
    needs = ["Reels", "Google profile", "SEO / website", "Branding", "Content calendar", "Not sure yet"]
    chips = "".join(f'<label><input type="checkbox" name="need" value="{n}"><span>{n}</span></label>' for n in needs)
    maps = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote("Karunya Digital Taktakpur Road Varanasi")
    body = f'''<main id="main">
{page_hero("Contact", "Let's <em>talk</em>.", "One message is enough. We'll understand your practice and suggest what's right for your clinic.")}
<section class="sec tight"><div class="w ct-g">
 <div class="ct-l">
  <a class="ct-wa" href="{wa()}" target="_blank" rel="noopener" data-r><span class="eyebrow">Fastest</span><b>Message us on WhatsApp</b><span class="ct-n">{WA_ICON}{WA_TXT}{ARROW}</span></a>
  <dl class="ct-i" data-r>
   <div><dt>Call</dt><dd><a href="tel:{CALL}">{CALL_TXT}</a></dd></div>
   <div><dt>Hours</dt><dd>Mon–Sat, 10am–7pm IST</dd></div>
   <div><dt>Office</dt><dd>{ADDR}<br><a class="tl" href="{maps}" target="_blank" rel="noopener">Open in Google Maps{ARROW_UR}</a></dd></div>
   <div><dt>Instagram</dt><dd><a href="{IG_KARUNYA}" target="_blank" rel="noopener">@karunyadigital</a> · <a href="{IG_FOUNDER}" target="_blank" rel="noopener">@bhanuhelpsdoctors</a></dd></div>
  </dl>
 </div>
 <form class="form" id="wa-form" novalidate data-r>
  <h2>Tell us about your practice</h2>
  <p class="muted">This prepares a WhatsApp message you can edit before sending.</p>
  <div class="two"><div><label for="f-name">Name</label><input id="f-name" name="name" type="text" autocomplete="name" placeholder="Dr. ..."></div>
  <div><label for="f-spec">Speciality</label><input id="f-spec" name="spec" type="text" placeholder="Gynaecology, Ortho, IVF..."></div></div>
  <div><label for="f-city">City</label><input id="f-city" name="city" type="text" autocomplete="address-level2" placeholder="Varanasi, Lucknow..."></div>
  <fieldset><legend>What do you need?</legend><div class="chips">{chips}</div></fieldset>
  <div><label for="f-msg">Anything else? (optional)</label><textarea id="f-msg" name="msg" placeholder="For example: opening a new clinic."></textarea></div>
  <p class="err" role="alert"></p>
  <button class="btn btn-lime" type="submit">{WA_ICON}Prepare WhatsApp message</button>
 </form>
</div></section>
</main>
'''
    return head("Contact | Karunya Digital", "Talk to Karunya Digital on WhatsApp or by phone. Taktakpur Road, Varanasi. Mon–Sat, 10am–7pm.", "contact") + header("Contact") + body + footer(cta=False)


# ------------------------------------------------------------------ SPECIALTY
def spec_page(k):
    sp = SPECS[k]
    msg = f"Hello Karunya Digital, I'm a {sp['who']} and I'd like to talk about reels and marketing for my clinic."
    dcards = "".join(doc_card(best, kk, n, c, ph) for best, kk, n, c, ph in doctors() if kk == k)
    vids = "".join(reel_card(v, name, city) for name, city, photo, vv, reels in sp["doctors"] for v in vv)
    topics = "".join(f"<li>{t}</li>" for t in sp["topics"])
    how = "".join(f'<div class="val" data-r><span class="n">0{i + 1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(sp["how"]))
    others = "".join(f'<a class="oth" href="{SPECS[o]["file"]}"><b>{SPECS[o]["name"]}</b><span>{plays_fmt(spec_total(o))} plays</span>{ARROW}</a>' for o in SPECS if o != k)
    tot = spec_total(k)
    body = f'''<main id="main">
<section class="ph"><div class="w ph-g">
 <div><p class="eyebrow up"><a href="index.html">Home</a> / {sp["name"]}</p>
 <h1 class="ph-h up d1">{sp["h1"]}</h1><p class="ph-p up d2">{sp["lead"]}</p>
 <div class="row up d3"><a class="btn btn-lime" href="{wa(msg)}" target="_blank" rel="noopener">{WA_ICON}Talk on WhatsApp</a><a class="btn btn-ghost" href="audit.html">Get a free check</a></div></div>
 <div class="ph-stat up d2"><p class="st-n"><span>{plays_fmt(tot).split()[0]}</span><em>{(" " + plays_fmt(tot).split()[1]) if " " in plays_fmt(tot) else ""}</em></p><p class="st-l">plays on our {sp["short"]} doctors' best reels</p></div>
</div></section>
<section class="sec tight"><div class="w"><div class="sh"><p class="eyebrow" data-r>Karunya Exclusives</p><h2 class="h2" data-r>Our {sp["short"]} doctors.</h2></div><div class="dc-grid">{dcards}</div></div></section>
{f'<section class="sec"><div class="w"><div class="sh"><p class="eyebrow" data-r>Reels</p><h2 class="h2" data-r>Edited by our team.</h2></div></div><div class="rc-row" data-drag>{vids}</div></section>' if vids else ''}
<section class="sec"><div class="w ab-g">
 <div><p class="eyebrow" data-r>Topics</p><h2 class="h2" data-r>What your patients search.</h2><p class="lead" data-r>Every question is a reel. Every reel is a way for the right patient to find you.</p></div>
 <ul class="topics" data-r>{topics}</ul>
</div></section>
<section class="sec"><div class="w"><div class="sh"><p class="eyebrow" data-r>Approach</p><h2 class="h2" data-r>What we do differently for {sp["short"]}.</h2></div><div class="vals three">{how}</div></div></section>
<section class="sec tight"><div class="w"><p class="eyebrow">Other specialties</p><div class="oths">{others}</div></div></section>
</main>
'''
    return head(f"Marketing for {sp['name']} Doctors | Karunya Digital", f"Instagram reels, Google Business Profile and SEO for {sp['name']} doctors. Our doctors' best reels: {plays_fmt(tot)} plays.", k) + header(sp["short"]) + body + footer()


# ------------------------------------------------------------------ AUDIT
def audit_page():
    b = audit_form()
    opts = "".join(f"<option>{x}</option>" for x in ["Gynaecology", "IVF / Fertility", "Orthopaedics", "Dental", "Pulmonology", "Paediatrics", "General physician", "Hospital", "Other"])
    gauge = '<svg viewBox="0 0 200 200" aria-hidden="true"><circle cx="100" cy="100" r="84" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="12"/><circle class="g-arc" cx="100" cy="100" r="84" fill="none" stroke="#D1FF42" stroke-width="12" stroke-linecap="round" pathLength="100" stroke-dasharray="100" stroke-dashoffset="100" transform="rotate(-90 100 100)"/></svg>'
    body = f'''<main id="main">
<section class="ph au-hero"><div class="w au-g">
 <div>
  <p class="eyebrow up">Free for doctors · 2 minutes</p>
  <h1 class="ph-h up d1">How easy is it for patients to <em>find you</em>?</h1>
  <p class="ph-p up d2">Get a free score for your Google profile and Instagram, with the three fixes that matter most. No call, no cost.</p>
  <ul class="au-pts up d3"><li>10 quick questions</li><li>Score out of 100</li><li>Your top 3 fixes</li></ul>
 </div>
 <form id="start" class="card au-start up d2" novalidate>
  <h2>Start your free check</h2>
  <div><label for="s-name">Your name</label><input id="s-name" name="name" type="text" autocomplete="name" placeholder="Dr. ..."></div>
  <div><label for="s-phone">WhatsApp number</label><input id="s-phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" placeholder="10-digit number"></div>
  <div class="two"><div><label for="s-spec">Speciality</label><select id="s-spec" name="speciality">{opts}</select></div>
  <div><label for="s-city">City</label><input id="s-city" name="city" type="text" autocomplete="address-level2" placeholder="Varanasi"></div></div>
  <p class="s-err err" role="alert"></p>
  <button class="btn btn-lime" type="submit">Start my free check{ARROW}</button>
  <p class="muted sm">Your report is shared only with you on WhatsApp. No spam.</p>
 </form>
</div></section>
<section class="sec tight" id="questions" hidden><div class="w au-q">
 <form id="audit" class="audit" novalidate>
  <div class="a-step"><h2><span>01</span>Your Google profile</h2>{b["g"]}</div>
  <div class="a-step"><h2><span>02</span>Your Instagram</h2>{b["i"]}</div>
  <p class="a-err err" role="alert"></p>
  <button class="btn btn-lime" type="submit">Show my score{ARROW}</button>
 </form>
 <aside class="a-side" aria-live="polite"><div class="card a-card">
  <div class="gauge">{gauge}<div class="g-num"><b data-score>0</b><span>/100</span></div></div>
  <p class="a-level" data-level>Answer the questions to see your score</p>
  <div class="a-bars"><div><span>Google</span><i><em data-bar="g"></em></i><b data-sub="g">0/50</b></div><div><span>Instagram</span><i><em data-bar="i"></em></i><b data-sub="i">0/50</b></div></div>
  <p class="a-prog muted"><b data-answered>0</b> of 10 answered</p>
 </div></aside>
</div></section>
<section class="sec" id="result" hidden><div class="w">
 <p class="eyebrow">Your result</p>
 <h2 class="h2"><span data-greet></span>, here are your top 3 fixes</h2>
 <ol class="fixes" data-fixes></ol>
 <div class="card a-lead"><div><h3>Your report is with the Karunya team.</h3><p class="muted">We'll review your actual Google profile and Instagram and share a detailed plan on WhatsApp.</p></div>
 <div class="row"><a class="btn btn-lime" data-wa-now href="{wa()}" target="_blank" rel="noopener">{WA_ICON}Chat on WhatsApp now</a><a class="btn btn-ghost" href="services.html#pricing">See plans</a></div></div>
</div></section>
<form name="free-check" data-netlify="true" netlify-honeypot="bot-field" hidden>
 <input name="bot-field"><input name="stage"><input name="name"><input name="phone"><input name="speciality"><input name="city">
 <input name="score"><input name="google_score"><input name="instagram_score"><textarea name="answers"></textarea>
</form>
</main>
'''
    return head("Free Google + Instagram Check for Doctors | Karunya Digital", "A free 2-minute check of your clinic's Google Business Profile and Instagram. Get a score out of 100 and your top 3 fixes.", "audit") + header("Free check") + body + footer(cta=False)


def page404():
    body = f'''<main id="main"><section class="ph nf"><div class="w">
 <p class="nf-n up">404</p>
 <h1 class="ph-h up d1">This page took a <em>wrong turn</em>.</h1>
 <p class="ph-p up d2">The page you're looking for doesn't exist. Your clinic, on the other hand, should never be this hard to find.</p>
 <div class="row up d3"><a class="btn btn-lime" href="index.html">Take me home{ARROW}</a><a class="btn btn-ghost" href="audit.html">Check how findable my clinic is</a></div>
</div></section></main>
'''
    h = head("Page not found | Karunya Digital", "This page doesn't exist. Head back to Karunya Digital.", "404")
    h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/">\n<meta name="robots" content="noindex">')
    return h + header() + body + footer(cta=False)


# ------------------------------------------------------------------ BLOG
def nice_date(d):
    try:
        return datetime.date.fromisoformat(d).strftime("%-d %B %Y")
    except Exception:
        return d


def post_card(p):
    return (f'<a class="pc" href="{p["slug"]}.html" data-r><div class="pc-i"><img src="media/blog/{p["slug"]}.jpg" alt="" width="1200" height="630" loading="lazy"></div>'
            f'<span class="pc-c">{E(p["category"])} · {p["minutes"]} min read</span><h3>{E(p["title"])}</h3><p>{E(p.get("description", ""))}</p>'
            f'<span class="tl">Read article{ARROW}</span></a>')


def blog_index(posts):
    cards = "".join(post_card(p) for p in posts)
    body = f'''<main id="main">
{page_hero("Blog", "Guides for doctors who want to be <em>found</em>.", "Google, Instagram, reels, SEO and the NMC rules, in plain language.")}
<section class="sec tight"><div class="w"><div class="pcs">{cards}</div></div></section>
</main>
'''
    return head("Blog: Healthcare Marketing Guides for Doctors | Karunya Digital", "Practical guides for doctors in India on Google Business Profile, Instagram reels, SEO, NMC rules and patient trust.", "blog") + header("Blog") + body + footer()


def blog_post(p, posts):
    others = [o for o in posts if o["slug"] != p["slug"]][:3]
    rel = "".join(post_card(o) for o in others)
    ld = json.dumps({"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"], "description": p.get("description", ""),
                     "datePublished": p.get("date", ""), "image": f"https://karunyadigital.online/media/blog/{p['slug']}.jpg",
                     "author": {"@type": "Person", "name": "Bhanu Pratap Rai", "url": IG_FOUNDER},
                     "publisher": {"@type": "Organization", "name": "Karunya Digital", "logo": {"@type": "ImageObject", "url": "https://karunyadigital.online/assets/icon-blue-512.png"}},
                     "mainEntityOfPage": f"https://karunyadigital.online/{p['slug']}.html"})
    body = f'''<main id="main">
<section class="ph post-h"><div class="w narrow">
 <p class="eyebrow up"><a href="blog.html">Blog</a> / {E(p["category"])}</p>
 <h1 class="ph-h sm up d1">{E(p["title"])}</h1>
 <div class="by up d2"><img src="media/founder.webp" alt="" width="44" height="44"><span><b>Bhanu Pratap Rai</b>{nice_date(p.get("date", ""))} · {p["minutes"]} min read</span></div>
</div></section>
<section class="sec tight"><div class="w post-g">
 <article class="prose"><img class="post-cover" src="media/blog/{p["slug"]}.jpg" alt="{E(p["title"])}" width="1200" height="630">{p["html"]}</article>
 <aside class="post-s"><div class="card">
  <p class="eyebrow">Free for doctors</p><h3>How findable is your clinic?</h3><p class="muted">Your Google + Instagram score and top 3 fixes in 2 minutes.</p>
  <a class="btn btn-lime" href="audit.html">Get my free check</a><a class="btn btn-ghost" href="{wa()}" target="_blank" rel="noopener">{WA_ICON}WhatsApp us</a>
 </div></aside>
</div></section>
{f'<section class="sec"><div class="w"><div class="sh"><h2 class="h2" data-r>Keep reading.</h2></div><div class="pcs">{rel}</div></div></section>' if rel else ''}
</main>
'''
    h = head(f"{p['title']} | Karunya Digital", p.get("description", ""), p["slug"], og_img=f"media/blog/{p['slug']}.jpg", extra=f'\n<script type="application/ld+json">{ld}</script>')
    return h + header("Blog") + body + footer()


# ------------------------------------------------------------------ WRITE
POSTS = load_posts()
files = [("index.html", home()), ("services.html", services()), ("work.html", work()), ("about.html", about()),
         ("contact.html", contact()), ("audit.html", audit_page()), ("404.html", page404()), ("blog.html", blog_index(POSTS))]
files += [(SPECS[k]["file"], spec_page(k)) for k in SPECS]
files += [(p["slug"] + ".html", blog_post(p, POSTS)) for p in POSTS]
for fn, html in files:
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as fh:
        fh.write(html)
pages = [""] + [f for f, _ in files if f not in ("index.html", "404.html")]
with open(os.path.join(OUT, "sitemap.xml"), "w") as fh:
    fh.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
             + "".join(f"<url><loc>https://karunyadigital.online/{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in pages) + "</urlset>")
print("built", len(files), "pages")
