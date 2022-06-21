##
# Oefening 11
# De som van alle natuurlijke getallen die kleiner zijn dan tien die 
# veelvouden zijn van 3 of van 5 is 23. Hiermee bedoel ik 3 + 5 + 6 + 9 
# die samengeteld 23 zijn. Laat de computer de som berekenen van alle 
# natuurlijke getallen die kleiner zijn dan 1000 en die veelvoud zijn 
# van 3 of 5. Druk het eindresultaat af.

som = 0
for getal in range(1000):
    if getal % 3 == 0 or getal % 5 == 0:
        som += getal
print(f"De som van het aantal veelvouden van 3 en 5 is {som}")
