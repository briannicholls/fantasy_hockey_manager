#Use NHL API service to collect and update information about Players, Teams, Games, etc.
from cmd import IDENTCHARS
import json
import requests

def get_player(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}".format(id), params={"Content-Type": "application/json"})
    json_data = response.json()
    return json_data['people'][0]   
    # print(json_data)
    # print(json_data['people'][0]['fullName'])

from Constants import *


def get_game_log(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=gameLog&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    game_log = json_data['stats'][0]['splits']
    return game_log


def div_stats_split(id):
    response = requests.get("https://statsapi.web.nhl.com/api/v1/people/{}/stats?stats=vsDivision&season={}".format(id,CURRENT_SEASON), params={"Content-Type": "application/json"})
    json_data = response.json()
    div_stats = json_data['stats'][0]['splits']
    return div_stats
