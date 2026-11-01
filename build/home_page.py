"""Home page (v4): logo shimmer + kinetic line on an Elite Blue canvas, three client journeys, big numbers.

Numbers (all real, combined to show the full reach):
- Instagram: 3.26 crore plays on our doctors' public reels (scan of 1 Nov 2026).
- Google Business Profile, 23 doctor & hospital profiles we manage, Nov 2024 - Oct 2026 (Windsor.ai / GBP API):
  9,39,426 profile views, 22,830 calls, 29,561 direction requests.
  -> 3.26 Cr + 0.094 Cr = 3.35 Cr views; 22,830 + 29,561 = 52,391 calls & direction requests.
"""

BIG = [("3.35", " Cr+", "views of our doctors on Instagram and Google"),
       ("52,000", "+", "patients called or asked for directions"),
       ("50", "+", "doctors and hospitals across India")]

WORDS = ["Gynaecologists", "Orthopaedic surgeons", "IVF specialists", "Dentists", "Pulmonologists", "Hospitals"]

PILLS = [("heart", "1,204 likes"), ("follow", "New follower from Varanasi"), ("call", "Call from Google"),
         ("pin", "Directions requested"), ("play", "Reel crossed 1 lakh"), ("follow", "New follower from Meerut"),
         ("call", "Appointment enquiry"), ("heart", "Saved by 312 people")]

ICON = {
    "heart": '<svg viewBox="0 0 24 24"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z" fill="currentColor"/></svg>',
    "follow": '<svg viewBox="0 0 24 24"><circle cx="10" cy="8" r="4" fill="currentColor"/><path d="M2 20c0-4 3.6-6 8-6s8 2 8 6M19 7v6M16 10h6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>',
    "call": '<svg viewBox="0 0 24 24"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" fill="currentColor"/><circle cx="12" cy="10" r="2.6" fill="#0251B0"/></svg>',
    "play": '<svg viewBox="0 0 24 24"><path d="M8 5l12 7-12 7z" fill="currentColor"/></svg>',
}


def hero_bg():
    """A growth curve that draws itself, a dot riding it, and social signals floating up."""
    pills = "".join(f'<span class="pill p{i}">{ICON[k]}{t}</span>' for i, (k, t) in enumerate(PILLS))
    path = "M0 500 C200 492 330 470 470 430 S720 330 850 250 1060 90 1200 40"
    return f"""<div class="hb" aria-hidden="true">
 <svg class="hb-curve" viewBox="0 0 1200 520" preserveAspectRatio="none">
  <defs><linearGradient id="cg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#D1FF42" stop-opacity=".2"/><stop offset="1" stop-color="#D1FF42" stop-opacity="0"/></linearGradient></defs>
  <path class="hb-area" d="{path} L1200 520 L0 520 Z" fill="url(#cg)"/>
  <path class="hb-line" d="{path}" fill="none" stroke="#D1FF42" stroke-width="2.5" pathLength="1" vector-effect="non-scaling-stroke"/>
 </svg>
 <div class="pills">{pills}</div>
</div>"""


def logo_mark():
    return '<div class="lm" aria-hidden="true"><span class="lm-word"></span></div>'


def journeys():
    garima = """<article class="jr jr-garima" data-r>
 <div class="jr-vis v-map" aria-hidden="true">
  <svg viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice"><path d="M-10 150 C60 120 90 160 150 120 S240 60 310 70" fill="none" stroke="#B0E0E6" stroke-width="16" stroke-linecap="round"/>
   <g stroke="#C7D1DD" stroke-width="1.5"><path d="M20 20 L120 190"/><path d="M90 0 L210 200"/><path d="M0 70 L300 40"/><path d="M0 120 L300 160"/><path d="M200 0 L260 200"/><path d="M0 30 L300 110"/></g>
   <circle class="rip" cx="150" cy="100" r="12"/><circle class="rip" cx="150" cy="100" r="12"/><circle class="rip" cx="150" cy="100" r="12"/>
   <circle cx="150" cy="100" r="8" fill="#0251B0" stroke="#fff" stroke-width="3"/></svg>
  <span class="map-l">Varanasi</span>
 </div>
 <div class="jr-b"><p class="jr-who"><img src="media/p-garima.jpg" alt="" width="40" height="40" loading="lazy"><span><b>Dr. Garima Singh</b>Gynaecologist, Varanasi</span></p>
  <h3>One month in, Banaras found her.</h3>
  <p>Her very first reel reached families across Varanasi. In the first month, people who found her online started walking into her hospital.</p>
  <p class="jr-n"><b>5.4 lakh</b> views on her first big reel</p></div>
</article>"""
    alka = """<article class="jr jr-alka" data-r>
 <div class="jr-vis v-trust" aria-hidden="true">
  <div class="tq"><span class="q1">“Will social media really work for a doctor?”</span><span class="q2">“Patients tell me they found me on Instagram.”</span></div>
  <div class="tbar"><i></i></div>
  <div class="trow"><span>Doubt</span><span>Trust</span></div>
 </div>
 <div class="jr-b"><p class="jr-who"><img src="media/p-alka.jpg" alt="" width="40" height="40" loading="lazy"><span><b>Dr. Alka Sony Chaudhary</b>Gynaecologist, Siwan</span></p>
  <h3>From doubt to her biggest source of new patients.</h3>
  <p>She didn't trust social media at first. We kept her creating, week after week. Today it is one of the biggest ways new patients reach her.</p>
  <p class="jr-n"><b>41 lakh</b> views on a single reel</p></div>
</article>"""
    manisha = """<article class="jr jr-manisha" data-r>
 <div class="jr-vis v-calls" aria-hidden="true">
  <span class="cw w1"></span><span class="cw w2"></span>
  <div class="cph"><span class="cring">""" + ICON["call"] + """</span><b data-tick="4131">4,131</b><span>calls from Google</span></div>
 </div>
 <div class="jr-b"><p class="jr-who"><img src="media/p-manisha.jpg" alt="" width="40" height="40" loading="lazy"><span><b>Dr. Manisha Chaudhary</b>Gynaecologist, Meerut</span></p>
  <h3>New city, new hospital, a busy OPD.</h3>
  <p>She had just joined a hospital in a city where few people knew her. Today most of her new patients come through Instagram and her Google profile.</p>
  <p class="jr-n"><b>1.29 lakh</b> Google views in two years</p></div>
</article>"""
    return garima + alka + manisha


