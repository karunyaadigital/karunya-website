"""Free Google + Instagram check: instant scored audit + Netlify Forms lead capture."""

QUESTIONS = [
    ("g", "g1", "Do you have a Google Business Profile for your clinic?", [("Yes, and I manage it", 10), ("Yes, but nobody updates it", 5), ("No / not sure", 0)],
     "Claim and complete your Google Business Profile. It is the first thing a patient sees when they search “near me”."),
    ("g", "g2", "How many Google reviews do you have?", [("150+", 10), ("50 to 150", 7), ("10 to 50", 4), ("Under 10", 1)],
     "Make your profile easy to find with a QR code at reception, and let genuine reviews come on their own. Never buy reviews or chase patients for them."),
    ("g", "g3", "Do you reply to your Google reviews?", [("Always", 10), ("Sometimes", 5), ("Never", 0)],
     "Reply to every review, good or bad, politely and without patient details. Patients read the replies."),
    ("g", "g4", "Photos on your Google profile?", [("20+ recent photos", 10), ("A few old photos", 4), ("None", 0)],
     "Add 20+ clear photos: clinic front, reception, OPD, team and you. A profile with photos gets many more calls."),
    ("g", "g5", "Do you post updates on Google?", [("Every week", 10), ("Once in a while", 4), ("Never", 0)],
     "Post one Google update every week: a health tip, timings or a camp. It keeps your profile active."),
    ("i", "i1", "Do you have an Instagram page for your practice?", [("Yes, a professional page", 10), ("Only my personal account", 4), ("No", 0)],
     "Create a professional Instagram page in your name with your speciality, city and WhatsApp in the bio."),
    ("i", "i2", "How many reels do you post per month?", [("8 or more", 10), ("4 to 8", 7), ("1 to 3", 3), ("None", 0)],
     "Post at least 2 reels a week answering real patient questions. Consistency matters more than perfection."),
    ("i", "i3", "Do you appear in your own videos?", [("Yes, regularly", 10), ("Sometimes", 5), ("Never", 1)],
     "Patients trust a face and a voice. Even a 20-second video of you explaining one thing builds trust."),
    ("i", "i4", "How many followers do you have?", [("20,000+", 10), ("5,000 to 20,000", 7), ("1,000 to 5,000", 4), ("Under 1,000", 1)],
     "Reels that answer local patient questions bring new followers from your own city. Focus on local, not viral."),
    ("i", "i5", "Does your bio have your clinic address, timings and a WhatsApp link?", [("Yes, all of it", 10), ("Some of it", 5), ("No", 0)],
     "Add clinic address, timings and a one-tap WhatsApp link to your bio, so interest turns into an appointment."),
]


def audit_form():
    blocks = {"g": "", "i": ""}
    for grp, qid, q, opts, tip in QUESTIONS:
        o = "".join(f'<label><input type="radio" name="{qid}" value="{s}" data-label="{t}"><span>{t}</span></label>' for t, s in opts)
        blocks[grp] += f'<fieldset class="aq" data-tip="{tip}"><legend>{q}</legend><div class="aq-opts">{o}</div></fieldset>'
    return blocks
