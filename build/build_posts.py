import os, re, glob
import markdown as _md
POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")


def load_posts():
    posts = []
    for f in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")), reverse=True):
        raw = open(f, encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            continue
        meta = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        base = os.path.basename(f)[:-3]
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)
        meta["slug"] = "blog-" + slug
        meta["html"] = _md.markdown(m.group(2), extensions=["tables", "sane_lists"])
        meta.setdefault("category", "Strategy")
        meta.setdefault("minutes", "5")
        posts.append(meta)
    posts.sort(key=lambda p: p.get("date", ""), reverse=True)
    return posts


