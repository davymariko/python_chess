from tinydb import TinyDB


def initiate_player_table():
    database = TinyDB('database/players.json')
    table = database.table('players')

    return table


def initiate_round_table():
    database = TinyDB('database/tours.json')
    table = database.table('game')

    return table


def initiate_tournament_table():
    database = TinyDB('database/tournaments.json')
    table = database.table('tournament')

    return table


def save_player(player_dict):
    players_table = initiate_player_table()
    result = check_player_duplicates(players_table, player_dict)
    if result == 1:
        print("réessayer avec un autre joueur")
        input("")
    else:
        players_table.insert(player_dict)

    return result


def save_rounds(match_info):
    match_table = initiate_round_table()
    for match in match_info:
        match_dict = {
            "players": match[0],
            "score": [float(match[1][0]), float(match[1][1])]
        }
        match_table.insert(match_dict)


def save_tournament(tournament):
    tournament_info = {
        'name': tournament.name,
        'venue': tournament.venue,
        'date': tournament.date,
        'rounds': tournament.tours,
        'round_matchs': tournament.round_matchs
    }
    tournament_table = initiate_tournament_table()
    tournament_table.insert(tournament_info)


def players_list():

    return initiate_player_table().all()


def matchs_list():

    return initiate_round_table().all()


def tournaments_list():

    return initiate_tournament_table()


def players_number():

    return len(initiate_player_table())


def delete_all_players():
    players_table = initiate_player_table()
    players_table.truncate()


def delete_all_matchs():
    rounds_table = initiate_round_table()
    rounds_table.truncate()


def check_player_duplicates(table, player_info):
    check = 0
    for player in table.all():
        if (player['id'] == player_info['id']):
            print("\n**** Ce joueur existe déjà\n")
            check += 1
            break

    return check
