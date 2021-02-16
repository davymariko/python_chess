from datetime import (date, datetime)


def birth_date_is_valid(date_given):
    date_given = date_given.split("/")
    if (len(date_given)) == 3:
        try:
            if len(date_given[2]) == 4:
                datetime(int(date_given[2]), int(date_given[1]), int(date_given[0]))
                return 0
            else:
                print("\n*** Date: Respectez le format (dd/mm/yyyy)")
        except ValueError:
            print("\n*** Date incorrect")
        except Exception:
            print("\n*** Date incorrect")
    else:
        print("\n*** Respectez le format (dd/mm/yyyy)")

    return 1


def date_tournament_is_valid(date_given):
    date_given = date_given.split("/")
    today = date.today()
    today = str(today).split('-')
    print(today)
    today_date = datetime(int(today[0]), int(today[1]), int(today[2]))
    if (len(date_given)) == 3:
        try:
            if len(date_given[2]) == 4:
                date_valid = datetime(int(date_given[2]), int(date_given[1]), int(date_given[0]))
                if today_date > date_valid:
                    print("Vous avez mis une date antérieure")
                else:
                    return 0
            else:
                print("\n*** Date: Respecter le format (jj/mm/aaaa)")
        except ValueError:
            print("Date incorrecte")
        except Exception:
            print("Date incorrecte")
    else:
        print("\n*** Date: respectez le format (jj/mm/aaaa)")

    return 1


def date_format():
    date_time_str = '18/09/2018'
    try:
        datetime.strptime(date_time_str, "%d/%m/%Y")
        return True
    except Exception:
        return False


def gender_is_valid(gender):
    if gender == "F" or gender == "M":
        return 0
    else:
        print("\n*** Format pour sexe à respecter (M ou F)")
        return 1


def ranking_is_valid(ranking):
    try:
        ranking_int = int(ranking)
        if ranking_int in range(0, 8):
            return 0
        else:
            print("\n*** Classement hors interval(1-8)")
    except Exception:
        print("\n*** Le classement doit être un chiffre naturel")

    return 1


def name_is_valid(name):
    print("Le nom est pas valide")


def wrong_choice():
    print("\n**** Mauvais choix, reessayer")
    input("")
