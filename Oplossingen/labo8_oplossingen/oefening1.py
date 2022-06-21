class Bolletje():
    def __init__(self, smaak):
        self.smaak = smaak
    def __str__(self):
        return self.smaak

def maak_bolletjes():
    bolletjes = [Bolletje('pistache'),
              Bolletje('speculoos'),
              Bolletje('vanille')]
    for bolletje in bolletjes:
        print(bolletje)

maak_bolletjes()