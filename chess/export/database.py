from tinydb import TinyDB


def initiate_database():
    database = TinyDB('database/db.json')
    table = database.table('players')

    return table


def delete_all_players():
    players_table = initiate_database()
    players_table.truncate()
