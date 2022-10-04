class Player:
  def __init__(self,ID):

    self.ID = ID

    self.attributes = API_serv.get_player(self.ID)
    
    self.game_log = API_serv.get_game_log(self.ID)

    self.season_stats = API_serv.single_season_stat(self.ID)

    self.div_stats = API_serv.div_stat_split(self.ID)

    self.mon_stats = API_serv.mon_stat_split(self.ID)

    self.week_stats = API_serv.week_stat_split(self.ID)

    self.league_stats = API_serv.vs_league_stat(self.ID)

    self.reg_pace = API_serv.reg_season_pace(self.ID)

    self.home_away_stats = API_serv.home_away_split(self.ID)

    self.w_l_stats = API_serv.w_l_split(self.ID)
    



  def __str__(self):
    return "The Player is {}.".format(self.name)

