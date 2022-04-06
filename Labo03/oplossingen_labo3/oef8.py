##
# Oefening 8
# Een priemgetal is een geheel getal groter dan één dat alleen deelbaar is 
# door één en zichzelf. Schrijf een functie die bepaalt of zijn parameter 
# een priemgetal is, en geef True terug als dat zo is, en anders False. 
# Schrijf in een functie main een programma dat een geheel getal van de 
# gebruiker leest en een bericht weergeeft dat aangeeft of het priemgetal is 
# of niet. Zorg ervoor dat het hoofdprogramma niet wordt uitgevoerd als het 
# bestand met jouw oplossing wordt geïmporteerd in een ander programma.

def is_priemgetal(getal):
    ''' Deze functie neemt een integer in als parameter en gaat na of het om een priemgetal gaat. De functie geeft True of False terug.'''
    if getal <= 1:
        return False
    for i in range(2, getal):
        if getal % i == 0:
            return False
    return True

def main():
    ''' Main applicatie functie '''
    antwoord = int(input("Geef een geheel getal in: "))
    if is_priemgetal(antwoord):
        print(f"{antwoord} is een priemgetal.")
    else:
        print(f"{antwoord} is geen priemgetal.")

if __name__ == "__main__":
    main()

