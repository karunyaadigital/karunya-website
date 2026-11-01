"""Specialty data, reel cards and specialty motion art."""
from art import BLUE, NAVY, LIME, SKY, GREY, PAPER, WHITE, MID, DEEP, SKIN

IG = "https://www.instagram.com/p/"

HANDLE = {
    "Dr. Garima Singh": "drgarimasinghgynaecologist",
    "Dr. Tanima Shukla": "dr_tanimas_clinic",
    "Dr. Raman Jindal": "drramanjindal_orthopedic",
    "Dr. Tanu Sharma": "fertilitywithdrtanu",
    "Dr. Madhuresh Kumar": "dr.madhuresh_kumar_siwan",
    "Dr. Manisha Chaudhary": "drmanishachaudhary_meerut",
    "Dr. Rishabh Jaiswal": "ortho_dr.rishabh",
    "Dr. Sunaina Gupta": "drsunainadentalcare",
    "Dr. Alka Sony Chaudhary": "dr_alkasonychaudhary_siwan",
}


def ig_profile(name):
    h = HANDLE.get(name)
    return f"https://www.instagram.com/{h}/" if h else None


DEG = {
    "Dr. Garima Singh": "MBBS, MS (Obs & Gynae), KGMU; FMAS",
    "Dr. Tanu Sharma": "MBBS, MS (Obs & Gynae), Fellowship in Reproductive Medicine",
    "Dr. Alka Sony Chaudhary": "MD (Obs & Gynae), KGMC Lucknow",
    "Dr. Rishabh Jaiswal": "MBBS, MS (Ortho), DNB (Ortho), FJJR",
    "Dr. Madhuresh Kumar": "MBBS, MS (Ortho), KGMC",
    "Dr. Manisha Chaudhary": "MBBS, MS (Obs & Gynae)",
    "Dr. Neetu Pal": "BDS, MDS",
    "Dr. Tanima Shukla": "MBBS, MD (Obs & Gynae)",
    "Dr. Harshit Singh": "MBBS, DGO, DNB (Obs & Gynae)",
    "Dr. Vaibhav Krishna": "MBBS, MD (Respiratory Medicine)",
    "Dr. Raman Jindal": "MBBS, MS (Orthopaedics)",
    "Dr. Sunaina Gupta": "BDS, Diploma in Dental Implants",
}


def plays_fmt(n):
    if n >= 10000000:
        return f"{n / 10000000:.2f} crore"
    if n >= 100000:
        return f"{n / 100000:.2f} lakh"
    s = str(n)
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:]); head = head[:-2]
        if head: parts.insert(0, head)
        return ",".join(parts) + "," + tail
    return s


