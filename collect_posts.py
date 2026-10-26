"""One-off collector for public posts on the Anime Forums discussion board.

Respects robots.txt (Crawl-delay: 3). Keeps each post's own text only: quoted
text, images, scripts and usernames are dropped. Writes raw posts to a JSON file.

    python collect_posts.py --out raw_posts.json --max-posts 500
"""
import argparse
import html
import json
import re
import time
import urllib.request
from html.parser import HTMLParser

BASE = "https://animeforums.net"
FORUM = BASE + "/forum/8-anime-discussion/"
UA = "Mozilla/5.0 (course project, one-off read)"
DELAY = 3


def fetch(url):
    time.sleep(DELAY)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


class PostParser(HTMLParser):
    """Collects the own text of each data-role='commentContent' block."""

    SKIP = {"blockquote", "script", "style", "iframe"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.posts = []
        self.depth = 0       # div depth inside a post, 0 = outside
        self.skip = 0        # depth inside a skipped element
        self.buf = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if self.buf is None:
            if tag == "div" and a.get("data-role") == "commentContent":
                self.buf, self.depth = [], 1
            return
        if tag in self.SKIP:
            self.skip += 1
        elif tag == "div":
            self.depth += 1
        elif tag in ("br", "p") and not self.skip:
            self.buf.append("\n")

    def handle_endtag(self, tag):
        if self.buf is None:
            return
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
        elif tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.posts.append(clean("".join(self.buf)))
                self.buf = None
        elif tag == "p" and not self.skip:
            self.buf.append("\n")

    def handle_data(self, data):
        if self.buf is not None and not self.skip:
            self.buf.append(data)


def clean(text):
    text = html.unescape(text).replace("\xa0", " ")
    text = re.sub(r"^\s*Edited [^\n]* by [^\n]*$", "", text, flags=re.M)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def topic_links(page):
    found = re.findall(r"""href=["'](https://animeforums\.net/topic/\d+-[^"'/?#]+/)["']""", page)
    seen = []
    for u in found:
        if u not in seen:
            seen.append(u)
    return seen


def next_page(page):
    m = re.search(r"""<link rel=["']next["'] href=["']([^"']+)["']""", page)
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="raw_posts.json")
    ap.add_argument("--max-posts", type=int, default=500)
    ap.add_argument("--max-listing-pages", type=int, default=8)
    ap.add_argument("--per-topic", type=int, default=12,
                    help="keep at most this many posts per thread (first page only), "
                         "so one long thread can't dominate")
    args = ap.parse_args()

    topics, url, n = [], FORUM, 0
    while url and n < args.max_listing_pages:
        page = fetch(url)
        for t in topic_links(page):
            if t not in topics:
                topics.append(t)
        url, n = next_page(page), n + 1
    print(f"{len(topics)} topics from {n} listing pages")

    rows, seen = [], set()
    for t in topics:
        page = fetch(t)
        p = PostParser()
        p.feed(page)
        for i, text in enumerate(p.posts[:args.per_topic]):
            if text and text not in seen:
                seen.add(text)
                rows.append({"topic": t, "text": text, "first_in_page": i == 0})
        print(f"{len(rows)} posts so far", flush=True)
        if len(rows) >= args.max_posts:
            break

    with open(args.out, "w") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(rows)} posts to {args.out}")


if __name__ == "__main__":
    main()
