from os import system, name


def start_game():
    print("###### Commencer un tournoi ########")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')