from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json

import sys

ciudad = str(sys.argv[1])

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.micole.net/mejores-colegios-de-" + ciudad
driver.get(url)
try:
    lista_nombre_pueblos = []
    lista_nombre_pueblos.append(
        driver.find_element_by_xpath("//*[@id='ranking_city']").text)

    lista_nombre_pueblos = [item.replace(' ', '-') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('\n------', ' ') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('á', 'a') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('Á', 'A') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('é', 'e') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('É', 'E') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('í', 'i') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('Í', 'I') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('ó', 'o') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('Ó', 'O') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('ú', 'u') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('Ú', 'U') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('ñ', 'n') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('Ñ', 'N') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace('---Ciudad ---\n', '') for item in lista_nombre_pueblos]
    lista_nombre_pueblos = [item.replace(' --', '') for item in lista_nombre_pueblos]

    cadena_nombres_pueblos = lista_nombre_pueblos[0]

    # Pasar la cadena de pueblos de ciudades a una lista (para usar en URL)
    lista_nombre_pueblos_definitiva = {
        'provincias': cadena_nombres_pueblos.split(' ')}

    # print(lista_nombre_pueblos_definitiva)

    with open('provincia.json', 'w', encoding='utf-8') as f:
        json.dump(lista_nombre_pueblos_definitiva, f, ensure_ascii=False)

except:
    pass

driver.quit()
