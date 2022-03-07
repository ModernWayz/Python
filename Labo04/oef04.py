from numpy import negative


stopped = False
positiveNumbers = []
negativeNumbers = []

while stopped == False:
    number = input("geef getal: ")
    if number == "":
        stopped = True
        break
    elif int(number) >= 0:
        positiveNumbers.append(number)
    elif int(number) < 0:
        negativeNumbers.append(number)

if stopped == True:
    for i in negativeNumbers:
        print(i)
    for i in positiveNumbers:
        print(i)