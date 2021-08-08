"""
Los diccionarios, como vimos, cuentan con elementos con claves y valores.

Estos no tienen un orden como las listas, sino que se indexan por clave.

Cada clave es única, pero dos claves distintas pueden tener un mismo valor.
"""

# Creamos un diccionario muy simple: una fruta que tiene un nombre y un color
manzana = {'nombre': 'Manzana', 'color': 'Rojo'}

# Algunas formas de referenciar valores
print(manzana['nombre'])  # 'Manzana'
print(manzana.get('color'))  # 'Rojo'
print(manzana.items())  # dict_items([('nombre', 'Manzana'), ('color', 'Rojo')]))

# Se pueden crear nuevas claves para ese diccionario, por ejemplo, el sabor de una manzana
manzana['sabor'] = 'Dulce'
print(manzana)  # {'nombre': 'Manzana', 'color': 'Rojo', 'sabor': 'Dulce'}

# Del mismo modo, se pueden modificar valores existentes. Por ejemplo, hagamos que la manzana sea verde
manzana['color'] = 'Verde'
print(manzana)  # {'nombre': 'Manzana', 'color': 'Verde', 'sabor': 'Dulce'}

# O también se pueden remover claves y sus respectivos valores
manzana.pop('nombre')
print(manzana)

# Y, al igual que con las listas, se puede vaciar
manzana.clear()
print(manzana)
