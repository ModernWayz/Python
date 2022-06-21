##
# Oefening 5
# De lengte van een maand varieert van 28 tot 31 dagen. Je schrijft een
# programma die de naam van een maand opvraagt als string. Je geeft een
# getal terug met het aantal dagen. Voor februari geeft je “28 of 29
# dagen” terug

maand = input("Geef de naam van een maand: ")
dagen = 31
if maand == "april" or maand == "juni" or \
    maand == "september" or maand == "november":
    dagen = 30
elif maand == "februari":
    dagen = "28 of 29"
print(f"{maand} telt {dagen} dagen.")