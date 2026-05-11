# IntelSource 🎯

> **A unified, multi-source OSINT reconnaissance tool designed for security researchers and intelligence analysts.**

Consolidate IP, domain, and email intelligence from multiple public sources into clean, actionable JSON output—all from an elegant, interactive CLI interface.

---

## ✨ Features

### 🔍 Intelligence Gathering
- **IP Address Reconnaissance** - GeoIP lookup, ASN data, reverse DNS, ISP information
- **Domain Analysis** - WHOIS registration data, comprehensive DNS enumeration
- **Email Validation** - MX record verification, deliverability checking
- **Full Reconnaissance Mode** - Complete intel gathering in a single command
- **Bulk Processing** - Analyze multiple targets from file with automatic results aggregation

### 📊 Data Sources
| Source | Data Type | Coverage |
|--------|-----------|----------|
| **WHOIS** | Registration, ownership, expiration dates | Domains & IPs |
| **DNS** | A, AAAA, MX, NS, TXT, CNAME, SOA records | Domains |
| **GeoIP (ipinfo.io)** | Location, country, city, timezone, ISP, ASN | IPs |
| **Reverse DNS** | Hostname resolution | IPs |
| **MX Records** | Mail server validation | Domains & Emails |

### 🎨 User Experience
- **Rich Terminal UI** - Beautiful colored menus, panels, and formatting
- **Syntax Highlighting** - JSON output with professional monokai theme
- **Smart Screen Management** - Automatic clearing for clean, distraction-free navigation
- **Real-time Status** - Animated loading indicators during queries
- **Professional Output** - Timestamped JSON files saved automatically

### ⚙️ Configuration
- **Environment Variables** - `.env` support for API tokens and settings
- **ipinfo.io Integration** - Free tier: 50k requests/month (optional paid plans available)
- **Customizable Timeouts** - DNS and WHOIS query timeout settings
- **No Authentication Required** - All core features work without API keys

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/osint-intell/IntelSource.git
cd IntelSource
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up environment (optional but recommended):**
```bash
# Copy the example configuration
cp .env.example .env

# Add your ipinfo.io API token (get free one at https://ipinfo.io)
# Edit .env and set: IPINFO_TOKEN=your_token_here
```

**4. Launch IntelSource:**
```bash
python3 main.py
```

---

## 📖 Usage Guide

### Main Menu Interface

When you launch IntelSource, you'll see this beautiful interactive menu:

```
╔═══════════════════════════════════════════════════════════════════╗
║            IntelSource - Unified OSINT Aggregator                ║
║  Multi-source IP, Domain & Email reconnaissance tool             ║
║  Fast • Accurate • Comprehensive                                 ║
╚═══════════════════════════════════════════════════════════════════╝

IntelSource - Main Menu

1  IP Address Lookup      WHOIS, DNS, GeoIP, ASN information
2  Domain Lookup          WHOIS, DNS enumeration, MX records
3  Email Validation       MX record validation & deliverability
4  Full Reconnaissance    Complete intel gathering for target
5  Bulk Import            Process multiple targets from file
6  Exit                   Quit IntelSource

➜ Enter your choice:
```

**Screen Flow:**
- ✅ Launches with cleared screen → fresh banner
- ✅ Each menu selection clears screen → dedicated interface
- ✅ Results displayed with syntax highlighting
- ✅ Press Enter to return → auto-clears and redisplays menu
- ✅ Clean, distraction-free workflow

---

## 💡 Examples

### Example 1: IP Address Intelligence

```bash
$ python3 main.py
➜ Enter your choice: 1
```

**Input:** `8.8.8.8` (Google DNS)

**Output:**
```json
{
  "target": "8.8.8.8",
  "type": "ip",
  "geoip": {
    "city": "Los Angeles",
    "country": "United States",
    "timezone": "America/Los_Angeles",
    "isp": "AS15169 Google LLC",
    "asn": "AS15169"
  },
  "reverse_dns": {
    "hostnames": ["dns.google"],
    "status": "success"
  }
}
```

