##
# Oefening 12
# We noemen twee woorden anagrammen als ze dezelfde letters bevatten, maar 
# in een verschillende volgorde. Schrijf een programma dat twee strings van 
# een gebruiker inleest en bepaalt en teruggeeft of beide strings anagrammen 
# zijn. Gebruik een dictionary om dit probleem op te lossen.

def ontleed_woord(woord):
    return_dict = {}
    for karakter in woord: # Je zou hier ook sorted(woord) hebben kunnen gebruiken, maar hoeft niet: volgorde in dictionaries speelt geen rol
        if karakter in return_dict:
            return_dict[karakter] = return_dict[karakter] + 1
        else:
            return_dict[karakter] = 1
    return return_dict

def main():
    eerste_woord = input("Geef het eerste woord: ") 
    tweede_woord = input("Geef het tweede woord: ")

    ontleed_eerste_woord = ontleed_woord(eerste_woord)
    ontleed_tweede_woord = ontleed_woord(tweede_woord)

    print(ontleed_eerste_woord)
    print(ontleed_tweede_woord)

    if ontleed_eerste_woord == ontleed_tweede_woord:
        print("Beide woorden zijn anagrammen.")
    else:
        print("Beide woorden zijn geen anagrammen.")

if __name__ == "__main__":
    main()