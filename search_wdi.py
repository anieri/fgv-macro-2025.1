import requests
import json

def search_wdi(query):
    url = f"https://api.worldbank.org/v2/indicator?format=json&per_page=2000&source=2"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        indicators = data[1]
        results = []
        for ind in indicators:
            if query.lower() in ind['name'].lower():
                results.append({'id': ind['id'], 'name': ind['name']})
        return results
    return []

# Queries to search for
queries = ["consumption", "investment", "government spending", "export", "import", "agriculture", "industry", "service", "health expenditure", "pharmaceutical", "retail"]

for q in queries:
    print(f"\n--- Results for {q} ---")
    res = search_wdi(q)
    for r in res[:10]: # Limit to first 10 for each
        print(f"{r['id']}: {r['name']}")

