##
# Oefening 11
# Schrijf een functie die bepaalt of een wachtwoord goed is of niet. We 
# definiëren een goed wachtwoord als een wachtwoord dat minimaal 8 tekens 
# lang is en minimaal één hoofdletter, minimaal één kleine letter en 
# minimaal één cijfer bevat. Jouw functie dient True terug te geven als het 
# wachtwoord dat eraan is doorgegeven is goed is, anders False. Voeg in een 
# functie main een programma toe dat een wachtwoord van de gebruiker leest 
# en meldt of het al dan niet goed is. Zorg ervoor dat je programma alleen 
# wordt uitgevoerd als je bestand niet is geïmporteerd in
# een ander bestand.

def controleer_wachtwoord(woord):
    ''' Deze functie kijkt na of een wachtwoord veilig is. Het geeft True terug indien dit het geval is en False indien dit niet het geval is.'''
    heeft_hoofdletter = False
    heeft_kleine_letter = False
    heeft_cijfer = False

    for karakter in woord:
        if karakter >= "A" and karakter <= "Z":
            heeft_hoofdletter = True
        elif karakter >= "a" and karakter <= "z":
            heeft_kleine_letter = True
        elif karakter >= "0" and karakter <= "9":
            heeft_cijfer = True
    if len(woord) >= 8 and heeft_hoofdletter and heeft_kleine_letter and heeft_cijfer:
        return True
    return False

def main():
    ''' Main applicatie functie '''
    wachtwoord = input("Geef een wachtwoord en ik check of het veilig is: ")
    if controleer_wachtwoord(wachtwoord):
        print("Jouw wachtwoord is een veilig wachtwoord.")
    else:
        print("Jouw wachtwoord is een onveilig wachtwoord.")

if __name__ == "__main__":
  main()
