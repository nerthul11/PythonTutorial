"""
Dentro de los temas básicos de Python, llegamos finalmente al más complejo de ellos: las clases.

Las clases se utilizan en la Programación Orientada a Objetos, y su finalidad es crear objetos que
cuenten con atributos y métodos únicos, y que múltiples variables puedan ser instancias de dicha clase.
"""
import random

class Pokemon:
    def __init__(self, pid, species, level, type1, type2=None, ataques_rapidos=['Placaje'], ataques_cargados=['Combate']):
        self.pid = pid
        self.level = level
        self.species = species
        self.type1 = type1
        self.type2 = type2
        self.ataque_iv = random.randint(0, 15)
        self.defensa_iv = random.randint(0, 15)
        self.salud_iv = random.randint(0, 15)
        self.ataque_rapido = random.choice(ataques_rapidos)
        self.ataque_cargado1 = random.choice(ataques_cargados)
        self.ataque_cargado2 = None

    def mt_rapido(self):
        ataques_rapidos = ['Impactrueno', 'Ataque Rápido']
        ataques_rapidos.remove(self.ataque_rapido)
        self.ataque_rapido = random.choice(ataques_rapidos)

    def mt_cargado(self, n):
        ataques_cargados = ['Chispazo', 'Rayo', 'Voltio Cruel']
        if n == 1:
            ataques_cargados.remove(self.ataque_cargado1)
            if self.ataque_cargado2:
                ataques_cargados.remove(self.ataque_cargado2)
            self.ataque_cargado1 = random.choice(ataques_cargados)
        elif n == 2:
            ataques_cargados.remove(self.ataque_cargado1)
            ataques_cargados.remove(self.ataque_cargado2)
            self.ataque_cargado2 = random.choice(ataques_cargados)

class Pikachu(Pokemon):
    def __init__(self, level):
        ataques_rapidos = ['Impactrueno', 'Ataque Rápido']
        ataques_cargados = ['Chispazo', 'Rayo', 'Voltio Cruel']
        Pokemon.__init__(self,
                         level=level,
                         pid=25, species="Pikachu",
                         type1="Electrico", ataques_rapidos=ataques_rapidos,
                         ataques_cargados=ataques_cargados)

    def __str__(self):
        return f"{self.species} Nv. {self.level} ({self.ataque_iv}/{self.defensa_iv}/{self.salud_iv})"

    def evolucionar(self):
        ataques_rapidos = ['Chispa', 'Voltiocambio', 'Impactrueno', 'Encanto']
        ataques_cargados = ['Puño Trueno', 'Demolición', 'Cabezazo', 'Voltio Cruel']

        self.pid = 26
        self.species = "Raichu"
        self.ataque_rapido = random.choice(ataques_rapidos)
        self.ataque_cargado1 = random.choice(ataques_cargados)
        ataques_cargados.remove(self.ataque_cargado1)
        if self.ataque_cargado2:
            self.ataque_cargado2 = random.choice(ataques_cargados)

if __name__ == "__main__":
    pikachu1 = Pikachu(10)
    pikachu2 = Pikachu(35)
    pikachu2.evolucionar()
    print(pikachu1)
    print(pikachu2)
