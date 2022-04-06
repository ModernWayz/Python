##
# Oefening 7
# Je maakt een functie is_integer() die nagaat of de karakters in een string 
# een integer vertegenwoordigen. Je verwijdert alle eventuele witruimte voor 
# en na de ingevoerde string. Je geeft True terug als de lengte na 
# verwijderen van witruimte minstens 1 bedraagt en enkel uit getallen 
# bestaat, of als het eerste karakter een + of een - is en de rest allemaal 
# getallen. Schrijf in een main-functie een programma dat een string vraagt 
# aan de gebruiker en teruggeeft of het hier al dan niet om een integer 
# gaat. Zorg ervoor dat het programma niet loopt als deze oplossing wordt 
# geïmporteerd binnen een ander programma.

# ik heb hier gebruik gemaakt van de isdigit functie. Deze oefening kan uiteraard
# ook zonder deze functie worden opgelost. Meer informatie vind je hier: https://www.w3schools.com/python/ref_string_isdigit.asp

def is_integer(mijn_string):
    ''' Deze functie kijkt na of een string een integer is of niet. Ze neemt een string aan als parameter en geeft True (het is een integer) of False (het is het niet) terug'''
    if (mijn_string[0] == "+" or mijn_string[0] == "-") and mijn_string[1:].isdigit():
        return True
    if mijn_string.isdigit():
        return True
    return False

def main():
    ''' Main applicatie functie '''
    antwoord = input("Geef een string: ")
    if is_integer(antwoord):
        print("Deze string vertegenwoordigt een integer.")
    else:
        print("Deze string vertegenwoordigt geen integer.")

if __name__ == "__main__":
    main()

