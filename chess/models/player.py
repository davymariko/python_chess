class Player():
    def __init__(self, first_name, last_name, birth_date, gender, score):
        self.first_name = first_name
        self.last_name = last_name
        self.date = birth_date
        self.gender = gender
        self.score = score

    # def is_valid(self):
    #     message = ""
    #     test_dat = self.score

    @property
    def record(self):

        return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'birth_date': self.date,
                    'gender': self.gender,
                    'score': self.score
                }
