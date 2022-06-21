'''Deze module bevat alle functionaliteit nodig voor het aanmaken van de statische website'''

import os
from pathlib import Path
import shutil
import input
import yaml
from jinja2 import Environment, PackageLoader, select_autoescape
from bs4 import BeautifulSoup as bs

def maak_site(bestemming, type, bestanden_dict):
    ''' Deze functie neemt de bestemmingsfolder, type (posts of pages) en de bestanden_dict als argumenten. Ze neemt zowel de leiding over het aanmaken van de structuur als van de bestanden zelf'''
    bestaan_locatie_checken(bestemming)
    for naam, content in bestanden_dict.items():
        if "permalink" in content[0].keys():
            foldernaam = content[0]["permalink"] 
        else:
            foldernaam = naam[0:naam.rfind(".")]
        if "home" in content[0].keys():
            homepage = True
        else: 
            homepage = False  
        if "layout" in content[0].keys():
            template = content[0]["layout"]
        else:
            if type == "posts":
                template = "posts"
            else:
                template = "pages"    
        structuur_aanmaken(bestemming, type, foldernaam, homepage)
        bestand_aanmaken(bestemming, type, foldernaam, content, homepage, template)

def bestand_aanmaken(bestemming, type, foldernaam, content, homepage, template):
    ''' Deze functie creëert het eigenlijke bestand. We strippen en parsen de front matter, parsen de markdown, en voeren de content aan Jinja met alle parameters '''
    if type == "posts":   
        bestand = f"{bestemming}/posts/{foldernaam}/index.html"
    else: 
        if homepage:
            bestand = f"{bestemming}/index.html"
        else: 
            bestand = f"{bestemming}/{foldernaam}/index.html"
    with open(bestand,"w") as bestand:
        inhoud_bestand = templates_toevoegen(content, template)
        inhoud_bestand = opschonen_html(inhoud_bestand)
        bestand.write(inhoud_bestand) 

def opschonen_html(content): # met behulp van BeautifulSoup
    content_bs = bs(content, "html.parser")                
    cleane_content_bs = content_bs.prettify() 
    return cleane_content_bs

def templates_toevoegen(content, template): # met behulp van Jinja2
    env = Environment(
      loader=PackageLoader('ssg', 'templates'),
      autoescape=select_autoescape([])
    )
    jinja_template = env.get_template(f"{template}.html")
    return_waarde = jinja_template.render(navigatie= input.navigatie, pagina = content[1], data = content[0], posts = input.blog)
    return return_waarde

def bestaan_locatie_checken(locatie):
    pad = Path(locatie)
    try:
        pad.mkdir()
    except FileExistsError as exc: 
        pass
        #print(exc)

def structuur_aanmaken(locatie, type, naam, homepage):
    if type == "posts":  
        bestaan_locatie_checken(f"{locatie}/posts")   
        pad = Path(f"{locatie}/posts/{naam}/")
    else: 
        pad = Path(f"{locatie}/{naam}/")
    try:
        if homepage == False:
            pad.mkdir()
    except FileExistsError as exc: 
        pass
        #print(exc)

def verwijder_site(bestemming): 
    try:
        shutil.rmtree(f"{bestemming}/")
    except:
        pass

def kopieer_assets(oorsprong, bestemming):
    shutil.copytree(f"{oorsprong}/", f"{bestemming}/{oorsprong}/")
    
    