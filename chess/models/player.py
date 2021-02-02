class Player():
    def __init__(self, first_name, last_name, birth_date, gender, score):
        self.first_name = first_name
        self.last_name = last_name
        self.date = birth_date
        self.gender = gender
        self.score = score
        self.id = (first_name[0].lower() + last_name.lower()+"_" +
                      birth_date.replace("/", ""))

    # def is_valid(self):
    #     message = ""
    #     test_dat = self.score

    @property
    def record(self):

        return {
                    'id': self.id,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'birth_date': self.date,
                    'gender': self.gender,
                    'score': self.score
                }
