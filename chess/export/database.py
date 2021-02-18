from tinydb import TinyDB


def initiate_player_table():
    database = TinyDB('database/players.json')
    table = database.table('players')

    return table


def initiate_match_table():
    database = TinyDB('database/matchs.json')
    table = database.table('game')

    return table


def initiate_tournament_table():
    pass


def save_player(player_dict):
    players_table = initiate_player_table()
    result = check_player_duplicates(players_table, player_dict)
    if result == 1:
        print("réessayer avec un autre joueur")
        input("")
    else:
        players_table.insert(player_dict)

    return result


def save_match(match_info):
    pass


def players_list():

    return initiate_player_table().all()


def players_number():

    return len(initiate_player_table())


def delete_all_players():
    players_table = initiate_player_table()
    players_table.truncate()
    print("\nTous les joueurs ont été effacés")


def check_player_duplicates(table, player_info):
    check = 0
    for player in table.all():
        if (player['id'] == player_info['id']):
            print("\n**** Ce joueur existe déjà\n")
            check += 1
            break

    return check
