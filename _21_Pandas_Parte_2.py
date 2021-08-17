"""
A continuación, tomando el ejemplo de API realizado, utilizaremos pandas para crear un CSV con la información
de nuestra Pokédex. Armaremos 5 archivos de ejemplo.
"""
import pandas as pd

# Primero, simplemente leeremos el JSON y lo pasaremos a CSV utilizando Pandas.
pokedex = pd.read_json('_18bis_Pokedex.json')
pokedex.to_csv('_21_Pokedex_0.csv')

# Al abrir el CSV, se ve que no queda muy lindo: Filas y Columnas están invertidas. Vamos a corregir eso.
pokedex = pokedex.transpose()
pokedex.to_csv('_21_Pokedex_1.csv')

# Ahora vemos que figuran con dos ID, lo cual no es necesario. Mostrar índice y columnas o no depende de parámetros.
pokedex.to_csv('_21_Pokedex_2.csv', index=False)

# Sumado a eso, vemos unos cuantos valores que son listas vacías y podemos remover.
pokedex = pokedex.mask(pokedex.applymap(str) == '[]')
pokedex.to_csv('_21_Pokedex_3.csv', index=False)

# Y por último, algo que no vimos, por ejemplo, es cómo eliminar una columna.
pokedex = pokedex.drop(columns=['evolutions'])
pokedex.to_csv('_21_Pokedex_4.csv', index=False)
