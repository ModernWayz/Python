##
# Oefening 4
# Maak een programma dat regels uit een bestand leest, er regelnummers aan 
# toevoegt en de genummerde regels vervolgens opslaat in een nieuw bestand. De 
# naam van het input-bestand wordt gevraagd aan de gebruiker, evenals de naam van 
# het nieuwe bestand dat je programma zal aanmaken. Elke regel in het 
# output-bestand moet beginnen met het regelnummer, gevolgd door een dubbele punt 
# en een spatie, gevolgd door de regel uit het input-bestand.

input_bestand = input("Geef de naam van het bestand dat moet worden ingelezen: ")
output_bestand = input("Geef de naam van het bestand waar moet naar worden geschreven: ")

try:
    with open(input_bestand, "r") as bestand:
        bestand_list = bestand.readlines()
except:
    print("Er is helaas iets foutgelopen. Probeer opnieuw ;-)")

try: 
    with open(output_bestand, "w") as bestand:
        for teller in range(len(bestand_list)):
            bestand.write(f"{str(teller+1)}: {bestand_list[teller]}")
except: 
    print("Er is helaas iets foutgelopen. Probeer opnieuw ;-)")


