import random

class Gebruiker():
    AANTAL_FIETSEN = 1
    """ Klasse Gebruiker: bestaat uit id, voornaam, naam en logs """
    def __init__(self, id, voornaam, naam):
        self.id = id
        self.voornaam = voornaam
        self.naam = naam
        self.inhoud = []

class Transporteur(Gebruiker):
    AANTAL_FIETSEN = 10


class Gebruikers():
    """ Klasse Gebruikers: bevat gebruikers-objecten in lijst alsook verwante bewerkingsmethods """
    def __init__(self):
        self.lijst = []
        self.index = 1 # start ID

    def toevoegen(self, voornaam, naam):
        nieuwe_gebruiker = Gebruiker(self.index, voornaam, naam)
        self.lijst.append(nieuwe_gebruiker) # toevoegen
        self.index += 1	# ga naar volgende ID
    
    def geef_info(self, id):
        return_data = "\n"
        for gebruiker in self.lijst:
            if gebruiker.id == id:
                fiets = "geen" if (len(gebruiker.inhoud) == 0) else gebruiker.inhoud[0].id
                return_data += f"{gebruiker.id}: {gebruiker.voornaam} {gebruiker.naam} (fiets: {fiets})\n"
        return return_data
    
    def geef_info_alle(self):
        return_data = "\n"
        for gebruiker in self.lijst:
                fiets = "geen" if (len(gebruiker.inhoud) == 0) else gebruiker.inhoud[0].id
                return_data += f"{gebruiker.id}: {gebruiker.voornaam} {gebruiker.naam} (fiets: {fiets})\n"
        return return_data
    
    def is_gebruiker_en_fiets_ontleenbaar(self, id):
        gebruiker = [g for g in self.lijst if (g.id == id and len(g.inhoud) < Gebruiker.AANTAL_FIETSEN )]
        return True if len(gebruiker) > 0 else False
    
    def plaats_fiets_op_kaart(self, id, fiets):
        gebruiker = [g for g in self.lijst if (g.id == id)]
        gebruiker[0].inhoud.append(fiets)

    def is_gebruiker_en_fiets_teruggeefbaar(self, id):
        gebruiker = [g for g in self.lijst if (g.id == id and len(g.inhoud) > 0)]
        return True if len(gebruiker) > 0 else False

    def fiets_van_kaart_nemen(self, id):
        gebruiker = [g for g in self.lijst if (g.id == id)]
        return gebruiker[0].inhoud.pop(0)

    def geef_willekeurige_gebruiker_zonder_fiets(self):
        lijst_van_beschikbare_gebruikers = []
        for gebruiker in self.lijst:
            lege_inhoud = 0
            if len(gebruiker.inhoud) == 0:
                lijst_van_beschikbare_gebruikers.append(gebruiker)
        return random.choice(lijst_van_beschikbare_gebruikers).id


