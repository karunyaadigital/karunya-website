"""Blog covers in the Karunya reel-thumbnail style (1200x630, used as card image, hero and og:image).

Optional front-matter keys per post (all fall back to sensible defaults):
  cover_script: Social          <- Waylimo script word
  cover_bold:   Agency kaise chunein   <- heavy uppercase line
  cover_sub:    Doctors ke liye [[5 sawaal]] pehle poochiye   <- [[...]] gets the lime highlight
  cover_tag:    2026            <- small red/lime badge after the bold line
  cover_theme:  blue | paper | lime   (default rotates)
  cover_prop:   reels | gmb | nmc | ads | checklist | chart  (default from category)
  cover_doc:    m | f
Run:  python3 build/covers.py [--force]
"""
import os, sys, base64, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_posts

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
OUTDIR = os.path.join(SITE, "media", "blog")
os.makedirs(OUTDIR, exist_ok=True)

B64 = lambda p: base64.b64encode(open(os.path.join(SITE, p), "rb").read()).decode()
FONT, FIG7, FIG5 = B64("fonts/Waylimo.woff2"), B64("fonts/figtree-latin-700-normal.woff2"), B64("fonts/figtree-latin-500-normal.woff2")
LOGO_W, LOGO_N = B64("assets/logo-white.png"), B64("assets/logo-navy.png")

BLUE, NAVY, LIME, SKY, PAPER, INK, SKIN, HAIR, RED = "#0251B0", "#012A5E", "#D1FF42", "#B0E0E6", "#F3F6FA", "#0B1F45", "#F2C29B", "#1D2340", "#E5484D"

CAT_PROP = {"Google Business Profile": "gmb", "Instagram": "reels", "Reels": "reels", "Meta Ads": "ads",
            "NMC": "nmc", "Agency": "checklist", "Branding": "reels", "Strategy": "chart", "SEO": "gmb", "Website": "chart"}
THEMES = ["blue", "paper", "lime", "navy", "sky"]
PROPS = ["reels", "gmb", "nmc", "ads", "checklist", "chart", "scales", "journey"]
LAYOUTS = ["right", "left"]


# ---------- character ----------
def limb(x1, y1, x2, y2, w=26, col="#fff"):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="{w+7}" stroke-linecap="round"/>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>')


