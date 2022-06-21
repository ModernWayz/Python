##
# Oefening 12
# Sommige van de namen die voorkomen in de lijsten werden zowel aan jongens als 
# aan meisjes gegeven. Schrijf een programma dat voor een - door de gebruiker 
# ingegeven - specifiek jaar aan meisjes én aan jongens werden gegeven. Je 
# programma geeft een boodschap als je voor dat bepaald jaar geen namen hebt 
# gevonden. Geef een gepaste foutmelding terug als je voor het aangevraagde jaar 
# geen data hebt. Maak gebruik van de babynamen dataset uit oefening 11.


# zelfde naam aan meisjes én jongens
# invoer jaartal van gebruiker

jaartal = input("Geef het jaar (tussen 1900 en 2021) waarop je wenst te zoeken: ")

meisjes_bestand = "baby_namen/" + str(jaartal) + "_GirlsNames.txt"
jongens_bestand = "baby_namen/" + str(jaartal) + "_BoysNames.txt"
meisjes_list = []
jongens_list = []
gemeenschappelijke_list = []

def vul_list(bestandsnaam, naam_list):
    try:
        with open(bestandsnaam, "r") as bestand:
            for regel in bestand:
                regel_list = regel.split()
                naam = regel_list[0]
                if naam not in naam_list:
                    naam_list.append(naam)
    except FileNotFoundError:
        print("Er is geen data bekend voor dit jaar")
        quit()


vul_list(meisjes_bestand, meisjes_list)
vul_list(jongens_bestand, jongens_list)

# gemeenschappelijke_list vullen
for naam in meisjes_list:
    if naam in jongens_list:
        gemeenschappelijke_list.append(naam)

if len(gemeenschappelijke_list) == 0:
    print(f"Er zijn voor het jaar {jaartal} geen gemeenschappelijke namen gevonden")
else:
    print(f"Er zijn voor het jaar {jaartal} volgende gemeenschappelijke namen gevonden: {', '.join(gemeenschappelijke_list)}")