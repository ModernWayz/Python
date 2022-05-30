class Gebruiker():
    def __init__(self, naam, familieNaam, velo = None): 
        self.naam = naam
        self.familieNaam = familieNaam
        self.velo = velo

    def __str__(self):
        return str(self.__dict__)

    def veloOntlenen(self, station):
        if(station.getAmountVelos() > 0):
            for slot in station.slots:
                if(slot.isOccupied() == True):
                    self.velo = slot.removeVelo()
                    break

    def veloInchecken(self, station, velo):
        if(station.getOccupiedSlots() < int(station.aantalPlaatsen)):
            station.addVelo(velo)
            self.velo = None