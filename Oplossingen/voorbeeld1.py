# collecties van klassen: een voorbeeld

class Kunstenaar():
    def __init__(self, voornaam, achternaam):
        self.id = None
        self.voornaam = voornaam
        self.achternaam = achternaam

    def __str__(self):
        return f"{self.id}  : {self.voornaam} {self.achternaam}"

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
print(mijn_app.kunstenaar_data.kunstenaar_dict)
mijn_app.kunstenaar_data.kunstenaar_dict[3].achternaam = "Bacon"
mijn_app.toon_kunstenaars()
francis_bacon = mijn_app.kunstenaar_data.kunstenaar_dict[3]
print(francis_bacon)
