# Proyecto integral – Concrete Slump Test

Análisis de 103 mezclas de concreto (UCI Machine Learning Repository, I-Cheng Yeh):
7 componentes de la mezcla y 3 resultados (asentamiento, flujo y resistencia a 28 días).

## Cómo ejecutarlo en VS Code
1. Abre la carpeta `PROYECTO_SLUMP` (File → Open Folder).
2. En la terminal: `pip install -r requirements.txt`
3. Ejecuta cada paso: `python 1_Cargar_Dataset.py`, `python 2_Limpieza_rapida.py`, ... hasta el 8.
4. Dashboard Streamlit: `streamlit run 9_Dashboard_Integral.py`
5. Dashboard web: abrir `9_Dashboard_propia_web.html` en el navegador y cargar `slump_test.csv`.

## Archivos
- `datos.py`: carga el CSV y define los nombres de columnas (si cambias de dataset, cambia solo este archivo).
- `1_` a `8_`: un script por paso (cargar, limpiar, KPIs, gráficos, 3D, correlaciones, tendencia, modelo).
- `9_`: dashboards.

## Nota sobre el paso 7
El dataset no tiene columna de edad (todas las resistencias son a 28 días), por eso la serie temporal
se reemplazó por la tendencia según el contenido de agua.
