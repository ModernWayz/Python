##
# Oefening 1
# Schrijf een programma dat een integer getal vraagt aan de gebruiker.
# Jouw programma geeft dan een boodschap terug met of het hier om een
# even of oneven getal gaat. Tip: gebruik de modulus operator (%) om te
# bepalen of een getal even of oneven is.

getal = int(input("Geef een geheel getal: "))
output = "oneven"
if getal % 2 == 0:
    output = "even"
print(f"Het getal {getal} is {output}")