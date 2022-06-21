##
# Oefening 6
# Maak een functie die een string als enige parameter heeft en een nieuwe 
# string teruggeeft die de oorspronkelijke correct van hoofdletters heeft 
# voorzien. Je functie maakt een hoofdletter van de eerste letter in de 
# string (eventuele witruimte niet meegerekend). Je gaat daarnaast van de 
# eerste letter na een punt, uitroepteken of vraagteken ook een hoofdletter 
# maken. Schrijf een programma dat de functie een aantal keer demonstreert.

def geef_hoofdletters(mijn_string):
    ''' Deze functie neemt tekst als string aan als parameter en geeft deze 
        string terug, correct van hoofdletters voorzien '''
    resultaat = mijn_string
    positie = 0
    while positie < len(mijn_string) and resultaat[positie] == " ":
        positie = positie + 1
    if positie < len(mijn_string):
        resultaat = resultaat[0 : positie] + resultaat[positie].upper() + \
             resultaat[positie + 1 : len(resultaat)]

    positie = 0
    while positie < len(mijn_string):
        if resultaat[positie] == "." or resultaat[positie] == "!" or \
        resultaat[positie] == "?":
            positie = positie + 1
            while positie < len(mijn_string) and resultaat[positie] == " ":
                positie = positie + 1

            if positie < len(mijn_string):
                resultaat = resultaat[0 : positie] + \
                 resultaat[positie].upper() + \
                 resultaat[positie + 1 : len(resultaat)]

        positie = positie + 1
    return resultaat

def main():
    ''' Main applicatie functie '''
    antwoord = input("Geef een tekst die correct van hoofdletters mag worden voorzien: ")
    correcte_hoofdletters = geef_hoofdletters(antwoord)
    print("Correct van hoofdletters voorzien: ", correcte_hoofdletters)

if __name__ == "__main__":
    main()

