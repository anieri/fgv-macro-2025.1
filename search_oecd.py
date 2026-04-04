import pandasdmx as sdmx
import pandas as pd

oecd = sdmx.Request('OECD')
# MEI: Main Economic Indicators
# Get the dataflow to see structure
dataflow = oecd.dataflow('MEI')
# Actually, fetching structure might be too slow. Let's try to fetch some data directly.
# KOR.PRINTO01.M (Total Industry)
# KOR.PRINTO01.Q (Total Industry)

# Try to find pharmaceuticals in MEI
# Common code for Pharma: PRPH01
try:
    data = oecd.data('MEI', key='KOR.PRPH01.M').to_pandas()
    print("Found PRPH01!")
    print(data.head())
except:
    print("PRPH01 not found.")

# Try PRIP01
try:
    data = oecd.data('MEI', key='KOR.PRIP01.M').to_pandas()
    print("Found PRIP01!")
    print(data.head())
except:
    print("PRIP01 not found.")

# Try OECD industry classification
# Production of manufactured goods: PRMA01
# Production of pharmaceuticals: PRPH01 or PRMA21
try:
    data = oecd.data('MEI', key='KOR.PRMA21.M').to_pandas()
    print("Found PRMA21!")
    print(data.head())
except:
    print("PRMA21 not found.")

