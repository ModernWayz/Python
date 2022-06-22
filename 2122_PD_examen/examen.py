import random
import sqlite3

DATABANK_PATH = "2122_PD_examen/examen.db"

class Opdracht():
    """ Klasse Opdracht: bestaat uit ... """
    # vul zelf in
    def __init__(self, aantalPanelen):
        FAMILIES = ["Peeters", "Janssens", "Maes", "Jacobs", "Mertens", "Willems", "Claes", "Wouters", "Goossens", "Dubois", "Vermeulen", "Pauwels", "Hermans", "Lambert", "Aerts", "Michiels", "Dupont", "Martens", "Smets", "Martin", "Desmet", "Hendrickx", "Claeys", "Devos", "Janssen", "Stevens", "Dumont", "Segers", "Lemmens", "Leroy", "Coppens", "Simon", "Wauters", "Laurent", "Leclercq", "Renard", "Denis", "Verhoeven", "Lejeune", "Cools", "Declercq", "Thomas", "Petit", "Charlier", "Lemaire", "Smet", "Timmermans", "Michel", "Vandenberghe", "Thys", "Bertrand", "Lenaerts", "Cornelis", "Depauw", "Bauwens", "Verheyen", "Lefebvre", "Mathieu", "Carlier", "Evrard", "Baert", "Verstraete", "Moens", "Lauwers", "Bernard", "Lambrechts", "Bosmans", "Bogaert", "Geerts", "Fontaine", "Bogaerts", "Verlinden", "Gerard", "Christiaens", "Deprez", "Verbeke", "Vermeiren", "Marchal", "Verschueren", "Beckers", "Legrand", "Jansen", "Wuyts", "Adam", "Simons", "Verstraeten", "Collard", "Moreau", "Verhaeghe", "Claessens", "Mahieu", "Vermeersch", "Vandamme", "Thijs", "Henry", "Robert", "Pieters", "Heylen", "De groote", "Verhaegen", "Ceulemans", "Goethals", "Lievens", "François", "Vandevelde", "Callens", "Noel", "Servais", "Bastin", "Leemans", "Verbruggen", "Verhelst", "Roels", "Vercammen", "Gielen", "Somers", "Luyten", "Daems", "Matthys", "Vandewalle", "Mortier", "Vercauteren", "Verdonck", "Herman", "Swinnen", "Smeets", "Andries", "Vervoort", "Nys", "Meert", "Vos", "Claus", "Dewulf", "Verheyden", "Coenen", "Lecomte", "Smits", "Deckers"]
        self.familie = FAMILIES[random.randint(0, len(FAMILIES) -1)]
        self.aantalPanelen = aantalPanelen
        self.drones = []

    def __str__(self):
        return f"Familie {self.familie} [aantal panelen={self.aantalPanelen}]"

    def voeg_drone_toe(self, drone):
        self.drones.append(drone)
        
class Drone():
    """ Klasse Drone: bestaat uit ... """
    # vul zelf in
    def __init__(self):
        NAAMLIJST = ["Cleaner", "Servicer", "Washer Man", "Panel Man", "Shiner", "Sparkles", "Dirty Bird", "Poop Chute", "Nemesis", "Miss Ruby", "Darth Videous", "Night Fury", "Proteus", "Bumbles", "Pulsar", "Dronesy", ]
        self.naam = NAAMLIJST[random.randint(0, len(NAAMLIJST) -1)]
        self.capaciteit = 1
        self.aantalKeerGebruikt = 0

    def __str__(self):
        return f"{self.naam} [capaciteit={self.capaciteit}]"

    def gebruik_drone(self):
        self.aantalKeerGebruikt += 1


class DroneXL(Drone):
    """ Klasse DroneXL: bestaat uit ... """
    # vul zelf in
    def __init__(self):
        super().__init__()
        self.naam += " XL"
        self.capaciteit = 2

    def __str__(self):
        return super().__str__()

    
class Drone_zilla():
    """ Een container-klasse voor alle andere klassen """
    # vul zelf in
    def __init__(self):
        self.drones = []
        self.opdrachten = []
    
    def initialiseer_drones_en_opdrachten(self, aantalDrones = 20, aantalOpdrachten = 100):
        # Maak 20 (of parameter) random drones aan
        for _ in range(aantalDrones):
            if random.randint(0, 1) == 0:
                self.drones.append(Drone())
            else:
                self.drones.append(DroneXL())
        # Maak 100 (of parameter) random opdrachten aan
        for _ in range(aantalOpdrachten):
            self.opdrachten.append(Opdracht(random.randint(1, 5)))

    def opdrachten_en_drones_matchen(self):
        maxGebruik = 0
        for opdracht in self.opdrachten:
            capaciteitNodig = opdracht.aantalPanelen
            while(capaciteitNodig != 0):
                for drone in random.sample(self.drones, len(self.drones)):
                    if(capaciteitNodig > 0 and capaciteitNodig - drone.capaciteit >= 0 and drone.aantalKeerGebruikt <= maxGebruik):
                        opdracht.voeg_drone_toe(drone)
                        drone.gebruik_drone()
                        capaciteitNodig -= drone.capaciteit
                    elif(capaciteitNodig == 0):
                        break
                maxGebruik += 1

    def rapporteer_naar_terminal(self):
        print("Overzicht per opdracht\n----------------------\n")
        count = 1
        for opdracht in self.opdrachten:
            print(str(count) + ":", opdracht)
            for drone in opdracht.drones:
                print("\t", drone)
            count += 1

    def schrijf_weg_naar_db(self):
        # Connectie maken
        connect = sqlite3.connect(DATABANK_PATH)
        cursor = connect.cursor()

        # Verwijder vorige batch opdrachten van db
        sql = "DELETE FROM opdrachten"
        cursor.execute(sql)

        # Opdrachten naar db schrijven
        count = 1
        for opdracht in self.opdrachten:
            droneList = ' '.join(str(drone) for drone in opdracht.drones)
            sql = f"INSERT INTO opdrachten (id, naam, aantal_panelen, drone_lijst) VALUES({count}, '{opdracht.familie}', {opdracht.aantalPanelen}, '{droneList}');"
            cursor.execute(sql)
            connect.commit()
            count += 1

        # Bekijk de waardes voor test (commented)
        # sql = "SELECT * FROM opdrachten"
        # alle_rijen = cursor.execute(sql).fetchall()
        # for rij in alle_rijen:
        #     print(rij)

        # Connectie sluiten
        try:
            cursor.close()
            connect.close()
        except sqlite3.ProgrammingError:
            pass

def main():
    # niets in wijzigen: gebruik de methods om de deelopdrachten te maken
    drone_zilla = Drone_zilla()
    drone_zilla.initialiseer_drones_en_opdrachten()
    drone_zilla.opdrachten_en_drones_matchen()
    drone_zilla.rapporteer_naar_terminal()
    drone_zilla.schrijf_weg_naar_db()

main()