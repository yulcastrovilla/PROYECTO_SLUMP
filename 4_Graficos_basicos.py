python 4_Graficos_basicos.py# Paso 4: histogramas con media, mediana y moda
import plotly.express as px
from datos import cargar, OBJETIVO, ASENTAMIENTO

df = cargar()


def histograma(columna, titulo, color):
    media = df[columna].mean()
    mediana = df[columna].median()
    moda = df[columna].mode().iloc[0]

    fig = px.histogram(df, x=columna, nbins=15, title=titulo,
                       color_discrete_sequence=[color])
    fig.add_vline(x=media, line_dash="dash", line_color="red",
                  annotation_text=f"Media: {media:.2f}", annotation_position="top right")
    fig.add_vline(x=mediana, line_dash="dot", line_color="black",
                  annotation_text=f"Mediana: {mediana:.2f}", annotation_position="top")
    fig.add_vline(x=moda, line_dash="dashdot", line_color="green",
                  annotation_text=f"Moda: {moda:.2f}", annotation_position="top left")
    fig.add_annotation(text=f"Desv. estándar: {df[columna].std():.2f}",
                       xref="paper", yref="paper", x=1, y=1.12, showarrow=False)
    fig.update_layout(yaxis_title="Cantidad de mezclas")
    return fig


histograma(OBJETIVO, "Distribución de la resistencia a compresión (28 días)", "#2a9d8f").show()
histograma(ASENTAMIENTO, "Distribución del asentamiento (slump)", "#e76f51").show()
