from tinydb import TinyDB
import pprint
from time import sleep


def save_player(player_dict):
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    result = check_duplicates(players_table, player_dict)
    if result == 1:
        print("réessayer avec un autre joueur")
        sleep(2)
    else:
        players_table.insert(player_dict)

    return result


def see_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    for play in players_table.all():
        print("\n-------------")
        pprint.pprint(play)


def delete_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    players_table.truncate()


def number_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    return len(players_table.all())


def check_duplicates(table, player_info):
    check = 0
    for player in table.all():
        if (player['first_name'] == player_info['first_name'] and
                player['last_name'] == player_info['last_name']):
            print("\n**** Ce joueur existe déjà\n")
            check += 1
            break

    return check
