import requests

url = 'https://netsg.cs.sfu.ca/youtubedata/'
zip_file_path = '0309.zip' 

try:
    response = requests.get(url)
    response.raise_for_status() 

    with open(zip_file_path, 'wb') as f:
        f.write(response.content)

    print("Archivo descargado exitosamente.")

except requests.exceptions.RequestException as e:
    print(f"Error al descargar el archivo: {e}")
