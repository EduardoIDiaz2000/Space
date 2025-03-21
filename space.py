import requests

def obtener_imagen():
    api_key = "W5hZks5ebJeEBlscnkNL6q7ew6sQOu8byvglePIv"
    # Construir la URL de la API de la imagen del día (APOD)
    url_api = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    # Realizamos la solicitud a la API
    response = requests.get(url_api)
    
    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        title = data.get("title", "imagen")
        print("Título:", title)
        print("URL de la imagen:", image_url)
        
        # Descargamos la imagen
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # Guardamos la imagen en un archivo
            filename = "apod.jpg"
            with open(filename, "wb") as file:
                file.write(image_response.content)
            print(f"Imagen guardada exitosamente como {filename}")
        else:
            print("Error al descargar la imagen:", image_response.status_code)
    else:
        print("Error en la solicitud a la API:", response.status_code)

