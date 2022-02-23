def pytha(side1, side2):
    hypotenusa = (side1 * side1) + (side2 * side2)
    return hypotenusa

def main():
    side1 = float(input("Lengte zijde 1? "))
    side2 = float(input("Lengte zijde 2? "))

    hypotenusa = pytha(side1, side2)

    print(f"De hypotenusa van de driehoek is: {hypotenusa}.")

main()