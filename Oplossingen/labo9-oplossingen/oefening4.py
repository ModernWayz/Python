class Transactie():
    balans = 0

    def __init__(self, bedrag):
        # geef een positief getal voor een storting en een negatief getal voor een opname
        self.bedrag = bedrag
        self.__class__.balans += bedrag

    def __repr__(self):
            return f"Deze transactie vertegenwoordigt een {'storting' if (self.bedrag > 0) else 'opname'} van {abs(self.bedrag)}. De huidige balans bedraagt {self.__class__.balans}.\n"


oTransactie1 = Transactie(200)
oTransactie2 = Transactie(100)
oTransactie3 = Transactie(-50)
print(oTransactie3)