import sys
import data
import checks

def main():
    data.initialisatie()
    if len(sys.argv) > 1: # commandline
        if sys.argv[1] == "-c": # checks uitvoeren via de commandline
            checks.uitvoeren()
            print("Check afgerond. Over en sluiten...")
        elif sys.argv[1] == "-a": # check toevoegen
            # "ping" hostname aantal_tests percentage
            type_check = sys.argv[2]
            check_data = [sys.argv[3], sys.argv[4], sys.argv[5]]
            checks.toevoegen(type_check, check_data)
        elif sys.argv[1] == "-d": # check verwijderen
            # indexgetal wordt gebruikt om check te verwijderen
            checks.verwijderen(sys.argv[2])
        elif sys.argv[1] == "-s": # geef lijst van bestaande checks
            print(checks.oplijsten())
    else: # interactief
        antwoord = int(input("Kies 1 om check aan te maken, 2 om check te verwijderen, 3 om op te lijsten, 4 om te checken, 0 om te verlaten: "))
        while antwoord != 0:
            if antwoord == 1: # check aanmaken
                type_check = input("Welke check wil je aanmaken? Kies ping voor een ping-check :")
                host_name = input("Naam van de host? ")
                aantal_tests = input("Hoeveel checks?")
                percentage = input("Percentage dat succesvol moet zijn (bvb 100)? ")
                check_data = [host_name, aantal_tests, percentage]
                checks.toevoegen(type_check, check_data)         
            elif antwoord == 2: # check verwijderen
                print(checks.oplijsten())
                index_getal = input("Geef het indexgetal van de check die je wil verwijderen: ")
                checks.verwijderen(index_getal)
            elif antwoord == 3: # check oplijsten
                print(checks.oplijsten())
            elif antwoord == 4: # checks uitvoeren
                checks.uitvoeren()
            antwoord = int(input("Kies 1 om check aan te maken, 2 om check te verwijderen, 3 om op te lijsten, 4 om te checken, 0 om te verlaten: "))

main()