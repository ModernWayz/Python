'''Deze module bevat alle functionaliteit nodig voor het inlezen van de bestanden en de informatie die ze bevatten'''

import os
import yaml
import mistune
from datetime import datetime

def initialiseren():
    global pages
    global posts
    global navigatie
    global blog
    pages = inlezen_bestanden("pages")
    posts = inlezen_bestanden("posts")
    navigatie = genereer_navigatie()
    blog = genereer_blog_landing(5)
    print(blog)

def genereer_blog_landing(aantal_tonen):
    return_list = []
    for content in posts.values():
        post_element_list = []
        if "date" in content[0].keys():
            post_element_list.append(content[0]["date"])
        permalink = content[0]["permalink"]
        post_element_list.append(f"/posts/{permalink}")
        post_element_list.append(content[0]["title"])
        post_element_list.append(content[0]["description"])
        return_list.append(post_element_list)
    return_list.sort(key = lambda date: datetime.strptime(date[0], '%Y-%m-%d'), reverse=True)
    return_list = return_list[:aantal_tonen]
    return return_list

def genereer_navigatie():
    return_list = []
    for naam, content in pages.items():
        if "navigation" in content[0].keys():
            navigatie_element = []
            navigatie_element.append(content[0]["navigation"]["name"])
            if "home" in content[0].keys():
                navigatie_element.append(f"/")
            else:
                foldernaam = naam[0:naam.rfind(".")]
                navigatie_element.append(f"/{foldernaam}")
            navigatie_element.append(content[0]["navigation"]["order"])
            return_list.append(navigatie_element)
    return_list.sort(key=lambda x:x[2])
    #print(return_list)
    # Vorm: [['Home', 'home', 1], ['Over', 'over', 2], ['Contact', 'contact', 3]]
    return return_list

def inlezen_bestanden(folder):
    return_dict = {}
    for dirpath, dirnames, files in os.walk(folder):
        for bestandsnaam in files:
            return_dict[bestandsnaam] = inlezen_content(f"{folder}/{bestandsnaam}")
    return return_dict

def inlezen_content(bestand):
    with open(bestand) as bestand:
        content = bestand.read()
        if content.find("---") != -1:
            yaml_dict = yaml.load(content[4:content.rfind("---")-1], Loader=yaml.FullLoader)
            markdown_content = mistune.html(content[content.rfind("---")+3:-1])
        else:
            yaml_dict = {}
            markdown_content = mistune.html(content)
        return [yaml_dict, markdown_content]