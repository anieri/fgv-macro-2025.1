import pandas as pd
import pandas_datareader.data as web
import wbgapi as wb
import datetime
import os

class SocioEconomicDataLoader:
    def __init__(self, start_year=1960, end_year=2024):
        self.start = datetime.datetime(start_year, 1, 1)
        self.end = datetime.datetime(end_year, 12, 31)
        self.country_code = 'KOR'

    def fetch_fred_data(self):
        """Fetches Monthly and Quarterly data from FRED."""
        print("Coletando dados do FRED (Mensal/Trimestral)...")
        indicators = {
            # Monthly
            'CPI_YoY': 'CPALTT01KRM659N',
            'Unemployment': 'LRHUTTTTKRM156S',
            'Ind_Prod': 'KORPROINDMISMEI',
            'Exchange_Rate': 'EXKOUS',
            'Exports_M': 'XTEXVA01KRM667S',
            'Imports_M': 'XTIMVA01KRM667S',
            'Policy_Rate': 'INTDSRKRM193N',
            'Retail_Sales': 'KORSLRTTO01IXOBM',
            'CPI_Health': 'KORCP060000GYM',
            'CPI_Index_KOR': 'KORCPIALLMINMEI',
            'CPI_Index_USA': 'USACPIALLMINMEI',
            # Quarterly
            'Real_GDP_Q': 'NGDPRSAXDCKRQ',
            'Consumption_Q': 'NAEXKP02KRQ189S',
            'Gov_Spending_Q': 'NAEXKP03KRQ189S',
            'Investment_Q': 'NAEXKP04KRQ189S'
        }
        
        df_list = []
        for name, code in indicators.items():
            try:
                data = web.DataReader(code, 'fred', self.start, self.end)
                data.columns = [name]
                df_list.append(data)
            except Exception as e:
                print(f"Erro ao coletar {name} ({code}): {e}")
        
        return pd.concat(df_list, axis=1)

    def fetch_wdi_data(self):
        """Fetches Annual data from World Bank (WDI)."""
        print("Coletando dados do Banco Mundial (Anual)...")
        indicators = {
            'Agri_VA': 'NV.AGR.TOTL.KD',
            'Ind_VA': 'NV.IND.TOTL.KD',
            'Srv_VA': 'NV.SRV.TOTL.KD',
            'Public_Health_Exp_GDP': 'SH.XPD.GHED.GD.ZS',
            'Private_Health_Exp_Total': 'SH.XPD.PVTD.CH.ZS',
            'Total_Health_Exp_GDP': 'SH.XPD.CHEX.GD.ZS',
            'Gov_Debt_GDP': 'GC.DOD.TOTL.GD.ZS',
            'Current_Account_GDP': 'BN.CAB.XOKA.GD.ZS',
            'Private_Credit_GDP': 'FS.AST.PRVT.GD.ZS'
        }
        
        try:
            # wbgapi returns a pandas series/dataframe
            data = wb.data.DataFrame(indicators.values(), self.country_code, time=range(self.start.year, self.end.year + 1))
            # Reshape: the index is currently indicator codes, we want time
            data = data.transpose()
            # Map codes back to friendly names
            inv_map = {v: k for k, v in indicators.items()}
            data.columns = [inv_map.get(col, col) for col in data.columns]
            # Convert index to datetime (format is YRXXXX)
            data.index = pd.to_datetime([str(i).replace('YR', '') for i in data.index], format='%Y')
            return data
        except Exception as e:
            print(f"Erro ao coletar dados do WDI: {e}")
            return pd.DataFrame()

    def get_full_dataset(self):
        """Combines all data into one master file."""
        fred_df = self.fetch_fred_data()
        wdi_df = self.fetch_wdi_data()
        
        # Merge all into one. Since WDI is Jan 1st of each year, 
        # it will naturally align with the monthly/quarterly series.
        master_df = fred_df.join(wdi_df, how='outer')
        
        os.makedirs('data', exist_ok=True)
        master_df.to_csv('data/south_korea_comprehensive.csv')
        print("Dataset completo salvo em data/south_korea_comprehensive.csv")
        return master_df

if __name__ == "__main__":
    loader = SocioEconomicDataLoader()
    loader.get_full_dataset()
