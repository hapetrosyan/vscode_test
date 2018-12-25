import pyodbc
import pandas as pd
import numpy as np
import datetime
from pandas import ExcelWriter
from pandas import ExcelFile
import shutil
import os
from os import walk

class DataOps:
    @staticmethod
    def get_stock_price_df_file(period_start, period_end, min_price):
        df = pd.read_excel(r"C:\Q_C_Hakob\PythonProjects\vscode_test\.vscode\sp_micro.xlsx", sheet_name='sp',
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



    # print(symbols_list)