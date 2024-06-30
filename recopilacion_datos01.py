import pandas as pd

# Simulación de datos de rendimiento recopilados
data = {
    'uso_cpu': [20, 30, 50, 40, 60, 70, 80, 55, 35, 45],
    'uso_memoria': [200, 250, 300, 280, 350, 400, 450, 320, 210, 260],
    'tiempo_respuesta': [120, 150, 200, 170, 230, 260, 300, 220, 130, 160],
    'tiempo_carga': [2.5, 3.1, 4.0, 3.5, 4.5, 5.0, 6.0, 4.2, 2.8, 3.3]
}

df = pd.DataFrame(data)
df.to_csv('datos_rendimiento.csv', index=False)
print("Datos de rendimiento guardados en 'datos_rendimiento.csv'")
