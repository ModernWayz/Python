from gebruiker import Gebruikers
from film import Films
from cinema import Cinemas
from voorstelling import Voorstellingen

class Filmzalen():
    """ Een container-klasse voor alle andere klassen """
    def __init__(self):
        self.gebruikers = Gebruikers()
        self.films = Films()
        self.cinemas = Cinemas()
        self.voorstellingen = Voorstellingen()
        self.initialiseer_gebruikers()
        self.initialiseer_films()
        self.initialiseer_cinemas()
        self.initialiseer_voorstellingen()
    
    def initialiseer_gebruikers(self):
        for naam in [["Kristof", "Michiels"], ["Bart", "Lammens"], ["Stijn", "Vrevels"], ["Dieter", "Argens"], ["Mohammed", "Ridouani"]]:
            self.gebruikers.toevoegen(naam[0], naam[1])

    def initialiseer_films(self):
        for film in [["Top Gun: Maverick", 2022], ["Turning Red", 2022], ["The Northman", 2022], ["The Batman", 2022], ["The Lost City", 2022]]:
            self.films.toevoegen(film[0], film[1])

    def initialiseer_cinemas(self):
        for cinema in [["Kinepolis", "Oostende"], ["Cinema Lumière", "Brugge"], ["UGC Bioscopen", "Antwerpen"], ["Sphinx Cinema", "Gent"], ["Cartoons Cinema", "Antwerpen"]]:
            self.cinemas.toevoegen(cinema[0], cinema[1])
    
    def initialiseer_voorstellingen(self):
        for voorstelling in [[1, "Top Gun: Maverick", 2, "Cinema Lumière"]]:
            self.voorstellingen.toevoegen(voorstelling[0], voorstelling[1], voorstelling[2], voorstelling[3])
    
    def terminal_interface_weergeven(self):
        keuze_string = "Maak een keuze:\n1: Toon gebruikers\n2: Toon Films en ratings\n3: Toon cinema's\n4: Toon voorstellingen\n5: Ticket kopen voor een bestaande voorstelling\n6: Een film raten\n7: Een voorstelling toevoegen\n0: Data opslaan en toepassing verlaten\nJouw keuze: "
        getal = int(input(keuze_string))
        while getal != 0:
            if getal == 1: #toon gebruikers
                print(self.gebruikers)
            elif getal == 2: #toon films en ratings
                print(self.films)
            elif getal == 3: #toon cinema's
                print(self.cinemas)
            elif getal == 4: #toon voorstellingen
                print(self.voorstellingen)
            elif getal == 5: #ticket kopen
                voorstelling_id = int(input("Geef het id van de voorstelling: "))
                gebruiker_id = int(input("Geef het id van de gebruiker: "))
                boodschap = self.voorstellingen.koop_ticket(gebruiker_id, voorstelling_id)
                print(f"\n{boodschap}\n")
            elif getal == 6: #film raten
                film_id = int(input("Geef het id van de film: "))
                gebruiker_id = int(input("Geef het id van de gebruiker: "))
                rating = int(input("Geef de rating (1- heel slecht t.e.m. 5- supergoed): "))
                boodschap = "Deze gebruiker kan niet raten, want geen voorstelling bijgewoond"
                for voorstelling in self.voorstellingen.lijst:
                    for gebruiker in voorstelling.gebruikers:
                        if gebruiker == gebruiker_id:
                            boodschap = self.films.geef_rating(film_id, gebruiker_id, rating)
                            break 
                print(f"\n{boodschap}\n")
            elif getal == 7: #voorstelling toevoegen
                film_id = int(input("Geef het id van de film: "))
                cinema_id = int(input("Geef het id van de cinema: "))
                film_titel = self.films.krijg_titel(film_id)
                cinema_naam = self.cinemas.krijg_naam(cinema_id)
                boodschap = self.voorstellingen.toevoegen(film_id, film_titel, cinema_id, cinema_naam) 
                print(f"\n{boodschap}\n")      
            getal = int(input(keuze_string))