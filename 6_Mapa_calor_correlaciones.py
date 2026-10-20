# Paso 6: mapa de calor de correlaciones
import plotly.express as px
from datos import cargar

df = cargar()
corr = df.corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    aspect="auto",
    title="Correlación entre componentes y propiedades del concreto",
    labels={"color": "Correlación"},
)
fig.show()
