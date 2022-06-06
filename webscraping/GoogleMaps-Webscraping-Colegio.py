import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import json

import sys

colegio = sys.argv[1]

URL = 'https://www.google.es/maps/search/'+colegio


def webscraping():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(5)

    try:
        # Reseña media
        resMedia = driver.find_element(
            By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span[1]').text
        print(resMedia)

        # Num comentarios
        numComentarios = driver.find_element(By.CLASS_NAME, 'DkEaL').text
        print(numComentarios)

        # Direccion
        direccion = driver.find_element(By.CLASS_NAME, 'Io6YTe').text
        print(direccion)

        colegio_json = {
            'nombre_colegio': colegio,
            'opinion_media': resMedia,
            'comentarios_cant': numComentarios,
            'direccion': direccion
            }

        with open('colegio.json', 'w', encoding='utf-8') as f:
            json.dump(colegio_json, f, ensure_ascii=False)

    except Exception as e:
        print(e.with_traceback)
        pass

    driver.quit()


webscraping()
