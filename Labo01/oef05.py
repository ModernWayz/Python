KLEINE_FLES = 0.12
GROTE_FLES = 0.25

aantal_kleine = float(input("Hoeveel kleine flessen ingeleverd? "))
aantal_grote = float(input("Hoeveel grote flessen ingeleverd? "))

totaal_klein = round(aantal_kleine * KLEINE_FLES, 2)
totaal_groot = round(aantal_grote * GROTE_FLES, 2)
totaal = round(totaal_klein + totaal_groot, 2)

print(f"Je krijgt €{totaal}.")