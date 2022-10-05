from API_serv import *
class Game:
  def __init__(self,ID):
    self.ID = ID

    self.box = game_box(ID)

    self.all_data = game_live(ID)

    