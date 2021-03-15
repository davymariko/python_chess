from time import sleep
from chess.view.view import clear, print_preview
from chess.export.database import Database
from chess.controller.manager import ManageTournament

database = Database()
manage = ManageTournament()


def start():
    check = True
    while check:
        clear()
        print_preview(101)
        game_choice = input(("\n>>> "))
        if game_choice == "1":
            if manage.check_existing_tournament():
                pass
            else:
                if manage.tournament() == 1:
                    pass
        elif game_choice == "2":
            if len(database.initiate_unfinished_tournament_table().all()) == 0:
                print_preview(121)
                input("")
            else:
                manage.tournament()
        elif game_choice == "3":
            if len(database.initiate_tournament_table().all()) == 0:
                print_preview(122)
                input("")
            else:
                manage.report()
        elif game_choice == "4":
            print_preview(103)
            check = False
            sleep(1)
            clear()
        else:
            print_preview(111)
            print_preview(102)
            input("")
