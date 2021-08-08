"""
Ahora, el paso siguiente es comenzar a comprender las operaciones posibles
a las que se puede someter una variable.
"""
var_str = "texto"
var_int = 10

# Suma
var_int += 1  # Esto es igual que decir: "var_int = var_int + 1"
var_str += "1"  # En cadenas de texto, se puede concatenar otro texto. El resultado aquí sería "texto1"

# Resta
var_int -= 1

# Multiplicación
var_int *= 2
var_str *= 2  # Se crean repeticiones del valor de la variable. En este caso, "texto1" * 2 = "texto1texto1"

# División
numero = 10
exacto = numero / 3  # Esto convierte a la variable en tipo Float, incluso si el número es exacto.
redondeado = numero // 3  # Al resultado se le corta la parte decimal (3 en lugar de 3.3333)
modulo = numero % 3

# Potencia
numero **= 2

"""
Hay más operaciones posibles, como la raíz de un número, o logaritmos, etc.

Estos están incluidos en una librería llamada "math". Las librerías son un concepto que se abordará pronto.
"""
