from bs4 import BeautifulSoup
import requests

import json

import sys

categoria = int(sys.argv[1])
pagina = sys.argv[2]

URLs = [
    {'https://www.20minutos.es/busqueda/'+pagina +
        '/?q=Educacion&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'},            # 0 = educacion
    {'https://www.20minutos.es/busqueda/'+pagina + \
        '/?q=Acoso+escolar&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'},        # 1 = acoso escolar
    {'https://www.20minutos.es/busqueda/'+pagina + \
        '/?q=Delitos+de+odio&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'},      # 2 = delitos de odio
    {'https://www.20minutos.es/busqueda/'+pagina + \
        '/?q=Discriminacion&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'},       # 3 = discriminación
    {'https://www.20minutos.es/busqueda/'+pagina + \
        '/?q=Discurso+de+odio&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'},     # 4 = discurso del odio
    {'https://www.20minutos.es/busqueda/'+pagina + \
        '/?q=Ciberodio&sort_field=&category=&publishedAt%5Bfrom%5D=&publishedAt%5Buntil%5D=&articleTypes%5B0%5D=&excludedArticleTypes%5B0%5D=mam'}             # 5 = ciberodio
]

listaArticulos = []


def webscraping():

    url = URLs[categoria].pop()

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Obtener los articulos
    articulos = soup.find('section').find_all('article')

    for articulo in articulos:

        try:
            # Titulo
            titulo = articulo.find('header').find('h1').find('a').text.strip()

            # Autor
            autor = articulo.find(class_='author').find('span').text.strip()

            # Descripcion
            descripcion = ''
            for li in articulo.find_all('li'):
                descripcion = descripcion + li.text + '\n'

            # Obtener la URL
            url_articulo = articulo.find('header').find(
                'h1').find(href=True)['href']

            articulo_html = BeautifulSoup(requests.get(
                url_articulo).content, "html.parser")

            # Fecha
            fecha = articulo_html.find(class_='article-date').find('a').text

            # URL Foto
            url_img = articulo_html.find(class_='image').find('img')['src']

            # Cuerpo
            # cuerpo = articulo_html.find(class_='article-text').find_all('p')

            if(url_articulo.find('videos') == -1):
                listaArticulos.append(
                    {
                        "titulo": titulo,
                        "fecha": fecha,
                        "autor": autor,
                        "descripcion": descripcion,
                        "url_articulos": url_articulo,
                        "url_foto": url_img,
                        "categoria": categoria,
                        "medio": "20min"
                    })

        except:
            pass

    with open('noticias.json', 'w', encoding='utf-8') as f:
        json.dump(listaArticulos, f, ensure_ascii=False)


webscraping()
