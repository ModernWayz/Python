## Oefening 4: # oppervlakte van een kamer
# Schrijf een programma dat de gebruiker vraagt om een lengte en breedte 
# van een kamer in te geven (twee afzonderlijke variabelen). Eens deze 
# waarden ingelezen zijn berekent je programma de oppervlakte van de 
# kamer. De lengte en de breedte zullen ingegeven worden als 
# komma-getallen. Voeg eenheden toe in de output-boodschap (meter). 
# Gebruik de float()-functie om de ingegeven waarden om te zetten van 
# string naar float.

lengte = float(input("Geef de lengte van de kamer (in m): "))
breedte = float(input("Geef de breedte van de kamer (in m): "))
oppervlakte_kamer = lengte * breedte
print(f"De oppervlakte van de kamer met lengte = {round(lengte,2)}m en breedte = {round(breedte,2)}m bedraagt {round(oppervlakte_kamer,2)} m2.")