def doctor(kind="m", pose="phone"):
    """Flat doctor: glasses, white coat, lime lanyard. viewBox 0 0 340 500. Raised hand ends near (270,96) for 'phone'/'up', (300,236) for 'point'."""
    s = []
    if kind == "f":  # long hair behind
        s.append(f'<path d="M116 104 Q114 40 160 36 Q208 40 206 104 L214 196 Q160 214 108 196 Z" fill="{HAIR}"/>')
    # legs + shoes
    s.append(f'<rect x="124" y="340" width="32" height="118" rx="6" fill="{NAVY}"/><rect x="166" y="340" width="32" height="118" rx="6" fill="{NAVY}"/>')
    s.append(f'<ellipse cx="136" cy="462" rx="24" ry="10" fill="{INK}"/><ellipse cx="188" cy="462" rx="24" ry="10" fill="{INK}"/>')
    # back arm (viewer left, hangs down)
    s.append(limb(108, 186, 90, 318))
    s.append(f'<circle cx="89" cy="330" r="13" fill="{SKIN}" stroke="{NAVY}" stroke-width="3"/>')
    # coat
    s.append(f'<path d="M104 176 Q160 160 216 176 L232 362 Q160 376 88 362 Z" fill="#fff" stroke="{NAVY}" stroke-width="3.5" stroke-linejoin="round"/>')
    s.append(f'<path d="M140 172 L160 236 L180 172 Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>')
    s.append(f'<path d="M160 236 L160 360" stroke="{NAVY}" stroke-width="3"/>')
    s.append(f'<rect x="186" y="270" width="28" height="22" rx="4" fill="none" stroke="{NAVY}" stroke-width="3"/>')
    # lanyard + badge
    s.append(f'<path d="M142 176 L158 262 M178 176 L162 262" stroke="{LIME}" stroke-width="6" stroke-linecap="round"/>')
    s.append(f'<rect x="146" y="258" width="28" height="34" rx="4" fill="#fff" stroke="{NAVY}" stroke-width="3"/><rect x="152" y="266" width="16" height="6" rx="2" fill="{LIME}"/>')
    # stethoscope
    s.append(f'<path d="M128 180 Q118 236 134 252 Q150 262 152 240" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/><circle cx="152" cy="236" r="6" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>')
    # neck + head
    s.append(f'<rect x="148" y="136" width="24" height="34" fill="{SKIN}" stroke="{NAVY}" stroke-width="3"/>')
    s.append(f'<circle cx="160" cy="104" r="40" fill="{SKIN}" stroke="{NAVY}" stroke-width="3.5"/>')
    if kind == "f":
        s.append(f'<path d="M120 100 Q122 58 160 56 Q200 58 200 100 Q186 76 160 74 Q134 76 120 100 Z" fill="{HAIR}"/>')
        s.append(f'<circle cx="160" cy="88" r="3.5" fill="{RED}"/>')
    else:
        s.append(f'<path d="M118 100 Q114 56 160 54 Q206 56 202 96 L196 84 Q176 70 142 76 Q128 82 124 100 Z" fill="{HAIR}"/>')
    # glasses, smile
    s.append(f'<rect x="130" y="98" width="26" height="18" rx="6" fill="rgba(255,255,255,.55)" stroke="{NAVY}" stroke-width="3.5"/>'
             f'<rect x="164" y="98" width="26" height="18" rx="6" fill="rgba(255,255,255,.55)" stroke="{NAVY}" stroke-width="3.5"/>'
             f'<path d="M156 106 L164 106" stroke="{NAVY}" stroke-width="3"/><circle cx="143" cy="107" r="2.6" fill="{NAVY}"/><circle cx="177" cy="107" r="2.6" fill="{NAVY}"/>')
    s.append(f'<path d="M148 126 Q160 136 172 126" fill="none" stroke="{NAVY}" stroke-width="3.5" stroke-linecap="round"/>')
    # front arm
    if pose == "point":
        s.append(limb(214, 188, 294, 232))
        s.append(f'<circle cx="302" cy="236" r="13" fill="{SKIN}" stroke="{NAVY}" stroke-width="3"/>')
    else:
        s.append(limb(214, 188, 262, 116))
        s.append(f'<circle cx="268" cy="104" r="13" fill="{SKIN}" stroke="{NAVY}" stroke-width="3"/>')
        if pose == "phone":
            s.append(f'<g transform="rotate(12 276 66)"><rect x="256" y="22" width="42" height="80" rx="9" fill="{SKY}" stroke="{NAVY}" stroke-width="3.5"/>'
                     f'<rect x="262" y="30" width="30" height="58" rx="4" fill="#fff"/><path d="M272 50 L286 59 L272 68 Z" fill="{BLUE}"/></g>')
    return f'<svg viewBox="0 0 340 500" xmlns="http://www.w3.org/2000/svg">{"".join(s)}</svg>'


# ---------- props / floating icons ----------
def bubble(x, y, sym, r=30, bg=LIME, fg=NAVY):
    glyph = {
        "heart": f'<path d="M0 10 C-18 -4 -12 -18 0 -9 C12 -18 18 -4 0 10Z" fill="{fg}"/>',
        "play": f'<path d="M-6 -10 L10 0 L-6 10Z" fill="{fg}"/>',
        "bell": f'<path d="M-10 6 Q-10 -12 0 -12 Q10 -12 10 6 Z M-4 9 Q0 14 4 9" fill="{fg}"/>',
        "chat": f'<rect x="-12" y="-10" width="24" height="16" rx="4" fill="{fg}"/><path d="M-6 6 L-8 13 L1 6Z" fill="{fg}"/>',
        "star": f'<path d="M0 -12 L3.5 -4 L12 -3.5 L5.5 2.5 L7.5 11 L0 6.5 L-7.5 11 L-5.5 2.5 L-12 -3.5 L-3.5 -4Z" fill="{fg}"/>',
        "tick": f'<path d="M-9 0 L-3 7 L10 -7" fill="none" stroke="{fg}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>',
        "cross": f'<path d="M-7 -7 L7 7 M7 -7 L-7 7" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/>',
        "up": f'<path d="M-10 8 L-2 0 L3 5 L11 -5 M4 -6 L11 -5 L10 2" fill="none" stroke="{fg}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
    }[sym]
    return f'<g transform="translate({x} {y})"><circle r="{r}" fill="{bg}" stroke="{NAVY}" stroke-width="3"/>{glyph}</g>'


