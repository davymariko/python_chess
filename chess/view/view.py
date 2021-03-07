from os import system, name


def print_tournament_pre_launch(info):
    print("######## Tournoi ########\n")
    print(f"Nom du tournoi: {info.name}\nLieu: {info.venue}\nDate du tournoi: {info.date}\nTours: {info.rounds}\
        \nNombre de joueurs: {len(info.players)}\nTours joués: {int(len(info.round_matchs)/4)}\
        \nDescription:{info.description}")

    return


def display_players(sorted_dict):
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
        whole_name1 = player1[0][0] + " " + player1[0][1]
        whole_name2 = player2[0][0] + " " + player1[0][1]
        print(f"{match}. {whole_name1:<20} vs   {whole_name2}")
        print("-"*40)
        match += 1


def print_player_to_rank(player):
    print(f"\nNom:  {player.last_name}\nPremon:  {player.first_name}\nSexe:  {player.gender}\
        \nDate de naissance:  {player.birth_date}\nAncien classement:  {player.ranking}")


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


def print_tournament_rounds(tournament):
    clear()
    number = 1
    num = 1
    print("Liste de tous les tours du tournoi\n=================================\n")
    for match in tournament["round_matchs"]:
        if ((number - 1) % 4) == 0:
            print(f"\nRound {num}", "\n", "*"*10)
            number = 1
            num += 1
        player1 = [[x['last_name'], x['first_name']] for x in tournament["players"] if x['id'] == match[0][0]]
        player2 = [[x['last_name'], x['first_name']] for x in tournament["players"] if x['id'] == match[1][0]]
        whole_name1 = player1[0][0] + " " + player1[0][1]
        whole_name2 = player2[0][0] + " " + player2[0][1]
        print(f"{number:<3}{whole_name1:<25}{match[0][1]:<2}  -  {match[1][1]:<5}{whole_name2}\n")
        number += 1
    input("")


def print_tournament_matchs(tournament):
    clear()
    number = 1
    print("Liste de tous les matchs du tournoi\n=================================\n")

    for match in tournament["round_matchs"]:
        player1 = [[x['last_name'], x['first_name']] for x in tournament["players"] if x['id'] == match[0][0]]
        player2 = [[x['last_name'], x['first_name']] for x in tournament["players"] if x['id'] == match[1][0]]
        whole_name1 = player1[0][0] + " " + player1[0][1]
        whole_name2 = player2[0][0] + " " + player2[0][1]

        print(f"{number:<3}{whole_name1:<25}{match[0][1]:<2}  -  {match[1][1]:<5}{whole_name2}\n")
        print("----------------------\n")
        number += 1

    input("")


def print_preview(message_number):
    messages_dict = {
        101: "######## Bienvenue ########\
            \n\n1. Commencer un tournoi\n2. Reprende un tournoi existant\
            \n3. Rapport des tournois passés\n4. Quitter",
        102: "\n\nAppuyer sur Entree pour continuer",
        103: "\n\n ---- A bientot ----",
        104: "\n**** Place à la création des joueurs",
        105: "######## Commencer le Tournoi ########\n",
        106: "\n*** C'est la fin du tournoi",
        107: "\n*** Mauvaise inscription du score. Format (1-0)\n*** Les scores acceptés : 0, 1, 0.5",
        108: "\n*** Entrez les score des matchs de ce tour\
            \n*** Entrer score par numéro/ordre des matchs\n*** Exemple format(1-0)\n",
        109: "\n1. Lancer le tournoi\n2. Voir les joeurs inscrits\n3. Mettre à jour le classement\
            \n4. Retour au menu principal",
        110: "\n1. Continuer à inscrire des joueurs\n2. Voir les joeurs inscrits\n3. Retour au menu principal",
        111: "\n**** Mauvais choix, reessayer",
        112: "######## Nouveau Classement ########\
            \n\n***Laissez vide pour garder le classement actuel du joueur",
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
        122: "\n\n *** Pas de tournoi deja joué",
        123: "\n\n1. Continuer\n0. Retour",
        124: "\nY a aucun joueur inscrit",
        125: "1. Par ordre croissant (Nom)\n2. Par ordre croissant (Classement)\
            \n3. Par ordre décroissant (Nom)\n4. Par ordre décroissant (Classement)\n5. Retour"
    }

    print(messages_dict[message_number])


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
