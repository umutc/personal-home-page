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

### AWS Amplify (Secondary - Working)
AWS Amplify deployment configuration:
- App ID: d2ktjps5ul2e7i
- Region: eu-west-1
- Console: https://eu-west-1.console.aws.amazon.com/amplify/apps/d2ktjps5ul2e7i
- Default Domain: https://d2ktjps5ul2e7i.amplifyapp.com
- Custom Domain: https://umutcelik.com.tr (and https://www.umutcelik.com.tr)
- Build spec: Defined in `amplify.yml`
- Status: ✅ Successfully deployed
- Note: Recreated app without IAM role to resolve permission issues

### Custom Domain Configuration
- Primary Domain: umutcelik.com.tr
- DNS: Managed via Route53 (Hosted Zone ID: Z06846003RPNEE6EG5Y01)
- SSL: AWS Certificate Manager (ACM) managed certificate
- CloudFront Distribution: d2hcxo4m33ny9y.cloudfront.net
- Both root domain and www subdomain are configured

## Important Considerations

1. **No Build Process**: This is pure HTML/CSS - no npm, webpack, or build tools
2. **Browser Compatibility**: Maintains support for older browsers (IE8+)
3. **External Resources**: Uses Google Fonts and has Google Analytics integration
4. **Template License**: Based on Identity by HTML5 UP (CCA 3.0 license)

## AWS Configuration

- AWS profile is umut. (--profile umut)

## Amplify Configuration

- Amplify Project ID: d2ktjps5ul2e7i
- Region: eu-west-1
- Repository: Connected via GitHub OAuth token
- Build Spec: Uses `amplify.yml` (no build required for static site)
- IAM Role: None (using default Amplify permissions)