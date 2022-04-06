## Oefening 2
# Ziehier de taxi-tarieven voor de stad Antwerpen: https://www.
# taxibedrijfantwerpen.be/prijs-taxi-antwerpen-kost-taxi-antwerpen/.
# Schrijf een functie die de afgelegde afstand (in kilometers) als
# parameter neemt, alsook ook andere nodige parameters (weekend,
# nacht, luchthaven) om de juiste prijs zoals je die op de site 
# geafficheerd ziet te kunnen berekenen. Als resultaat geeft de
# functie de kostprijs van de rit terug. Schrijf binnen een
# main-functie een programma dat de functie demonstreert. Gebruik
# constanten om de tariefonderdelen weer te geven

TARIEF_LUCHTHAVEN = 78
KMPRIJS_EXTRA_LUCHTHAVEN = 2
NACHTTOESLAG = 2.5
INSTAPGELD = 2.9
KMPRIJS_STANDARD_SCHIJF1 = 2.5
KMPRIJS_STANDARD_SCHIJF2 = 2.2
KMPRIJS_STANDARD_SCHIJF3 = 2
KMPRIJS_WEEKEND_SCHIJF1 = 2.5
KMPRIJS_WEEKEND_SCHIJF2 = 2.3
KMPRIJS_WEEKEND_SCHIJF3 = 2.1

def bereken_prijs_taxirit(aantal_km, is_weekend, is_nacht,is_naar_luchthaven):
    ''' Functie berekent de prijs van een taxirit. Neemt als argumenten: het aantal_km (integer), is_weekend (boolean), is_nacht (boolean) en is_naar_luchthaven (boolean) '''
    kostprijs = 0

    if is_naar_luchthaven == "True":
        if aantal_km > 50:
            kostprijs = TARIEF_LUCHTHAVEN + ((aantal_km - 50) *     KMPRIJS_EXTRA_LUCHTHAVEN)
        else:
            kostprijs = TARIEF_LUCHTHAVEN
        return kostprijs
    else:
        kostprijs += INSTAPGELD
        if is_nacht == "True":
            kostprijs += NACHTTOESLAG
        if is_weekend == "True":
            if aantal_km > 20:
                kostprijs += (KMPRIJS_WEEKEND_SCHIJF1 * 5) + (KMPRIJS_WEEKEND_SCHIJF2 * 15) + (KMPRIJS_WEEKEND_SCHIJF3 * (aantal_km-20))
            elif aantal_km > 6:
                kostprijs += (KMPRIJS_WEEKEND_SCHIJF1 * 5) + (KMPRIJS_WEEKEND_SCHIJF2 * (aantal_km-5))
            else:
                kostprijs += KMPRIJS_WEEKEND_SCHIJF1 * aantal_km
        else:
            if aantal_km > 20:
                kostprijs += (KMPRIJS_STANDARD_SCHIJF1 * 5) + (KMPRIJS_STANDARD_SCHIJF2 * 15) + (KMPRIJS_STANDARD_SCHIJF3 * (aantal_km-20))
            elif aantal_km > 6:
                kostprijs += (KMPRIJS_STANDARD_SCHIJF1 * 5) + (KMPRIJS_STANDARD_SCHIJF2 * (aantal_km-5))
            else:
                kostprijs += KMPRIJS_STANDARD_SCHIJF1 * aantal_km
        return kostprijs

def main():
    ''' Main applicatie functie '''
    aantal_km = float(input("Geef het aantal km van deze rit: "))
    weekend = bool(input("Is het weekend (True/False)? "))
    nacht = bool(input("Is het na 22u (True/False)? "))
    luchthaven = bool(input("Is het naar de luchthaven (True/False)? "))
    resultaat = bereken_prijs_taxirit(aantal_km, weekend, nacht, luchthaven)
    print(f"De kostprijs voor de rit bedraagt {resultaat}eur.")

if __name__ == "__main__":
    main()


