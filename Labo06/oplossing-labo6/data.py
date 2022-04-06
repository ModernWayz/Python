''' Deze module bundelt de functies die lezen en schrijven naar bestanden en loggen naar html-bestanden '''

import json
from datetime import datetime

def initialisatie():
    global checks_list
    global logs_list
    checks_list = lezen_bestand("checks.json")
    logs_list = lezen_bestand("logs.json")

def lezen_bestand(naam):
    ''' Deze functie leest een json-object van een bestand. Ze neemt een bestand als parameter en geeft een list terug '''
    try:
        with open(naam, "r") as bestand:
            data_list = json.load(bestand)
        return data_list
    except FileNotFoundError:
        with open(naam, "w") as bestand:
            json.dump([],bestand)
        return []

def schrijven_bestand(naam, data_list):
    ''' Deze functie schrijft een json-object naar een bestand. Ze neemt een bestand en een list als parameters'''
    with open(naam,"w") as bestand:
        json.dump(data_list,bestand)

def schrijven_naar_html():
    ''' Deze functie schrijft list-data naar een html-bestand. Ze neemt een list, een html-template-bestand, en een html-output-bestand als parameters'''
    with open("template.html", "r") as input_bestand:
        template_string = input_bestand.read()
    schrijfpositie = template_string.find("output")+8
    begin = template_string[0:schrijfpositie]
    einde = template_string[schrijfpositie:-1]
    logging = ""
    logs_list_kopie = logs_list[:]
    logs_list_kopie.sort(key = lambda date: datetime.strptime(date[0], '%Y-%m-%d %X'), reverse=True)
    for event in logs_list_kopie:
        if event[5][0] == None:
            succes = 0
            rapportering = f"Geen antwoord / offline"
        else:
            succes = int(100 - float(event[5][0]))
            rapportering = f"Min: {event[5][1]}ms | Avg: {event[5][2]}ms |  Max: {event[5][3]}ms"
        if succes == 100:
            boodschap = f"<strong class='ok'>{event[3]}</strong>"
        else: 
            boodschap = f"<strong class='not_ok'>{event[3]}</strong>"
        
        event_string = f"{boodschap} <span>{event[4]}</span> {succes}% OK | {rapportering} <time datetime='{event[1]} {event[2]}'>{event[1]} {event[2]}</time>"
        
        logging += "<li>" + event_string + "</li>"
    with open("logging.html", "w") as output_bestand:
        output_bestand.write(begin + logging + einde)
