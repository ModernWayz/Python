from oef10 import generatePassword
from oef11 import verifyPassword

def main():
    tries = 1
    password = generatePassword()
    while not verifyPassword(password):
        password = generatePassword()
        tries += 1
    
    print(f"Wachtwoord: {password}")
    print(f"Aantal pogingen: {tries}")

main()