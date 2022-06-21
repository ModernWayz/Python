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

oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')

print(oWolf1)
print(oSchaap1)
print(oSlang1)
print(oPapegaai1)