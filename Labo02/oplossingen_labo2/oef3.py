##
# Oefening 3
# Je maakt een programma dat een letter van het alfabet vraagt aan de
# gebruiker. Als de gebruiker een klinker (a, e, i, o of u) invoert dan
# volgt een bericht dat de letter die is ingevoerd een klinker is. Bij
# invoer van y volgt de boodschap dat deze letter soms als klinker, en
# soms als medeklinker kan gelden. In elk ander geval volgt de boodschap
# dat een medeklinker werd ingevoerd. Bij een string die langer is dan 1
# karakter zorg je voor een bericht dat je de uitkomst niet kan bereken
# als meer dan één karakter werd ingevoerd. Tip: je kan dit laatste
# checken met de len() functie.

letter = input("Geef een letter: ")
if len(letter) > 1:
    print("Je mag slechts één letter invoeren")
else:
    if letter == "a" or letter == "e" or letter == "i" or \
        letter == "o" or letter == "u":
        print("De ingevoerde letter is een klinker")
    elif letter == "y":
        print("De ingevoerde letter wordt soms beschouwd als klinker, soms als medeklinker")
    else:
        print("De ingevoerde letter is een medeklinker")
