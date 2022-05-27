from bs4 import BeautifulSoup
import requests

import json

import sys

categoria = int(sys.argv[1])
pagina = sys.argv[2]

URLs = [
    {'https://www.educatolerancia.com/categoria/educacion/page/' +
        pagina},            # 0 = educacion
    {'https://www.educatolerancia.com/categoria/acoso-escolar/page/' + \
        pagina},        # 1 = acoso escolar
    {'https://www.educatolerancia.com/categoria/delitos-de-odio/page/' + \
        pagina},      # 2 = delitos de odio
    {'https://www.educatolerancia.com/categoria/discriminacion/page/' + \
        pagina},       # 3 = discriminación
    {'https://www.educatolerancia.com/categoria/discurso-del-odio/page/' + \
        pagina},    # 4 = discurso del odio
    {'https://www.educatolerancia.com/categoria/ciberodio/page/' + \
        pagina}             # 5 = ciberodio
]

listaArticulos = []


def webscraping():

    url = URLs[categoria].pop()

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Obtener los articulos
    articulos = soup.find(id='primary').find_all('article')

    for articulo in articulos:

        try:
            # ID
            id = articulo.get('id')

            # Titulo
            titulo = articulo.find('header').find('h1').find('a').text

            # Fecha
            fecha = articulo.find('time').text

            # Autor
            autor = articulo.find(class_='author').find('a').text

            # Descripcion
            descripcion = articulo.find('p').text

            # Obtener la URL
            url_articulo = articulo.find('header').find(
                'h1').find(href=True)['href']

            articulo_html = BeautifulSoup(requests.get(articulo.find('header').find(
                'h1').find(href=True)['href']).content, "html.parser")

            # URL Foto
            url_img = articulo_html.find(id='content').find('img')['src']

            # Cuerpo
            # cuerpo = str(articulo_html.find(class_='entry-content'))

            listaArticulos.append(
                {
                    "id": id,
                    "titulo": titulo,
                    "fecha": fecha,
                    "autor": autor,
                    "descripcion": descripcion,
                    "url_articulos": url_articulo,
                    "url_foto": url_img,
                    "categoria": categoria,
                    "medio": "et"
                })

        except:
            pass

    with open('noticias.json', 'w', encoding='utf-8') as f:
        json.dump(listaArticulos, f, ensure_ascii=False)


webscraping()
