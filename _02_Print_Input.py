"""
Hasta el momento, solo se han declarado variables. Es decir, ejecutar ese código
no tiene ninguna acción concreta.

En este archivo se verá la función integrada print() y se utilizará el comando
input() para poder definir una variable con un valor que sea, justamente, variable.

El resultado de este programa será un mensaje que diga un nombre.

Primero, definiremos el nombre usando la consola
"""
nombre = input("Escribe tu nombre: ") # Esto hará que un mensaje aparezca. El espacio al final es por estética.
print(nombre)

"""
Luego ejecutaremos un print que diga "Hola, " seguido del nombre insertado.

La f adelante de las comillas indica que es una formatted string, es decir, una cadena con formato, que
incluye dentro de ella una variable.
"""
print(f"Hola, {nombre}")
