class LogFile():
    def __init__(self, bestandsnaam):
        self.bestandsnaam = bestandsnaam
        self.bestand = open(self.bestandsnaam, "a")

    def schrijf(self, tekst):
        self.bestand.write(tekst)

    def sluit(self):
        self.bestand.close()


class Drank ():
    def __init__(self, naam, temperatuur=20):
        self.naam = naam
        self.temperatuur = temperatuur

    def log(self):
        print(f"Naam: {self.naam}, Temperatuur: {self.temperatuur}")
        logfile = LogFile("oefening1b-log.txt")
        logfile.schrijf(f"Naam: {self.naam}, Temperatuur: {self.temperatuur}\n")

oDrank1 = Drank("Seven-Up")
oDrank2 = Drank("Minute Maid", 16)
oDrank3 = Drank("Koffie",40)

dranklijstje = [oDrank1, oDrank2, oDrank3]

for drank in dranklijstje:
    drank.log()
