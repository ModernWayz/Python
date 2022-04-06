## Oefening 2: een visitekaartje afgeven
# Maak een programma dat een virtuele business card van jezelf 
# weergeeft. Je gebruikt daarvoor het print-commando. De informatie, die 
# ook uit wat interesses mag bestaan, bepaal je zelf. Je mag hiervoor 
# enkele variabelen  creëren en gebruik maken van f-strings en 
# niet-afdrukbare tekens als "\n” om ze te formatteren. Dit programma 
# verwacht geen input van de gebruiker.

# Dit is maar een voorbeeld. De html-elementen zijn hier gebruikt als 
# humoristisch element, meer niet ;-)
voornaam = "Kristof"
naam = "Michiels"
functie = "Ontwikkelaar Web"
email = "kristof.michiels01@ap.be"

print("<card>")
print(f"\t<name>{voornaam} {naam}</name>")
print(f"\t<title>{functie}</title>")
print(f"\t<email>{functie}</email>")
print("</card>")