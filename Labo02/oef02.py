DOG_YEAR = 4
EARLY_DOG_YEAR = 10.5

humanYear = int(input("Hoe oud is je hond? (in jaar) "))
dogYear = 0

if humanYear < 0:
    print("Je kan geen negatief getal ingeven")
else:
    i = 0
    for number in range(humanYear):
        if i < 2:
            dogYear += EARLY_DOG_YEAR
        else:
            dogYear += DOG_YEAR
        i += 1
    print(f"Jouw hond is {dogYear} jaar oud in hondenjaren.")