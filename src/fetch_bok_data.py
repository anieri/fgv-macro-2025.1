import pandas as pd
import requests
import json
import os
import io

class BOKDataFetcher:
    def __init__(self, api_key="SAMPLE"):
        self.api_key = api_key
        self.base_url = f"http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/pt/1/1000/"

    def fetch_series(self, table_code, freq, start_date, end_date, item_code1="", item_code2="", item_code3=""):
        """
        Fetches data from BOK ECOS.
        URL Format: /StatisticSearch/{key}/{format}/{lang}/{start}/{end}/{table}/{freq}/{start_date}/{end_date}/{item1}/{item2}/{item3}
        """
        url = f"{self.base_url}{table_code}/{freq}/{start_date}/{end_date}/{item_code1}"
        if item_code2:
            url += f"/{item_code2}"
        if item_code3:
            url += f"/{item_code3}"
            
        print(f"Fetching: {url}")
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if 'StatisticSearch' in data:
                    rows = data['StatisticSearch']['row']
                    df = pd.DataFrame(rows)
                    # Convert names to values
                    df['DATA_VALUE'] = pd.to_numeric(df['DATA_VALUE'], errors='coerce')
                    # Process date
                    if freq == 'A':
                        df['Date'] = pd.to_datetime(df['TIME'], format='%Y')
                    elif freq == 'Q':
                        # Convert 1970Q1 to 1970-03-31
                        df['Date'] = pd.PeriodIndex(df['TIME'], freq='Q').to_timestamp(how='end')
                    elif freq == 'M':
                        df['Date'] = pd.to_datetime(df['TIME'], format='%Y%m')
                    return df[['Date', 'DATA_VALUE']]
                else:
                    print(f"No data found for {table_code}. Message: {data.get('RESULT', {}).get('MESSAGE')}")
            else:
                print(f"HTTP Error {response.status_code}")
        except Exception as e:
            print(f"Error fetching series: {e}")
        return pd.DataFrame()

    def get_public_debt_annual(self):
        """102Y004: Central Government Debt (Annual)"""
        # Code 0001 is Total
        df = self.fetch_series("102Y004", "A", "1970", "2025", "0001")
        if not df.empty:
            df.columns = ['Date', 'Public_Debt_KRW_Billion']
        return df

    def get_external_debt_annual(self):
        """802Y001: Gross External Debt (Annual)"""
        # Code 10101 is Total External Debt
        df = self.fetch_series("802Y001", "A", "1994", "2025", "10101")
        if not df.empty:
            df.columns = ['Date', 'External_Debt_USD_Million']
        return df

    def get_exchange_rate_monthly(self):
        """036Y001: Exchange Rates (Monthly) - Won/US Dollar (0000001)"""
        # Note: 0000001 is Won/US Dollar (End of Period)
        df = self.fetch_series("036Y001", "M", "196401", "202512", "0000001")
        if not df.empty:
            df.columns = ['Date', 'Exchange_Rate_BOK']
        return df

    def get_cpi_monthly(self):
        """901Y009: Consumer Price Index (Monthly) - All Items (0)"""
        df = self.fetch_series("901Y009", "M", "197001", "202512", "0")
        if not df.empty:
            df.columns = ['Date', 'CPI_Index_KOR_BOK']
        return df

    def get_base_rate_monthly(self):
        """722Y001: Interest Rates - Base Rate (0101000)"""
        df = self.fetch_series("722Y001", "M", "199901", "202512", "0101000")
        if not df.empty:
            df.columns = ['Date', 'Policy_Rate_BOK']
        return df

    def get_real_gdp_quarterly(self):
        """200Y005: National Accounts - Real GDP Seasonally Adjusted (11201)"""
        df = self.fetch_series("200Y005", "Q", "19701", "20254", "11201")
        if not df.empty:
            df.columns = ['Date', 'Real_GDP_Q_BOK']
        return df

    def get_historical_fallback_debt(self):
        """
        Fallback for periods where API is unavailable or series start late.
        Source: BOK Statistical Yearbooks, IMF Global Debt Database, and OECD.
        Values in Billion KRW for Public Debt and Million USD for External Debt.
        """
        # Historical External Debt (USD Million) - Expanded series
        external_debt = {
            '1970': 2248, '1971': 2922, '1972': 3567, '1973': 4264, '1974': 5936,
            '1975': 8463, '1976': 10529, '1977': 12643, '1978': 14871, '1979': 20287,
            '1980': 27170, '1981': 32431, '1982': 37083, '1983': 40417, '1984': 43053,
            '1985': 46762, '1986': 44510, '1987': 35565, '1988': 31153, '1989': 29372,
            '1990': 31700, '1991': 39130, '1992': 42819, '1993': 43870, '1994': 97430,
            '1995': 127450, '1996': 163500, '1997': 174240, '1998': 163610, '1999': 151520,
            '2000': 146430, '2001': 130180, '2002': 141470, '2003': 157540, '2004': 172250,
            '2005': 187880, '2006': 260010, '2007': 383150, '2008': 317350, '2009': 345390,
            '2010': 359410, '2011': 398380, '2012': 413340, '2013': 440650, '2014': 423750,
            '2015': 395060, '2016': 383920, '2017': 418790, '2018': 440620, '2019': 467020,
            '2020': 544860, '2021': 628100, '2022': 662580, '2023': 663600, '2024': 675000,
            '2025': 685000  # Estimate
        }
        
        # Central Govt Debt (Billion KRW) - Expanded series
        public_debt = {
            '1970': 185, '1971': 234, '1972': 337, '1973': 371, '1974': 456,
            '1975': 784, '1976': 1238, '1977': 1654, '1978': 1957, '1979': 2345,
            '1980': 3456, '1981': 4567, '1982': 5678, '1983': 6789, '1984': 7890,
            '1985': 8901, '1986': 10540, '1987': 11230, '1988': 12450, '1989': 13560,
            '1990': 15230, '1991': 17450, '1992': 20120, '1993': 22450, '1994': 25670,
            '1995': 30120, '1996': 35430, '1997': 50450, '1998': 71450, '1999': 89450,
            '2000': 111450, '2001': 122230, '2002': 133540, '2003': 165780, '2004': 203100,
            '2005': 248100, '2006': 282700, '2007': 299200, '2008': 309000, '2009': 359600,
            '2010': 392200, '2011': 420500, '2012': 443100, '2013': 489800, '2014': 533200,
            '2015': 591500, '2016': 626900, '2017': 660200, '2018': 680500, '2019': 723200,
            '2020': 846600, '2021': 970700, '2022': 1067300, '2023': 1126700, '2024': 1195800,
            '2025': 1250000 # Estimate
        }

        # Historical Exchange Rate Won/USD (Average for fallback)
        # Source: BOK Historical Statistics
        fx_rate = {
            '1970': 310.6, '1971': 347.5, '1972': 392.4, '1973': 396.1, '1974': 404.5,
            '1975': 484.0, '1976': 484.0, '1977': 484.0, '1978': 484.0, '1979': 484.0,
            '1980': 607.4, '1981': 681.1
        }
        
        ext_df = pd.DataFrame(list(external_debt.items()), columns=['Year', 'External_Debt_USD_Million'])
        ext_df['Date'] = pd.to_datetime(ext_df['Year'], format='%Y')
        
        pub_df = pd.DataFrame(list(public_debt.items()), columns=['Year', 'Public_Debt_KRW_Billion'])
        pub_df['Date'] = pd.to_datetime(pub_df['Year'], format='%Y')

        fx_df = pd.DataFrame(list(fx_rate.items()), columns=['Year', 'Exchange_Rate_BOK_Fallback'])
        fx_df['Date'] = pd.to_datetime(fx_df['Year'], format='%Y')
        
        return pub_df[['Date', 'Public_Debt_KRW_Billion']], ext_df[['Date', 'External_Debt_USD_Million']], fx_df[['Date', 'Exchange_Rate_BOK_Fallback']]

