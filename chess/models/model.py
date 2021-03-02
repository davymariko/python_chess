from chess.errors.error import birth_date_is_valid, date_tournament_is_valid, \
    gender_is_valid, text_is_alpha, number_is_valid


class Player():
    def __init__(self, first_name, last_name, birth_date, gender, ranking):
        try:
            self.first_name = first_name.capitalize()
            self.last_name = last_name.capitalize()
            self.gender = gender.upper()
        except Exception:
            self.first_name = first_name
            self.last_name = last_name
            self.gender = gender

        self.birth_date = birth_date

        try:
            self.ranking = int(ranking)
        except Exception:
            self.ranking = ranking
        try:
            self.id = (first_name[0].lower() + last_name.lower() + "_" + birth_date.replace("/", ""))
        except Exception:
            self.id = ""

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
        except Exception:
            pass

        return result


class Tournament:
    def __init__(self, name, venue, date, rounds, players, round_matchs, description):

        self.name = name
        self.venue = venue
        self.date = date
        try:
            self.rounds = int(rounds)
        except Exception:
            self.rounds = rounds
        self.players = players
        self.description = description
        self.round_matchs = round_matchs

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

    def players_in_list(self):
        players_list = []
        for player in self.players:
            player_record = {
                    'id': player.id,
                    'first_name': player.first_name,
                    'last_name': player.last_name,
                    'birth_date': player.birth_date,
                    'gender': player.gender,
                    'ranking': player.ranking
            }
            players_list.append(player_record)

        return players_list

    def matchs_to_list(self):
        matchs_list = []
        for match in self.round_matchs:
            matchs_dict = {
                'players': [match[0][0], match[1][0]],
                'score': [match[0][1], match[1][1]]
            }
            matchs_list.append(matchs_dict)

        return matchs_list


class Match:
    def __init__(self, players):
        self.players = players


class Round:
    def __init__(self, tour_number, matchs):
        self.tour_number = tour_number
        self.matchs = matchs
