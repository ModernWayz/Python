def calcOrderCost(amount):
    total = 0
    for i in range(amount):
        if i == 0:
            total += 8.5
        else:
            total += 3
    
    return total

def main():
    amount = int(input("Hoeveel artikelen? "))
    cost = calcOrderCost(amount)

    print(f"Verzendkosten: €{cost}.")

main()