from classes.gebruiker import Gebruiker

class Transporteur(Gebruiker):
    def __init__(self, naam, familieNaam): 
        super().__init__(naam, familieNaam)
        self.velos = []
    
    def velosOntlenen(self, station, amount):
        for i in range(amount):
            for slot in station.slots:
                if(slot.isOccupied() == True):
                    self.velos.append(slot.removeVelo())
                    break

    def velosInchecken(self, station, amount):
        for i in range(amount):
            if(station.getOccupiedSlots() < int(station.aantalPlaatsen)):
                station.addVelo(self.velos[0])
                self.velos.pop(0)