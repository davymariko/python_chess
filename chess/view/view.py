from os import system, name


def start_game():
    print("######## Bienvenue ########\n")
    print("1. Commencer un tournoi\n2. Voir joueurs inscrits\
        \n3. Nombre de joueurs inscrits\n4. Effacer tous les joueurs\
        \n5. Rapport\n6. Quitter")
    try:
        game_choice = input(("\n>>> "))
        if game_choice == "":
            game_choice = 0
        else:
            game_choice = int(game_choice)
    except Exception:
        game_choice = 999

    return game_choice


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
