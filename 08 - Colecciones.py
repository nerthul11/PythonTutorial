"""
Hemos visto variables, operadores, condicionales y un tipo de ciclo. Ahora, veremos que existen formas de
almacenar múltiples valores en una única variable. Existen 4 formas de hacerlo.
"""

# Set: Se encierra entre llaves. Son elementos que están desordenados, inmutables y que no se pueden repetir.
data_set = {"rojo", "azul", "amarillo", "rojo"}
print(data_set)  # Al imprimirlo, el valor "rojo", que figura dos veces, aparece una vez y se ignora la segunda.

# Tupla (Tuple): Las tuplas también son inmutables (no se pueden modificar) pero tienen un orden y pueden repetirse.
data_tuple = (1, 2, 5, 3, 1, 0)
print(data_tuple)
print(data_tuple[0])  # El número entre corchetes indica la posición dentro de la tupla, empezando desde 0.

# Lista (List): Las listas tienen un orden y pueden modificarse. Los elementos pueden repetirse.
data_list = [1, 5, 3, 2, 9]

# Diccionario (Dict): Cada componente de un diccionario posee una clave (key) y un valor (value)
data_dict = {"nombre": "Leandro", "edad": 29}
