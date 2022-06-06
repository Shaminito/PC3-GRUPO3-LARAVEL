import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from sentiment_analysis_spanish import sentiment_analysis

import json

import sys

colegio = sys.argv[1]

URL = 'https://www.google.es/maps/search/'+colegio

listaOpiniones = []


def analisis_sentimiento(texto):

    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    score = sentiment.sentiment(texto)

    return score


def webscraping():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)
    time.sleep(2)

    try:
        # Lista de Usuarios/reseñas
        driver.find_element(By.CLASS_NAME, 'DkEaL').click()
        time.sleep(2)

        usuarios = driver.find_elements(By.CLASS_NAME, 'd4r55')
        comentarios = driver.find_elements(By.CLASS_NAME, 'wiI7pd')

        for i in range(5):
            if comentarios[i].text:
                listaOpiniones.append(
                    {
                        'usuario': usuarios[i].text,
                        'comentario': comentarios[i].text,
                        'analisis_sent': analisis_sentimiento(comentarios[i].text)
                    }
                )
    except:
        pass

    with open('opiniones.json', 'w', encoding='utf-8') as f:
        json.dump(listaOpiniones, f, ensure_ascii=False)


webscraping()
