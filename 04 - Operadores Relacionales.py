"""
El valor de algo también puede definirse haciendo una comparación entre dos o más elementos.
>: Mayor que.
>=: Mayor o igual que.
==: Igual que. (Recordemos que un solo "=" se usa para asignar valores)
<=: Menor o igual que.
<: Menor que.

Esto dará como resultado un valor booleano (True o False).
Asimismo, estos operadores son válidos únicamente con valores numéricos (Int o Float)
"""

variable = 5 > 3
print(variable)  # El valor de variable es True porque 5 es mayor que 3.

variable = 5 >= 5
print(variable)  # El valor sigue siendo True, porque >= contempla casos de igualdad.