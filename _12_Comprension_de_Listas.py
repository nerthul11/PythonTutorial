"""
El uso del bucle For es una herramienta muy potente con listas, diccionarios u objetos complejos como los
vistos hasta ahora. Sin embargo, en ocasiones puede traer algunos problemas, y ahora veremos algunas formas
para resolverlos.

Asimismo, también veremos cómo simplificar la sintaxis de algunas operaciones utilizando la comprensión de listas.
"""

# Creamos una lista hipotética: Números del 0 al 99 (pero no todos!)
lista = [90, 41, 31, 92, 46, 74, 51, 88, 26, 83, 77, 15, 42, 14, 97, 98, 45, 84, 72, 18, 65, 76, 70, 69, 71, 4, 17, 47, 81, 50, 43, 27, 13, 36, 44, 0, 82, 30, 53, 29, 62, 37, 96, 10, 56, 9, 68, 38, 66, 54, 28, 24, 99, 7, 32, 59, 8, 16, 19, 95, 48, 63, 78, 40, 52, 87, 5, 79, 55, 91, 67, 73, 2, 57, 12, 3, 89]

# Creamos un for que elimine todos los elementos mayores a 10.
for numero in lista:
    if numero > 10:
        lista.remove(numero)

# El resultado esperado, en este caso, sería: [4, 0, 10, 9, 7, 8, 5, 2, 3]
print(lista)

"""
Un momento, esto me da bastante distinto y hice lo que decía acá... ¿Qué pasó?

Un error muy común, si no estamos prevenidos, es intentar, mediante un bucle, modificar una lista existente.
Algunas consideraciones: Un "for", lo que hace, es ir posición por posición dentro de una lista.

En este caso, primero agarra la posición 0 (90) y, comprobando que sea mayor a 10, lo elimina.
Luego, busca la posición 1, que originalmente era el número 41. Sin embargo, como se eliminó de la lista
el número 90, este pasa a ser la posición 0, y por lo tanto el for agarra la posición 1 que ahora es 31.
Luego, busca la posición 2, que normalmente sería el 31, pero sin el 90 ni el 31, esta pasa a ser el 46, y así,
este proceso se repite y al final del mismo casi la mitad de los números mayores a 10 no fueron filtrados.

Busquémosle la vuelta.
"""

# Primero, devolvemos la lista a su estado original.
lista = [90, 41, 31, 92, 46, 74, 51, 88, 26, 83, 77, 15, 42, 14, 97, 98, 45, 84, 72, 18, 65, 76, 70, 69, 71, 4, 17, 47, 81, 50, 43, 27, 13, 36, 44, 0, 82, 30, 53, 29, 62, 37, 96, 10, 56, 9, 68, 38, 66, 54, 28, 24, 99, 7, 32, 59, 8, 16, 19, 95, 48, 63, 78, 40, 52, 87, 5, 79, 55, 91, 67, 73, 2, 57, 12, 3, 89]

# Ahora, para evitar trabajar sobre una lista existente, crearemos una nueva y trabajaremos sobre la misma.
nueva_lista = list()

# Con un For, en lugar de borrar los mayores de 10, agregaremos a esta nueva lista los menores a 10.
for numero in lista:
    if numero <= 10:
        nueva_lista.append(numero)

# La Comprensión de Listas es un modo de simplificar esta operación, sin necesidad de emplear nuevas variables.
lista = [numero for numero in lista if numero <= 10]

"""
lista y nueva_lista ahora mismo son iguales, son dos modos distintos de llegar a lo mismo, pero la comprensión de
listas te permite no necesitar la asignación de nuevas variables para modificar una lista existente.

Ahora supongamos que queremos hacer que a nuestra lista original se le sumen los números del 0 al 10 que le faltan.

Podemos utilizar la comprensión de listas para identificar todos los que falten.
"""
faltantes = [n for n in range(0, 11) if n not in lista]

# Pero la comprensión de listas no nos va a permitir utilizar append, así que agregamos los faltantes con un For.
for numero in faltantes:
    lista.append(numero)
