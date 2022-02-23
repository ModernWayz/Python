def calcDays(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        # Check leap year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        return 28
    if month in {4, 6, 9, 11}:
        return 30
    return False

def main():
    month = int(input("Maand? (getal): "))
    year = int(input("Jaar?: "))

    days = calcDays(month, year)

    print(f"Aantal dagen in geselecteerde maand: {days}")

# Prevent main conflict on import
if __name__ == "__main__":
    main()