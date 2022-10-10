from API_serv import *
class Team:
  all = []

  def __init__(self,ID,data):
    self.ID = ID
    self.data_from_teams = data
    # self.schedule = team_schedule(ID)

    self.roster = team_roster(ID)

    # self.details = http_get_team_details(ID)

    self.all.append(self)
    print("Team " + str(self.ID) + " Created")

  def __str__():
    print(self.ID)

  # todo: dont want to create duplicates
  def save(self):
    # self.all.append(self)
    # print("Team " + str(self.ID) + " Created")