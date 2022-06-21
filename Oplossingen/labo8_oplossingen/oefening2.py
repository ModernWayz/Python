class Bolletje():
    def __init__(self, smaak):
        self.smaak = smaak

class Hoorntje():
    def __init__(self):
        self.bolletjes = []

    def bolletjes_toevoegen(self, *nieuwe_bolletjes):
        for één_bolletje in nieuwe_bolletjes:
            self.bolletjes.append(één_bolletje)

    def één_bolletje_toevoegen(self, nieuw_bolletje):
        self.bolletjes.append(nieuw_bolletje)

    def __str__(self):
        #BETER ZOU ZIJN: return "\n".join(b.smaak for b in self.bolletjes) 
        # een Python list comprehension: zien we nog!
        # https://realpython.com/list-comprehension-python/
        returnlist = []
        for b in self.bolletjes:
            returnlist.append(b.smaak)
        return "\n".join(returnlist)

oBolletje1 = Bolletje('pistache')
oBolletje2 = Bolletje('speculoos')
oBolletje3 = Bolletje('vanille')
oBolletje4 = Bolletje('chocolade')

oHoorntje1 = Hoorntje()
oHoorntje1.één_bolletje_toevoegen(oBolletje4)
oHoorntje1.bolletjes_toevoegen(oBolletje1, oBolletje2)
oHoorntje1.bolletjes_toevoegen(oBolletje3)
print(oHoorntje1)