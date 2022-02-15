import random

GREEN = [0, 00]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

print("Place your bets")
betNumber = int(input("nummer? "))
betColor = input("rood/zwart? ")
betEven = input("even/oneven? ")
#betNumberGroup = input("")

randomInt = random.randint(0, 36)

# ik heb geen goesting in deze oefening sorry

print(f"Het balletje is beland op vakje: {randomInt}.")
