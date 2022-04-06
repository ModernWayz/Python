##
# Oefening 13
# Anagrammen kunnen ook uit meerdere woorden bestaan. Bijvoorbeeld: “Marten 
# Asmodom Vilijn” en “Mijn naam is Voldemort” als je hoofdletters en spaties 
# niet meerekent. Breid oefening 12 uit zodat je programma kan checken of 
# twee zinnen anagrammen zijn. Je negeert hierbij hoofdletters, punctuatie 
# en spaties.

def filter_woord(woord):
    return_woord = ""
    filter_list = [" ",".","!","?"]
    for letter in woord.lower():
        if not(letter in filter_list):
            return_woord += letter
    return return_woord

def ontleed_woorden(woord):
    gefilterd_woord = filter_woord(woord)
    return_dict = {}
    for karakter in gefilterd_woord:
        if karakter in return_dict:
            return_dict[karakter] = return_dict[karakter] + 1
        else:
            return_dict[karakter] = 1
    return return_dict

def main():
    eerste_woord = input("Geef het eerste woord: ") 
    tweede_woord = input("Geef het tweede woord: ")

    ontleed_eerste_woord = ontleed_woorden(eerste_woord)
    ontleed_tweede_woord = ontleed_woorden(tweede_woord)

    print(ontleed_eerste_woord)
    print(ontleed_tweede_woord)

    if ontleed_eerste_woord == ontleed_tweede_woord:
        print("Beide woorden zijn anagrammen.")
    else:
        print("Beide woorden zijn geen anagrammen.")

if __name__ == "__main__":
    main()