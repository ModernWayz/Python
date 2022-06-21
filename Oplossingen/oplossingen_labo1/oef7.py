## Oefening 7: samengestelde rente
# Beeld je in dat je net een nieuwe bankrekening hebt geopend die je 1,
# 2% rente per jaar geeft. Deze rente wordt uitbetaald op het einde van 
# het jaar en toegevoegd aan je bankrekening. Schrijf een programma dat 
# begint met het lezen van het bedrag dat je bij het begin van het jaar 
# op je rekening hebt gezet. Het programma rekent dan uit (en toont) de 
# stand van de rekening na 1, 2 en 3 jaar. Toon elk bedrag met wat 
# uitleg en afgerond tot op 2 cijfers na de komma.

startbedrag = float(input("Geef het startbedrag (in eur) dat je op je bankrekening wil zetten: ")) 
JAARLIJKSE_INTRESTVOET = 1.2
bedrag_na_een_jaar = (startbedrag * (100 + 1.2))/100
bedrag_na_twee_jaar = (bedrag_na_een_jaar * (100 + 1.2))/100
bedrag_na_drie_jaar = (bedrag_na_twee_jaar * (100 + 1.2))/100
print(f"Stand van de rekening na 1 jaar: {round(bedrag_na_een_jaar,2)}eur.")
print(f"Stand van de rekening na 2 jaar: {round(bedrag_na_twee_jaar,2)}eur.")
print(f"Stand van de rekening na 3 jaar: {round(bedrag_na_drie_jaar,2)}eur.")