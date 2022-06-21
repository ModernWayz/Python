##
# Oefening 6
# Het jaar kent 4 seizoenen. De weerkundige overgang varieert elk jaar
# een beetje, maar wij gebruiken hier volgende data: lente (vanaf 20
# maart), zomer (vanaf 21 juni), herfst (vanaf 22 september), winter
# (vanaf 21 december). Schrijf een programma dat een maand en een dag
# vraagt aan de gebruiker. De gebruiker voert de naam van maand in als
# string en daarna de dag van de maand als integer. Je programma geeft
# dan het seizoen terug dat bij deze ingegeven datum hoort.

dag = int(input("Geef het getal van de dag: "))
maand = input("Geef de naam van de maand: ")
if maand == "januari" or maand == "februari":
    seizoen = "winter"
elif maand == "maart":
    if dag < 20:
        seizoen = "winter"
    else:
        seizoen = "lente"
elif maand == "april" or maand == "mei":
    seizoen = "lente"
elif maand == "juni":
    if dag < 21:
        seizoen = "lente"
    else:
        seizoen = "zomer"
elif maand == "juli" or maand == "augustus":
    seizoen = "zomer"
elif maand == "september":
    if dag < 22:
        seizoen = "zomer"
    else:
        seizoen = "herfst"
elif maand == "october" or maand == "november":
    seizoen = "herfst"
elif maand == "december":
    if dag < 21:
        seizoen = "herfst"
    else:
        seizoen = "winter"

print(f"{dag} {maand} valt in de {seizoen}.")