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
min_stock_price = 1000
min_increase_pct = .01
data_source = 'db_local'

sym = s.Symbol('AMZN')

print(sym.alphavantage_intraday_1_min_df)
# print(sym.alphavantage_100_days_df)


# alphavantage_intraday_5_min_df = pd.DataFrame(columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])


# sym_dict = sym.alphavantage_intraday_5_min_dict.items()
# for k, v in sym_dict:
#     # print(k, v)
#     # print(k, v['open'], v['high'], v['low'], v['close'], v['volume'])
#     alphavantage_intraday_5_min_df = alphavantage_intraday_5_min_df.append({'datetime': k, 'open': v['open'], 'high': v['high'], 'low': v['low'], 'close': v['close'], 'volume': v['volume']}, ignore_index=True)


# print(alphavantage_intraday_5_min_df)


# df = pd.DataFrame.from_dict(sym_dict, orient='index')




# symbols = {}


# df = do.get_stock_price_df(period_start, period_end, min_stock_price, data_source)

# unique_symbols_list = do.get_all_symbols_list(df)

# for symbol in unique_symbols_list:
#     symbol_object = s.Symbol(symbol)
#     symbols[symbol] = symbol_object

# print(len(symbols))
# # print(symbols)
#     # for k, v in symbol_object.alphavantage_100_days_dict.items():
#     #     print(k, v)

# print(symbols['AMZN'].alphavantage_intraday_5_min_dict)


'''
for symbol in unique_symbols_list:
    symbol_obj = s.Symbol(symbol, df, period_start, period_end)
    if symbol_obj.symbol_rolling_sum > min_increase_pct and symbol_obj.symbol_rolling_sum_1w > min_increase_pct and symbol_obj.symbol_rolling_sum_1m > min_increase_pct:
        print(symbol_obj.symbol, symbol_obj.symbol_rolling_sum, symbol_obj.symbol_rolling_sum_1w, symbol_obj.symbol_rolling_sum_1m)
        slope, intercept, r_value, p_value, std_err = stats.linregress(date_as_int, price)
        print(slope, intercept)
'''
