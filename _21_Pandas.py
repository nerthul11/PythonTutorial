"""
La librería Pandas permite leer, modificar y procesar datos de un modo simple y eficiente.

Primero se instala la misma en la terminal: pip install pandas
"""
import pandas as pd  # El as pd permite asignarle otro nombre a la librería en este archivo.

# Pandas utiliza un tipo de valores llamado DataFrame para construir tablas de datos.
data = {"comprador": ['Leandro', 'Eliana', 'Gabriel', 'Leandro', 'Leandro'],
        "producto": ['Manzana', 'Naranja', 'Pera', 'Kiwi', 'Naranja'],
        "precio": [10, 8, 15, 25, 8]}

df = pd.DataFrame(data)
print(df)

# Esto ya permite visualizar una tabla completa. Ahora veamos algunos ejemplos de cómo aplicar filtros.
leandro = df.loc[df['comprador'] == "Leandro"]
precios = df.loc[df['precio'] >= 10]

rosittos = ['Leandro', 'Gabriel']
parte_de_una_lista = df.loc[df['comprador'].isin(rosittos)]
no_en_una_lista = df.loc[~df['comprador'].isin(rosittos)]

# También se pueden alterar campos, por ejemplo, aumentar el precio de todos los artículos un 25%:
df["precio"] *= 1 + (25 / 100)

# O alterar únicamente cuando se cumple una condición
df.loc[df["producto"] == "Naranja", "precio"] += 1

# Ordenar los datos
df = df.sort_values(by=["comprador", "precio"])

# O incluso agruparlos por distintos criterios. Algunos de ellos:
size = df.groupby("comprador").size()  # Devuelve cuántas compras hizo cada uno
suma = df.groupby("comprador").sum()  # Suma el valor de todos los gastos de cada usuario

# Y por supuesto, también se puede guardar en archivos tipo CSV o Excel.
df.to_csv("_20bis_DataFrame.csv")
