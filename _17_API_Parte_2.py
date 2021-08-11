"""
Ahora intentaremos hacer algo similar a lo que creamos en el archivo 15 pero utilizando las API de
https://pogoapi.net/

Para lograr lo hecho, necesitamos contar con los campos de ID, Nombre, Tipo, Ataques y Evolución.
"""
import requests

# Haremos que el programa se corra en una función para poder darle un uso en otros archivos.
def crear_pokedex():
    base_path = 'https://pogoapi.net/'

    # Primero, descargaremos toda la información necesaria: Nombres, Ataques, Tipos y Evoluciones.
    names = requests.get(f'{base_path}/api/v1/released_pokemon.json').json()
    moves = requests.get(f'{base_path}/api/v1/current_pokemon_moves.json').json()
    types = requests.get(f'{base_path}/api/v1/pokemon_types.json').json()
    evolutions = requests.get(f'{base_path}/api/v1/pokemon_evolutions.json').json()

    # Luego creamos un nuevo diccionario y lo empezamos a completar, primero con los ID y nombres.
    nueva_pokedex = dict()
    for pid, data in names.items():
        nueva_pokedex[int(pid)] = {'id': data['id'], 'name': data['name']}

    # Ahora sumaremos el tipo: Aquí filtramos todos los que tengan formas alternativas para dar simpleza.
    for pokemon in types:
        if pokemon['form'] == 'Normal':
            try:
                nueva_pokedex[pokemon['pokemon_id']]['type'] = pokemon['type']
            except KeyError:  # En caso de que alguna ID no esté en el listado original, lo salteamos.
                pass

    # Luego sumaremos las evoluciones.
    for pokemon in evolutions:
        if pokemon['form'] == 'Normal':
            try:
                nueva_pokedex[pokemon['pokemon_id']]['evolutions'] = pokemon['evolutions']
            except KeyError:
                pass

    # Y, finalmente, sumamos sus técnicas.
    for pokemon in moves:
        if pokemon['form'] == 'Normal':
            try:
                nueva_pokedex[pokemon['pokemon_id']]['fast_moves'] = pokemon['fast_moves']
                nueva_pokedex[pokemon['pokemon_id']]['elite_fast_moves'] = pokemon['elite_fast_moves']
                nueva_pokedex[pokemon['pokemon_id']]['charged_moves'] = pokemon['charged_moves']
                nueva_pokedex[pokemon['pokemon_id']]['elite_charged_moves'] = pokemon['elite_charged_moves']
            except KeyError:
                pass

    # Finalizamos la función retornando la nueva pokedex completa.
    return nueva_pokedex

if __name__ == '__main__':
    # Ejecutamos la función.
    data = crear_pokedex()

    # Finalmente, visualizamos cómo queda un ejemplo X, en este caso el Pokemon 25: Pikachu.
    print(data[25])
