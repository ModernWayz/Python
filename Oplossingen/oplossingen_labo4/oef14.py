##
# Oefening 14
# Een bingo-kaart bestaat uit 5 kolommen van telkens 5 getallen. De kolommen 
# zijn gelabeld met de letters B, I, N, G en O. Er zijn 15 getallen die 
# onder elke letter kunnen terecht komen:
# - Onder de “B” zijn dat 1 tot en met 15
# - Onder de “I” zijn dat 16 tot en met 30
# - Onder de “N” zijn dat 31 tot en met 45
# - Onder de “G” zijn dat 46 tot en met 60
# - Onder de “O” zijn dat 61 tot en met 75
# Schrijf een functie die een willekeurige bingo-kaart aanmaakt en deze als 
# dictionary opslaat. De keys zijn de letters, de waarden telkens een list 
# van 5 getallen. Schrijf een tweede functie die de bingo-kaart weergeeft 
# met de gelabelde kolommen en een dictionary aanneemt als parameter.

from random import randrange

CIJFERS_PER_LETTER = 15

def maak_kaart():
    card = {}
    lower = 1
    upper = 1 + CIJFERS_PER_LETTER
    for letter in ["B", "I", "N", "G", "O"]: 
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
            if next_num not in card[letter]:
                card[letter].append(next_num)
        lower = lower + CIJFERS_PER_LETTER
        upper = upper + CIJFERS_PER_LETTER
    return card

def toon_kaart(bingo_kaart):
    print("B\tI\tN\tG\tO")
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print(f"{bingo_kaart[letter][i]}\t", end="")
        print()

def main():
  mijn_bingo_kaart = maak_kaart()
  toon_kaart(mijn_bingo_kaart)

if __name__ == "__main__":
  main()

