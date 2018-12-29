import symbol as s
import data_ops as do


sym = s.Symbol('AMZN')


# print(d1['ccp'])
# print(d1['ccp'][-10:])
# print(sym.get_last_n_ccp_sum(d1, 10))
print(sym.get_last_n_ccp_sum())
print(sym.get_last_n_ccp_sum(n = 10, period = '100_days'))
