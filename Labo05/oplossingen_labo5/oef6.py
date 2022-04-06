##
# Oefening 6
# Schrijf een programma dat het woord (of de woorden) weergeeft die het vaakst in 
# een bestand voorkomen. Je programma begint met het vragen van de naam van het 
# bestand dat moet ingelezen worden aan de gebruiker. Dan zou het elke regel in 
# het bestand moeten verwerken. Elke regel moet worden opgesplitst in woorden en 
# alle leestekens vóór of achter moeten uit elk woord worden verwijderd. Je 
# programma negeert ook de hoofdletters bij het tellen hoe vaak elk woord 
# voorkomt: ‘Favoriet’ en ‘favoriet’ bvb zijn dus hetzelfde woord.

input_bestand = input("Geef de naam van het bestand dat moet worden ingelezen: ")

try:
    with open(input_bestand, "r") as bestand:
        bestand_string = bestand.read()
    bestand_list = bestand_string.split()
except:
    print("Er is helaas iets foutgelopen. Probeer opnieuw ;-)")

# We stoppen alle woorden in onze list in een dictionary die als value de frequentie van voorkomen heeft
frequentie_dict = {}
for woord in bestand_list:
    woord = woord.lower().strip('!?')
    if woord in frequentie_dict:
      frequentie_dict[woord] += 1
    else:
      frequentie_dict[woord] = 1

# We bekomen de hoogste frequentie, met wat we tot op heden in de lessen hebben gezien (het kan korter)
hoogste_frequentie = 1
for key, value in frequentie_dict.items():
    if value > hoogste_frequentie:
        hoogste_frequentie = value

# We bekomen alle woorden met deze hoogste frequentie
print(f"Volgend(e) woord(en) komen het vaakst voor, namelijk {hoogste_frequentie} keer:")
for key, value in frequentie_dict.items():
    if value == hoogste_frequentie:
        print(key)


