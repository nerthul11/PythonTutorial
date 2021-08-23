"""
Otro concepto clave en programación es el de ciclo o bucle (Loop).

En Python existen dos tipos de bucle, ahora veremos uno de ellos: While (mientras que).

Un ciclo es un fragmento de código que se ejecuta una y otra vez hasta que se rompe.

El ciclo while se ejecutará indefinidamente hasta que se cumpla la condición o bien
se utilice el comando "break"
"""

# Creamos una variable llamada n y le asignamos de valor 0
n = 0

# Creamos un ciclo que, "mientras que" (while) n sea menor a 10, le sume 1 al valor de n y lo imprima en pantalla.
while n < 10:
    n += 1
    print(n)

print("El ciclo finalizó")
