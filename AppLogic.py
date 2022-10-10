from API_serv import *
from Local_serv import *
from Team import *

print("Welcome to the Fantasy Hockey Manager's Helper \n")

#get all teams by ID in list

all_teams = get_active_teams()

print(all_teams)

#instatiate all teams
active_players = []

# roster = Team(all_teams[0])
# print (roster.roster)


for id in all_teams:
    team = Team(id)
    for player in team.roster:
        active_players.append(player)
    

# print(len(active_players))
# print(active_players[826])






print("Please search for a player by name")