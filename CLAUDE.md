# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio site for Umut Çelik at https://umutcelik.com.tr. Static HTML/CSS, no build step, deployed via GitHub Pages on every push to `main`.

## Development Workflow

Edit files, commit, push. There's no build step and no framework to learn.

```bash
# Local preview
python3 -m http.server 8000
# open http://localhost:8000
```

## Architecture

- `index.html` — single page, semantic HTML with JSON-LD Person schema in head
- `assets/css/main.css` — hand-written CSS, system font stack, CSS variables, `prefers-color-scheme` dark mode
- `umut-celik.jpg` — avatar (400x400, ~60 KB, resized from a 767 KB PNG via `sips`)
- `robots.txt` + `sitemap.xml` — crawler metadata
- `CNAME` — managed automatically by GitHub Pages Settings; do not create a file by hand

## Deployment

**GitHub Pages is the only live target.** Configured via `.github/workflows/static.yml`:
- Triggers on push to `main` (or via `workflow_dispatch`)
- No build — uploads the repo root as the Pages artifact
- Takes ~1-2 minutes; watch with `gh run list -R umutc/personal-home-page`

### DNS / domain (do not change)

- Custom domain `umutcelik.com.tr` is set in GitHub Pages Settings (no `CNAME` file in repo)
- Route53 hosted zone `Z06846003RPNEE6EG5Y01` (AWS profile `umut`)
- A records point to GitHub Pages IPs `185.199.108-111.153`
- `www` CNAME → `umutc.github.io`
- HTTPS via Let's Encrypt, provisioned automatically by GitHub Pages

### Retired infrastructure

The old AWS Amplify app (`d2ktjps5ul2e7i`, eu-west-1) and ACM validation CNAMEs are inactive but still exist. Do not reconnect or redeploy to Amplify.

## Content rules

- Content is English (job market is US). Comments, commits, PR messages: English.
- Keep it tight. No skill bars, no "hire me" buttons, no auto-play anything, no testimonials carousel.
- Do not mention visa / sponsorship / F-1 / CPT / OPT on the public site. Those conversations belong after recruiter interest is established.
- Phone number stays off the site.
- Work section: 3-4 roles max, curated. Latest first.

## Tech guardrails

- Keep the page single-file, no JS unless a feature genuinely needs it.
- System font stack (no Google Fonts, no web fonts). Page should render before first paint.
- Lighthouse target: 100/100/100/100. If a change drops any score, revert or fix.
- No external analytics beacon currently. If added later, prefer Plausible over GA4.
- Accessibility: `<html lang="en">`, skip link, semantic landmarks, visible `:focus-visible` outline, `prefers-reduced-motion` respected.

## Canonical identity data

The source of truth for Umut's work history, skills, education, and contact info lives in `/Users/umut/code/carrier/knowledge/people/umut-celik/`. When updating site content (new role, new stack), pull from there rather than inventing copy.
