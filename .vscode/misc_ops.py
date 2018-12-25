import pandas as pd
import datetime
from re import sub

class MiscOps:

    @staticmethod
    def rolling_sum(df, symbol, period_start, period_end):


        symbol_series = df[df.Symbol == symbol]\
        [df.Date >= period_start]\
        [df.Date <= period_end]\
        [['Date', 'Price']]

        ts = pd.Series(symbol_series['Price'].values, index=symbol_series['Date'])
        ts.sort_index(inplace=True)
        pc = ts.pct_change(1)
        return (pc.sum())

    @staticmethod
    def get_unique_symbols_list(df):
        return df['Symbol'].unique()

    @staticmethod
    def get_date_from_string(x):
        yy = int(x[0:4])
        mm = int(x[5:7])
        dd = int(x[8:10])
        return datetime.date(yy, mm, dd)

    @staticmethod
    def add_days_to_string_date(date, days_diff):
        a = MiscOps.get_date_from_string(date) + datetime.timedelta(days = days_diff)
        return a.strftime('%Y-%m-%d')

    @staticmethod
    def date_to_int(date):
        return int(sub('[^0-9]', '', str(date)))