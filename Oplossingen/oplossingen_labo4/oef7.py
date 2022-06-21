## 
# Oefening 7
# Een sublist is een list die deel is van een grotere list. Een sublist kan 
# een list zijn die bestaat uit een enkel element, meerdere element of zelfs 
# geen enkel element. Bijvoorbeeld: [1], [2], [3] en [4] zijn allen sublists 
# van de list [1, 2, 3, 4]. De list [2, 3] is eveneens een sublist van [1, 
# 2, 3, 4], maar [2, 4] is geen sublist van [1, 2, 3, 4] omdat elementen 2 
# en 4 niet aangrenzend zijn. Een lege list is een sublist van elke list. 
# Dus [] is een sublist van [1, 2, 3, 4]. Een list is ook een sublist van 
# zichzelf, dus [1, 2, 3, 4] is ook een sublist van [1, 2, 3, 4].
# Schrijf een functie is_sublist die twee lists (een kleinere en een 
# grotere) als parameters aanneemt en bepaalt of de ene list een sublist is 
# van de andere. De functie geeft True terug als de kleinere list een 
# sublist is van de grotere. In je programma demonstreer je de werking van 
# de functie.

def is_sublist(kleine_list, grote_list):
    """ Deze functie bepaalt of kleine_list een sublist is van grote_list. De functie geeft True terug als dit het geval is, anders False """
    # Eerst bepalen we alle sublists van grote_list
    grote_list_sublists = [[]]
    for length in range(1, len(grote_list) + 1):
        for i in range(0, len(grote_list) - length + 1):
            grote_list_sublists.append(grote_list[i : i + length])
    if kleine_list in grote_list_sublists:
        return True
    else:
        return False

def main():
    print(f"Is [] een sublist van [1, 2, 3, 4]? {is_sublist([], [1, 2, 3, 4])}")
    print(f"Is [1,2] een sublist van [1, 2, 3, 4]? {is_sublist([1,2], [1, 2, 3, 4])}")
    print(f"Is [1,6] een sublist van [1, 2, 3, 4]? {is_sublist([1,6], [1, 2, 3, 4])}")
    print(f"Is [1,4] een sublist van [1, 2, 3, 4]? {is_sublist([1,4], [1, 2, 3, 4])}")

if __name__ == "__main__":
    main()
