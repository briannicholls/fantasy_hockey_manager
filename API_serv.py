#Use NHL API service to collect and update information about Players, Teams, Games, etc.
from cmd import IDENTCHARS
import json
from urllib import response
import requests


## Services for Player class
##

def get_player(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}".format(id), params={"Content-Type": "application/json"})
    json_data = response.json()
    # print(json_data['people'][0]['fullName'])
    return json_data['people'][0]   
#test print   
# get_player(8471214)


from Constants import *

def get_game_log(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=gameLog&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    game_log = json_data['stats'][0]['splits']
    # print (game_log[0])
    # gamePK "The Game" = The first 4 digits identify the season of the game (ie. 2017 for the 2017-2018 season). The next 2 digits give the type of game, where 01 = preseason, 02 = regular season, 03 = playoffs, 04 = all-star. The final 4 digits identify the specific game number. 
    return game_log
#test print   
# get_game_log(8471214)


def single_season_stat(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=statsSingleSeason&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    season_stat = json_data['stats'][0]['splits'][0]
    # print (season_stat)
    return season_stat
#test print   
# single_season_stat(8471214)


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


def win_loss_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=winLoss&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    win_loss = json_data['stats'][0]['splits']
    return win_loss


def player_schedule(id):
    pass
    ## needs to look up the player's team and then pull the teams schedule for the player
    # response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=winLoss&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    # json_data = response.json()
    # win_loss = json_data['stats'][0]['splits']
    # return win_loss



## Services for Game class
##

def game_box(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/game/{}/boxscore".format(id), params={"Content-Type": "application/json"})
    json_data = response.json()
    game_box = json_data['teams']
    # print (game_box)
    return game_box


def game_live(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/game/{}/feed/live".format(id), params={"Content-Type": "application/json"})
    json_data = response.json()
    game_live = json_data
    # print (game_live)
    return game_live


## Services for Team class
##

def team_schedule(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId={}&startDate={}&endDate={}".format(id,START_DATE,END_DATE), params={"Content-Type": "application/json"})
    json_data = response.json()
    team_schedule = json_data
    print (team_schedule)
    return team_schedule