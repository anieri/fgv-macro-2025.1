import pandas_datareader.data as web
import datetime
import pandas as pd

codes = ['KORAGRGDPASMEI', 'KORINDGDPASMEI', 'KORSRVGDPASMEI', 'KORPRMA2101GYM', 'KORPRMA2101IXOBM', 'KORPRMNTO01IXOBM']
results = []
start = datetime.datetime(1960, 1, 1)

for code in codes:
    try:
        data = web.DataReader(code, 'fred', start)
        if not data.empty:
            results.append({'Code': code, 'Start': data.index[0].strftime('%Y-%m-%d'), 'Freq': 'Monthly' if (data.index[1]-data.index[0]).days < 40 else 'Quarterly'})
    except:
        pass
print(pd.DataFrame(results))
