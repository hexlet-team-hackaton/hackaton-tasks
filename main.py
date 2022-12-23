import requests
import json


response = requests.get('https://datsanta.dats.team/json/map/faf7ef78-41b3-4a36-8423-688a61929c08.json')

# with open('result.json', 'w') as f:
#     json.dump(data.json(), f, indent=4, ensure_ascii=False)

data = response.json()
