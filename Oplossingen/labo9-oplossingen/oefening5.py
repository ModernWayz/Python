class Envelop():
    frankeerfactor = 10

    def __init__(self, gewicht, is_verstuurd=False):
        self.gewicht = gewicht
        self.is_verstuurd = is_verstuurd
        self.is_voldoende_gefrankeerd = False
        self.portokosten = 0

    def verstuur(self):
        if self.is_voldoende_gefrankeerd:
            self.is_verstuurd = True

    def frankeer(self, portokosten):
        if self.portokosten >= self.gewicht * self.frankeerfactor:
            self.is_voldoende_gefrankeerd = True

    def portokosten_nodig(self):
        self.portokosten = self.gewicht * self.frankeerfactor
        return f"De portokosten voor deze envelop bedragen {self.portokosten}eur"

    def __repr__(self):
        return f"Deze enveloppe werd {'' if self.is_verstuurd else 'nog niet '}verstuurd."


class GroteEnvelop(Envelop):
    frankeerfactor = 15




oEnvelop1 = Envelop(100)
print(oEnvelop1)
print(oEnvelop1.portokosten_nodig())
oEnvelop1.frankeer(1000)
oEnvelop1.verstuur()
print(oEnvelop1)

oEnvelop2 = GroteEnvelop(100)
print(oEnvelop2)
print(oEnvelop2.portokosten_nodig())
oEnvelop2.frankeer(1500)
oEnvelop2.verstuur()
print(oEnvelop2)
