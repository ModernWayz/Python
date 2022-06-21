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
    ruimte_nodig = 10
    geluid = 'awoooh'
    def __init__(self, kleur):
        super().__init__(kleur)


class Schaap(VierpotigDier):
    ruimte_nodig = 5
    geluid = 'baaah'
    def __init__(self, kleur):
        super().__init__(kleur)


class Slang(NulpotigDier):
    ruimte_nodig = 2
    geluid = 'sisss'
    def __init__(self, kleur):
        super().__init__(kleur)


class Papegaai(TweepotigDier):
    ruimte_nodig = 1
    geluid = 'koppie krauw'
    def __init__(self, kleur):
        super().__init__(kleur)


dier_veiligheid = {Wolf: [Wolf, Slang, Papegaai],
                 Schaap: [Schaap, Slang, Papegaai],
                 Slang: [Wolf, Schaap],
                 Papegaai: [Wolf, Schaap]}

class Kooi():
    maximum_aantal_dieren = 3

    def __init__(self, identificatienummer, totale_ruimte):
        self.identificatienummer = identificatienummer
        self.dieren = []
        self.totale_ruimte = totale_ruimte

    def voeg_dieren_toe(self, *dieren):
        for een_dier in dieren:
            for huidige_bewoner in self.dieren:
                if (self.ruimte_gebruikt() + een_dier.ruimte_nodig > self.totale_ruimte) or type(een_dier) not in dier_veiligheid[type(huidige_bewoner)]:
                    raise Exception
            if (len(self.dieren) < self.maximum_aantal_dieren):
                self.dieren.append(een_dier)

    def ruimte_gebruikt(self):
        return sum(een_dier.ruimte_nodig
                   for een_dier in self.dieren)

    def __repr__(self):
        output = f"Kooi {self.identificatienummer}\n"
        output += '\n'.join('\t' + str(dier)
                            for dier in self.dieren)
        return output

class GroteKooi(Kooi):
    maximum_aantal_dieren = 6


oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')
oWolf2 = Wolf('wit')

oKooi1 = Kooi(1,25)
oGroteKooi1 = GroteKooi(2,35)


oKooi1.voeg_dieren_toe(oWolf1)
oKooi1.voeg_dieren_toe(oSlang1)
oKooi1.voeg_dieren_toe(oWolf2)
oGroteKooi1.voeg_dieren_toe(oSchaap1)
oGroteKooi1.voeg_dieren_toe(oPapegaai1)
print(oKooi1.dieren)
print(oKooi1.ruimte_gebruikt())
print(oGroteKooi1.dieren)
print(oGroteKooi1.ruimte_gebruikt())
