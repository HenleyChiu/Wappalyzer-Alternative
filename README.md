# Wappalyzer Alternative API

Detect B2B tech stacks via API — including backend tools like Okta, Salesforce, Workday, and ChatGPT that Wappalyzer and BuiltWith can't see.

## Why Bloomberry?

|  | Wappalyzer | BuiltWith | Bloomberry |
|---|---|---|---|
| Frontend tech (React, GTM, analytics) | ✅ | ✅ | ✅ |
| Backend tech (Okta, Workday, Salesforce) | ❌ | ❌ | ✅ |
| Enterprise AI (ChatGPT, Claude, Perplexity) | ❌ | ❌ | ✅ |
| Real-time adoption signals | ❌ | ❌ | ✅ |
| Churn detection | ❌ | ❌ | ✅ |
| Products tracked | ~1,500 | ~50,000+ | 1,200+ B2B products |

Wappalyzer and BuiltWith detect frontend scripts on websites. Bloomberry detects **backend and enterprise software** that leaves no website footprint — HR systems, security tools, CRMs, DevOps, and AI platforms.

## How It Works

We monitor multiple data streams: DNS record changes, certificate transparency logs, subprocessor list updates, subdomain patterns (like `okta.company.com`), and infrastructure signals. No scraping job postings or relying on self-reported data.

Signals appear within **3 days** of adoption. Churn signals within **1-2 weeks**.

## Quick Start

### Get companies using a specific product
```bash
curl "https://api.revealera.com/accounts/tech.json?vendor=okta" \
  -H "x-api-key: YOUR_API_KEY"
```

**Response:**
```json
{
  "results": [
    {
      "domain": "stripe.com",
      "company_name": "Stripe",
      "vendor": "Okta",
      "category": "Identity and Access Management",
      "status": "active",
      "first_detected": "2023-04-12",
      "employees": "5001-10000",
      "industry": "Financial Services"
    }
  ]
}
```

### Get recent tech stack changes (adoptions & churns)
```bash
curl "https://api.revealera.com/signals/tech.json?vendor=salesforce&signal_type=churn" \
  -H "x-api-key: YOUR_API_KEY"
```

**Response:**
```json
{
  "results": [
    {
      "domain": "acme.com",
      "company_name": "Acme Corp",
      "vendor": "Salesforce",
      "signal_type": "churn",
      "detected_date": "2025-02-15",
      "employees": "201-500",
      "industry": "Software Development"
    }
  ]
}
```

### Get all vendors in a category
```bash
curl "https://api.revealera.com/vendors/all_vendors.json?category=CRM" \
  -H "x-api-key: YOUR_API_KEY"
```

## Use Cases

| Use Case | How |
|----------|-----|
| **Find competitor customers** | Query companies using a rival product |
| **Detect churn signals** | Get alerts when targets drop a vendor |
| **Enrich CRM leads** | Add tech stack data to existing accounts |
| **Build prospecting lists** | Find companies that recently adopted tools in your category |
| **Trigger outbound campaigns** | Target companies that just churned from a competitor |

## Coverage

- **1,200+ B2B products** across 175 categories
- **Fortune 500 to SMBs** (5+ employees)
- **Global coverage** — US, EU, APAC, and more
- **Categories:** CRM, Security, HR/HCM, DevOps, Sales Intelligence, Enterprise AI, and [170+ more](https://api.bloomberry.com/categories.txt)

## Code Examples

- [Python](/examples/python.py)
- [Node.js](/examples/node.js)
- [cURL](/examples/curl.sh)

## Get Your Free API Key

→ **[bloomberry.com/signup](https://bloomberry.com/signup.html)** — 200 free credits to test

## Full Documentation

→ **[docs.bloomberry.com](https://docs.bloomberry.com)**

## Sample Data

Want to see real output before signing up? Check [`/sample-data`](/sample-data) for example API responses.

---

Built by [Revealera](https://revealera.com) — providing tech adoption data to hedge funds since 2020.
