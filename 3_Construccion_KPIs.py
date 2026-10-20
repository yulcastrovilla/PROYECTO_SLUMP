# Paso 3: indicadores clave (KPIs)
from datos import cargar, OBJETIVO, ASENTAMIENTO, FLUJO, COMPONENTES

df = cargar()

material_cementante = df["Cemento"] + df["Escoria"] + df["Ceniza volante"]
relacion_agua_cementante = (df["Agua"] / material_cementante).mean()

print(f"Resistencia promedio a 28 días: {df[OBJETIVO].mean():.2f} MPa")
print(f"Resistencia máxima: {df[OBJETIVO].max():.2f} MPa")
print(f"Resistencia mínima: {df[OBJETIVO].min():.2f} MPa")
print(f"Asentamiento promedio: {df[ASENTAMIENTO].mean():.2f} cm")
print(f"Flujo promedio: {df[FLUJO].mean():.2f} cm")
print(f"Relación agua/material cementante promedio: {relacion_agua_cementante:.3f}")
print(f"Número de mezclas analizadas: {df.shape[0]}")
