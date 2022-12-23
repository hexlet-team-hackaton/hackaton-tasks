import copy

import requests


response = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json').json()

gifts = response['gifts']
moves_count = response['children']
stackOfBags: list[list] = list()
moves: list[dict] = list()


gifts_bag = list()
weight = 0
volume = 0
for gift in gifts:
    if gift['weight'] + weight > 200 or gift['volume'] + volume > 100:
        gifts_bag_copy = copy.deepcopy(gifts_bag)
        stackOfBags.append(gifts_bag_copy)
        gifts_bag.clear()
        weight = 0
        volume = 0
    else:
        gifts_bag.append(gift['id'])
        weight += gift['weight']
        volume += gift['volume']
