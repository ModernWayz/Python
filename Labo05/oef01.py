filePath = input("Geef een bestandslocatie: ")
lines = 0

try:
    with open(filePath, "r") as the_file:
        for line in the_file:
            print(line)
            lines += 1
            if lines >= 10:
                break
except FileNotFoundError:
    print("Bestand niet gevonden")