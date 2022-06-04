import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import json

import sys

URL = str(sys.argv[1])

listaOpiniones = []


def webscraping():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(2)

    # Lista de Usuarios/reseñas
    driver.find_element(By.CLASS_NAME, 'DkEaL').click()
    time.sleep(2)

    usuarios = driver.find_elements(By.CLASS_NAME, 'd4r55')
    comentarios = driver.find_elements(By.CLASS_NAME, 'wiI7pd')

    for i in range(len(usuarios)):
        listaOpiniones.append(
            {
                'usuario': usuarios[i].text,
                'comentario': comentarios[i].text
            }
        )

    with open('opiniones.json', 'w', encoding='utf-8') as f:
        json.dump(listaOpiniones, f, ensure_ascii=False)

webscraping()
