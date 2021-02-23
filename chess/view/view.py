from os import system, name
from chess.export.database import players_number, players_list


def print_game_start():
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Rapport des tournois passés\n3. Quitter")


def print_tournament_pre_launch(info):
    print("######## Nouveau Tournoi ########\n")
    print(f"Nom du tournoi: {info.name}\nLieu: {info.venue}\nDate du tournoi: {info.date}\
        \nTours: {info.rounds}\nNombre de joueurs: {players_number()}\nDescription: {info.description}")

    return


def print_players(players_list):
    if len(players_list) == 0:
        print("Y a aucun joueur inscrit")
        input("")
        return
    check = 0
    while check < 1:
        clear()
        print("1. Par ordre croissant (Nom)\n2. Par ordre croissant (Classement)\
        \n3. Par ordre décroissant (Nom)\n4. Par ordre décroissant (Classement)\n5. Retour")
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
            print("*** Mauvaix choix")
        number = 1
        print("Liste des joueurs\n==================")
        print("   Nom\t\t\t\tDate de Naissance\tSexe\tClassement\
            \n--------------------------------------------------------------------------")
        for play in sorted_dict:
            whole_name = play['last_name'] + " " + play['first_name']
            print(f"{number}. {whole_name:<20s}\t\t{play['birth_date']}\t\t{play['gender']}\t{play['ranking']}")
            number += 1
        input("")


def print_pairs(pairs_list, current_tour):
    players = players_list()
    print(f"Paires généreées pour le Round {current_tour}\n")
    match = 1
    for pair in pairs_list:
        player1 = [[x['last_name'], x['first_name']] for x in players if x['id'] == pair[0]]
        player2 = [[x['last_name'], x['first_name']] for x in players if x['id'] == pair[1]]
        print(f"{match}. {player1[0][0]} {player1[0][1]} vs  {player2[0][0]}  {player2[0][1]}")
        print("----------------------")
        match += 1


def print_create_players(taken_seats):
    print("########  Créer joueur ########\n")
    print(f"Places restantes: {8-taken_seats}\n")


def print_continue():
    input("\n\nAppuyer sur Entree pour continuer")


def print_bye():
    print("\n\n ---- A bientot ----")


def print_players_complete():
    print("\n**** Y a déjà 8 joueurs inscrits")


def print_generate_players():
    print("\n**** Place à la création des joueurs")


def print_start_tournament():
    print("######## Commencer le Tournoi ########\n")


def print_exit_tournament():
    print("\nEn sortant de ce tournoi vous l'annulez")


def print_end_tournament():
    print("\n*** C'est la fin du tournoi")


def print_wrong_score():
    print("\n*** Mauvaise inscription du score. Format (1-0)\n*** Les scores acceptés : 0, 1, 0.5")


def print_enter_score():
    print("\n*** Entrez les score des matchs de ce tour\n*** Entrer score par numéro/ordre des matchs\
        \n*** Exemple format(1-1)\n")


def print_tournament_ready():
    print("\n1. Lancer le tournoi\n2. Voir les joeurs inscrits\n3. Retour au menu principal")


def print_tournament_not_ready():
    print("\n1. Continuer à inscrire des joueurs\n2. Voir les joeurs inscrits\n3. Retour au menu principal")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
