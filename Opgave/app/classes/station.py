from classes.slot import Slot

class Station():
    def __init__(self, x, y, objectId, objectType, typeVelo, ligging, straatNaam, huisNummer, aanvulling, district, postCode, objectCode, gebruik, aantalPlaatsen): 
        self.x = x
        self.y = y
        self.objectId = objectId
        self.objectType = objectType
        self.typeVelo = typeVelo
        self.ligging = ligging
        self.straatNaam = straatNaam
        self.huisNummer = huisNummer
        self.aanvulling = aanvulling
        self.district = district
        self.postCode = postCode
        self.objectCode = objectCode
        self.gebruik = gebruik
        self.aantalPlaatsen = aantalPlaatsen
        self.slots = []

        if(gebruik == 'IN_GEBRUIK'):
            for i in range(int(aantalPlaatsen)):
                    slot = Slot(i)
                    self.slots.append(slot)

    def __str__(self):
        return str(self.__dict__)

    def addSlot(self, slot):
        if(len(self.slots) <= int(self.aantalPlaatsen)):
            self.slots.append(slot)

    def addVelo(self, velo):
        for slot in self.slots:
            if(slot.isOccupied() == False):
                slot.addVelo(velo)
                break
            
    def removeVelo(self, velo):
        for slot in self.slots:
            if(slot.isOccupied() == True):
                slot.removeVelo(velo)
                break

    def getOccupiedSlots(self):
        occupiedSlots = 0
        for slot in self.slots:
            if(slot.isOccupied()):
                occupiedSlots += 1
        return occupiedSlots

    def getAmountVelos(self):
        velos = 0
        for slot in self.slots:
            if(slot.isOccupied() == True):
                velos += 1
        return velos