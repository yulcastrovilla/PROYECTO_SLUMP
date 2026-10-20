# Paso 1: cargar el dataset y mirar su estructura
from datos import cargar

df = cargar(limpio=False)

print(df.head())          # primeras 5 filas
df.info()                 # columnas, tipos y valores no nulos
print(df.shape)           # (filas, columnas)
print(df.describe().T)    # resumen estadístico por columna
