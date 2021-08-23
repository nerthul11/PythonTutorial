"""
Las listas y diccionarios son elementos extremadamente útiles y versátiles.

Primero trabajaremos con las listas y algunos de los usos que se les puede dar.
"""

# Primero, crearemos una lista con algunos nombres
lista_de_nombres = ["Leandro", "Eliana", "Lidia", "Gabriel"]
print(lista_de_nombres)  # ['Leandro', 'Eliana', 'Lidia', 'Gabriel']

# Como ya vimos, se puede referenciar un elemento particular de la lista por su posición
print(lista_de_nombres[0])  # 'Leandro'
print(lista_de_nombres[-1])  # 'Gabriel' - Números negativos indican que se mueve de atrás hacia adelante.

# Se pueden agregar elementos a una lista
lista_de_nombres.append("Brenda")
print(lista_de_nombres)  # ['Leandro', 'Eliana', 'Lidia', 'Gabriel', 'Brenda']

# Se pueden ordenar alfabéticamente
lista_de_nombres.sort()
print(lista_de_nombres)  # ['Brenda', 'Eliana', 'Gabriel', 'Leandro', 'Lidia']

# Se puede encontrar la posición de un valor (si es repetido, la posición indica su primera aparición)
print(lista_de_nombres.index("Leandro"))  # 3. Si no existe el valor dentro de la lista, recibimos un ValueError

# Se pueden remover valores
lista_de_nombres.remove("Leandro")
print(lista_de_nombres)  # ['Brenda', 'Eliana', 'Gabriel', 'Lidia']

# Se pueden contar cuántos elementos tiene utilizando la función len()
print(len(lista_de_nombres))  # 4

# Se puede limpiar por completo
lista_de_nombres.clear()
print(lista_de_nombres)  # []
