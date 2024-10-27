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
import nfl_api
import display
import pywebio
import builtins
import nfl_api
print = pprint.pprint
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

class UrlStatusError(Exception):
    pass

class MlbFeedNotAvailable(Exception):
    pass

def build_api_url():
    """sport = nfl_api.SportAPI
    sport.choose_sport(nfl_api.SportAPI)
    url = sport.api_links(nfl_api.SportAPI)
    logger.info(print(url))
    return url"""

    initial_url = 'https://api.sportsdata.io/v3/mlb/scores/json/Stadiums'
    key = '?key=2b60f921b3a841f5a87fd5275c373f9e'
    url = (initial_url + key)
    if requests.get(url).status_code != 200:
        raise UrlStatusError
    return url

def download_mlb_data():
    delay = 0
    while True:
        try:
            response_stats = requests.get(build_api_url())
            logger.info('URL Access Successful')
        except UrlStatusError:
            logger.info('URL NOT Access Successful')
            if delay > 30:
                raise MlbFeedNotAvailable
            delay += 5
            time.sleep(delay)
            continue
        else:
            break
    raw_data = json.loads(response_stats.text)
    number_games = (len(raw_data))
    nfl_api.mongo_sports(raw_data)
    data = pd.DataFrame(raw_data)
    print(data)

    return raw_data
    # return {game_index: raw_data[game_index]['StadiumDetails'] for game_index in range(number_games)}

def main():
    download_mlb_data()

if __name__ == '__main__':
    main()