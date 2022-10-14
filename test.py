from Team import Team
import names

# add some teams
for i in range(1, 10):
  Team(i, {
    "name": 'Fake Team ' + str(i), 
  })



# select team by name
team_1 = Team.select_team('Fake Team 1')

print( team_1.roster[0]['person'])



