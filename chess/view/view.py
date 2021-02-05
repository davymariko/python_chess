from os import system, name
import pprint
from chess.export.database import players_number


def start_game():
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Voir joueurs inscrits\
        \n3. Nombre de joueurs inscrits\n4. Effacer tous les joueurs\
        \n5. Rapport\n6. Quitter")


def start_tournament(info):
    print("######## Nouveau Tournoi ########\n")
    print(f"Nom du tournoi: {info[0]}\nLieu: {info[1]}\nDate du tournoi: {info[2]}\
        \nTours: {info[3]}\nNombre de joueurs: {players_number()}\nDescription: {info[4]}")

    return


def print_players(players_list):
    number = 1
    print("Liste des joueurs\n==================")
    print("   Nom\t\t\t\tDate de Naissance\tSexe\tClassement\
        \n--------------------------------------------------------------------------")
    for play in players_list:
        whole_name = play['first_name'] + " " + play['last_name']
        print(f"{number}. {whole_name:<20s}\t\t{play['birth_date']}\t\t{play['gender']}\t{play['ranking']}")
        number += 1


def print_players_number():
    print(f"Nombre de joeurs inscrits: {players_number()}")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
