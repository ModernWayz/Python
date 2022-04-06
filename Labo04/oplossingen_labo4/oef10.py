##
# Oefening 10
# In deze oefening simuleer je 1000 worpen van twee dobbelstenen. Je 
# schrijft een functie die geen parameters aanneemt en de worp van twee 
# dobbelstenen simuleert. Deze functie geeft het totaal van de worpen 
# terug.  Schrijf een programma dat deze functie 1000 keer uitvoert.  Het 
# programma telt het aantal keer dat een bepaalde waarde voorkomt. Je 
# gebruikt een dictionary om de data bij te houden. Na afloop toont het 
# programma een tabel die de data samenvat.

from random import randrange

AANTAL_WORPEN = 1000
AANTAL_VLAKKEN = 6
def dubbele_worp():
    worp1 = randrange(1, AANTAL_VLAKKEN + 1)
    worp2 = randrange(1, AANTAL_VLAKKEN + 1)
    return worp1 + worp2

def main():
    statistisch_verwacht = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, \
              7: 6/36, 8: 5/36, 9: 4/36,  10: 3/36, \
              11: 2/36, 12: 1/36}
    uitslagen_worpen = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, \
            8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for _ in range(AANTAL_WORPEN): # _ omdat we in deze loop geen teller nodig hebben
        t = dubbele_worp()
        uitslagen_worpen[t] = uitslagen_worpen[t] + 1
    
    print("Totaal\tGesimuleerd\tVerwacht")
    print("      \tPercentage  \tPercentage")
    for teller in sorted(uitslagen_worpen.keys()):
        print(f"{teller}\t{round(uitslagen_worpen[teller] / AANTAL_WORPEN * 100,2)}\t\t{round(statistisch_verwacht[teller] * 100,2)}")

if __name__ == "__main__":
    main()