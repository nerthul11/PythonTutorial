"""
El ejemplo anterior funciona muy bien, pero presenta un problema para nada menor: Construir un listado con toda
la información de todos los Pokémon. De hecho, en el ejemplo anterior obtuvimos información útil, pero para
nada exhaustiva sobre toda la que existe.

Eso es un trabajo no solamente muy engorroso sino además innecesario, pues ya alguien debe haberlo hecho, y
así es. Para ello, usaremos lo que se llaman API (Application program interface).

Primero importaremos una librería llamada "requests". En caso de no tenerla instalada, hay que abrir una
terminal e instalarla con el comando: pip install requests.
"""
import requests

# Luego, utilizando requests.get (Una función de esa librería) accederemos a la info publicada en un link:
res = requests.get('https://pogoapi.net/api/v1/released_pokemon.json')

# Nota: Suponiendo que el link funcione, el "Status Code", la respuesta del servidor, es 200. Comprobemos eso.
print(res.status_code)  # Si el valor es distinto a 200 es porque algo salió mal.

# Si entran al link, se verá un listado enorme de Pokémon, que se puede utilizar aquí de este modo:
pokes = res.json()
print(pokes["376"])

"""
¡Pero esto solo me da el ID y el nombre, necesito más información!

Para eso, por lo general las fuentes de las API documentan su información. En este caso, el link de la
documentación de pogoapi es este: https://pogoapi.net/documentation/

Allí hay muchas posibilidades de importar API y trabajar sobre ellas, la clave está en comprender cómo se
estructuran los datos en la fuente y en cómo los queremos utilizar.
"""
