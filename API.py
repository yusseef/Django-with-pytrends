import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
pytrend.build_payload(kw_list=['miami heat', 'boston celtics'])
df = pytrend.interest_by_region(resolution='USA', inc_low_vol=False)
print(df)
# df.to_csv('historical.csv')