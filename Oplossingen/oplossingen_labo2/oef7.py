##
# Oefening 7
# Volgens de chinese dierenriem zijn we dit jaar het jaar van de tijger.
# Om dit te berekenen zijn er 12 dieren die in een 12-jarige cyclus
# telkens de naam geven aan het jaar. Je vindt bvb hier een overzicht:
# https://wikikids.nl/Chinese_sterrenbeelden. Schrijf een programma dat
# een jaar vraagt aan de gebruiker en teruggeeft welk dier het jaar
# bepaalt. Je programma werkt voor elk jaar groter dan of gelijk aan 0.

jaar = int(input("Geef een jaar: "))
if jaar % 12 == 8:
    dier = "draak"
elif jaar % 12 == 9:
    dier = "slang"
elif jaar% 12 == 10:
    dier = "paard"
elif jaar % 12 == 11:
    dier = "schaap"
elif jaar % 12 == 0:
    dier = "aap"
elif jaar % 12 == 1:
    dier = "haan"
elif jaar % 12 == 2:
    dier = "hond"
elif jaar % 12 == 3:
    dier = "varken"
elif jaar % 12 == 4:
    dier = "rat"
elif jaar % 12 == 5:
    dier = "os"
elif jaar % 12 == 6:
    dier = "tijger"
elif jaar % 12 == 7:
    dier = "haas"
print(f"{jaar} is het jaar van de/het {dier}")