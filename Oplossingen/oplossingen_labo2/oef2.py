##
# Oefening 2
# Een mensenjaar, zo wordt gezegd, komt overeen met 7 hondenjaren. 
# Honden bereiken evenwel de volwassenheid in gemiddeld 2 jaar. Soms 
# wordt gedacht dat het beter is de eerste 2 jaar als 10,5 hondenjaar te
# beschouwen en elk volgend jaar als 4 hondenjaren. Schrijf een
# programma dat deze berekening maakt voor een hond, van mensenjaren
# naar hondenjaren. Zorg dat het werkt voor honden die jonger zijn dan
# drie en geef een bericht terug als de gebruiker een negatief getal
# invoert.

leeftijd_mensenjaren = int(input("Wat is de leeftijd van de hond in mensenjaren? "))

if leeftijd_mensenjaren < 0:
    print("De leeftijd kan niet negatief zijn")
else:
    if leeftijd_mensenjaren < 3:
        leeftijd_hondenjaren = leeftijd_mensenjaren * 10.5
    else:
        leeftijd_hondenjaren = 21 + (leeftijd_mensenjaren-2) * 4
    print(f"Een hond met leeftijd {leeftijd_mensenjaren} in mensenjaren is {leeftijd_hondenjaren} jaar oud in hondenjaren")