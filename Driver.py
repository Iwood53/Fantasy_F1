class Driver:
    def __init__(self, p_first_name, p_last_name, p_team, p_number):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.team = p_team
        self.number = p_number
        self.odds_to_win_num = 0
        self.odds_to_win_den = 0
        self.pole_position = 0

    def __str__(self):
        return self.last_name
