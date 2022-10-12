from API_serv import *
from Local_serv import *
from Team import *

print("Welcome to the Fantasy Hockey Manager's Helper \n")

#get all teams from API

teams = get_active_teams()

print(Team.all)

#get all players from API

players = get_active_players()

#print of Class variables example

print(Player.all[0])

print(Player.player_count)





print("\n")
print("Please search for a player by name")