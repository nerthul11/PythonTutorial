"""
Existen tres operadores booleanos.

and: Devuelve True si dos condiciones se cumplen.
or: Devuelve True si al menos una de dos condiciones se cumplen.
not: Devuelve el valor contrario (True -> False, False -> True)

Estos permiten hacer comparaciones entre varios términos.
"""

caso1 = 7 > 3 and 4 * 2 + 1 == 7  # True and False -> False
caso2 = 3 < 6 and 10 == 10.0  # True and True -> True
caso3 = 7 > 3 or 4 * 2 + 1 == 7  # True and False -> True
caso4 = 5 != 5 or False  # False and False -> False
caso5 = not caso4  # False -> True