ORBIT = [("play", "Reels"), ("pin", "Google Maps"), ("search", "Search"), ("heart", "Trust"), ("call", "Calls"), ("follow", "Followers")]
ICON["search"] = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M16 16l4.5 4.5" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>'


def brand_motion():
    """Karunya's own motion piece: the K mark at the centre, everything a patient touches orbiting it."""
    inner = "".join(f'<span class="ob" style="--a:{i * 120}deg"><i>{ICON[k]}</i><em>{t}</em></span>' for i, (k, t) in enumerate(ORBIT[:3]))
    outer = "".join(f'<span class="ob" style="--a:{60 + i * 120}deg"><i>{ICON[k]}</i><em>{t}</em></span>' for i, (k, t) in enumerate(ORBIT[3:]))
    return f"""<div class="bm-orb" aria-hidden="true">
  <div class="orb o1">{inner}</div><div class="orb o2">{outer}</div>
  <div class="bm-core"><img src="assets/k-lime.png" alt="" width="120" height="120"></div>
 </div>"""


def home_body(ctx):
    g = ctx
    ARROW, WA_ICON, wa, IG_FOUNDER = g["ARROW"], g["WA_ICON"], g["wa"], g["IG_FOUNDER"]
    big = "".join(f'<div class="bn" data-r><p class="bn-n"><span>{n}</span>{s}</p><p class="bn-l">{l}</p></div>' for n, s, l in BIG)
    words = "".join(f'<span class="kw">{w}</span>' for w in WORDS)
    pf = g["plays_fmt"]
    ex = "".join(f'<li class="ex"><img src="media/{ph}.jpg" alt="{n}" width="300" height="375" loading="lazy"><span class="ex-b"><b>{n}</b>{g["SPECS"][k]["short"] if k in g["SPECS"] else "Pulmonology"} · {c}{f"<em>{pf(best)} views</em>" if best else ""}</span></li>'
                 for best, k, n, c, ph in g["doctors"]())
    what = [("Reels patients actually watch", "We study what your patients ask, write the script, guide your shoot on your phone, then edit, caption and post."),
            ("A Google profile that rings", "Complete, active and accurate, so you show up when someone nearby searches for your speciality."),
            ("Search pages that answer first", "Website pages and articles written for real patient questions in your city.")]
    what_html = "".join(f'<li data-r><h3>{t}</h3><p>{d}</p></li>' for t, d in what)
    posts = g["POSTS"][:3]
    blog = ""
    if posts:
        f0 = posts[0]
        blog = (f'<a class="bp-main" href="{f0["slug"]}.html" data-r><img src="media/blog/{f0["slug"]}.jpg" alt="" width="1200" height="630" loading="lazy">'
                f'<span class="bp-c">{f0["category"]} · {f0["minutes"]} min read</span><h3>{f0["title"]}</h3><p>{f0.get("description", "")}</p></a>')
        blog += '<div class="bp-side">' + "".join(
            f'<a class="bp-s" href="{p["slug"]}.html" data-r><img src="media/blog/{p["slug"]}.jpg" alt="" width="1200" height="630" loading="lazy"><span><span class="bp-c">{p["category"]}</span><b>{p["title"]}</b></span></a>'
            for p in posts[1:]) + '</div>'
    return f"""<main id="main">
<section class="hero" aria-labelledby="hero-h" data-trail="ribbon">
 <div class="canvas">
  {hero_bg()}
  <div class="hero-in">
   {logo_mark()}
   <h1 id="hero-h" class="kin"><span class="kin-slot" aria-hidden="true">{words}</span><span class="sr">Doctors and hospitals </span><span class="kin-rest">become the name patients trust.</span></h1>
   <p class="hero-p">Reels, Google and search for doctors. One team in Varanasi does the work. You approve every post.</p>
   <div class="row hero-cta"><a class="btn btn-lime" href="audit.html">Get a free check</a><a class="btn btn-line" href="{wa()}" target="_blank" rel="noopener">{WA_ICON}WhatsApp us</a></div>
  </div>
  <div class="bns">{big}</div>
 </div>
 <p class="note w">Instagram: public reels of our client doctors, 1 Nov 2026. Google: Business Profile data of the 23 doctor and hospital profiles we manage, Nov 2024 to Oct 2026.</p>
</section>

<section class="bm" aria-labelledby="bm-h" data-trail="spark">
 <div class="w bm-g">
  <div class="bm-t">
   <h2 id="bm-h" class="bm-h"><span class="bm-l l1">You heal.</span><span class="bm-l l2">We get you heard.</span></h2>
   <p>Every reel, Google post and search page we make has one job: when a patient in your city looks for help, they find you, and they trust what they see.</p>
  </div>
  {brand_motion()}
 </div>
</section>

<section class="sec exs" aria-labelledby="ex-h" data-trail="dots">
 <div class="w sh-row"><div class="sh"><p class="eyebrow">Karunya Exclusives</p><h2 id="ex-h" class="h2">The doctors who trust us.</h2></div><a class="tl" href="work.html">See all{ARROW}</a></div>
 <div class="marq ex-m"><ul class="marq-t">{ex}{ex}</ul></div>
</section>

<section class="sec og-sec soft" aria-labelledby="og-h" data-trail="comet">
 <div class="w sh-row"><div class="sh"><p class="eyebrow">Karunya Originals</p><h2 id="og-h" class="h2">Our own series, made for doctors.</h2></div>
 <div class="arrows"><button type="button" class="arw" data-scroll="-1" aria-label="Previous episodes">←</button><button type="button" class="arw" data-scroll="1" aria-label="Next episodes">→</button></div></div>
 {g["originals_row"]().replace('class="og-row" data-drag', 'class="og-row" data-drag data-scroller')}
</section>

<section class="sec" aria-labelledby="ad-h" data-trail="ribbon">
 <div class="w ad-g">
  <div class="ad-v" data-r>{g["reel_card"]("karunya-ad", "Karunya Digital in 45 seconds", "Made the way we make reels for doctors")}</div>
  <div data-r><p class="eyebrow">Watch</p><h2 id="ad-h" class="h2">Karunya Digital in 45 seconds.</h2>
   <p class="lead">Made exactly the way we make reels for our doctors: a clear hook, a simple story and a reason to act. Tap “Sound on”.</p>
   <div class="row" style="margin-top:26px"><a class="btn btn-lime" href="{wa()}" target="_blank" rel="noopener">{WA_ICON}Make one like this for me</a></div></div>
 </div>
</section>

<section class="sec soft" aria-labelledby="wd-h" data-trail="dots">
 <div class="w wd-g">
  <h2 id="wd-h" class="h2" data-r>Everything a patient sees before they call you.</h2>
  <ul class="wd">{what_html}</ul>
 </div>
</section>

<section class="sec" aria-labelledby="tm-h" data-trail="spark">
 <div class="w">
  <div class="sh"><p class="eyebrow">The team</p><h2 id="tm-h" class="h2" data-r>One team. Every skill a doctor needs.</h2>
  <p class="lead" data-r>Strategy, scripts, editing, motion graphics, design, Google and client care, all under one roof in Varanasi.</p></div>
  {g["team_grid"]()}
 </div>
</section>

<section class="sec soft" aria-labelledby="fd-h" data-trail="comet">
 <div class="w fd" data-r>
  <img src="media/founder.webp" alt="Bhanu Pratap Rai" width="420" height="420" loading="lazy">
  <div>
   <h2 id="fd-h" class="fd-q">“We work only with doctors. Honest work every week, and a report you can understand in two minutes.”</h2>
   <p class="fd-n"><b>Bhanu Pratap Rai</b>Founder, Karunya Digital · <a href="{IG_FOUNDER}" target="_blank" rel="noopener">@bhanuhelpsdoctors</a></p>
  </div>
 </div>
</section>

<section class="sec" aria-labelledby="bl-h" data-trail="dots">
 <div class="w">
  <div class="sh-row"><div class="sh"><p class="eyebrow">From the blog</p><h2 id="bl-h" class="h2">Guides for doctors who want to be found.</h2></div><a class="tl" href="blog.html">All articles{ARROW}</a></div>
  <div class="bp">{blog}</div>
 </div>
</section>

<section class="sec tight" aria-label="Plans and NMC">
 <div class="w duo">
  <a class="duo-c" href="services.html#pricing" data-r><p class="duo-k">Plans</p><p class="duo-h">From ₹20,000 a month</p><span class="tl">See plans{ARROW}</span></a>
  <a class="duo-c blue" href="blog-nmc-new-guidelines-doctors-social-media.html" data-r data-trail="spark"><p class="duo-k">NMC ready</p><p class="duo-h">Every post follows the October 2026 NMC guidelines</p><span class="tl">Read the guide{ARROW}</span></a>
 </div>
</section>
</main>
{g["video_modal"]()}
"""
