from datetime import (date, datetime)


def birth_date_is_valid(date_given):
    date_given = date_given.split("/")
    if (len(date_given)) == 3:
        try:
            if len(date_given[2]) == 4:
                datetime(int(date_given[2]), int(date_given[1]), int(date_given[0]))
                return True
            else:
                print("\n*** Date: Respectez le format (dd/mm/yyyy)")
        except ValueError:
            print("\n*** Date incorrect")
        except Exception:
            print("\n*** Date incorrect")
    else:
        print("\n*** Respectez le format (dd/mm/yyyy)")

    return False


def date_tournament_is_valid(date_given):
    date_given = date_given.split("/")
    today = date.today()
    today = str(today).split('-')
    today_date = datetime(int(today[0]), int(today[1]), int(today[2]))
    if (len(date_given)) == 3:
        try:
            if len(date_given[2]) == 4:
                date_valid = datetime(int(date_given[2]), int(date_given[1]), int(date_given[0]))
                if today_date > date_valid:
                    print("Vous avez mis une date antérieure")
                else:
                    return True
            else:
                print("\n*** Date: Respecter le format (jj/mm/aaaa)")
        except ValueError:
            print("Date incorrecte")
        except Exception:
            print("Date incorrecte")
    else:
        print("\n*** Date: respectez le format (jj/mm/aaaa)")

    return False


def date_format():
    date_time_str = '18/09/2018'
    try:
        datetime.strptime(date_time_str, "%d/%m/%Y")
        return True
    except Exception:
        return False


def gender_is_valid(gender):
    if gender == "F" or gender == "M":
        return True
    else:
        print("\n*** Format pour sexe à respecter (M ou F)")
        return False


def text_is_alpha(string_text):
    if len(string_text) > 0 and string_text.isalpha():
        return True
    else:
        print("\n*** Le champ de nom ou lieu doit être completé et contenir que des alphabets")
        return False


def wrong_choice():
    print("\n**** Mauvais choix, reessayer")
    input("")


def score_input(score_input):
    try:
        if len(score_input.split("-")) == 2:
            if float(score_input.split("-")[0]) == 1.0 and float(score_input.split("-")[1]) == 0.0:
                return 0
            elif float(score_input.split("-")[0]) == 0.0 and float(score_input.split("-")[1]) == 1.0:
                return 0
            elif float(score_input.split("-")[0]) == 0.5 and float(score_input.split("-")[1]) == 0.5:
                return 0
            else:
                return 1
        else:
            return 1
    except Exception:
        return 1


def number_is_valid(number):
    if isinstance(number, int):
        return True
    else:
        print("\n**** Classement et tours doivent etre des nombres entiers")
        return False
