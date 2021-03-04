from os import system, name


def print_tournament_pre_launch(info):
    print("######## Tournoi ########\n")
    print(f"Nom du tournoi: {info.name}\nLieu: {info.venue}\nDate du tournoi: {info.date}\nTours: {info.rounds}\
        \nNombre de joueurs: {len(info.players)}\nTours joués: {int(len(info.round_matchs)/4)}\
        \nDescription:{info.description}")

    return


def print_players(players_list):
    if len(players_list) == 0:
        print("Y a aucun joueur inscrit")
        input("")
        return
    check = True
    while check:
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
        print("     Nom\t\t\tDate de Naissance\tSexe\tClassement")
        print("-"*75)
        for play in sorted_dict:
            whole_name = play['last_name'] + " " + play['first_name']
            print(f"{number:<5}{whole_name:<28s}{play['birth_date']}\t\t{play['gender']}\t{play['ranking']}")
            number += 1
        input("")


def print_pairs(pairs_list, players_list, current_tour):
    print(f"Paires générées pour le Round {current_tour}\n")
    match = 1
    for pair in pairs_list:
        player1 = [[x['last_name'], x['first_name']] for x in players_list if x['id'] == pair[0]]
        player2 = [[x['last_name'], x['first_name']] for x in players_list if x['id'] == pair[1]]
        print(f"{match}. {player1[0][0]} {player1[0][1]} vs  {player2[0][0]}  {player2[0][1]}")
        print("-"*10)
        match += 1


def print_player_to_rank(player):
    print(f"Nom: {player.last_name}\nPremon: {player.first_name}\nSexe: {player.gender}\
        \nDate de naissance: {player.birth_date}")


def print_create_players(untaken_seats):
    print("########  Créer joueur ########\n")
    print(f"Places restantes: {untaken_seats}\n")


def print_tournaments_report(tournaments_list):
    clear()
    print("  Nom\t\t\tLieu\t\t\tDate\t\tDescription")
    print("-"*100, "\n")
    number = 1
    for tour in tournaments_list:
        name = tour["name"]
        venue = tour["venue"]
        date = tour["date"]
        description = tour["description"]
        print(f"{number}. {name:<21s}{venue:<24s}{date}\t{description}\n")
        
        number += 1


def print_players_by_tournament(tournaments_list, choice):
    print_players(tournaments_list[choice-1]["players"])


def print_all_players(tournament_list):
    all_players_list = []
    for tournament in tournament_list:
        for player in tournament["players"]:
            all_players_list.append(player)

    print_players(all_players_list)


def print_tournament_rounds(tournament):
    clear()
    number = 1
    print("Liste de tous les tours du tournoi\n=================================\n")
    for match in tournament["round_matchs"]:
        print(f"{number:<3}{match[0][0]:<25}{match[0][1]:<2} - {match[1][1]:<5}{match[1][0]}\n")
        print("*"*100, "\n")
        number += 1
    input("")


def print_tournament_matchs(tournament):
    clear()
    number = 1
    print("Liste de tous les matchs du tournoi\n=================================\n")

    for match in tournament["round_matchs"]:
        print(f"{number:<3}{match[0][0]:<25}{match[0][1]:<2} - {match[1][1]:<5}{match[1][0]}\n")
        print("----------------------\n")
        number += 1

    input("")


def print_preview(message_number):
    messages_dict = {
        101: "######## Bienvenue ########\
        \n\n1. Commencer un tournoi\n2. Reprende un tournoi existant\n3. Rapport des tournois passés\n4. Quitter",
        102: "\n\nAppuyer sur Entree pour continuer",
        103: "\n\n ---- A bientot ----",
        104: "\n**** Place à la création des joueurs",
        105: "######## Commencer le Tournoi ########\n",
        106: "\n*** C'est la fin du tournoi",
        107: "\n*** Mauvaise inscription du score. Format (1-0)\n*** Les scores acceptés : 0, 1, 0.5",
        108: "\n*** Entrez les score des matchs de ce tour\
            \n*** Entrer score par numéro/ordre des matchs\n*** Exemple format(1-0)\n",
        109: "\n1. Lancer le tournoi\n2. Voir les joeurs inscrits\n3. Retour au menu principal",
        110: "\n1. Continuer à inscrire des joueurs\n2. Voir les joeurs inscrits\n3. Retour au menu principal",
        111: "\n**** Mauvais choix, reessayer",
        112: "######## Nouveau Classement ########\n",
        113: "\n**** Classement et tours doivent etre des nombres entiers",
        114: "\n\n1. Confirmer\n2. Refaire\n3. Retour",
        115: "######## Rapport ########\n\n1. Liste des tournois\n2. Liste des joueurs\
        \n3. Liste des matchs par tournoi\n4. Liste des tours par tournoi\n5. Retour",
        116: "\n\nChoisissez un tournoi en entrant le numéro correspondant (0 pour sortir)",
        117: "######## Rapport des joueurs ########\n\
        \n1. Tous les joueurs\n2. Joueurs par tournoi\n3. Retour",
        118: "######## Rapport du tournoi ########\n\n1. Liste de tous les tours\
        \n2. Liste de tous les matchs\n3. Retour",
        119: "\n\n *** Y a un tournoi deja existant. Continuer l'annulera\n\nContinuer Oui(O) ou (Non)?",
        120: "\n\n *** Le joueur existe déjà",
        121: "\n\n *** Pas de tournoi en cours",
        122: "\n\n *** Pas de tournoi deja joué"
    }

    print(messages_dict[message_number])


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
