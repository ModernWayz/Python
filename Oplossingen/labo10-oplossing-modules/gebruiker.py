class Gebruiker():
    """ Klasse gebruiker: bestaat uit een id, voornaam en naam """
    def __init__(self, id, voornaam, naam):
        self.id = id
        self.voornaam = voornaam
        self.naam = naam


class Gebruikers():
    """ Klasse gebruikers: bevat gebruiker-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, voornaam, naam):
        nieuwe_gebruiker = Gebruiker(self.index, voornaam, naam)
        self.lijst.append(nieuwe_gebruiker) # toevoegen
        self.index += 1	# ga naar volgende ID
    
    def __str__(self):
        rs = "\nJe vroeg een lijst van de gebruikers:\n"
        for gebruiker in self.lijst:
            rs += f"{str(gebruiker.id)}: {gebruiker.voornaam} {gebruiker.naam}\n"
        return rs