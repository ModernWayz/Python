## Oefening 8: volume van een cilinder
# Het volume van een cilinder kan berekend worden door de oppervlak van 
# de cirkelvormige basis te vermenigvuldigen met zijn hoogte. Maak een 
# programma die de straal en de hoogte van de cilinder opvraagt aan de 
# gebruiker en vervolgens het volume berekent. Toon het resultaat 
# afgerond tot op 1 cijfer na de komma.

# volume cilinder = π x straal² x hoogte

import math
PI = math.pi
straal = float(input("Geef de straal van de cilinder (in cm): "))
hoogte = float(input("Geef de hoogte van de cilinder (in cm): "))
volume_cilinder = PI * (straal ** 2) * hoogte
print(f"Het volume van de cilinder bedraagt {round(volume_cilinder,2)}cm3.")