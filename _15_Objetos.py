"""
Recién vimos cómo crear clases y subclases, pero nos encontramos con un problema:

No resulta nada práctico crear una subclase para CADA Pokémon, puesto que todos ellos tienen prácticamente
todos los mismos atributos. Por lo tanto, tomaremos el ejemplo anterior y lo optimizaremos un poco.
"""
import random
from _15bis_Pokedex import pokedex

class Pokemon:
    def __init__(self, data, level):
        self.pid = data['id']
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
        ataques_rapidos = pokedex[self.pid-1]['fast_moves']
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
        if pokedex[self.pid]['evolutions']:
            self.pid = pokedex[self.pid]['evolutions']
            self.species = pokedex[self.pid]['name']
            self.ataque_rapido = random.choice(pokedex[self.pid]['fast_moves'])
            ataques_cargados = pokedex[self.pid]['charged_moves']
            self.ataque_cargado1 = random.choice(pokedex[self.pid]['charged_moves'])
            ataques_cargados.remove(self.ataque_cargado1)
            if self.ataque_cargado2:
                self.ataque_cargado2 = random.choice(ataques_cargados)

    def __str__(self):
        a = f"{self.species} Nv. {self.level} ({self.ataque_iv}/{self.defensa_iv}/{self.salud_iv})"
        b = f"\n{self.ataque_rapido}, {self.ataque_cargado1}/{self.ataque_cargado2}"
        return a + b

poke = Pokemon(pokedex[random.randint(1, 2)], random.randint(1, 35))
print(poke)
poke.agregar_segundo_ataque()
print(poke)
poke.evolucionar()
print(poke)
