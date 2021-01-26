from time import sleep
from chess.models.game import start_game, clear


def main():
    print("\n===================\n")
    print("Bienvenue au jeux des échecs\n\n")
    jeux = input(("Commencer un tournoi? Oui(o) ou Non(n)\n\n>>>> "))
    if jeux in ["OUI", "Oui", "oui", "O", "o"]:
        clear()
        sleep(1)
        start_game()
    elif jeux in ["NON", "Non", "non", "N", "n"]:
        print(jeux)


main()