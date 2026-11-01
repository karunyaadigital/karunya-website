"""Animated flat characters for the team section. Each one is doing their job, so the team reads as many hands."""

INK = "#012A5E"
SKIN = ["#F2C29B", "#E0A878", "#C98D5E", "#F5CBA7"]
HAIR = "#1D2340"


def _bust(skin, shirt, hair_kind="short", glasses=False, extra_head=""):
    hair = {
        "short": f'<path d="M58 52 Q56 26 80 24 Q104 26 102 50 L98 42 Q86 34 70 38 Q62 42 60 52Z" fill="{HAIR}"/>',
        "long": f'<path d="M56 54 Q54 22 80 22 Q106 22 104 54 L108 96 Q80 104 52 96Z" fill="{HAIR}"/><path d="M60 50 Q62 30 80 30 Q98 30 100 50 Q92 38 80 38 Q68 38 60 50Z" fill="{HAIR}"/>',
        "bun": f'<circle cx="80" cy="20" r="11" fill="{HAIR}"/><path d="M58 52 Q58 28 80 27 Q102 28 102 52 Q94 36 80 36 Q66 36 58 52Z" fill="{HAIR}"/>',
        "curly": f'<g fill="{HAIR}"><circle cx="64" cy="34" r="10"/><circle cx="78" cy="27" r="11"/><circle cx="93" cy="32" r="10"/><circle cx="101" cy="44" r="7"/><circle cx="59" cy="46" r="7"/></g>',
    }[hair_kind]
    behind = hair if hair_kind == "long" else ""
    front = "" if hair_kind == "long" else hair
    gl = (f'<rect x="64" y="50" width="13" height="10" rx="4" fill="#ffffff80" stroke="{INK}" stroke-width="2.4"/>'
          f'<rect x="83" y="50" width="13" height="10" rx="4" fill="#ffffff80" stroke="{INK}" stroke-width="2.4"/><path d="M77 55h6" stroke="{INK}" stroke-width="2"/>') if glasses else ""
    return f'''{behind}<path d="M36 150 Q38 104 80 100 Q122 104 124 150Z" fill="{shirt}" stroke="{INK}" stroke-width="3"/>
<rect x="72" y="80" width="16" height="22" fill="{skin}" stroke="{INK}" stroke-width="2.5"/>
<g class="t-head"><circle cx="80" cy="56" r="25" fill="{skin}" stroke="{INK}" stroke-width="3"/>{front}
<g class="t-eyes"><circle cx="71" cy="56" r="2.4" fill="{INK}"/><circle cx="89" cy="56" r="2.4" fill="{INK}"/></g>{gl}
<path d="M72 67 Q80 73 88 67" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>{extra_head}</g>'''


