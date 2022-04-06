##
# Oefening 4
# Maak een programma dat gehele getallen inleest van de gebruiker, tot een 
# lege lijn wordt ingegeven. Het programma toont vervolgens eerst de 
# negatieve getallen, gevolgd door alle nullen, en tot slot gevolgd door de 
# positieve getallen. Binnen elke groepen worden de getallen getoond in de 
# volgorde in dewelke ze werden ingegeven door de gebruiker. Een voorbeeld: 
# als de gebruiker de waarden 5, -2, 2 0, -1, 0, 3 en -2 ingeeft moet je 
# programma tot volgende output komen: -2, -1, -2, 0, 0, 5, 2 en 3. Je 
# programma print elke waarde uit op een eigen regel.

negatieve_getallen = []
nullen = []
positieve_getallen = []
antwoord = input("Geef een geheel getal (leeg antwoord om af te sluiten): ")
while antwoord != "":
    getal = int(antwoord)
    if getal < 0:
        negatieve_getallen.append(getal)
    elif getal > 0:
        positieve_getallen.append(getal)
    else:
        nullen.append(getal)
    antwoord = input("Geef een geheel getal (leeg antwoord om af te sluiten): ")

print("De ingevoerde getallen waren: ")
for n in negatieve_getallen:
    print(n)
for n in nullen:
    print(n)
for n in positieve_getallen:
    print(n)