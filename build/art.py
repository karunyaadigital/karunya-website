"""SVG art for the Karunya Digital site. Original illustrations drawn in code, brand palette only."""
import math

BLUE = "#0251B0"; NAVY = "#012A5E"; LIME = "#D1FF42"; SKY = "#B0E0E6"
GREY = "#C7D1DD"; PAPER = "#F3F6FA"; WHITE = "#FFFFFF"
MID = "#2F7FD6"      # lighter working blue for variety
DEEP = "#0A3F85"     # far silhouettes
SKIN = ["#E3A878", "#C98A5B", "#F0BE93", "#A86B3F"]


def _lit(i, j):
    return ((i * 7 + j * 13 + i * j) % 5) in (0, 2)


def building(x, w, top, base, fill, shade, awning=None, tank=False, dish=False, floors_gap=58, shop_h=92, seed=0, balcony=True):
    out = [f'<g>']
    h = base - top
    out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" fill="{fill}"/>')
    out.append(f'<rect x="{x + w - 16}" y="{top}" width="16" height="{h}" fill="{shade}"/>')
    out.append(f'<rect x="{x - 4}" y="{top - 8}" width="{w + 8}" height="10" fill="{shade}"/>')
    if tank:
        tx = x + w * 0.2
        out.append(f'<rect x="{tx}" y="{top - 44}" width="34" height="36" rx="6" fill="{NAVY}"/>')
        out.append(f'<rect x="{tx + 40}" y="{top - 34}" width="26" height="26" rx="5" fill="{NAVY}"/>')
        out.append(f'<rect x="{tx + 6}" y="{top - 10}" width="4" height="4" fill="{NAVY}"/>')
    if dish:
        dx = x + w * 0.68
        out.append(f'<path d="M{dx} {top - 8} v-26 M{dx - 14} {top - 38} q14 18 28 0 z" stroke="{NAVY}" stroke-width="3" fill="{NAVY}"/>')
    cols = max(2, int((w - 40) // 52))
    gap = (w - 16 - cols * 24) / (cols + 1)
    row = 0
    y = top + 26
    while y + 40 < base - shop_h + 6:
        for c in range(cols):
            wx = x + gap + c * (24 + gap)
            lit = _lit(row + seed, c)
            col = LIME if lit else NAVY
            op = 0.95 if lit else 0.85
            out.append(f'<path d="M{wx} {y + 38} v-26 a12 12 0 0 1 24 0 v26 z" fill="{col}" opacity="{op}"/>')
            if not lit:
                out.append(f'<rect x="{wx + 4}" y="{y + 18}" width="16" height="3" fill="{SKY}" opacity=".35"/>')
        if balcony:
            out.append(f'<rect x="{x + 6}" y="{y + 42}" width="{w - 28}" height="5" fill="{shade}" opacity=".8"/>')
        y += floors_gap
        row += 1
    # ground floor shop
    sy = base - shop_h
    out.append(f'<rect x="{x}" y="{sy}" width="{w - 16}" height="{shop_h}" fill="{NAVY}" opacity=".92"/>')
    sw = w - 16
    n = max(1, int(sw // 70))
    for k in range(n):
        px = x + 8 + k * (sw - 16) / n
        pw = (sw - 16) / n - 8
        out.append(f'<rect x="{px}" y="{sy + 26}" width="{pw}" height="{shop_h - 26}" fill="{LIME if (k + seed) % 2 == 0 else SKY}" opacity=".22"/>')
        out.append(f'<rect x="{px}" y="{sy + 40}" width="{pw}" height="3" fill="{WHITE}" opacity=".35"/>')
    if awning:
        stripes = int(sw // 14)
        for s in range(stripes):
            out.append(f'<rect x="{x + s * 14}" y="{sy + 6}" width="14" height="22" fill="{awning if s % 2 == 0 else WHITE}"/>')
        out.append(f'<path d="M{x} {sy + 28} h{sw} v8 q-{sw / 2 / 7} 8 -{sw / 7} 0 z" fill="{awning}" opacity="0"/>')
    out.append('</g>')
    return "".join(out)


def hero_scene():
    base = 612
    s = []
    s.append('<svg class="scene" viewBox="0 0 1600 720" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMax slice">')
    s.append(f'''<defs>
  <radialGradient id="moonGlow"><stop offset="0" stop-color="{LIME}" stop-opacity=".55"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></radialGradient>
  <linearGradient id="lampCone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{LIME}" stop-opacity=".38"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></linearGradient>
  <radialGradient id="signGlow"><stop offset="0" stop-color="{LIME}" stop-opacity=".7"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></radialGradient>
  <linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY}" stop-opacity="0"/><stop offset="1" stop-color="{SKY}" stop-opacity=".35"/></linearGradient>
</defs>''')

    # --- sky furniture
    stars = [(120, 60), (300, 120), (470, 40), (760, 90), (860, 40), (1130, 70), (1380, 60), (1500, 150), (640, 160), (1010, 30), (1560, 70)]
    s.append('<g id="stars">')
    for i, (x, y) in enumerate(stars):
        s.append(f'<circle class="star" style="animation-delay:{(i * 0.37) % 3:.2f}s" cx="{x}" cy="{y}" r="{1.6 + (i % 3) * .5}" fill="{WHITE}"/>')
    s.append('</g>')
    s.append(f'<g id="moon"><circle cx="1215" cy="128" r="120" fill="url(#moonGlow)"/><circle cx="1215" cy="128" r="46" fill="{LIME}"/><circle cx="1232" cy="116" r="9" fill="#BEEA2C" opacity=".6"/><circle cx="1200" cy="146" r="6" fill="#BEEA2C" opacity=".6"/></g>')

    # clouds (drift)
    def cloud(x, y, sc, cls):
        return (f'<g class="cloud {cls}" transform="translate({x} {y}) scale({sc})"><path d="M0 40 q0 -22 24 -22 q8 -22 36 -18 q24 -14 44 6 q26 -4 30 20 q22 2 22 14 z" fill="{SKY}" opacity=".5"/></g>')
    s.append(cloud(180, 160, 1.1, "c1") + cloud(780, 70, .8, "c2") + cloud(1330, 230, 1.0, "c3"))

    # birds
    s.append('<g id="birds">')
    for i, (x, y, d) in enumerate([(900, 200, 0), (950, 184, .4), (930, 220, .8)]):
        s.append(f'<path class="bird" style="animation-delay:{d}s" d="M{x} {y} q8 -9 16 0 q8 -9 16 0" fill="none" stroke="{WHITE}" stroke-width="2.4" stroke-linecap="round" opacity=".85"/>')
    s.append('</g>')

    # --- FAR layer
    s.append('<g id="far">')
    s.append(f'<path d="M0 {base} V430 h60 v-40 h50 v40 h40 v-70 h30 v70 h70 v-110 q14 -30 28 -70 q14 40 28 70 v110 h60 v-60 h50 v60 h46 v-96 h22 v96 h80 v-130 h40 v130 h40 V{base} z" fill="{DEEP}" opacity=".72"/>')
    # shikhara temple (right)
    s.append(f'<path d="M1370 {base} V330 q-6 -60 20 -110 q8 -22 4 -60 q16 28 28 60 q26 50 20 110 V{base} z" fill="{DEEP}" opacity=".78"/>')
    s.append(f'<path d="M1398 160 v-34" stroke="{DEEP}" stroke-width="4" opacity=".78"/><path d="M1398 126 l16 8 l-16 8 z" fill="{LIME}" opacity=".9"/>')
    s.append(f'<path d="M1100 {base} V420 h40 v-50 q40 -50 80 0 v50 h40 V{base} z M1040 {base} V440 h30 v-24 h30 v24 h20 V{base} z" fill="{DEEP}" opacity=".7"/>')
    # trees
    for (tx, ty, r) in [(470, 470, 54), (520, 486, 40), (700, 470, 46), (1080, 460, 40), (1560, 452, 56)]:
        s.append(f'<circle cx="{tx}" cy="{ty}" r="{r}" fill="{NAVY}" opacity=".5"/>')
    s.append('</g>')

    # --- MID layer (buildings)
    s.append('<g id="mid">')
    s.append(building(-20, 190, 470, base, GREY, "#A9B8CB", awning=LIME, seed=1, shop_h=86))
    s.append(building(158, 200, 436, base, PAPER, "#CCD7E4", awning=SKY, tank=True, seed=2, shop_h=86))
    s.append(building(366, 170, 486, base, SKY, "#8DC3CB", awning=WHITE, dish=True, seed=3, shop_h=86))
    s.append(building(544, 200, 412, base, MID, "#1F66B8", awning=LIME, tank=True, seed=4, shop_h=90))
    s.append(building(752, 168, 380, base, SKY, "#8DC3CB", awning=WHITE, dish=True, seed=5, shop_h=90))
    # clinic
    cx, cw, ctop = 928, 246, 318
    s.append(building(cx, cw, ctop, base, PAPER, "#CCD7E4", awning=None, tank=True, seed=6, shop_h=120, floors_gap=60))
    s.append(f'<g id="clinic">')
    s.append(f'<ellipse id="signGlow" class="glow" cx="{cx + cw / 2 - 8}" cy="{base - 150}" rx="190" ry="70" fill="url(#signGlow)"/>')
    s.append(f'<rect class="sign" x="{cx + 14}" y="{base - 172}" width="{cw - 44}" height="46" rx="10" fill="{NAVY}" stroke="{LIME}" stroke-width="3"/>')
    s.append(f'<g class="sign-cross"><rect x="{cx + 28}" y="{base - 160}" width="22" height="8" rx="2" fill="{LIME}"/><rect x="{cx + 35}" y="{base - 167}" width="8" height="22" rx="2" fill="{LIME}"/></g>')
    s.append(f'<text class="sign-text" x="{cx + 64}" y="{base - 141}" font-family="Figtree, sans-serif" font-weight="700" font-size="22" fill="{WHITE}" letter-spacing="3">CLINIC</text>')
    # door + doctor
    dx = cx + cw / 2 - 28
    s.append(f'<path d="M{dx - 4} {base} v-80 a34 34 0 0 1 68 0 v80 z" fill="{LIME}" opacity=".95"/>')
    s.append(doctor_figure(dx + 30, base, scale=0.92, skin=SKIN[0], coat=WHITE, hair=NAVY, cls="doc-wave"))
    s.append('</g>')
    s.append(building(1182, 190, 392, base, GREY, "#A9B8CB", awning=LIME, dish=True, seed=7, shop_h=90))
    s.append(building(1380, 220, 440, base, PAPER, "#CCD7E4", awning=SKY, tank=True, seed=8, shop_h=86))
    s.append('</g>')

    # --- pin (maps)
    px = cx + cw / 2 - 8
    s.append(f'<g id="pin"><g transform="translate({px} 0)">')
    s.append(f'<ellipse class="pin-shadow" cx="0" cy="{ctop - 14}" rx="20" ry="5" fill="{NAVY}" opacity=".35"/>')
    s.append(f'<g class="pin-rings">' + "".join(f'<circle class="ring r{i}" cx="0" cy="{ctop - 14}" rx="0" r="30" fill="none" stroke="{LIME}" stroke-width="3"/>' for i in range(3)) + '</g>')
    s.append(f'<g class="pin-drop"><g class="pin-float"><path d="M0 {ctop - 18} c-26 -30 -40 -44 -40 -68 a40 40 0 0 1 80 0 c0 24 -14 38 -40 68 z" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/>'
             f'<circle cx="0" cy="{ctop - 86}" r="15" fill="{NAVY}"/><path d="M-7 {ctop - 87} h14 M0 {ctop - 94} v14" stroke="{LIME}" stroke-width="4" stroke-linecap="round"/></g></g>')
    s.append(f'<g class="pin-bubble"><rect x="56" y="{ctop - 128}" width="172" height="42" rx="21" fill="{WHITE}"/><path d="M62 {ctop - 94} l-10 12 l22 -6 z" fill="{WHITE}"/>'
             f'<text x="142" y="{ctop - 101}" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="700" font-size="18" fill="{NAVY}">Your clinic</text>'
             '</g>')
    s.append('</g></g>')

    # --- NEAR layer: wires, poles, lamp, people, rickshaw, road
    s.append('<g id="near">')
    # poles & wires
    for (x, y) in [(486, 335), (1272, 330)]:
        s.append(f'<rect x="{x - 4}" y="{y}" width="8" height="{base - y}" fill="{NAVY}"/>')
        s.append(f'<rect x="{x - 30}" y="{y + 8}" width="60" height="6" rx="3" fill="{NAVY}"/>')
    for k, off in enumerate([0, 12, 24]):
        s.append(f'<path d="M-20 {350 + off} Q 230 {410 + off} 486 {343 + off} Q 880 {440 + off} 1272 {338 + off} Q 1460 {392 + off} 1640 {350 + off}" fill="none" stroke="{NAVY}" stroke-width="2" opacity=".65"/>')
    # lamp
    lx = 668
    s.append(f'<path d="M{lx - 6} {base - 4} V430 q0 -30 34 -30 h20" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>')
    s.append(f'<path class="cone" d="M{lx + 42} 408 L{lx - 10} {base} L{lx + 98} {base} z" fill="url(#lampCone)"/>')
    s.append(f'<rect x="{lx + 28}" y="398" width="34" height="12" rx="6" fill="{LIME}"/>')
    # footpath & road
    s.append(f'<rect x="-10" y="{base - 6}" width="1620" height="18" fill="#0B3F86"/>')
    s.append(f'<rect x="-10" y="{base + 12}" width="1620" height="120" fill="{NAVY}"/>')
    s.append(f'<rect x="-10" y="{base + 12}" width="1620" height="4" fill="{BLUE}" opacity=".7"/>')
    dashes = "".join(f'<rect x="{i * 150}" y="{base + 78}" width="72" height="6" rx="3" fill="{PAPER}" opacity=".7"/>' for i in range(-1, 12))
    s.append(f'<g class="dashes">{dashes}</g>')
    # people
    s.append(walker(120, base - 2, NAVY, LIME, cls="walk-a"))
    s.append(walker(1010, base - 2, WHITE, SKY, cls="walk-b"))
    s.append(f'<g class="rick" >{rickshaw()}</g>')
    s.append('</g>')
    s.append(f'<rect x="0" y="{base - 160}" width="1600" height="170" fill="url(#haze)" pointer-events="none"/>')
    s.append('</svg>')
    return "".join(s)


def walker(x, y, body, accent, cls=""):
    return (f'<g class="{cls}" transform="translate({x} {y})"><g class="step">'
            f'<circle cx="0" cy="-64" r="7" fill="{body}"/>'
            f'<path d="M-9 -56 h18 l3 28 h-24 z" fill="{body}"/>'
            f'<path d="M-9 -54 q9 12 18 0" fill="none" stroke="{accent}" stroke-width="4"/>'
            f'<rect x="-8" y="-30" width="6" height="30" rx="2" fill="{body}"/><rect x="2" y="-30" width="6" height="30" rx="2" fill="{body}"/>'
            f'</g></g>')


def rickshaw():
    return (f'<g transform="translate(0 {612 + 54})"><g class="rick-bob">'
            f'<ellipse cx="62" cy="2" rx="70" ry="5" fill="#000" opacity=".25"/>'
            # body
            f'<path d="M0 -20 v-46 q0 -18 18 -22 h60 q22 4 34 26 l14 22 q6 8 6 20 z" fill="{LIME}"/>'
            f'<path d="M0 -20 h132 v8 h-132 z" fill="#BEEA2C"/>'
            # roof
            f'<path d="M-4 -86 q0 -10 14 -12 h70 q18 0 28 12 z" fill="{NAVY}"/>'
            # windshield
            f'<path d="M90 -84 q14 6 24 26 l-34 0 z" fill="{SKY}" opacity=".9"/>'
            # seat/driver & passenger window
            f'<rect x="12" y="-80" width="50" height="34" rx="6" fill="{NAVY}" opacity=".88"/>'
            f'<circle cx="86" cy="-62" r="7" fill="{SKIN[1]}"/><path d="M76 -54 h20 l2 20 h-24 z" fill="{BLUE}"/>'
            f'<circle cx="34" cy="-64" r="6" fill="{SKIN[2]}"/><path d="M26 -58 h16 l2 14 h-20 z" fill="{PAPER}"/>'
            # headlight
            f'<circle class="headlight" cx="136" cy="-44" r="6" fill="{WHITE}"/><path class="beam" d="M142 -44 L230 -70 L230 -16 z" fill="{LIME}" opacity=".18"/>'
            # wheels
            f'<g><circle cx="26" cy="-12" r="14" fill="{NAVY}"/><circle cx="26" cy="-12" r="5" fill="{PAPER}"/></g>'
            f'<g><circle cx="116" cy="-12" r="14" fill="{NAVY}"/><circle cx="116" cy="-12" r="5" fill="{PAPER}"/></g>'
            f'</g></g>')


def doctor_figure(x, base, scale=1.0, skin=None, coat=WHITE, hair=NAVY, cls=""):
    skin = skin or SKIN[0]
    # standing doctor, feet at base, arm waving
    return (f'<g class="{cls}" transform="translate({x} {base}) scale({scale})">'
            f'<rect x="-14" y="-34" width="10" height="34" rx="3" fill="{NAVY}"/><rect x="4" y="-34" width="10" height="34" rx="3" fill="{NAVY}"/>'
            f'<path d="M-22 -92 q22 -14 44 0 l6 62 h-56 z" fill="{coat}"/>'
            f'<path d="M-6 -92 l6 30 l6 -30" fill="none" stroke="{BLUE}" stroke-width="3"/>'
            f'<path d="M-10 -88 q-6 22 4 30 M10 -88 q6 22 -4 30" stroke="{NAVY}" stroke-width="3" fill="none"/><circle cx="-5" cy="-56" r="4" fill="{NAVY}"/>'
            f'<g class="wave-arm"><path d="M22 -90 q18 -4 22 -30" stroke="{coat}" stroke-width="12" stroke-linecap="round" fill="none"/><circle cx="45" cy="-124" r="6" fill="{skin}"/></g>'
            f'<path d="M-22 -90 q-8 16 -4 34" stroke="{coat}" stroke-width="12" stroke-linecap="round" fill="none"/>'
            f'<circle cx="0" cy="-108" r="14" fill="{skin}"/>'
            f'<path d="M-15 -112 q2 -18 16 -16 q14 0 14 16 q-8 -8 -16 -6 q-8 0 -14 6 z" fill="{hair}"/>'
            f'</g>')


# ------------------------------------------------------------- avatars (doctor types)
def avatar(kind, size=96):
    """Flat doctor characters: ortho, gynaec, ivf, pulmo, hospital. Original drawings."""
    bg = {"ortho": SKY, "gynaec": LIME, "ivf": GREY, "pulmo": SKY, "hospital": PAPER}[kind]
    parts = [f'<svg class="avatar" viewBox="0 0 120 120" width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">',
             f'<circle cx="60" cy="60" r="60" fill="{bg}"/>',
             '<clipPath id="av-' + kind + '"><circle cx="60" cy="60" r="60"/></clipPath><g clip-path="url(#av-' + kind + ')">']
    if kind == "ortho":
        parts += [f'<path d="M14 130 q4 -44 46 -46 q42 2 46 46 z" fill="{WHITE}"/>',
                  f'<rect x="50" y="68" width="20" height="18" fill="{SKIN[1]}"/>',
                  f'<ellipse cx="60" cy="54" rx="21" ry="24" fill="{SKIN[1]}"/>',
                  f'<path d="M38 50 q0 -26 22 -26 q22 0 22 26 q-8 -14 -22 -14 q-14 0 -22 14 z" fill="{NAVY}"/>',
                  f'<g fill="none" stroke="{NAVY}" stroke-width="3"><circle cx="51" cy="56" r="7"/><circle cx="69" cy="56" r="7"/><path d="M58 56 h4"/></g>',
                  f'<path d="M48 70 q12 8 24 0" stroke="{NAVY}" stroke-width="3" fill="none"/>',
                  f'<path d="M40 90 q-6 20 10 26 M80 90 q6 20 -10 26" stroke="{NAVY}" stroke-width="3.5" fill="none"/>',
                  f'<path d="M60 84 l-8 14 l8 8 l8 -8 z" fill="{BLUE}"/>']
    elif kind == "gynaec":
        parts += [f'<path d="M14 130 q4 -44 46 -46 q42 2 46 46 z" fill="{WHITE}"/>',
                  f'<circle cx="60" cy="24" r="12" fill="{NAVY}"/>',
                  f'<rect x="51" y="68" width="18" height="16" fill="{SKIN[0]}"/>',
                  f'<ellipse cx="60" cy="52" rx="20" ry="24" fill="{SKIN[0]}"/>',
                  f'<path d="M38 56 q-4 -34 22 -34 q26 0 22 34 q-4 -22 -22 -22 q-18 0 -22 22 z" fill="{NAVY}"/>',
                  f'<circle cx="60" cy="42" r="2.6" fill="{BLUE}"/>',
                  f'<circle cx="52" cy="54" r="2.4" fill="{NAVY}"/><circle cx="68" cy="54" r="2.4" fill="{NAVY}"/>',
                  f'<path d="M52 64 q8 6 16 0" stroke="{NAVY}" stroke-width="3" fill="none" stroke-linecap="round"/>',
                  f'<path d="M42 88 q-4 22 12 26 M78 88 q4 22 -12 26" stroke="{NAVY}" stroke-width="3.5" fill="none"/><circle cx="54" cy="114" r="5" fill="{NAVY}"/>']
    elif kind == "ivf":
        parts += [f'<path d="M14 130 q4 -44 46 -46 q42 2 46 46 z" fill="{SKY}"/>',
                  f'<rect x="51" y="68" width="18" height="16" fill="{SKIN[2]}"/>',
                  f'<ellipse cx="60" cy="52" rx="20" ry="23" fill="{SKIN[2]}"/>',
                  f'<path d="M39 48 q2 -26 21 -26 q20 0 21 26 q-6 -10 -21 -10 q-15 0 -21 10 z" fill="{NAVY}"/>',
                  f'<circle cx="52" cy="54" r="2.4" fill="{NAVY}"/><circle cx="68" cy="54" r="2.4" fill="{NAVY}"/>',
                  f'<path d="M52 64 q8 6 16 0" stroke="{NAVY}" stroke-width="3" fill="none" stroke-linecap="round"/>',
                  f'<path d="M44 88 l16 20 l16 -20" stroke="{WHITE}" stroke-width="6" fill="none"/>',
                  f'<circle cx="86" cy="96" r="9" fill="{WHITE}" stroke="{BLUE}" stroke-width="3"/><circle cx="86" cy="96" r="3" fill="{LIME}"/>']
    elif kind == "pulmo":
        parts += [f'<path d="M14 130 q4 -44 46 -46 q42 2 46 46 z" fill="{WHITE}"/>',
                  f'<rect x="51" y="68" width="18" height="16" fill="{SKIN[3]}"/>',
                  f'<ellipse cx="60" cy="52" rx="21" ry="24" fill="{SKIN[3]}"/>',
                  f'<path d="M38 48 q0 -26 22 -26 q22 0 22 26 q-10 -12 -22 -12 q-12 0 -22 12 z" fill="{NAVY}"/>',
                  f'<path d="M42 58 h36 q-2 20 -18 22 q-16 -2 -18 -22 z" fill="{SKY}"/><path d="M42 60 l-6 -6 M78 60 l6 -6" stroke="{SKY}" stroke-width="2.5"/>',
                  f'<circle cx="52" cy="52" r="2.4" fill="{NAVY}"/><circle cx="68" cy="52" r="2.4" fill="{NAVY}"/>',
                  f'<path d="M60 84 v22 M46 92 q14 20 28 0" stroke="{NAVY}" stroke-width="3.5" fill="none"/>']
    else:  # hospital
        parts += [f'<rect x="22" y="36" width="76" height="90" fill="{WHITE}"/><rect x="22" y="36" width="76" height="10" fill="{BLUE}"/>',
                  f'<rect x="52" y="52" width="16" height="30" rx="3" fill="{LIME}"/><rect x="45" y="59" width="30" height="16" rx="3" fill="{LIME}"/>',
                  f'<g fill="{NAVY}" opacity=".75"><rect x="30" y="92" width="12" height="16" rx="6"/><rect x="54" y="92" width="12" height="16" rx="6"/><rect x="78" y="92" width="12" height="16" rx="6"/></g>']
    parts.append('</g></svg>')
    return "".join(parts)


def k_avatar(size=96):
    return f'<img class="avatar" src="assets/icon-gradient.png" width="{size}" height="{size}" alt="" style="border-radius:50%">'


# ------------------------------------------------------------- lotus
def lotus(cls="lotus", size=420):
    petals = []
    spec = [(-72, .78, SKY), (72, .78, SKY), (-46, .92, WHITE), (46, .92, WHITE), (-22, 1.0, SKY), (22, 1.0, SKY), (0, 1.12, WHITE)]
    order = sorted(spec, key=lambda p: -abs(p[0]))
    for i, (ang, sc, col) in enumerate(order):
        petals.append(f'<g class="petal" style="--a:{ang}deg;--i:{i}" transform="translate(200 300)"><g transform="rotate({ang}) scale({sc})">'
                      f'<path d="M0 0 C-46 -52 -40 -150 0 -208 C40 -150 46 -52 0 0 z" fill="{col}" stroke="{NAVY}" stroke-width="3.5" stroke-linejoin="round"/>'
                      f'<path d="M0 -20 C-10 -70 -8 -120 0 -170" fill="none" stroke="{NAVY}" stroke-width="2.4" opacity=".35"/></g></g>')
    return (f'<svg class="{cls}" viewBox="0 0 400 340" width="{size}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            f'<path d="M20 318 q90 -26 180 -6 q90 -20 180 6" fill="none" stroke="{SKY}" stroke-width="5" stroke-linecap="round" opacity=".6"/>'
            + "".join(petals) +
            f'<g transform="translate(200 300)"><circle cx="0" cy="-12" r="14" fill="{LIME}" stroke="{NAVY}" stroke-width="3.5"/></g></svg>')


# ------------------------------------------------------------- service icons
def icon(kind, size=300):
    h = 240
    head = f'<svg class="svc-art art-{kind}" viewBox="0 0 320 {h}" width="{size}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
    body = ""
    if kind == "reels":
        body = (f'<rect x="96" y="14" width="128" height="212" rx="22" fill="{NAVY}"/>'
                f'<rect x="104" y="26" width="112" height="188" rx="14" fill="{BLUE}"/>'
                f'<circle cx="160" cy="112" r="26" fill="{LIME}"/><path d="M152 98 l22 14 l-22 14 z" fill="{NAVY}"/>'
                f'<rect x="114" y="168" width="70" height="8" rx="4" fill="{WHITE}"/><rect x="114" y="184" width="46" height="8" rx="4" fill="{SKY}"/>'
                f'<g class="floaters"><path class="f1" d="M246 120 c-10 -14 -30 -2 -18 14 l18 16 l18 -16 c12 -16 -8 -28 -18 -14z" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/>'
                f'<path class="f2" d="M70 150 c-8 -11 -24 -2 -14 11 l14 13 l14 -13 c10 -13 -6 -22 -14 -11z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
                f'<circle class="f3" cx="266" cy="70" r="10" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/></g>')
    elif kind == "gmb":
        body = (f'<rect x="30" y="40" width="260" height="170" rx="16" fill="{PAPER}" stroke="{NAVY}" stroke-width="4"/>'
                f'<path d="M30 120 q70 -40 120 -10 t140 -20" fill="none" stroke="{GREY}" stroke-width="10"/><path d="M60 40 v170 M180 40 v170" stroke="{GREY}" stroke-width="6" opacity=".6"/>'
                f'<rect x="60" y="150" width="130" height="14" rx="7" fill="{NAVY}"/><rect x="60" y="174" width="90" height="10" rx="5" fill="{GREY}"/>'
                f'<g fill="{LIME}" stroke="{NAVY}" stroke-width="2">' + "".join(f'<path transform="translate({204 + i * 16} 150)" d="M0 -8 l3 6 7 1 -5 5 1 7 -6 -3 -6 3 1 -7 -5 -5 7 -1z"/>' for i in range(5)) + '</g>'
                f'<g class="pin-b"><path d="M200 112 c-20 -22 -30 -32 -30 -50 a30 30 0 0 1 60 0 c0 18 -10 28 -30 50z" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/><circle cx="200" cy="62" r="11" fill="{NAVY}"/></g>'
                f'<rect x="236" y="176" width="40" height="22" rx="11" fill="{BLUE}"/><text x="256" y="191" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="11" fill="{WHITE}">Open</text>')
    elif kind == "ads":
        body = (f'<g class="mega"><path d="M70 100 l130 -52 v130 l-130 -52 z" fill="{LIME}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
                f'<rect x="40" y="96" width="42" height="52" rx="10" fill="{BLUE}" stroke="{NAVY}" stroke-width="4"/>'
                f'<path d="M92 150 l10 46 h26 l-12 -38" fill="{NAVY}"/></g>'
                f'<g class="waves" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"><path d="M220 90 q16 22 0 44"/><path d="M240 76 q26 36 0 72"/><path d="M260 62 q36 50 0 100"/></g>'
                f'<g><rect x="214" y="160" width="86" height="44" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><circle cx="234" cy="182" r="9" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/><rect x="250" y="172" width="38" height="7" rx="3.5" fill="{NAVY}"/><rect x="250" y="186" width="26" height="7" rx="3.5" fill="{GREY}"/></g>')
    elif kind == "calendar":
        cells = ""
        for r in range(4):
            for c in range(5):
                x = 62 + c * 38; y = 86 + r * 32
                tick = (r * 5 + c) % 3 == 0
                cells += f'<rect x="{x}" y="{y}" width="30" height="24" rx="6" fill="{LIME if tick else WHITE}" stroke="{NAVY}" stroke-width="2.5"/>'
        body = (f'<rect x="170" y="30" width="110" height="150" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" transform="rotate(8 225 105)"/>'
                f'<g transform="rotate(8 225 105)"><rect x="186" y="52" width="60" height="8" rx="4" fill="{BLUE}"/><rect x="186" y="72" width="78" height="6" rx="3" fill="{GREY}"/><rect x="186" y="88" width="70" height="6" rx="3" fill="{GREY}"/><rect x="186" y="104" width="78" height="6" rx="3" fill="{GREY}"/></g>'
                f'<rect x="40" y="36" width="230" height="180" rx="16" fill="{PAPER}" stroke="{NAVY}" stroke-width="4"/>'
                f'<rect x="40" y="36" width="230" height="36" rx="16" fill="{BLUE}"/><rect x="40" y="56" width="230" height="16" fill="{BLUE}"/>'
                f'<rect x="76" y="24" width="10" height="26" rx="5" fill="{NAVY}"/><rect x="224" y="24" width="10" height="26" rx="5" fill="{NAVY}"/>'
                + cells)
    elif kind == "brand":
        body = (f'<rect x="40" y="30" width="150" height="150" rx="26" fill="{BLUE}" stroke="{NAVY}" stroke-width="4"/>'
                f'<rect x="64" y="58" width="102" height="10" rx="5" fill="{LIME}"/><rect x="64" y="82" width="80" height="8" rx="4" fill="{SKY}"/><rect x="64" y="100" width="92" height="8" rx="4" fill="{SKY}"/><circle cx="84" cy="146" r="14" fill="{LIME}"/><circle cx="118" cy="146" r="14" fill="{SKY}"/><circle cx="152" cy="146" r="14" fill="{WHITE}"/>'
                f'<circle cx="238" cy="78" r="46" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/><circle cx="238" cy="78" r="30" fill="{SKY}"/><path d="M214 108 q24 -30 48 0" fill="{NAVY}"/><circle cx="238" cy="70" r="12" fill="{SKIN[0]}"/><path d="M226 64 q12 -16 24 0 q-12 -4 -24 0z" fill="{NAVY}"/>'
                f'<g class="swatch"><rect x="204" y="150" width="32" height="32" rx="8" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/><rect x="238" y="150" width="32" height="32" rx="8" fill="{LIME}" stroke="{NAVY}" stroke-width="3"/><rect x="272" y="150" width="32" height="32" rx="8" fill="{NAVY}" stroke="{NAVY}" stroke-width="3"/></g>')
    return head + body + '</svg>'


# ------------------------------------------------------------- strips for inner page heroes
def skyline_strip():
    s = ['<svg class="strip" viewBox="0 0 1600 170" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    s.append(f'<path d="M0 170 V96 h70 v-40 h46 v40 h60 v-70 q12 -26 24 -50 q12 24 24 50 v70 h60 v-52 h40 v52 h80 v-84 h26 v84 h60 v-60 h50 v60 h90 v-100 h30 v100 h70 v-42 h70 v42 h100 v-90 q12 -30 24 -60 q12 30 24 60 v90 h70 v-50 h44 v50 h90 v-70 h30 v70 h60 v-36 h60 v36 h150 z" fill="{DEEP}" opacity=".8"/>')
    s.append(f'<path d="M0 170 V128 h120 v-30 h40 v30 h90 v-46 h60 v46 h100 v-24 h50 v24 h130 v-54 h60 v54 h110 v-36 h70 v36 h120 v-48 h50 v48 h140 v-30 h90 v30 h120 v-20 h70 v20 h140 z" fill="{NAVY}"/>')
    # lit windows
    for i in range(34):
        x = 40 + i * 47; y = 134 + (i * 7) % 20
        s.append(f'<rect x="{x}" y="{y}" width="8" height="10" rx="3" fill="{LIME}" opacity="{.9 if i % 3 else .0}"/>')
    s.append('</svg>')
    return "".join(s)


def ghat():
    s = ['<svg class="ghat" viewBox="0 0 1200 460" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" preserveAspectRatio="xMidYMax slice">']
    s.append(f'<defs><radialGradient id="gSun"><stop offset="0" stop-color="{LIME}" stop-opacity=".6"/><stop offset="1" stop-color="{LIME}" stop-opacity="0"/></radialGradient></defs>')
    s.append(f'<circle cx="1010" cy="150" r="150" fill="url(#gSun)"/><circle cx="1010" cy="150" r="54" fill="{LIME}"/>')
    # far temples
    s.append(f'<g fill="{DEEP}" opacity=".85"><path d="M60 300 V240 h40 v-60 q10 -30 20 -60 q10 30 20 60 v60 h40 v60 z"/><path d="M300 300 V220 q20 -60 50 -110 q30 50 50 110 v80 z"/><path d="M520 300 V250 h60 v-40 q20 -50 40 -90 q20 40 40 90 v40 h60 v50 z"/><path d="M820 300 V230 h30 v-34 q14 -44 28 -70 q14 26 28 70 v34 h30 v70 z"/><path d="M1040 300 V250 h50 v-50 q12 -34 25 -60 q13 26 25 60 v50 h50 v50 z"/></g>')
    # ghat steps
    for i in range(9):
        y = 300 + i * 16
        s.append(f'<rect x="0" y="{y}" width="1200" height="16" fill="{[PAPER, SKY, GREY][i % 3]}" opacity="{.95 - i * .06:.2f}"/>')
    # water
    s.append(f'<rect x="0" y="420" width="1200" height="40" fill="{BLUE}"/>')
    s.append(f'<g class="ripple" fill="none" stroke="{SKY}" stroke-width="3" stroke-linecap="round" opacity=".7"><path d="M80 432 q20 -8 40 0 t40 0"/><path d="M400 444 q20 -8 40 0 t40 0"/><path d="M700 434 q20 -8 40 0 t40 0"/><path d="M1000 446 q20 -8 40 0 t40 0"/></g>')
    # boat
    s.append(f'<g class="boat"><path d="M300 404 h160 q-14 24 -40 24 h-80 q-26 0 -40 -24 z" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/><path d="M380 404 v-52 l44 40 z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><rect x="378" y="350" width="4" height="54" fill="{NAVY}"/></g>')
    # diyas
    for (x, y) in [(120, 440), (240, 452), (560, 446), (860, 440), (1100, 450)]:
        s.append(f'<g class="diya"><path d="M{x - 11} {y} q11 12 22 0 z" fill="{LIME}" stroke="{NAVY}" stroke-width="2.5"/><path d="M{x} {y - 2} q-6 -10 0 -16 q6 6 0 16" fill="{WHITE}"/></g>')
    s.append('</svg>')
    return "".join(s)


def wa_icon(size=22):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38a9.9 9.9 0 0 0 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2zm0 18.15c-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.38c0-4.54 3.7-8.23 8.25-8.23 4.54 0 8.23 3.69 8.23 8.23s-3.7 8.24-8.23 8.24zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.17.25-.64.81-.78.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-2-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.02-.38.11-.51.11-.11.25-.29.37-.43.12-.14.17-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43h-.48c-.17 0-.43.06-.66.31-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.23 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.67-1.18.21-.58.21-1.07.14-1.18-.06-.1-.23-.16-.48-.29z"/></svg>')


# ------------------------------------------------------------- v3 metaphor art
def bridge():
    """Clinic on the left, home on the right, Karunya builds the bridge of light between them."""
    s = ['<svg class="bridge" viewBox="0 0 1200 420" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    s.append('<defs><linearGradient id="br" x1="0" x2="1"><stop offset="0" stop-color="#D1FF42"/><stop offset="1" stop-color="#B0E0E6"/></linearGradient></defs>')
    # ground
    s.append(f'<path d="M0 360 Q300 340 600 352 T1200 350 V420 H0z" fill="{NAVY}" opacity=".5"/>')
    # clinic
    s.append(f'<g class="b-clinic"><rect x="80" y="170" width="200" height="190" rx="6" fill="{PAPER}"/><rect x="80" y="170" width="200" height="22" fill="{BLUE}"/>'
             f'<rect x="164" y="210" width="32" height="64" rx="6" fill="{LIME}"/><rect x="148" y="226" width="64" height="32" rx="6" fill="{LIME}"/>'
             f'<path d="M156 360 v-56 a24 24 0 0 1 48 0 v56z" fill="{NAVY}"/>'
             f'<text x="180" y="396" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="20" fill="{SKY}">Your clinic</text></g>')
    # home
    s.append(f'<g class="b-home"><path d="M930 240 L1030 170 L1130 240 V360 H930z" fill="{PAPER}"/><path d="M915 248 L1030 160 L1145 248" fill="none" stroke="{BLUE}" stroke-width="14" stroke-linejoin="round"/>'
             f'<rect class="b-win" x="960" y="262" width="44" height="40" rx="6" fill="{LIME}"/><rect x="1050" y="290" width="40" height="70" rx="6" fill="{NAVY}"/>'
             f'<text x="1030" y="396" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="20" fill="{SKY}">Your patient</text></g>')
    # bridge arc
    p = "M280 250 C 480 40, 720 40, 930 250"
    s.append(f'<path d="{p}" fill="none" stroke="{SKY}" stroke-width="3" stroke-dasharray="6 10" opacity=".45"/>')
    s.append(f'<path class="b-arc" d="{p}" fill="none" stroke="url(#br)" stroke-width="8" stroke-linecap="round" pathLength="100"/>')
    # travelling tokens: reel, pin, heart, star
    toks = [("M0 10 C-14 0 -12 -12 -5 -12 C-2 -12 0 -9 0 -7 C0 -9 2 -12 5 -12 C12 -12 14 0 0 10z", LIME), ("M0 -12 l3.5 7 7.5 1 -5.5 5 1.4 7.5 -6.9 -3.6 -6.9 3.6 1.4 -7.5 -5.5 -5 7.5 -1z", WHITE)]
    for i, (d, c) in enumerate(toks):
        s.append(f'<g class="b-tok"><path d="{d}" fill="{c}" stroke="{NAVY}" stroke-width="2.5"/>'
                 f'<animateMotion dur="5s" begin="{i * 2.5}s" repeatCount="indefinite" path="{p}" rotate="0"/></g>')
    # Karunya badge at the top of the arc
    s.append(f'<g class="b-k"><circle cx="605" cy="92" r="40" fill="{NAVY}" stroke="{LIME}" stroke-width="4"/><text x="605" y="114" text-anchor="middle" font-family="Waylimo,serif" font-size="56" fill="{LIME}">K</text></g>')
    s.append('</svg>')
    return "".join(s)


def footer_scene():
    s = ['<svg class="f-scene" viewBox="0 0 1600 260" preserveAspectRatio="xMidYMax slice" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    for i, (x, y) in enumerate([(80, 40), (260, 90), (420, 30), (700, 70), (980, 40), (1180, 90), (1380, 30), (1520, 80), (560, 110), (860, 120)]):
        s.append(f'<circle class="star" style="animation-delay:{i * .4:.1f}s" cx="{x}" cy="{y}" r="2" fill="{WHITE}"/>')
    s.append(f'<circle cx="1300" cy="70" r="34" fill="{LIME}" opacity=".9"/><circle cx="1300" cy="70" r="70" fill="{LIME}" opacity=".08"/>')
    # Kashi skyline: temples and ghats
    s.append(f'<path d="M0 260 V190 h60 v-30 h40 v30 h50 v-60 q14 -40 28 -70 q14 30 28 70 v60 h70 v-40 h40 v40 h60 v-90 q18 -50 36 -90 q18 40 36 90 v90 h80 v-36 h50 v36 h90 v-70 q12 -30 24 -56 q12 26 24 56 v70 h70 v-46 h40 v46 h100 v-100 q20 -60 40 -100 q20 40 40 100 v100 h80 v-30 h60 v30 h70 v-66 q14 -36 28 -60 q14 24 28 60 v66 h90 v-40 h60 v40 h120 V260z" fill="#0A2A55"/>')
    for i in range(8):
        y = 214 + i * 6
        s.append(f'<rect x="0" y="{y}" width="1600" height="6" fill="{["#123A6E", "#0E3262"][i % 2]}"/>')
    s.append(f'<rect x="0" y="236" width="1600" height="24" fill="{BLUE}" opacity=".55"/>')
    s.append(f'<g class="ripple" fill="none" stroke="{SKY}" stroke-width="2" opacity=".6"><path d="M120 246 q16 -6 32 0 t32 0"/><path d="M640 252 q16 -6 32 0 t32 0"/><path d="M1180 246 q16 -6 32 0 t32 0"/></g>')
    s.append(f'<g class="boat"><path d="M420 236 h110 q-10 16 -28 16 h-54 q-18 0 -28 -16z" fill="{LIME}"/><path d="M474 236 v-38 l30 30z" fill="{WHITE}"/></g>')
    for x in range(70, 1600, 120):
        s.append(f'<g class="diya" style="animation-delay:{(x % 7) * .2:.1f}s"><path d="M{x - 7} 214 q7 8 14 0z" fill="{LIME}"/><path d="M{x} 212 q-4 -7 0 -12 q4 5 0 12" fill="#FFE7A3"/></g>')
    s.append('</svg>')
    return "".join(s)


def lost_scene():
    """404: a rickshaw driver lost in the galis, a map pin searching, street signs pointing everywhere."""
    s = ['<svg class="lost" viewBox="0 0 560 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    s.append(f'<circle cx="280" cy="250" r="210" fill="{BLUE}" opacity=".35"/><circle class="orbit" cx="280" cy="250" r="190" fill="none" stroke="{SKY}" stroke-width="2" stroke-dasharray="4 12" opacity=".6"/>')
    # big 404 made of street sign boards
    s.append(f'<g class="signpost"><rect x="272" y="60" width="10" height="330" fill="{NAVY}"/>'
             f'<g class="sign sg1"><path d="M282 84 h150 l22 22 -22 22 h-150z" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/><text x="352" y="114" text-anchor="middle" font-family="Waylimo,serif" font-size="34" fill="{NAVY}">404</text></g>'
             f'<g class="sign sg2"><path d="M272 150 h-140 l-22 20 22 20 h140z" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><text x="196" y="177" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="17" fill="{NAVY}">Yahan nahi</text></g>'
             f'<g class="sign sg3"><path d="M282 206 h120 l20 18 -20 18 h-120z" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="346" y="230" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="16" fill="{NAVY}">Wahan bhi nahi</text></g></g>')
    # searching pin with question mark
    s.append(f'<g class="lost-pin"><path d="M120 300 c-22 -24 -34 -36 -34 -56 a34 34 0 0 1 68 0 c0 20 -12 32 -34 56z" fill="{LIME}" stroke="{NAVY}" stroke-width="4"/>'
             f'<text x="120" y="256" text-anchor="middle" font-family="Waylimo,serif" font-size="40" fill="{NAVY}">?</text></g>')
    s.append(f'<ellipse class="lost-shadow" cx="120" cy="316" rx="20" ry="5" fill="{NAVY}" opacity=".4"/>')
    # road
    s.append(f'<rect x="20" y="390" width="520" height="40" rx="20" fill="{NAVY}"/>' + "".join(f'<rect x="{50 + i * 90}" y="407" width="40" height="5" rx="2.5" fill="{PAPER}" opacity=".7"/>' for i in range(6)))
    # rickshaw + confused driver
    s.append(f'<g class="lost-rick" transform="translate(330 0)">{rickshaw().replace("translate(0 666)", "translate(0 396)")}</g>')
    s.append(f'<g class="driver" transform="translate(436 300)"><circle cx="0" cy="0" r="16" fill="{SKIN[1]}"/><path d="M-16 -4 q16 -22 32 0 q-16 -8 -32 0z" fill="{NAVY}"/>'
             f'<circle cx="-5" cy="1" r="2" fill="{NAVY}"/><circle cx="6" cy="1" r="2" fill="{NAVY}"/><path d="M-5 9 q5 -3 10 0" stroke="{NAVY}" stroke-width="2.5" fill="none"/>'
             f'<g class="scratch"><path d="M14 -6 q16 -10 18 10" stroke="{BLUE}" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="14" cy="-8" r="5" fill="{SKIN[1]}"/></g></g>')
    # floating question marks
    for i, (x, y) in enumerate([(470, 240), (500, 200), (440, 210)]):
        s.append(f'<text class="qm" style="animation-delay:{i * .7:.1f}s" x="{x}" y="{y}" font-family="Waylimo,serif" font-size="{30 - i * 4}" fill="{LIME}">?</text>')
    # map in hand
    s.append(f'<g class="lost-map" transform="translate(372 316) rotate(-8)"><rect width="56" height="40" rx="4" fill="{PAPER}" stroke="{NAVY}" stroke-width="3"/><path d="M8 30 q12 -18 22 -6 t20 -14" stroke="{RED_SAFE}" stroke-width="3" fill="none" stroke-dasharray="4 4"/></g>')
    s.append('</svg>')
    return "".join(s)


RED_SAFE = "#E0475B"


def journey(cls="journey", compact=False):
    """Viral journey: a reel plays -> likes & shares burst -> people find it -> map pin -> clinic, doctor waves.
    Micro-motion only; a dot travels the whole path on loop."""
    W, H = 1200, 300
    s = [f'<svg class="{cls}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">']
    path = "M150 170 C 260 70, 360 70, 450 150 S 640 230, 720 150 S 900 70, 1040 160"
    s.append(f'<path d="{path}" fill="none" stroke="{SKY}" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round" opacity=".55"/>')
    s.append(f'<path class="j-line" d="{path}" fill="none" stroke="{LIME}" stroke-width="4" stroke-linecap="round" pathLength="100"/>')
    # 1. phone with reel
    s.append(f'<g class="j-phone"><rect x="88" y="96" width="96" height="170" rx="18" fill="{NAVY}" stroke="{SKY}" stroke-width="3"/>'
             f'<rect x="97" y="108" width="78" height="146" rx="10" fill="{BLUE}"/>'
             f'<circle cx="136" cy="170" r="20" fill="{LIME}"/><path d="M130 160 l16 10 -16 10z" fill="{NAVY}"/>'
             f'<rect x="106" y="226" width="44" height="6" rx="3" fill="{WHITE}" opacity=".8"/><rect x="106" y="238" width="28" height="6" rx="3" fill="{SKY}" opacity=".8"/></g>')
    # likes / shares rising from phone
    for i, (x, sym) in enumerate([(120, "heart"), (150, "share"), (106, "heart"), (166, "eye")]):
        if sym == "heart":
            d = f'<path d="M{x} 92 c-6 -8 -18 -2 -12 8 l12 10 l12 -10 c6 -10 -6 -16 -12 -8z" fill="{LIME}"/>'
        elif sym == "share":
            d = f'<path d="M{x - 8} 98 l16 -8 v6 h6 v4 h-6 v6z" fill="{WHITE}"/>'
        else:
            d = f'<g><ellipse cx="{x}" cy="96" rx="11" ry="7" fill="{WHITE}"/><circle cx="{x}" cy="96" r="3.5" fill="{NAVY}"/></g>'
        s.append(f'<g class="j-up" style="animation-delay:{i * .7:.1f}s">{d}</g>')
    # 2. social icons cluster (platform-neutral glyphs)
    icons = [(400, 92, "ig"), (452, 70, "yt"), (500, 100, "g"), (448, 122, "wa")]
    for i, (x, y, k) in enumerate(icons):
        if k == "ig":
            g = f'<rect x="-15" y="-15" width="30" height="30" rx="9" fill="none" stroke="{NAVY}" stroke-width="3.5"/><circle r="7" fill="none" stroke="{NAVY}" stroke-width="3.5"/>'
        elif k == "yt":
            g = f'<rect x="-17" y="-12" width="34" height="24" rx="7" fill="{NAVY}"/><path d="M-5 -6 l11 6 -11 6z" fill="{LIME}"/>'
        elif k == "g":
            g = f'<circle r="15" fill="none" stroke="{NAVY}" stroke-width="3.5"/><path d="M2 -1 h11" stroke="{NAVY}" stroke-width="3.5"/><circle cx="0" cy="0" r="3" fill="{NAVY}"/>'
        else:
            g = f'<path d="M0 -15 a15 15 0 1 1 -11 25 l-6 3 2 -7 a15 15 0 0 1 15 -21z" fill="none" stroke="{NAVY}" stroke-width="3.5"/>'
        s.append(f'<g class="j-ico" style="animation-delay:{i * .5:.1f}s" transform="translate({x} {y})"><circle r="24" fill="{LIME if i % 2 == 0 else WHITE}"/>{g}</g>')
    # 3. people appearing (patients finding the reel)
    for i, (x, y, skin) in enumerate([(610, 210, SKIN[0]), (650, 236, SKIN[1]), (690, 206, SKIN[2]), (632, 176, SKIN[3]), (676, 168, SKIN[0])]):
        s.append(f'<g class="j-person" style="animation-delay:{i * .35:.2f}s"><circle cx="{x}" cy="{y}" r="9" fill="{skin}"/>'
                 f'<path d="M{x - 11} {y + 26} q11 -20 22 0z" fill="{WHITE if i % 2 else SKY}"/></g>')
    # 4. map pin
    s.append(f'<g class="j-pin"><path d="M860 120 c-18 -20 -28 -30 -28 -46 a28 28 0 0 1 56 0 c0 16 -10 26 -28 46z" fill="{LIME}" stroke="{NAVY}" stroke-width="3.5"/>'
             f'<circle cx="860" cy="74" r="10" fill="{NAVY}"/></g><ellipse class="j-pinsh" cx="860" cy="128" rx="14" ry="4" fill="{NAVY}" opacity=".35"/>')
    # 5. clinic + doctor
    s.append(f'<g class="j-clinic"><rect x="990" y="150" width="140" height="120" rx="6" fill="{PAPER}"/><rect x="990" y="150" width="140" height="16" fill="{BLUE}"/>'
             f'<rect x="1046" y="178" width="28" height="10" rx="3" fill="{LIME}"/><rect x="1055" y="169" width="10" height="28" rx="3" fill="{LIME}"/>'
             f'<path d="M1044 270 v-40 a16 16 0 0 1 32 0 v40z" fill="{NAVY}"/>'
             f'<rect class="j-win" x="1004" y="210" width="22" height="22" rx="4" fill="{SKY}"/><rect class="j-win w2" x="1094" y="210" width="22" height="22" rx="4" fill="{SKY}"/></g>')
    s.append(doctor_figure(1160, 270, scale=.62, skin=SKIN[1], coat=WHITE, hair=NAVY, cls="j-doc"))
    # traveller
    s.append(f'<circle r="7" fill="{LIME}"><animateMotion dur="7s" repeatCount="indefinite" path="{path}"/></circle>')
    s.append(f'<circle r="14" fill="{LIME}" opacity=".25"><animateMotion dur="7s" repeatCount="indefinite" path="{path}"/></circle>')
    if not compact:
        labels = [(136, "Reel"), (450, "Viral"), (650, "People share"), (860, "Search"), (1060, "Clinic")]
        for x, t in labels:
            s.append(f'<text x="{x}" y="296" text-anchor="middle" font-family="Figtree,sans-serif" font-weight="700" font-size="17" fill="{SKY}">{t}</text>')
    s.append('</svg>')
    return "".join(s)
