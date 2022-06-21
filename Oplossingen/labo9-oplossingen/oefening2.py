class Boek ():
    def __init__(self, titel, auteur, prijs, dikte):
        self.titel = titel
        self.auteur = auteur
        self.prijs = prijs
        self.dikte = dikte

class Kast():
    def __init__(self, beschikbare_ruimte):
        self.boeken = []
        self.ingenomen_ruimte = 0
        self.beschikbare_ruimte = beschikbare_ruimte

    def voeg_boek_toe(self, boek):
        if self.ingenomen_ruimte + boek.dikte > self.beschikbare_ruimte:
            return False
        self.boeken.append(boek)
        self.ingenomen_ruimte += boek.dikte
        return True

    def totale_prijs(self):
        return sum(boek.prijs
                   for boek in self.boeken)

    def bevat_boek(self, titel):
        for boek in self.boeken:
            if titel == boek.titel:
                return True
        return False

    def geef_boeken(self):
        # zelf toegevoegd ;-)
        boekenlijst = ""
        for boek in self.boeken:
            boekenlijst += f"{boek.auteur}, {boek.titel}, {boek.prijs}eur, {boek.dikte}cm.\n"
        return boekenlijst


oBoek1 = Boek("A Brave New World", "Aldous Huxley", 20, 3)
oBoek2 = Boek("Ulysses", "James Joyce", 22, 4)
oBoek3 = Boek("The Great Gatsby", "F. Scott Fitzgerald", 19, 2)
oBoek4 = Boek("Moby Dick", "Herman Melville", 20, 3)
oBoek5 = Boek("Hamlet", "William Shakespeare", 20, 3)

mijnboeken = [oBoek1, oBoek2, oBoek3, oBoek4, oBoek5]
oKast1 = Kast(10)

for boek in mijnboeken:
    oKast1.voeg_boek_toe(boek)

print(oKast1.totale_prijs())
print(oKast1.bevat_boek("A Brave New World"))
print(oKast1.geef_boeken())