def voornamen_lijst():
    return ["Arthur", "Noah" ,"Lucas", "Liam", "Leon", "Jules", "Finn", "Louis", "Victor", "Lewis", "Adam","Lars", "Vic", "Vince", "Matteo", "Mathis", "Mohamed", "Emiel", "Jack", "Elias", "Alexander", "Gust", "Oscar", "Stan", "Maurice", "Lou", "Lowie", "Marcel", "Milan", "Mats", "Felix", "Wout", "Kobe", "Nathan", "Tuur", "Warre", "Viktor", "Seppe", "Lukas", "Rayan", "Léon", "Cas", "Eden","Ferre", "David", "Daan", "Amir", "Otis", "Thomas", "Miel", "Luca", "Bas", "Mauro", "Oliver", "Emile", "Georges", "Jayden", "Sem", "Cyriel", "Lenn", "Maxim", "Mil", "Henri", "Siebe", "Jef","Mohammed", "Lex", "Sam", "Juul", "Senne", "Loïc", "Alex", "Remi", "Levi", "Max", "Kamiel", "Ali", "Milo", "Youssef", "Gabriel", "Hamza", "Nand", "Simon", "Vik", "Imran", "Gaston", "Leander", "Aaron", "Andreas", "Lio", "Nolan", "Ilyas", "Jasper", "Oskar", "Omar", "Maxime", "Ayden", "Dries", "Ibrahim", "Kasper", "Owen", "Julian", "Mathias", "Samuel", "Fons", "Lander", "Theo", "Thor", "Yusuf", "James", "Morris", "Rik", "Tibo", "Jesse", "Aiden", "Daniel","Mila", "Olivia", "Marie", "Emma", "Ella", "Louise", "Amélie", "Noor", "Elena", "Juliette", "Anna", "Nora", "Elise", "Liv", "Lena", "Alice", "Julie", "Renée", "Lina", "Lotte", "Camille", "Charlotte", "Nina", "Lily", "Ellie", "Mona", "Sofia", "Amelie", "Manon", "Sara", "Amber", "Fien", "Mia", "Billie", "Helena", "Oona", "Lucie", "Luna", "Janne", "Lou", "Axelle", "Esméé", "Ellis", "Nore", "Fleur", "Emilia", "Rosalie", "Laura", "Amira", "Chloé", "Julia", "Lara", "Kato", "Lore", "Zoë", "Eva", "Sophia", "Stella", "Inaya", "Roos", "Noa", "Lize", "Hannah", "Lisa", "Fran", "Féline", "Victoria", "Hanne", "Sam", "Estelle", "Maria", "Jade", "Leonie", "Tess", "Céleste", "Anaïs", "Odette", "Lea", "Emily", "Hailey", "Romy", "Sarah", "Amelia", "Lio", "Amina", "Flo", "Aline", "Marie-Lou", "Rosie", "Alix", "Marilou", "Yara", "June", "Lia", "Linde", "Flore", "Febe", "Hanna", "Elif", "Lauren", "Alicia"]


def familienamen_lijst():
    return ["Peeters", "Janssens", "Maes", "Jacobs", "Mertens", "Willems", "Claes", "Wouters", "Goossens", "Dubois", "Vermeulen", "Pauwels", "Hermans", "Lambert", "Aerts", "Michiels", "Dupont", "Martens", "Smets", "Martin", "Desmet", "Hendrickx", "Claeys", "Devos", "Janssen", "Stevens", "Dumont", "Segers", "Lemmens", "Leroy", "Coppens", "Simon", "Wauters", "Laurent", "Leclercq", "Renard", "Denis", "Verhoeven", "Lejeune", "Cools", "Declercq", "Thomas", "Petit", "Charlier", "Lemaire", "Smet", "Timmermans", "Michel", "Vandenberghe", "Thys", "Bertrand", "Lenaerts", "Cornelis", "Depauw", "Bauwens", "Verheyen", "Lefebvre", "Mathieu", "Carlier", "Evrard", "Baert", "Verstraete", "Moens", "Lauwers", "Bernard", "Lambrechts", "Bosmans", "Bogaert", "Geerts", "Fontaine", "Bogaerts", "Verlinden", "Gerard", "Christiaens", "Deprez", "Verbeke", "Vermeiren", "Marchal", "Verschueren", "Beckers", "Legrand", "Jansen", "Wuyts", "Adam", "Simons", "Verstraeten", "Collard", "Moreau", "Verhaeghe", "Claessens", "Mahieu", "Vermeersch", "Vandamme", "Thijs", "Henry", "Robert", "Pieters", "Heylen", "De groote", "Verhaegen", "Ceulemans", "Goethals", "Lievens", "François", "Vandevelde", "Callens", "Noel", "Servais", "Bastin", "Leemans", "Verbruggen", "Verhelst", "Roels", "Vercammen", "Gielen", "Somers", "Luyten", "Daems", "Matthys", "Vandewalle", "Mortier", "Vercauteren", "Verdonck", "Herman", "Swinnen", "Smeets", "Andries", "Vervoort", "Nys", "Meert", "Vos", "Claus", "Dewulf", "Verheyden", "Coenen", "Lecomte", "Smits", "Deckers"]