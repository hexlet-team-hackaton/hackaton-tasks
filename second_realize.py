import copy

import loguru
import requests


response = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json').json()

gifts = response['gifts']
moves_by_coord = response['children']
stackOfBags: list[list] = list()
moves: list[dict] = moves_by_coord


gifts_bag = list()
next_bag = list()
next_coord = list()
weight = 0
volume = 0


for gift in gifts:
    _id = gift['id']
    if gift['weight'] + weight > 200 or gift['volume'] + volume > 100:
        next_bag.append(gift)
        gifts_bag_copy = copy.deepcopy(gifts_bag)
        stackOfBags.append(gifts_bag_copy)
        moves.insert(_id - 1, {'x': 0, 'y': 0})
        gifts_bag.clear()
        weight = 0
        volume = 0
    else:
        if len(next_bag) != 0:
            gifts_bag.append(next_bag[0]['id'])
            weight += next_bag[0]['weight']
            volume += next_bag[0]['volume']
            next_bag.clear()
        gifts_bag.append(gift['id'])
        weight += gift['weight']
        volume += gift['volume']


last_gift = gifts_bag[-3:]
stackOfBags.append(gifts_bag[0: -3])
stackOfBags.append(last_gift)

# for i in stackOfBags:
#     _len += len(i)
# print(_len)
#
# print(moves)

# _request = requests.post('https://datsanta.dats.team/api/round',
#                          headers={
#                              'content-type': 'application/json',
#                              'X-API-Key': 'dbf6c320-65af-4558-bba6-8f4714ea69c3'
#                                   },
#                          json={
#                              'mapID': 'faf7ef78-41b3-4a36-8423-688a61929c08',
#                              'moves': moves,
#                              'stackOfBags': stackOfBags,
#                                }
#                          )
# print(_request.text)

# print(moves)
print(requests.get(
    'https://datsanta.dats.team/api/round/01GN0QVWQX9150Y1PV54APPBGR',
    headers={'X-API-Key': 'dbf6c320-65af-4558-bba6-8f4714ea69c3',
             'content-type': 'application/json',
             },
).text)
