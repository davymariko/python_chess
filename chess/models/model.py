from tinydb import TinyDB
import pprint
from time import sleep


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, score):
        self.first_name = first_name
        self.last_name = last_name
        self.date = birth_date
        self.gender = gender
        self.score = score
        self.id = (first_name[0].lower() + last_name.lower()+"_" + birth_date.replace("/", ""))

    # def is_valid(self):
    #     message = ""
    #     test_dat = self.score

    @property
    def record(self):

        return {
                    'id': self.id,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'birth_date': self.date,
                    'gender': self.gender,
                    'score': self.score
                }


class Tournoi:
    def __init__(self, name, venue, date, tours, tournee, players, description):

        self.name = name
        self.venue = venue
        self.date = date
        self.tours = tours
        self.tournee = tournee
        self.players = players
        self.description = description

    @property
    def define_time(self):
        print("Hello")


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


def players_list():
    database = TinyDB('database/db.json')
    players_table = database.table('players')

    return players_table.all()


def see_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    for play in players_table.all():
        print("\n-------------")
        pprint.pprint(play)


def delete_all_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    players_table.truncate()


# def delete_player():
#     database = TinyDB('database/db.json')
#     # players_table = database.table('players')
#     id = input(("Entrer l'id du joueur à effacer: "))
#     database.remove(where('id') == id)
#     print("Le joueur {id} a été effacé")


def number_players():
    database = TinyDB('database/db.json')
    players_table = database.table('players')
    return len(players_table.all())


def check_duplicates(table, player_info):
    check = 0
    for player in table.all():
        if (player['id'] == player_info['id']):
            print("\n**** Ce joueur existe déjà\n")
            check += 1
            break

    return check


def swiss_pair_generator():
    print("Paires générées pour ce tour: ")
    input("")


def launch_tournament():
    pass


# def play_record():
#     database = TinyDB('database/db.json')
#     play_records = database.table('record')


def test():
    database = TinyDB('database/db.json')
    test = database.table('players')

    print(test.all()[0]['id'])
