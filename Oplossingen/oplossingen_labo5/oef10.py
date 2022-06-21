##
# Oefening 10
# Schrijf een programma dat een bestand met informatie over chemische elementen 
# inleest en opslaat in een of meer geschikte datastructuren. Vervolgens zou je 
# programma invoer van de gebruiker moeten lezen en verwerken. Als de gebruiker 
# een geheel getal invoert, moet je programma het symbool en de naam van het 
# element met het aantal ingevoerde protonen weergeven. Als de gebruiker een 
# niet-gehele waarde invoert, moet je programma het aantal protonen weergeven voor 
# het element met die naam of dat symbool. Je programma zou een passende 
# foutmelding moeten weergeven als er geen element bestaat voor de naam, het 
# symbool of het aantal ingevoerde protonen. Ga door met het lezen van invoer van 
# de gebruiker totdat er een lege regel is ingevoerd.

# lees in bestand in met de elementen

# vraag aan de gebruiker: OF geheel getal (= PROTONEN geef terug: symbool en naam van het elementen) OF ELEMENT (aantal protonen weergeven)

# foutmelding indien er geen element bestaat 
# inlezen tot er een lege regel is ingevoerd

protonen_dict = {}
elementen_dict = {}
with open("labo5-elementen.txt", "r") as elementen_bestand:
    for element in elementen_bestand:
        element = element.rstrip().split(",")
        protonen_dict[element[0]] = f"{element[2]} ({element[1]})"
        elementen_dict[element[2]] = f"{element[0]} protonen voor {element[2]} ({element[1]})"

antwoord = input("Geef aantal protonen of de naam van een element (leeg antwoord om de toepassing te verlaten): ")

while antwoord != "":
    try:
        antwoord = int(antwoord)
        try:
            print(protonen_dict[str(antwoord)])
        except KeyError:
            print("Er bestaat geen element met het ingegeven aantal protonen")
    except ValueError:
        try:
            print(elementen_dict[str(antwoord)])
        except KeyError:
            print("Er bestaat geen element met die naam")
    antwoord = input("Geef aantal protonen of de naam van een element (leeg antwoord om de toepassing te verlaten): ")

