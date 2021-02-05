from time import sleep
from chess.view.view import clear
from chess.view.view import (start_game, print_players, print_players_number, start_tournament)
from chess.models.model import Player
from chess.export.database import (save_player, delete_all_players, players_number, players_list)


def start():
    check = 0
    while check < 1:
        clear()
        start_game()
        try:
            game_choice = input(("\n>>> "))
            if game_choice == "":
                game_choice = 0
            else:
                game_choice = int(game_choice)
        except Exception:
            game_choice = 999

        if game_choice == 1:
            tournament()
        elif game_choice == 2:
            clear()
            print_players(players_list())
            input("")
        elif game_choice == 3:
            clear()
            print_players_number()
            input("")
        elif game_choice == 4:
            delete_all_players()
            input("")
        elif game_choice == 5:
            clear()
            print("Rapport")
            input("")
        elif game_choice == 6:
            print("\n\n ---- A bientot ----")
            check = 1
            sleep(2)
            clear()
        else:
            print("\n\n**** Mauvais choix, reessayer")
            input("")


def tournament():
    clear()
    print("######## Commencer le Tournoi ########\n")
    tournament_name = input("Nom du tournoi: ")
    venue = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    tournament_tours = input("Tours du tournoi: ")
    description = input("Description: ")
    tournament_info = [tournament_name, venue, tournament_date, tournament_tours, description]
    print("\n**** Place à la création des joueurs")
    sleep(2)
    result = generate_players()
    if result == 0:
        pass
    clear()
    start_tournament(tournament_info)
    players_choice = 999
    if players_number() == 8:
        print("\n1. Lancer le tournoi\n2. Retour au menu principal")
        players_choice = int(input("\n>>> "))
    else:
        print("\n1. Continuer à inscrire des joueurs\n2. Retour au menu principal")
        players_choice = int(input("\n>>> "))

    if players_choice == 1 and players_number() == 8:
        clear()
        generate_pairs()
    elif players_choice == 1:
        generate_players()
    elif players_choice == 2:
        print("En sortant de ce tournoi vous l'annulez")
        input("")
        start_game()
    else:
        print("\n*** Mauvais choix. Veuillez entrer encore une fois")
        sleep(2)
        tournament()


def generate_players():
    check = 0
    number_of_players = players_number()
    while (check < (8-number_of_players)):
        clear()
        taken_seats = players_number()
        print("########  Créer joueur ########\n")
        print(f"Place restant: {8-taken_seats}\n")
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
        gender = input("Sexe(M ou F): ")
        score = 0
        verify = input("\n\n1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
        if verify == '1':
            player = Player(
                first_name, last_name, birth_date, gender, score)
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
    round = 1
    total_players = players_number()
    print("Paires généreées pour le Round {1}\n")
    players = players_list()
    if round == 1:
        pairing = 0
        while pairing < (total_players/2):
            versus = pairing+int(total_players/2)
            print(f"\n{players[pairing]['first_name']} {players[pairing]['last_name']}\
 vs {players[versus]['first_name']} {players[versus]['last_name']}\n")
            print("----------------------")
            pairing += 1
        input("")


def players_exist():
    number = players_number()
    if number > 0:
        return 0
    else:
        return 1


def played_together():
    pass
