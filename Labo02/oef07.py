year = int(input("Geef een jaar: "))

if year >= 0:
    if (year - 2000) % 12 == 0:
        animal = "draak"
    if (year - 2000) % 12 == 1:
        animal = "slang"
    if (year - 2000) % 12 == 2:
        animal = "paard"
    if (year - 2000) % 12 == 3:
        animal = "geit"
    if (year - 2000) % 12 == 4:
        animal = "aap"
    if (year - 2000) % 12 == 5:
        animal = "haan"
    if (year - 2000) % 12 == 6:
        animal = "hond"
    if (year - 2000) % 12 == 7:
        animal = "varken"
    if (year - 2000) % 12 == 8:
        animal = "rat"
    if (year - 2000) % 12 == 9:
        animal = "os"
    if (year - 2000) % 12 == 10:
        animal = "tijger"
    else:
        animal = "konijn"
    print(f"{year} is het jaar van: {animal}.")
else:
    print("Dat is geen geldig jaar.")