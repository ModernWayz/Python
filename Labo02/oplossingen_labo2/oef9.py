##
# Oefening 9
# Een roulettewiel heeft 38 vakjes. Van deze vakjes zijn er 18 zwart, 18 
# rood en 2 groen. De groene vakjes hebben de nummers 0 en 00. De rode 
# 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 en 36. 
# De overblijvende gehele getallen tussen 1 en 36 zijn zwart. In 
# roulette kan je verschillende gokken doen. We zullen in deze oefening 
# enkel de volgende gebruiken:
# - Enkel nummer (1 tot 36, 0 en 00)
# - Rood vs zwart
# - Oneven vs even (0 en 00 tellen niet als even) 1 t.e.m. 18 vs 19 
#   t.e.m. 36
# Schrijf een programma dat een draai aan het roulettewiel simuleert.
# Toon het nummer dat werd gekozen en maak duidelijk welke gokken moeten
# uitbetaald worden. Bvb:
# - Balletje is beland op vakje 15 Betaal 15
# - Betaal zwart
# - Betaal oneven
# - Betaal 1 t.e.m. 18
# - Als de simulatie resulteert in 0 of 00 geeft het programma gewoon 
#   “Betaal 0” of “Betaal 00” terug.
# Tip: maak hiervoor gebruik van de random module en de randint()
# method: https://www.w3schools.com/python/ref_random_randint.asp

from random import randrange

waarde = randrange(0, 38)
# We gebruiken 37 als voorstelling 00
if waarde == 37:
    print("Balletje kwam terecht in vakje 00.")
else:
    print(f"Balletje kwam terecht in {waarde}")
if waarde == 37:
    print("Betaal 00")
else:
    print("Betaal", waarde)

if waarde % 2 == 1 and waarde >= 1 and waarde <= 9 or \
   waarde % 2 == 0 and waarde >= 12 and waarde <= 18 or \
   waarde % 2 == 1 and waarde >= 19 and waarde <= 27 or \
   waarde % 2 == 0 and waarde >= 30 and waarde <= 36:
    print("Betaal rood")
elif waarde == 0 or waarde == 37:
    pass 
    # Of print("Doe niets")
else:
    print("Betaal zwart")

if waarde >= 1 and waarde <= 36:
    if waarde % 2 == 1:
        print("Betaal oneven")
    else:
        print("Betaal even")

if waarde >= 1 and waarde <= 18:
    print("Betaal 1 tot 18")
elif waarde >= 19 and waarde <= 36:
    print("Betaal 19 tot 36")