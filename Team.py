from API_serv import *
class Team:
  def __init__(self,ID):
    self.ID = ID

    self.schedule = team_schedule(ID)

  