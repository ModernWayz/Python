def verifyPassword(password):
    hasLower = False
    hasUpper = False
    hasDigit = False

    if len(password) >= 8:
        for i in password:
            # Check for lower char
            if i.islower():
                hasLower = True
            # Check for upper char
            if i.isupper():
                hasUpper = True
            # Check for digit char
            if i.isdigit():
                hasDigit = True
        # If everything passed checks -> true
        if hasLower == True and hasUpper == True and hasDigit == True:
            return True
    else:
        return False

def main():
    password = input("Password: ")
    if verifyPassword(password):
        print("Het wachtwoord voldoet aan de normen.")
    else:
        print("Het wachtwoord is te shit.")

# Prevent main conflict on import
if __name__ == "__main__":
    main()