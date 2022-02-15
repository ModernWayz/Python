letter = input("Geef een letter van het alfabet: ")

VOWELS = ["a","e","i","o","u"]

if len(letter) > 1:
    print("De uitkomst kan niet berekend worden als meer dan één karakter werd ingevoerd.")
else:
    if letter in VOWELS:
        print(f"{letter} is een klinker.")
    elif letter == "y":
        print(f"{letter} is een klinker maar kan ook een medeklinker zijn.")
    else:
        print(f"{letter} is een medeklinker.")