import requests
import pandas as pd

code = 'SH.XPD.PVTD.CH.ZS' # Domestic private health expenditure (% of current health expenditure)
url = f"https://api.worldbank.org/v2/country/KOR/indicator/{code}?format=json&per_page=1000"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    if len(data) > 1 and data[1]:
        df = pd.DataFrame(data[1])
        df = df.dropna(subset=['value'])
        if not df.empty:
            print(f"{code}: {df['date'].min()} to {df['date'].max()}")
        else:
            print(f"{code}: No data")
    else:
        print(f"{code}: No data")
else:
    print(f"{code}: Error {response.status_code}")
