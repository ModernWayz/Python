import statistics

from numpy import number

def calcMedian(number1, number2, number3):
    numbers = [number1, number2, number3]
    return statistics.median(numbers)

number1 = int(input("Getal 1? "))
number2 = int(input("Getal 2? "))
number3 = int(input("Getal 3? "))

medianNumber = calcMedian(number1, number2, number3)

print(f"De mediaan is: {medianNumber}.")