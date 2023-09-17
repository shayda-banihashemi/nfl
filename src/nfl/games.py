from dataclasses import dataclass
import datetime

@dataclass
class Game:
    competitors: []
    score: int
    duration_seconds: int
    location: str
    date: datetime

class Football:
    game: Game
    def set_teams(self, teams: list):
