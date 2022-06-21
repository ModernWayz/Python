class Boek ():
    def __init__(self, titel, auteur, prijs, dikte):
        self.titel = titel
        self.auteur = auteur
        self.prijs = prijs
        self.dikte = dikte

class Schap():
    def __init__(self, beschikbare_ruimte):
        self.boeken = []
        self.beschikbare_ruimte = beschikbare_ruimte
        self.ingenomen_ruimte = 0

    def voeg_boek_toe(self, boek):
        if self.ingenomen_ruimte + boek.dikte > self.beschikbare_ruimte:
            return False
        self.boeken.append(boek)
        self.ingenomen_ruimte += boek.dikte
        return True

class Kast():
    def __init__(self):
        self.schappen = []

    def voeg_schap_toe(self, schap):
        self.schappen.append(schap)

    def totale_prijs(self):
        totale_waarde = 0
        for schap in self.schappen:
            for boek in schap.boeken:
                totale_waarde += boek.prijs
        return totale_waarde

    def bevat_boek(self, titel):
        for schap in self.schappen:
            for boek in schap.boeken:
                if titel == boek.titel:
                    return True
        return False

    def geef_boeken(self):
        # zelf toegevoegd ;-)
        boekenlijst = ""
        for schap in self.schappen:
            for boek in schap.boeken:
                boekenlijst += f"{boek.auteur}, {boek.titel}, {boek.prijs}eur, {boek.dikte}cm.\n"
        return boekenlijst


oBoek1 = Boek("A Brave New World", "Aldous Huxley", 20, 3)
oBoek2 = Boek("Ulysses", "James Joyce", 22, 4)
oBoek3 = Boek("The Great Gatsby", "F. Scott Fitzgerald", 19, 2)
oBoek4 = Boek("Moby Dick", "Herman Melville", 20, 3)
oBoek5 = Boek("Hamlet", "William Shakespeare", 20, 3)

oBoek6 = Boek("A Brave New World", "Aldous Huxley", 20, 3)

mijnboeken = [oBoek1, oBoek2, oBoek3, oBoek4, oBoek5]
oKast1 = Kast()
oSchap1 = Schap(15)
oSchap2 = Schap(15)
oKast1.voeg_schap_toe(oSchap1)
oKast1.voeg_schap_toe(oSchap2)
for boek in mijnboeken:
    oSchap1.voeg_boek_toe(boek)
oSchap2.voeg_boek_toe(oBoek6)

print(oKast1.totale_prijs())
print(oKast1.bevat_boek("A Brave New World"))
print(oKast1.geef_boeken())