##
# # Oefening 1
# 
# Schrijf een programma dat gehele getallen van de gebruiker 
# leest en opslaat in een list. Je programma gaat door met het 
# lezen van waarden totdat de gebruiker 0 invoert. Dan zou het 
# alle waarden moeten weergeven die door de gebruiker zijn 
# ingevoerd (behalve de 0) in oplopende volgorde, met één 
# waarde op elke regel. Gebruik ofwel de sort method of de 
# sorted-functie om de list te ordenen.

mijn_data = []
getal = int(input("Geef een geheel getal (0 om af te sluiten): "))
while getal != 0:
    mijn_data.append(getal)
    getal = int(input("Geef een geheel getal (0 om af te sluiten): "))
    mijn_data.sort()
    print("De ingevoerde waarden, van klein naar groot, zijn:")
    
# je zou hier ook kunnen schrijven: for getal in sorted(mijn_data):
for getal in mijn_data:
    print(getal)