✅ Results saved to: `results/8.8.8.8_20260510_112345.json`

---

### Example 2: Domain Reconnaissance

```bash
$ python3 main.py
➜ Enter your choice: 2
```

**Input:** `github.com`

**Output:**
```json
{
  "target": "github.com",
  "type": "domain",
  "whois": {
    "registrar": "GitHub, Inc.",
    "creation_date": "2007-10-29",
    "name_servers": ["ns1.github.com", "ns2.github.com"],
    "status": "success"
  },
  "dns": {
    "records": {
      "A": ["140.82.113.4"],
      "MX": ["aspmx.l.google.com"],
      "NS": ["ns1.github.com", "ns2.github.com"],
      "TXT": ["v=spf1 include:sendgrid.net ~all"]
    }
  }
}
```

✅ Results saved automatically with timestamp

---

### Example 3: Email Validation

```bash
$ python3 main.py
➜ Enter your choice: 3
```

**Input:** `contact@example.com`

**Output:**
```json
{
  "email": "contact@example.com",
  "domain": "example.com",
  "mx_records": [
    {"priority": 10, "exchange": "mail.example.com"}
  ],
  "status": "valid"
}
```

✅ Verifies domain has active MX records

---

### Example 4: Bulk Import

**Create `targets.txt`:**
```
8.8.8.8
1.1.1.1
google.com
admin@example.com
```

**Run bulk import:**
```bash
$ python3 main.py
➜ Enter your choice: 5
➜ Enter file path: targets.txt
⟳ Processing 4 targets...
✓ Processed 4/4 targets
```

**Output:** Single JSON with all results
```json
{
  "bulk_results": [
    { "target": "8.8.8.8", ... },
    { "target": "1.1.1.1", ... },
    { "target": "google.com", ... },
    { "target": "admin@example.com", ... }
  ],
  "total": 4,
  "processed": 4
}
```

---

## 🔧 Configuration

### Environment Variables

Edit `.env` to customize behavior:

```bash
# ipinfo.io API Token
# Get free token: https://ipinfo.io (50k requests/month)
IPINFO_TOKEN=your_token_here

# DNS Query Settings
DNS_TIMEOUT=5              # Seconds to wait for DNS response
DNS_RETRIES=2              # Number of retry attempts

# WHOIS Query Settings
WHOIS_TIMEOUT=10           # Seconds to wait for WHOIS response

# Future API Integrations
SHODAN_API_KEY=            # For port/service scanning (coming soon)
CENSYS_API_ID=             # For historical data (coming soon)
CENSYS_API_SECRET=         # For historical data (coming soon)

# Output Formatting
COLORIZE_OUTPUT=true       # Use colored terminal output
```

### File Structure

