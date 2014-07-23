class Driver:
    def __init__(self, p_first_name, p_last_name, p_team, p_number):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.team = p_team
        self.number = p_number
        self.odds_to_win_top = 0
        self.odds_to_win_bottom = 0
        self.pole_position = 0

    def __str__(self):
        return self.last_name


def parse_paddy_power(driver_list):
    start_str = '<!-- start oddsTable -->'
    page_str = open('odds_page').read().split(start_str)
    page_str.pop(0)

    for driver in driver_list:
        for odds in page_str:
            if odds.find(str(driver)) > 0:
                print driver



drivers = []
for line in open("driver_list.csv"):
    first_name, last_name, team, number = line.split(',')
    drivers.append(Driver(first_name, last_name, team, number))

parse_paddy_power(drivers)






