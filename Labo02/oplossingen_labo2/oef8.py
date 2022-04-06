##
# Oefening 8
# De meeste jaren hebben 365 dagen. De tijd die de aarde nodig heeft om
# rond de zon te gaan is echter een klein beetje langer dan dat. Als
# resultaat hebben we schrikkeljaren en geven we in die jaren februari
# een extra 29ste dag. De regels voor een schrikkeljaar:
# - Elk jaar deelbaar door 400 is een schrikkeljaar
# - Van de overige jaren: elk jaar deelbaar door 100 is geen
# schrikkeljaar 
# - Van de overige jaren: elk jaar deelbaar door 4 is een schrikkeljaar
# - Alle andere jaren zijn geen schrikkeljaren
# Schrijf een programma dat een jaar vraagt aan de gebruiker en een
# bericht teruggeeft dat meegeeft of dat jaar een schrikkeljaar is of niet.

jaar = int(input("Geef een jaar: "))
if jaar % 400 == 0:
    is_schrikkeljaar = True
elif jaar % 100 == 0:
    is_schrikkeljaar = False
elif jaar % 4 == 0:
    is_schrikkeljaar = True
else:
    is_schrikkeljaar = False

if is_schrikkeljaar:
    print(f"{jaar} is een schrikkeljaar.")
else:
    print(f"{jaar} is geen schrikkeljaar.")
