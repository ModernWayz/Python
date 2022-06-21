from rating import Rating

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