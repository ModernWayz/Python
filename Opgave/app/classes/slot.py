class Slot():
    def __init__(self, id, velo = None): 
        self.id = id
        self.velo = velo
    
    def __str__(self):
        return str(self.__dict__)

    def addVelo(self, velo):
        self.velo = velo

    def removeVelo(self):
        velo = self.velo
        self.velo = None
        return velo

    def isOccupied(self):
        if(self.velo != None):
            return True
        return False