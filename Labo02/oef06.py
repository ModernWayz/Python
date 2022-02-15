MONTHS_SPRING = ["maart", "april", "mei"]
MONTHS_SUMMER = ["juni", "juli", "augustus"]
MONTHS_FALL = ["september", "oktober", "november"]
MONTHS_WINTER = ["december", "januari", "februari"]

START_SPRING = 20 #maart
START_SUMMER = 21 #juni
START_FALL = 22 #september
START_WINTER = 21 #december

SEASONS = ["lente", "zomer", "herfst", "winter"]

month = input("Maand: ")
day = int(input("Dag: "))

if month in MONTHS_SPRING:
    season = SEASONS[0]
    if month == MONTHS_SPRING[0] and day < START_SPRING:
        season = SEASONS[3]

if month in MONTHS_SUMMER:
    season = SEASONS[1]
    if month == MONTHS_SUMMER[0] and day < START_SUMMER:
        season = SEASONS[0]

if month in MONTHS_FALL:
    season = SEASONS[2]
    if month == MONTHS_FALL[0] and day < START_FALL:
        season = SEASONS[1]

if month in MONTHS_WINTER:
    season = SEASONS[3]
    if month == MONTHS_WINTER[0] and day < START_WINTER:
        season = SEASONS[2]

print(f"{day} {month} valt in de {season}.")