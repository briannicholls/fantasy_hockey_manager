class Game:
  def __init__(self,ID):
    self.ID = ID

    self.box = APIserv.game_box(ID)

    self.all_data = APIserv.game_live(ID)

    