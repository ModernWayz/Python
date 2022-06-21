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


class Dierentuin():
    def __init__(self):
        self.kooien = []

    def voeg_kooien_toe(self, *kooien):
        for een_kooi in kooien:
            self.kooien.append(een_kooi)

    def __repr__(self):
        return '\n'.join(str(een_kooi)
                         for een_kooi in self.kooien)


    def totaal_aantal_poten(self):
        return sum(een_dier.aantal_poten
                   for een_kooi in self.kooien
                   for een_dier in een_kooi.dieren)

    def geef_dieren(self, **kwargs):
        print(f'{kwargs=}')
        return [een_dier
                for een_kooi in self.kooien
                for een_dier in een_kooi.dieren
                if (('kleur' in kwargs and een_dier.kleur == kwargs['kleur']) and
                    ('poten' in kwargs and een_dier.aantal_poten == kwargs['poten']))]

    def verhuis_dier(self, ontvangende_dierentuin, soort):
        for een_kooi in self.kooien:
            for een_dier in een_kooi.dieren:
                if isinstance(een_dier, soort):
                    een_kooi.dieren.remove(een_dier)
                    ontvangende_dierentuin.kooien[0].voeg_dieren_toe(een_dier)

oWolf1 = Wolf('grijs')
oSchaap1 = Schaap('zwart')
oSlang1 = Slang('groen')
oPapegaai1 = Papegaai('rood')
oWolf2 = Wolf('wit')

oDierentuin1 = Dierentuin()
oDierentuin2 = Dierentuin()

oGroteKooi1 = GroteKooi(1,35)
oGroteKooi2 = GroteKooi(2, 35)

oDierentuin1.voeg_kooien_toe(oGroteKooi1)
oDierentuin2.voeg_kooien_toe(oGroteKooi2)

oGroteKooi1.voeg_dieren_toe(oWolf1)
oGroteKooi1.voeg_dieren_toe(oPapegaai1)
oGroteKooi2.voeg_dieren_toe(oSchaap1)

print(oDierentuin1.kooien[0].dieren)
print(oDierentuin2.kooien[0].dieren)


oDierentuin1.verhuis_dier(oDierentuin2,Papegaai)

print(oDierentuin1.kooien[0].dieren)
print(oDierentuin2.kooien[0].dieren)