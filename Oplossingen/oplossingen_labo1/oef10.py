## Oefening 10: Celsius naar Fahrenheit en Kelvin
# Schrijf een programma dat begint met het opvragen van een temperatuur 
# in Celsius. Vervolgens toont je programma deze temperatuur in graden 
# Fahrenheit en Kelvin. De berekeningen die je hiervoor nodig hebt vind 
# je gemakkelijk op het internet.

graden_celsius = int(input("Geef de huidige temperatuur in graden Celsius: "))
graden_fahrenheit = (graden_celsius * 1.8) + 32
graden_kelvin = graden_celsius + 273.15
print(f"{graden_celsius} graden Celsius stemt overeen met {graden_fahrenheit} graden Fahrenheit en {graden_kelvin} graden Kelvin")
