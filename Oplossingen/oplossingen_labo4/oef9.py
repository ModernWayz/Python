##
# Oefening 9
# Schrijf een functie omgekeerd_zoeken die alle keys in een dictionary vindt 
# die een bepaalde value hebben. Deze functie heeft twee parameters: de 
# dictionary en de waarde die moet worden gevonden. De functie geeft een 
# (mogelijke lege) list van keys terug uit de dictionary die dus mappen op 
# de gezochte waarde. Je voegt een programma toe die de functie een aantal 
# keer demonstreert met relevante voorbeelden.

def omgekeerd_zoeken(data, waarde):
    keys = []
    for key in data:
        if data[key] == waarde:
            keys.append(key)
    return keys

def main():
    mijn_dict = {"speler 1" : 1200, "speler 2" : 1800, "speler 3" : 23000, "speler 4" : 1200}
    print(omgekeerd_zoeken(mijn_dict, 1200))
    print(omgekeerd_zoeken(mijn_dict, 1800))
    print(omgekeerd_zoeken(mijn_dict, 3500))

if __name__ == "__main__":
    main()
