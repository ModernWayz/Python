## Oefening 1
# Schrijf een functie waaraan de lengtes van de twee rechthoekszijden 
# van een rechthoekige driehoek moeten meegegeven worden. Geef als 
# resultaat van de functie de lengte van de hypotenusa (dit is de 
# schuine zijde) van de driehoek terug, berekend met de stelling van 
# Pythagoras. Voeg binnen een main-functie een programma toe dat de 
# lengtes van de kortere zijden van een rechthoekige driehoek aan de 
# gebruiker vraagt, en de eerste functie gebruikt om de lengte van de 
# hypotenusa te berekenen, en het resultaat weergeeft.
import math

def lengte_hypotenusa(lengte_a, lengte_b):
    ''' Functie berekent de lengte van de hypotenusa van een
    rechthoekige driehoek. Ze neemt de lengtes van de rechthoekszijden
    als argument '''
    hypotenusa = math.sqrt(lengte_a ** 2 + lengte_b ** 2)
    return hypotenusa

def main():
    ''' Main applicatie-functie '''
    lengte_a = float(input("Geef de lengte van de eerste rechthoekszijde (in cm): "))
    lengte_b = float(input("Geef de lengte van de tweede rechthoekszijde (in cm): "))
    resultaat = round(lengte_hypotenusa(lengte_a, lengte_b),2)
    print(f"De lengte van de hypotenusa bedraagt: {resultaat}cm")

if __name__ == "__main__":
    main()
