##
# Oefening 3
# Op Unix gebaseerde besturingssystemen bevatten doorgaans ook een tool genaamd 
# cat, een afkorting voor concatenate of samenvoegen. Het doel is om de 
# aaneenschakeling van een of meer bestanden weer te geven waarvan de namen worden 
# meegegeven als command-line argumenten. De bestanden worden weergegeven in 
# dezelfde volgorde als waarin ze zijn meegegeven. Maak een Python-programma dat 
# deze taak uitvoert. Je programma genereert ook een passende foutmelding voor elk 
# bestand dat niet kan worden weergegeven en gaat vervolgens verder naar het 
# volgende bestand. Geef een passend foutbericht weer als het programma wordt 
# gestart zonder het command-line argument(en).

import sys

if len(sys.argv) == 1:
    print("Je moet minstens één bestandsnaam meegeven als command-line argument.")
    quit() # programma stopt meteen na gebruik van de quit-functie

for teller in range(1, len(sys.argv)):
    bestandsnaam = sys.argv[teller]
    try:
        with open(bestandsnaam, "r") as bestand:
            for regel in bestand:
                print(regel.rstrip())
    except:
        print(f"Ik kon bestand {bestandsnaam} niet openen.")