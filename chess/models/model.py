from tinydb import TinyDB
from chess.errors.error import birth_date_is_valid, date_tournament_is_valid, \
    gender_is_valid, text_is_alpha, number_is_valid


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.gender = gender.upper()
        try:
            self.ranking = int(ranking)
        except Exception:
            self.ranking = ranking
        self.id = (first_name[0].lower() + last_name.lower() + "_" + birth_date.replace("/", ""))

    def is_valid(self):
        result = 0
        try:
            if gender_is_valid(self.gender):
                result += 1
            if birth_date_is_valid(self.birth_date):
                result += 1
            if number_is_valid(self.ranking):
                result += 1
            if text_is_alpha(self.first_name) and text_is_alpha(self.last_name):
                result += 1
        except:
            pass

        return result


class Tournament:
    def __init__(self, name, venue, date, rounds, round_match, players, description):

        self.name = name
        self.venue = venue
        self.date = date
        try:
            self.rounds = int(rounds)
        except Exception:
            self.rounds = rounds
        self.round_match = round_match
        self.players = players
        self.description = description

    def is_valid(self):
        result = 0
        try:
            if text_is_alpha(self.name) and text_is_alpha(self.venue):
                result += 1
            if date_tournament_is_valid(self.date):
                result += 1
            if number_is_valid(self.rounds):
                result += 1
        except Exception:
            pass

        return result

    @property
    def define_time(self):
        print("Hello")


class Match:
    def __init__(self, players):
        self.players = players


class Round:
    def __init__(self, tour_number, matchs):
        self.tour_number = tour_number


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
