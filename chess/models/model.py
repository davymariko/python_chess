from tinydb import TinyDB
from chess.errors.error import (birth_date_is_valid, date_tournament_is_valid, gender_is_valid, ranking_is_valid)


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.gender = gender.upper()
        self.ranking = ranking
        self.id = (first_name[0].lower() + last_name.lower()+"_" + birth_date.replace("/", ""))

    def is_valid(self):
        result = 0
        result = gender_is_valid(self.gender)
        result = birth_date_is_valid(self.birth_date)
        result = ranking_is_valid(self.ranking)
        input("")

        return result

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

    def is_valid(self):
        result = 0
        result = date_tournament_is_valid(self.date)
        input("")

        return result

    @property
    def define_time(self):
        print("Hello")


class match:
    def __init__(self, players):
        self.players = players


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
