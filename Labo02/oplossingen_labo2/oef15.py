##
# Oefening 15
# Is een string een palindroom? https://nl.wikipedia.org/wiki/
# Palindroom. Een string is een palindroom als het identiek is gelezen 
# van links en rechts en van rechts naar links. Zo zijn “meetsysteem” en 
# “stormrots” voorbeelden van palindromen. Schrijf een programma dat een 
# string vraagt aan een gebruiker en een loop gebruikt om te bepalen of 
# het woord al dan niet een palindroom is. Gebruik print om met een 
# betekenisvol bericht eventueel te bevestigen of dat het geval is.
# Tip:
# Je kunt bvb positie 5 van een string opvragen met mijnstring[4]... De 
# aantal karakters in een string krijg je met len(mijnstring)...

woord = input("Geef een string: ")
is_palindroom = True

i=0
while i < len(woord) / 2 and is_palindroom:
    if woord[i] != woord[len(woord) - i - 1]:
        is_palindroom = False
    i=i+1
if is_palindroom:
    print(f"De string '{woord}' is een palindroom")
else:
    print(f"De string '{woord}' is GEEN palindroom")