# name, city, photo, video(s), reels [(plays, url)]
SPECS = {
    "gynae": dict(
        file="gynae.html", short="Gynae", name="Gynaecology & Obstetrics", who="gynaecologist",
        h1="The doctor every mother trusts first.",
        lead="Pregnancy, periods, PCOS, delivery. These are the questions families search late at night. We turn your knowledge into clear answers they can trust.",
        doctors=[
            ("Dr. Manisha Chaudhary", "Meerut", "p-manisha", [], [(785706, IG + "DaOGOq8DGIV/"), (279644, IG + "DZ-K_xnledw/")]),
            ("Dr. Garima Singh", "Varanasi", "p-garima", ["garima"], [(540277, IG + "DdLt6EJlSV0/"), (279150, IG + "DcvbVXfFcfl/")]),
            ("Dr. Alka Sony Chaudhary", "Siwan", "p-alka", ["alka"], [(4102136, IG + "DcDxddjzYnv/"), (3856640, IG + "DfEonRcj-PL/")]),
            ("Dr. Tanima Shukla", "Lucknow", "p-tanima", [], [(64422, IG + "DWlAwwyDzsc/"), (47878, IG + "DZUSLPkgvVe/")]),
        ],
        topics=["Late periods: what to do", "Early signs of PCOS", "Confusing pregnancy test results", "How to calculate a due date", "Normal delivery or C-section?", "What to eat during pregnancy", "Recovery after a C-section", "Changes during menopause", "When is discharge normal?"],
        how=[("Sensitive topics, handled with dignity", "Periods, PCOS and infertility explained so a mother and daughter can watch together."),
             ("Myths vs facts", "Pregnancy and delivery myths cleared in simple words, so families feel calm, not scared."),
             ("Found in “near me” search", "A complete Google profile and website pages, so women nearby find accurate information first.")],
    ),
    "ivf": dict(
        file="ivf.html", short="IVF", name="IVF & Fertility", who="IVF / fertility specialist",
        h1="Hope, told honestly.",
        lead="IVF is one of the most emotional decisions a family makes. Couples research quietly for months. We give them your clear, claim-free guidance at every step.",
        doctors=[
            ("Dr. Tanu Sharma", "IVF Specialist", "p-tanu", ["tanu"], [(1605452, IG + "DakuYFujxOH/"), (178935, IG + "DcyPaDMElSg/")]),
        ],
        topics=["When to consider egg freezing", "What your AMH report means", "IUI or IVF?", "Common IVF myths", "Male infertility", "Questions to ask at your first visit", "After embryo transfer", "Age and fertility"],
        how=[("Honest and NMC-safe", "No success-rate claims. Just the process, realistic hope and the right information for couples."),
             ("No patient stories", "No testimonials or patient images, ever. Only your expertise, explained clearly."),
             ("Content for a long journey", "IVF patients follow for months. We build series that guide them step by step.")],
    ),
    "ortho": dict(
        file="ortho.html", short="Ortho", name="Orthopaedics & Spine", who="orthopaedic / spine surgeon",
        h1="When the pain starts, they remember your name.",
        lead="Knee pain, back pain, slip disc. Almost every home has someone who suffers. When they search, your voice should ease their fear of surgery.",
        doctors=[
            ("Dr. Rishabh Jaiswal", "Max Hospital, Lucknow", "p-rishabh", [], [(666198, IG + "DZ0BZIkgvgk/"), (48464, IG + "DaUvKZtCOZo/")]),
            ("Dr. Raman Jindal", "Sangeeta Hospital, Meerut", "p-raman", ["raman"], [(167524, IG + "DaAVDuhpLP-/"), (10219, IG + "DXy5808ANDH/")]),
            ("Dr. Madhuresh Kumar", "Siwan", "p-madhuresh", [], [(89515, IG + "DbDcUCYyDDg/"), (6761, IG + "DbSZAsFycZt/")]),
        ],
        topics=["Knee pain: when to see a doctor", "Fear of knee replacement", "Signs of a slip disc", "Back pain from desk jobs", "Sciatica", "Recovery after a fracture", "Exercise with arthritis", "Neck pain and phone use"],
        how=[("Less fear of surgery", "Animation and plain language that show what really happens in an operation."),
             ("Made to be shared", "Content that sons and daughters forward to their parents."),
             ("Grow the doctor and the hospital", "The hospital's name and the doctor's reputation rise together.")],
    ),
    "dental": dict(
        file="dental.html", short="Dental", name="Dental", who="dentist",
        h1="The clinic your whole city smiles about.",
        lead="Dental content is among the most shared in healthcare. One good reel can reach lakhs of people. One of Dr. Sunaina Gupta's reels has crossed 54 lakh plays.",
        doctors=[
            ("Dr. Sunaina Gupta", "Agra", "p-sunaina", [], [(5473055, IG + "DUsC0YPiIJY/"), (433813, IG + "Dd6XW7lErrs/")]),
            ("Dr. Neetu Pal", "Greater Noida", "p-neetu", ["neetu"], []),
        ],
        topics=["Why gums bleed", "Fear of root canal", "Implant or bridge?", "Children's teeth", "Braces and aligners", "Bad breath", "Teeth whitening", "Tooth sensitivity"],
        how=[("Animation people remember", "A friendly tooth character and a toothbrush journey that kids and adults watch and share."),
             ("From fear to the chair", "We ease the fear of root canals and implants so patients book."),
             ("Known in your area", "Google profile, reviews and reels work together to make you the local name.")],
    ),
}


def spec_total(k):
    return sum(p for d in SPECS[k]["doctors"] for p, _ in d[4])


