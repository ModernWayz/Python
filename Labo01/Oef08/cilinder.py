import math

straal = float(input("Straal? "))
hoogte = float(input("Hoogte? "))

volume = round(math.pi * (straal * straal) * hoogte, 1)

print(f"Het volume van de cilinder: {volume} cm3")