## Oefening 4
# Schrijf een functie waaraan drie getallen als parameters meegegeven 
# worden die als resultaat de mediaan (het midden) van die parameters 
# teruggeeft. Voeg een programma toe dat drie waarden leest van de 
# gebruiker en hun mediaan weergeeft. Hoe bereken je de mediaan of 
# midden?  Met midden wordt het middelste element in de verdeling of de 
# geordende verzameling bedoeld: bvb de mediaan van 4, 3 en 8 is 4.

def bereken_mediaan(a, b, c):
    ''' Deze functie geeft de mediaan terug en neemt 3 getallen als parameter '''
    if a < b and b < c or a > b and b > c:
        returnwaarde = b
    if b < a and a < c or b > a and a > c:
        returnwaarde = a
    if c < a and b < c or c > a and b > c:
        returnwaarde = c
    return returnwaarde
    
def bereken_mediaan_alternatief(a, b, c):
    ''' Deze functie geeft de mediaan terug en neemt 3 getallen als parameter '''
    return a + b + c - min(a, b, c) - max(a, b, c)

def main():
    ''' Main applicatie-functie '''
    x = float(input("Geef het eerste getal: "))
    y = float(input("Geef het tweede getal: "))
    z = float(input("Geef het derde getal: "))
    print("De mediaanwaarde is:", bereken_mediaan(x, y, z))
    print("De mediaan, anders berekend:", bereken_mediaan_alternatief(x, y, z))

if __name__ == "__main__":
    main()

