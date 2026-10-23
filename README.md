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

The Vercel project is linked to this repository: every push to `main` deploys to production.

1. **10:50 a.m. Eastern:** a scheduled Claude task researches AI agent adoption, writes a post and commits `posts/YYYY-MM-DD.json` and `posts/index.json` here. The push deploys the site, so the post is live by about 11 a.m. The same task then shares it on LinkedIn.
2. **11:15 a.m. Eastern:** the GitHub Actions workflow `.github/workflows/sync-posts.yml` runs `scripts/sync_posts.py` as a safety net. If a post reached the live site without being committed here, the workflow copies it into `posts/` and commits it. You can also run it by hand from the Actions tab ("Publish daily post to GitHub" → "Run workflow").

`.vercelignore` keeps this README, `scripts/` and `.github/` out of the deployed site.

## Running locally

The blog loads its posts with `fetch`, so serve the folder rather than opening the file directly:

```
python3 -m http.server 8000
```

Then open http://localhost:8000.
