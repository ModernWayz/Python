def is_priem(number):
    priem = False

    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                priem = False
                break
        else:
            priem = True
    return priem

def main():
    number = int(input("Geef een getal: "))
    if is_priem(number):
        print(f"{number} is een priemgetal.")
    else:
        print(f"{number} is geen priemgetal.")

# Prevent main conflict on import
if __name__ == "__main__":
    main()