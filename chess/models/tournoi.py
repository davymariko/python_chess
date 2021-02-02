class Tournoi:
    def __init__(self, name, venue, date, tours, tournee, players, description):

        self.name = name
        self.venue = venue
        self.date = date
        self.tours = tours
        self.tournee = tournee
        self.players = players
        self.description = description

    @property
    def define_time(self):
        print("Hello")
