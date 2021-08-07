"""
Existen tres operadores booleanos.

and: Devuelve True si dos condiciones se cumplen.
or: Devuelve True si al menos una de dos condiciones se cumplen.
not: Devuelve el valor contrario (True -> False, False -> True)
"""

# Ejercicio: Pensar si cada uno de estos es True o False.
ejemplo0 = True
ejemplo1 = True or False
ejemplo2 = True and False
ejemplo3 = not False
ejemplo4 = not True or False
ejemplo5 = True and True or False and False or True
ejemplo6 = not(True or False) or False and not False
ejemplo7 = False or not(not False and not(False or True) or True)

# Respuestas:
print(f"El ejemplo 0 es {ejemplo0}")
print(f"El ejemplo 1 es {ejemplo1}")
print(f"El ejemplo 2 es {ejemplo2}")
print(f"El ejemplo 3 es {ejemplo3}")
print(f"El ejemplo 4 es {ejemplo4}")
print(f"El ejemplo 5 es {ejemplo5}")
print(f"El ejemplo 6 es {ejemplo6}")
print(f"El ejemplo 7 es {ejemplo7}")
