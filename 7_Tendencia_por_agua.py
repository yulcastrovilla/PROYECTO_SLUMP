# Paso 7: este dataset NO tiene columna de edad (todas las resistencias son a 28 días),
# así que en lugar de la serie por edad se analiza la tendencia según el contenido de agua.
import pandas as pd
import plotly.express as px
from datos import cargar, OBJETIVO, ASENTAMIENTO, FLUJO

df = cargar()

limites = [159, 175, 190, 205, 220, 240]
df["Rango de agua (kg/m³)"] = pd.cut(df["Agua"], bins=limites).astype(str)

tendencia = (
    df.groupby("Rango de agua (kg/m³)", observed=True)[[OBJETIVO, ASENTAMIENTO, FLUJO]]
    .mean()
    .reset_index()
)
# ordenar por el límite inferior del rango
tendencia["orden"] = tendencia["Rango de agua (kg/m³)"].str.extract(r"\((\d+)").astype(int)
tendencia = tendencia.sort_values("orden").drop(columns="orden")
print(tendencia.round(2))

largo = tendencia.melt(id_vars="Rango de agua (kg/m³)", var_name="Propiedad", value_name="Promedio")
fig = px.line(
    largo, x="Rango de agua (kg/m³)", y="Promedio", facet_row="Propiedad",
    markers=True, title="Propiedades promedio según el contenido de agua",
)
fig.update_yaxes(matches=None)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.show()
