MIN_VALUE = 3
MAX_VALUE = 10

amountOfSides = int(input("Aantal zijden van veelhoek? "))

if(amountOfSides > MIN_VALUE and amountOfSides < MAX_VALUE):
    if amountOfSides == 3:
        nameFigure = "driehoek"
    if amountOfSides == 4:
        nameFigure = "vierhoek"
    if amountOfSides == 5:
        nameFigure = "vijfhoek"
    if amountOfSides == 6:
        nameFigure = "zeshoek"
    if amountOfSides == 7:
        nameFigure = "zevenhoek"
    if amountOfSides == 8:
        nameFigure = "achthoek"
    if amountOfSides == 9:
        nameFigure = "negenhoek"
    if amountOfSides == 10:
        nameFigure = "tienhoek"

    print(f"Het is een {nameFigure}.")
else:
    print(f"Het programma ondersteund enkel waardes tussen {MIN_VALUE} en {MAX_VALUE}.")