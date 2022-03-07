def sumItems(someList):
    line = ""
    j = 0
    for i in someList:
        if j == len(someList) -2:
            line += i + " en "
        elif j == len(someList) -1:
            line += i
        else:
            line += i + ", "
        j+= 1
    print(line)

myList = ["rozen", "kranten", "ketels", "wanten"]
sumItems(myList)