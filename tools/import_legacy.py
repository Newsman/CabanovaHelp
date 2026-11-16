#!/usr/bin/env python3
"""Importă o singură dată articolele vechi de pe help.cabanova.com (editorul clasic, EN) în content/ro/editorul-vechi/."""
import re, sys, time, urllib.request, html
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
R = Path(__file__).resolve().parent.parent
SRC = "https://help.cabanova.com/"
OUT = R / "content/ro/editorul-vechi"; IMG = R / "static/legacy"
OUT.mkdir(parents=True, exist_ok=True); IMG.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 Chrome/130"}
def get(u):
    for i in range(6):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read()
        except Exception as e:
            if "429" not in str(e) or i == 5: raise
            time.sleep(5 * (i + 1))
lines = [l.split("\t") for l in (R / "tools/legacy-en.tsv").read_text().splitlines() if l and not l.startswith("#")]
slugs = {s for _, s, _ in lines}
group, order, w = None, {}, 0

def md(node):
    out = []
    for c in node.children:
        if isinstance(c, NavigableString): out.append(re.sub(r"\s+", " ", str(c))); continue
        t = c.name; inner = md(c)
        st = (c.get("style") or "").replace(" ", "")
        if t in ("br",): out.append("\n")
        elif t in ("div", "p"): out.append("\n\n" + inner.strip() + "\n\n")
        elif t in ("h1", "h2", "h3", "h4"): out.append("\n\n## " + inner.strip() + "\n\n")
        elif t == "li": out.append("\n- " + inner.strip())
        elif t in ("ul", "ol"): out.append("\n" + inner + "\n")
        elif t == "a":
            href = c.get("href", "")
            if href.endswith(".html") and href[:-5] in slugs: href = "../" + href[:-5] + "/"
            out.append(f"[{inner.strip()}]({href})" if inner.strip() and href else inner)
        elif t in ("b", "strong") or "font-weight:bold" in st:
            out.append(f"**{inner.strip()}** " if inner.strip() else inner)
        else: out.append(inner)
    return "".join(out)

for lv, slug, title in lines:
    lv = int(lv); w += 1
    if lv == 1: group = title
    try: soup = BeautifulSoup(get(SRC + slug + ".html"), "lxml")
    except Exception as e: print("EROARE", slug, e); continue
    els = []
    for el in soup.select(".cbel"):
        cls = el.get("class"); st = el.get("style") or ""
        top = re.search(r"top:(\d+)", st); left = re.search(r"left:(\d+)", st)
        if not top or not left or int(left.group(1)) < 330 or int(top.group(1)) < 340 or "cb-behaviour" in cls: continue
        if "cb-text" in cls:
            txt = el.get_text(" ", strip=True)
            if not txt or txt.startswith(("< Go", "∧", "<", "Go ")) or el.find_parent(class_="cbel"): continue
            if el.find("h1"): continue
            els.append((int(top.group(1)), int(left.group(1)), "t", el))
        elif "cb-image" in cls and el.name == "img":
            els.append((int(top.group(1)), int(left.group(1)), "i", el))
    els.sort(key=lambda x: (x[0], x[1]))
    body = []
    for top, left, k, el in els:
        if k == "t":
            body.append(re.sub(r"\n{3,}", "\n\n", re.sub(r"[ \t]+\n", "\n", md(el))).strip())
        else:
            src = el.get("src", ""); name = src.split("/")[-1]
            try:
                if not (IMG / name).exists(): (IMG / name).write_bytes(get(SRC + src))
                body.append(f'![{html.escape(el.get("alt") or title)}](legacy/{name})')
            except Exception as e: print("img", slug, src, e)
    text = "\n\n".join(b for b in body if b)
    text = re.sub(r"\*\*\s*\*\*", "", text); text = re.sub(r"\n{3,}", "\n\n", text)
    fm = f'---\ntitle: "{title}"\ngroup: "{group}"\nweight: {w}\nlegacy: true\naliases: ["/{slug}.html"]\n---\n'
    (OUT / f"{slug}.md").write_text(fm + text + "\n")
    time.sleep(0.6)
print("gata", len(lines))
