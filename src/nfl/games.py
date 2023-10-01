from dataclasses import dataclass
import datetime

@dataclass
class Game:
    competitors: None
    score: None
    duration_seconds: int
    location: dict
    date: datetime

class Football:
    game: Game

    def set_teams(self, teams: list):
        return teams
    def set_score(self, score: list):
        return score
    def set_location(self, city: str, state: str, country: str, stadium: str):
        return {'city': city, 'state': state, 'country': country, 'stadium': stadium}

    game.teams = self.set_teams(self, teams)
    game.score = self.set_score(self, score)
    game.location = self.set_location(self, set_location())


game = Game()

print(game)

football = Football()
baseball = Baseball()
football.game