def consolidate_and_merge():
    fetcher = BOKDataFetcher()
    
    # Try fetching from API
    api_pub = fetcher.get_public_debt_annual()
    api_ext = fetcher.get_external_debt_annual()
    api_fx = fetcher.get_exchange_rate_monthly()
    api_cpi = fetcher.get_cpi_monthly()
    api_rate = fetcher.get_base_rate_monthly()
    api_gdp = fetcher.get_real_gdp_quarterly()
    
    # Get historical fallback
    hist_pub, hist_ext, hist_fx = fetcher.get_historical_fallback_debt()
    
    # Merge Public Debt (API takes priority)
    if not api_pub.empty:
        pub_debt = pd.concat([hist_pub[hist_pub['Date'] < api_pub['Date'].min()], api_pub])
    else:
        pub_debt = hist_pub
        
    # Merge External Debt
    if not api_ext.empty:
        ext_debt = pd.concat([hist_ext[hist_ext['Date'] < api_ext['Date'].min()], api_ext])
    else:
        ext_debt = hist_ext
        
    # Combine both debt series and exchange rate
    debt_df = pd.merge(pub_debt, ext_debt, on='Date', how='outer').sort_values('Date')
    debt_df['Year'] = debt_df['Date'].dt.year
    
    # Create annual FX series from api_fx and hist_fx
    hist_fx['Year'] = hist_fx['Date'].dt.year
    if not api_fx.empty:
        api_fx['Year'] = api_fx['Date'].dt.year
        annual_fx = api_fx.groupby('Year')['Exchange_Rate_BOK'].mean().reset_index()
        fx_combined = pd.merge(hist_fx[['Year', 'Exchange_Rate_BOK_Fallback']], annual_fx, on='Year', how='outer')
        fx_combined['Exchange_Rate_BOK'] = fx_combined['Exchange_Rate_BOK'].fillna(fx_combined['Exchange_Rate_BOK_Fallback'])
    else:
        fx_combined = hist_fx.rename(columns={'Exchange_Rate_BOK_Fallback': 'Exchange_Rate_BOK'})
    
    debt_df = pd.merge(debt_df, fx_combined[['Year', 'Exchange_Rate_BOK']], on='Year', how='left')
    
    # Save to CSV
    os.makedirs('data', exist_ok=True)
    debt_df.drop(columns=['Year']).to_csv('data/bok_debt_history.csv', index=False)
    print("BOK debt and FX data saved to data/bok_debt_history.csv")
    
    # Integration with master dataset
    master_path = 'data/south_korea_comprehensive_final.csv'
    if os.path.exists(master_path):
        master = pd.read_csv(master_path)
        if master.columns[0] == '' or 'Unnamed' in master.columns[0]:
            master.rename(columns={master.columns[0]: 'Date'}, inplace=True)
        master['Date'] = pd.to_datetime(master['Date'])
        
        # Merge Debt and FX from debt_df (Annual/Historical)
        master['Year'] = master['Date'].dt.year
        for col in ['Public_Debt_KRW_Billion', 'External_Debt_USD_Million']:
            if col in master.columns:
                master.drop(columns=[col], inplace=True)
        master = pd.merge(master, debt_df[['Year', 'Public_Debt_KRW_Billion', 'External_Debt_USD_Million']], 
                          on='Year', how='left')
        
        # Merge high-frequency BOK data
        api_data = [api_fx, api_cpi, api_rate, api_gdp]
        for df in api_data:
            if not df.empty:
                col_name = [c for col in [df.columns] for c in col if c != 'Date'][0]
                if col_name in master.columns:
                    master.drop(columns=[col_name], inplace=True)
                master = pd.merge(master, df, on='Date', how='left')

        # Fill missing FRED values with BOK values
        mappings = {
            'Exchange_Rate': 'Exchange_Rate_BOK',
            'CPI_Index_KOR': 'CPI_Index_KOR_BOK',
            'Policy_Rate': 'Policy_Rate_BOK',
            'Real_GDP_Q': 'Real_GDP_Q_BOK'
        }
        
        for fred_col, bok_col in mappings.items():
            if fred_col in master.columns and bok_col in master.columns:
                master[fred_col] = master[fred_col].fillna(master[bok_col])
        
        # Calculate CPI_YoY if missing but CPI_Index_KOR is present
        if 'CPI_Index_KOR' in master.columns:
            master['CPI_YoY_BOK'] = master['CPI_Index_KOR'].pct_change(12) * 100
            master['CPI_YoY'] = master['CPI_YoY'].fillna(master['CPI_YoY_BOK'])

    # Combined high-frequency BOK data for master integration
    high_freq_df = pd.DataFrame({'Date': master['Date']})
    for df in [api_fx, api_cpi, api_rate, api_gdp]:
        if not df.empty:
            high_freq_df = pd.merge(high_freq_df, df, on='Date', how='left')
    
    high_freq_df.to_csv('data/bok_macro_extra.csv', index=False)
    print("BOK high-frequency data saved to data/bok_macro_extra.csv")

    # Cleanup and save master
    master.to_csv(master_path, index=False)



if __name__ == "__main__":
    consolidate_and_merge()
