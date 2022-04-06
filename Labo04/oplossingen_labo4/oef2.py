## 
# Oefening 2
# Schrijf een functie die een list en een niet-negatief geheel getal n als 
# parameters aanneemt. De functie geeft een nieuwe kopie van de list terug 
# met de n-aantal grootste en kleinste elementen uit de oorspronkelijke list 
# weggefilterd. De oorspronkelijke volgorde van de elementen in de list moet 
# niet worden behouden. Schrijf een programma dat de werking van de functie 
# demonstreert. Je functie geeft een “foutmelding” terug als het aantal 
# elementen in de lijst niet voldoende blijkt om het aantal grootste en 
# kleinste elementen te doen verdwijnen. Zo bevat een lijst van 4 elementen 
# onvoldoende elementen om de grootste en kleinste 2 elementen te doen 
# verdwijnen. Er moet minstens 1 kunnen overblijven.

def verwijder_uitersten(mijn_data, aantal_uitersten):
    if not ((len(mijn_data) - (2 * aantal_uitersten)) < 1):
        return_waarde = sorted(mijn_data)
        for i in range(aantal_uitersten):
            return_waarde.pop()
        for i in range(aantal_uitersten):
            return_waarde.pop(0)
        return return_waarde
    else:
        return "De list bevat te weinig elementen om de gevraagde uitersten te verwijderen"   

def main():
    waarden = []
    antwoord = input("Geef een waarde (leeg antwoord om af te sluiten): ") 
    while antwoord != "":
        waarde = float(antwoord)
        waarden.append(waarde)
        antwoord = input("Geef een waarde (leeg antwoord om af te sluiten): ") 
    aantal_uitersten = int(input("Geef aan hoeveel uitersten moeten worden weggenomen: "))
    print(verwijder_uitersten(waarden, aantal_uitersten))

if __name__ == "__main__":
    main()