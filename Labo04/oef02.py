def removeHighestAndLowestFromList(someList, n):
    if n < 0:
        return "Number can not be negative."
    elif len(someList) / 2 <= n:
        return "Number is too high for the list."
    else:
        # Remove highest and lowest value n amount of times
        for i in range(n):
            # Get the index value of the highest value of the list and pop it
            someList.pop(someList.index(max(someList)))
            # Get the index value of the lowest value of the list and pop it
            someList.pop(someList.index(min(someList)))
        # Return the list
        return someList

myArray = [1, 2, 3, 4, 5, 6, 7, 8]
print(removeHighestAndLowestFromList(myArray, 4))
