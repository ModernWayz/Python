##
# Oefening 15
# Bij het schrijven van een functie is een goede manier van werken om een 
# docstring te voorzien die de werking van de functie beschrijft. Soms vergeet de 
# ontwikkelaar evenwel om de docstring toe te voegen. Maak een programma dat één 
# of meerdere .py bestanden inleest en functies detecteert die niet voorzien zijn 
# van een docstring. Je programma toont alle functies, vergezeld van de 
# bestandsnaam waar de functie zich bevindt. De gebruiker zal de naam of namen van 
# één of meerdere bestanden die moeten nagekeken worden meegeven als command-line 
# argument(en). Je voorziet een gepaste foutmelding wanneer bestanden niet bestaan 
# of kunnen worden geopend. Je programma loopt wel verder en analyseert de 
# bestanden die wel bestaan.

import sys

if len(sys.argv) == 1:
    print("Je moet minstens één na te kijken bestand meegeven als command-line argument")
    quit()

for bestands_naam in sys.argv[1 : len(sys.argv)]: 
    # [1 : len(sys.argv)] om sys.argv[0] niet mee te nemen
    try:
        with open(bestands_naam, "r") as bestand:
            vorige_regel = " "
            regel_nummer = 0
            for regel in bestand: 
                if vorige_regel.startswith("def") and regel.lstrip()[0:3] != "'''":
                    pos_haakje = vorige_regel.index("(")
                    naam = vorige_regel[4 : pos_haakje]
                    print(f"Bestand {bestands_naam} op regel {regel_nummer}: {naam} heeft geen docstring.")
                vorige_regel = regel
                regel_nummer = regel_nummer + 1
    except:
        print(f"Er was een probleem met bestand {bestands_naam}. Ik probeer het volgende bestand...")