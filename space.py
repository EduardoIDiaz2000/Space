import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def obtener_imagen():
    # Obtener la clave API desde .env
    api_key = os.getenv("NASA_API_KEY")

    if not api_key:
        print("❌ Error: No se encontró la API Key en .env")
        return

    # Construir la URL de la API
    url_api = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    # Hacer la solicitud a la API
    response = requests.get(url_api)

    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        title = data.get("title", "imagen")
        
        print("Título:", title)
        print("URL de la imagen:", image_url)
        
        if image_url:
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                filename = "apod.jpg"
                with open(filename, "wb") as file:
                    file.write(image_response.content)
                print(f"✅ Imagen guardada como {filename}")
            else:
                print("❌ Error al descargar la imagen:", image_response.status_code)
        else:
            print("❌ No se encontró la URL de la imagen en la respuesta.")
    else:
        print("❌ Error en la solicitud a la API:", response.status_code)
