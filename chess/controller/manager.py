from time import sleep
from chess.view.view import clear, print_preview, display_players, print_tournament_pre_launch, \
    print_pairs, print_player_to_rank, print_create_players, print_tournaments_report, \
    print_tournament_matchs, print_tournament_rounds
from chess.errors.error import score_input
from chess.models.model import Player, Tournament
from chess.export.database import Database

database = Database()


class ManageTournament:
    def tournament(self):

        if len(database.initiate_unfinished_tournament_table().all()) > 0:
            tournament = self.load_existing_tournament()
        else:
            info_input = self.enter_tournament_info()
            if info_input == 0:
                return 1
            else:
                tournament = info_input
                # tournament = self.enter_players(tournament)

        tournament = self.alternative_entry(tournament)

        check_launch = True
        while check_launch:
            clear()
            print_tournament_pre_launch(tournament)
            if len(tournament.players) == 8:
                print_preview(109)
                players_choice = input("\n>>> ")
            else:
                print_preview(110)
                players_choice = input("\n>>> ")

            if players_choice == "1" and len(tournament.players) == 8:
                played_rounds = int(len(database.initiate_round_table().all()) / 4)
                for current_round in range(1 + played_rounds, tournament.rounds + 1):
                    clear()
                    pairs = self.generate_pairs(tournament, current_round)
                    tournament = self.enter_score(pairs, tournament, current_round)
                    check_exit = True
                    check = False
                    while check_exit:
                        print_preview(123)
                        choice_in_round = input(">>> ")
                        if choice_in_round == "1":
                            check_exit = False
                        elif choice_in_round == "0":
                            check_exit = False
                            check = True
                        else:
                            print_preview(111)
                        clear()
                    if check:
                        break

                if len(tournament.round_matchs) == 16:
                    print_preview(106)
                    sleep(2)
                    check_launch = False

            elif players_choice == "1" and len(tournament.players) < 8:
                check_players = self.enter_players(tournament)
                if check_players == 0:
                    pass
                else:
                    for player in tournament.players:
                        tournament.players.append(player)
            elif players_choice == "2":
                self.print_players(tournament.players_in_list())
            elif players_choice == "3":
                tournament = self.set_ranking(tournament)
            elif players_choice == "4":
                check_launch = False
            else:
                print_preview(111)
                input("")
        if len(tournament.players) == 8 and len(tournament.round_matchs) == 16:
            tournament = self.set_ranking(tournament)
            database.save_tournament(tournament)
            database.delete_existing_tournament()

        return 0

    def enter_tournament_info(self):
        check = True
        while check:
            clear()
            print_preview(105)
            tournament_name = input("Nom du tournoi: ")
            venue = input("Lieu: ")
            tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
            rounds = input("Nombre de tours du tournoi: ")
            if len(rounds) == 0:
                rounds = 4
            description = input("Description: ")
            tournament = Tournament(tournament_name, venue, tournament_date, rounds, [], [], description)

            print_preview(114)
            verify = input("\n>>> ")
            if verify == "1":
                if tournament.is_valid() == 3:
                    database.pre_save_tournament(tournament)
                    check = False
                else:
                    input("")
            elif verify == "2":
                pass
            elif verify == "3":
                return 0
            else:
                print_preview(111)
                print_preview(102)
                input("")

        return tournament

    def enter_players(self, tournament):
        print_preview(104)
        sleep(1)
        taken_seat = len(tournament.players)
        remaining = 8 - taken_seat
        while (taken_seat < remaining):
            clear()
            available_seats = 8 - len(tournament.players)
            print_create_players(available_seats)
            first_name = input("Prénom: ")
            last_name = input("Nom: ")
            birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
            ranking = input("Classement: ")
            gender = input("Sexe(H ou F): ")
            print_preview(114)
            verify = input("\n>>> ")
            if verify == '1':
                player = Player(first_name, last_name, birth_date, gender, ranking)
                if player.is_valid() == 4:
                    if not self.check_player_exists(tournament.players, player):
                        tournament.players.append(player)
                        database.save_player(player)
                        taken_seat = len(tournament.players)
                else:
                    input("")
            elif verify == '2':
                pass
            elif verify == '3':
                break

        return tournament

    def generate_pairs(self, tournament, current_round):
        total_players = len(tournament.players)
        pairs_list = []
        sorted_players = []
        if current_round == 1:
            pairing = 0
            players = tournament.players_in_list()
            sorted_players = sorted(players, key=lambda players: players.get('ranking', {}))
            while pairing < (total_players/2):
                versus = pairing+int(total_players/2)
                pairs_list.append([sorted_players[pairing]['id'], sorted_players[versus]['id']])
                pairing += 1
        else:
            sorted_players = self.order_by_score_ranking(tournament, self.score_per_player(tournament))
            unmatched_players = [player[0] for player in sorted_players]
            player_index = 0
            while player_index < total_players - 1:
                versus = player_index + 1
                player1 = sorted_players[player_index][0]
                player2 = sorted_players[versus][0]
                check_pair = True
                while check_pair:
                    if player1 in unmatched_players:
                        if (player2 in unmatched_players and
                                self.not_played_with(self.list_of_played_with(tournament), player1, player2)):
                            pairs_list.append([player1, player2])
                            unmatched_players.remove(player1)
                            unmatched_players.remove(player2)
                            check_pair = False
                        else:
                            versus += 1
                            player2 = sorted_players[versus][0]
                    else:
                        check_pair = False
                player_index += 1

        return pairs_list

    def enter_score(self, pairs_list, tournament, tour_level):
        check = True
        while check:
            clear()
            print_pairs(pairs_list, tournament.players_in_list(), tour_level)
            print_preview(108)
            for match in range(0, len(pairs_list)):
                score = input(f"Match {match + 1}. >>> ")
                if score_input(score) == 1:
                    print_preview(107)
                    input("")
                    break
                else:
                    tournament.round_matchs.append(([pairs_list[match][0], float(score.split("-")[0])],
                                                    [pairs_list[match][1], float(score.split("-")[1])]))
                    check = False

            database.save_rounds(tournament.round_matchs)

        return tournament

    def set_ranking(self, tournament):
        for index in range(0, len(tournament.players)):
            check = True
            while check:
                clear()
                print_preview(112)
                print_player_to_rank(tournament.players[index])
                ranking = input("\nNouveau classement >>> ")
                try:
                    if len(ranking) == 0:
                        check = False
                    else:
                        tournament.players[index].ranking = int(ranking)
                        check = False
                except Exception:
                    print_preview(113)
                    input("")

        return tournament

    def print_players(self, players_list):
        if len(players_list) == 0:
            print_preview(124)
            input("")
            return
        check = True
        while check:
            clear()
            print_preview(125)
            order_choice = input("\n>>> ")
            sorted_dict = []
            if order_choice == "1":
                sorted_dict = sorted(players_list, key=lambda players: players.get('last_name', {}))
            elif order_choice == "2":
                sorted_dict = sorted(players_list, key=lambda players: players.get('ranking', {}))
            elif order_choice == "3":
                sorted_dict = sorted(players_list, key=lambda players: players.get('last_name', {}), reverse=True)
            elif order_choice == "4":
                sorted_dict = sorted(players_list, key=lambda players: players.get('ranking', {}), reverse=True)
            elif order_choice == "5":
                break
            else:
                print_preview(111)

            display_players(sorted_dict)

    def print_players_by_tournament(self, tournaments_list, choice):
        self.print_players(tournaments_list[choice-1]["players"])

    def print_all_players(self, tournament_list):
        all_players_list = []
        for tournament in tournament_list:
            for player in tournament["players"]:
                all_players_list.append(player)

        self.print_players(all_players_list)

    def check_existing_tournament(self):
        check = True
        while check:
            clear()
            if len(database.initiate_unfinished_tournament_table().all()) == 0:
                return False
            else:
                print_preview(119)
                choice = input(("\n>>> "))
                if choice.lower() == "o" or choice.lower() == "oui":
                    database.delete_existing_tournament()
                    return False
                elif choice.lower() == "n" or choice.lower() == "non":
                    return True
                else:
                    print_preview(111)
                    input("")

    def check_player_exists(self, players_list, player):
        if len(players_list) == 0:
            return False
        else:
            for existing in players_list:
                try:
                    if player.id == existing.id:
                        print_preview(120)
                        input("")
                        return True
                    else:
                        return False
                except Exception:
                    return False

    def score_per_player(self, tournament):
        matchs = tournament.matchs_to_list()
        score_dict = {}
        for match in matchs:
            try:
                score_dict[match['players'][0]] += match['score'][0]
            except Exception:
                score_dict[match['players'][0]] = match['score'][0]

            try:
                score_dict[match['players'][1]] += match['score'][1]
            except Exception:
                score_dict[match['players'][1]] = match['score'][1]

        return score_dict

    def order_by_score_ranking(self, tournament, score_per_player):
        list_player_by_stats = []
        for player_id in score_per_player:
            ranking = [x['ranking'] for x in tournament.players_in_list() if x['id'] == player_id]
            list_player_by_stats.append([player_id, score_per_player[player_id], ranking[0]])
        players_sorted_by_stats = sorted(list_player_by_stats, key=lambda x: (x[1], -x[2]), reverse=True)

        return players_sorted_by_stats

    def list_of_played_with(self, tournament):
        matchs = tournament.matchs_to_list()
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

    def not_played_with(self, played_with_dict, player1, player2):
        if player2 not in played_with_dict[player1]:
            return True
        else:
            return False

    def report(self):
        check_report = True
        tournaments_list = database.initiate_tournament_table().all()
        while check_report:
            clear()
            print_preview(115)
            choice = input('\n>>> ')

            if choice == "1":
                print_tournaments_report(tournaments_list)
                print_preview(102)
                input("")
            elif choice == "2":
                self.players_report(tournaments_list)
            elif choice == "3":
                self.matchs_report(tournaments_list)
            elif choice == "4":
                self.rounds_report(tournaments_list)
            elif choice == "5":
                check_report = False
            else:
                print_preview(111)
                input("")

    def players_report(self, tournaments_list):
        check_report = True
        while check_report:
            clear()
            print_preview(117)
            choice = input('\n>>> ')
            if choice == "1":
                self.print_all_players(tournaments_list)
            elif choice == "2":
                self.choose_tournament(tournaments_list)
            elif choice == "3":
                check_report = False
            else:
                print_preview(111)
                input("")

    def matchs_report(self, tournaments_list):
        check_report = True
        while check_report:
            clear()
            print_tournaments_report(tournaments_list)
            print_preview(116)
            try:
                choice = int(input('\n>>> '))
                if choice == 0:
                    check_report = False
                elif choice < (len(tournaments_list) + 1) and choice > 0:
                    clear()
                    print_tournament_matchs(tournaments_list[choice-1])
                else:
                    print_preview(111)
                    input("")
            except Exception:
                print_preview(111)
                input("")

    def rounds_report(self, tournaments_list):
        check_report = True
        while check_report:
            clear()
            print_tournaments_report(tournaments_list)
            print_preview(116)
            try:
                choice = int(input('\n>>> '))
                if choice == 0:
                    check_report = False
                elif choice < (len(tournaments_list) + 1) and choice > 0:
                    clear()
                    print_tournament_rounds(tournaments_list[choice-1])
                else:
                    print_preview(111)
                    input("")
            except Exception:
                print_preview(111)
                input("")

    def choose_tournament(self, tournament_list):
        check = True
        while check:
            clear()
            print_tournaments_report(tournament_list)
            print_preview(116)
            try:
                choice = int(input('\n>>> '))
                if choice == 0:
                    check = False
                elif choice <= len(database.initiate_tournament_table().all()) and choice > 0:
                    self.print_players_by_tournament(tournament_list, choice)
                else:
                    print_preview(111)
                    input("")
            except Exception:
                print_preview(111)
                input("")

    def load_existing_tournament(self):
        tournament_data = database.initiate_unfinished_tournament_table().all()[0]

        tournament = Tournament(tournament_data["name"], tournament_data["venue"], tournament_data["date"],
                                tournament_data["rounds"], [], [], tournament_data["description"])

        if len(database.initiate_player_table().all()) != 0:
            for player in database.initiate_player_table().all():
                player_object = Player(player["first_name"], player["last_name"], player["birth_date"],
                                       player["gender"], player["ranking"])
                tournament.players.append(player_object)

        if len(tournament.players) == 8:
            for match in database.initiate_round_table().all():
                tournament.round_matchs.append(([match["players"][0], match["score"][0]],
                                                [match["players"][1], match["score"][1]]))

        return tournament

    def alternative_entry(self, tournament):

        player_auto = [["Davy", "Nimbona", "19/06/1995", 1, "H"], ["Marie", "Hautot", "10/06/1993", 2, "F"],
        ["Guy", "Nimbona", "01/12/1996", 3, "H"], ["Carelle", "Mugisha", "29/01/1994", 4, "F"],
        ["Junkers", "Ntwari", "18/03/1994", 5, "H"], ["Gretta", "Nkanagu", "30/08/1995", 6, "F"],
        ["Orlando", "Nkurunziza", "08/05/1996", 7, "H"], ["Lorraine", "Bafutwabo", "18/08/1995", 8, "F"]]

        # player_auto = [["Olivier", "Nimbona", "10/12/1994", 1, "H"], ["Ange", "Tuyizere", "19/02/1999", 2, "F"],
        #                 ["Lydia", "Hakizimana", "26/07/1983", 3, "F"], ["Jocelin", "Ntungane", "14/03/1997", 4, "H"],
        #                 ["Kessia", "Ntibibuka", "03/02/1997", 5, "F"], ["Arno", "Rwasa", "04/04/1994", 6, "H"],
        #                 ["Orlando", "Nkurunziza", "08/05/1996", 7, "H"], ["Vanessa", "Uwase", "04/03/1995", 8, "F"]]

        list_temp = []
        for play in player_auto:
            player = Player(play[0], play[1], play[2], play[4], play[3])
            database.save_player(player)

            list_temp.append(player)

        # list_temp = []
        # for play in players_list():
        #     player = Player(play["first_name"], play["last_name"], play["birth_date"],
        #                     play["gender"], play["ranking"])

        #     list_temp.append(player)

        tournament.players = list_temp

        return tournament

        # pass
