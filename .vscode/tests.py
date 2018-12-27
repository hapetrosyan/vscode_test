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
min_stock_price = 0
min_increase_pct = .01
data_source = 'db_local'

df = do.get_stock_price_df(period_start, period_end, min_stock_price, data_source)

unique_symbols_list = mo.get_unique_symbols_list(df)
i = 0
for symbol in unique_symbols_list:
    # i++
    print(i, symbol)


# for symbol in unique_symbols_list:
#     symbol_obj = s.Symbol(symbol, df, period_start, period_end)
#     if symbol_obj.symbol_rolling_sum > min_increase_pct and symbol_obj.symbol_rolling_sum_1w > min_increase_pct and symbol_obj.symbol_rolling_sum_1m > min_increase_pct:
#         print(symbol_obj.symbol, symbol_obj.symbol_rolling_sum, symbol_obj.symbol_rolling_sum_1w, symbol_obj.symbol_rolling_sum_1m)
        # slope, intercept, r_value, p_value, std_err = stats.linregress(date_as_int, price)
        # print(slope, intercept)


# symbol_object = s.Symbol('AMZN', df, period_start, period_end)
# for k, v in symbol_object.alphavantage_intraday_5_min_dict.items():
#     print(k, v)
