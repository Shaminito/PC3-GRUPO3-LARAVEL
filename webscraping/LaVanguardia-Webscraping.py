from bs4 import BeautifulSoup
import requests

import json

import sys

categoria = int(sys.argv[1])

URLs = [
    {'https://stories.lavanguardia.com/search?q=Educacion'},            # 0 = educacion
    {'https://stories.lavanguardia.com/search?q=Acoso+escolar'},        # 1 = acoso escolar
    {'https://stories.lavanguardia.com/search?q=Delitos+de+odio'},      # 2 = delitos de odio
    {'https://stories.lavanguardia.com/search?q=Discriminacion'},       # 3 = discriminación
    {'https://stories.lavanguardia.com/search?q=Discurso+de+odio'},     # 4 = discurso del odio
    {'https://stories.lavanguardia.com/search?q=Ciberodio'}             # 5 = ciberodio
]

listaArticulos = []


def webscraping():

    url = URLs[categoria].pop()

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    articulos = soup.find(id='results').find_all('article')
    # print(articulos)

    for articulo in articulos:

        try:
            # Titulo
            titulo = articulo.find('h2').find('a').text

            # Fecha
            fecha = articulo.find(class_='date').text

            # Imagen
            url_img = ''
            if (articulo.find('img') is not None):
                url_img = articulo.find('img')['data-src']

            # Autor
            autor = ''
            if (articulo.find(class_='author') is not None):
                autor = articulo.find(class_='author').text

            # Descripcion
            descripcion = ''
            if (articulo.find(class_='description') is not None):
                descripcion = articulo.find(class_='description').text

            # Obtener la URL
            url_articulo = ''
            if(articulo.find('h2').find('a') is not None):
                url_articulo = articulo.find('h2').find(href=True)['href']

            # articulo_html = BeautifulSoup(requests.get(
            # url_articulo).content, "html.parser")

            # Cuerpo
            # cuerpo = ''
            # if(articulo_html.find(class_='article-content').find(class_='article-modules')):
            #     cuerpo = articulo_html.find(class_='article-content').find(class_='article-modules').find_all('p')

            listaArticulos.append(
                {
                    "titulo": titulo,
                    "fecha": fecha,
                    "autor": autor,
                    "descripcion": descripcion,
                    "url_articulos": url_articulo,
                    "url_foto": url_img,
                    "categoria": categoria,
                    "medio": "van"
                })

        except Exception as e:
            print(e.args)
            pass

    with open('noticias.json', 'w', encoding='utf-8') as f:
        json.dump(listaArticulos, f, ensure_ascii=False)


webscraping()
