##
# Oefening 5
# Als we een lijst met elementen in een tekst weergeven scheiden we de 
# elementen doorgaans met een komma. Voor het laatste element komt dan een 
# “en”.  Schrijf een functie die een list van strings als enige parameter 
# aanneemt. Jouw functie geeft een string terug die alle alle elementen van 
# de list geformatteerd teruggeeft op de manier die je hierboven ziet. Je 
# test de functie in je programma uit met lists van verschillende lengtes.

def maak_lijst(elementen):
    if len(elementen) == 0:
        return "De lijst is leeg"
    if len(elementen) == 1:
        return str(elementen[0])
    resultaat = ""
    for i in range(0, len(elementen) - 2):
        resultaat = resultaat + str(elementen[i]) + ", "
    resultaat = resultaat + str(elementen[len(elementen) - 2]) + " en "
    resultaat = resultaat + str(elementen[len(elementen) - 1])
    return resultaat

def main():
    elementen = []
    antwoord = input("Geef een item (leeg antwoord om af te sluiten): ") 
    while antwoord != "":
        elementen.append(antwoord)
        antwoord = input("Geef een item (leeg antwoord om af te sluiten): ") 
    print(maak_lijst(elementen))

if __name__ == "__main__":
    main()