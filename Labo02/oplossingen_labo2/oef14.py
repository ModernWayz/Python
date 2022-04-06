##
# Oefening 14
# Eén van de oudste vormen van encryptie werd naar verluid gebruikt door 
# Julius Caesar. Hij wilde instructies sturen naar zijn generaals, 
# zonder dat zijn vijanden de boodschap zouden kunnen ontcijferen mocht 
# ze in hun handen belanden. Hiervoor werd het zgn Caesarcijfer 
# ontwikkeld (https://nl.wikipedia.org/wiki/Caesarcijfer). Het idee 
# erachter is eenvoudig: elke letter in de originele boodschap wordt 
# verschoven met 3 plaatsen: A wordt D, B wordt E, C wordt F enz.
# De drie laatste letters van het alfabet mappen terug op de 
# beginletters Niet-letter karakters worden niet aangepast. Schrijf een 
# programma die de encryptie uitvoert. Laat de gebruiker toe de 
# boodschap in te geven, alsook het getal dat dient te worden 
# opgeschoven (hierboven was dat 3). Zorg ervoor dat je programma zowel 
# kleine als grote letters encodeert. Je programma moet ook negatieve 
# shifts ondersteunen, zodat het programma ook kan gebruikt worden om de 
# boodschap te ontcijferen.

print(f"Een voorbeeld: de unicode-positie van de letter 'h' is {ord('h')}")
print(f"Een voorbeeld: het karakteer dat unicode 105 vertegenwoordigt is {chr(105)}")

boodschap = input("Geef de boodschap: ")
shift = int(input("Hoeveel plaatsen opschuiven? "))
nieuwe_boodschap = ""
for karakter in boodschap:
    if karakter >= "a" and karakter <= "z":
        pos = ord(karakter) - ord("a")
        pos = (pos + shift) % 26
        nieuw_karakter = chr(pos + ord("a")) 
        nieuwe_boodschap = nieuwe_boodschap + nieuw_karakter
    elif karakter >= "A" and karakter <= "Z":
        pos = ord(karakter) - ord("A")
        pos = (pos + shift) % 26
        nieuw_karakter = chr(pos + ord("A"))
        nieuwe_boodschap = nieuwe_boodschap + nieuw_karakter
    else:
        # een niet-letter
        nieuwe_boodschap = nieuwe_boodschap + karakter
print(f"De beveiligde boodschap is {nieuwe_boodschap}")