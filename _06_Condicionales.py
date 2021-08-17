"""
Muy lindo los not and or True False, pero... ¿Para qué quiero saber eso?

En este archivo se verá un uso muy útil de las variables booleanas: los condicionales.

Un condicional verifica si se cumple o no una condición y ejecuta un código si se cumple,
y, opcionalmente, un código si no se cumple.
"""

n = int(input("Escribe un número entero: "))

if n >= 10:
    print(f"{n} es mayor o igual a 10.")
elif n >= 5:
    print(f"{n} es mayor o igual a 5 pero menor a 10.")
else:
    print(f"{n} es menor a 5.")
print("Esto ya no forma parte del if.")

# También se pueden anidar condicionales, es decir: un if adentro de otro if
if n >= 100:
    if n % 2 == 0:
        print(f"{n} es par y mayor o igual a 100.")
    else:
        print(f"{n} es impar y mayor a 100.")
else:
    print(f"{n} es menor a 100.")
