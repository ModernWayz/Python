import time

class Voorstelling():
    """ Klasse voorstelling: bestaat uit een id, film, cinema, tijdstip en gebruikers """
    def __init__(self, id, film_id, film_titel, cinema_id, cinema_naam, tijdstip):
        self.id = id
        self.film_id = film_id
        self.film_titel = film_titel
        self.cinema_id = cinema_id
        self.cinema_naam = cinema_naam
        self.tijdstip = tijdstip
        self.gebruikers = [] # gebruikers die ticket hebben gekocht komen hier in

class Voorstellingen():
    """ Klasse voorstellingen: bevat voorstelling-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, film_id, film_titel, cinema_id, cinema_naam):
        nieuwe_voorstelling = Voorstelling(self.index, film_id, film_titel, cinema_id, cinema_naam, time.time())
        self.lijst.append(nieuwe_voorstelling) # toevoegen
        self.index += 1	# ga naar volgende ID

    def koop_ticket(self, gebruiker_id, voorstelling_id):
        try:
            if gebruiker_id in self.lijst[voorstelling_id-1].gebruikers:
                return "Deze gebruiker heeft al een ticket voor deze voorstelling"
            else:
                self.lijst[voorstelling_id-1].gebruikers.append(gebruiker_id)
                return "Ticket voor de voorstelling gekocht voor deze gebruiker"
        except IndexError:
            return "Voorstelling bestaat niet"

    def __str__(self):
        rs = "\nJe vroeg een lijst van de voorstellingen:\n"
        for voorstelling in self.lijst:
            rs += f"{str(voorstelling.id)}: {voorstelling.film_titel} in {voorstelling.cinema_naam}. Gebruikers: {str(voorstelling.gebruikers)}\n"
        return rs