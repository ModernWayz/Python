class Cinema():
    """ Klasse cinema: bestaat uit een id, naam en stad """
    def __init__(self, id, naam, stad):
        self.id = id
        self.naam = naam
        self.stad = stad


class Cinemas():
    """ Klasse cinemas: bevat cinema-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, naam, stad):
        nieuwe_cinema = Cinema(self.index, naam, stad)
        self.lijst.append(nieuwe_cinema) # toevoegen
        self.index += 1	# ga naar volgende ID

    def krijg_naam(self, cinema_id):
        for cinema in self.lijst:
            if cinema.id == cinema_id:
                return cinema.naam
    
    def __str__(self):
        rs = "\nJe vroeg een lijst van de cinema's:\n"
        for cinema in self.lijst:
            rs += f"{str(cinema.id)}: {cinema.naam} {cinema.stad}\n"
        return rs