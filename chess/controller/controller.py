from os import system, name
from time import sleep
from chess.models.player import Player
from chess.models.model import (save_player, see_players, number_players,
                                delete_players)


def start_game():
    clear()
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Voir classement\
        \n3. Voir les tournois passés\n4. Quitter")
    jeux = int(input(("\n>>> ")))
    if jeux == 1:
        start_tournament()


def start_tournament():
    clear()
    print("######## Nouveau Tournoi ########\n")
    print("1. Ajouter des joueurs\n2. Charger liste des joueurs existants")
    print("3. Nombre de joueurs inscrits")
    print("4. Effacer tous les jouers")
    print("5. Retour au menu principal")
    players_choice = int(input("\n>>> "))

    if players_choice == 5:
        start_game()
    elif players_choice == 1:
        generate_players(players_choice)
    elif players_choice == 2:
        see_players()
    elif players_choice == 3:
        print(number_players())
    elif players_choice == 4:
        delete_players()
    else:
        print("\n*** Mauvais choix. Veuillez entrer encore une fois")
        sleep(1)


def generate_players(choice):
    if choice == 1:
        check = 0
        number = number_players()
        while (check < (4-number)):
            clear()
            print("########  Créer joueur ########\n")
            first_name = input("Prénom: ")
            last_name = input("Nom: ")
            birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
            gender = input("Sexe(M ou F): ")
            score = 0
            verify = input("Taper 1+Entrer pour confirmer: ")
            if verify == '1':
                player = Player(
                    first_name, last_name, birth_date, gender, score)
                result = save_player(player.record)
                if result == 1:
                    check -= 1
            check = check + 1
            sleep(1)
            clear()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
