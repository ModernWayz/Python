##
# Oefening 7
# Maak een programma dat alle door de gebruiker ingevoerde getallen bij elkaar 
# optelt. Het negeert daarbij alle invoer die niet uit een geldig getal bestaat 
# (bvb een woord). Je programma geeft de som weer nadat elk nummer is ingevoerd. 
# Het geeft een passend bericht weer telkens de gebruiker iets anders dan een 
# getal heeft ingevoerd. Verlaat het programma wanneer de gebruiker een lege regel 
# invoert. Zorg ervoor dat je programma correct werkt voor zowel integers als 
# floats.


antwoord = input("Geef een getal: ")
totaal = 0
while antwoord != "":
    try:
        getal = float(antwoord)
        totaal += getal
        print(f"Het tussentotaal bedraagt {totaal}")
    except ValueError:
        print("Dat was geen getal. Probeer opnieuw...")
    antwoord = input("Geef een getal: ")
print(f"Het eindtotaal bedraagt {totaal}")