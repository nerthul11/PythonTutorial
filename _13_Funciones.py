"""
Aquí veremos cómo definir, estructurar y llamar una función.

En general, conviene ubicar las funciones en las primeras líneas del código, porque para poder utilizarlas
primero deben estar definidas.

Primero, vamos a definir una función que no tome parámetros:
"""
def hola_mundo():
    print("Hola, mundo")


# Luego, creamos una función que tome un parámetro y haga algo a partir de ello
def es_par(numero):
    return numero % 2 == 0


# Luego llamaremos ambas funciones, un hola_mundo suelto y es_par lo probaremos con dos números
if __name__ == "__main__":  # Esta línea la explicaremos mejor en el próximo archivo
    hola_mundo()

    numero_par = es_par(4)
    numero_impar = es_par(3)
    print(numero_par)
    print(numero_impar)
