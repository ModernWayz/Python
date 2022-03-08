from xml.etree.ElementTree import Element


def is_sublist(smallList, bigList):
    smallList = [element for element in smallList if element in bigList]
    bigList = [element for element in bigList if element in smallList]
    return smallList == bigList

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

list1 = [1, 4]
list2 = [1, 2, 3, 4]
print(sublist(list1, list2))

# Geen idee tbh geen zin