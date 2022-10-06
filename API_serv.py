# Use NHL API service to collect and update information about Players, Teams, Games, etc.
from cmd import IDENTCHARS
import json
from tkinter import END
from urllib import response
import requests
from Constants import *
#########################################################################################
### http get to retrieve NHL API JSON

def http_get(endpoint):
    api_response = requests.get(BASE_URL+endpoint, params={"Content-Type": "application/json"})
    return api_response.json()

#########################################################################################
## Services for Player class
##

def get_player(player_id):
    player_attributes = http_get(ENDPOINT_DICT['get_player'].format(player_id))
    return player_attributes['people'][0]


def get_game_log(player_id):
    game_log = http_get(ENDPOINT_DICT['get_game_log'].format(player_id, CURRENT_SEASON))
    return game_log['stats'][0]['splits']


def season_stat(player_id):
    season_stats = http_get(ENDPOINT_DICT['season_stat'].format(player_id,CURRENT_SEASON))
    return season_stats['stats'][0]['splits'][0]


def div_split(player_id):
    div_stats = http_get(ENDPOINT_DICT['div_split'].format(player_id,CURRENT_SEASON))
    return div_stats['stats'][0]['splits'][0]


def mon_split(player_id):
    mon_stats = http_get(ENDPOINT_DICT['mon_split'].format(player_id,CURRENT_SEASON))
    return mon_stats['stats'][0]['splits'][0]


def week_split(player_id):
    week_split = http_get(ENDPOINT_DICT['week_split'].format(player_id,CURRENT_SEASON))
    return week_split['stats'][0]['splits'][0]


def league_stat(player_id):
    league_stat = http_get(ENDPOINT_DICT['league_stat'].format(player_id,CURRENT_SEASON))
    return league_stat['stats'][0]['splits'][0]


def season_pace(player_id):
    #only works in season per API
    season_pace = http_get(ENDPOINT_DICT['season_pace'].format(player_id,CURRENT_SEASON))
    return season_pace['stats'][0]['splits']


def sit_goals(player_id):
    sit_goals = http_get(ENDPOINT_DICT['sit_goals'].format(player_id,CURRENT_SEASON))
    return sit_goals['stats'][0]['splits'][0]


def day_split(player_id):
    day_split = http_get(ENDPOINT_DICT['day_split'].format(player_id,CURRENT_SEASON))
    return day_split['stats'][0]['splits']


def home_away_split(player_id):
    home_away_split = http_get(ENDPOINT_DICT['home_away_split'].format(player_id,CURRENT_SEASON))
    return home_away_split['stats'][0]['splits']


def win_loss_split(player_id):
    win_loss_split = http_get(ENDPOINT_DICT['win_loss_split'].format(player_id,CURRENT_SEASON))
    return win_loss_split['stats'][0]['splits']


def player_schedule(id):
    pass
    ## needs to look up the player's team and then pull the teams schedule for the player


## Services for Game class
##

def game_box(game_id):
    game_box = http_get(ENDPOINT_DICT['game_box'].format(game_id))
    return game_box['teams']


def game_live(game_id):
    game_live = http_get(ENDPOINT_DICT['game_live'].format(game_id))
    return game_live


## Services for Team class
##


def team_id():
    team_id = http_get(ENDPOINT_DICT['team_id'])
    return team_id['teams']


def team_schedule(team_id):
    team_schedule = http_get(ENDPOINT_DICT['team_schedule'].format(team_id, START_DATE, END_DATE))
    return team_schedule['dates']


def team_roster(team_id):
    team_roster = http_get(ENDPOINT_DICT['team_roster'].format(team_id))
    return team_roster['dates']


  


