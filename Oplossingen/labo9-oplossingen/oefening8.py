class Dier():
    def __init__(self, kleur):
        self.soort = self.__class__.__name__
        self.kleur = kleur

    def __repr__(self):
        return f"{self.soort}, kleur: {self.kleur}, {self.aantal_poten} poten, maakt volgend geluid: {self.geluid}"


class NulpotigDier(Dier):
    def __init__(self, kleur):
        super().__init__(kleur)
        self.aantal_poten = 0


class TweepotigDier(Dier):
    def __init__(self, kleur):
        super().__init__(kleur)
        self.aantal_poten = 2


class VierpotigDier(Dier):
    def __init__(self, kleur):
        super().__init__(kleur)
        self.aantal_poten = 4


class Wolf(VierpotigDier):
    geluid = 'awoooh'

    def __init__(self, kleur):
        super().__init__(kleur)


class Schaap(VierpotigDier):
    geluid = 'baaah'

    def __init__(self, kleur):
        super().__init__(kleur)


class Slang(NulpotigDier):
    geluid = 'sisss'

    def __init__(self, kleur):
        super().__init__(kleur)


class Papegaai(TweepotigDier):
    geluid = 'koppie krauw'

    def __init__(self, kleur):
        super().__init__(kleur)


oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')

print(oWolf1)
print(oSchaap1)
print(oSlang1)
print(oPapegaai1)




