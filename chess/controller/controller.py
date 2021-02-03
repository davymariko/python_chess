from os import system, name
from time import sleep
from chess.models.model import Player
from chess.models.model import (save_player, see_players, number_players,
                                delete_all_players, players_list)


def start_game():
    clear()
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Voir joueurs inscrits\
        \n3. Nombre de joueurs inscrits\n4. Effacer tous les joueurs\
        \n5. Rapport\n6. Quitter")
    game_choice = int(input(("\n>>> ")))
    if game_choice == 1:
        start_tournament()
    elif game_choice == 2:
        clear()
        see_players()
        input("")
        start_game()
    elif game_choice == 3:
        clear()
        print(f'Nombre de joueurs inscrits: {number_players()}')
        input("")
        start_game()
    elif game_choice == 4:
        delete_all_players()
        clear()
        print("Tous les joueurs ont été effacés")
        input("")
        start_game()


def start_tournament():
    clear()
    print("######## Nouveau Tournoi ########\n")
    tournament_name = input("Nom du tournoi: ")
    venue = input("Lieu: ")
    tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
    description = input("Description: ")
    print("\n**** Place à la création des joueurs")
    sleep(2)
    generate_players(1)
    clear()
    print("######## Nouveau Tournoi ########\n")
    print(f"Nom du tournoi: {tournament_name}\nLieu: {venue}\nDate du\
tournoi: {tournament_date}\nNombre de joueurs: {number_players()}\
    \nDescription: {description}")
    print("\n1. Lancer le tournoi\n2. Retour au menu principal")
    players_choice = int(input("\n>>> "))
    if players_choice == 1:
        clear()
        generate_pairs()
    elif players_choice == 2:
        print("En sortant de ce tournoi vous l'annulez")
        input("")
        start_game()
    else:
        print("\n*** Mauvais choix. Veuillez entrer encore une fois")
        sleep(2)
        start_tournament()


def generate_players(choice):
    if choice == 1:
        check = 0
        number = number_players()
        while (check < (8-number)):
            clear()
            remaining_seat = number_players()
            print("########  Créer joueur ########\n")
            print(f"Place restant: {8-remaining_seat}\n")
            first_name = input("Prénom: ")
            last_name = input("Nom: ")
            birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
            gender = input("Sexe(M ou F): ")
            score = 0
            verify = input("\n\n1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
            if verify == '1':
                player = Player(
                    first_name, last_name, birth_date, gender, score)
                result = save_player(player.record)
                if result == 1:
                    check -= 1
            elif verify == '2':
                generate_players(1)
            elif verify == '3':
                start_game()
            check = check + 1
            sleep(1)


def generate_pairs():
    round = 1
    total_players = number_players()
    print("Paires généreées pour le Round {1}\n")
    players = players_list()
    if round == 1:
        pairing = 0
        while pairing < (total_players/2):
            versus = pairing+int(total_players/2)
            print(f"\n{players[pairing]['first_name']} {players[pairing]['last_name']}\
 vs {players[versus]['first_name']} {players[versus]['last_name']}\n")
            print("========================")
            pairing += 1
        input("")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
