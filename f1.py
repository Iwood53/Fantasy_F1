import Player
import Driver
import Race
import gen_pick_list
import py_conf

options = '\nFantasy Formula-1\n'
options += '\n1 - Generate Best Pick Order'
options += '\n2 - Play Game(no live scoring)'
options += '\n\nSelect an Option: '

selection = raw_input(options)

if selection == '1':
    pick_list = gen_pick_list.go(py_conf.paddy_power_url)
    for driver in pick_list:
        print driver
    raw_input()

if selection == '2':
    race = Race.Race('race')
    race.populate_driver_list()
    race.cmdln_set_players()
    race.cmdln_pick_drivers()
    race.cmdln_show_player_selection()
    raw_input()

