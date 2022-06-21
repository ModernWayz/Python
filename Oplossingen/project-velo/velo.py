import json
import random
import time
import shutil
from jinja2 import Environment, PackageLoader, select_autoescape
from station import Stations
from fiets import Fiets
from gebruiker import Gebruikers, voornamen_lijst, familienamen_lijst
from log import Log

class Velo():
    """ Een container-klasse voor alle andere klassen """
    AANTAL_FIETSEN = 3800
    AANTAL_GEBRUIKERS = 400
    SIMULATIE_INTERVAL = 0.2
    def __init__(self):
        self.stations = Stations()
        self.gebruikers = Gebruikers()
        self.initialiseer_stations()
        self.initialiseer_gebruikers()
        self.initialiseer_fietsen()
        self.fietsenden = []
        self.simulator_tijd = time.time()
        self.relatieve_tijd = time.time()
        self.simulator_factor = 1
        self.log_index = 1

    def terminal_interface_weergeven(self): # terminal interface van de toepassing
        keuze_string = "\nMaak een keuze:\n1: Toon gebruikersgegevens\n2: Toon stationsgegevens\n3: Fiets uitchecken\n4: Fiets terugzetten\n5: Simulatie-modus starten\n6: HTML-export maken\n0: Data opslaan en toepassing verlaten\nJouw keuze: "
        getal = int(input(keuze_string))
        while getal != 0:
            if getal == 1: # Toon gebruikersgegevens
                id_alle = int(input("Geef het id van de gebruiker of '0' om alle gebruikers te zien: "))
                if id_alle == 0:
                    print(self.gebruikers.geef_info_alle())
                else:
                    print(self.gebruikers.geef_info(int(id_alle)))
            elif getal == 2: # Toon stationsgegevens
                id_alle = int(input("Geef het id van het station of '0' om alle stations te zien: "))
                if id_alle == 0:
                    print(self.stations.geef_info_alle())
                else:
                    print(self.stations.geef_info(int(id_alle)))  
            elif getal == 3: # Fiets uitchecken 
                gebruiker_id = int(input("Geef het id van de gebruiker: "))
                station_id = int(input("Geef het id van de station: "))
                self.fiets_uitchecken(gebruiker_id, station_id, time.time())
            elif getal == 4: # Fiets teruggeven
                gebruiker_id = int(input("Geef het id van de gebruiker: "))
                station_id = int(input("Geef het id van de station: "))
                self.fiets_inchecken(gebruiker_id, station_id, time.time())
            elif getal == 5: #simulator
                factor = int(input("Aan welke snelheid dient de simulator te lopen (1=standaard, 5=5x sneller): "))
                print(f"\nSimulatie gestart aan snelheid x{factor} om {time.strftime('%d-%m %H:%M:%S', time.localtime(self.simulator_tijd))}. Druk op ctrl-c om de simulatie te stoppen\n")
                if self.simulator_tijd < time.time():
                    print("ja is kleiner")
                    self.simulator_tijd = time.time()
                self.relatieve_tijd = time.time()
                self.simulator_factor = factor
                try:
                    while True:
                        self.simuleer()
                except KeyboardInterrupt:
                    self.simulatie_beeindigen()
                    print(f"\nDe simulatie werd afgerond om {time.strftime('%d-%m %H:%M:%S', time.localtime(self.simulator_tijd))}\n")
            elif getal == 6: #HTML-export
                shutil.rmtree("_site/") # oude pagina's verwijderen
                shutil.copytree("assets/", "_site/assets/") # static assets toevoegen
                env = Environment(loader=PackageLoader('velo', 'templates'),autoescape=select_autoescape([]))
                bestand = "_site/index.html" # overzicht stations
                template = env.get_template('home.html')
                with open(bestand,"w") as bestand:
                    station_string = ""
                    for station in self.stations.lijst:
                        station_string += f"<li><a href='{station.id}.html'>{station.naam}</a></li>"
                    bestand.write(template.render(lijst_stations=station_string))
                for station in self.stations.lijst:
                    bestand = f"_site/{station.id}.html" # details stations
                    template = env.get_template('station.html')
                    with open(bestand,"w") as bestand:
                        slot_string = ""
                        nummer = 1
                        for slot in station.slots:
                            fiets = "-" if (slot.inhoud is None) else f"<span>Fiets #{slot.inhoud.id}</span>"             
                            slot_string += f"<li>{nummer}: {fiets}</li>"
                            nummer += 1
                        log_string = ""
                        for log in station.logs:
                            log_string += f"<li>{log.id}: {log.beschrijving} [T: {time.strftime('%d-%m %H:%M', time.localtime(log.tijdstempel))} | G: {log.gebruiker_id} | F: {log.fiets_id}]</li>"
                        bestand.write(template.render(titel=f"Station {station.naam}", slots = slot_string, logs = log_string))
            getal = int(input(keuze_string))

    def log_event(self, gebruiker_id, station_id, fiets_id, boodschap, richting, tijdstempel):
        self.stations.maak_log_aan(station_id, Log(self.log_index, gebruiker_id, station_id, fiets_id, boodschap, richting, tijdstempel))
        self.log_index += 1

    def fiets_uitchecken(self, gebruiker_id, station_id, tijdstempel = time.time()):
        if self.gebruikers.is_gebruiker_en_fiets_ontleenbaar(gebruiker_id) and self.stations.station_is_niet_leeg(station_id): 
            fiets = self.stations.fiets_uitchecken(station_id)
            self.gebruikers.plaats_fiets_op_kaart(gebruiker_id, fiets)
            boodschap = "Een gebruiker heeft een fiets met succes uitgeleend"
            self.log_event(gebruiker_id, station_id, fiets.id, boodschap, "uit", tijdstempel)
            print(f"{boodschap} [T: {time.strftime('%d-%m %H:%M:%S', time.localtime(tijdstempel))} | G: {gebruiker_id} | F: {fiets.id}]\n")
        else: 
            print("\nGebruiker bestaat niet of kan geen fiets ontlenen...\n")

    def fiets_inchecken(self, gebruiker_id, station_id, tijdstempel = time.time()):
        if self.gebruikers.is_gebruiker_en_fiets_teruggeefbaar(gebruiker_id) and self.stations.station_is_niet_volzet(station_id):
            fiets = self.gebruikers.fiets_van_kaart_nemen(gebruiker_id)
            self.stations.plaats_fiets_in_slot(station_id, fiets)
            boodschap = "Een gebruiker heeft een fiets met succes teruggebracht"
            self.log_event(gebruiker_id, station_id, fiets.id, boodschap, "in", tijdstempel)
            print(f"{boodschap} [T: {time.strftime('%d-%m %H:%M:%S', time.localtime(tijdstempel))} | G: {gebruiker_id} | F: {fiets.id}] | S: {station_id}\n")
        else:
            print("\nGebruiker bestaat niet, kan geen fiets teruggeven, of station is volzet\n")

    def simuleer(self): # simulatie uitvoeren
        simulatie_tijdstempel = ((time.time() - self.relatieve_tijd)* self.simulator_factor) + self.simulator_tijd
        willekeurige_gebruiker = self.gebruikers.geef_willekeurige_gebruiker_zonder_fiets()
        self.fietsenden.append(willekeurige_gebruiker)
        self.fiets_uitchecken(willekeurige_gebruiker, self.stations.geef_willekeurig_station_percent_gevuld("minimum", 25), simulatie_tijdstempel)
        if len(self.fietsenden) > 5:
            random.shuffle(self.fietsenden)
            self.fiets_inchecken(self.fietsenden.pop(), self.stations.geef_willekeurig_station_percent_gevuld("maximum", 50), simulatie_tijdstempel)
        time.sleep(self.SIMULATIE_INTERVAL)

    def simulatie_beeindigen(self): # na afloop simulatie fietsen terugzetten
        simulatie_tijdstempel = ((time.time() - self.relatieve_tijd)* self.simulator_factor) + self.simulator_tijd
        for _ in range(len(self.fietsenden)):
            self.fiets_inchecken(self.fietsenden.pop(), self.stations.geef_willekeurig_station_percent_gevuld("maximum", 80), simulatie_tijdstempel)
        self.simulator_tijd = ((time.time() - self.relatieve_tijd)* self.simulator_factor) + self.simulator_tijd

    def initialiseer_stations(self): # stations aanmaken
        bestand = open("velo.geojson")
        aan_te_maken_stations = json.load(bestand)
        for aan_te_maken_station in aan_te_maken_stations["features"]:
            self.stations.toevoegen(aan_te_maken_station["properties"]["Straatnaam"], int(aan_te_maken_station["properties"]["Aantal_plaatsen"]))
    
    def initialiseer_gebruikers(self): # gebruikers aanmaken
        for _ in range(Velo.AANTAL_GEBRUIKERS):
            self.gebruikers.toevoegen(random.choice(voornamen_lijst()), random.choice(familienamen_lijst()))

    def initialiseer_fietsen(self): # fietsen aanmaken
        slot_lijst = []
        for station in self.stations.lijst:
            for slot in station.slots:
                slot_lijst.append(slot)
        sample_slot_lijst = random.sample(slot_lijst, k=Velo.AANTAL_FIETSEN)
        for getal in range(Velo.AANTAL_FIETSEN):
            sample_slot_lijst[getal].fiets_toevoegen(Fiets())
