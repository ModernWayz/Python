##
# Oefening 11
# Maak een programma die het aantal unieke karakters bepaalt en weergeeft in 
# een string die door de gebruiker werd ingegeven. Bijvoorbeeld: “Ik hou van 
# Python!” heeft 13 unieke karakters. Gebruik een dictionary om dit probleem 
# op te lossen.

antwoord = input("Geef een string: ")
dict_unieke_karakters = {}
for karakter in antwoord:
    dict_unieke_karakters[karakter] = True

print(f"Deze string telt {len(dict_unieke_karakters)} unieke karakters.")