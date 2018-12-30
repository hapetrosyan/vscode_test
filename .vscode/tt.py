import symbol as s
import data_ops as do
import time

sym = s.Symbol('TMO')
print(sym.cpp_sum_10_100)
time.sleep(15)
sym = s.Symbol('EPAM')
print(sym.cpp_sum_10_100)
time.sleep(15)
sym = s.Symbol('AMZN')
print(sym.cpp_sum_10_100)
time.sleep(15)
sym = s.Symbol('AMP')
print(sym.cpp_sum_10_100)





# syms = ['TMO', 'EPAM', 'AMZN', 'AMP']
# for symbol in syms:
#     sym = s.Symbol(symbol)
#     # print(symbol)
#     # print(sym.alphavantage_100_days_df)
#     print(symbol, sym.get_last_n_ccp_sum(n = 10, period = '100_days'))
