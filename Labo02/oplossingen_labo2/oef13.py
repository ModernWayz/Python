##
# Oefening 13
# Een pretpark baseert zijn toegangsprijs op de leeftijd van de 
# bezoeker. Kinderen jonger dan 3 betalen niets. Tussen 3 en 12 jaar 
# betalen kinderen 15eur. Mensen van 65 of ouder betalen 20eur. Alle 
# anderen betalen 30eur. Maak een programma dat alle leeftijden van een 
# bepaalde groep mensen één voor één kan inlezen. Een blanco lijn als 
# invoer markeert het einde. Het programma toont daarop de totaalprijs 
# voor deze groep en gaat vergezeld van een toepasselijke boodschap: je 
# vermeldt ook met hoeveel ze zijn en en de totaalprijs per categorie. 
# Je toont de prijzen met 2 cijfers na de komma.


BABY_PRIJS = 0.00
KINDEREN_PRIJS = 15.00
VOLWASSENEN_PRIJS = 30.00
SENIOREN_PRIJS = 20.00
BABY_LIMIET = 2
KINDEREN_LIMIET = 12
VOLWASSENEN_LIMIET = 64
totaal_bedrag = 0
bezoeker_nummer = 1
vraag = input(f"Geef de leeftijd van bezoeker nr. {bezoeker_nummer} (laat leeg om te eindigen): ")
while vraag != "":
    bezoeker_nummer += 1
    leeftijd = int(vraag)
    if leeftijd <= BABY_LIMIET:
        totaal_bedrag = totaal_bedrag + BABY_PRIJS
    elif leeftijd <= KINDEREN_LIMIET:
        totaal_bedrag = totaal_bedrag + KINDEREN_PRIJS
    elif leeftijd <= VOLWASSENEN_LIMIET:
        totaal_bedrag = totaal_bedrag + VOLWASSENEN_PRIJS
    else:
        totaal_bedrag = totaal_bedrag + SENIOREN_PRIJS
    vraag = input("Geef de leeftijd van bezoeker nr. {bezoeker_nummer} (laat leeg om te eindigen): ")
print(f"Het totale toegangsbedrag voor deze groep is {totaal_bedrag}")