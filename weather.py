import requests
import json

url = 'http://api.weatherapi.com/v1/current.json?key=d63159ad8f4948f4bb7224129240309&q=Baltimore'
key = '?key=d63159ad8f4948f4bb7224129240309'
#url = (initial_url + key)
print(url)
data = requests.get(url)
print(data)
raw_data = json.loads(data.text)
print(raw_data)