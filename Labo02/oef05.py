MONTHS_31 = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
MONTHS_30 = ["april", "juni", "september", "november"]

month = input("Naam van de maand? ")

if month == "februari":
    days = "28 of 29"
elif month in MONTHS_30:
    days = 30
elif month in MONTHS_31:
    days = 31
else:
    days = "NA"

print(f"{month} heeft {days} dagen.")