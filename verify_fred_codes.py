import pandas_datareader.data as web
import datetime
import pandas as pd

def verify_codes(codes):
    results = []
    start = datetime.datetime(1960, 1, 1)
    end = datetime.datetime.now()
    
    for code in codes:
        try:
            print(f"Checking {code}...")
            data = web.DataReader(code, 'fred', start, end)
            if not data.empty:
                # Frequency is usually given in metadata, but pandas-datareader doesn't return all of it.
                # We can infer it from the index.
                diff = data.index.to_series().diff().mode()[0]
                freq = "Monthly" if diff.days <= 31 else ("Quarterly" if diff.days <= 93 else "Annual")
                first_date = data.index[0].strftime('%Y-%m-%d')
                results.append({'Code': code, 'Start Date': first_date, 'Frequency': freq})
            else:
                results.append({'Code': code, 'Start Date': 'N/A', 'Frequency': 'N/A'})
        except Exception as e:
            results.append({'Code': code, 'Start Date': 'N/A', 'Frequency': f'Error: {e}'})
    
    return pd.DataFrame(results)

codes_to_test = [
    'KORPFCEADSMEI', 'KORGFCFADSMEI', 'KORGFCEADSMEI', 'KOREXPGDPASMEI', 'KORIMPGDPASMEI', # GDP components
    'KORSLRTTO01GYM', 'KORSLRTTO01GPM', 'KORSLRTTO01IXOB', 'KORSLRTTO01MEI', # Retail Sales
    'KORPROINDMISMEI', 'KORPROPHAMEI', # Industrial Production
    'CPALTT01KRM659N', 'EXKOUS', 'MYAGM2KRM189N', 'IRLTLT01KRM156N', # Others
    'KORIPPHASMMEI', # Ind Prod Pharmaceuticals
    'KORIPPHADSMEI',
    'KORPI2300000', # PPI Pharmaceuticals?
]

df = verify_codes(codes_to_test)
print(df)
