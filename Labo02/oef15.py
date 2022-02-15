word = input("Geef een woord: ")

if word == word[::-1]:
    print(f"{word} is een palindroom.")
else:
    print(f"{word} is geen palindroom.")