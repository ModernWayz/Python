from curses.ascii import isupper


text = input("Te encrypteren tekst: ")

CHAR_SHIFT = 3

encrypted = ""
decrypted = ""

for i in range(len(text)):
    tsjerekter = text[i]
    if isupper(tsjerekter):
        encrypted += chr((ord(tsjerekter) + CHAR_SHIFT - 65) % 26 + 65)
    else:
        encrypted += chr((ord(tsjerekter) + CHAR_SHIFT - 97) % 26 + 97)

for i in range(len(encrypted)):
    tsjerekter = encrypted[i]
    if isupper(tsjerekter):
        decrypted += chr((ord(tsjerekter) - CHAR_SHIFT - 65) % 26 + 65)
    else:
        decrypted += chr((ord(tsjerekter) - CHAR_SHIFT - 97) % 26 + 97)

print(f"Geëncrypteerd: {encrypted}")
print(f"Hacked: {decrypted}")