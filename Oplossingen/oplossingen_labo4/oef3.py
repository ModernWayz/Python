##
# Oefening 3
# Schrijf een programma dat woorden aan de gebruiker als input vraagt zolang 
# de gebruiker geen lege lijn teruggeeft. Nadat dit laatste gebeurd is geeft 
# het programma elk woord dat is ingevoerd exact één keer terug. De woorden 
# moeten weergegeven worden in dezelfde volgorde als ze werden ingevoerd.

woorden = []
woord = input("Geef een woord (leeg antwoord om af te sluiten): ")

while woord != "":
    if woord not in woorden:
        woorden.append(woord)
    woord = input("Geef een woord (leeg antwoord om af te sluiten): ")

for woord in woorden:
  print(woord)