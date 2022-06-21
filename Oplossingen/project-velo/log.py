import time

class Log():
    """ Klasse Log: bestaat uit id, beschrijving, tijdstempel """
    def __init__(self, id, gebruiker_id, station_id, fiets_id, beschrijving, richting = "uit", tijdstempel = time.time()):
        self.id = id
        self.gebruiker_id = gebruiker_id 
        self.station_id = station_id
        self.fiets_id = fiets_id
        self.beschrijving = beschrijving
        self.richting = richting
        self.tijdstempel = tijdstempel


