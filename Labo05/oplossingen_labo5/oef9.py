##
# Oefening 9
# Schrijf een programma dat een bestand leest dat een lijst met woorden bevat, er 
# willekeurig twee selecteert en ze samenvoegt om een wachtwoord te produceren. 
# Zorg er bij het maken van het wachtwoord voor dat de totale lengte tussen 12 en 
# 15 tekens is en dat elk gebruikt woord ten minste drie letters lang is. Zet elk 
# woord in het wachtwoord met een hoofdletter, zodat de gebruiker gemakkelijk kan 
# zien waar het ene woord eindigt en het volgende begint. Tot slot geeft je 
# programma het wachtwoord weer.

from random import randrange

WOORDEN_BESTAND = "oef9.txt"
woorden_list = []

bestand = open(WOORDEN_BESTAND, "r")
for regel in bestand:
    regel = regel.rstrip()
    if len(regel) >= 3 and len(regel) <= 7:
        woorden_list.append(regel)
bestand.close()
eerste_woord = woorden_list[randrange(0, len(woorden_list))]
eerste_woord = eerste_woord.capitalize()
wachtwoord = eerste_woord
while len(wachtwoord) < 8 or len(wachtwoord) > 10:
    tweede_woord = woorden_list[randrange(0, len(woorden_list))]
    tweede_woord = tweede_woord.capitalize()
    wachtwoord = eerste_woord + tweede_woord

print("Het willekeurige wachtwoord is:", wachtwoord)
