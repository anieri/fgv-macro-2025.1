import requests
import pandas as pd

indicators = [
    'SH.XPD.CHEX.GD.ZS', # Total Current Health Expenditure (% of GDP)
    'SH.XPD.GHED.GD.ZS', # General Government Health Expenditure (% of GDP)
    'SH.XPD.PVTD.GD.ZS', # Private Health Expenditure (% of GDP)
    'SH.XPD.CHEX.PC.CD', # Total Health Expenditure per capita
]

results = []
for code in indicators:
    url = f"https://api.worldbank.org/v2/country/KOR/indicator/{code}?format=json&per_page=1000"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1 and data[1]:
            df = pd.DataFrame(data[1])
            df = df.dropna(subset=['value'])
            if not df.empty:
                results.append({'Code': code, 'Start': df['date'].min(), 'End': df['date'].max()})
print(pd.DataFrame(results))
