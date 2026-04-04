import requests
import pandas as pd

def check_kor_wdi(indicators):
    results = []
    for code in indicators:
        url = f"https://api.worldbank.org/v2/country/KOR/indicator/{code}?format=json&per_page=1000"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data) > 1 and data[1]:
                # Find first non-null date
                df = pd.DataFrame(data[1])
                df = df.dropna(subset=['value'])
                if not df.empty:
                    first_date = df['date'].min()
                    last_date = df['date'].max()
                    results.append({'Code': code, 'Start Date': first_date, 'End Date': last_date, 'Frequency': 'Annual'})
                else:
                    results.append({'Code': code, 'Start Date': 'N/A', 'End Date': 'N/A', 'Frequency': 'N/A'})
            else:
                results.append({'Code': code, 'Start Date': 'N/A', 'End Date': 'N/A', 'Frequency': 'N/A'})
        else:
            results.append({'Code': code, 'Start Date': 'N/A', 'End Date': 'N/A', 'Frequency': f'Error: {response.status_code}'})
    return pd.DataFrame(results)

indicators = [
    'NE.CON.PRVT.KD', 'NE.CON.GOVT.KD', 'NE.GDI.FTOT.KD', 'NE.EXP.GNFS.KD', 'NE.IMP.GNFS.KD', # GDP
    'NV.AGR.TOTL.KD', 'NV.IND.TOTL.KD', 'NV.SRV.TOTL.KD', # Sectoral
    'SH.XPD.GHED.GD.ZS', 'SH.XPD.PVTD.GD.ZS', # Health
]

df = check_kor_wdi(indicators)
print(df)
