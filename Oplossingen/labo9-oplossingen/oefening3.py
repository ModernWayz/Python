class Persoon():
    populatie = 0

    def __init__(self, naam):
        self.naam = naam
        # je kan hier ook schrijven: Persoon.populatie
        self.__class__.populatie += 1

    def __del__(self):
        self.__class__.populatie -= 1

    def __repr__(self):
        return f"Persoon {self.naam} is onderdeel van een totale populatie van {self.__class__.populatie} personen\n"


oPersoon1 = Persoon("Kristof Michiels")
oPersoon2 = Persoon("Nina Michiels")
oPersoon3 = Persoon("Kai Michiels")

print(oPersoon1)

del oPersoon1

print(oPersoon2)