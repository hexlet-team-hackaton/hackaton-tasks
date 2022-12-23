import requests
import json


data = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json')

gifts = data.json()['gifts']
moves_count = data.json()['children']
stackOfBags: list[list] = list()
moves: list[dict] = list()



gifts_bag = list()
weight = 0
volume = 0
for gift in gifts:
