##
# Oefening 14
# Gebruik de dataset uit oefeningen 11, 12 en 13. Schrijf een programma dat elk 
# bestand in de dataset uitleest. Terwijl je programma de bestanden uitleest houdt 
# het elke verschillende naam die voorkomt bij (doe dit voor jongens en voor 
# meisjes afzonderlijk). Na afloop rapporteert je programma beide naamlijsten. 
# Deze lijsten bevatten geen dubbele namen.

START_JAAR = 1900 
EIND_JAAR = 2012

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

def main():
    meisjes_dict = {}
    jongens_dict = {}
    for jaar in range(START_JAAR, EIND_JAAR + 1):
        meisjes_bestand = "baby_namen/" + str(jaar) + "_GirlsNames.txt"
        jongens_bestand = "baby_namen/" + str(jaar) + "_BoysNames.txt"
        laden_toevoegen(meisjes_bestand, meisjes_dict)
        laden_toevoegen(jongens_bestand, jongens_dict)
    print("Alle verschillende meisjesnamen die tussen 1900 en 2012 zijn gegeven:")
    for naam in meisjes_dict:
        print(naam)
    print()
    print("Alle verschillende jongensnamen die tussen 1900 en 2012 zijn gegeven:")
    for naam in jongens_dict:
        print(naam)
    
main()