import requests

API_KEY = "your_api_key"
BASE_URL = "https://api.revealera.com"

# Get companies using Okta
response = requests.get(
    f"{BASE_URL}/accounts/tech.json",
    params={"vendor": "Okta"},
    headers={"x-api-key": API_KEY}
)

for company in response.json()["results"]:
    print(f"{company['company_name']} ({company['domain']})")
