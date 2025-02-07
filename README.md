# Extracción de Datos Web con Python

Este script de Python utiliza las bibliotecas `requests` y `BeautifulSoup` para extraer datos de una página web. El script realiza las siguientes funciones:

1. **Realizar una solicitud GET:** Obtiene el contenido HTML de la URL proporcionada.
2. **Crear un objeto BeautifulSoup:** Analiza el contenido HTML.
3. **Extraer el título de la página:** Imprime el título de la página si existe.
4. **Extraer enlaces:** Imprime todos los enlaces (`<a>`) encontrados en la página.
5. **Extraer párrafos:** Imprime el texto de todos los párrafos (`<p>`) encontrados en la página.

## Requisitos

- Python 3.x
- requests
- BeautifulSoup4

Puedes instalar las dependencias necesarias usando pip:

```sh
pip install requests beautifulsoup4
