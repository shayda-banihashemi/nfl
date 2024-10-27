import json
import pprint
import requests
import pandas as pd
import datetime
import time
from loguru import logger
import collections
import pickle
import os


#print = pprint.pprint

"""
initial_url = 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/'
key = '?key=1455ced235a74c71862688fb1a38dc7f'
url = (initial_url + '2022' + key)
print(url)
data = requests.get(url)
print(data)
raw_data = json.loads(data.text)
print(raw_data)
"""



netflix_data = pd.read_csv('/kaggle/input/netflix-data-analysis/netflix_movies (1).csv')
netflix_data

