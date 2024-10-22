import zipfile
import os

zip_file_path = '0309.zip' 
extract_folder = 'PROBLEMA 3/ARCHIVO DESCOMPRIMIDO'


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("Archivos descomprimidos en:", extract_folder)


