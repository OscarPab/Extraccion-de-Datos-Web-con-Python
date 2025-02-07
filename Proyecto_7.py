import requests
from bs4 import BeautifulSoup

def extraer_datos(url):
    try:
        # Realizar una solicitud GET a la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si la solicitud fue exitosa
        
        # Crear un objeto BeautifulSoup con el contenido HTML
        sopa = BeautifulSoup(respuesta.content, 'html.parser')
        
        # Extraer el título de la página
        if sopa.title:
            titulo = sopa.title.string
            print(f"Título de la página: {titulo}")
        else:
            print("La página no tiene una etiqueta <title>.")
        
        # Extraer todos los enlaces de la página
        enlaces = sopa.find_all('a')
        for enlace in enlaces:
            print(enlace.get('href'))
        
        # Extraer todos los párrafos de la página
        parrafos = sopa.find_all('p')
        for parrafo in parrafos:
            print(parrafo.text)
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    except Exception as e:
        print(f"Error al procesar la página: {e}")

# Solicitar al usuario la URL de la página web
url = input("Introduce la URL de la página web que deseas analizar: ")
extraer_datos(url)
