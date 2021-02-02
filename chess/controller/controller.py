from os import system, name
from time import sleep
from chess.models.player import Player
from chess.models.model import (save_player, see_players, number_players,
                                delete_players, swiss_pair_generator)


def start_game():
    clear()
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Voir joueurs inscrits\
        \n3. Nombre de joueurs inscrits\n4. Effacer tous les joueurs\
        \n5. Rapport\n6. Quitter")
    jeux = int(input(("\n>>> ")))
    if jeux == 1:
        start_tournament()
    elif jeux == 2:
        clear()
        see_players()
        input("")
        start_game()
    elif jeux == 3:
        clear()
        print(f'Nombre de joueurs inscrits: {number_players()}')
        input("")
        start_game()
    elif jeux == 4:
        delete_players()
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
    print("\n**** Place à la création des joueurs")
    sleep(2)
    generate_players(1)
    clear()
    print("######## Nouveau Tournoi ########\n")
    print(f"Nom du tournoi: {tournament_name}")
    print(f"Lieu: {venue}")
    print(f"Date du tournoi: {tournament_date}")
    print("\n1. Lancer le tournoi\n2. Retour au menu principal")
    players_choice = int(input("\n>>> "))
    if players_choice == 1:
        clear()
        swiss_pair_generator()
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
        while (check < (2-number)):
            clear()
            remaining_seat = number_players()
            print("########  Créer joueur ########\n")
            print(f"Place restant: {2-remaining_seat}\n")
            first_name = input("Prénom: ")
            last_name = input("Nom: ")
            birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
            gender = input("Sexe(M ou F): ")
            score = 0
            verify = input("1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
            if verify == '1':
                player = Player(
                    first_name, last_name, birth_date, gender, score)
                result = save_player(player.record)
                if result == 1:
                    check -= 1
            elif verify == '2':
                generate_players(1)
            elif verify == '3':
                start_tournament()
            check = check + 1
            sleep(1)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
