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
            'Policy_Rate': 'INTDSRKRM193N',
            'Retail_Sales': 'KORSLRTTO01IXOBM',
            'CPI_Health': 'KORCP060000GYM',
            'CPI_Index_KOR': 'KORCPIALLMINMEI',
            'CPI_Index_USA': 'USACPIALLMINMEI',
            'KOR_CCI': 'CSCICP03KRM665S',
            'KOR_BCI': 'BSCICP03KRM665S',
            # Quarterly
            'Real_GDP_Q': 'NGDPRSAXDCKRQ',
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
            'External_Debt_GNI': 'DT.DOD.DECT.GN.ZS',
            'Private_Credit_GDP': 'FS.AST.PRVT.GD.ZS',
            'Exp_GDP': 'NE.EXP.GNFS.ZS',
            'Imp_GDP': 'NE.IMP.GNFS.ZS',
            'KOR_GDP_Growth_WDI': 'NY.GDP.MKTP.KD.ZG',
            # Constant 2015 USD for demand components
            'Consumption_KD': 'NE.CON.PRVT.KD',
            'Gov_Spending_KD': 'NE.CON.GOVT.KD',
            'Investment_KD': 'NE.GDI.FTOT.KD',
            'Exports_KD': 'NE.EXP.GNFS.KD',
            'Imports_KD': 'NE.IMP.GNFS.KD'
        }
        
        try:
            # Fetch for South Korea
            df_kor = wb.data.DataFrame(indicators.values(), self.country_code, time=range(self.start.year, self.end.year + 1))
            df_kor = df_kor.transpose()
            inv_map = {v: k for k, v in indicators.items()}
            df_kor.columns = [inv_map.get(col, col) for col in df_kor.columns]
            df_kor.index = pd.to_datetime([str(i).replace('YR', '') for i in df_kor.index], format='%Y')

            # Fetch for OECD (OED)
            oecd_indicators = {
                'NY.GDP.MKTP.KD.ZG': 'OECD_GDP_Growth',
                'FP.CPI.TOTL.ZG': 'OECD_Inflation',
                'SL.UEM.TOTL.ZS': 'OECD_Unemployment'
            }
            df_oecd = wb.data.DataFrame(oecd_indicators.keys(), 'OED', time=range(self.start.year, self.end.year + 1))
            df_oecd = df_oecd.transpose()
            df_oecd.columns = [oecd_indicators.get(col, col) for col in df_oecd.columns]
            df_oecd.index = pd.to_datetime([str(i).replace('YR', '') for i in df_oecd.index], format='%Y')

            # Combine
            return df_kor.join(df_oecd, how='outer')
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
