import random
import time
from slot import Slot

class Station():
    """ Klasse Station: bestaat uit id, naam, slots en logs """
    def __init__(self, id, naam):
        self.id = id
        self.naam = naam
        self.slots = []
        self.logs = []

    def slot_toevoegen(self):
        self.slots.append(Slot())


class Stations():
    """ Klasse Stations: bevat station-objecten in lijst alsook verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, naam, aantal_slots):
        nieuw_station = Station(self.index, naam)
        for _ in range(aantal_slots):
            nieuw_station.slot_toevoegen()
        self.lijst.append(nieuw_station) # toevoegen
        self.index += 1	# ga naar volgende ID

    def geef_info(self, id):
        return_data = "\n"
        station = [s for s in self.lijst if (s.id == id)][0]
        return_data += f"{station.id}: {station.naam}\n"
        return_data += "\nSlots:\n"
        nummer = 1
        for slot in station.slots:       
            fiets = "Leeg" if (slot.inhoud is None) else f"Fiets {slot.inhoud.id}"              
            return_data += f"{nummer}: {fiets}\n"
            nummer += 1
        return_data += "\nLogs:\n"
        for log in station.logs:
            return_data += f"{log.id}: {log.beschrijving} [T: {time.strftime('%d-%m %H:%M', time.localtime(log.tijdstempel))} | G: {log.gebruiker_id} | F: {log.fiets_id}]\n"
        return return_data
    
    def geef_info_alle(self):
        return_data = "\n"
        for station in self.lijst:
            return_data += f"{station.id}: {station.naam}\n"
            nummer = 1
            for slot in station.slots:       
                fiets = "Leeg" if (slot.inhoud is None) else f"Fiets {slot.inhoud.id}"              
                return_data += f"\t{nummer}: {fiets}\n"
                nummer += 1
        return return_data

    def fiets_uitchecken(self, id):
        station = [s for s in self.lijst if (s.id == id)]
        volle_slots = [s for s in station[0].slots if (s.inhoud is not None)]
        slot = random.choice(volle_slots) # een willekeurig slot vrijgeven
        return_fiets = slot.inhoud
        slot.inhoud = None
        return return_fiets

    def plaats_fiets_in_slot(self, id, fiets):
        station = [s for s in self.lijst if (s.id == id)]
        lege_slots = [s for s in station[0].slots if (s.inhoud is None)]
        slot = random.choice(lege_slots)
        slot.inhoud = fiets

    def station_is_niet_volzet(self, id):
        station = [s for s in self.lijst if (s.id == id)]
        lege_slots = [s for s in station[0].slots if (s.inhoud is None)]
        return True if len(lege_slots) > 0 else False
    
    def station_is_niet_leeg(self, id):
        station = [s for s in self.lijst if (s.id == id)]
        volle_slots = [s for s in station[0].slots if (s.inhoud is not None)]
        return True if len(volle_slots) > 0 else False

    def geef_willekeurig_station_percent_gevuld(self, min_of_max, percentage):
        lijst_van_stations = []
        for station in self.lijst:
            volle_slots = 0
            totaal = 0
            for slot in station.slots:
                totaal += 1
                if slot.inhoud is not None:
                    volle_slots += 1
            if min_of_max == "minimum":
                if ((volle_slots / totaal) * 100) >= percentage:
                    lijst_van_stations.append(station)
            else:
                if ((volle_slots / totaal) * 100) <= percentage:
                    lijst_van_stations.append(station)
        return random.choice(lijst_van_stations).id

    def maak_log_aan(self, id, log): # log object toevoegen aan station.logs
        station = [s for s in self.lijst if (s.id == id)]
        station[0].logs.insert(0, log) 





    