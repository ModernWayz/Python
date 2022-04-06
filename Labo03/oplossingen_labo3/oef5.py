##  
# Oefening 5
# Schrijf een functie waaraan een string en de beschikbare ruimte in 
# karakters als parameters kunnen worden meegegeven. De functie geeft een 
# string terug waarbij voor de oorspronkelijke string spaties zijn 
# toegevoegd zodat de string gezien de beschikbare ruimte in het midden zal 
# komen te staan. Als de lengte van de string groter is dan de beschikbare 
# ruimte dan dient gewoon de string te worden teruggegeven. Is de lengte van 
# de string kleiner dan de beschikbare ruimte dan worden voor de 
# oorspronkelijke string (len(string) - karakters) // 2 karakters witruimte 
# toegevoegd. Schrijf een programma dat de functie een aantal keer 
# demonstreert.

BREEDTE = 80

def centreer(tekst, breedte):
    ''' Functie die tekst centreert op basis van een beschikbare breedte. De functie geeft gecentreerde tekst terug '''
    if breedte < len(tekst):
        return tekst
    spaties = (breedte - len(tekst)) // 2
    resultaat = " " * spaties + tekst
    return resultaat

def main():
    ''' Main applicatie functie '''
    print(centreer("Python programmeren", BREEDTE))
    print(centreer("door:", BREEDTE))
    print(centreer("Kristof Michiels", BREEDTE))
    print()
    print("Python is prachtig!")

if __name__ == "__main__":
    main()

