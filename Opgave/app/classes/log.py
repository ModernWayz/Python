class Log():
    def __init__(self, action, station = None, gebruiker = None, velo = None, transporteur = None, amount = 1, logtime = None):
        self.action = action
        self.station = station
        self.gebruiker = gebruiker
        self.velo = velo
        self.transporteur = transporteur
        self.amount = amount
        self.logtime = logtime
    
    def __str__(self):            
        return str(self.__dict__)