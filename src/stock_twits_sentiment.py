import robin_stocks as robin
import requests
import json
import stocktwits as twits


def get_stocks_universe():
    with open('universe.json') as json_file:
        return json.loads(json_file.read())

        
stocks = get_stocks_universe()  
for stock in stocks:
    print(stock['symbol'])
    sentiment = twits.get_twits_sentiment_for_symbol(stock['symbol'])
    if (sentiment['bull'] > 15):
        print('Buy: ', stock['symbol'])


print(stocks)
print("Done!")