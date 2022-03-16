filePath = input("Geef een bestandslocatie: ")
fileList = []

try:
    with open(filePath, "r") as the_file:
        for line in the_file:
            fileList.append(line.rstrip())
        for line in fileList[-10:]:
            print(line)
except FileNotFoundError:
    print("Bestand niet gevonden")