def grand_total():
    return sum(spec_total(k) for k in SPECS)


def reel_count():
    return sum(len(d[4]) for k in SPECS for d in SPECS[k]["doctors"])


IG_ICON = ('<svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2">'
           '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>')
SOUND = ('<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z" fill="currentColor"/>'
         '<path d="M16 8.5a5 5 0 0 1 0 7M18.5 6a8.5 8.5 0 0 1 0 12" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')


def rcard(name, city, photo=None, video=None, plays=None, url=None, spec="", lazy=True):
    """A phone-frame reel card. Video if we have it, otherwise the doctor's photo with the play count."""
    badge = f'<span class="plays"><b>{plays_fmt(plays)}</b> plays</span>' if plays else ""
    link = f'<a class="ig-link" href="{url}" target="_blank" rel="noopener">{IG_ICON}Watch on Instagram</a>' if url else ""
    if video:
        inner = (f'<video src="media/{video}.mp4" poster="media/{video}.jpg" muted loop playsinline preload="none" data-auto aria-label="Reel by {name}"></video>'
                 f'<button class="sound" type="button" data-sound aria-pressed="false">{SOUND}<span>Sound on</span></button>{badge}')
    else:
        img = f'<img src="media/{photo}.jpg" alt="{name}" loading="lazy" width="600" height="750">' if photo else f'<span class="mono">{name.replace("Dr. ", "")[:1]}</span>'
        inner = (f'<a class="still" href="{url}" target="_blank" rel="noopener" aria-label="{name} : watch reel on Instagram">{img}'
                 f'<span class="igplay"><svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M8 5l12 7-12 7z" fill="currentColor"/></svg></span>{badge}</a>')
    return (f'<figure class="reel rc" data-spec="{spec}"><div class="reel-frame">{inner}</div>'
            f'<figcaption><b>{name}</b>{f"<small class=deg>{DEG[name]}</small>" if name in DEG else ""}<span>{city}</span>{link}</figcaption></figure>')


def profile_card(name, city, photo, plays, spec=""):
    url = ig_profile(name)
    if not url:
        return ""
    img = f'<img src="media/{photo}.jpg" alt="{name}" loading="lazy" width="600" height="750">' if photo else f'<span class="mono">{name.replace("Dr. ", "")[:1]}</span>'
    deg = f'<small class="deg">{DEG[name]}</small>' if name in DEG else ""
    pl = f'<p class="pf-plays"><b>{plays_fmt(plays)}</b> plays on best reel</p>' if plays else ""
    return (f'<a class="pf" data-spec="{spec}" href="{url}" target="_blank" rel="noopener" aria-label="{name}: see Instagram profile">'
            f'<div class="pf-ph"><span class="ex-badge">Karunya Exclusive</span>{img}</div>'
            f'<div class="pf-body"><b class="pf-n">{name}</b>{deg}<span class="pf-c">{city}</span>{pl}'
            f'<span class="pf-go">{IG_ICON}Click to see profile</span></div></a>')


def profile_cards(keys=None):
    out = []
    for k in (keys or list(SPECS)):
        for name, city, photo, vids, reels in SPECS[k]["doctors"]:
            best = max((pp for pp, _ in reels), default=None)
            out.append((best or 0, profile_card(name, city, photo, best, k)))
    out.sort(key=lambda x: -x[0])
    return "".join(c for _, c in out if c)


def spec_cards(k, videos=True):
    """Best Instagram reels (with real play counts) first, then our edited videos for the same doctors."""
    out = []
    if videos:
        for name, city, photo, vids, reels in SPECS[k]["doctors"]:
            for v in vids:
                out.append(rcard(name, city, photo, v, None, None, k))
    return out


def top_cards(n=8):
    allr = []
    for k in SPECS:
        for name, city, photo, vids, reels in SPECS[k]["doctors"]:
            for i, (p, u) in enumerate(reels):
                allr.append((p, name, city, photo, None, u, k))
    allr.sort(key=lambda r: -r[0])
    seen = {}
    picked = []
    for r in allr:
        if seen.get(r[1], 0) >= 1:
            continue
        seen[r[1]] = 1
        picked.append(rcard(r[1], r[2], r[3], r[4], r[0], r[5], r[6]))
        if len(picked) >= n:
            break
    return picked


