##
# Oefening 2
# Op Unix gebaseerde besturingssystemen bevatten doorgaans ook een tool met de 
# naam tail. Het toont de laatste 10 regels van een bestand waarvan de naam is 
# opgegeven als een command-line argument. Schrijf een Python-programma met 
# hetzelfde gedrag. Geef een passend foutbericht weer als het door de gebruiker 
# gevraagde bestand niet bestaat of als het command-line argument wordt 
# weggelaten. Er zijn verschillende benaderingen die kunnen worden gevolgd om dit 
# probleem op te lossen.
# Een optie is om de volledige inhoud van het bestand in een lijst te laden en 
# vervolgens de laatste 10 elementen weer te geven. Een andere optie is om de 
# inhoud van het bestand twee keer te lezen, een keer om de regels te tellen en 
# een tweede keer om de laatste 10 regels weer te geven. Beide oplossingen zijn 
# echter ongewenst bij het werken met grote bestanden. Er bestaat een andere 
# oplossing waarbij u het bestand slechts één keer hoeft te lezen en slechts 10 
# regels uit het bestand tegelijk hoeft op te slaan. Voor een extra uitdaging, 
# ontwikkel een dergelijke oplossing.

import sys

AANTAL_REGELS = 10

if len(sys.argv) != 2:
    print("Geef de naam van het bestand mee als command-line argument.")
    quit() # programma stopt meteen na gebruik van de quit-functie

try:
    regels_list = []
    with open(sys.argv[1], "r") as mijn_bestand:
        for regel in mijn_bestand:
            regels_list.append(regel.rstrip())
            
            if len(regels_list) > AANTAL_REGELS:
                regels_list.pop(0)

except IOError: # fout bij het openen/lezen van het bestand
    print("Er is iets fout gelopen bij het openen/lezen van het bestand.")

for regel in regels_list:
    print(regel)