import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import json

import sys

busqueda = sys.argv[1]

URL = 'https://www.google.es/maps/search/'+busqueda

listaColegios = []


def webscraping():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(2)

    colegios = driver.find_elements(By.CLASS_NAME, 'Nv2PK')

    listaUrls = []

    for colegio in colegios:

        # Extraer url colegio
        url = colegio.find_element(By.TAG_NAME, 'a').get_attribute("href")
        listaUrls.append(url)

    for url in listaUrls:
        driver.get(url)

        try:
            # Reseña media
            resMedia = driver.find_element(
                By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span[1]').text
            # print(resMedia)

            # Nombre Colegio
            nomColegio = driver.find_element(By.TAG_NAME, 'h1').text
            # print(nomColegio)

            # Num comentarios
            numComentarios = driver.find_element(By.CLASS_NAME, 'DkEaL').text
            # print(numComentarios)

            # Direccion
            direccion = driver.find_element(By.CLASS_NAME, 'Io6YTe').text
            # print(direccion)

            # Lista de Usuarios/reseñas
            # driver.find_element(By.CLASS_NAME, 'DkEaL').click()
            # time.sleep(2)

            # usuarios = driver.find_elements(By.CLASS_NAME, 'd4r55')
            # for usuario in usuarios:
            #     print (usuario.text)

            # comentarios = driver.find_elements(By.CLASS_NAME, 'wiI7pd')
            # for comentario in comentarios:
            #     print(comentario.text)

            listaColegios.append(
                {
                    'nombre_colegio': nomColegio,
                    'opinion_media': resMedia,
                    'comentarios_cant': numComentarios,
                    'direccion': direccion
                }
            )
        except:
            pass

    with open('colegios.json', 'w', encoding='utf-8') as f:
        json.dump(listaColegios, f, ensure_ascii=False)
    driver.quit()


webscraping()
