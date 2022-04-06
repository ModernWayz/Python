##
# Oefening 1
# Op Unix gebaseerde besturingssystemen bevatten een tool met de naam head. 
# Het toont de eerste 10 regels van een bestand waarvan de naam is opgegeven 
# als een command-line argument. Schrijf een Python-programma met hetzelfde 
# gedrag. Geef een passend foutbericht weer als het door de gebruiker 
# gevraagde bestand niet bestaat, of als het command-line
# argument wordt weggelaten.

import sys

AANTAL_REGELS = 10

if len(sys.argv) != 2:
    print("Geef de naam van het bestand mee als command-line argument.")
    quit() # programma stopt meteen na gebruik van de quit-functie

try:
    with open(sys.argv[1], "r") as mijn_bestand:
        regel = mijn_bestand.readline()
        teller = 0
        while teller < AANTAL_REGELS and regel != "":    
            regel = regel.rstrip()
            teller = teller + 1
            print(regel)
            regel = mijn_bestand.readline()
except IOError: # fout bij het openen/lezen van het bestand
    print("Er is iets fout gelopen bij het openen/lezen van het bestand.")



