import robin_stocks as robin
from env import Env


robin.login(Env.robin_username, Env.robin_password, expiresIn=99999999)
symbol = 'BTC'

pairs = robin.get_crypto_currency_pairs()
positions = robin.get_crypto_positions()
info = robin.get_crypto_info(symbol)
quote = robin.get_crypto_quote(symbol)


print('done!!')