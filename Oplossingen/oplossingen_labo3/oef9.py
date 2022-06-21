##
# Oefening 9
# Je maakt een functie genaamd volgend_priemgetal die een geheel getal als 
# parameter neemt en het eerste priemgetal dat groter is dan dat getal vindt 
# en teruggeeft. Voeg een programma toe dat een geheel getal leest van de 
# gebruiker en het eerste priemgetal teruggeeft dat groter is dan de 
# ingevoerde waarde. Importeer en gebruik je oplossing van de vorige oefening.

from oef8 import is_priemgetal

def volgend_priemgetal(getal):
    '''Deze functie neemt een geheel getal als parameter en geeft het eerste priemgetal terug dat groter is dan dat getal '''
    teller = getal+1
    while is_priemgetal(teller) == False:
        teller += 1
    return teller

def main():
    ''' Main applicatie functie '''
    antwoord = int(input("Geef een geheel getal in: "))
    print(f"Het eerste priemgetal volgend op {antwoord} is {volgend_priemgetal(antwoord)}")

if __name__ == "__main__":
    main()


