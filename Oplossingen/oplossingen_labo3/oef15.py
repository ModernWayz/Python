##
# Oefening 15
# Een magische datum is een datum waarbij de dag vermenigvuldigd met de 
# maand gelijk is aan de twee laatste cijfers van het jaar. 31 maart 1993 is 
# bijvoorbeeld een magische datum omdat maart de 3de maand is en 3 keer 31 
# is 93, wat gelijk is aan het jaar van twee cijfers. Schrijf een functie 
# die bepaalt of een datum al dan niet een magische datum is. Gebruik je 
# functie in een programma dat alle magische datums in de 20e eeuw vindt en 
# weergeeft. Maak gebruik van de oplossing van de vorige oefening.

from oef14 import dagen_in_een_maand

def is_magische_datum(dag, maand, jaar):
    '''Deze functie geeft terug als een meegegeven datum een zgn magische datum is'''
    if dag * maand == jaar % 100:
        return True
    return False

def main():
    ''' Main applicatie functie '''
    for jaar in range(1900, 2000):
        for maand in range(1, 13):
            for dag in range(1, dagen_in_een_maand(maand, jaar) + 1):
                if is_magische_datum(dag, maand, jaar):
                    print(f"{dag}/{maand}/{jaar} is een magische datum")

if __name__ == "__main__":
  main()