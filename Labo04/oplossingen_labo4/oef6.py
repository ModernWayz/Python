##
# Oefening 6
# Om de hoofdprijs in een bepaalde loterij te winnen, moet men alle 6 
# nummers op een loterijbriefje matchen met de 6 nummers tussen 1 en 49 die 
# zijn getrokken door de organisator van de loterij. Schrijf een programma 
# dat een willekeurige selectie van 6 nummers genereert voor een 
# loterijbriefje. Zorg ervoor dat de 6 geselecteerde nummers geen dubbele 
# nummers bevatten. Geef de nummers in oplopende volgorde weer.

from random import randrange

MIN_GETAL = 1
MAX_GETAL = 49
AANTAL_GETALLEN = 6

loterij_ticket = []
for i in range(AANTAL_GETALLEN):
    willekeurig_getal = randrange(MIN_GETAL, MAX_GETAL + 1)
    while willekeurig_getal in loterij_ticket:
        willekeurig_getal = randrange(MIN_GETAL, MAX_GETAL + 1)
    loterij_ticket.append(willekeurig_getal)

loterij_ticket.sort()
print("De getallen op jouw ticket zijn: ")
for getal in loterij_ticket:
  print(getal)
