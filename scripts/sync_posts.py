"""Copy blog posts from the live site into this repository.

Reads https://asim-siddique.vercel.app/posts/index.json, downloads every post
file that is missing (or different) here, and rewrites posts/index.json to
match the live site. Prints a one-line summary; exits non-zero on bad data.
"""
import json
import pathlib
import re
import sys
import urllib.request

SITE = "https://asim-siddique.vercel.app"
ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "posts"
ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fetch(path):
    req = urllib.request.Request(SITE + path, headers={"Cache-Control": "no-cache", "User-Agent": "blog-sync"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    POSTS.mkdir(exist_ok=True)
    index_bytes = fetch("/posts/index.json")
    ids = json.loads(index_bytes).get("posts", [])
    bad = [i for i in ids if not ID_RE.match(str(i))]
    if bad:
        sys.exit(f"Unexpected post IDs in live index: {bad}")

    changed = []
    for pid in ids:
        body = fetch(f"/posts/{pid}.json")
        post = json.loads(body)  # validates JSON
        if not post.get("title") or post.get("date") != pid:
            sys.exit(f"Post {pid} is missing a title or has a mismatched date")
        target = POSTS / f"{pid}.json"
        if not target.exists() or target.read_bytes() != body:
            target.write_bytes(body)
            changed.append(pid)

    idx = POSTS / "index.json"
    if not idx.exists() or idx.read_bytes() != index_bytes:
        idx.write_bytes(index_bytes)
        changed.append("index")

    print("changed: " + (", ".join(changed) if changed else "nothing"))


if __name__ == "__main__":
    main()
