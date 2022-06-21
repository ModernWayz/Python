# Datum en tijd 
# Verschillende manieren om datum/tijd te representeren
# Bovendien zijn datum/tijd vertegenwoordiging vaak ambigu: 
# - 12/12/2022
# - Tijd: tijdzones, zomertijd
# Verschillende modules: datetime, time, calendar, dateutil


# De datetime module gebruiken
# ----------------------------

# 4 object klassen, elk met verschillende methods
# date voor years, months en days
# time voor hours, minutes, seconds en fractions
# datetime voor datum en tijd samen
# timedelta voor datum en/of tijd intervallen

#date
from datetime import date
gisteren = date(2022, 5, 3)
print(gisteren) # 2022-05-03
print(gisteren.day) # 3
print(gisteren.month) # 5
print(gisteren.year) # 2022
print(gisteren.isoformat()) # 2022-05-05 jaar, maand, dag

vandaag = date.today()
print(vandaag) # 2022-05-04

# range voor date loopt van date.min (year=1, month=1, day=1) tot date.max (year=9999, month=12, day=31).

#timedelta
from datetime import timedelta
een_dag = timedelta(days=1)
morgen = vandaag + een_dag
print(morgen)
print(vandaag + 12*een_dag) # 2022-05-16
print(vandaag - een_dag) # 2022-05-03

#time
from datetime import time
middag = time(12, 0, 0)
print(middag)
print(middag.hour) # 12
print(middag.minute) # 0
print(middag.second) # 0

#datetime
from datetime import datetime
willekeurige_dag = datetime(2021, 5, 6, 13, 30, 40, 230)
print(willekeurige_dag)
# The datetime object also has an isoformat() method:
print(willekeurige_dag.isoformat())
# datetime has a now() method to return the current date and time:
nu = datetime.now()
print(nu)
print(nu.year)
print(nu.month)
print(nu.day)
print(nu.hour)
print(nu.minute)
print(nu.second)
print(nu.microsecond)

# Met combine() kan je een date en een time object "combineren" tot een datetime 
from datetime import datetime, time, date
middag = time(12)
vandaag = date.today()
middag_vandaag = datetime.combine(vandaag, middag)
print(middag_vandaag) # 2022-05-05 12:00:00

# Je kan een datetime uit elkaar trekken tot een date en een time met de date() en time() methods
print(middag_vandaag.date()) # 2022-05-05
print(middag_vandaag.time()) # 12:00:00


# De time module gebruiken
# ------------------------

# Een manier om een absolute tijd weer te geven: aantal seconden tellen sinds een bepaald startpunt. Epoch-tijd = sinds 1 januari 1970.
# time() functie geeft tijd weer als een epoch-waarde
# Epoch-waarden zijn heel bruikbaar bij uitwisseling van data tussen heterogene systemen

import time
nu = time.time()
print(nu) # bvb 1651746195.851634

# Een epoch-waarde omzetten naar een string doe je met ctime()
print(time.ctime(nu)) # bvb Thu May  5 12:25:02 2022

# Soms wil je kunnen omzetten naar dagen, uren enz. Time geeft je hiervoor struct_time objecten
# localtime() geeft de tijd in jouw tijdzone, en gmtime() geeft het in UTC (te prefereren)

print(time.localtime(nu))
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=5, tm_hour=12, tm_min=29, tm_sec=49, tm_wday=3, tm_yday=125, tm_isdst=1)

print(time.gmtime(nu))
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=5, tm_hour=10, tm_min=29, tm_sec=49, tm_wday=3, tm_yday=125, tm_isdst=0)

nu = time.gmtime() # huidige tijd wordt genomen!
print(nu)
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=5, tm_hour=10, tm_min=35, tm_sec=13, tm_wday=3, tm_yday=125, tm_isdst=0)

# Als je niet alle tm_-waarden wenst te gebruiken kan je ook via indexgetal:
print(nu[0]) # 2022

# mktime() zet een struct_time object om naar epoch-waarde
print(time.mktime(nu)) # 1651743510.0


# Datum en tijd lezen en schrijven
# --------------------------------

# We zagen reeds isoformat() en ctime() om te schrijven en converteren
# Je kan ook datum en tijd converteren met strftime()
# strftime is een method in de datetime, date en time objecten en een functie in de time module
# strftime gebruikt format-string om de output vorm te geven

# %Y - jaar - 1900-
# %m - maand - 01-12
# %B - naam maand - January
# %b - maand afk - Jan
# %d - dag van de maand - 01-31
# %A - dag vd week - Monday
# a - weekdag afk - Mon
# %H - uur (24u) - 00-23
# %I - uur (12u) - 01-12
# %p - AM/PM - AM, PM
# %M - minuten - 00-59
# %S - seconden - 00-59

import time
vorm = "%A, %B %d, %Y, %I:%M:%S%p"
tijd = time.localtime()
print(tijd) # time.struct_time(tm_year=2022, tm_mon=5, tm_mday=5, tm_hour=12, tm_min=49, tm_sec=12, tm_wday=3, tm_yday=125, tm_isdst=1)
print(time.strftime(vorm, tijd)) # Thursday, May 05, 2022, 12:49:12PM

from datetime import date
dag = date(2022, 5, 4)
vorm = "%A, %B %d, %Y, %I:%M:%S%p"
print(dag.strftime(vorm)) # tijd default op middernacht
# Wednesday, May 04, 2022, 12:00:00AM

from datetime import time
vorm = "%A, %B %d, %Y, %I:%M:%S%p"
tijd = time(11, 43)
print(tijd.strftime(vorm)) # enkel tijdsdelen geconverteerd
# Monday, January 01, 1900, 11:43:00AM

# Andersom kan je een string omzetten naar een datum/tijd met strptime() met gebruik van dezelfde format-string
import time
vorm = "%Y-%m-%d"
print(time.strptime("2022-03-30", vorm))
# time.struct_time(tm_year=2022, tm_mon=3, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=89, tm_isdst=-1)

# Namen zoals dag van de week en maanden zijn specifiek voor de locale-internationalisatie settings voor je besturingssysteem
# Je kan de locale aanpassen met de setlocale() functie
# Deze functie neemt 2 argumenten: locale.LC_TIME voor datums en tijd. De 2de is een string die taal combineert met een afkorting voor het land: 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', 'nl_be'

import locale
from datetime import date
een_datum = date(2022, 5, 5)
locale.setlocale(locale.LC_TIME, "nl_be")
print(een_datum.strftime("%A %d %B %Y"))
# donderdag 05 mei 2022


# BONUS: schrikkeljaar
# -------------------
import calendar
print(calendar.isleap(2024))