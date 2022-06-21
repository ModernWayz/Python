## Oefening 3
# Een bedrijf biedt verzending voor zijn artikelen tegen een tarief van 
# 8,5 euro voor het eerste artikel in een bestelling en 3 euro voor elk 
# volgend artikel in dezelfde bestelling. Schrijf een functie die het 
# aantal artikelen in de bestelling als enige parameter heeft. Geef als 
# resultaat de verzendkosten terug voor de bestelling. Voeg binnen een 
# main-functie een programma toe dat het aantal artikelen leest dat door 
# de gebruiker is gekocht en toon de verzendkosten.

def bereken_verzendkosten(aantal_artikelen):
    ''' Bereken de verzendkosten voor het meegegeven aantal artikelen '''
    if aantal_artikelen > 1:
        return 8.5 + ((aantal_artikelen-1)*3)
    else:
        return 8.5


def main():
    ''' Main applicatie functie '''
    aantal_artikelen = int(input("Geef het aantal artikelen: "))
    verzendkosten = bereken_verzendkosten(aantal_artikelen)
    print(f"De totale verzendkosten voor het versturen van {aantal_artikelen} bedraagt {verzendkosten}")


if __name__ == "__main__":
    main()


