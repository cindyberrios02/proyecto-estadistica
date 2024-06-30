import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

# Cargar datos
data = pd.read_csv('datos_rendimiento.csv')

# Selección de características y variable objetivo
X = data[['uso_cpu', 'uso_memoria', 'tiempo_respuesta']]
y = data['tiempo_carga']

# División de los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse}, R²: {r2}')

# Visualización de resultados
plt.scatter(y_test, y_pred)
plt.xlabel('Valores Reales')
plt.ylabel('Predicciones')
plt.title('Valores Reales vs Predicciones')
plt.savefig('valores_reales_vs_predicciones.png')
print("Gráfico guardado como 'valores_reales_vs_predicciones.png'")

# Guardar el modelo entrenado
joblib.dump(model, 'modelo_regresion_lineal.pkl')
print("Modelo guardado como 'modelo_regresion_lineal.pkl'")
