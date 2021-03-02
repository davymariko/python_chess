from time import sleep
from chess.view.view import clear, print_preview, print_players, print_tournament_pre_launch, \
    print_pairs, print_player_to_rank, print_create_players
from chess.errors.error import score_input, check_player_duplicates, number_is_valid
from chess.models.model import Player, Tournament, Round
from chess.export.database import save_player, delete_all_players, save_rounds, \
    matchs_list, delete_all_matchs, tournaments_list, save_tournament


def start():
    check = 0
    while check < 1:
        clear()
        print_preview(101)
        game_choice = input(("\n>>> "))
        if game_choice == "1":
            check_tournament = 0
            while check_tournament < 1:
                if tournament() == 0:
                    break
                else:
                    pass
        elif game_choice == "2":
            clear()
            existing_tournament()
        elif game_choice == "3":
            clear()
            tournament_report()
        elif game_choice == "4":
            print_preview(103)
            check = 1
            sleep(1)
            clear()
        else:
            print_preview(111)
            print_preview(102)
            input("")


def tournament():
    """La fonction qui lance le tournoi.
    Dans cette function on appelle les differentes fonctions du jeu d'echecs:
    Creer un tournoi, joueurs, generer des paires, entrer les scores et sauvegarder le tournoi
    """
    tournament = enter_tournament_info()
    # check_tournament_input = enter_players(tournament)

    # if check_tournament_input == 0:
    #     pass
    # else:
    #     tournament = check_tournament_input

    player_auto = [["Davy", "Nimbona", "19/06/1995", 1, "H"], ["Marie", "Hautot", "10/06/1993", 2, "F"],
    ["Guy", "Nimbona", "01/12/1996", 3, "H"], ["Carelle", "Mugisha", "29/01/1994", 4, "F"],
    ["Junkers", "Ntwari", "18/03/1994", 5, "H"], ["Gretta", "Nkanagu", "30/08/1995", 6, "F"],
    ["Orlando", "Nkurunziza", "08/05/1996", 7, "H"], ["Lorraine", "Bafutwabo", "18/08/1995", 8, "F"]]

    list_temp = []
    for play in player_auto:
        player = Player(play[0], play[1], play[2], play[4], play[3])

        list_temp.append(player)
    tournament.players = list_temp

    check_launch = 0
    while check_launch < 1:
        clear()
        print_tournament_pre_launch(tournament)
        try:
            if len(tournament.players) == 8:
                print_preview(109)
                players_choice = int(input("\n>>> "))
            else:
                print_preview(110)
                players_choice = int(input("\n>>> "))
        except Exception:
            players_choice = 999

        if players_choice == 1 and len(tournament.players) == 8:
            for current_round in range(1, (tournament.rounds + 1)):
                clear()
                pairs = generate_pairs(tournament, current_round)
                tournament = enter_score(pairs, tournament, current_round)

            print_preview(106)
            sleep(2)
            check_launch = 1
        
        elif players_choice == 1 and len(tournament.players) < 8:
            check_players = enter_players(tournament)
            if check_players == 0:
                pass
            else:
                for player in tournament.players:
                    tournament.players.append(player)
        elif players_choice == 2:
            print_players(tournament.players_in_list())
        elif players_choice == 3:
            check_launch = 1
        else:
            print_preview(111)
            input("")

    tournament = set_ranking(tournament)
    save_tournament(tournament)

    return 0


def enter_tournament_info():
    check = 0
    while check < 1:
        clear()
        print_preview(105)
        tournament_name = input("Nom du tournoi: ")
        venue = input("Lieu: ")
        tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        rounds_number = input("Nombre de tours du tournoi: ")
        if len(rounds_number) == 0:
            rounds_number = 4
        description = input("Description: ")
        tournament = Tournament(tournament_name, venue, tournament_date, rounds_number, [], [], description)
        if tournament.is_valid() == 3:
            check = 1
        else:
            input("")

    return tournament


def enter_players(tournament):
    print_preview(104)
    sleep(1)
    taken_seat = len(tournament.players)
    remaining = 8 - len(tournament.players)
    while (taken_seat < remaining):
        clear()
        untaken_seats = 8 - len(tournament.players)
        print_create_players(untaken_seats)
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
        ranking = input("Classement: ")
        gender = input("Sexe(H ou F): ")
        verify = input("\n\n1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
        if verify == '1':
            player = Player(first_name, last_name, birth_date, gender, ranking)
            if player.is_valid() == 4:
                result = check_player_exists(tournament.players, player)
                if result == 1:
                    tournament.players.append(player)
                    taken_seat = len(tournament.players)
            else:
                input("")
        elif verify == '2':
            pass
        elif verify == '3':
            break

    return tournament


def generate_pairs(tournament, current_round):
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
        sorted_players = order_by_score_ranking(tournament, score_per_player(tournament))
        unmatched_players = [player[0] for player in sorted_players]
        for player_index in range(0, total_players-1):
            versus = player_index + 1
            player1 = sorted_players[player_index][0]
            player2 = sorted_players[versus][0]
            check_pair = 0
            while check_pair < 1:
                if player1 in unmatched_players:
                    if (player2 in unmatched_players and
                            not_played_with(list_of_played_with(tournament), player1, player2)):
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


def enter_score(pairs_list, tournament, tour_level):
    check = 0
    while check < 1:
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
                check = 1

    return tournament


def set_ranking(tournament):
    for index in range(0, len(tournament.players)):
        check = 0
        while check < 1:
            clear()
            print_preview(112)
            print_player_to_rank(tournament.players[index])
            ranking = input("\nNouveau classement >>> ")
            try:
                tournament.players[index].ranking = int(ranking)
                check += 1
            except Exception:
                print_preview(113)
                input("")

    return tournament

def check_tournament_launch():
    pass



def check_player_exists(players_list, player):
    if len(players_list) == 0:
        return 1
    else:
        for existing in players_list:
            try:
                if player.id == existing.id:
                    return 0
                else:
                    return 1
            except Exception:
                pass
        return 1


def score_per_player(tournament):
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


def order_by_score_ranking(tournament, score_per_player):
    list_player_by_stats = []
    for player_id in score_per_player:
        ranking = [x['ranking'] for x in tournament.players_in_list() if x['id'] == player_id]
        list_player_by_stats.append([player_id, score_per_player[player_id], ranking[0]])
    players_sorted_by_stats = sorted(list_player_by_stats, key=lambda x: (x[1], -x[2]), reverse=True)

    return players_sorted_by_stats


def list_of_played_with(tournament):
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


def not_played_with(played_with_dict, player1, player2):
    if player2 not in played_with_dict[player1]:
        return True
    else:
        return False


def existing_tournament():
    pass


def tournament_report():
    clear()
    print("Rapport")
    try:
        for tournament in tournaments_list():
            print_players(tournament["players"])
    except Exception:
        print("Aucun tournoi à voir")
