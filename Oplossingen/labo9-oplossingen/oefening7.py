class Brood():
    def __init__(self):
        # voedingswaarde per sneetje
        self.energie = 66
        self.eiwit = 3.2
        self.koolhydraten = 16.8
        self.suiker = 0.8
        self.vet = 0.6

    def eet_sneetjes(self, sneetjes):
        mijndict = {"Energie": self.energie*sneetjes, "Eiwit": self.eiwit * sneetjes, "Koolhydraten": self.koolhydraten * sneetjes, "Suikers": self.suiker * sneetjes, "Vet": self.vet * sneetjes}
        return mijndict

class VolkorenBrood(Brood):
    def __init__(self):
        super().__init__()
        self.energie = 82
        self.eiwit = 3.8
        self.koolhydraten = 13.7
        self.suiker = 0.7
        self.vet = 0.7

class ZuurdesemBrood(Brood):
    def __init__(self):
        super().__init__()
        self.energie = 118
        self.eiwit = 4.7
        self.koolhydraten = 20.2
        self.suiker = 1.1
        self.vet = 1.3

oBrood1 = Brood()
oVolkorenBrood1 = VolkorenBrood()
oZuurdesemBrood1 = ZuurdesemBrood()

print(oBrood1.eet_sneetjes(2))
print(oVolkorenBrood1.eet_sneetjes(3))
print(oZuurdesemBrood1.eet_sneetjes(5))



