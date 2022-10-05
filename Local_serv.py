from API_serv import *


# Services for local handling


# generate a list of all team IDs

NHL_team_IDs = []

teams = team_IDs()

# use a team count for while loop iteration
team_count = 0

while team_count < 32:
    NHL_team_IDs.append(teams[team_count]['id'])
    team_count += 1

# generate a list of all players in the NHL currently
NHL_players = []







###

# print(NHL_team_IDs)
# print(len(NHL_team_IDs))

# print teams list
# print(teams)


# printing the first teams ID number
# print(teams[0]['id'])

# printing the first teams active status
# print(teams[0]['active'])