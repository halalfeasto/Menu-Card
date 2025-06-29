# Security Policy

## Supported Versions

This project is a static website for restaurant menu display. Security updates are provided for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Considerations

### Content Security
- All images and videos are locally hosted
- No external API calls or third-party integrations
- No user data collection or storage
- No form submissions or user input handling

### Best Practices Implemented
- ✅ Static HTML/CSS/JavaScript only
- ✅ No server-side processing
- ✅ No database connections
- ✅ No user authentication required
- ✅ No sensitive data stored
- ✅ Responsive design with mobile optimization

### Potential Security Areas
- **Cross-Site Scripting (XSS)**: Mitigated by using static content only
- **Content Security**: All media files are self-hosted
- **Privacy**: No tracking or analytics implemented
- **Data Protection**: No personal data collection

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it by:

1. **Do NOT** create a public GitHub issue
2. Email the maintainers directly at: [your-security-email@domain.com]
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

### Response Timeline
- **Initial Response**: Within 48 hours
- **Status Update**: Within 1 week
- **Fix Implementation**: Within 2 weeks (for valid vulnerabilities)

## Security Guidelines for Contributors

When contributing to this project:

1. **No External Dependencies**: Avoid adding external JavaScript libraries or APIs
2. **Local Assets Only**: All images, videos, and resources should be self-hosted
3. **Static Content**: Maintain the static nature of the website
4. **Code Review**: All changes should be reviewed before merging
5. **Testing**: Test on multiple browsers and devices

## Deployment Security

When deploying this website:

### Recommended Hosting Platforms
- ✅ GitHub Pages (free, secure)
- ✅ Netlify (free tier available)
- ✅ Vercel (free tier available)
- ✅ Traditional web hosting with HTTPS

### Security Headers (Recommended)
```
Content-Security-Policy: default-src 'self'; img-src 'self'; video-src 'self'; style-src 'self' 'unsafe-inline'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
```

### HTTPS Configuration
- Always use HTTPS in production
- Implement HTTP to HTTPS redirects
- Use secure hosting platforms that provide SSL certificates

## Privacy Considerations

This website:
- ❌ Does NOT collect user data
- ❌ Does NOT use cookies
- ❌ Does NOT track users
- ❌ Does NOT require user registration
- ✅ Is completely anonymous for visitors

## File Security

### Excluded from Repository
- No sensitive configuration files
- No API keys or credentials
- No personal information
- No payment processing code

### Safe Files Included
- ✅ Static HTML, CSS, JavaScript
- ✅ Restaurant food images
- ✅ Promotional videos
- ✅ Public restaurant information

## Updates and Maintenance

- Security updates will be applied as needed
- Dependencies are minimal (only Tailwind CSS via CDN)
- Regular security reviews of the codebase
- Monitoring for any potential vulnerabilities

---

For any security questions or concerns, please contact the project maintainers.