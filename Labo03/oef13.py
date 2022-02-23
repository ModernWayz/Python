import math

def reduceFraction(numerator, denominator):
    # Grootste Gemene Deler = ggd
    divisor = math.gcd(numerator, denominator)
    # Delen door ggd
    numerator /= divisor
    denominator /= divisor
    # Done
    return numerator, denominator

def main():
    print(reduceFraction(6, 27))

# Prevent main conflict on import
if __name__ == "__main__":
    main()