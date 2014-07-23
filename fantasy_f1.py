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


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def isolate_num(line_str):
    final_num = []
    for char in line_str:
        if is_number(char):
            final_num.append(char)
    final_num_string = "".join(str(x) for x in final_num)
    return final_num_string


def parse_paddy_power(driver_list):
    start_str = '<!-- start oddsTable -->'
    page_str = open('odds_page').read().split(start_str)
    #page_str.pop(0)

    for driver in driver_list:
        for odds in page_str:
            if odds.find(str(driver)) > 0:
                split_lines = odds.split('\n')

                for odds_line in split_lines:
                    if odds_line.find('lp_num') > 0:
                        odds_num = isolate_num(odds_line)
                        break

                for odds_line in split_lines:
                    if odds_line.find('lp_den') > 0:
                        odds_den = isolate_num(odds_line)
                        break

                if odds_num != '' and odds_den != '':
                    driver.odds_to_win_num = odds_num
                    driver.odds_to_win_den = odds_den

    for driver in driver_list:
        print driver.last_name
        print driver.odds_to_win_num
        print driver.odds_to_win_den


drivers = []

for line in open("driver_list.csv"):
    first_name, last_name, team, number = line.split(',')
    drivers.append(Driver(first_name, last_name, team, number))


parse_paddy_power(drivers)


