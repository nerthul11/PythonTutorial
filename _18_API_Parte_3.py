"""
Suponiendo que tuviéramos un sitio web propio, podríamos utilizar el trabajo de recién para crear una
API en la cual se puedan descargar la información que construimos.

Para ello, tenemos que guardar en un archivo .json la información completa. Luego, suponiendo que contásemos con
un sitio web propio, basta con crear un link que de como resultado este JSON para que otros desarrolladores puedan
usar nuestro API.
"""
import json
from _17_API_Parte_2 import crear_pokedex

data = crear_pokedex()
with open('_18bis_Pokedex.json', 'w') as f:
    json.dump(data, f)
