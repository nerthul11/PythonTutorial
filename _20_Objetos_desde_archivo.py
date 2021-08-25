"""
Ahora que tenemos nuestra Pokedex mucho más completa, podemos rearmar un poco la Clase de _15_Objetos.py adaptándola
a las pequeñas pero existentes diferencias de formato, y leyendo desde el archivo que creamos en lugar de crear el
contenido de la variable cada vez que se ejecuta el programa, algo que consume mucho tiempo y memoria.
"""
import random
import json

with open('_19bis_Pokedex.json', 'r') as archivo:
    pokedex = json.loads(archivo.read())

class Pokemon:
    def __init__(self, data, level):
        self.pid = str(data['id'])
        self.level = level
        self.species = data['name']
        self.type1 = data['type'][0]
        self.type2 = data['type'][1] if len(data['type']) > 1 else None
        self.ataque_iv = random.randint(0, 15)
        self.defensa_iv = random.randint(0, 15)
        self.salud_iv = random.randint(0, 15)
        self.ataque_rapido = random.choice(data['fast_moves'])
        self.ataque_cargado1 = random.choice(data['charged_moves'])
        self.ataque_cargado2 = None

    def mt_rapido(self):
        ataques_rapidos = pokedex[self.pid]['fast_moves']
        ataques_rapidos.remove(self.ataque_rapido)
        self.ataque_rapido = random.choice(ataques_rapidos)

    def mt_cargado(self, n):
        ataques_cargados = pokedex[self.pid]['charged_moves']
        if n == 1:
            ataques_cargados.remove(self.ataque_cargado1)
            if self.ataque_cargado2:
                ataques_cargados.remove(self.ataque_cargado2)
            self.ataque_cargado1 = random.choice(ataques_cargados)
        elif n == 2:
            ataques_cargados.remove(self.ataque_cargado1)
            ataques_cargados.remove(self.ataque_cargado2)
            self.ataque_cargado2 = random.choice(ataques_cargados)

    def agregar_segundo_ataque(self):
        if not self.ataque_cargado2:
            ataques_cargados = pokedex[self.pid]['charged_moves']
            ataques_cargados.remove(self.ataque_cargado1)
            self.ataque_cargado2 = random.choice(ataques_cargados)

    def evolucionar(self):
        try:
            evolution = random.choice(pokedex[self.pid]['evolutions'])
            self.pid = str(evolution['pokemon_id'])
            self.species = pokedex[self.pid]['name']
            self.ataque_rapido = random.choice(pokedex[self.pid]['fast_moves'])
            ataques_cargados = pokedex[self.pid]['charged_moves']
            self.ataque_cargado1 = random.choice(pokedex[self.pid]['charged_moves'])
            ataques_cargados.remove(self.ataque_cargado1)
            if self.ataque_cargado2:
                self.ataque_cargado2 = random.choice(ataques_cargados)
            print('¡La evolución fue un éxito!')
        except KeyError:
            print(f'{self.species} no puede evolucionar.')

    def __str__(self):
        a = f"{self.species} Nv. {self.level} ({self.ataque_iv}/{self.defensa_iv}/{self.salud_iv})"
        b = f"\n{self.ataque_rapido}, {self.ataque_cargado1}/{self.ataque_cargado2}"
        return a + b

pokemon_salvaje = Pokemon(random.choice(list(pokedex.values())), random.randint(1, 35))
print(pokemon_salvaje)
pokemon_salvaje.agregar_segundo_ataque()
print(pokemon_salvaje)
pokemon_salvaje.evolucionar()
print(pokemon_salvaje)
