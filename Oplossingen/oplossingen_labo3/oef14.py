# Oefening 14
# Schrijf een functie die uitrekent hoeveel dagen er in een bepaalde maand 
# zijn. Deze functie heeft twee parameters: de maand als een geheel getal 
# tussen 1 en 12 en het jaar als een geheel getal van vier cijfers. Zorg 
# ervoor dat jouw functie het juiste aantal dagen in februari teruggeeft 
# voor schrikkeljaren. Voeg een programma toe dat een maand en jaar van de 
# gebruiker afleest en het aantal dagen in die maand weergeeft.

def dagen_in_een_maand(maand_getal, jaar):
    '''Functie die een maand en een jaar als integer inneemt en het aantal dagen dat deze maand telt teruggeeft'''
    if maand_getal in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif maand_getal in [4, 6, 9, 11]:
        return 30
    else:
        if schrikkeljaar(jaar):
            return 29
        else:            
            return 28

def schrikkeljaar(jaar):
    '''Functie die bepaalt of een bepaald jaar een schrikkeljaar is'''
    if jaar % 400 == 0:
        return True
    if jaar % 100 == 0:
        return False
    if jaar % 4 == 0:
        return True
    return False

def main():
    ''' Main applicatie functie '''
    maand = int(input("Geef de maand als geheel getal: "))
    jaar = int(input("Geef de maand als geheel getal: "))
    print(f"{maand}/{jaar} bestaat uit {dagen_in_een_maand(maand,jaar)} dagen")

if __name__ == "__main__":
  main()


