##
# Oefening 13
# Gebruik de dataset uit oefeningen 11 en 12. Schrijf een programma waarin de 
# gebruiker twee jaartallen kan ingeven. Analyseer voor deze tijdspanne (bvb van 
# 2002 tot en met 2007) de data en geef de populairste jongens- en meisjesnaam 
# terug voor de volledige periode.

start_jaartal = int(input("Geef het startjaar van de periode waarop je wenst te zoeken: "))
eind_jaartal = int(input("Geef het eindjaar van de periode waarop je wenst te zoeken: "))

jongens_dict = {}
meisjes_dict = {}

def laden_toevoegen(bestandsnaam, naam_dict): 
    with open(bestandsnaam, "r") as bestand:
        for regel in bestand:
            regel_list = regel.split()
            naam = regel_list[0]
            aantal = int(regel_list[1])
            if naam in naam_dict:
                naam_dict[naam] += aantal
            else:
                naam_dict[naam] = aantal

for jaar in range(start_jaartal, eind_jaartal + 1):
    meisjes_bestand = "baby_namen/" + str(jaar) + "_GirlsNames.txt"
    jongens_bestand = "baby_namen/" + str(jaar) + "_BoysNames.txt"
    laden_toevoegen(meisjes_bestand, meisjes_dict)
    laden_toevoegen(jongens_bestand, jongens_dict)

populairste_jongensnaam = ""
populairste_jongensnaam_aantal = 0

for key, value in jongens_dict.items():
    if value > populairste_jongensnaam_aantal:
        populairste_jongensnaam = key
        populairste_jongensnaam_aantal = value

populairste_meisjesnaam = ""
populairste_meisjesnaam_aantal = 0

for key, value in meisjes_dict.items():
    if value > populairste_meisjesnaam_aantal:
        populairste_meisjesnaam = key
        populairste_meisjesnaam_aantal = value

print(f"Populairste jongensnaam voor de gekozen periode: {populairste_jongensnaam }. Deze naam kwam {populairste_jongensnaam_aantal} keer voor in de dataset voor deze periode.")
print(f"Populairste meisjesnaam voor de gekozen periode: {populairste_meisjesnaam }. Deze naam kwam {populairste_meisjesnaam_aantal} keer voor in de dataset voor deze periode.")
