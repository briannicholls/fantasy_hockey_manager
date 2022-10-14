from API_serv import *
from Local_serv import *
from Team import *

print("Welcome to the Fantasy Hockey Manager's Helper \n")

#get all teams from API

teams = get_active_teams()

print(Team.all)

# select a team by name
Team.select_team("New Jersey Devils")
print("\n")
print("\n")

print(Team.current_team) 
print("\n")
print("\n")



###commented player information to reduce run-time while working on Teams
# #get all players from API

# players = get_active_players()

# #print of Class variables example

# print(Player.all)
# print("\n")
# print("\n")

# #print pf class variables example
# print(Player.player_count)
# print("\n")
# print("\n")




# #continue
# print("Please search for a player by name")