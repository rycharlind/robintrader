import robin_stocks as robin
from tabulate import tabulate
import pathlib
import json
from env import Env

def save_json(filename, json_object):
    current_dir = pathlib.Path().absolute()
    file = str(pathlib.Path().absolute()) + '/data/' + filename + '.json'
    with open(file, 'w') as outfile:
        json.dump(json_object, outfile)


robin.login(Env.robin_username, Env.robin_password, expiresIn=99999999)

symbol = 'AET'

quotes = robin.get_quotes(symbol)
fundementals = robin.get_fundamentals(symbol)
instrumentals = robin.get_instruments_by_symbols(symbol)
lastest_price = robin.get_latest_price(symbol)
popularity = robin.get_popularity(symbol)
all_positions = robin.get_all_positions()
ratings = robin.get_ratings(symbol)
earnings = robin.get_earnings(symbol)
pricebook = robin.get_pricebook_by_symbol(symbol)
#save_json('earnings', earnings)

print('done!!')