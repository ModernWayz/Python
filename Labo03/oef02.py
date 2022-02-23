def calcPrice(distance, weekend, night, airport):
    total = 0
    if airport == False:
        total = 2.90
        
        if distance <= 5:
            priceKM = 2.50
        elif distance > 5 and distance <= 20:
            priceKM = 2.20
        else:
            priceKM = 2.00

        if distance > 5 and weekend == True:
            priceKM += 0.10

        total += (distance * priceKM)
        if night == True:
            total += 2.50
    else:
        total = 78
        if distance > 50:
            total += (distance - 50) * 2

    return total

def main():
    km = int(input("Hoeveel kilometer? "))
    weekendString = input("Is het in het weekend? (y/n) ")
    nightString = input("Is het tussen 22u en 6u? (y/n) ")
    airportString = input("Ist voor de luchthaven te doen? (y/n) ")

    weekend = False
    night = False
    airport = False
    if weekendString == "y":
        weekend = True
    if nightString == "y":
        night = True
    if airportString == "y":
        airport = True

    price = calcPrice(km, weekend, night, airport)

    print(f"De totaal prijs: €{price}.")

main()