def prop_layer(prop, theme):
    """Returns (svg behind character, svg in front, pose). Canvas 520x560 (right panel)."""
    ring = LIME
    back, front, pose = "", "", "phone"
    if prop == "reels":
        back = (f'<circle cx="260" cy="270" r="190" fill="none" stroke="{ring}" stroke-width="16" opacity=".35" filter="url(#glow)"/>'
                f'<circle cx="260" cy="270" r="190" fill="none" stroke="{ring}" stroke-width="7"/>')
        front = bubble(70, 170, "heart") + bubble(462, 210, "play") + bubble(80, 400, "bell", 26) + bubble(452, 410, "chat", 26)
        front += (f'<g transform="translate(118 452) rotate(-8)"><rect width="150" height="46" rx="6" fill="{NAVY}" stroke="{LIME}" stroke-width="3"/>'
                  f'<text x="75" y="31" text-anchor="middle" font-family="F7" font-size="22" fill="{LIME}" letter-spacing="2">ACTION</text></g>')
    elif prop == "gmb":
        pose = "point"
        back = f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.18)"}"/>'
        front = (f'<g transform="translate(330 70)"><rect width="176" height="150" rx="20" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                 f'<path d="M88 26 C64 26 52 44 52 60 C52 86 88 118 88 118 C88 118 124 86 124 60 C124 44 112 26 88 26Z" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>'
                 f'<circle cx="88" cy="60" r="13" fill="#fff"/>'
                 + "".join(f'<path transform="translate({34+i*27} 136) scale(.8)" d="M0 -12 L3.5 -4 L12 -3.5 L5.5 2.5 L7.5 11 L0 6.5 L-7.5 11 L-5.5 2.5 L-12 -3.5 L-3.5 -4Z" fill="#F5B301" stroke="{NAVY}" stroke-width="2"/>' for i in range(5))
                 + '</g>')
        front += (f'<g transform="translate(20 470)"><rect width="300" height="54" rx="27" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                  f'<circle cx="32" cy="27" r="10" fill="none" stroke="{NAVY}" stroke-width="3.5"/><path d="M39 34 L47 42" stroke="{NAVY}" stroke-width="3.5" stroke-linecap="round"/>'
                  f'<text x="60" y="36" font-family="F5" font-size="22" fill="{NAVY}">doctor near me</text></g>')
        front += bubble(60, 150, "star", 28) + bubble(470, 300, "chat", 26)
    elif prop == "nmc":
        pose = "point"
        front = (f'<g transform="translate(26 150)"><rect x="34" y="230" width="16" height="190" fill="{NAVY}"/><rect width="84" height="240" rx="18" fill="{INK}" stroke="{NAVY}" stroke-width="3"/>'
                 f'<circle cx="42" cy="44" r="27" fill="{RED}"/><path d="M32 34 L52 54 M52 34 L32 54" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
                 f'<circle cx="42" cy="120" r="27" fill="#4a4a3a"/><circle cx="42" cy="196" r="27" fill="#2f6b3c"/></g>')
        front += (f'<g transform="translate(-20 470) rotate(-6)"><rect width="580" height="40" fill="#F5B301" stroke="{NAVY}" stroke-width="3"/>'
                  + "".join(f'<path d="M{i*44} 0 L{i*44+22} 0 L{i*44+2} 40 L{i*44-20} 40Z" fill="{INK}"/>' for i in range(14))
                  + f'<rect x="150" y="6" width="290" height="28" fill="#F5B301"/><text x="295" y="28" text-anchor="middle" font-family="F7" font-size="19" fill="{INK}" letter-spacing="2">NMC · DO NOT CROSS</text></g>')
        front += (f'<g transform="translate(372 160)"><rect width="120" height="84" rx="16" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                  f'<path d="M20 84 L14 104 L40 84Z" fill="#fff" stroke="{NAVY}" stroke-width="3.5" stroke-linejoin="round"/>'
                  f'<rect x="24" y="18" width="28" height="48" rx="5" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
                  f'<circle cx="84" cy="42" r="18" fill="{RED}"/><path d="M76 34 L92 50 M92 34 L76 50" stroke="#fff" stroke-width="4.5" stroke-linecap="round"/></g>')
    elif prop == "ads":
        pose = "up"
        back = f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.18)"}"/>'
        front = (f'<g transform="translate(330 300)"><rect width="170" height="150" rx="18" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                 + "".join(f'<rect x="{24+i*36}" y="{120-h}" width="24" height="{h}" rx="4" fill="{BLUE if i<3 else LIME}" stroke="{NAVY}" stroke-width="2.5"/>' for i, h in enumerate([30, 52, 72, 98]))
                 + f'<path d="M30 70 L66 50 L102 36 L140 12" fill="none" stroke="{RED}" stroke-width="4" stroke-linecap="round"/></g>')
        front += bubble(470, 230, "up", 30) + bubble(70, 180, "heart") + bubble(70, 400, "chat", 26)
    elif prop == "checklist":
        pose = "point"
        back = f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.18)"}"/>'
        rows = "".join(
            f'<rect x="22" y="{58+i*46}" width="26" height="26" rx="6" fill="{LIME if i<3 else "#fff"}" stroke="{NAVY}" stroke-width="3"/>'
            + (f'<path d="M27 {71+i*46} L33 {78+i*46} L44 {64+i*46}" fill="none" stroke="{NAVY}" stroke-width="3.5" stroke-linecap="round"/>' if i < 3 else "")
            + f'<rect x="60" y="{64+i*46}" width="{[96,80,104,70][i]}" height="12" rx="6" fill="{SKY}"/>' for i in range(4))
        front = (f'<g transform="translate(320 80) rotate(5)"><rect width="190" height="250" rx="16" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                 f'<rect x="60" y="-14" width="70" height="30" rx="8" fill="{NAVY}"/>{rows}</g>')
        front += bubble(70, 160, "tick", 30) + bubble(462, 420, "star", 28)
    elif prop == "scales":
        pose = "point"
        back = f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.18)"}"/>'
        front = (f'<g transform="translate(330 64)">'
                 f'<rect x="84" y="20" width="10" height="150" fill="{NAVY}"/><rect x="50" y="166" width="78" height="14" rx="6" fill="{NAVY}"/>'
                 f'<g transform="rotate(-9 89 30)"><rect x="-6" y="26" width="190" height="9" rx="4" fill="{NAVY}"/>'
                 f'<path d="M10 34 L-14 96 M10 34 L34 96 M170 34 L146 96 M170 34 L194 96" stroke="{NAVY}" stroke-width="2.5"/>'
                 f'<path d="M-22 96 Q10 122 42 96 Z" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/>'
                 f'<path d="M138 96 Q170 122 202 96 Z" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
                 f'<circle cx="10" cy="76" r="17" fill="#2f9e5b" stroke="{NAVY}" stroke-width="3"/><path d="M2 76 L8 83 L19 70" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
                 f'<circle cx="170" cy="76" r="17" fill="{RED}" stroke="{NAVY}" stroke-width="3"/><path d="M163 69 L177 83 M177 69 L163 83" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>'
                 f'<circle cx="89" cy="22" r="10" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/></g>')
        front += (f'<g transform="translate(14 430) rotate(-7)"><rect width="190" height="110" rx="10" fill="{NAVY}"/><rect x="10" y="8" width="172" height="94" rx="6" fill="#fff"/>'
                  f'<rect x="10" y="8" width="18" height="94" fill="{LIME}"/><text x="105" y="50" text-anchor="middle" font-family="F7" font-size="26" fill="{NAVY}">NMC</text>'
                  f'<text x="105" y="80" text-anchor="middle" font-family="F5" font-size="17" fill="{NAVY}">Guidelines 2026</text></g>')
        front += bubble(56, 150, "tick", 28) + bubble(466, 330, "cross", 26, bg=RED, fg="#fff")
    elif prop == "journey":
        pose = "point"
        back = (f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.14)"}"/>'
                f'<path d="M70 150 C-10 300 40 470 200 520 S470 470 470 230" fill="none" stroke="{LIME}" stroke-width="6" stroke-dasharray="4 14" stroke-linecap="round"/>')
        front = (f'<g transform="translate(30 90) rotate(-8)"><rect width="74" height="120" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="3.5"/>'
                 f'<rect x="8" y="14" width="58" height="88" rx="6" fill="#fff"/><path d="M28 42 L50 58 L28 74 Z" fill="{BLUE}"/>'
                 f'<path d="M16 92 C14 84 22 82 24 88 C26 82 34 84 32 92 L24 99Z" fill="{RED}"/></g>')
        front += bubble(40, 360, "chat", 28) 
        front += (f'<g transform="translate(150 488)"><rect width="200" height="48" rx="24" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                  f'<circle cx="28" cy="24" r="9" fill="none" stroke="{NAVY}" stroke-width="3.5"/><path d="M34 30 L41 37" stroke="{NAVY}" stroke-width="3.5" stroke-linecap="round"/>'
                  f'<text x="52" y="32" font-family="F5" font-size="20" fill="{NAVY}">doctor near me</text></g>')
        front += (f'<g transform="translate(400 150)"><path d="M10 120 L10 50 L60 18 L110 50 L110 120 Z" fill="#fff" stroke="{NAVY}" stroke-width="3.5" stroke-linejoin="round"/>'
                  f'<rect x="46" y="80" width="28" height="40" fill="{BLUE}"/><rect x="50" y="40" width="20" height="20" fill="{RED}"/>'
                  f'<path d="M60 44 L60 56 M54 50 L66 50" stroke="#fff" stroke-width="4"/>'
                  f'<path d="M60 -40 C44 -40 36 -28 36 -18 C36 0 60 22 60 22 C60 22 84 0 84 -18 C84 -28 76 -40 60 -40Z" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/><circle cx="60" cy="-18" r="8" fill="{NAVY}"/></g>')
    else:  # chart
        pose = "point"
        back = f'<circle cx="260" cy="290" r="200" fill="{SKY if theme in ("paper","lime") else "#fff" if theme=="sky" else "rgba(176,224,230,.18)"}"/>'
        front = (f'<g transform="translate(326 110)"><rect width="180" height="150" rx="18" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>'
                 f'<path d="M24 120 L64 90 L100 102 L150 40" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
                 f'<circle cx="150" cy="40" r="9" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/></g>')
        front += bubble(70, 170, "up", 30) + bubble(80, 410, "heart", 26)
    return back, front, pose


