"""Carga y nombres de columnas compartidos por todos los scripts."""
from pathlib import Path
import pandas as pd

RUTA = Path(__file__).resolve().parent / "slump_test.csv"

RENOMBRAR = {
    "Cement": "Cemento",
    "Slag": "Escoria",
    "Fly ash": "Ceniza volante",
    "Water": "Agua",
    "SP": "Superplastificante",
    "Coarse Aggr.": "Agregado grueso",
    "Fine Aggr.": "Agregado fino",
    "SLUMP(cm)": "Asentamiento (cm)",
    "FLOW(cm)": "Flujo (cm)",
    "Compressive Strength (28-day)(Mpa)": "Resistencia 28d (MPa)",
}

OBJETIVO = "Resistencia 28d (MPa)"
ASENTAMIENTO = "Asentamiento (cm)"
FLUJO = "Flujo (cm)"
COMPONENTES = [
    "Cemento", "Escoria", "Ceniza volante", "Agua",
    "Superplastificante", "Agregado grueso", "Agregado fino",
]


def cargar(limpio=True):
    """Devuelve el dataset con nombres en español.
    limpio=True elimina las filas completamente duplicadas."""
    df = pd.read_csv(RUTA)
    df.columns = df.columns.str.strip()
    df = df.drop(columns="No").rename(columns=RENOMBRAR)
    if limpio:
        df = df.drop_duplicates()
    return df
