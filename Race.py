import Driver
import Player
import py_conf


class Race:
    def __init__(self, p_name):
        self.name = p_name
        self.players = []
        self.drivers = []
        self.point_scale = {'1': 25, '2': 18, '3': 15, '4': 12, '5': 10, '6': 8, '7': 6, '8': 4, '9': 2, '10': 1}

    def __str__(self):
        return self.name

    @staticmethod
    def is_number(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def populate_driver_list(self):
        for line in open(py_conf.driver_csv):
            first_name, last_name, team, number = line.split(',')
            self.drivers.append(Driver.Driver(first_name, last_name, team, number.rstrip()))

    def is_driver_num(self, driver_num):
        is_driver = False
        return_driver = Driver
        for driver in self.drivers:
            if driver.number == driver_num:
                return_driver = driver
                is_driver = True
                break
        return is_driver, return_driver

    def cmdln_pick_drivers(self):
        entered_num = False
        while entered_num is False:
            num_drivers = raw_input("How many drivers will each player pick?: ")
            if self.is_number(num_drivers):
                entered_num = True
                num_drivers = int(num_drivers)
        pop_drivers_list = self.drivers
        while num_drivers > 0:
            for player in self.players:
                picked_driver = False
                while picked_driver is False:
                    for driver in pop_drivers_list:
                        print driver.number + ' ' + driver.first_name + ' ' + driver.last_name
                    selection = raw_input(player.name + ' Select a driver by number: ')
                    is_driver_ret = Race.is_driver_num(self, selection)
                    if is_driver_ret[0] is True:
                        player.driver_list.append(is_driver_ret[1])
                        picked_driver = True
                        for index, pop_driver in enumerate(pop_drivers_list):
                            if is_driver_ret[1] == pop_driver:
                                pop_drivers_list.pop(index)
            num_drivers -= 1

    def cmdln_set_players(self):
        get_number = True
        while get_number:
            num_players = raw_input('Enter number of players: ')
            if Race.is_number(num_players):
                get_number = False
            else:
                print "Please enter a number"

        for num in range(1, int(num_players)+1):
            question_string = 'Enter player ' + str(num) + ' name: '
            self.players.append(Player.Player(raw_input(question_string)))

    def cmdln_show_player_selection(self):
        for player in self.players:
            print "\n" + player.name + ':'
            for driver in player.driver_list:
                print driver.number + ' ' + driver.first_name + ' ' + driver.last_name

