import pathlib
import json


class Env:
    robin_username = ''
    robin_password = ''

    def __init__(self):
        file = str(pathlib.Path().absolute()) + '../env.json'
        with open(file) as json_file:
            data = json.load(json_file)
            robin_username = data['robin_username']
            robin_password = data['robin_password']


