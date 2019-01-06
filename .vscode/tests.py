import data_ops
import pandas as pd
import misc_ops
import symbol as s
import datetime
from scipy import stats

mo = misc_ops.MiscOps()
do = data_ops.DataOps()

period_start = '2018-11-15'
period_end = '2018-12-24'
min_stock_price = 100
min_increase_pct = .01
data_source = 'file'

sym = s.Symbol('GOOG')

print(sym.alphavantage_intraday_1_min_df[['datetime', 'close', 'ccp', 'volume']])

print(sym.ccp_sum_100_1_min)
print(sym.ccp_sum_50_1_min)
print(sym.ccp_sum_20_1_min)
print(sym.ccp_sum_10_1_min)
print(sym.ccp_sum_5_1_min)

