import random

def generatePassword():
    length = random.randint(7, 10)
    password = ""
    for i in range(length):
        randomChar = random.randint(33, 126)
        password += chr(randomChar)
    return password

def main():
    print(generatePassword())

# Prevent main conflict on import
if __name__ == "__main__":
    main()