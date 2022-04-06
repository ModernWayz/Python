##
# Oefening 12
# Je maakt een computerprogramma dat het gemiddelde berekent van een 
# reeks waarden die door de gebruiker één voor één worden ingevoerd. Het 
# programma blijft naar nieuwe getallen vragen tot de gebruiker 0 
# ingeeft. Je toont een foutmelding als het eerste getal dat de 
# gebruiker ingeeft 0 zou zijn en het laatste getal 0 telt uiteraard 
# niet mee om het gemiddelde te berekenen.

getal = int(input("Geef een geheel getal aub (0 om het gemiddelde van de getallen te berekenen): "))
som = 0
aantal = 0
while getal != 0:
    aantal += 1
    som += getal
    getal = int(input("Geef een nieuwe geheel getal (0 om de app te verlaten): "))
print(f"het aantal ingevoerde getallen is {aantal}")
print(f"Het gemiddelde van de ingevulde getallen is {som / aantal}")