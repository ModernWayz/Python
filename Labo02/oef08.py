year = int(input("Geef een jaar: "))
LEAP_YEAR = False

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    LEAP_YEAR = True

if LEAP_YEAR:
    print(f"{year} is een schrikkeljaar.")
else:
    print(f"{year} is geen schrikkeljaar.")