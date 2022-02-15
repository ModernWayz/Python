print("Temperatuur omzetten")
celsius = float(input("Wat is de temperatuur? (in °C) "))

# Convert temperatures
fahrenheit = round(celsius * (9/5) + 32)
kelvin = round(celsius + 273.15)

print(f"De temperatuur is in Fahrenheit: {fahrenheit}°F")
print(f"De temperatuur is in Kelvin: {kelvin}°K")