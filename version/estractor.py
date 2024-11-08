import requests
from bs4 import BeautifulSoup
import re

def obtener_urls_multimedia(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Diccionario para almacenar y clasificar URLs
        recursos = {
            "imagenes": [],
            "videos": [],
            "audios": [],
            "documentos": [],
            "otros": []
        }
        
        # Obtener todos los enlaces en la página
        for tag in soup.find_all(['img', 'a', 'video', 'audio', 'source']):
            recurso_url = tag.get('src') or tag.get('href')
            if recurso_url:
                # Clasificar según la extensión del archivo
                if re.search(r'\.(jpg|jpeg|png|gif|svg)$', recurso_url, re.IGNORECASE):
                    recursos["imagenes"].append(recurso_url)
                elif re.search(r'\.(mp4|webm|avi)$', recurso_url, re.IGNORECASE):
                    recursos["videos"].append(recurso_url)
                elif re.search(r'\.(mp3|wav|ogg)$', recurso_url, re.IGNORECASE):
                    recursos["audios"].append(recurso_url)
                elif re.search(r'\.(pdf|docx|txt)$', recurso_url, re.IGNORECASE):
                    recursos["documentos"].append(recurso_url)
                else:
                    recursos["otros"].append(recurso_url)
        
        return recursos
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return None

# Ejecución interactiva
url = input("INGRESA UNA URL: ")
recursos = obtener_urls_multimedia(url)

if recursos:
    for tipo, urls in recursos.items():
        print(f"{tipo.capitalize()}: {len(urls)} encontrados")
        for recurso in urls:
            print(f"  - {recurso}")
import requests
from bs4 import BeautifulSoup
import re

def obtener_urls_multimedia(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Diccionario para almacenar y clasificar URLs
        recursos = {
            "imagenes": [],
            "videos": [],
            "audios": [],
            "documentos": [],
            "otros": []
        }
        
        # Obtener todos los enlaces en la página
        for tag in soup.find_all(['img', 'a', 'video', 'audio', 'source']):
            recurso_url = tag.get('src') or tag.get('href')
            if recurso_url:
                # Clasificar según la extensión del archivo
                if re.search(r'\.(jpg|jpeg|png|gif|svg)$', recurso_url, re.IGNORECASE):
                    recursos["imagenes"].append(recurso_url)
                elif re.search(r'\.(mp4|webm|avi)$', recurso_url, re.IGNORECASE):
                    recursos["videos"].append(recurso_url)
                elif re.search(r'\.(mp3|wav|ogg)$', recurso_url, re.IGNORECASE):
                    recursos["audios"].append(recurso_url)
                elif re.search(r'\.(pdf|docx|txt)$', recurso_url, re.IGNORECASE):
                    recursos["documentos"].append(recurso_url)
                else:
                    recursos["otros"].append(recurso_url)
        
        return recursos
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return None

# Ejecución interactiva
url = input("INGRESA UNA URL: ")
recursos = obtener_urls_multimedia(url)

if recursos:
    for tipo, urls in recursos.items():
        print(f"{tipo.capitalize()}: {len(urls)} encontrados")
        for recurso in urls:
            print(f"  - {recurso}")
