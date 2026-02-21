const API_KEY = "your_api_key";

const response = await fetch(
  `https://api.revealera.com/accounts/tech.json?vendor_name=Hubspot%20Marketing%20Hub&api_key=${API_KEY}`
);

const data = await response.json();
data.users.forEach(company => {
  console.log(`${company.company_name} (${company.domain}) - ${company.company_size_range} employees`);
});
