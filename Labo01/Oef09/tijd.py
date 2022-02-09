# Set seconds
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

print("Tijd omzetten naar seconden")
dagen = float(input("Aantal dagen? "))
uren = float(input("Aantal uren? "))
minuten = float(input("Aantal minuten? "))
seconden = float(input("Aantal seconden? "))

totaal = 0
totaal += dagen * SECONDS_IN_DAY
totaal += uren * SECONDS_IN_HOUR
totaal += minuten * SECONDS_IN_MINUTE
totaal += seconden

print(f"De opgegeven tijd is in totaal: {round(totaal)} seconden.")