# ---------- text ----------
def default_text(p):
    t = p["title"]
    head = re.split(r"[:\-–|]", t)[0].strip()
    words = head.split()
    script = words[0] if words else "Doctors"
    bold = " ".join(words[1:6]) or "ke liye"
    sub = p.get("description", "")[:70].rsplit(" ", 1)[0]
    return script, bold, sub


def sub_html(s):
    s = html.escape(s)
    return re.sub(r"\[\[(.+?)\]\]", r'<mark>\1</mark>', s)


def cover_html(p, idx):
    theme = p.get("cover_theme") or THEMES[idx % 3]
    prop = p.get("cover_prop") or CAT_PROP.get(p.get("category", ""), "chart")
    kind = p.get("cover_doc") or ("f" if idx % 2 else "m")
    ds, dbold, dsub = default_text(p)
    script = p.get("cover_script") or ds
    bold = (p.get("cover_bold") or dbold).upper()
    sub = p.get("cover_sub") or dsub
    tag = p.get("cover_tag", "")
    ep = f"BLOG {idx+1:02d}"
    back, front, pose = prop_layer(prop, theme)
    fig = doctor(kind, pose)

    if theme == "blue":
        bg = f"background:{BLUE}"
        dots = "radial-gradient(rgba(255,255,255,.16) 1.4px,transparent 1.5px)"
        sc_col, bold_col, sub_col, logo = LIME, "#fff", "#EAF2FF", LOGO_W
        mark_bg, mark_col, pill_bg, pill_col = LIME, NAVY, LIME, NAVY
        under = f'<div class="disc" style="background:{NAVY};opacity:.55"></div>'
    elif theme == "paper":
        bg = f"background:{PAPER}"
        dots = "radial-gradient(rgba(1,42,94,.12) 1.4px,transparent 1.5px)"
        sc_col, bold_col, sub_col, logo = BLUE, NAVY, NAVY, LOGO_N
        mark_bg, mark_col, pill_bg, pill_col = LIME, NAVY, LIME, NAVY
        under = ""
    elif theme == "navy":
        bg = f"background:radial-gradient(90% 120% at 70% 40%,#0A3A7A 0%,{NAVY} 70%)"
        dots = "radial-gradient(rgba(209,255,66,.14) 1.4px,transparent 1.5px)"
        sc_col, bold_col, sub_col, logo = LIME, "#fff", SKY, LOGO_W
        mark_bg, mark_col, pill_bg, pill_col = LIME, NAVY, LIME, NAVY
        under = f'<div class="disc" style="background:{BLUE}"></div><div class="disc ring2"></div>'
    elif theme == "sky":
        bg = f"background:{SKY}"
        dots = "radial-gradient(rgba(1,42,94,.13) 1.4px,transparent 1.5px)"
        sc_col, bold_col, sub_col, logo = BLUE, NAVY, NAVY, LOGO_N
        mark_bg, mark_col, pill_bg, pill_col = NAVY, LIME, NAVY, LIME
        under = f'<div class="disc" style="background:#fff"></div>'
    else:  # lime sunburst
        bg = f"background:{LIME}"
        dots = "radial-gradient(rgba(1,42,94,.10) 1.4px,transparent 1.5px)"
        sc_col, bold_col, sub_col, logo = BLUE, NAVY, NAVY, LOGO_N
        mark_bg, mark_col, pill_bg, pill_col = NAVY, LIME, NAVY, LIME
        under = (f'<div class="burst"></div><div class="disc" style="background:{BLUE}"></div>')

    n = len(bold)
    bsize = 76 if n <= 14 else 64 if n <= 22 else 54 if n <= 32 else 46
    ssize = 150 if len(script) <= 7 else 124 if len(script) <= 10 else 100
    tag_html = f'<span class="tag">{html.escape(tag)}</span>' if tag else ""
    left = (p.get("cover_layout") or LAYOUTS[idx % 2]) == "left"
    if left:
        lay = (".panel{left:10px!important}.disc{left:40px!important}.burst{left:-480px!important}"
               ".copy,.pill,.url{left:590px!important}.copy{width:560px!important}")
    else:
        lay = ""

    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:W;src:url(data:font/woff2;base64,{FONT})}}
