from time import sleep
from chess.view.view import clear, game_start, print_players, print_players_number, start_tournament, \
    print_pairs, print_no_tournament, print_bye, print_generate_players, print_players_complete, \
    print_exit_tournament, print_create_players, print_enter_score, print_continue, print_wrong_score
from chess.errors.error import wrong_choice, score_input
from chess.models.model import Player
from chess.export.database import save_player, delete_all_players, players_number, players_list, save_tours, \
    matchs_list


def start():
    check = 0
    while check < 1:
        clear()
        game_start()
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
    print("######## Commencer le Tournoi ########\n")
    tournament_name = input("Nom du tournoi: ")
    venue = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    tournament_tours = input("Tours du tournoi: ")
    description = input("Description: ")
    tournament_info = [tournament_name, venue, tournament_date, tournament_tours, description]
    if players_exist() == 1:
        print_generate_players()
    else:
        print_players_complete()
    sleep(2)
    result = generate_players()
    if result == 0:
        pass
    clear()
    start_tournament(tournament_info)
    players_choice = 999
    if players_number() == 8:
        print("\n1. Lancer le tournoi\n2. Voir les joeurs inscrits\n3. Retour au menu principal")
        players_choice = int(input("\n>>> "))
    else:
        print("\n1. Continuer à inscrire des joueurs\n2. Voir les joeurs inscrits\n3. Retour au menu principal")
        players_choice = int(input("\n>>> "))

    if players_choice == 1 and players_number() == 8:
        clear()
        generate_pairs()
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
            valid = player.is_valid()
            if valid == 0:
                result = save_player(player.record)
                if result == 1:
                    check -= 1
            else:
                check -= 1
        elif verify == '2':
            check -= 1
        elif verify == '3':
            return 0
        check = check + 1
        sleep(1)


def generate_pairs():
    total_players = players_number()
    for current_round in range(1, 4+1):
        pairs_list = []
        pairing = 0
        if current_round == 1:
            sorted_dict = []
            players = players_list()
            sorted_dict = sorted(players, key=lambda players: players.get('ranking', {}), reverse=True)
        else:
            sorted_dict = []
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
            sorted_dict = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
            input("")

        while pairing < (total_players/2):
            versus = pairing+int(total_players/2)
            if current_round == 1:
                pairs_list.append([sorted_dict[pairing]['id'], sorted_dict[versus]['id']])
            else:
                pairs_list.append([sorted_dict[pairing][0], sorted_dict[versus][0]])
            pairing += 1
        check = 0
        while check < 1:
            print_pairs(pairs_list, current_round)
            if enter_score(pairs_list) == 1:
                clear()
            else:
                break
        print_continue()
        clear()


def resume_tournament():
    print_no_tournament()


def players_exist():
    number = players_number()
    if number == 8:
        return 0
    else:
        return 1


def played_together():
    pass


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
