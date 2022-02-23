from oef08 import is_priem

def volgend_priemgetal(number):
    number += 1
    while not is_priem(number):
        number += 1
    return number

def main():
    number = int(input("Geef een getal: "))
    newPriem = volgend_priemgetal(number)
    print(f"Het eerstvolgende priem getal is: {newPriem}.")

main()