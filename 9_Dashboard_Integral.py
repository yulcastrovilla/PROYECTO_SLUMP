# Paso 9: dashboard con Streamlit  ->  streamlit run 9_Dashboard_Integral.py
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from datos import cargar, OBJETIVO, ASENTAMIENTO, FLUJO, COMPONENTES

st.set_page_config(page_title="Dashboard de mezclas de concreto", layout="wide")


@st.cache_data
def datos():
    return cargar()


df = datos()
st.title("Análisis de mezclas de concreto (Slump Test)")

tab_res, tab_dist, tab_mezcla, tab_corr, tab_modelo = st.tabs(
    ["Resumen", "Distribución", "Mezcla y resistencia", "Correlaciones", "Modelo predictivo"]
)

with tab_res:
    st.subheader("Indicadores clave")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Resistencia promedio", f"{df[OBJETIVO].mean():.2f} MPa")
    c2.metric("Resistencia máxima", f"{df[OBJETIVO].max():.2f} MPa")
    c3.metric("Resistencia mínima", f"{df[OBJETIVO].min():.2f} MPa")
    c4.metric("Asentamiento promedio", f"{df[ASENTAMIENTO].mean():.2f} cm")
    c5.metric("Mezclas analizadas", f"{len(df)}")
    st.subheader("Vista previa")
    st.dataframe(df.head(10), width="stretch")

with tab_dist:
    variable = st.selectbox("Variable", [OBJETIVO, ASENTAMIENTO, FLUJO])
    fig = px.histogram(df, x=variable, nbins=15, title=f"Distribución: {variable}")
    fig.add_vline(x=df[variable].mean(), line_dash="dash", line_color="red",
                  annotation_text=f"Media: {df[variable].mean():.2f}")
    st.plotly_chart(fig, width="stretch")
    st.caption(f"Mediana: {df[variable].median():.2f} · Desv. estándar: {df[variable].std():.2f}")

with tab_mezcla:
    x = st.selectbox("Componente (eje X)", COMPONENTES, index=3)
    fig = px.scatter(df, x=x, y=OBJETIVO, color=ASENTAMIENTO, trendline="ols",
                     color_continuous_scale="Viridis",
                     title=f"{x} vs resistencia a 28 días")
    st.plotly_chart(fig, width="stretch")

with tab_corr:
    corr = df.corr(numeric_only=True)
    fig = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r",
                    zmin=-1, zmax=1, aspect="auto")
    st.plotly_chart(fig, width="stretch")
    st.caption("La correlación mide asociación lineal; no demuestra causalidad.")

with tab_modelo:
    X_train, X_test, y_train, y_test = train_test_split(
        df[COMPONENTES], df[OBJETIVO], test_size=0.25, random_state=42)
    modelo = LinearRegression().fit(X_train, y_train)
    st.write(f"R² en prueba: **{modelo.score(X_test, y_test):.3f}**")

    st.subheader("Predecir la resistencia de una mezcla")
    valores = {}
    columnas = st.columns(4)
    for i, comp in enumerate(COMPONENTES):
        valores[comp] = columnas[i % 4].number_input(
            f"{comp} (kg/m³)", float(df[comp].min()), float(df[comp].max()),
            float(df[comp].median()))
    pred = modelo.predict(pd.DataFrame([valores]))[0]
    st.success(f"Resistencia predicha a 28 días: {pred:.2f} MPa")
