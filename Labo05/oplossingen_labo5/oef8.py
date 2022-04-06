##
# Oefening 8
# Python gebruikt een hashtag om het begin van een commentaarregel aan te geven. 
# Deze regel bestaat vervolgens volledig uit commentaar. In deze oefening maak je 
# een programma dat alle opmerkingen uit een Python-bestand verwijdert. Controleer 
# elke regel in het bestand om te bepalen of een #-teken aanwezig is. Als dit het 
# geval is verwijdert het programma alle tekens van het #-teken tot het einde van 
# de regel (we negeren de situatie waarin het commentaarteken ergens in het midden 
# van een regel voorkomt). Sla het gewijzigde bestand op met een nieuwe naam. 
# Zowel de naam van het invoerbestand als de naam van het uitvoerbestand moeten 
# aan de gebruiker worden gevraagd. Zorg ervoor dat er een passend foutbericht 
# wordt weergegeven als zich een probleem voordoet bij het openen van één van de 
# bestanden.

try:
    input_bestandsnaam = input("Geef de naam van het in te lezen bestand: ")
    input_bestand = open(input_bestandsnaam, "r")
except:
    print("Er was een probleem met het openen van het invoerbestand.") 
    quit()

try:
    output_bestandsnaam = input("Geef de naam van het bestand waarnaar moet geschreven worden: ")
    output_bestand = open(output_bestandsnaam, "w")
except:
    input_bestand.close()
    print("Er was een probleem met het openen van het outputbestand.") 
    quit()

try:
    for regel in input_bestand:
        positie = regel.find("#")
        if positie > -1:
            regel = regel[0 : positie]
            regel = regel + "\n"
        output_bestand.write(regel)
    input_bestand.close()
    output_bestand.close()
except:
    print("Er heeft zich een probleem voorgedaan bij het wegschrijven naar het uitvoerbestand")