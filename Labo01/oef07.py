bedrag = float(input("Bedrag begin van jaar? €"))

PERCENTAGE = 0.012

# Bereken bedrag & rente
rente = bedrag * PERCENTAGE
bedrag = bedrag + rente
print(f"Stand van rekening na 1 jaar: €{round(bedrag, 2)}")

# Bereken bedrag & rente
rente = bedrag * PERCENTAGE
bedrag = bedrag + rente
print(f"Stand van rekening na 2 jaar: €{round(bedrag, 2)}")

# Bereken bedrag & rente
rente = bedrag * PERCENTAGE
bedrag = bedrag + rente
print(f"Stand van rekening na 3 jaar: €{round(bedrag, 2)}")