"""
El término librería refiere a un paquete de Python. Un paquete de Python son archivos, con código,
que pueden importarse para trabajar en otros archivos.

Hay librerías complejas, que cumplen muchas funciones, y hay otras un tanto más simples.

También se pueden importar funciones de archivos que tengas en la misma carpeta.
"""

import random
from _13_Funciones import es_par

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)
print(es_par(numero_aleatorio))
