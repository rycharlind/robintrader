import requests
import json

def get_twits_sentiment_for_symbol(symbol):
    count = {}
    count['total'] = 0
    count['bull'] = 0
    count['bear'] = 0
    response = requests.get("https://api.stocktwits.com/api/2/streams/symbol/%s.x.json" % (symbol) )
    if response.status_code == 200:
        twits = response.json()
        for message in twits['messages']:
            count['total'] += 1
            entities = message['entities']
            if (entities):
                sentiment = entities['sentiment']
                if (sentiment):
                    if (sentiment['basic'] == 'Bullish'):
                        count['bull'] += 1

                    if (sentiment['basic'] == 'Bearish'):
                        count['bear'] += 1
        
        return count