import pyodbc
import pandas as pd
import numpy as np
import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
import shutil
import os
from os import walk
import requests
import misc_ops


class DataOps:
    @staticmethod
    def get_stock_price_df_file(period_start, period_end, min_price):
        df = pd.read_excel(r"C:\Q_C_Hakob\PythonProjects\vscode_test\.vscode\sp_mini.xlsx", sheet_name='sp',
                           dtype={'Date': datetime.date, 'Symbol': str})

        df = df[df.Price > min_price][df.Date >= period_start][df.Date <= period_end]
        return df

    @staticmethod
    def get_stock_price_df_db_prod(period_start, period_end, min_price):

        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=corp-bi;"
                              "Database=ClientStatement;"
                              "Trusted_Connection=yes;")


        query = """SELECT
                    sp.ProcessingDate AS Date, RTRIM(crk.Symbol) AS Symbol, sp.SecurityPriceAmount AS Price
                    FROM SecuritiesTradeManagement.dbo.BpsSecurityMasterSecurityPrice sp
                    INNER JOIN [SecuritiesTradeManagement].[dbo].[BpsSecurityMasterCrossReferenceKey] crk ON crk.SecurityNumber = sp.SecurityNumber AND crk.Symbol IS NOT NULL
                    WHERE 1=1
                    AND sp.CurrencyCode = '001'
                    AND sp.PriceTypeCode = 'C'
                    AND sp.CountryCode = 'US'
                    AND sp.ProcessingDate BETWEEN '"""+period_start+"""' AND '"""+period_end+"""'
                    AND sp.SecurityPriceAmount > """+str(min_price)+"""
                    ORDER BY crk.ProcessingDate ASC"""

        df = pd.read_sql_query(query, cnxn, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
        df['Date'] = pd.to_datetime(df['Date'])
        return df


    @staticmethod
    def get_stock_price_df_db_local(period_start, period_end, min_price):

        cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=localhost;"
                              "Database=SPA;"
                              "Trusted_Connection=yes;")

        query = """SELECT Date, RTRIM(Symbol) AS Symbol, Price
                    FROM SPA.dbo.SecurityPriceHistorical
                    WHERE Date BETWEEN '"""+period_start+"""' AND '"""+period_end+"""' 
                    AND Price > """+str(min_price)+""" 
                    ORDER BY Date ASC"""

        df = pd.read_sql_query(query, cnxn, index_col=None, coerce_float=True, params=None, parse_dates=None, chunksize=None)
        df['Date'] = pd.to_datetime(df['Date'])
        return df


    def get_stock_price_df(self, period_start, period_end, min_price, data_source='file'):
        if data_source == 'file':
            return self.get_stock_price_df_file(period_start, period_end, min_price)
        elif data_source == 'db_local':
            return self.get_stock_price_df_db_local(period_start, period_end, min_price)
        elif data_source == 'db_prod':
            return self.get_stock_price_df_db_prod(period_start, period_end, min_price)


    @staticmethod
    def get_alphavantage_100_days_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (Daily)']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))

    @staticmethod
    def get_alphavantage_intraday_5_min_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=5min&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (5min)']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))


    @staticmethod
    def get_alphavantage_intraday_1_min_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=1min&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Time Series (1min)']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))

    @staticmethod
    def get_alphavantage_1_week_dict(symbol):
        mo = misc_ops.MiscOps()
        request_link = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+symbol+'&apikey=K2L959U20SZIKBDG'
        resp = requests.get(request_link)

        if resp.status_code != 200:
            # This means something went wrong.
            raise ApiError('GET /tasks/ {}'.format(resp.status_code))
        resp_json = resp.json() # ['Time Series (Daily)']
        # for todo_item in resp.json():
            # print('{} {}'.format(todo_item['id'], todo_item['login']))
            # print(todo_item)

        # resp_metadata = resp_json['Meta Data']
        try:
            resp_time_series = resp_json['Weekly Time Series']
        except:
            resp_time_series = {}
        return(mo.format_alphavantage_dict(resp_time_series))


    @staticmethod
    def get_all_symbols_list(df):
        return df['Symbol'].unique()