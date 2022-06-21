##
# Oefening 4
# Schrijf een programma die het aantal zijden van een veelhoek opvraagt.
# Geef dan de naam van de veelhoek terug (bvb een zeshoek). Je programma
# ondersteunt vormen van 3 tot en met 10 zijden. Als de gebruiker een
# waarde invoert die buiten deze range valt dan reageer je met een
# gepaste melding.

aantal_zijden = int(input("Geef het aantal zijden: "))
naam = ""
if aantal_zijden == 3:
    naam = "driehoek"
elif aantal_zijden == 4:
    naam = "vierhoek"
elif aantal_zijden == 5:
    naam = "vijfhoek"
elif aantal_zijden == 6:
    naam = "zeshoek"
elif aantal_zijden == 7:
    naam = "zevenhoek"
elif aantal_zijden == 8:
    naam = "achthoek"
elif aantal_zijden == 9:
    naam = "negenhoek"
elif aantal_zijden == 10:
    naam = "tienhoek"
if naam == "":
    print("Dit antwoord wordt niet ondersteund door het programma")
else:
    print("Je bedoelt een ", naam)