from oef14 import calcDays

def showMagicDates(START_YEAR, END_YEAR):
    year = START_YEAR
    while year <= END_YEAR:
        month = 1
        while month <= 12:
            day = 1
            while day <= calcDays(month, year):
                # Convert year to array/list whatever of integers
                arrayYear = [int(i) for i in str(year)]
                # Snap the year in half, thanos style
                thanosSnappedYear = int(str(arrayYear[2]) + str(arrayYear[3]))
                # Magic date formula
                if day * month == thanosSnappedYear:
                    print(f"{day}/{month}/{year}")
                day += 1
            month += 1
        year += 1

def main():
    showMagicDates(1901, 2000)

# Prevent main conflict on import
if __name__ == "__main__":
    main()