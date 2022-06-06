from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
url="https://www.micole.net/"
driver.get(url)

# Obtener la lista de las principales ciudades de españa
lista_nombre_ciudades = []
categorias = ["//*[@id='regiones']/div/div/div[3]", "//*[@id='regiones']/div/div/div[4]", "//*[@id='regiones']/div/div/div[5]", "//*[@id='regiones']/div/div/div[6]", "//*[@id='regiones']/div/div/div[7]"]

for n in categorias:
    lista_nombre_ciudades.append(driver.find_element_by_xpath(n).text)

lista_nombre_ciudades = [item.replace(' ', '-') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('\n', ' ') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('á', 'a') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('Á', 'A') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('é', 'e') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('É', 'E') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('í', 'i') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('Í', 'I') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('ó', 'o') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('Ó', 'O') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('ú', 'u') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('Ú', 'U') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('ñ', 'n') for item in lista_nombre_ciudades]
lista_nombre_ciudades = [item.replace('Ñ', 'N') for item in lista_nombre_ciudades]

cadena_nombres_ciudades = lista_nombre_ciudades[0] + ' ' + lista_nombre_ciudades[1] + ' ' + lista_nombre_ciudades[2] + ' ' + lista_nombre_ciudades[3] + ' ' + lista_nombre_ciudades[4]

# Pasar la cadena de nombres de ciudades a una lista (para usar en URL)
lista_nombre_ciudades_definitiva = {'ciudades':cadena_nombres_ciudades.split(' ')}

# print(lista_nombre_ciudades_definitiva)

with open('ciudades.json', 'w', encoding='utf-8') as f:
        json.dump(lista_nombre_ciudades_definitiva, f, ensure_ascii=False)

driver.quit()