from pip._internal.index import collector
from pymongo import MongoClient


class SportAPI:
    def __init__(self, sport):
        self.sport = sport
        self.api_link = {
            'nfl': 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/2022?key=1455ced235a74c71862688fb1a38dc7f',
            'mlb': 'https://api.sportsdata.io/v3/mlb/scores/json/Stadiums?key=2b60f921b3a841f5a87fd5275c373f9e',
            'usta': 'https://api.sportsdata.io/v3/tennis/scores/json/Players?key=c399f941dd994a6e96d899b51666921d'
        }

        self.this_api = self.api_link.get(sport)

    def api_links(self):
        self.nfl_api = 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/2022?key=1455ced235a74c71862688fb1a38dc7f'
        self.usta_api = 'https://api.sportsdata.io/v3/tennis/scores/json/Players?key=c399f941dd994a6e96d899b51666921d'

        if self.chosen_sport == 1:
            return self.nfl_api
        if self.chosen_sport == 2:
            return self.usta_api


class MongoDBConnection:
    """MongoDB Connection"""

    def __init__(self, host='127.0.0.1', port=27017):
        """
        be sure to use the ip address not name for local windows
        CAUTION: Don't do this in production!!!
        """
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def print_mdb_collection(collection_name):
    for doc in collection_name.find():
        print(doc)


def mongo_sports(nfl_dict):
    mongo = MongoDBConnection()

    with mongo:
        # mongodb database; it all starts here
        db = mongo.connection.stats

        # collection in database
        stats = db["stats"]

        stats_ip = nfl_dict
        stats.insert_many(stats_ip)
        # print_mdb_collection(stats)

        # start afresh next time?
        yorn = input("Drop data?")
        if yorn.upper() == 'Y':
            stats.drop()
