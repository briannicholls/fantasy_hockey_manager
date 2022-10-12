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
    print("Team " + str(self.ID) +f" - {self.data_from_teams['name']}" + " Created")

  def __str__():
    print(self.ID)

  # todo: dont want to create duplicates
  def save(self):
    pass
    # self.all.append(self)
    # print("Team " + str(self.ID) + " Created")


  @classmethod
  def find_team(cls, name, birth_year):
    # calculate age an set it as a age
    # return new object
    return cls(name, date.today().year - birth_year)
