import pandas as pd
import joblib

# Cargar el modelo entrenado
model = joblib.load('modelo_regresion_lineal.pkl')

# Nuevos datos para predicción
nuevos_datos = {
    'uso_cpu': [50, 60, 40],
    'uso_memoria': [300, 350, 280],
    'tiempo_respuesta': [200, 230, 170]
}

df_nuevos_datos = pd.DataFrame(nuevos_datos)

# Predicciones con nuevos datos
nuevas_predicciones = model.predict(df_nuevos_datos)
print(nuevas_predicciones)
