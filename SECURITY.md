# Security Policy

## Reporting Security Vulnerabilities

**Do NOT create a public GitHub issue for security vulnerabilities.**

If you discover a security vulnerability in IntelSource, please follow these steps:

1. **Email** the vulnerability details to: [Open an issue with security label](https://github.com/osint-intell/IntelSource/security/advisories)
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)

3. **Wait** for acknowledgment within 24-48 hours
4. **Allow** time for a fix before public disclosure (typically 30-90 days)

We take all security reports seriously and appreciate responsible disclosure.

## Supported Versions

| Version | Supported | Status |
|---------|-----------|--------|
| 1.0.x   | ✅ Yes    | Latest (Current) |
| < 1.0   | ❌ No     | Pre-release |

## Security Best Practices

When using IntelSource:

### ✅ DO:
- ✅ Only analyze targets you own or have permission to test
- ✅ Store `.env` files securely (never commit API keys)
- ✅ Review logs in `logs/intelsource.log` for unauthorized activity
- ✅ Update to the latest version regularly
- ✅ Report security issues privately

### ❌ DON'T:
- ❌ Use for unauthorized reconnaissance
- ❌ Commit `.env` files with credentials to git
- ❌ Share API keys or sensitive data
- ❌ Use on systems without permission
- ❌ Disclose vulnerabilities publicly before a fix is available

## Known Limitations

- DNS queries respect rate limiting but may timeout on slow networks
- WHOIS data depends on registrar responsiveness
- GeoIP accuracy depends on ipinfo.io database accuracy
- Bulk processing is sequential (not parallelized yet)

## Vulnerability Disclosure Timeline

1. **Report Received** → Initial response within 24 hours
2. **Assessment** → Severity and scope determined within 1 week
3. **Fix Development** → Patch created and tested
4. **Review** → Internal security review
5. **Release** → Public fix released with CVE if applicable
6. **Disclosure** → Full details published after fix is available

## Dependencies Security

IntelSource depends on these external libraries:
- `dnspython` - DNS queries
- `whois` - WHOIS lookups
- `requests` - HTTP requests
- `colorama` / `rich` - Terminal output
- `python-dotenv` - Environment loading
- `geoip2` / `maxminddb` - Geolocation

All dependencies are regularly updated. Check `requirements.txt` for current versions.

To scan dependencies for known vulnerabilities:
```bash
pip install safety
safety check -r requirements.txt
```

## Security-Related Links

- [OWASP Security Guidelines](https://owasp.org/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

---

**Thank you for helping keep IntelSource secure!** 🛡️
