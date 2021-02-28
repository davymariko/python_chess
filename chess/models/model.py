from chess.view.view import print_pairs, clear, print_wrong_score
from chess.export.database import tournaments_list
from chess.errors.error import birth_date_is_valid, date_tournament_is_valid, \
    gender_is_valid, text_is_alpha, number_is_valid, score_input


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

    def generate_pairs(self, current_round):
        total_players = len(self.players)
        pairs_list = []
        sorted_players = []
        if current_round == 1:
            pairing = 0
            players = self.players_in_list()
            sorted_players = sorted(players, key=lambda players: players.get('ranking', {}))
            while pairing < (total_players/2):
                versus = pairing+int(total_players/2)
                pairs_list.append([sorted_players[pairing]['id'], sorted_players[versus]['id']])
                pairing += 1
        else:
            sorted_players = self.order_by_score_ranking(self.score_per_player())
            unmatched_players = [player[0] for player in sorted_players]
            for player_index in range(0, total_players-1):
                versus = player_index + 1
                player1 = sorted_players[player_index][0]
                player2 = sorted_players[versus][0]
                check_pair = 0
                while check_pair < 1:
                    if player1 in unmatched_players:
                        if (player2 in unmatched_players and
                                not_played_with(self.list_of_played_with(), player1, player2)):
                            pairs_list.append([player1, player2])
                            unmatched_players.remove(player1)
                            unmatched_players.remove(player2)
                            check_pair = 1
                        else:
                            versus += 1
                            player2 = sorted_players[versus][0]
                    else:
                        check_pair = 1
        
        return pairs_list

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

    def matchs_to_dict(self):
        for match in self.round_matchs:
            matchs_dict = {
                'players': [match[0][0], match[1][0]],
                'score': [match[0][1], match[1][1]]
            }
        
        return matchs_dict

    def score_per_player(self,):
        matchs = self.matchs_to_dict()
        score_dict = {}
        for match in matchs:
            try:
                score_dict[match['players'][0]] += float(match['score'][0])
            except Exception:
                score_dict[match['players'][0]] = float(match['score'][0])

            try:
                score_dict[match['players'][1]] += float(match['score'][1])
            except Exception:
                score_dict[match['players'][1]] = float(match['score'][1])

        return score_dict

    def order_by_score_ranking(self, score_per_player):
        list_player_by_stats = []
        for player_id in score_per_player:
            ranking = [x['ranking'] for x in self.players_in_list() if x['id'] == player_id]
            list_player_by_stats.append([player_id, score_per_player[player_id], ranking[0]])
        players_sorted_by_stats = sorted(list_player_by_stats, key=lambda x: (x[1], -x[2]), reverse=True)

        return players_sorted_by_stats

    def list_of_played_with(self):
        matchs = self.matchs_to_dict()
        played_with_dict = {}
        for match in matchs:
            try:
                played_with_dict[match['players'][0]].append(match['players'][1])
            except Exception:
                played_with_dict[match['players'][0]] = [match['players'][1]]

            try:
                played_with_dict[match['players'][1]].append(match['players'][0])
            except Exception:
                played_with_dict[match['players'][1]] = [match['players'][0]]

        return played_with_dict

class Match:
    def __init__(self, players):
        self.players = players

class Round:
    def __init__(self, tour_number, matchs):
        self.tour_number = tour_number
        self.matchs = matchs


# def test():
#     database = TinyDB('database/db.json')
#     test = database.table('players')

#     print(test.all()[0]['id'])


def not_played_with(played_with_dict, player1, player2):
    if player2 not in played_with_dict[player1]:
        return True
    else:
        return False
