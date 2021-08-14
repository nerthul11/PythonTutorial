"""
Habiendo aprendido sobre las colecciones, estamos en condiciones de aprender el otro ciclo: For.

For tiene una idea similar a While, pero a diferencia de While que es un "mientras que", el For
podría traducirse como "para cada uno de estos elementos", lo que lo hace más útil para iterar sobre
elementos específicos que While.
"""

# Supongamos que tenemos una lista de frutas y queremos imprimir las frutas una por una
frutas = ['manzana', 'naranja', 'banana', 'pera']

# Normalmente, hubiéramos hecho print(frutas[0]), print(frutas[1]) y así, pero no es muy eficiente que digamos.

# Esto podría leerse como "para cada fruta dentro de frutas"
for fruta in frutas:
    print(fruta)  # Imprime el valor de fruta -> manzana, naranja, ...

# For también se puede usar para recorrer un String letra por letra
nombre = "Leandro"

for letra in nombre:
    print(letra)

# O los números dentro de un rango.
for numero in range(0, 10):
    print(numero)  # Esto imprime todos los números del 0 al 10 (no inclusive!)

# O bien también puede usarse para recorrer todos los objetos de un diccionario y sus valores
diccionario = {'nombre': 'Manzana', 'color': 'Rojo', 'sabor': 'Dulce'}

for clave, valor in diccionario.items():
    print(clave)
    print(valor)
