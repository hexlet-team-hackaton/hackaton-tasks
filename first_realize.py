import requests


response = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json')

data = response.json()

stack_of_bags = list()
gifts_bag = list()
moves = list()


def stack_of_bags_collect(data):
    gifts_bag = list()
    weight = 0
    volume = 0
    for gift in data.get('gifts'):
        if volume > 100 or weight > 200:
            continue
        else:
            gifts_bag.append(gift.get('id'))
            weight += gift.get('weight')
            volume += gift.get('volume')
    yield gifts_bag


for i in stack_of_bags_collect(data):
    print(i)

for i in stack_of_bags_collect(data):
    print(i)

print(stack_of_bags_collect(data))