def char(kind):
    """kind: script, editor, motion, design, google, care, research"""
    if kind == "script":   # writing on a laptop, lines appear
        body = _bust(SKIN[0], "#B0E0E6", "bun", glasses=True)
        prop = (f'<g class="t-laptop"><rect x="34" y="112" width="92" height="34" rx="5" fill="#fff" stroke="{INK}" stroke-width="3"/>'
                f'<rect class="t-line l1" x="44" y="120" width="48" height="4" rx="2" fill="#0251B0"/><rect class="t-line l2" x="44" y="128" width="62" height="4" rx="2" fill="#C7D1DD"/>'
                f'<rect class="t-line l3" x="44" y="136" width="36" height="4" rx="2" fill="#C7D1DD"/></g>')
    elif kind == "editor":  # headphones + moving timeline playhead
        hp = f'<path d="M54 56 Q54 26 80 26 Q106 26 106 56" fill="none" stroke="{INK}" stroke-width="5"/><rect x="48" y="50" width="10" height="18" rx="4" fill="#D1FF42" stroke="{INK}" stroke-width="2.5"/><rect x="102" y="50" width="10" height="18" rx="4" fill="#D1FF42" stroke="{INK}" stroke-width="2.5"/>'
        body = _bust(SKIN[2], "#0251B0", "short", extra_head=hp)
        prop = (f'<g><rect x="30" y="118" width="100" height="26" rx="5" fill="{INK}"/>'
                f'<rect x="36" y="123" width="26" height="7" rx="2" fill="#D1FF42"/><rect x="64" y="123" width="38" height="7" rx="2" fill="#B0E0E6"/><rect x="104" y="123" width="20" height="7" rx="2" fill="#F5B301"/>'
                f'<rect x="36" y="133" width="60" height="5" rx="2" fill="#5A6D8C"/><rect class="t-play" x="36" y="119" width="2.5" height="22" fill="#fff"/></g>')
    elif kind == "motion":  # stylus drawing a sparkle that pops
        body = _bust(SKIN[1], "#D1FF42", "curly")
        prop = (f'<g><rect x="40" y="112" width="80" height="36" rx="6" fill="#fff" stroke="{INK}" stroke-width="3"/>'
                f'<path class="t-draw" d="M52 138 C62 118 74 140 84 124 S104 120 110 128" fill="none" stroke="#0251B0" stroke-width="3" stroke-linecap="round" pathLength="1"/></g>'
                f'<path class="t-spark" d="M124 92 l3 8 8 3 -8 3 -3 8 -3 -8 -8 -3 8 -3z" fill="#F5B301"/>')
    elif kind == "design":  # colour palette dots cycling
        body = _bust(SKIN[3], "#F3F6FA", "long")
        prop = (f'<g class="t-pal"><ellipse cx="80" cy="132" rx="44" ry="16" fill="#fff" stroke="{INK}" stroke-width="3"/>'
                f'<circle class="t-dot d1" cx="58" cy="130" r="6" fill="#0251B0"/><circle class="t-dot d2" cx="74" cy="126" r="6" fill="#D1FF42"/>'
                f'<circle class="t-dot d3" cx="90" cy="126" r="6" fill="#B0E0E6"/><circle class="t-dot d4" cx="104" cy="131" r="6" fill="#012A5E"/></g>')
    elif kind == "google":  # map pin dropping with a ring
        body = _bust(SKIN[0], "#012A5E", "short", glasses=True)
        prop = (f'<g><ellipse class="t-ring" cx="124" cy="138" rx="12" ry="4" fill="none" stroke="#0251B0" stroke-width="2"/>'
                f'<g class="t-pin"><path d="M124 136 C124 136 110 122 110 112 A14 14 0 0 1 138 112 C138 122 124 136 124 136Z" fill="#E5484D" stroke="{INK}" stroke-width="2.5"/><circle cx="124" cy="112" r="5" fill="#fff"/></g></g>')
    elif kind == "care":  # phone with WhatsApp bubbles popping
        body = _bust(SKIN[2], "#B0E0E6", "bun")
        prop = (f'<g><rect x="104" y="96" width="26" height="46" rx="6" fill="{INK}"/><rect x="107" y="101" width="20" height="34" rx="3" fill="#fff"/>'
                f'<rect class="t-bub b1" x="110" y="104" width="13" height="7" rx="3" fill="#25D366"/><rect class="t-bub b2" x="111" y="114" width="13" height="7" rx="3" fill="#C7D1DD"/>'
                f'<rect class="t-bub b3" x="110" y="124" width="13" height="7" rx="3" fill="#25D366"/></g>')
    else:  # research: lightbulb blinking over a notepad
        body = _bust(SKIN[1], "#0251B0", "long", glasses=True)
        prop = (f'<g class="t-bulb"><circle cx="122" cy="34" r="11" fill="#D1FF42" stroke="{INK}" stroke-width="2.5"/><rect x="117" y="44" width="10" height="7" rx="2" fill="{INK}"/></g>'
                f'<g><rect x="40" y="114" width="56" height="34" rx="4" fill="#fff" stroke="{INK}" stroke-width="3"/><path d="M48 124h38M48 132h30M48 140h34" stroke="#C7D1DD" stroke-width="3" stroke-linecap="round"/></g>')
    return f'<svg class="tchar t-{kind}" viewBox="0 0 160 150" aria-hidden="true">{body}{prop}</svg>'


TEAM = [
    ("photo", "Bhanu Pratap Rai", "Founder & strategy", "Sets the plan for every doctor we work with. Shares lessons for doctors on @bhanuhelpsdoctors."),
    ("script", "Ankita Rai", "Manager & scripts", "Writes the scripts and runs client coordination, so every reel says the right thing."),
    ("research", "Research team", "Topics & keywords", "Finds what patients in your city are asking and searching, every week."),
    ("editor", "Video editing team", "High-end editing", "Editors who pair AI tools with real craft and understand the emotion of every cut."),
    ("motion", "Motion graphics team", "Animation", "Turns hard medical ideas into simple, moving visuals patients remember."),
    ("design", "Design team", "Brand & thumbnails", "Your colours, covers, thumbnails and printables, consistent everywhere."),
    ("google", "Google & SEO team", "Search & maps", "Keeps your Google profile, posts and pages working so you show up first."),
    ("care", "Client care", "Always on WhatsApp", "Your one point of contact for approvals, changes and quick questions."),
]
