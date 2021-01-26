class Player():
    def __init__(self, first_name, last_name, birth_date, gender, score):
        self.first_name = first_name
        self.last_name = last_name
        self.date = birth_date
        self.gender = gender
        self.score = score

    @property
    def change_score(self, new_score):
        self.score = new_score