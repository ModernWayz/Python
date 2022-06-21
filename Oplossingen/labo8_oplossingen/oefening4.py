class Bolletje():
    def __init__(self, smaak):
        self.smaak = smaak

class Hoorntje():
    maximum_bolletjes = 3

    def __init__(self):
        self.bolletjes = []

    def bolletjes_toevoegen(self, *nieuwe_bolletjes):
        for één_bolletje in nieuwe_bolletjes:
            if len(self.bolletjes) < self.maximum_bolletjes:
                self.bolletjes.append(één_bolletje)

    def __repr__(self):
        return '\n'.join(s.smaak for s in self.bolletjes)

class Reuzehoorntje(Hoorntje):
    maximum_bolletjes = 5

oBolletje1 = Bolletje('pistache')
oBolletje2 = Bolletje('kersen')
oBolletje3 = Bolletje('vanille')
oBolletje4 = Bolletje('passievrucht')
oBolletje5 = Bolletje('speculoos')

oReuzeHoorntje1 = Reuzehoorntje()
oReuzeHoorntje1.bolletjes_toevoegen(oBolletje1, oBolletje2)
oReuzeHoorntje1.bolletjes_toevoegen(oBolletje3)
oReuzeHoorntje1.bolletjes_toevoegen(oBolletje4, oBolletje5)
print(oReuzeHoorntje1)