class SportAPI:
    def __init__(self, sport):
        self.sport = sport
        self.api_link = {
            'nfl': 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/2022?key=1455ced235a74c71862688fb1a38dc7f',
            'mlb': 'https://api.sportsdata.io/v3/mlb/scores/json/Stadiums?key=2b60f921b3a841f5a87fd5275c373f9e',
            'tennis': 'https://api.sportsdata.io/v3/tennis/scores/json/Players?key=c399f941dd994a6e96d899b51666921d'
        }

        self.this_api = self.api_link.get(sport)

    def api_links(self):
        self.nfl_api = 'https://api.sportsdata.io/v3/nfl/scores/json/Scores/2022?key=1455ced235a74c71862688fb1a38dc7f'
        self.tennis_api = 'https://api.sportsdata.io/v3/tennis/scores/json/Players?key=c399f941dd994a6e96d899b51666921d'

        if self.chosen_sport == 1:
            return self.nfl_api
        if self.chosen_sport == 2:
            return self.tennis_api


"""class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self, message):
        self.message = message + ' ' + self.name
        return self.message
    def __str__(self):
        return f"this person is named {self.name}"

andy = Person('shayda')
print(andy.say_hello('hey'))
bob = Person('andy')
print(bob.say_hello('hi'))
print(bob.name)
print(andy)"""