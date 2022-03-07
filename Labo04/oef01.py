stopped = False
numbers = []

while stopped == False:
    number = int(input("geef geheel getal: "))
    if number == 0:
        stopped = True
        break
    numbers.append(number)

if stopped == True:
    for i in sorted(numbers):
        print(i)