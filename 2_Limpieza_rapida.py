# Paso 2: revisión de nulos y duplicados
from datos import cargar

df = cargar(limpio=False)

print("Valores nulos por columna:")
print(df.isnull().sum())

duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {duplicados}")

df = df.drop_duplicates()
print(f"Dimensiones después de limpiar: {df.shape}")

# En esta mezcla de concreto un 0 es un dato válido (sin escoria, sin ceniza o asentamiento nulo),
# por eso no se eliminan ceros.
print("Ceros por columna (son válidos en este dataset):")
print((df == 0).sum())
