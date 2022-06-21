##
# Oefening 5
# In deze oefening maak je een Python-programma dat de langste woorden in een 
# bestand identificeert. Jouw programma moet een passend bericht weergeven dat de 
# lengte van het langste woord bevat, samen met alle woorden van die lengte die in 
# het bestand voorkwamen. Behandel elke groep karakters die geen witruimte zijn 
# als een woord, zelfs als deze cijfers of leestekens bevat.

input_bestand = input("Geef de naam van het bestand dat moet worden ingelezen: ")

try:
    with open(input_bestand, "r") as bestand:
        bestand_string = bestand.read()
    bestand_list = bestand_string.split()
except:
    print("Er is helaas iets foutgelopen. Probeer opnieuw ;-)")

langste_woord = ""

for woord in bestand_list:
    if len(woord) > len(langste_woord):
        langste_woord = woord

langste_woorden_list = []
for woord in bestand_list:
    if len(woord) == len(langste_woord):
        langste_woorden_list.append(woord)

print(f"Het langste woord in het bestand is {langste_woord} met {len(langste_woord)} karakters. Andere woorden met {len(langste_woord)} karakters zijn: {', '.join(langste_woorden_list)}.")