# Paso 5: dispersión 3D interactiva (se puede girar y acercar)
import plotly.express as px
from datos import cargar, OBJETIVO, ASENTAMIENTO

df = cargar()

fig = px.scatter_3d(
    df,
    x="Agua",
    y="Cemento",
    z=OBJETIVO,
    color=ASENTAMIENTO,
    color_continuous_scale="Viridis",
    opacity=0.85,
    hover_data=["Ceniza volante", "Escoria", "Superplastificante"],
    title="Agua, cemento y resistencia (color = asentamiento)",
)
fig.update_traces(marker={"size": 5})
fig.update_layout(
    scene={
        "xaxis_title": "Agua (kg/m³)",
        "yaxis_title": "Cemento (kg/m³)",
        "zaxis_title": "Resistencia (MPa)",
        "camera": {"eye": {"x": 1.6, "y": 1.6, "z": 1.2}},
    },
    coloraxis_colorbar={"title": "Asentamiento (cm)"},
)
fig.show()
