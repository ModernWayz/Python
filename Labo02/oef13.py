ages = []
stopped = False

PRICE_KIDS = 15
PRICE_ADULTS = 30
PRICE_SENIORS = 20

priceKids = 0
priceAdults = 0
priceSeniors = 0

while stopped == False:
    ageInput = input("Leeftijd? ")
    if ageInput == "":
        stopped = True
        break
    
    age = int(ageInput)
    ages.append(age)
    if age <= 3:
        priceKids += 0
    elif age > 3 and age <= 12:
        priceKids += PRICE_KIDS
    elif age >= 65:
        priceSeniors += PRICE_SENIORS
    else:
        priceAdults += PRICE_ADULTS

print(f"Jullie zijn met {len(ages)} personen.")
print("Prijs per categorie:")
print(f"Kids: €{round(priceKids, 2)}")
print(f"Volwassenen: €{round(priceAdults, 2)}")
print(f"Seniors: €{round(priceSeniors, 2)}")
print(f"Totaal: €{round(priceKids + priceAdults + priceSeniors, 2)}")