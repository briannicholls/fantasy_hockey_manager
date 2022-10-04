#Use NHL API service to collect and update information about Players, Teams, Games, etc.
from cmd import IDENTCHARS
import json
from urllib import response
import requests

def get_player(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}".format(id), params={"Content-Type": "application/json"})
    json_data = response.json()
    # print(json_data['people'][0]['fullName'])
    return json_data['people'][0]   
#test print   
# get_player(8471214)


from Constants import *

def single_season_stat(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=statsSingleSeason&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    season_stat = json_data['stats'][0]['splits'][0]
    # print (season_stat)
    return season_stat
#test print   
# single_season_stat(8471214)


def get_game_log(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=gameLog&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    game_log = json_data['stats'][0]['splits']
    # print (game_log[0])
    return game_log
#test print   
# get_game_log(8471214)

def div_stat_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=vsDivision&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    div_stats = json_data['stats'][0]['splits']
    return div_stats


def mon_stat_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=byMonth&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    mon_stat = json_data['stats'][0]['splits']
    return mon_stat

def week_stat_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=byDayOfWeek&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    week_stat = json_data['stats'][0]['splits']
    return week_stat

def vs_league_stat(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=regularSeasonStatRankings&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    league_stat = json_data['stats'][0]['splits']
    return league_stat

def reg_season_pace(id):
    #only works in season
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=onPaceRegularSeason&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    season_pace = json_data['stats'][0]['splits']
    return season_pace

def home_away_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=homeAndAway&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    home_away = json_data['stats'][0]['splits']
    return home_away
