import py_conf
import urllib2
import Driver


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


def generate_pick_order(driver_list):
    driver_odds = []
    for driver in driver_list:
        if driver.odds_to_win_den > 0:
            odds = float(driver.odds_to_win_num) / float(driver.odds_to_win_den)
        else:
            odds = float(11111)
        driver_odds.append([driver.last_name, odds, int(driver.pole_position)])

    driver_odds.sort(key=lambda row: row[2])
    driver_odds.sort(key=lambda row: row[1])

    final_driver_list = []
    for index, driver in enumerate(driver_odds):
        final_driver_list.append([index+1, driver[0]])

    return final_driver_list


def populate_pole_pos(driver_list, pole_positions_csv):
    poles = []
    for line in open(pole_positions_csv):
        pole, driver_name = line.split(',')
        poles.append([pole, driver_name])

    for pole in poles:
        for driver in driver_list:
            if pole[1].strip() == driver.last_name:
                driver.pole_position = pole[0]

    return driver_list


def generate_driver_list(drivers_csv, pole_positions_csv):
    drivers = []
    for line in open(drivers_csv):
        first_name, last_name, team, number = line.split(',')
        drivers.append(Driver.Driver(first_name, last_name, team, number))

    drivers = populate_pole_pos(drivers, pole_positions_csv)

    return drivers


def parse_paddy_power(driver_list, url):
    start_str = '<!-- start oddsTable -->'
    response = urllib2.urlopen(url)
    page_str = response.read().split(start_str)

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

    return driver_list


def go(url):
    driver_list = generate_driver_list(py_conf.driver_csv, py_conf.pole_pos_csv)
    driver_list = parse_paddy_power(driver_list, url)
    pick_order = generate_pick_order(driver_list)
    return pick_order
