from datetime import (date, datetime)


def birth_date_is_valid(date_given):
    date_given = date_given.split("/")
    if (len(date_given)) == 3:
        try:
            if len(date_given[2]) == 4:
                datetime(int(date_given[2]), int(date_given[1]), int(date_given[0]))
                return 0
            else:
                print("\n***** Respectez le format (dd/mm/yyyy)")
        except ValueError:
            print("\n**** Date incorrect")
        except Exception:
            print("\n**** Date incorrect")
    else:
        print("\n***** Respectez le format (dd/mm/yyyy)")

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
                print(date_valid)
                if today_date > date_valid:
                    print("Vous avez mis une date antérieure")
            else:
                print("\n***** Respecter le format (dd/mm/yyyy)")
        except ValueError:
            print("Date incorrect")
        except Exception:
            print("Date incorrect")
    else:
        print("\n***** Respectez le format (dd/mm/yyyy)")


def gender_is_valid(gender):
    gender = gender.lower()
    if gender == "f" or gender == "h":
        return 0
    else:
        return 1