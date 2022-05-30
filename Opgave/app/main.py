# Imports
import csv
from os import path
import os
import random
import sys
from datetime import datetime
from classes.log import Log

from constants import *
from functions import *

def main():
    # Initialise logs
    logs = []
    # Check if system argument is given
    if len(sys.argv) > 1:
        if sys.argv[1] == "-s":
            # Check if saves exist -> load or generate
            if(path.exists(SAVE_DIR + 'stations.pkl')):
                stations, velos, gebruikers, transporteurs, logs = loadData()
            else:
                stations, velos, gebruikers, transporteurs = generateData()
            # Check for additional parameter
            try:
                try:
                    simulations = int(sys.argv[2])
                except:
                    print('Je moet een geldig getal opgeven voor het aantal simulaties.')
            except:
                try:
                    simulations = int(input('\nAantal simulaties: '))
                except:
                    print('Je moet een geldig getal opgeven voor het aantal simulaties.')
                    sys.exit()
            print('Verplaatsingen aan het simuleren...')
            simulateData(stations, gebruikers, transporteurs, logs, simulations)
            print(simulations, 'verplaatsingen gesimuleerd!\n')
    else:
        # Interface menu intro
        if(path.exists(SAVE_DIR + 'stations.pkl')):
            print('\nWelkom terug bij Velo Antwerpen!\n\nWil je opnieuw beginnen of verder gaan met de opgeslagen data?')
            print('1. Opnieuw beginnen')
            print('2. Verder gaan')
            try:
                answer_save = int(input('Keuze: '))
                if(answer_save == 1):
                    print('\nNieuwe data genereren...')
                    stations, velos, gebruikers, transporteurs = generateData()
                    saveData(stations, velos, gebruikers, transporteurs, logs)
                    print('Nieuwe data is gegenereerd en opgeslagen!\n')
                else:
                    stations, velos, gebruikers, transporteurs, logs = loadData()
                    print('Data is geladen!\n')
            except:
                stations, velos, gebruikers, transporteurs, logs = loadData()
                print('Data is geladen!\n')
        else:
            print('\nWelkom bij Velo Antwerpen!\n')
            print('Nieuwe data genereren...')
            stations, velos, gebruikers, transporteurs = generateData()
            saveData(stations, velos, gebruikers, transporteurs, logs)
            print('Nieuwe data is gegenereerd en opgeslagen!\n')

    # Interface menu
    stopped = False
    while(stopped == False):
        print('Wat wil je doen?')
        print('1. Manuele acties')
        print('2. Simulatiemodus')
        print('3. HTML genereren')
        print('4. Applicatie stoppen en opslaan')
        try:
            answer1 = int(input('Keuze: '))
            if(answer1 == 1):
                print('\nWelke actie wil je ondernemen?')
                print('0. Terug')
                print('1. Fiets ontlenen')
                print('2. Fiets inchecken')
                print('3. Station maintenance')
                try:
                    answer_action = int(input('Keuze: '))
                    if(answer_action == 0):
                        continue
                    elif(answer_action == 1):
                        if(gebruikers[0].velo == None):
                            randomStationKey = random.randint(0, len(stations) - 1)
                            gebruikers[0].veloOntlenen(stations[randomStationKey])
                            logs.append(Log('ontlenen', stations[randomStationKey], gebruikers[0], gebruikers[0].velo, logtime = datetime.today().strftime(TIME_FORMAT)))
                            print('\nJe hebt velo #' + str(gebruikers[0].velo.id) + ' ontleend van station #' + str(stations[randomStationKey].objectId) + '\n')
                        else:
                            print('\nJe hebt al een velo in je bezit!\n')
                    elif(answer_action == 2):
                        if(gebruikers[0].velo == None):
                            print('\nJe hebt geen velo in je bezit!\n')
                        else:
                            randomStationKey = random.randint(0, len(stations) - 1)
                            logs.append(Log('inchecken', stations[randomStationKey], gebruikers[0], gebruikers[0].velo, logtime = datetime.today().strftime(TIME_FORMAT)))
                            print('\nJe hebt velo #' + str(gebruikers[0].velo.id) + ' ingecheckt bij station #' + str(stations[randomStationKey].objectId) + '\n')
                            gebruikers[0].veloInchecken(stations[randomStationKey], gebruikers[0].velo)
                    elif(answer_action == 3):
                        stationMaintenance(stations, transporteurs, logs, datetime.today())
                        print('\nDe stations zijn bijgewerkt.\n')
                    else:
                        print('\nOptie ' + str(answer_action) + ' bestaat niet, probeer nogmaals.\n')
                except:
                    print('\nFoutieve input, probeer nogmaals\n')
            elif(answer1 == 2):
                simulations = int(input('\nAantal simulaties: '))
                print('Verplaatsingen aan het simuleren...')
                simulateData(stations, gebruikers, transporteurs, logs, simulations)
                print(simulations,'verplaatsingen gesimuleerd!\n')
            elif(answer1 == 3):
                print('\nHTML paginas aan het genereren...')
                generateHtml(stations, velos, gebruikers, logs)
                print('HTML paginas gegenereerd!\n')
            elif(answer1 == 4):
                stopped = True
                print('\nApplicatie aan het opslaan...')
                saveData(stations, velos, gebruikers, transporteurs, logs)
                print('Applicatie is opgeslaan!')
                print('Applicatie is gestopt.\n')
            else:
                print('\nOptie ' + str(answer1) + ' bestaat niet, probeer nogmaals.\n')
        except:
            print('\nFoutieve input, probeer nogmaals\n')

if __name__ == "__main__":
    main()