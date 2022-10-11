from functools import reduce
import operator 
from API_serv import *
from Player import *
from Team import Team
#########################################################################################
# Services for local handling
#########################################################################################
### generate a list of all team IDs
#########################################################################################
### generate a list of all players (dictionaries)

def get_active_teams():
    # get all active team IDs
    NHL_team_IDs = []
    teams = team_id()

    for team in teams:
        # breakpoint()
        this_team = Team(team['id'])


    def fetch_team_id(team):
        return team['id']

    return map(fetch_team_id, Team.all)
        # team_count = 0

        # while team_count < 32:
        #     NHL_team_IDs.append(teams[team_count]['id'])
        #     team_count += 1
        # return NHL_team_IDs

### moved to app logic to call from Class: Team
# def get_active_players():
#     # generate a list of all active players
#     NHL_players = []

#     for team in NHL_team_IDs:
#         roster = team_roster(team)
#         for player in roster: 
#             player_array = player['person']
#             # print(player_array)
#             NHL_players.append(player_array)
#     return NHL_players

  
## instantiate the class Player

# selected_player = Player(NHL_players[0]['id'])

# print(selected_player.attributes)

get_active_teams()