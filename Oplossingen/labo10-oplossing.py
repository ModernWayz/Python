import time
import pickle

class Gebruiker():
    """ Klasse gebruiker: bestaat uit een id, voornaam en naam """
    def __init__(self, id, voornaam, naam):
        self.id = id
        self.voornaam = voornaam
        self.naam = naam


class Gebruikers():
    """ Klasse gebruikers: bevat gebruiker-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, voornaam, naam):
        nieuwe_gebruiker = Gebruiker(self.index, voornaam, naam)
        self.lijst.append(nieuwe_gebruiker) # toevoegen
        self.index += 1	# ga naar volgende ID
    
    def __str__(self):
        rs = "\nJe vroeg een lijst van de gebruikers:\n"
        for gebruiker in self.lijst:
            rs += f"{str(gebruiker.id)}: {gebruiker.voornaam} {gebruiker.naam}\n"
        return rs
         

class Film():
    """ Klasse film: bestaat uit een id, titel, jaar en ratings """
    def __init__(self, id, titel, jaar):
        self.id = id
        self.titel = titel
        self.jaar = jaar
        self.ratings = []


class Films():
    """ Klasse films: bevat film-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, titel, jaar):
        nieuwe_film = Film(self.index, titel, jaar)
        self.lijst.append(nieuwe_film) # toevoegen
        self.index += 1	# ga naar volgende ID

    def geef_rating(self, film_id, gebruiker_id, score):
        for film in self.lijst:
            if film.id == film_id:
                nieuwe_rating = Rating(gebruiker_id, score)
                for rating in film.ratings:
                    if rating.gebruiker_id == gebruiker_id:
                        return "Deze gebruiker heeft reeds een rating toegevoegd"
                film.ratings.append(nieuwe_rating)
                return "De rating werd toegevoegd"

    def krijg_titel(self, film_id):
        for film in self.lijst:
            if film.id == film_id:
                return film.titel

    def __str__(self):
        rs = "\nJe vroeg een lijst van de films:\n"
        for film in self.lijst:
            rating_info = ""
            for rating in film.ratings:
                rating_info += f"[Gebruiker: {rating.gebruiker_id} - Rating: {rating.score}]"
            rs += f"{str(film.id)}: {film.titel} {film.jaar}. Ratings: {rating_info}\n"
        return rs


class Cinema():
    """ Klasse cinema: bestaat uit een id, naam en stad """
    def __init__(self, id, naam, stad):
        self.id = id
        self.naam = naam
        self.stad = stad


class Cinemas():
    """ Klasse cinemas: bevat cinema-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, naam, stad):
        nieuwe_cinema = Cinema(self.index, naam, stad)
        self.lijst.append(nieuwe_cinema) # toevoegen
        self.index += 1	# ga naar volgende ID

    def krijg_naam(self, cinema_id):
        for cinema in self.lijst:
            if cinema.id == cinema_id:
                return cinema.naam
    
    def __str__(self):
        rs = "\nJe vroeg een lijst van de cinema's:\n"
        for cinema in self.lijst:
            rs += f"{str(cinema.id)}: {cinema.naam} {cinema.stad}\n"
        return rs


class Voorstelling():
    """ Klasse voorstelling: bestaat uit een id, film, cinema, tijdstip en gebruikers """
    def __init__(self, id, film_id, film_titel, cinema_id, cinema_naam, tijdstip):
        self.id = id
        self.film_id = film_id
        self.film_titel = film_titel
        self.cinema_id = cinema_id
        self.cinema_naam = cinema_naam
        self.tijdstip = tijdstip
        self.gebruikers = [] # gebruikers die ticket hebben gekocht komen hier in

class Voorstellingen():
    """ Klasse voorstellingen: bevat voorstelling-objecten en verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, film_id, film_titel, cinema_id, cinema_naam):
        nieuwe_voorstelling = Voorstelling(self.index, film_id, film_titel, cinema_id, cinema_naam, time.time())
        self.lijst.append(nieuwe_voorstelling) # toevoegen
        self.index += 1	# ga naar volgende ID

    def koop_ticket(self, gebruiker_id, voorstelling_id):
        try:
            if gebruiker_id in self.lijst[voorstelling_id-1].gebruikers:
                return "Deze gebruiker heeft al een ticket voor deze voorstelling"
            else:
                self.lijst[voorstelling_id-1].gebruikers.append(gebruiker_id)
                return "Ticket voor de voorstelling gekocht voor deze gebruiker"
        except IndexError:
            return "Voorstelling bestaat niet"

    def __str__(self):
        rs = "\nJe vroeg een lijst van de voorstellingen:\n"
        for voorstelling in self.lijst:
            rs += f"{str(voorstelling.id)}: {voorstelling.film_titel} in {voorstelling.cinema_naam}. Gebruikers: {str(voorstelling.gebruikers)}\n"
        return rs


class Rating():
    """ Klasse rating: bevat gebruiker_id, score en tijdstip """
    def __init__(self, gebruiker_id, rating):
        self.gebruiker_id = gebruiker_id
        self.score = rating
        self.tijdstip = time.time()


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


def main():
    try:
        with open("labo10-pickle.dat", "rb") as f:
            verder_string = input("\nDruk 'v' om verder te gaan op de vorige situatie of 'o' om opnieuw te beginnen:")
            if verder_string == "v":
                app = pickle.load(f) 
            else:
                app = Filmzalen()
    except FileNotFoundError:
        app = Filmzalen()
    app.terminal_interface_weergeven()
    with open("labo10-pickle.dat", "wb") as f:
        pickle.dump(app, f)

main()




