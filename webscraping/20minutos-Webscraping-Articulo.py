from bs4 import BeautifulSoup
import requests

import sys

import json

url_articulo = sys.argv[1]

listaArticulos = []

def webscraping():

    url = url_articulo

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Cuerpo
    cuerpo = str(soup.find(class_='article-text'))
    cuerpo = cuerpo.replace('\n', '')
    
    with open('cuerpo.txt', 'w', encoding='utf-8') as f:
        json.dump(cuerpo, f, ensure_ascii=False)


webscraping()
