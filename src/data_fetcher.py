import pandas as pd
import requests
import io
import os

class OECDDataFetcher:
    def __init__(self):
        # Older, but reliable OECD API
        self.base_url = "https://stats.oecd.org/SDMX-JSON/data"

    def fetch_south_korea_data(self):
        """
        Fetches South Korea (KOR) data from OECD for:
        - Inflation (CPI)
        - GDP Growth
        - Unemployment Rate
        """
        print("Fetching South Korea macroeconomic data from OECD...")
        
        # Dataset, Key, Frequency
        # PRINTO01: CPI, VIXOBSA: GDP Growth, LRHUTTTT: Unemployment
        indicators = {
            'CPI': ('MEI', 'KOR.PRINTO01.M'), 
            'GDP_Growth': ('MEI', 'KOR.VIXOBSA.Q'),
            'Unemployment': ('MEI', 'KOR.LRHUTTTT.M')
        }
        
        results = {}
        
        for name, (dataset, key) in indicators.items():
            print(f"Fetching {name}...")
            try:
                # Using the older SDMX-JSON data explorer's CSV output
                url = f"{self.base_url}/{dataset}/{key}/all?startTime=2015&contentType=csv"
                response = requests.get(url)
                if response.status_code == 200:
                    df = pd.read_csv(io.StringIO(response.text))
                    results[name] = df
                    df.to_csv(f"data/{name.lower()}_kor.csv", index=False)
                else:
                    print(f"Failed to fetch {name}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching {name}: {e}")
        
        return results

if __name__ == "__main__":
    fetcher = OECDDataFetcher()
    data = fetcher.fetch_south_korea_data()
    if data:
        for name, df in data.items():
            print(f"\n{name} Data (first 2 rows):")
            print(df.head(2))
