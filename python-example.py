import requests

API_KEY = "your_api_key"

response = requests.get(
    "https://api.revealera.com/accounts/tech.json",
    params={"vendor_name": "Hubspot Marketing Hub", "api_key": API_KEY}
)

for company in response.json()["users"]:
    print(f"{company['company_name']} ({company['domain']}) - {company['company_size_range']} employees")
