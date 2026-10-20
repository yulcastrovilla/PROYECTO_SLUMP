# Paso 8: regresión lineal múltiple para predecir la resistencia a 28 días
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from datos import cargar, OBJETIVO, COMPONENTES

df = cargar()
X = df[COMPONENTES]
y = df[OBJETIVO]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

print(f"R² en entrenamiento: {modelo.score(X_train, y_train):.4f}")
print(f"R² en prueba: {modelo.score(X_test, y_test):.4f}")
print(f"Error medio absoluto (prueba): {mean_absolute_error(y_test, modelo.predict(X_test)):.2f} MPa")

print("\nCoeficientes (MPa por kg/m³):")
print(pd.Series(modelo.coef_, index=COMPONENTES).sort_values().round(4))

# Predicción para una mezcla nueva
mezcla = pd.DataFrame([{
    "Cemento": 250, "Escoria": 80, "Ceniza volante": 150, "Agua": 190,
    "Superplastificante": 9, "Agregado grueso": 880, "Agregado fino": 740,
}])
print(f"\nResistencia predicha para la mezcla nueva: {modelo.predict(mezcla)[0]:.2f} MPa")
