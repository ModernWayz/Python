## Oefening 5: # statiegeld berekenen
# Je schrijft een programma dat berekent hoeveel statiegeld moet worden 
# uitbetaald aan iemand die flessen komt inleveren. Er kunnen kleine 
# flesjes worden teruggegeven en grote flessen. De kleine leveren 0,
# 12eur statiegeld op, de grote 0,25eur. Je maakt van deze waarden 
# constanten. Het programma vraagt hoeveel kleine en grote flessen 
# worden ingeleverd en berekent dan hoeveel de gebruiker zal ontvangen. 
# Je werkt met floats en rondt het eindgetal af tot op 2 cijfers na de 
# komma

STATIEGELD_KLEIN = 0.12
STATIEGELD_GROOT = 0.25
aantal_kleine_flessen = int(input("Hoeveel kleine flessen worden ingeleverd? "))
aantal_grote_flessen = int(input("Hoeveel grote flessen worden ingeleverd? "))
teruggave = aantal_kleine_flessen * STATIEGELD_KLEIN + aantal_grote_flessen * STATIEGELD_GROOT
print(f"De totale teruggave bedraagt {round(teruggave,2)}eur.")
