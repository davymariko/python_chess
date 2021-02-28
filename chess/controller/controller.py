from time import sleep
from chess.view.view import clear, print_game_start, print_players, print_tournament_pre_launch, \
    print_pairs, print_bye, print_generate_players, print_exit_tournament, print_player_to_rank, \
    print_create_players, print_enter_score, print_continue, print_wrong_score, print_end_tournament, \
    print_start_tournament, print_tournament_ready, print_tournament_not_ready
from chess.errors.error import wrong_choice, score_input, check_player_duplicates, number_is_valid
from chess.models.model import Player, Tournament, Round
from chess.export.database import save_player, delete_all_players, players_number, players_list, save_rounds, \
    matchs_list, delete_all_matchs, tournaments_list


def start():
    """La fonction qui lance le menu principal
    """
    check = 0
    while check < 1:
        clear()
        print_game_start()
        try:
            game_choice = input(("\n>>> "))
            if game_choice == "":
                game_choice = 0
            else:
                game_choice = int(game_choice)
        except Exception:
            game_choice = 999

        if game_choice == 1:
            check_tournament = 0
            while check_tournament < 1:
                if tournament() == 0:
                    break
                else:
                    pass
        elif game_choice == 2:
            clear()
            tournament_report()
            print_continue()
        elif game_choice == 3:
            print_bye()
            check = 1
            sleep(2)
            clear()
        else:
            wrong_choice()


def tournament():
    """La fonction qui lance le tournoi.
    Dans cette function on appelle les differentes fonctions du jeu d'echecs:
    Creer un tournoi, joueurs, generer des paires, entrer les scores et sauvegarder le tournoi
    """
    check = 0
    while check < 1:
        clear()
        print_start_tournament()
        tournament_name = input("Nom du tournoi: ")
        venue = input("Lieu: ")
        tournament_date = input("Date du tournoi (Format: jj/mm/aaaa): ")
        rounds_number = input("Nombre de tours du tournoi: ")
        if len(rounds_number) == 0:
            rounds_number = 4
        description = input("Description: ")
        tournament = Tournament(tournament_name, venue, tournament_date, rounds_number, [], [], description)
        if tournament.is_valid() == 3:
            check = 1
        else:
            input("")
            print("Else")

    # check_players = enter_players(tournament)
    # if check_players == 0:
    #     pass
    # else:
    #     tournament.players = (check_players)

    player_auto = [["Davy", "Nimbona", "19/06/1995", 1, "H"], ["Marie", "Hautot", "10/06/1993", 2, "F"], 
    ["Guy", "Nimbona", "01/12/1996", 3, "H"], ["Carelle", "Mugisha", "29/01/1994", 4, "F"], 
    ["Junkers", "Ntwari", "18/03/1994", 5, "H"], ["Gretta", "Nkanagu", "30/08/1995", 6, "F"],
    ["Orlando", "Nkurunziza", "08/05/1996", 7, "H"], ["Lorraine", "Bafutwabo", "18/08/1995", 8, "F"]]

    list_temp = []
    for play in player_auto:
        player = Player(play[0], play[1], play[2], play[4], play[3])

        list_temp.append(player)
    tournament.players = list_temp

    check_launch = 0
    while check_launch < 1:
        clear()
        print_tournament_pre_launch(tournament)
        try:
            if len(tournament.players) == 8:
                print_tournament_ready()
                players_choice = int(input("\n>>> "))
            else:
                print_tournament_not_ready()
                players_choice = int(input("\n>>> "))
        except Exception:
            players_choice = 999

        if players_choice == 1 and len(tournament.players) == 8:
            for current_round in range(1, (tournament.rounds + 1)):
                clear()
                pairs = tournament.generate_pairs(current_round)
                scores = enter_score(pairs, tournament.players_in_list(), current_round)
                tournament.round_matchs.append(scores)
            
            print_end_tournament()
            check_launch = 1
            input("")
        elif players_choice == 1 and len(tournament.players) < 8:
            check_players = enter_players(tournament)
            if check_players == 0:
                pass
            else:
                for player in check_players:
                    tournament.players.append(player)
        elif players_choice == 2:
            print_players(tournament.players_in_list())
        elif players_choice == 3:
            check_launch = 1
            print_exit_tournament()
            print_continue()
        else:
            wrong_choice()
            sleep(1)

    return 0


def enter_players(tournament):
    print_generate_players()
    sleep(1)
    untaken_seats = 8 - len(tournament.players)
    players_list = []
    check = 0
    while (check < (8- len(tournament.players))):
        clear()
        print_create_players(untaken_seats)
        first_name = input("Prénom: ")
        last_name = input("Nom: ")
        birth_date = input("Date de naissance (Format: jj/mm/aaaa): ")
        ranking = input("Classement: ")
        gender = input("Sexe(H ou F): ")
        verify = input("\n\n1. Confirmer\n2. Refaire\n3. Retour\n>>> ")
        if verify == '1':
            player = Player(first_name, last_name, birth_date, gender, ranking)
            if player.is_valid() == 4:
                result = check_player_exists(players_list, player)
                if result == 1:
                    players_list.append(player)
                    untaken_seats = untaken_seats - 1
            else:
                check -= 1
        elif verify == '2':
            check -= 1
        elif verify == '3':
            return 0
        check = check + 1
        sleep(1)

    return players_list


def enter_score(pairs_list, players_list, tour_level):
    print
    pairs_scores = []
    check = 0
    while check < 1:
        clear()
        print_pairs(pairs_list, players_list, tour_level)
        print_enter_score()
        for match in range(0, len(pairs_list)):
            score = input(f"Match {match + 1}. >>> ")
            if score_input(score) == 1:
                print_wrong_score()
                input("")
                break
            else:
                pairs_scores.append(([pairs_list[match][0], float(score.split("-")[0])],
                                    [pairs_list[match][1], float(score.split("-")[1])]))
                check = 1                

    return pairs_scores


def set_ranking(tournament):
    ranks_list = []
    for player in tournament.players:
        check = 0
        while check < 1:
            print_player_to_rank(player)
            ranking = input("Nouveau classement >>> ")
            if number_is_valid(ranking):
                ranks_list.append(int(ranking))
                check += 1
            else:
                pass
                
def check_player_exists(players_list, player):
    if len(players_list) == 0:
        return 1
    else:
        for existing in players_list:
            try:
                if player.id == existing.id:
                    return 0
                else:
                    return 1
            except Exception:
                return 1


def tournament_report():
    clear()
    print("Rapport")
    try:
        for tournament in tournaments_list():
            print_players(tournament["players"])
    except Exception:
        print("Aucun tournoi à voir")
