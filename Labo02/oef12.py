stopped = False
firstIteration = True

print("Geef getallen om een gemiddelde van te berekenen")
print("Zet een 0 om te stoppen")

numbers = []
while stopped == False:
    number = int(input("Geef een getal: "))
    if number == 0:
        if firstIteration:
            print("Je kan niet 0 als eerste getal geven.")
        else:
            stopped = True
    else:
        numbers.append(number)
        firstIteration = False

average = round(sum(numbers) / len(numbers), 2)

print(f"Het gemiddelde is {average}.")