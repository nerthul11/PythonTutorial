"""
Partiendo de la base del JSON creado en el archivo _18_API_Parte3.py, agregar un campo cuya clave sea
"shiny_disponible" y su valor sea True o False según el valor marcado en la API.
"""
import json

with open('_18bis_Pokedex.json', 'r') as archivo:
    pokedex = json.loads(archivo.read())
