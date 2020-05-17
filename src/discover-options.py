import robin_stocks as robin
import pathlib
import json
from env import Env

robin.login(Env.robin_username, Env.robin_password, expiresIn=99999999)

options = robin.find_options_for_list_of_stocks_by_expiration_date('AAPL', '2020-05-22')

print('Done!')

