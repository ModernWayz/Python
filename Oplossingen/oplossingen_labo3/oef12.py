##
# Oefening 12
# Gebruik de oplossingen uit de twee vorige oefeningen en schrijf een 
# programma dat een random wachtwoord genereert en het toont en test of het 
# een goed wachtwoord betreft. Tel en toon de aantal pogingen die nodig 
# waren om tot een goed wachtwoord te komen. Structureer je oplossing zo dat 
# deze oefening de functies in de vorige importeert en gebruikt.

from oef10 import willekeurig_wachtwoord
from oef11 import controleer_wachtwoord

teller = 1
wachtwoord = willekeurig_wachtwoord()
while controleer_wachtwoord(wachtwoord) == False:
    wachtwoord = willekeurig_wachtwoord()
    teller += 1

print(f"We hebben een veilig wachtwoord gevonden na {teller} keer proberen: {wachtwoord}")
