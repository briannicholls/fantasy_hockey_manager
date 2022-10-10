from API_serv import *

class Player:
  def __init__(self,ID):

    self.ID = ID

    self.attributes = get_player(self.ID)
    
    self.game_log = get_game_log(self.ID)

    self.season_stats = season_stat(self.ID)

    self.div_stats = div_split(self.ID)

    self.day_stats = day_split(self.ID)

    self.mon_stats = mon_split(self.ID)

    self.week_stats = week_split(self.ID)

    self.league_stats = league_stat(self.ID)

    self.season_pace = season_pace(self.ID)

    self.home_away_stats = home_away_split(self.ID)

    self.w_l_stats = win_loss_split(self.ID)

    self.sit_goals = sit_goals(self.ID)

    self.schedule = player_schedule(self.ID)

    
    



  def __str__(self):
    return "The Player is {}.".format(self.name)

