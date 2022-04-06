## Oefening 6: # Som van de eerste *n* positieve gehele getallen
# Schrijf een programma dat een positief geheel getal als input vraagt 
# en dan als resultaat de som weergeeft van alle gehele getallen van 1 
# tot *n*. Je kan dit berekenen met de volgende formule:
# som = (n)*(n+1)/2

getal = int(input("Geef een positief geheel getal: "))
som_van_de_getallen = (getal * (getal+1))/2 
print(f"De som van alle positieve gehele getallen tot {getal} is {int(som_van_de_getallen)}")
