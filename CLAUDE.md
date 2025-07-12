# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static personal portfolio website built with HTML, CSS, and minimal JavaScript. It's based on the "Identity" template by HTML5 UP and is deployed via GitHub Pages.

## Development Workflow

Since this is a static site with no build process:
- Edit HTML/CSS files directly
- Test changes by opening `index.html` in a browser
- Commit and push to `main` branch to deploy via GitHub Pages

## Architecture and Structure

### Key Files
- `index.html` - Single page containing all content
- `assets/css/main.css` - Primary stylesheet
- `umut-celik.png` - Profile image referenced in HTML

### Design Patterns
- **Single Page Application**: All content is in index.html
- **Responsive Design**: Uses media queries for mobile/tablet breakpoints
- **Progressive Enhancement**: Includes IE8+ compatibility layers
- **Data URI Usage**: Favicon is embedded as data URI for security

## Deployment

### GitHub Pages (Primary - Working)
GitHub Pages deployment is automated via `.github/workflows/static.yml`:
- Triggers on push to `main` branch
- No build step required - deploys static files directly
- Site available at: https://umutcelik.github.io/personal-home-page/
- Status: ✅ Successfully deployed

### AWS Amplify (Secondary - Has Issues)
AWS Amplify deployment configuration:
- App ID: d29ml85157wf4g
- Region: eu-west-1
- Console: https://eu-west-1.console.aws.amazon.com/amplify/apps/d29ml85157wf4g
- Domain: https://d29ml85157wf4g.amplifyapp.com
- Build spec: Defined in `amplify.yml`
- Status: ❌ Failing due to IAM role assumption error
- Issue: "Unable to assume specified IAM Role" - requires AWS Console intervention

## Important Considerations

1. **No Build Process**: This is pure HTML/CSS - no npm, webpack, or build tools
2. **Browser Compatibility**: Maintains support for older browsers (IE8+)
3. **External Resources**: Uses Google Fonts and has Google Analytics integration
4. **Template License**: Based on Identity by HTML5 UP (CCA 3.0 license)

## AWS Configuration

- AWS profile is umut. (--profile umut)

## Amplify Configuration

- Amplify Project ID: d29ml85157wf4g
- Region: eu-west-1
- Repository: Connected via GitHub OAuth token
- Build Spec: Uses `amplify.yml` (no build required for static site)
- IAM Role: Currently has issues - app was configured with `arn:aws:iam::585576670327:role/umut-home-amplify` but fails to assume it