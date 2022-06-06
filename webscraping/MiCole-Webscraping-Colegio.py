from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import sys

import json


def webscraping(url):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        driver.get(driver.find_element(By.TAG_NAME, 'ol').find_element(
            By.TAG_NAME, 'li').find_element(By.TAG_NAME, 'a').get_attribute("href"))

        nombre = driver.find_element(By.TAG_NAME, 'h1').text
        # Devuelve el nombre y las valoraciones. Solo obtiene el nombre
        # print(nombre.split('\n')[0])

        driver.quit()
        
        with open('nombre.txt', 'w', encoding='utf-8') as f:
            json.dump(nombre.split('\n')[0].encode().decode(), f, ensure_ascii=False)
    except:
        pass


def main():

    ciudad = 0
    provincia = 0

    try:
        ciudad = str(sys.argv[1])

        provincia = str(sys.argv[2])
    except:
        pass
    finally:

        if(provincia):
            url = "https://www.micole.net/" + ciudad + "/mejores-colegios-de-" + provincia

            return webscraping(url)

        if(ciudad):
            url = "https://www.micole.net/mejores-colegios-de-" + ciudad
            return webscraping(url)


main()
