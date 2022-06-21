# Werken met Pickle - eenvoudig vasthouden van objecten en object-structuren uit eigen klassen
# Vrijblijvende tekst: https://realpython.com/python-pickle-module/

import pickle

mijn_pickle_bestand = "mijn_pickle.dat"


class Kunstenaar():
    def __init__(self, voornaam, achternaam):
        self.id = None
        self.voornaam = voornaam
        self.achternaam = achternaam


class Kunstenaars():
	def __init__(self):
		self.kunstenaar_dict = {} # kunstenaars_dictionary
		self.index = 1 # start ID

	def voeg_kunstenaar_toe(self, kunstenaar):
		kunstenaar.id = self.index # ID zetten
		self.index += 1	# ga naar volgende ID
		self.kunstenaar_dict.update({kunstenaar.id: kunstenaar}) # toevoegen


class App():
	def __init__(self):
		self.kunstenaar_data = Kunstenaars()
		self.kunstenaar_data.voeg_kunstenaar_toe(Kunstenaar("Pablo", "Picasso"))
		self.kunstenaar_data.voeg_kunstenaar_toe(Kunstenaar("Agnes", "Martin"))
		self.kunstenaar_data.voeg_kunstenaar_toe(Kunstenaar("Francis", "Picabia"))
	
	def toon_kunstenaars(self):
		dict = self.kunstenaar_data.kunstenaar_dict
		for key in dict:
			kunstenaar = dict[key]
			print(kunstenaar.id, " : ", kunstenaar.voornaam, kunstenaar.achternaam)


mijn_app = App()
mijn_app.toon_kunstenaars()

# naar een string dumpen
mijn_gepekelde_object = pickle.dumps(mijn_app)

# of naar een bestand dumpen
with open(mijn_pickle_bestand, "wb") as f:
    pickle.dump(mijn_app, f)

mijn_app.kunstenaar_data.kunstenaar_dict[3].achternaam = "Bacon"

print(mijn_app.kunstenaar_data.kunstenaar_dict[3].achternaam)

# van een string lezen
mijn_app = pickle.loads(mijn_gepekelde_object)

# of van een bestand lezen
with open(mijn_pickle_bestand, "rb") as f:
    mijn_app = pickle.load(f) 

print(mijn_app.kunstenaar_data.kunstenaar_dict[3].achternaam)
