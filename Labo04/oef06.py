import random

lottery = []

for i in range(6):
    number = random.randint(1, 49)
    if number not in lottery:
        lottery.append(number)

print(sorted(lottery))

