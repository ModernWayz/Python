##
# Oefening 13
# Schrijf een functie waaraan twee positieve gehele getallen die de teller 
# en noemer van een breuk vertegenwoordigen, als enige parameters moeten 
# doorgegeven worden. De functie moet de breuk vereenvoudigen en reduceren 
# tot de eenvoudigste vorm en vervolgens zowel de teller als de noemer van 
# de gereduceerde breuk als resultaat teruggeven. Als de parameters die aan 
# de functie worden doorgegeven bijvoorbeeld 6 en 27 zijn, moet de functie 2 
# en 9 teruggeven. Voeg een main-programma toe waarmee de gebruiker een 
# teller en noemer kan invoeren. Jouw programma geeft dan de gereduceerde 
# breuk terug aan de gebruiker.

def grootste_gemene_deler(getal1, getal2):
    kleinste_getal = min(getal1, getal2)
    while getal1 % kleinste_getal != 0 or getal2 % kleinste_getal != 0: 
        kleinste_getal -= 1
    return kleinste_getal

def vereenvoudig(teller, noemer):
    if teller == 0:
        return (0, 1)
    ggd = grootste_gemene_deler(teller, noemer)
    return (teller // ggd, noemer // ggd)

def main():
    ''' Main applicatie functie '''
    teller = int(input("Geef de teller: ")) 
    noemer = int(input("Geef de noemer: "))
    (vteller, vnoemer) = vereenvoudig(teller, noemer)
    print(f"{teller}/{noemer} kan vereenvoudigd worden tot {vteller}/{vnoemer}")

main()

