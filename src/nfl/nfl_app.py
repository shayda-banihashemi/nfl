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

Stadium_Stats = {}


class UrlStatusError(Exception):
    pass

class NflFeedNotAvailable(Exception):
    pass

"""def choose_api_url():
    chosen_sport = input('What sport do you want to access? Select a number. \n (1) NFL \n (2) Tennis \n')
    return chosen_sport"""

def build_api_url():
    test = nfl_api.SportAPI
    test.choose_sport(nfl_api.SportAPI)
    url = test.api_links(nfl_api.SportAPI)
    logger.info(print(url))
    return url

    """initial_url = 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/'
    key = '?key=1455ced235a74c71862688fb1a38dc7f'
    url = (initial_url + '2022' + key)
    if requests.get(url).status_code != 200:
        raise UrlStatusError
    return url"""


def get_most_recent_year():
    return datetime.datetime.now().year - 1




def download_nfl_data():
    delay = 0
    while True:
        try:
            response_stats = requests.get(build_api_url())
            logger.info('URL Access Successful')
        except UrlStatusError:
            if delay > 30:
                raise NflFeedNotAvailable
            delay += 5
            time.sleep(delay)
            continue
        else:
            break
    raw_data = json.loads(response_stats.text)
    number_games = (len(raw_data))
    return raw_data
    # return {game_index: raw_data[game_index]['StadiumDetails'] for game_index in range(number_games)}


def get_users_team():
    users_team = 'BAL'
    return users_team
    """query = {'team': {'prompt': 'Enter a team ', 'value': None, 'is_valid': False, 'min_value': 0, 'max_value': 3}}
    for field_title, field_data in query.items():
        field_data['value'] = input(field_data['prompt'])
    return query"""


def validate_users_team():
    pass


def get_stadium_attributes(stadium_state, attribute_type):
    stadium_data = ({game_index: stadium_state[game_index] for game_index in range(len(stadium_state))})
    stadium_state_data = (
    {game_index: stadium_state[game_index]['StadiumDetails'][attribute_type] for game_index in stadium_data})
    stadium_attribute_counter = collections.Counter(stadium_state_data.values())
    Stadium_Stats[attribute_type] = stadium_attribute_counter
    return stadium_attribute_counter


def get_team_stats(users_team, nfl_data):
    team_schedule = {}
    nfl_game_data = ({game_index: nfl_data[game_index] for game_index in range(len(nfl_data))})
    for game in nfl_game_data:
        if users_team == nfl_game_data[game]['AwayTeam']:
            team_schedule.update({nfl_game_data[game]['Week']: nfl_game_data[game]['AwayScore']})
        if users_team == nfl_game_data[game]['HomeTeam']:
            team_schedule.update({nfl_game_data[game]['Week']: nfl_game_data[game]['HomeScore']})
    print(team_schedule)


def main():
    # build_api_url()
    # get_most_recent_year()



    if os.path.isfile('nfl.pkl'):
        with open('nfl.pkl', 'rb') as f:
            stadium_details = pickle.load(f)
    else:
        stadium_details = download_nfl_data()
        with open('nfl.pkl', 'wb') as f:
            pickle.dump(stadium_details, f)
    stadium_stats = [get_stadium_attributes(stadium_details, attribute_type) for attribute_type in
                     ('PlayingSurface', 'Type', 'State')]
    get_team_stats(users_team=get_users_team(), nfl_data=download_nfl_data())

    # validate_users_team()
    # team = get_users_team()
    # validate_users_team(team)
    for stat in stadium_stats:
        print(stat)



    # get_nfl_data()


if __name__ == '__main__':
    main()
