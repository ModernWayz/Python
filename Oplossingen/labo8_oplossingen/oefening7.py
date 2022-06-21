class Dier():
    def __init__(self, kleur, aantal_poten):
        self.soort = self.__class__.__name__.lower()
        self.kleur = kleur
        self.aantal_poten = aantal_poten

    def __repr__(self):
        return f"{self.soort}, kleur: {self.kleur}, {self.aantal_poten} poten"


class Wolf(Dier):
    def __init__(self, kleur):
        super().__init__(kleur, 4)

class Schaap(Dier):
    def __init__(self, kleur):
        super().__init__(kleur, 4)

class Slang(Dier):
    def __init__(self, kleur):
        super().__init__(kleur, 0)

class Papegaai(Dier):
    def __init__(self, kleur):
        super().__init__(kleur, 2)

class Kooi():
    def __init__(self, identificatienummer):
        self.identificatienummer = identificatienummer
        self.dieren = []

    def voeg_dieren_toe(self, *dieren):
        for één_dier in dieren:
            self.dieren.append(één_dier)

    def __repr__(self):
        output = f"Kooi {self.identificatienummer}\n"
        output += '\n'.join('\t' + str(dier)
                            for dier in self.dieren)
        return output


class Dierentuin():
    def __init__(self):
        self.kooien = []

    def voeg_kooien_toe(self, *kooien):
        for kooi in kooien:
            self.kooien.append(kooi)

    def __repr__(self):
        return '\n'.join(str(één_kooi) for één_kooi in self.kooien)
         # is een list comprehension - zie oefening 2 voor de minder pythonic-oplossing

    def dieren_met_kleur(self, kleur):
        # BETER: LIST COMPREHENSION GEBRUIKEN
        #return [één_dier
        #        for één_kooi in self.kooien
        #       for één_dier in één_kooi.dieren
        #       if één_dier.kleur == kleur]
        returnwaarde = []
        for één_kooi in self.kooien:
            for één_dier in één_kooi.dieren:
                if één_dier.kleur == kleur:
                    returnwaarde.append(één_dier)
        return returnwaarde

    def dieren_met_aantal_poten(self, aantal_poten):
        return [één_dier
                for één_kooi in self.kooien
                for één_dier in één_kooi.dieren
                if één_dier.aantal_poten == aantal_poten]

    def totaal_aantal_poten(self):
        return sum(één_dier.aantal_poten
                   for één_kooi in self.kooien
                   for één_dier in één_kooi.dieren)

oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSchaap2 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')

print(oWolf1)
print(oSchaap1)
print(oSlang1)
print(oPapegaai1)

oKooi1 = Kooi(1)
oKooi1.voeg_dieren_toe(oWolf1, oSchaap1, oSchaap2)

oKooi2 = Kooi(2)
oKooi2.voeg_dieren_toe(oSlang1, oPapegaai1)

oDierentuin1 = Dierentuin()
oDierentuin1.voeg_kooien_toe(oKooi1, oKooi2)

print(oDierentuin1)
print(oDierentuin1.dieren_met_kleur('zwart'))
print(oDierentuin1.dieren_met_aantal_poten(4))
print(oDierentuin1.totaal_aantal_poten())