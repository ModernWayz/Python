# Imports
import csv
import os
import random
import pickle
import jinja2
from datetime import datetime, timedelta
from classes.log import Log
from classes.transporteur import Transporteur
from classes.velo import Velo
from classes.gebruiker import Gebruiker
from classes.station import Station

from constants import *

def getRandomLineFromFile(filepath):
    lines = open(filepath, encoding="utf-8").read().splitlines()
    random_line = random.choice(lines)
    return random_line

def generateData():
    # Initialise lists
    stations, velos, gebruikers, transporteurs = [], [], [], []

    # Create 309 Stations from csv file
    csv_file = csv.reader(open(DATA_DIR + 'velo.csv'))
    header = next(csv_file)
    if header != None:
        for row in csv_file:
            station = Station(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
            stations.append(station)

    # Create velos
    for i in range(AMOUNT_VELOS):
        velo = Velo(i)
        velos.append(velo)

    # Add velos to random slots
    for velo in velos:
        added = False
        while (added == False):
            stationKey = random.randint(0, len(stations) - 1)
            if(stations[stationKey].gebruik == 'IN_GEBRUIK'):
                if(stations[stationKey].getOccupiedSlots() < int(stations[stationKey].aantalPlaatsen)):
                    stations[stationKey].addVelo(velo)
                    added = True

    # Create random gebruikers
    for i in range(AMOUNT_GEBRUIKERS):
        gebruiker = Gebruiker(getRandomLineFromFile(DATA_DIR + 'voornamen.txt'), getRandomLineFromFile(DATA_DIR + 'achternamen.txt'))
        gebruikers.append(gebruiker)

    # Add 1 transporteur
    transporteurs.append(Transporteur(getRandomLineFromFile(DATA_DIR + 'voornamen.txt'), getRandomLineFromFile(DATA_DIR + 'achternamen.txt')))

    return stations, velos, gebruikers, transporteurs

def getFullestStation(stations):
    fullestStation = stations[0]
    for station in stations:
        if(station.getOccupiedSlots() > fullestStation.getOccupiedSlots()):
            fullestStation = station
    return fullestStation

def stationMaintenance(stations, transporteurs, logs, simulatedTime):
    # Check for almost empty and almost full stations
    for station in stations:
        if(station.gebruik == 'IN_GEBRUIK'):
            seconds = random.randint(0, 500)
            simulatedTime += timedelta(seconds = seconds)
            if(len(transporteurs[0].velos) <= 18):
                fullestStation = getFullestStation(stations)
                amount = 18 - len(transporteurs[0].velos)
                if(amount > 0):
                    logs.append(Log('ontlenen', fullestStation, transporteur = transporteurs[0], amount = amount, logtime = simulatedTime.strftime(TIME_FORMAT)))
                    transporteurs[0].velosOntlenen(fullestStation, amount)
            # Full
            if(station.getOccupiedSlots() >= int(station.aantalPlaatsen) - 5):
                logs.append(Log('ontlenen', station, transporteur = transporteurs[0], amount = round(int(station.aantalPlaatsen) / 2), logtime = simulatedTime.strftime(TIME_FORMAT)))
                transporteurs[0].velosOntlenen(station, round(int(station.aantalPlaatsen) / 2))
            # Empty
            elif(station.getOccupiedSlots() <= 5):
                logs.append(Log('inchecken', station, transporteur = transporteurs[0], amount = round(int(station.aantalPlaatsen) / 3), logtime = simulatedTime.strftime(TIME_FORMAT)))
                transporteurs[0].velosInchecken(station, round(int(station.aantalPlaatsen) / 3))

def simulateData(stations, gebruikers, transporteurs, logs, SIMULATIONS):
    # If logs exist -> continue simulating from that point in time
    try:
        simulatedTime_str = logs[-1].logtime
        simulatedTime = datetime.strptime(simulatedTime_str, TIME_FORMAT)
    except:
        simulatedTime = datetime.today()

    for i in range(SIMULATIONS):
        # Select random gebruiker and station
        gebruikerKey = random.randint(0, len(gebruikers) - 1)
        stationKeyStart = random.randint(0, len(stations) - 1)
        stationKeyStop = random.randint(0, len(stations) - 1)

        # Add to random time
        minutes = random.randint(1, 200)
        seconds = random.randint(0, 60)
        simulatedTime += timedelta(minutes = minutes, seconds = seconds)

        # Add to random time for an end time
        minutes = random.randint(1, 200)
        seconds = random.randint(0, 60)
        endTime = simulatedTime + timedelta(minutes = minutes, seconds = seconds)

        # Get velo from station or place in station
        if(gebruikers[gebruikerKey].velo == None):
            gebruikers[gebruikerKey].veloOntlenen(stations[stationKeyStart])
            # Log
            logs.append(Log('ontlenen', stations[stationKeyStart], gebruikers[gebruikerKey], gebruikers[gebruikerKey].velo, logtime = simulatedTime.strftime(TIME_FORMAT)))
            # Log
            logs.append(Log('inchecken', stations[stationKeyStart], gebruikers[gebruikerKey], gebruikers[gebruikerKey].velo, logtime = endTime.strftime(TIME_FORMAT)))
            gebruikers[gebruikerKey].veloInchecken(stations[stationKeyStop], gebruikers[gebruikerKey].velo)

        stationMaintenance(stations, transporteurs, logs, simulatedTime)

def generateHtml(stations, velos, gebruikers, logs):
    outputfile = ""
    # Sort logs by date
    logs.sort(key=lambda date: datetime.strptime(date.logtime, TIME_FORMAT))
    # Get all templates
    for page in os.listdir(TEMPLATE_DIR):
        outputfile = os.path.join(SITE_DIR, page)
        subs = jinja2.Environment(
            loader=jinja2.FileSystemLoader(TEMPLATE_DIR)
        ).get_template(page).render(velos = velos, stations = stations, gebruikers = gebruikers, logs = logs)
        # lets write the substitution to a file
        with open(outputfile, 'w') as f: f.write(subs)

def saveData(stations, velos, gebruikers, transporteurs, logs):
    with open(SAVE_DIR + 'stations.pkl', 'wb') as f:
        pickle.dump(stations, f)
    with open(SAVE_DIR + 'velos.pkl', 'wb') as f:
        pickle.dump(velos, f)
    with open(SAVE_DIR + 'gebruikers.pkl', 'wb') as f:
        pickle.dump(gebruikers, f)
    with open(SAVE_DIR + 'transporteurs.pkl', 'wb') as f:
        pickle.dump(transporteurs, f)
    with open(SAVE_DIR + 'logs.pkl', 'wb') as f:
        pickle.dump(logs, f)

def loadData():
    with open(SAVE_DIR + 'stations.pkl', 'rb') as f:
        stations = pickle.load(f)
    with open(SAVE_DIR + 'velos.pkl', 'rb') as f:
        velos = pickle.load(f)
    with open(SAVE_DIR + 'gebruikers.pkl', 'rb') as f:
        gebruikers = pickle.load(f)
    with open(SAVE_DIR + 'transporteurs.pkl', 'rb') as f:
        transporteurs = pickle.load(f)
    with open(SAVE_DIR + 'logs.pkl', 'rb') as f:
        logs = pickle.load(f)
    return stations, velos, gebruikers, transporteurs, logs