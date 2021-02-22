from time import sleep
from chess.view.view import clear, print_game_start, print_players, print_players_number, start_tournament, \
    print_pairs, print_no_tournament, print_bye, print_generate_players, print_exit_tournament, \
    print_create_players, print_enter_score, print_continue, print_wrong_score, print_end_tournament, \
    print_start_tournament
from chess.errors.error import wrong_choice, score_input
from chess.models.model import Player
from chess.export.database import save_player, delete_all_players, players_number, players_list, save_tours, \
    matchs_list, delete_all_matchs


def start():
    check = 0
    while check < 1:
        clear()
        print_game_start()
        try:
            game_choice = input(("\n>>> "))
            if game_choice == "":
                game_choice = 0
            else:
                game_choice = int(game_choice)
        except Exception:
            game_choice = 999

        if game_choice == 1:
            check_tournament = 0
            while check_tournament < 1:
                if tournament() == 0:
                    break
                else:
                    pass
        elif game_choice == 2:
            print_no_tournament()
            print_continue()
        elif game_choice == 3:
            clear()
            print_players(players_list())
        elif game_choice == 4:
            clear()
            print_players_number()
            print_continue()
        elif game_choice == 5:
            delete_all_players()
            print_continue()
        elif game_choice == 6:
            clear()
            print("Rapport")
            print_continue()
        elif game_choice == 7:
            print_bye()
            check = 1
            sleep(2)
            clear()
        else:
            wrong_choice()


def tournament():
    clear()
    delete_all_matchs()
    delete_all_players()
    print_start_tournament()
    tournament_name = input("Nom du tournoi: ")
    venue = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    tournament_tours = input("Tours du tournoi: ")
    description = input("Description: ")
    tournament_info = [tournament_name, venue, tournament_date, tournament_tours, description]
    print_generate_players()
    sleep(2)
    result = generate_players()
    if result == 0:
        pass
    clear()
    start_tournament(tournament_info)
    try:
        if players_number() == 8:
            print("\n1. Lancer le tournoi\n2. Voir les joeurs inscrits\n3. Retour au menu principal")
            players_choice = int(input("\n>>> "))
        else:
            print("\n1. Continuer à inscrire des joueurs\n2. Voir les joeurs inscrits\n3. Retour au menu principal")
            players_choice = int(input("\n>>> "))
    except Exception:
        players_choice = 999

    if players_choice == 1 and players_number() == 8:
        clear()
        generate_pairs()
        print_end_tournament()
        input("")
    elif players_choice == 1 and players_number() < 8:
        generate_players()
    elif players_choice == 2:
        print_players(players_list())
    elif players_choice == 3:
        print_exit_tournament()
        print_continue()
    else:
        wrong_choice()
        sleep(1)
        return 1

    return 0


def generate_players():
    check = 0
    number_of_players = players_number()
    while (check < (8-number_of_players)):
        clear()
        taken_seats = players_number()
        print_create_players(taken_seats)
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
        ranking = input("Classement: ")
        gender = input("Sexe(M ou F): ")
        verify = input("\n\n1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
        if verify == '1':
            player = Player(
                first_name, last_name, birth_date, gender, ranking)
            if player.is_valid() == 4:
                player_record = {
                    'id': player.id,
                    'first_name': player.first_name,
                    'last_name': player.last_name,
                    'birth_date': player.birth_date,
                    'gender': player.gender,
                    'ranking': player.ranking
                }
                result = save_player(player_record)
                if result == 1:
                    check -= 1
            else:
                check -= 1
        elif verify == '2':
            check -= 1
        elif verify == '3':
            return 0
        check = check + 1
        sleep(2)


def generate_pairs():
    total_players = players_number()
    for current_round in range(1, 4+1):
        pairs_list = []
        sorted_players = []
        if current_round == 1:
            pairing = 0
            players = players_list()
            sorted_players = sorted(players, key=lambda players: players.get('ranking', {}), reverse=True)
            while pairing < (total_players/2):
                versus = pairing+int(total_players/2)
                pairs_list.append([sorted_players[pairing]['id'], sorted_players[versus]['id']])
                pairing += 1
        else:
            total_score_per_player = score_per_player()
            sorted_players = order_by_score_ranking(total_score_per_player)
            unmatched_players = [player[0] for player in sorted_players]
            for player_index in range(0, total_players-1):
                versus = player_index + 1
                player1 = sorted_players[player_index][0]
                player2 = sorted_players[versus][0]
                check_pair = 0
                while check_pair < 1:
                    if player1 in unmatched_players:
                        if player2 in unmatched_players and not_played_with(list_of_played_with(), player1, player2):
                            pairs_list.append([player1, player2])
                            unmatched_players.remove(player1)
                            unmatched_players.remove(player2)
                            check_pair = 1
                        else:
                            versus += 1
                            player2 = sorted_players[versus][0]
                    else:
                        check_pair = 1

        check = 0
        while check < 1:
            print_pairs(pairs_list, current_round)
            if enter_score(pairs_list) == 1:
                input("")
                clear()
            else:
                break
        print_continue()
        clear()


def score_per_player():
    matchs = matchs_list()
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


def order_by_score_ranking(total_score_per_player):
    list_player_by_stats = []
    for player_id in total_score_per_player:
        ranking = [x['ranking'] for x in players_list() if x['id'] == player_id]
        list_player_by_stats.append([player_id, total_score_per_player[player_id], ranking[0]])
    players_sorted_by_stats = sorted(list_player_by_stats, key=lambda x: (x[1], -x[2]), reverse=True)

    return players_sorted_by_stats


def not_played_with(played_with_dict, player1, player2):
    if player2 not in played_with_dict[player1]:
        return True
    else:
        return False


def resume_tournament():
    print_no_tournament()


# def players_exist():
#     number = players_number()
#     if number == 8:
#         return 0
#     else:
#         return 1


def list_of_played_with():
    matchs = matchs_list()
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


def enter_score(pairs_list):
    print_enter_score()
    tour_scores = []
    for match in range(1, len(pairs_list)+1):
        score = input(f"Match {match}>>> ")
        if score_input(score) == 1:
            print_wrong_score()
            return 1
        else:
            tour_scores.append([pairs_list[match-1], score.split("-")])

    save_tours(tour_scores)
