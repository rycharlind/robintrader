import robin_stocks as robin
import pathlib
import json
import csv
import pathlib
from datetime import datetime, timedelta
import numpy
import pandas as pd
import math
from env import Env
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def read_csv(filename: str) -> pd.DataFrame:
    file = str(pathlib.Path().absolute()) + '/data/' + filename + '.csv'
    return pd.read_csv(file)


def write_csv(dataframe: pd.DataFrame, filename: str):
    file = str(pathlib.Path().absolute()) + '/data/' + filename + '.csv'
    dataframe.to_csv(file, sep=',')


def get_next_report_date(earnings):
    current_date = None
    if (earnings):
        for earning in earnings:
            report = earning['report']
            current_date = get_latest_date(current_date, report['date'])

    return current_date


def get_latest_date(current_date, date_string):
    new_date = datetime.strptime(date_string, '%Y-%m-%d')
    if (current_date):
        if (new_date > current_date):
            return new_date
        return current_date
    else:
        return new_date


def get_date_from_str(date_string):
    return datetime.strptime(date_string, '%Y-%m-%d')


def get_date(date_object):
    if (type(date_object) is str):
        return get_date_from_str(date_object)
    else:
        return date_object


def request_data() -> pd.DataFrame:
    stocks = read_csv('stocks-dev')
    for index, row in stocks.iterrows():
        try:
            earnings = robin.get_earnings(row.symbol)
            next_report_date = get_next_report_date(earnings)
            stocks.at[index, 'next_report_date'] = next_report_date
        except:
            logging.error('%s failed earnings request', row.symbol)

        try:
            price = robin.get_latest_price(row.symbol)
            stocks.at[index, 'price'] = price[0]
        except:
            logging.error('%s failed price request', row.symbol)

    return stocks


def get_date_before(date_string, days):
    return get_date_from_str(date_string) - timedelta(days=days)


def buy(symbol):
   print('Buy: ', symbol)


def sell(symbol):
    print('Sell: ', symbol) 


def start(reload=False):
    stocks = None
    robin.login(Env.robin_username, Env.robin_password, expiresIn=99999999)
    if (reload):
        stocks = request_data()
        write_csv(stocks, 'stocks_df')
    else:
        stocks = read_csv('stocks_df')

    for index, row in stocks[stocks.next_report_date.notnull()].iterrows():
        report_day_before = get_date(row.next_report_date) - timedelta(days=1)
        if (datetime.today().date() == report_day_before.date()):
            buy(row.symbol)


start(reload=False)
#stocks = read_csv('stocks_df')
#print(stocks[stocks.price.notnull()].count())
#print(stocks.price.max())
