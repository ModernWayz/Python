''' Deze module bundelt de functies die server-checks faciliteren en specifieke checks uitvoeren '''

import platform
import subprocess
import data
from datetime import datetime

def toevoegen(type, check_parameters):
    ''' Deze functie faciliteert de aanmaak van een check in het systeem. Ze neemt een type check, een list met check_parameters en de checks_list als parameters'''
    data.checks_list.append([type, check_parameters])
    data.schrijven_bestand("checks.json",data.checks_list)

def verwijderen(index_getal):
    ''' Deze functie faciliteert het verwijderen van een check uit het systeem. Ze neemt een index-getal en de checks_list als parameters'''
    del data.checks_list[int(index_getal)]
    data.schrijven_bestand("checks.json",data.checks_list)

def oplijsten():
    ''' Deze functie verzorgt het oplijsten van de checks die in het systeem zijn ingebracht. Ze neemt de checks_list als parameter en geeft een string terug die de lijst in gebruiksvriendelijke vorm weergeeft '''
    return data.checks_list

def uitvoeren():
    ''' Deze functie zorgt voor het effectief uitvoeren van de checks. Na uitvoeren van alle checks in de checks_list wordt het resultaat van de check gelogd naar de logs_list. Ze neemt de checks_list en de logs_list als parameters. '''
    for check in data.checks_list:
        if check[0] == "ping":
            resultaat = ping(check[1][0], check[1][1])
            datum_tijd = datetime.now()
            datum_tijd_clean = datum_tijd.strftime("%Y-%m-%d %X")
            datum = datum_tijd.strftime("%d-%m-%Y")
            tijd = datum_tijd.strftime("%X")
            check_resultaat = [str(datum_tijd_clean), str(datum), str(tijd), "ping", check[1][0], resultaat]
            data.logs_list.append(check_resultaat)
    data.schrijven_bestand("logs.json",data.logs_list)
    data.schrijven_naar_html()

def ping(host_name, aantal_frames):
    ''' Deze functie neemt een hostname en het aantal frames dat moet gestuurd worden. De functie geeft een list terug met volgende elementen:
        - Het percentage aan packets dat verloren gegaan is
        - Min round-trip tijd in ms
        - Avg round-trip tijd in ms
        - Max round-trip tijd in ms
        - Stddev round-trip tijd in ms'''
    try:
        parameter = '-n' if platform.system().lower()=='windows' else '-c'
        response = subprocess.check_output(
            ['ping', parameter, str(aantal_frames), host_name],
            stderr=subprocess.STDOUT,  # get all output
            universal_newlines=True  # return string not bytes
        )
    except subprocess.CalledProcessError:
        response = [None]
        return response
    else:
        if platform.system().lower()=='windows':
            packets_lost = response[response.find("Lost = ")+10:response.find("loss")-2]
            minimum = response[response.find("Minimum = ")+10:response.find("ms, Maximum")]
            average = response[response.find("Average = ")+10:response.rfind("ms")]
            maximum = response[response.find("Maximum = ")+10:response.find("ms, Average")]
            stddev = '-'
            mijn_list = []
            mijn_list.append(packets_lost)
            mijn_list.append(minimum)
            mijn_list.append(average)
            mijn_list.append(maximum)
            mijn_list.append(stddev)
            return mijn_list
        else: 
            packets_lost = response[response.find("packets received")+18:response.find("packet loss")-2]
            round_trip = response[response.find("stddev")+9:response.rfind("ms")-1]
            return_string = packets_lost + "/" + round_trip
            return return_string.split("/")
