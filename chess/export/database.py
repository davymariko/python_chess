from tinydb import TinyDB


class Database:
    def __init__(self):
        self.tournaments_db = 'database/tournaments.json'
        self.temporary_db = 'database/temporary.json'

    def initiate_player_table(self):
        database = TinyDB(self.temporary_db)
        table = database.table('players')

        return table

    def initiate_round_table(self):
        database = TinyDB(self.temporary_db)
        table = database.table('game')

        return table

    def initiate_tournament_table(self):
        database = TinyDB(self.tournaments_db)
        table = database.table('tournament')

        return table

    def initiate_unfinished_tournament_table(self):
        database = TinyDB(self.temporary_db)
        table = database.table('tournament')

        return table

    def save_player(self, player):
        player_record = {
            'id': player.id,
            'first_name': player.first_name,
            'last_name': player.last_name,
            'birth_date': player.birth_date,
            'gender': player.gender,
            'ranking': player.ranking
        }

        players_table = self.initiate_player_table()
        players_table.insert(player_record)

    def save_rounds(self, match_info):
        match_table = self.initiate_round_table()
        for match in match_info:
            match_dict = {
                "players": [match[0][0], match[1][0]],
                "score": [float(match[0][1]), float(match[1][1])]
            }
            match_table.insert(match_dict)

    def save_tournament(self, tournament):
        tournament_table = self.initiate_tournament_table()

        tournament_info = {
            'name': tournament.name,
            'venue': tournament.venue,
            'date': tournament.date,
            'rounds': tournament.rounds,
            'players': tournament.players_in_list(),
            'description': tournament.description,
            'round_matchs': tournament.round_matchs
        }

        tournament_table.insert(tournament_info)

    def pre_save_tournament(self, tournament):
        tournament_table = self.initiate_unfinished_tournament_table()

        tournament_info = {
            'name': tournament.name,
            'venue': tournament.venue,
            'date': tournament.date,
            'rounds': tournament.rounds,
            'description': tournament.description
        }

        tournament_table.insert(tournament_info)

    def delete_all_players(self):
        players_table = self.initiate_player_table()
        players_table.truncate()

    def delete_all_matchs(self):
        rounds_table = self.initiate_round_table()
        rounds_table.truncate()

    def delete_existing_tournament(self):
        tournament_table = self.initiate_unfinished_tournament_table()
        tournament_table.truncate()
        self.delete_all_players()
        self.delete_all_matchs()


# # Linear programming
# def initiate_player_table():
#     database = TinyDB('database/temporary.json')
#     table = database.table('players')

#     return table


# def initiate_round_table():
#     database = TinyDB('database/temporary.json')
#     table = database.table('game')

#     return table


# def initiate_tournament_table():
#     database = TinyDB('database/tournaments.json')
#     table = database.table('tournament')

#     return table


# def initiate_unfinished_tournament_table():
#     database = TinyDB('database/temporary.json')
#     table = database.table('tournament')

#     return table


# def save_player(player):
#     player_record = {
#         'id': player.id,
#         'first_name': player.first_name,
#         'last_name': player.last_name,
#         'birth_date': player.birth_date,
#         'gender': player.gender,
#         'ranking': player.ranking
#     }

#     players_table = initiate_player_table()
#     players_table.insert(player_record)


# def save_rounds(match_info):
#     match_table = initiate_round_table()
#     for match in match_info:
#         match_dict = {
#             "players": [match[0][0], match[1][0]],
#             "score": [float(match[0][1]), float(match[1][1])]
#         }
#         match_table.insert(match_dict)


# def save_tournament(tournament):
#     tournament_table = initiate_tournament_table()

#     tournament_info = {
#         'name': tournament.name,
#         'venue': tournament.venue,
#         'date': tournament.date,
#         'players': tournament.players_in_list(),
#         'rounds': tournament.rounds,
#         'round_matchs': tournament.round_matchs,
#         'description': tournament.description
#     }

#     tournament_table.insert(tournament_info)


# def pre_save_tournament(tournament):
#     tournament_table = initiate_unfinished_tournament_table().all

#     tournament_info = {
#         'name': tournament.name,
#         'venue': tournament.venue,
#         'date': tournament.date,
#         'description': tournament.description,
#         'players': tournament.players_in_list(),
#         'rounds': tournament.rounds,
#         'round_matchs': tournament.round_matchs
#     }

#     tournament_table.insert(tournament_info)


# def players_list():

#     return initiate_player_table().all()


# def matchs_list():

#     return initiate_round_table().all()


# def tournaments_list():

#     return initiate_tournament_table().all()


# def players_number():

#     return len(initiate_player_table())


# def delete_all_players():
#     players_table = initiate_player_table()
#     players_table.truncate()


# def delete_all_matchs():
#     rounds_table = initiate_round_table()
#     rounds_table.truncate()
