##
# Oefening 11
# De babynamen-set bevat meer dan 200 bestanden. Elk bestand bevat een lijst met 
# 100 namen, alsook het aantal keer dat de naam voor komt voor elk jaar. De lijnen 
# in de bestanden zijn gerangschikt van meest naar minst vaak gebruikt. Er zijn 
# twee bestanden voor elk jaar: een met namen voor meisjes en de andere met namen 
# voor jongens. De dataset bevat gegevens voor elk jaar van 1900 tot 2012. Schrijf 
# een programma dat elk bestand in de dataset leest en alle namen identificeert 
# die het meest populair waren in ten minste één jaar. Je programma dient twee 
# lijsten weer te geven: een met de meest populaire namen voor jongens en de 
# andere met de meest populaire namen voor meisjes. Geen van de lijsten mag 
# tweemaal dezelfde waarde bevatten.

START_JAAR = 1900 
EIND_JAAR = 2012

def laden_toevoegen(bestandsnaam, naam_list): 
    with open(bestandsnaam, "r") as bestand:
        regel = bestand.readline()
    regel_list = regel.split()
    naam = regel_list[0]
    if naam not in naam_list:
        naam_list.append(naam)

def main():
    meisjes_list = []
    jongens_list = []
    for jaar in range(START_JAAR, EIND_JAAR + 1):
        meisjes_bestand = "baby_namen/" + str(jaar) + "_GirlsNames.txt"
        jongens_bestand = "baby_namen/" + str(jaar) + "_BoysNames.txt"
        laden_toevoegen(meisjes_bestand, meisjes_list)
        laden_toevoegen(jongens_bestand, jongens_list)
    print("De meisjesnamen die tussen 1900 en 2012 de nummer1-plek hebben bekleed:")
    for naam in meisjes_list:
        print(f" {naam}")
    print()
    print("De jongensnamen die tussen 1900 en 2012 de nummer1-plek hebben bekleed:")
    for naam in jongens_list:
        print(f" {naam}")
main()