```
IntelSource/
├── main.py                 # Entry point with Rich UI
├── .env                    # Your local configuration (create from .env.example)
├── .env.example            # Configuration template
├── requirements.txt        # Python dependencies
├── config/
│   └── config.json         # Default settings
├── collectors/             # Data gathering modules
│   ├── whois_collector.py
│   ├── dns_collector.py
│   ├── geoip_collector.py
│   └── email_validator.py
├── utils/                  # Utility functions
│   ├── validators.py       # Input validation
│   ├── output.py           # Formatting & display
│   └── logger.py           # Logging configuration
├── results/                # Output directory (auto-created)
│   └── *.json              # Timestamped result files
├── logs/                   # Log directory (auto-created)
│   └── intelsource.log     # Application logs
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

---

## 📊 Output Format

All results are saved as **timestamped JSON files** for easy integration with other tools:

```
results/
├── 8.8.8.8_20260510_112345.json
├── github.com_20260510_112346.json
├── contact@example.com_20260510_112347.json
└── Bulk_Import_20260510_112348.json
```

**Benefits:**
- ✅ Machine-readable format for automation
- ✅ Timestamped for tracking
- ✅ Easily parseable by scripts
- ✅ Compatible with JSON processing tools (jq, etc.)

---

## 📝 Logging & Diagnostics

All queries and errors are logged to `logs/intelsource.log`:

```
2026-05-10 11:23:45 - collectors.geoip_collector - INFO - Performing GeoIP lookup for 8.8.8.8
2026-05-10 11:23:46 - collectors.geoip_collector - INFO - GeoIP lookup successful for 8.8.8.8
2026-05-10 11:23:47 - collectors.dns_collector - INFO - Performing reverse DNS lookup for 8.8.8.8
2026-05-10 11:23:48 - collectors.dns_collector - INFO - Reverse DNS lookup successful for 8.8.8.8
2026-05-10 11:23:49 - main - INFO - Results saved to: results/8.8.8.8_20260510_112345.json
```

**View logs:**
```bash
tail -f logs/intelsource.log      # Follow logs in real-time
cat logs/intelsource.log          # View full log
grep "ERROR" logs/intelsource.log # Find errors only
```

---

## 🛡️ Security & Responsible Use

⚠️ **Important Reminders:**

### Authorization
- ✅ Only gather intelligence on systems **you own or have permission to test**
- ✅ **Never** use this tool for unauthorized scanning or reconnaissance
- ✅ Understand local laws regarding OSINT activities in your jurisdiction

### Rate Limiting
- ✅ DNS queries include automatic rate limiting to avoid blocking
- ✅ ipinfo.io free tier: 50k requests/month
- ✅ Respect API rate limits to avoid temporary bans

### Data Privacy
- ✅ Results are stored locally in `results/` directory
- ✅ Logs contain all query history in `logs/intelsource.log`
- ✅ No data is sent to external servers (except API providers)
- ✅ `.env` file is ignored by git (never commit API keys)

### Best Practices
1. **Verify authority** before analyzing any target
2. **Respect rate limits** on DNS and API queries
3. **Follow local laws** regarding security research
4. **Use responsibly** - this is a tool for authorized work only
5. **Document your actions** - maintain audit trails for compliance

---

## 🗺️ Roadmap

### Current Version (v1.0)
- ✅ IP reconnaissance (GeoIP, ASN, reverse DNS)
- ✅ Domain analysis (WHOIS, DNS enumeration)
- ✅ Email validation (MX records)
- ✅ Bulk processing
- ✅ Rich CLI interface
- ✅ JSON export

### Planned Features (v1.1+)
- 🔲 Shodan integration for open port discovery
- 🔲 Censys historical data lookups
- 🔲 SSL certificate enumeration
- 🔲 Web scraping & title grabbing
- 🔲 Service version detection
- 🔲 CVE correlation

### Future Enhancements
- 🔲 Database storage for historical tracking
- 🔲 REST API server for programmatic access
- 🔲 Web UI dashboard
- 🔲 Advanced filtering & pivoting
- 🔲 Report generation (HTML, PDF)
- 🔲 Integration with SIEM platforms

---

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, feature requests, or improvements—your help makes IntelSource better.

### Getting Started
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes with clear commits
4. **Test** thoroughly before submitting
5. **Open** a Pull Request with a detailed description

### Code Standards
- ✅ Use Python 3.7+ features
- ✅ Include type hints where helpful
- ✅ Write docstrings for all functions/classes
- ✅ Follow PEP 8 style guide
- ✅ Test your changes before submitting
- ✅ Update README if adding features

### Areas for Contribution
- New data collectors (Shodan, Censys, etc.)
- Improved error handling
- Additional output formats (CSV, HTML)
- Performance optimizations
- Documentation improvements
- Bug fixes & edge cases

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### MIT License Summary
- ✅ Free to use for commercial and personal projects
- ✅ Modify and distribute freely
- ✅ No warranty provided
- ✅ Include license copy in derivatives

---

## 📞 Support & Feedback

### Getting Help
- 📖 **Documentation** - Check this README first
- 🐛 **Issues** - Open a GitHub issue for bugs
- 💡 **Features** - Suggest improvements via GitHub discussions
- 🔒 **Security** - Report vulnerabilities responsibly

### Common Issues

**Q: "No module named 'whois'" error**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Q: ".env file not found" warning**
```bash
# Solution: Create .env from template
cp .env.example .env
```

**Q: Rate limit errors from ipinfo.io**
```bash
# Solution: Add API token to .env (free 50k/month)
# Or upgrade to paid plan at https://ipinfo.io
```

**Q: DNS queries timing out**
```bash
# Solution: Increase DNS_TIMEOUT in .env
DNS_TIMEOUT=10
```

---

## 📚 Resources

### OSINT Tools & References
- [ipinfo.io](https://ipinfo.io) - IP geolocation and ASN data
- [crt.sh](https://crt.sh) - Certificate transparency logs
- [WHOIS Lookup](https://www.whois.com/) - Domain registration data
- [DNSdumpster](https://dnsdumpster.com/) - DNS reconnaissance

### Security Research
- [OWASP](https://owasp.org/) - Web security standards
- [MITRE ATT&CK](https://attack.mitre.org/) - Adversary tactics & techniques
- [NIST Cybersecurity](https://www.nist.gov/cyberframework) - Security standards

### Related Projects
- [theHarvester](https://github.com/laramies/theHarvester) - Email discovery
- [Shodan CLI](https://cli.shodan.io/) - Port scanning
- [amass](https://github.com/OWASP/amass) - Subdomain enumeration

---

## 🎯 Use Cases

### Penetration Testing
- Gather intelligence before engagement
- Map target infrastructure
- Identify related domains and IPs

### Bug Bounty Hunting
- Reconnaissance phase
- Scope verification
- Target expansion

### Security Research
- Threat intelligence gathering
- Infrastructure analysis
- Vulnerability discovery

### OSINT Investigations
- Digital forensics
- Person/organization research
- Threat monitoring

---

## 👨‍💻 About

**IntelSource** is maintained by the **OSINT Intelligence** community as part of the initiative to provide open-source security tools.

- 🌐 Website: [osintintelligence.xyz](https://osintintelligence.xyz)
- 📊 GitHub Org: [osint-intell](https://github.com/osint-intell)
- 📧 Contact: [Open an issue](https://github.com/OsintIntelligence/IntelSource/issues)

---

## 📊 Statistics

- ✅ **4 Data Collectors** - WHOIS, DNS, GeoIP, Email validation
- ✅ **6 Menu Options** - Multiple reconnaissance modes
- ✅ **Supports 3 Target Types** - IPs, domains, emails
- ✅ **Automated Output** - Timestamped JSON results
- ✅ **Full Logging** - Audit trail & diagnostics
- ✅ **Production Ready** - Battle-tested code

---

## 📈 Performance

| Operation | Time | Source |
|-----------|------|--------|
| IP Lookup | ~1-2s | ipinfo.io API |
| Domain WHOIS | ~3-5s | WHOIS servers |
| DNS Enumeration | ~2-3s | Public DNS |
| Email Validation | ~1-2s | DNS MX lookup |
| Bulk (10 targets) | ~20-30s | Concurrent queries |

*Times vary based on network conditions and target availability*

---

## 🎉 Changelog

### v1.0.0 (2026-05-10)
- 🎯 Initial release
- ✅ IP reconnaissance
- ✅ Domain analysis
- ✅ Email validation
- ✅ Rich CLI UI
- ✅ Bulk processing
- ✅ JSON export

---

**Last Updated:** 2026-05-10  
**Version:** 1.0.0  
**Status:** Production Ready ✅

---

**Happy hunting! 🎯**
