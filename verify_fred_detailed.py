import pandas_datareader.data as web
import datetime
import pandas as pd

def get_fred_info(code):
    start = datetime.datetime(1960, 1, 1)
    end = datetime.datetime.now()
    try:
        data = web.DataReader(code, 'fred', start, end)
        if not data.empty:
            first_date = data.index[0].strftime('%Y-%m-%d')
            last_date = data.index[-1].strftime('%Y-%m-%d')
            # Determine frequency from index
            diffs = data.index.to_series().diff().dropna()
            avg_diff = diffs.mean().days
            if avg_diff <= 31:
                freq = "Monthly"
            elif avg_diff <= 93:
                freq = "Quarterly"
            else:
                freq = "Annual"
            return {'Code': code, 'Start Date': first_date, 'End Date': last_date, 'Frequency': freq}
    except:
        pass
    return None

codes_to_test = [
    'KORPFCEADSMEI', 'KORGFCEADSMEI', 'KORGFCFADSMEI', # GDP Annual
    'NAEXKP02KRQ189S', 'NAEXKP03KRQ189S', 'NAEXKP04KRQ189S', 'NAEXKP06KRQ189S', 'NAEXKP07KRQ189S', # GDP Quarterly?
    'KORRETTTO01IXOBSAM', 'KORRETTTO01IXOBM', 'KORRETTTO01GYM', # Retail Sales
    'KORPROPHARMMEI', 'KORIPPHASMMEI', 'KORPROPHASMMEI', # Pharmaceuticals
    'XTEXVA01KRM667S', 'XTIMVA01KRM667S', # Exports/Imports Monthly
    'KORPROINDMISMEI', # Ind Prod
    'KORSLRTTO01IXOBM', # Retail
    'KORRETTTO01GYSAM', # Retail
]

results = []
for code in codes_to_test:
    info = get_fred_info(code)
    if info:
        results.append(info)

df = pd.DataFrame(results)
print(df)
