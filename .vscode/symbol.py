import pandas as pd
import misc_ops as mo
import data_ops

class Symbol:
    def __init__(self, symbol, df = '', period_start = '', period_end = ''):
        do = data_ops.DataOps()
        self.symbol = symbol
        # self.hist_price_df = df
        # self.period_start = period_start
        # self.period_end = period_end
        # self.symbol_hist_price_df = df[df['Symbol'] == symbol][['Date', 'Price']].sort_values(by=['Date'])
        # self.symbol_series_1w = pd.Series([])
        # self.symbol_rolling_sum_1w = 0
        # self.period_start_1w = mo.MiscOps.add_days_to_string_date(self.period_end, -7)
        # self.symbol_series_1m = pd.Series([])
        # self.symbol_rolling_sum_1m = 0
        # self.period_start_1m = mo.MiscOps.add_days_to_string_date(self.period_end, -30)
        # """ calculating rolling sum for the last 1 week """
        # if ((mo.MiscOps.get_date_from_string(period_end) - mo.MiscOps.get_date_from_string(period_start)).days >= 7):
        #     self.symbol_series_1w = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start_1w, self.period_end)
        #     self.symbol_rolling_sum_1w = self.get_symbol_rolling_sum(self.symbol_series_1w)
        # """ calculating rolling sum for the last 1 month """
        # if ((mo.MiscOps.get_date_from_string(period_end) - mo.MiscOps.get_date_from_string(period_start)).days >= 30):
        #     self.symbol_series_1m = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start_1m, self.period_end)
        #     self.symbol_rolling_sum_1m = self.get_symbol_rolling_sum(self.symbol_series_1m)
        # self.symbol_series = self.get_symbol_series(self.hist_price_df, self.symbol, self.period_start, self.period_end)
        # self.symbol_rolling_sum = self.get_symbol_rolling_sum(self.symbol_series)

        self.alphavantage_100_days_dict = do.get_alphavantage_100_days_dict(self.symbol)
        self.alphavantage_intraday_5_min_dict = do.get_alphavantage_intraday_5_min_dict(self.symbol)
        # self.alphavantage_1_week_dict = do.get_alphavantage_1_week_dict(self.symbol)

        self.alphavantage_intraday_5_min_df = self.get_alphavantage_df_from_dict(self.alphavantage_intraday_5_min_dict)


    @staticmethod
    def get_symbol_series(df, symbol, period_start, period_end):
        symbol_series = df[df.Symbol == symbol]\
        [df.Date >= period_start]\
        [df.Date <= period_end]\
        [['Date', 'Price']]

        return symbol_series

    @staticmethod
    def get_symbol_rolling_sum(symbol_series):
        ts = pd.Series(symbol_series['Price'].values, index=symbol_series['Date'])
        ts.sort_index(inplace=True)
        pc = ts.pct_change(1)
        return (pc.sum())

    @staticmethod
    def get_alphavantage_df_from_dict(alphavantage_dict):
        alphavantage_df = pd.DataFrame(columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        for k, v in alphavantage_dict.items():
            alphavantage_df = alphavantage_df.append({'datetime': k, 'open': v['open'], 'high': v['high'], 'low': v['low'], 'close': v['close'], 'volume': v['volume']}, ignore_index=True)
        return alphavantage_df