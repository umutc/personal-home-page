# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio site for Umut Celik at https://umutcelik.com.tr. Static HTML/CSS, no build step, deployed via GitHub Pages on every push to `main`.

## Development Workflow

Edit files, commit, push. There's no build step and no framework to learn.

```bash
# Local preview
python3 -m http.server 8000
# open http://localhost:8000
```

## Architecture

- `index.html` — homepage, semantic HTML with JSON-LD Person schema in head
- `blog/index.html` — post list; `blog/<slug>/index.html` — one folder per post (BlogPosting JSON-LD, og tags)
- `assets/css/main.css` — tokens, the shared shell (page width, site nav, footer, skip link) and the homepage; system font stack, `prefers-color-scheme` dark mode
- `assets/css/post.css` — blog-only styles, loaded after `main.css` on blog pages; charts are static SVG or HTML/CSS bars, no JS
- `umut-celik.jpg` — avatar (400x400, ~60 KB, resized from a 767 KB PNG via `sips`)
- `robots.txt` + `sitemap.xml` — crawler metadata
- `CNAME` — managed automatically by GitHub Pages Settings; do not create a file by hand

## Deployment

**GitHub Pages is the only live target.** Configured via `.github/workflows/static.yml`:
- Triggers on push to `main` (or via `workflow_dispatch`)
- No build. The workflow copies an explicit allowlist of site files into `_site/` and uploads only that folder, so CLAUDE.md, README.md, scripts/ and editor config are never served. A new public file must be added to that `cp` line.
- After deploy the workflow pings IndexNow (Bing, and through it ChatGPT search and Copilot) with every URL in `sitemap.xml`; the key file is the `<hex>.txt` at the repo root.
- Takes ~1-2 minutes; watch with `gh run list -R umutc/personal-home-page`

### DNS / domain (do not change)

- Custom domain `umutcelik.com.tr` is set in GitHub Pages Settings (no `CNAME` file in repo)
- Route53 hosted zone `Z06846003RPNEE6EG5Y01` (AWS profile `personal`)
- A records point to GitHub Pages IPs `185.199.108-111.153`
- `www` CNAME → `umutc.github.io`
- HTTPS via Let's Encrypt, provisioned automatically by GitHub Pages

### Retired infrastructure

The old AWS Amplify app (`d2ktjps5ul2e7i`, eu-west-1) and ACM validation CNAMEs are inactive but still exist. Do not reconnect or redeploy to Amplify.

## Content rules

- Content is English (job market is US). Comments, commits, PR messages: English.
- The public name is "Umut Celik" (ASCII, no Ç) everywhere: titles, headings, alt text, structured data, OG images, favicon. The only exception is the invisible JSON-LD `alternateName`, which lets searches for the Turkish spelling resolve to the same person.
- Keep it tight. No skill bars, no "hire me" buttons, no auto-play anything, no testimonials carousel.
- No phone number anywhere: not in the page HTML, not in the hosted resume PDF.
- Public location is "New York, NY".
- Personal job-search rules and identity sources live in `CLAUDE.local.md` (gitignored, never committed). Read it before changing public content.
- Work section: 3-4 roles max, curated. Latest first.

## Tech guardrails

- JSON-LD dates (`dateModified`, `datePublished`, `dateCreated`) are full ISO 8601 datetimes with offset, e.g. `2026-09-30T00:00:00-04:00`. A bare date makes Search Console flag ProfilePage with "Invalid datetime value".
- No JS unless a feature genuinely needs it (JSON-LD data blocks are fine). New posts reuse `post.css`. For each new post: add it to `blog/index.html` (and its Blog JSON-LD), the homepage Writing panel, `blog/feed.xml`, `sitemap.xml` and `llms.txt`; add an entry to `POSTS` in `scripts/build-og.py` and regenerate the OG images; link the author to the `#person` @id.
- System font stack (no Google Fonts, no web fonts). Page should render before first paint.
- Lighthouse target: 100/100/100/100. If a change drops any score, revert or fix.
- No external analytics beacon currently. If added later, prefer Plausible over GA4.
- Accessibility: `<html lang="en">`, skip link, semantic landmarks, visible `:focus-visible` outline, `prefers-reduced-motion` respected.
