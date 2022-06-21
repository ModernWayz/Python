##
# Oefening 8
# Gebruik makend van de definitie van een sublist uit de vorige oefening 
# schrijf je een functie die een list teruggeeft met daarin alle mogelijke 
# sublists van een list die aan de functie als argument wordt meegegeven. 
# Bijvoorbeeld: de sublists van [1,2,3] zijn [], [1], [2], [3], [1, 2], [2, 
# 3] en [1, 2, 3]. Merk op dat je functie altijd een list teruggeeft die 
# minstens een lege list teruggeeft omdat een lege list een sublist is van 
# elke list. Voeg een programma toe die de werking van de functie 
# illustreert door de functie verschillende keren aan te roepen met 
# verschillende lists.

def geef_alle_sublists(data):
    sublists = [[]] # een list met een lege list als element ;-)
    for length in range(1, len(data) + 1):
        for i in range(0, len(data) - length + 1):
            sublists.append(data[i : i + length])
    return sublists

def main():
    print("The sublists van [] zijn: ")
    print(geef_alle_sublists([]))
    print("The sublists of [1] zijn: ")
    print(geef_alle_sublists([1]))
    print("The sublists of [1, 2] zijn: ")
    print(geef_alle_sublists([1, 2]))
    print("The sublists of [1, 2, 3] zijn: ")
    print(geef_alle_sublists([1, 2, 3]))
    print("The sublists of [1, 2, 3, 4] zijn: ")
    print(geef_alle_sublists([1, 2, 3, 4]))

if __name__ == "__main__":
    main()