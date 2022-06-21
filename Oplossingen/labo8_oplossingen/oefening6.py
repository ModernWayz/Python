class Dier():
    def __init__(self, kleur, aantal_poten):
        self.soort = self.__class__.__name__
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
        output += '\n'.join('\t' + str(dier) for dier in self.dieren) 
        # is een list comprehension - zie oefening 2 voor de minder pythonic-oplossing
        return output


oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')

oKooi1 = Kooi(1)
oKooi1.voeg_dieren_toe(oWolf1, oSchaap1)

oKooi2 = Kooi(2)
oKooi2.voeg_dieren_toe(oSlang1, oPapegaai1)

print(oKooi1)
print(oKooi2)