from tinydb import TinyDB


def initiate_player_table():
    database = TinyDB('database/db.json')
    table = database.table('players')

    return table


def initiate_game_table():
    pass


def initiate_tournament_table():
    pass


def delete_all_players():
    players_table = initiate_player_table()
    players_table.truncate()
