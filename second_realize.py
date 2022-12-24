import copy
import requests


MAP = 'https://datsanta.dats.team/json/map/' \
      'faf7ef78-41b3-4a36-8423-688a61929c08.json'
VOLUME = 100
WEIGHT = 200


def get_data() -> dict:
    return requests.get(MAP).json()
