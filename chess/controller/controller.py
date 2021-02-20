from time import sleep
from chess.view.view import clear, game_start, print_players, print_players_number, start_tournament, \
    print_pairs, print_no_tournament, print_bye, print_generate_players, print_players_complete, \
    print_exit_tournament, print_create_players, print_enter_score, print_continue
from chess.errors.error import wrong_choice
from chess.models.model import Player
from chess.export.database import (save_player, delete_all_players, players_number, players_list, save_tours)


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

        while pairing < (total_players/2):
            versus = pairing+int(total_players/2)
            pairing += 1
            pairs_list.append([sorted_dict[pairing]['id'], sorted_dict[versus]['id']])
        print_pairs(pairs_list, current_round)
        enter_score(pairs_list)
        print_continue()
        clear()


# def generate_pairs():
#     round = 1
#     total_players = players_number()
#     print("Paires généreées pour le Round {1}\n")
#     players = players_list()
#     if round == 1:
#         pairing = 0
#         while pairing < (total_players/2):
#             versus = pairing+int(total_players/2)
#             print(f"\n{players[pairing]['first_name']} {players[pairing]['last_name']}\
#  vs {players[versus]['first_name']} {players[versus]['last_name']}\n")
#             print("----------------------")
#             pairing += 1
#         print_continue()
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
    for match in range(1, len(pairs_list)+1):
        score = input(f"Match {match}>>> ")
        save_tours([pairs_list[match-1], score.split("-")])