# ---------------------------------------------------------------- specialty motion art
def spec_art(k, cls="spec-art"):
    head = f'<svg class="{cls} art-{k}" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
    ring = f'<circle cx="200" cy="200" r="176" fill="{SKY}" opacity=".18"/><circle class="orbit" cx="200" cy="200" r="150" fill="none" stroke="{SKY}" stroke-width="2" stroke-dasharray="4 10" opacity=".7"/>'
    b = ""
    if k == "gynae":
        b = (f'<circle cx="200" cy="200" r="118" fill="{WHITE}"/>'
             f'<g class="heart"><path d="M200 262 C130 210 136 150 176 146 C192 145 200 158 200 166 C200 158 208 145 224 146 C264 150 270 210 200 262 Z" fill="{LIME}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/></g>'
             f'<path class="ecg" d="M40 214 H140 l12 -28 l16 56 l14 -86 l16 86 l12 -28 H360" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
             f'<g class="bubbles"><circle cx="300" cy="110" r="14" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/><circle cx="96" cy="300" r="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/></g>')
    elif k == "ivf":
        b = (f'<circle cx="200" cy="200" r="122" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
             f'<circle cx="200" cy="200" r="104" fill="{SKY}" opacity=".35"/>'
             f'<g class="cells">'
             f'<circle class="c1" cx="200" cy="200" r="60" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/>'
             f'<g class="c2"><circle cx="172" cy="200" r="40" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/><circle cx="228" cy="200" r="40" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/></g>'
             f'<g class="c4"><circle cx="176" cy="176" r="30" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/><circle cx="224" cy="176" r="30" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/><circle cx="176" cy="224" r="30" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/><circle cx="224" cy="224" r="30" fill="{LIME}" stroke="{NAVY}" stroke-width="5"/></g>'
             f'</g>')
    elif k == "ortho":
        verts = ""
        for i in range(7):
            y = 92 + i * 34
            w = 64 + (i * 6)
            verts += (f'<g class="v" style="--i:{i}"><rect x="{200 - w / 2}" y="{y}" width="{w}" height="24" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
                      f'<rect x="{200 - w / 2 - 14}" y="{y + 8}" width="14" height="8" rx="4" fill="{NAVY}"/><rect x="{200 + w / 2}" y="{y + 8}" width="14" height="8" rx="4" fill="{NAVY}"/></g>')
            if i < 6:
                verts += f'<rect class="disc" style="--i:{i}" x="{200 - w / 2 + 8}" y="{y + 25}" width="{w - 16}" height="8" rx="4" fill="{LIME}"/>'
        b = f'<g class="spine">{verts}</g>'
    elif k == "dental":
        b = (f'<g class="tooth"><path d="M140 120 C140 90 170 84 200 100 C230 84 260 90 260 120 C262 170 246 196 240 250 C236 290 222 304 214 280 C208 258 206 236 200 236 C194 236 192 258 186 280 C178 304 164 290 160 250 C154 196 138 170 140 120 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/>'
             f'<path d="M168 128 q12 -10 22 -2" stroke="{SKY}" stroke-width="6" fill="none" stroke-linecap="round"/>'
             f'<circle cx="180" cy="160" r="6" fill="{NAVY}"/><circle cx="220" cy="160" r="6" fill="{NAVY}"/><path d="M184 186 q16 14 32 0" stroke="{NAVY}" stroke-width="5" fill="none" stroke-linecap="round"/></g>'
             f'<g class="spark s1"><path d="M290 110 l6 18 l18 6 l-18 6 l-6 18 l-6 -18 l-18 -6 l18 -6z" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/></g>'
             f'<g class="spark s2"><path d="M104 150 l4 12 l12 4 l-12 4 l-4 12 l-4 -12 l-12 -4 l12 -4z" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/></g>'
             f'<g class="spark s3"><path d="M300 270 l4 12 l12 4 l-12 4 l-4 12 l-4 -12 l-12 -4 l12 -4z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/></g>')
    return head + ring + b + '</svg>'
