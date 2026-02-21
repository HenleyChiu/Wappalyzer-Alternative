# Wappalyzer Alternative - Bloomberry

Detect B2B tech stacks via API — including backend tools like Okta, Salesforce, Workday, and ChatGPT that Wappalyzer and BuiltWith can't see.

## Why Bloomberry?

|  | Wappalyzer | BuiltWith | Bloomberry |
|---|---|---|---|
| Frontend tech (React, GTM, analytics) | ✅ | ✅ | ✅ |
| Backend tech (Okta, Workday, Salesforce, Hubspot) | ❌ | ❌ | ✅ |
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
curl "https://api.revealera.com/accounts/tech.json?vendor_name=Hubspot%20Marketing%20Hub&api_key=YOUR_API_KEY"
```

**Response:**
```json
{
  "users": [
    {
      "id": "1217675115",
      "domain": "nextsecurities.com",
      "company_name": "Next Securities",
      "company_logo": "https://media.licdn.com/dms/image/...",
      "industry": "Financial Services",
      "company_size_range": "51–200",
      "country": "KR",
      "region": "Asia",
      "vendor_name": "Hubspot Marketing Hub",
      "vendor_category": "advanced marketing automation",
      "usage_started_at": "2026-02-21"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total_pages": 524,
    "total_items": 10462,
    "next_token": "eyJzb3J0IjpbMTc3MDcxMDM4NCwiMTQ5MDAwMjg1Il0sInBhZ2UiOjJ9"
  }
}
```

### Get recent tech stack changes (adoptions & churns)
```bash
curl "https://api.revealera.com/signals/tech.json?vendor_name=Hubspot%20Marketing%20Hub&api_key=YOUR_API_KEY"
```

**Response:**
```json
{
  "signals": [
    {
      "id": "7531436",
      "change_date": "2026-02-21T08:34:19-05:00",
      "change_type": "unsubscribed",
      "change_description": "unsubscribed from Hubspot Marketing Hub",
      "domain": "g6hospitality.com",
      "company_name": "G6 Hospitality LLC",
      "company_logo": "https://media.licdn.com/dms/image/...",
      "industry": "Hospitality",
      "company_size_range": "201–500",
      "country": "US",
      "region": "North America",
      "vendor_name": "Hubspot Marketing Hub",
      "vendor_category": "advanced marketing automation"
    },
    {
      "id": "7530701",
      "change_date": "2026-02-21T06:51:47-05:00",
      "change_type": "subscribed",
      "change_description": "subscribed to Hubspot Marketing Hub",
      "domain": "lumalabs.ai",
      "company_name": "Luma AI",
      "industry": "Software Development",
      "company_size_range": "51–200",
      "country": "US",
      "region": "North America",
      "vendor_name": "Hubspot Marketing Hub",
      "vendor_category": "advanced marketing automation"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total_pages": 97,
    "total_items": 1938,
    "next_token": "eyJzb3J0IjpbMTc3MTM1MzY3OSwiNzQ3MzczOCJdLCJwYWdlIjoyfQ=="
  }
}
```

### Get all vendors in a category
```bash
curl "https://api.revealera.com/vendors/all_vendors.json?category=CRM&api_key=YOUR_API_KEY"
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

- [Python](python-example.py)
- [Node.js](node-example.js)
- [cURL](curl-example.sh)

## Get Your Free API Key

→ **[bloomberry.com/signup](https://bloomberry.com/signup.html)** — 200 free credits to test

## Full Documentation

→ **[docs.bloomberry.com](https://docs.bloomberry.com)**

---

Built by [Revealera](https://revealera.com) — providing tech adoption data to hedge funds since 2020.
