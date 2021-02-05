from tinydb import TinyDB
from chess.errors.error import (birth_date_is_valid, gender_is_valid)


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.gender = gender.upper()
        self.ranking = ranking
        self.id = (first_name[0].lower() + last_name.lower()+"_" + birth_date.replace("/", ""))

    def is_valid(self):
        if gender_is_valid(self.gender) == 0 and birth_date_is_valid(self.birth_date) == 0:
            return 0
        else:
            return 1

    @property
    def record(self):

        return {
                    'id': self.id,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'birth_date': self.birth_date,
                    'gender': self.gender,
                    'ranking': self.ranking
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


# def delete_player():
#     database = TinyDB('database/db.json')
#     # players_table = database.table('players')
#     id = input(("Entrer l'id du joueur à effacer: "))
#     database.remove(where('id') == id)
#     print("Le joueur {id} a été effacé")


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