@font-face{{font-family:F7;font-weight:700;src:url(data:font/woff2;base64,{FIG7})}}
@font-face{{font-family:F5;font-weight:500;src:url(data:font/woff2;base64,{FIG5})}}
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;{bg};position:relative;font-family:F7,sans-serif}}
.dots{{position:absolute;inset:0;background-image:{dots};background-size:24px 24px}}
.burst{{position:absolute;left:640px;top:-260px;width:1150px;height:1150px;border-radius:50%;
  background:repeating-conic-gradient(from 0deg,rgba(255,255,255,.55) 0deg 7deg,transparent 7deg 20deg);
  -webkit-mask:radial-gradient(circle,#000 30%,transparent 70%);mask:radial-gradient(circle,#000 30%,transparent 70%);transform:translateX(-25%)}}
.disc{{position:absolute;left:705px;top:120px;width:460px;height:460px;border-radius:50%}}
.pill{{position:absolute;left:64px;top:52px;background:{pill_bg};color:{pill_col};font-size:22px;letter-spacing:1px;padding:9px 20px;border-radius:999px}}
.logo{{position:absolute;right:56px;top:44px;height:54px}}
.copy{{position:absolute;left:64px;top:118px;width:620px}}
.sc{{font-family:W,serif;color:{sc_col};font-size:{ssize}px;line-height:1;margin-bottom:6px;white-space:nowrap}}
.bd{{color:{bold_col};font-size:{bsize}px;line-height:1.02;letter-spacing:1px}}
.tag{{display:inline-block;vertical-align:middle;background:{RED};color:#fff;font-size:.42em;padding:6px 16px;border-radius:999px;margin-left:10px;letter-spacing:0}}
.sb{{margin-top:26px;color:{sub_col};font-family:F5,sans-serif;font-size:30px;line-height:1.35;max-width:560px}}
.sb mark{{background:{mark_bg};color:{mark_col};font-family:F7;padding:0 8px;border-radius:6px}}
.panel{{position:absolute;left:675px;top:70px;width:520px;height:560px}}
.panel svg.l{{position:absolute;inset:0;width:520px;height:560px;overflow:visible}}
.fig{{position:absolute;left:100px;top:62px;width:340px;height:500px}}
.fig svg{{width:100%;height:100%}}
.ring2{{background:none;border:4px dashed rgba(209,255,66,.6);transform:scale(1.12)}}
{lay}
.url{{position:absolute;left:64px;bottom:40px;font-family:F5;font-size:20px;color:{sub_col};opacity:.75;letter-spacing:.5px}}
</style></head><body><div class="dots"></div>{under}
<span class="pill">{ep}</span><img class="logo" src="data:image/png;base64,{logo}">
<div class="copy"><div class="sc">{html.escape(script)}</div><div class="bd">{html.escape(bold)}{tag_html}</div><div class="sb">{sub_html(sub)}</div></div>
<div class="panel"><svg class="l" viewBox="0 0 520 560"><defs><filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter></defs>{back}</svg>
<div class="fig">{fig}</div>
<svg class="l" viewBox="0 0 520 560" style="font-family:F7">{front}</svg></div>
<span class="url">karunyadigital.online/blog</span>
</body></html>"""


def used_combos(posts):
    return {(p.get("cover_theme"), p.get("cover_prop"), p.get("cover_layout")) for p in posts}


def suggest(category=""):
    """Pick a theme/prop/layout/doc combo not used by any existing post, preferring props that fit the category
    and avoiding the theme and prop of the two newest covers. Prints front-matter lines."""
    import random
    posts = build_posts.load_posts()
    used = used_combos(posts)
    recent = posts[:2]
    avoid_t = {p.get("cover_theme") for p in recent}
    avoid_p = {p.get("cover_prop") for p in recent}
    pref = CAT_PROP.get(category)
    cands = [(t, pr, l) for t in THEMES for pr in PROPS for l in LAYOUTS
             if (t, pr, l) not in used and t not in avoid_t and pr not in avoid_p]
    random.shuffle(cands)
    cands.sort(key=lambda c: 0 if c[1] == pref else 1)
    t, pr, l = cands[0]
    last_doc = recent[0].get("cover_doc", "m") if recent else "m"
    print(f"cover_theme: {t}\ncover_prop: {pr}\ncover_layout: {l}\ncover_doc: {'f' if last_doc == 'm' else 'm'}")


def main():
    if "--suggest" in sys.argv:
        i = sys.argv.index("--suggest")
        return suggest(sys.argv[i + 1] if len(sys.argv) > i + 1 else "")
    from playwright.sync_api import sync_playwright
    posts = build_posts.load_posts()
    order = sorted(posts, key=lambda p: (p.get("date", ""), p["slug"]))  # chronological -> stable BLOG nn
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        for idx, p in enumerate(order):
            out = os.path.join(OUTDIR, p["slug"] + ".jpg")
            if only and p["slug"] not in only:
                continue
            if os.path.exists(out) and "--force" not in sys.argv and not only:
                continue
            pg.set_content(cover_html(p, idx))
            pg.wait_for_timeout(350)
            pg.screenshot(path=out, type="jpeg", quality=84)
            print("cover", out)
        b.close()


if __name__ == "__main__":
    main()
