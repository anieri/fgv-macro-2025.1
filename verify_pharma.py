import pandas_datareader.data as web
import datetime
import pandas as pd

codes_to_test = [
    'KORPRMA2101IXOBM', 'KORPRMA2101GYM', 'KORPRMA2101GPM',
    'KORPRMA2101GYSAM', 'KORPRMA2101GPSAM', 'KORPRMA2101IXNBM',
    'KORPRIN2101IXOBM', 'KORPRIN2101GYSAM',
    'PRMA21KRM661N', 'PRMA21KRM659N',
    'KORPROPHASMEI', 'KORPROPHAMEI',
]

results = []
start = datetime.datetime(1960, 1, 1)
end = datetime.datetime.now()

for code in codes_to_test:
    try:
        data = web.DataReader(code, 'fred', start, end)
        if not data.empty:
            results.append({'Code': code, 'Start': data.index[0].strftime('%Y-%m-%d'), 'End': data.index[-1].strftime('%Y-%m-%d')})
    except:
        pass

df = pd.DataFrame(results)
print(df)
