import pandas as pd
import pandas_datareader.data as web
import datetime
import os

def fetch_kor_monthly_data():
    """
    Fetches monthly macroeconomic data for South Korea from FRED.
    """
    start = datetime.datetime(1960, 1, 1)
    end = datetime.datetime(2024, 12, 31)
    
    # Updated dictionary of FRED codes for South Korea
    indicators = {
        'CPI_YoY': 'CPALTT01KRM659N',       # CPI YoY Growth
        'Ind_Prod': 'KORPROINDMISMEI',      # Industrial Production Index (Monthly, starts 1990)
        'Exchange_Rate': 'EXKOUS',          # Exchange Rate (Monthly, starts 1981)
        'M2': 'MYAGM2KRM189N',              # M2 Money Supply (Monthly, starts 1960)
        'Bond_Yield_10Y': 'IRLTLT01KRM156N',# 10Y Bond Yield (Monthly, starts 2000)
        'REER': 'RBKRBIS',                  # Real Effective Exchange Rate (BIS, starts 1994)
        'Unemployment': 'LRHUTTTTKRM156S',  # Unemployment Rate (OECD, starts 1990)
        'Exports': 'XTEXVA01KRM667S',       # Exports Value (Monthly, starts 1960)
        'Imports': 'XTIMVA01KRM667S',       # Imports Value (Monthly, starts 1960)
        'Real_GDP_Q': 'NGDPRSAXDCKRQ'       # Real GDP (Quarterly, starts 1960) - crucial for 1970s
    }
    
    print(f"Fetching data from FRED for South Korea ({start.year}-{end.year})...")
    
    df_list = []
    for name, code in indicators.items():
        try:
            print(f"Fetching {name} ({code})...")
            data = web.DataReader(code, 'fred', start, end)
            data.columns = [name]
            df_list.append(data)
        except Exception as e:
            print(f"Error fetching {name}: {e}")
            
    if not df_list:
        print("No data fetched.")
        return None
        
    # Merge all dataframes on the index (Date)
    final_df = pd.concat(df_list, axis=1)
    
    # Save to CSV
    os.makedirs('data', exist_ok=True)
    file_path = 'data/kor_monthly_macro.csv'
    final_df.to_csv(file_path)
    print(f"Successfully saved data to {file_path}")
    
    return final_df

if __name__ == "__main__":
    df = fetch_kor_monthly_data()
    if df is not None:
        print("\nData Overview:")
        print(df.describe())
        print("\nMissing values per column:")
        print(df.isnull().sum())
        print("\nFirst available date per column:")
        for col in df.columns:
            first_date = df[col].first_valid_index()
            print(f"{col}: {first_date}")
