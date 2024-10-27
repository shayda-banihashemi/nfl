"""NFL statistics feature tests."""
import nfl.nfl_app
import pytest

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

#@scenario('test_publish.feature', 'List wins and losses')
def test_list_wins_and_losses():
    pass
    """List wins and losses."""

@pytest.fixture
def nfl_keys():
    return ['GameKey', 'SeasonType', 'Season', 'Week', 'Date', 'AwayTeam', 'HomeTeam', 'AwayScore', 'HomeScore',
            'Channel', 'PointSpread', 'OverUnder', 'Quarter', 'TimeRemaining', 'Possession', 'Down', 'Distance',
            'YardLine', 'YardLineTerritory', 'RedZone', 'AwayScoreQuarter1', 'AwayScoreQuarter2', 'AwayScoreQuarter3',
            'AwayScoreQuarter4', 'AwayScoreOvertime', 'HomeScoreQuarter1', 'HomeScoreQuarter2', 'HomeScoreQuarter3',
            'HomeScoreQuarter4', 'HomeScoreOvertime', 'HasStarted', 'IsInProgress', 'IsOver', 'Has1stQuarterStarted',
            'Has2ndQuarterStarted', 'Has3rdQuarterStarted', 'Has4thQuarterStarted', 'IsOvertime', 'DownAndDistance',
            'QuarterDescription', 'StadiumID', 'LastUpdated', 'GeoLat', 'GeoLong', 'ForecastTempLow',
            'ForecastTempHigh', 'ForecastDescription', 'ForecastWindChill', 'ForecastWindSpeed', 'AwayTeamMoneyLine',
            'HomeTeamMoneyLine', 'Canceled', 'Closed', 'LastPlay', 'Day', 'DateTime', 'AwayTeamID', 'HomeTeamID',
            'GlobalGameID', 'GlobalAwayTeamID', 'GlobalHomeTeamID', 'PointSpreadAwayTeamMoneyLine',
            'PointSpreadHomeTeamMoneyLine', 'ScoreID', 'Status', 'GameEndDateTime', 'HomeRotationNumber',
            'AwayRotationNumber', 'NeutralVenue', 'RefereeID', 'OverPayout', 'UnderPayout', 'HomeTimeouts',
            'AwayTimeouts', 'DateTimeUTC', 'Attendance', 'IsClosed', 'StadiumDetails']

@pytest.fixture
def years():
    return 2000, 2022

@given('A year')
def test_get_most_recent_year(years):
    assert years[0] <= nfl.nfl_app.get_most_recent_year() <= years[1]


def test_download_nfl_data(nfl_keys):
    nfl_t = nfl.nfl_app.download_nfl_data()
    assert isinstance(nfl_t, dict)
    assert isinstance(nfl_t[0], dict)
    assert list(nfl_t[0].keys()) == nfl_keys
    #print(list(nfl_t[0].keys()))
