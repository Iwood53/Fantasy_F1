class Driver:
    def __init__(self, p_first_name='', p_last_name='', p_team='', p_number=''):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.team = p_team
        self.number = p_number

    def __str__(self):
        return self.number + ' ' + self.first_name + ' ' + self.last_name


class Player:
    def __init__(self, p_name):
        self.name = p_name
        self.driver_list = []

    def __str__(self):
        return self.name


class Race:
    def __init__(self, p_name):
        self.name = p_name
        self.players = []
        self.drivers = []

    def __str__(self):
        return self.name

    def populate_driver_list(self):
        for line in open('driver_list.csv'):
            first_name, last_name, team, number = line.split(',')
            self.drivers.append(Driver(first_name, last_name, team, number.rstrip()))


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


race_name = raw_input('Enter Race Name: ')
race = Race(race_name)
race.populate_driver_list()

get_number = True
while get_number:
    num_players = raw_input('Enter number of players: ')
    if is_number(num_players):
        get_number = False
    else:
        print "Please enter a number"

for num in range(1, int(num_players)+1):
    question_string = 'Enter player ' + str(num) + ' name: '
    race.players.append(Player(raw_input(question_string)))

popable_driver_list = race.drivers

while len(popable_driver_list) > 0:
    for player in race.players:
        for driver in popable_driver_list:
            print driver
        driver_num = raw_input(player.name + ' choose a driver number:')
        for index, driver in enumerate(popable_driver_list):
            if driver.number == driver_num:
                player.driver_list.append(driver)
                popable_driver_list.pop(index)











