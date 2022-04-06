## Oefening 9: eenheden van tijd
# Maak een programma dat een lengte van tijd opvraagt van een gebruiker 
# als een reeks dagen, uren, minuten en seconden (afzonderlijk 
# opgevraagd). Bereken en toon het totale aantal seconden dat deze tijd 
# vertegenwoordigt.

aantal_dagen = int(input("Geef het aantal dagen: "))
aantal_uren = int(input("Geef het aantal uren: "))
aantal_minuten = int(input("Geef het aantal minuten: "))
aantal_seconden = int(input("Geef het aantal seconden: "))
totaal_aantal_seconden = aantal_seconden + (aantal_minuten*60) + (aantal_uren*3600) + (aantal_dagen*24*3600)
print(f"De door jou ingegeven tijd bedraagt {totaal_aantal_seconden}s")

