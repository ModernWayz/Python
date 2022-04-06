## 
# Oefening 10
# Schrijf een functie die een willekeurig wachtwoord genereert. Het
# wachtwoord moet een willekeurige lengte hebben tussen 7 en 10 tekens. Elk
# teken moet willekeurig worden gekozen uit posities 33 tot 126 in de
# ASCII-tabel. Je functie heeft geen parameters nodig. Het zal het
# willekeurig gegenereerde wachtwoord teruggeven als resultaat. Voer de 
# functie uit binnen je programma en zorg ervoor dat dat het alleen wordt 
# uitgevoerd als dit bestand niet in een ander bestand is geïmporteerd. Tip: 
# gebruik de random module en de chr-functie bij het oplossen van deze 
# oefening.

from random import randint

KORTSTE = 7
LANGSTE = 10
MIN_ASCII_CODE = 33
MAX_ASCII_CODE = 126

def willekeurig_wachtwoord():
    ''' Deze functie genereert en geeft een willekeurig wachtwoord terug '''
    willekeurige_lengte = randint(KORTSTE, LANGSTE)
    resultaat = ""
    for i in range(willekeurige_lengte):
        willekeurig_karakter = chr(randint(MIN_ASCII_CODE, MAX_ASCII_CODE))
        resultaat = resultaat + willekeurig_karakter
    return resultaat

def main():
    ''' Main applicatie functie '''
    print("Je willekeurige wachtwoord is:", willekeurig_wachtwoord())

if __name__ == "__main__":
    main()