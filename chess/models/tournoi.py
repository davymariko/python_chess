class Tournoi:
    def __init__(self, name, venue, date, tournee, players, description):

        self.name = name
        self.venue = venue
        self.date = date
        self.tours = 4
        self.tournee = tournee
        self.players = players
        self.description = description

    @property
    def define_time(self):
        print("Hello")
