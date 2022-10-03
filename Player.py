class Player:
  def __init__(self,ID):
    self.ID = ID
    self.attributes = API_serve.get_player(self.ID)
    self.stats = 
  def __str__(self):
    return "The Player {}.".format(self.name)

