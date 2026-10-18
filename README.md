# Asim Siddique — personal website

Source for https://asim-siddique.vercel.app, the personal brand site of Asim Siddique (security, compliance and enterprise infrastructure).

## What's here

| Path | Purpose |
|---|---|
| `index.html` | Homepage: hero, career stats, about, expertise, selected work, experience, credentials, latest blog posts, contact |
| `blog.html` | Blog page listing every post with its sources |
| `blog.js` | Small loader shared by both pages; reads `posts/index.json` and the post files |
| `posts/index.json` | List of post IDs (`YYYY-MM-DD`), newest first |
| `posts/YYYY-MM-DD.json` | One file per post: `slug`, `date`, `title`, `summary`, `content` (paragraphs), `sources` |
| `headshot.webp` | Portrait used on the homepage |

It is a static site with no build step. Every page is plain HTML, CSS and JavaScript.

## Adding a post

1. Add `posts/YYYY-MM-DD.json` with the fields above.
2. Add the same `YYYY-MM-DD` to the top of the list in `posts/index.json`.
3. Deploy.

## Daily publishing

1. **10:50 a.m. Eastern:** a scheduled Claude task researches AI agent adoption, writes a post and deploys it straight to Vercel, so it is live by about 11 a.m.
2. **11:15 a.m. Eastern:** the GitHub Actions workflow `.github/workflows/sync-posts.yml` runs `scripts/sync_posts.py`. The script copies any new posts from the live site into `posts/`, and the workflow commits them here. You can also run it by hand from the Actions tab ("Publish daily post to GitHub" → "Run workflow").

## Running locally

The blog loads its posts with `fetch`, so serve the folder rather than opening the file directly:

```
python3 -m http.server 8000
```

Then open http://localhost:8000.
